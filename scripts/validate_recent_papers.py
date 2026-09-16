#!/usr/bin/env python3
"""Offline integrity validation, not a network or scientific-claim checker."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from catalog_tools import RECENT_BEGIN, RECENT_END, generated_files, load_records, render_recent, validate_records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        records = load_records(root)
        errors = validate_records(records)
    except (OSError, json.JSONDecodeError, TypeError) as exc:
        raise SystemExit(f'Cannot load catalog: {exc}')
    if errors:
        raise SystemExit('\n'.join(errors))
    for relative, expected in generated_files(records).items():
        path = root / relative
        if not path.is_file() or path.read_text(encoding='utf-8') != expected:
            errors.append(f'Generated file missing or stale: {relative}')
    readme_path = root / 'README.md'
    if readme_path.is_file():
        readme = readme_path.read_text(encoding='utf-8')
        if readme.count(RECENT_BEGIN) != 1 or readme.count(RECENT_END) != 1:
            errors.append('README has no unique generated recent-paper block')
        else:
            actual = readme.split(RECENT_BEGIN, 1)[1].split(RECENT_END, 1)[0]
            if actual != '\n' + render_recent(records):
                errors.append('README recent-paper block is stale')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'OK: {len(records)} distinct papers; schema, dates, identifiers and all generated exports agree.')
    print('Scope: offline integrity only. Remote links, venues and empirical claims were not re-tested.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
