"""Regression checks for the immutable pre-integration source archives."""
import csv
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def blob_sha(path):
    data = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


class PreservedMaterialTests(unittest.TestCase):
    def test_source_archives_are_exact(self):
        expected = {
            'docs/archive/README.before-2026-09-16.md': '4048642f8ff1e35a0c05f5e65b809c67495cfa2b',
            'docs/archive/recent_papers.before-2026-09-16.csv': '3cfd3a03f93bff32104ec3b1571b5130938f80ca',
        }
        for relative, sha in expected.items():
            with self.subTest(path=relative):
                self.assertEqual(sha, blob_sha(ROOT / relative))

    def test_expanded_catalog_retains_prior_csv_metadata(self):
        archive = ROOT / 'docs/archive/recent_papers.before-2026-09-16.csv'
        with archive.open(encoding='utf-8', newline='') as stream:
            earlier = list(csv.DictReader(stream))
        records = json.loads((ROOT / 'resources/recent_papers.json').read_text(encoding='utf-8'))
        by_url = {record['paper_url']: record for record in records}
        self.assertEqual(81, len(earlier))
        for row in earlier:
            with self.subTest(paper=row['paper_url']):
                self.assertIn(row['paper_url'], by_url)
                for field, value in row.items():
                    self.assertEqual(value, by_url[row['paper_url']][field])


if __name__ == '__main__':
    unittest.main()
