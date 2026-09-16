"""Standard-library utilities for the 2026-09-16 literature update.

No network requests, repository writes, or tracking requests occur on import.
"""
from __future__ import annotations

import csv
import hashlib
import html
import io
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

CUTOFF = "2026-09-16"
REPOSITORY = "Shawn-CodeDev/Awesome-Consistency-Diffusion-Visual-Generation"
REPO_URL = f"https://github.com/{REPOSITORY}"
UPDATE_MARKER = "<!-- consistency-literature-update: 2026-09-16 -->"
RECENT_BEGIN = "<!-- BEGIN GENERATED RECENT PAPERS -->"
RECENT_END = "<!-- END GENERATED RECENT PAPERS -->"
RELATIONS = ("External", "Internal", "Normative")
THEMES = {
    "External": (
        "Image editing and in-context generation",
        "Compositionality and spatial grounding",
        "Typography and text rendering",
        "Structural and camera control",
        "Temporally consistent video editing",
        "Editing and reasoning evaluation",
    ),
    "Internal": (
        "Subject and identity preservation",
        "Subject and identity evaluation",
        "Multi-view and geometric consistency",
        "Multi-shot narratives and persistent memory",
        "Long-horizon video generation",
    ),
    "Normative": (
        "Preference alignment and reward learning",
        "Safety, erasure and capability retention",
        "Physics-aware generation",
        "Physical and causal evaluation",
    ),
}
DEFAULT_FIGURES = {"Cons": "paper/Cons_01.png", "Eval": "paper/Eval_01.png", "Optimize": "paper/Optimize_01.png"}
DEFAULT_VISITOR = "https://visitor-badge.laobi.icu/badge?page_id=Shawn-CodeDev.Awesome-Consistency-Diffusion-Visual-Generation"
SURVEY_BIB = """@misc{yan2026consistency,
  title        = {Consistency in Diffusion-Based Visual Generation: A Survey},
  author       = {Yan, Song and Zhai, Wei and Wang, Chenfeng and Li, Ruixuan and Yang, Zhangping and Cai, Yancheng and Zhang, Tao and Wang, Ling and Lan, Yunwei and He, Yujie and Cao, Yang and Li, Min and Zha, Zheng-Jun},
  year         = {2026},
  howpublished = {Preprints.org},
  doi          = {10.20944/preprints202606.0870.v1},
  url          = {https://www.preprints.org/manuscript/202606.0870/v1},
  note         = {Version 1; posted 11 June 2026; preprint}
}
"""


