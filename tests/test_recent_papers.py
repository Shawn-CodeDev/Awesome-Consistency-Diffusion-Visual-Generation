"""Offline catalog and rendering tests; no third-party test runner is needed."""
from __future__ import annotations
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from catalog_tools import (
    DEFAULT_FIGURES, RECENT_BEGIN, RECENT_END, apply_corrections, collection_count,
    detect_existing, discover_presentation, extract_collection, generated_files,
    load_records, relocate_to_docs, render_recent, validate_records, update_existing_readme,
)


class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = load_records(ROOT)
        cls.corrections = json.loads((ROOT / 'resources/link_corrections.json').read_text(encoding='utf-8'))

    def test_integrity(self):
        self.assertEqual([], validate_records(self.records))

    def test_generated_files_are_current(self):
        for path, expected in generated_files(self.records).items():
            with self.subTest(path=path):
                self.assertEqual(expected, (ROOT / path).read_text(encoding='utf-8'))

    def test_readme_block_is_current(self):
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertEqual(1, readme.count(RECENT_BEGIN))
        self.assertEqual(1, readme.count(RECENT_END))
        block = readme.split(RECENT_BEGIN)[1].split(RECENT_END)[0]
        self.assertEqual('\n' + render_recent(self.records), block)

    def test_duplicates_are_rejected(self):
        invalid = copy.deepcopy(self.records)
        invalid.append(copy.deepcopy(invalid[0]))
        messages = validate_records(invalid)
        self.assertTrue(any('duplicate identifier' in e for e in messages))
        self.assertTrue(any('duplicate normalized title' in e for e in messages))

    def test_future_dates_are_rejected(self):
        invalid = copy.deepcopy(self.records)
        invalid[0]['first_submitted'] = '2030-01-01'
        self.assertTrue(any('exceeds' in e for e in validate_records(invalid)))

    def test_paper_identifier_mismatch_is_rejected(self):
        invalid = copy.deepcopy(self.records)
        invalid[0]['paper_url'] = 'https://arxiv.org/abs/0000.00000'
        self.assertTrue(any('mismatch' in e for e in validate_records(invalid)))

    def test_invalid_relations_are_rejected(self):
        invalid = copy.deepcopy(self.records)
        invalid[0]['secondary_relations'] = [invalid[0]['primary_relation']]
        self.assertTrue(any('redundant' in e for e in validate_records(invalid)))

    def test_figures_and_visitor_key_are_preserved(self):
        text = '''<img src="paper/Cons_v2.png"><img src="paper/Eval_01.png">\n[![opt](paper/Optimize_latest.png)](paper/Optimize.pdf)\n<img src="https://visitor-badge.laobi.icu/badge?page_id=my.original.key&amp;left_color=gray">'''
        figures, visitor = discover_presentation(text)
        self.assertEqual('paper/Cons_v2.png', figures['Cons'])
        self.assertEqual('paper/Eval_01.png', figures['Eval'])
        self.assertEqual('paper/Optimize_latest.png', figures['Optimize'])
        self.assertIn('page_id=my.original.key&left_color=gray', visitor)

    def test_scoped_link_corrections_do_not_corrupt_other_entries(self):
        old = '''## External consistency
- [FreeDoM](https://github.com/vvictoryuki/FreeDoM) [Paper](https://arxiv.org/abs/2303.16747)
- [HumanSD](https://github.com/IDEA-Research/HumanSD) [Paper](https://arxiv.org/abs/2303.16747)
- [Composer](https://github.com/damo-vilab/composer) [Paper](https://arxiv.org/abs/2302.09778)
- [FastComposer](https://github.com/mit-han-lab/fastcomposer) [Paper](https://arxiv.org/abs/2302.09778)
'''
        fixed, _ = apply_corrections(old, self.corrections)
        self.assertEqual(collection_count(old), collection_count(fixed))
        lines = fixed.splitlines()
        self.assertIn('2303.09833', lines[1])
        self.assertIn('2304.04269', lines[2])
        self.assertIn('2302.09778', lines[3])
        self.assertIn('2305.10431', lines[4])
        fixed_twice, report = apply_corrections(fixed, self.corrections)
        self.assertEqual(fixed, fixed_twice)
        self.assertEqual(0, sum(c['replaced_links'] for c in report))

    def test_collection_extraction_handles_thematic_headings(self):
        text = '''# Consistency in Diffusion-Based Visual Generation\n## Overview\nText\n## 01 · External consistency\n### Editing\n- [Example](https://example.com)\n## 02 · Internal consistency\n- [Example2](https://example.com/2)\n## Citation\nKeep separately\n'''
        result = extract_collection(text)
        self.assertTrue(result.startswith('## 01 · External'))
        self.assertEqual(2, collection_count(result))
        self.assertNotIn('## Citation', result)

    def test_collection_extraction_fails_closed(self):
        with self.assertRaises(ValueError):
            extract_collection('# unrelated\ntext')

    def test_relative_links_relocate_without_changing_external_urls(self):
        text = '[Local](resources/data.csv) [Anchor](#test) [Remote](https://example.com/a) <img src="paper/Fig.png">'
        result = relocate_to_docs(text)
        self.assertIn('(../resources/data.csv)', result)
        self.assertIn('(#test)', result)
        self.assertIn('(https://example.com/a)', result)
        self.assertIn('src="../paper/Fig.png"', result)

    def test_existing_arxiv_ids_and_aliases_are_detected(self):
        first = self.records[0]
        self.assertIn(first['id'], detect_existing(self.records, f"- [Test]({first['paper_url']})"))
        self.assertIn(first['id'], detect_existing(self.records, f"- [{first['name'].split(' / ')[0]}](https://example.com)"))

    def test_all_titles_are_in_evidence_register(self):
        text = (ROOT / 'docs/recent-papers.md').read_text(encoding='utf-8')
        for record in self.records:
            self.assertIn(record['title'], text)

    def test_bold_legacy_entries_count(self):
        self.assertEqual(2, collection_count('- **[One](https://a.org)**\n  detail\n- [Two](https://b.org)\n'))

    def test_multiline_scoped_correction(self):
        old = '- **[FreeDoM](https://github.com/vvictoryuki/FreeDoM)** <sub>2023</sub>  \n  Description [Paper](https://arxiv.org/abs/2303.16747)\n- **[HumanSD](https://github.com/IDEA-Research/HumanSD)** <sub>2023</sub>  \n  Description [Paper](https://arxiv.org/abs/2303.16747)\n'
        fixed, report = apply_corrections(old, self.corrections)
        self.assertIn('2303.09833', fixed.splitlines()[1])
        self.assertIn('2304.04269', fixed.splitlines()[3])
        self.assertEqual(2, sum(r['replaced_links'] for r in report))
        self.assertEqual(2, collection_count(fixed))

    def live_fixture(self):
        return '<div align="center">\n# Consistency in Diffusion-Based Visual Generation: A Survey\n<a href="#resource-collection">Resources</a>\n<img src="https://visitor-badge.laobi.icu/badge?page_id=keep.key">\n</div>\n## Overview\nKeep overview.\n<img src="paper/Cons_01.png"><img src="paper/Eval_01.png"><img src="paper/Optimize_01.png">\n## Resource collection\nKeep navigation.\n<a id="external-consistency"></a>\n## 01 · External consistency\n- **[An existing item](https://example.org)** <sub>2025</sub>  \n  Keep this description.\n## Citation\nKeep citation.\n'

    def test_live_readme_preserved_with_inserted_register(self):
        before = self.live_fixture()
        after, _ = update_existing_readme(before, self.records, self.corrections)
        self.assertIn('Keep overview.', after)
        self.assertIn(before[before.index('## Resource collection'):], after)
        self.assertEqual(discover_presentation(before), discover_presentation(after))
        self.assertEqual(1, collection_count(extract_collection(after)))
        self.assertEqual(1, after.count(RECENT_BEGIN))
        self.assertEqual(1, after.count(RECENT_END))

    def test_live_update_refuses_repeat(self):
        after, _ = update_existing_readme(self.live_fixture(), self.records, self.corrections)
        with self.assertRaises(ValueError):
            update_existing_readme(after, self.records, self.corrections)

    def test_bold_alias_deduplication(self):
        first = self.records[0]
        self.assertIn(first['id'], detect_existing(self.records, f"- **[{first['name']}](https://example.org)**"))


if __name__ == '__main__':
    unittest.main()
