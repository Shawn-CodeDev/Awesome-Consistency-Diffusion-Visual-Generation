#!/usr/bin/env python3
"""Regenerate recent-paper exports. No network access is required."""
from __future__ import annotations
import argparse
from pathlib import Path
from catalog_tools import RECENT_BEGIN, RECENT_END, generated_files, load_records, render_recent, validate_records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--update-readme', action='store_true', help='Replace only the marked recent-paper block in README.md')
    args = parser.parse_args()
    root = args.root.resolve()
    records = load_records(root)
    errors = validate_records(records)
    if errors:
        raise SystemExit('\n'.join(errors))
    outputs = generated_files(records)
    if args.update_readme:
        readme = (root / 'README.md').read_text(encoding='utf-8')
        if readme.count(RECENT_BEGIN) != 1 or readme.count(RECENT_END) != 1:
            raise SystemExit('README.md must have exactly one generated-paper block; nothing was written.')
        left, rest = readme.split(RECENT_BEGIN, 1)
        _, right = rest.split(RECENT_END, 1)
        outputs['README.md'] = left + RECENT_BEGIN + '\n' + render_recent(records) + RECENT_END + right
    for relative, text in outputs.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8', newline='\n')
        print(f'Wrote {relative}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