def load_records(root: Path) -> list[dict]:
    return json.loads((root / "resources/recent_papers.json").read_text(encoding="utf-8"))


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def validate_records(records: list[dict]) -> list[str]:
    errors = []
    if not isinstance(records, list) or not records:
        return ["Catalog must be a nonempty list."]
    required = {
        "id", "name", "title", "first_submitted", "primary_relation", "theme",
        "resource_type", "modalities", "secondary_relations", "first_author",
        "description", "paper_url", "project_url", "code_url", "source_url",
        "verification_level", "checked_on", "publication_status", "scope_basis",
    }
    seen_ids, seen_titles = set(), set()
    for i, r in enumerate(records, 1):
        tag = f"record {i} ({r.get('id', '?')})" if isinstance(r, dict) else f"record {i}"
        if not isinstance(r, dict):
            errors.append(f"{tag}: expected object")
            continue
        missing = required - r.keys()
        if missing:
            errors.append(f"{tag}: missing {sorted(missing)}")
            continue
        for field in required - {"project_url", "code_url", "secondary_relations"}:
            if not r[field]:
                errors.append(f"{tag}: empty {field}")
        if not re.fullmatch(r"\d{4}\.\d{4,5}", r["id"]):
            errors.append(f"{tag}: invalid arXiv identifier")
        if r["id"] in seen_ids:
            errors.append(f"{tag}: duplicate identifier")
        seen_ids.add(r["id"])
        title_key = re.sub(r"\W+", "", r["title"].casefold())
        if title_key in seen_titles:
            errors.append(f"{tag}: duplicate normalized title")
        seen_titles.add(title_key)
        for field in ("first_submitted", "checked_on"):
            try:
                d = date.fromisoformat(r[field])
                if d > date.fromisoformat(CUTOFF):
                    errors.append(f"{tag}: {field} exceeds the research cutoff")
            except (ValueError, TypeError):
                errors.append(f"{tag}: invalid {field}")
        if r["first_submitted"][:4] not in {"2025", "2026"}:
            errors.append(f"{tag}: outside the declared first-posted year window")
        if r["checked_on"] != CUTOFF:
            errors.append(f"{tag}: inconsistent checked_on")
        if r["primary_relation"] not in RELATIONS:
            errors.append(f"{tag}: invalid primary relation")
        elif r["theme"] not in THEMES[r["primary_relation"]]:
            errors.append(f"{tag}: theme does not belong to primary relation")
        secondary = r["secondary_relations"]
        if not isinstance(secondary, list) or any(v not in RELATIONS for v in secondary):
            errors.append(f"{tag}: invalid secondary relations")
        elif len(set(secondary)) != len(secondary) or r["primary_relation"] in secondary:
            errors.append(f"{tag}: redundant secondary relation")
        if not isinstance(r["modalities"], list) or not r["modalities"]:
            errors.append(f"{tag}: modalities must be a nonempty list")
        expected = f"https://arxiv.org/abs/{r['id']}"
        if r["paper_url"] != expected or r["source_url"] != expected:
            errors.append(f"{tag}: paper/source identifier mismatch")
        for key in ("paper_url", "source_url", "project_url", "code_url"):
            if r[key]:
                parsed = urlparse(r[key])
                if parsed.scheme != "https" or not parsed.netloc or any(c.isspace() for c in r[key]):
                    errors.append(f"{tag}: invalid {key}")
        if r["verification_level"] != "primary-abstract-metadata":
            errors.append(f"{tag}: unsupported verification claim")
    return errors


def ordered(records: list[dict]) -> list[dict]:
    return sorted(records, key=lambda r: (r["first_submitted"], r["id"]), reverse=True)


def md_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def render_recent(records: list[dict], root_prefix: str = "") -> str:
    counts = Counter(r["primary_relation"] for r in records)
    years = Counter(r["first_submitted"][:4] for r in records)
    lines = [
        '<a id="recent-literature"></a>',
        "## Recent literature · 2025–2026", "",
        f"**{len(records)} distinct papers · {years['2026']} first posted in 2026 · {years['2025']} first posted in 2025**  ",
        f"Research snapshot: **{CUTOFF}**. Dates below are first arXiv submission dates, not conference publication dates.", "",
        f"[JSON]({root_prefix}resources/recent_papers.json) · [CSV]({root_prefix}resources/recent_papers.csv) · "
        f"[BibTeX, abbreviated authors]({root_prefix}resources/recent_papers.bib) · "
        f"[Evidence register]({root_prefix}docs/recent-papers.md#evidence-register) · "
        f"[Scope and limitations]({root_prefix}docs/research-notes.md)", "",
        "> **Reading note.** Titles, dates and short summaries were checked against original arXiv records or their indexed abstracts. "
        "Conference status and empirical results were not comprehensively audited. The three-relation assignments are editorial annotations "
        "under this survey's taxonomy. A method and its associated benchmark are counted once when they share one paper.", "",
        "| Primary relation | Papers in this update | Browse |", "|:--|--:|:--|",
    ]
    for rel in RELATIONS:
        lines.append(f"| **{rel}** | {counts[rel]} | [{rel} consistency](#recent-{rel.lower()}) |")
    lines.extend(["", "Within each topic, the most recently posted papers appear first. **Paper titles link to the original arXiv record**; optional code/project links are author-provided discovery links, not a deployment or availability guarantee.", ""])
    for index, rel in enumerate(RELATIONS, 1):
        lines += [f'<a id="recent-{rel.lower()}"></a>', f"### {index:02d} · {rel} consistency", ""]
        for theme in THEMES[rel]:
            subset = ordered([r for r in records if r["primary_relation"] == rel and r["theme"] == theme])
            if not subset:
                continue
            lines += [f"#### {theme}", "", "| First posted | Paper and resources | Consistency focus |", "|:--|:--|:--|"]
            for r in subset:
                meta = f"{r['resource_type']} · {' / '.join(r['modalities'])}"
                if r["secondary_relations"]:
                    meta += " · also " + "/".join(r["secondary_relations"])
                links = []
                if r["code_url"]:
                    links.append(f"[Code]({r['code_url']})")
                if r["project_url"]:
                    links.append(f"[Project]({r['project_url']})")
                cell = f"**[{md_cell(r['name'])}]({r['paper_url']})**<br><sub>{md_cell(meta)}</sub>"
                if links:
                    cell += "<br>" + " · ".join(links)
                lines.append(f"| {r['first_submitted']} | {cell} | {md_cell(r['description'])} |")
            lines += ["", "[Back to recent-literature navigation](#recent-literature)", ""]
    return "\n".join(lines).rstrip() + "\n"


