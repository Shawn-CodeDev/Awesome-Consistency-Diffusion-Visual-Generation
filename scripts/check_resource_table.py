#!/usr/bin/env python3
import csv
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
csv_path = ROOT / "resources" / "benchmark_coverage.csv"

valid_coverage = {"H", "M", "L"}
coverage_cols = ["P/C", "S/E", "ID", "V/T", "N/S", "P/W"]
required_cols = [
    "Section", "Resource", "BibTeXKey", "CodeURL", "Type", "Modality",
    "Primary", *coverage_cols, "DiagnosticUseAndBlindSpot"
]

with csv_path.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

errors = []
if not rows:
    errors.append("benchmark_coverage.csv contains no resource rows.")

missing = [c for c in required_cols if c not in (rows[0].keys() if rows else [])]
if missing:
    errors.append(f"Missing columns: {missing}")

seen = set()
for i, row in enumerate(rows, start=2):
    key = row.get("BibTeXKey", "").strip()
    if not key:
        errors.append(f"Line {i}: missing BibTeXKey")
    if key in seen:
        errors.append(f"Line {i}: duplicate BibTeXKey {key}")
    seen.add(key)

    for col in coverage_cols:
        if row.get(col, "").strip() not in valid_coverage:
            errors.append(f"Line {i}: invalid coverage value for {col}: {row.get(col)!r}")

    url = row.get("CodeURL", "").strip()
    if url:
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            errors.append(f"Line {i}: invalid CodeURL: {url}")

if errors:
    raise SystemExit("\n".join(errors))

print(f"OK: {len(rows)} resource rows validated.")
