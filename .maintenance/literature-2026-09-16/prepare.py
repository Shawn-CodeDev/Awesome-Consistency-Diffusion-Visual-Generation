"""One-time, fail-closed integration of the reviewed register into this checkout."""
from pathlib import Path
import hashlib
import json
import os
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from catalog_tools import (CUTOFF, collection_count, detect_existing, discover_presentation,
    extract_collection, generated_files, update_existing_readme, validate_records)

EXPECTED_README_BLOB = '4048642f8ff1e35a0c05f5e65b809c67495cfa2b'
BASE_COMMIT = 'c294df451fb73db11bc118eedfa8cc59a4fa179c'


def blob_sha(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def main():
    seeds = [json.loads(p.read_text(encoding='utf-8')) for p in sorted(Path(__file__).parent.glob('records-*.json'))]
    if len(seeds) != 3 or len({tuple(s['fields']) for s in seeds}) != 1:
        raise ValueError('Expected three compatible seed files')
    seed = {'fields': seeds[0]['fields'], 'records': [r for s in seeds for r in s['records']]}
    records = []
    for row in seed['records']:
        if len(row) != len(seed['fields']):
            raise ValueError('Invalid seed row width')
        r = dict(zip(seed['fields'], row))
        r['paper_url'] = r['source_url'] = f"https://arxiv.org/abs/{r['id']}"
        r['verification_level'] = 'primary-abstract-metadata'
        r['checked_on'] = CUTOFF
        r['publication_status'] = 'arXiv record; proceedings status not audited'
        r['scope_basis'] = 'Editorial classification under the survey taxonomy'
        records.append(r)
    errors = validate_records(records)
    if errors:
        raise ValueError('\n'.join(errors))
    original = (ROOT / 'README.md').read_bytes()
    if blob_sha(original) != EXPECTED_README_BLOB:
        raise ValueError('README changed from the reviewed snapshot; refusing to overwrite it.')
    text = original.decode('utf-8')
    figures, visitor = discover_presentation(text)
    for p in figures.values():
        if '://' in p or not (ROOT / p).is_file():
            raise ValueError(f'Unreviewed or missing figure: {p}')
    corrections = json.loads((ROOT / 'resources/link_corrections.json').read_text())
    readme, corrected = update_existing_readme(text, records, corrections)
    collection = extract_collection(text)
    overlap = detect_existing(records, collection)
    report = {
        'snapshot': CUTOFF,
        'status': 'generated-from-reviewed-repository-snapshot',
        'base_commit': BASE_COMMIT,
        'base_readme_blob': EXPECTED_README_BLOB,
        'base_readme_sha256': hashlib.sha256(original).hexdigest(),
        'legacy_list_entries_preserved_inline': collection_count(collection),
        'distinct_recent_papers': len(records),
        'recognized_existing_recent_ids': overlap,
        'not_recognized_in_base_collection': len(records) - len(overlap),
        'deduplication_scope': 'canonical arXiv identifiers and normalized leading entry names; not a semantic audit',
        'figure_paths_preserved': figures,
        'visitor_badge_source': visitor,
        'targeted_corrections': corrected,
        'archive': f'docs/archive/README.before-{CUTOFF}.md',
        'verification_scope': 'primary abstract/metadata register; no full-text or experimental replication claim',
    }
    outputs = {report['archive']: original,
        'resources/recent_papers.json': (json.dumps(records, ensure_ascii=False, indent=2) + '\n').encode(),
        **{k: v.encode() for k, v in generated_files(records).items()},
        'docs/literature-update-report.json': (json.dumps(report, indent=2) + '\n').encode(),
        'README.md': readme.encode()}
    for relative in outputs:
        path = ROOT / relative
        for part in [path, *path.parents]:
            if part == ROOT:
                break
            if part.is_symlink():
                raise ValueError(f'Symlink destination: {relative}')
        if relative != 'README.md' and path.exists():
            raise ValueError(f'Output already exists: {relative}')
    written = []
    try:
        for relative, data in outputs.items():
            path = ROOT / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            fd, tmp = tempfile.mkstemp(dir=path.parent, prefix='.' + path.name)
            try:
                with os.fdopen(fd, 'wb') as f:
                    f.write(data)
                os.chmod(tmp, 0o644)
                os.replace(tmp, path)
                written.append(relative)
            finally:
                if os.path.exists(tmp):
                    os.unlink(tmp)
    except Exception:
        for relative in reversed(written):
            path = ROOT / relative
            if relative == 'README.md':
                path.write_bytes(original)
            else:
                path.unlink()
        raise
    print(json.dumps(report, indent=2))
    print('Wrote:', ', '.join(outputs))


if __name__ == '__main__':
    main()