def bib_escape(text: str) -> str:
    return text.replace("&", r"\&").replace("%", r"\%").replace("_", r"\_").replace("#", r"\#")


def render_bib(records: list[dict]) -> str:
    lines = [
        "% Discovery bibliography for the 2026-09-16 update.",
        "% AUTHOR LISTS ARE ABBREVIATED: first author and others, not complete metadata.",
        "% Replace abbreviated authors with the official export before submitting a manuscript.",
        "% arXiv dates are first-submission dates; proceedings status was not audited.", "",
    ]
    for r in ordered(records):
        author = bib_escape(r["first_author"])
        if "," not in author:
            author = "{" + author + "}"
        lines.extend([
            f"@misc{{recent_{r['id'].replace('.', '_')},",
            f"  title        = {{{{{bib_escape(r['title'])}}}}},",
            f"  author       = {{{author} and others}},",
            f"  year         = {{{r['first_submitted'][:4]}}},",
            f"  archivePrefix = {{arXiv}},",
            f"  eprint       = {{{r['id']}}},",
            f"  url          = {{{r['paper_url']}}},",
            f"  note         = {{First submitted {r['first_submitted']}; abbreviated author list; proceedings status not audited}}",
            "}", "",
        ])
    return "\n".join(lines).rstrip() + "\n"


def render_csv(records: list[dict]) -> str:
    fields = list(records[0])
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    for record in ordered(records):
        row = {key: "; ".join(value) if isinstance(value, list) else value for key, value in record.items()}
        writer.writerow(row)
    return buffer.getvalue()


def render_evidence_register(records: list[dict]) -> str:
    lines = ['<a id="evidence-register"></a>', "## Evidence register", "",
             "This register preserves full titles and the exact primary-source identifiers used in this update. "
             "The recorded author is the first author only. Short names in the tables are navigation labels, not replacement bibliographic titles.", ""]
    for r in ordered(records):
        lines += [f"### {r['id']} · {r['name']}", "", f"**{r['title']}**", "",
                  f"First author: {r['first_author']}. First submitted: {r['first_submitted']}. "
                  f"Source: [arXiv:{r['id']}]({r['source_url']}). Checked: {r['checked_on']}.", "",
                  f"Relation: **{r['primary_relation']}**; topic: {r['theme']}. "
                  f"Secondary relations: {', '.join(r['secondary_relations']) or 'none recorded'}.", "",
                  r["description"], ""]
    return "\n".join(lines).rstrip() + "\n"


def generated_files(records: list[dict]) -> dict[str, str]:
    return {
        "docs/recent-papers.md": "# Recent papers and evidence register\n\n[Return to the survey](../README.md)\n\n" + render_recent(records, "../") + "\n---\n\n" + render_evidence_register(records),
        "resources/recent_papers.csv": render_csv(records),
        "resources/recent_papers.bib": render_bib(records),
        "resources/survey_preprint.bib": SURVEY_BIB,
    }


def discover_presentation(readme: str) -> tuple[dict[str, str], str]:
    """Keep manually selected figure assets and the existing visitor-counter key."""
    urls = [html.unescape(u) for u in re.findall(r'(?:src|href)=["\']([^"\']+)["\']', readme)]
    urls += re.findall(r'\]\(([^\s)]+)', readme)
    figures = dict(DEFAULT_FIGURES)
    for stem in figures:
        candidates = [u for u in urls if re.search(rf"(?:^|/){stem}(?:[_\-.][^/?#]*)?\.(?:png|jpg|jpeg|webp|svg)(?:[?#].*)?$", u, re.I)]
        if candidates:
            # Prefer source assets in this repository; an external image URL is retained only if supplied by the README.
            figures[stem] = candidates[0]
    visitors = [u for u in urls if "visitor-badge.laobi.icu/badge?" in u]
    return figures, visitors[0] if visitors else DEFAULT_VISITOR


def extract_collection(readme: str) -> str:
    """Extract literature without assuming the existing heading numbering or case."""
    headings = list(re.finditer(r"^##(?!#)\s+(.+)$", readme, flags=re.M))
    starts = [m for m in headings if re.search(r"\bexternal consistency\b", m.group(1), re.I)]
    if not starts:
        starts = [m for m in headings if re.search(r"\bresource collection\b", m.group(1), re.I)]
    if not starts:
        raise ValueError("Cannot locate the existing literature collection. No files were changed.")
    start = starts[0].start()
    end = len(readme)
    # Stops cover the original and themed README variants; a full unmodified archive is always retained as well.
    for m in headings:
        if m.start() <= start:
            continue
        if re.search(r"machine.readable|coverage labels|contribut|maintenance|^citation$|^license$|repository resources|resource files", m.group(1), re.I):
            end = m.start()
            break
    return readme[start:end].strip() + "\n"


def collection_count(collection: str) -> int:
    return len(re.findall(r"^[ \t]*-[ \t]+(?:\*\*)?\[", collection, re.M))


def normalize_name(text: str) -> str:
    return re.sub(r"[^a-z0-9]", "", text.casefold())


def detect_existing(records: list[dict], original: str) -> list[str]:
    ids = set(re.findall(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})", original, re.I))
    names = {normalize_name(s) for s in re.findall(r"^\s*-\s+(?:\*\*)?\[([^\]]+)\]", original, re.M)}
    return sorted(r["id"] for r in records if r["id"] in ids or any(normalize_name(alias) in names for alias in r["name"].split(" / ")))


def apply_corrections(collection: str, corrections: list[dict]) -> tuple[str, list[dict]]:
    """Patch only the named list entry, including indented continuation lines."""
    lines = collection.splitlines(keepends=True)
    report = []
    for correction in corrections:
        matches, changes = 0, 0
        for i, line in enumerate(lines):
            match = re.match(r"^[ \t]*-[ \t]+(?:\*\*)?\[([^\]]+)\]\(", line)
            if not match or match[1] != correction["name"]:
                continue
            matches += 1
            j = i + 1
            while j < len(lines) and (not lines[j].strip() or lines[j].startswith(("  ", "\t"))):
                j += 1
            for k in range(i, j):
                for old in correction["old_urls"]:
                    changes += lines[k].count(old)
                    lines[k] = lines[k].replace(old, correction["paper_url"])
        report.append({"name": correction["name"], "matched_entries": matches,
                       "replaced_links": changes, "paper_url": correction["paper_url"]})
    return "".join(lines), report


def relocate_to_docs(text: str) -> str:
    def relative(url: str) -> str:
        if not url or url.startswith(("#", "/")) or urlparse(url).scheme:
            return url
        return "../" + url.removeprefix("./")
    text = re.sub(r"(\]\()([^\s)]+)", lambda m: m[1] + relative(m[2]), text)
    text = re.sub(r"((?:src|href)=[\"'])([^\"']+)", lambda m: m[1] + relative(m[2]), text)
    return text


def render_legacy(collection: str, report: list[dict], base_label: str) -> str:
    count = collection_count(collection)
    changes = sum(r["replaced_links"] for r in report)
    return (
        f"# Earlier resource collection\n\n[Survey home](../README.md) · [Recent papers](recent-papers.md) · [Research notes](research-notes.md)\n\n"
        f"This section preserves the literature collection from **{base_label}**. "
        f"It contains **{count} list entries**, not {count} independently verified or unique papers. "
        f"This update made **{changes} targeted paper-link replacements**; see [the correction register](research-notes.md#targeted-corrections).\n\n"
        "> **Legacy metadata.** Other titles, venues, links and topic placeholders below are retained rather than re-certified. "
        "Entries that point to search pages remain discovery placeholders. Inclusion is not a claim of reproducibility or endorsement.\n\n"
        "---\n\n" + relocate_to_docs(collection)
    )


def update_existing_readme(original: str, records: list[dict], corrections: list[dict]) -> tuple[str, list[dict]]:
    """Retain the live overview, figures, topic navigation and full earlier list."""
    if RECENT_BEGIN in original or RECENT_END in original:
        raise ValueError("Dated update already applied; use the renderer for later edits.")
    if "consistency in diffusion-based visual generation" not in original.lower():
        raise ValueError("Unexpected repository README.")
    heading = re.search(r"^## Resource collection[ \t]*$", original, re.M)
    if not heading:
        raise ValueError("Cannot locate the resource-collection insertion point.")
    old_count = collection_count(extract_collection(original))
    if old_count == 0:
        raise ValueError("Cannot recognize the existing resource entries.")
    fixed, report = apply_corrections(original, corrections)
    position = re.search(r"^## Resource collection[ \t]*$", fixed, re.M).start()
    notice = (
        f"> **Curation update · {CUTOFF}.** The dated register below contains {len(records)} distinct papers. "
        f"The existing collection of {old_count} list entries remains fully expanded further down this page; "
        "legacy entries are not a count of independently verified, unique papers. "
        "[Research scope](docs/research-notes.md) · [Update report](docs/literature-update-report.json).\n\n"
    )
    block = notice + RECENT_BEGIN + "\n" + render_recent(records) + RECENT_END + "\n\n---\n\n"
    updated = fixed[:position] + block + fixed[position:]
    updated = updated.replace('<a href="#resource-collection">Resources</a>',
        '<a href="#recent-literature">Recent papers</a> ·\n  <a href="#resource-collection">Resources</a>', 1)
    updated = updated.replace('Paper-Preprint-b31b1b', 'Paper-Preprints.org-b31b1b', 1)
    overview = updated.find('## Overview')
    header = updated[:overview] if overview >= 0 else ''
    badges = []
    if 'img.shields.io/github/stars/' not in header:
        badges.append(f'  <a href="{REPO_URL}/stargazers"><img src="https://img.shields.io/github/stars/{REPOSITORY}?style=flat-square&amp;label=Stars&amp;color=E3B341" alt="GitHub stars"></a>')
    if 'visitor-badge.laobi.icu/badge?' not in header:
        _, visitor = discover_presentation(original)
        badges.append(f'  <a href="{REPO_URL}"><img src="{html.escape(visitor, quote=True)}" alt="Visitor badge requests"></a>')
    badges.append(f'  <a href="#recent-literature"><img src="https://img.shields.io/badge/Recent%20papers-{len(records)}-2563EB?style=flat-square" alt="{len(records)} recent papers"></a>')
    close = updated.find('</div>')
    if close < 0 or (overview >= 0 and close > overview):
        raise ValueError('Expected centered header was not found; refusing an unreviewed layout.')
    updated = updated[:close] + '<p align="center">\n' + '\n'.join(badges) + '\n</p>\n\n' + updated[close:]
    updated = UPDATE_MARKER + '\n' + updated
    if collection_count(extract_collection(updated)) != old_count:
        raise ValueError('Legacy resource count changed unexpectedly.')
    return updated, report
