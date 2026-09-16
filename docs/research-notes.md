# Literature update: scope, provenance and maintenance

[Survey home](../README.md) · [Recent register](recent-papers.md) · [Application report](literature-update-report.json)

## Research snapshot

The **2026-09-16** register contains **81 distinct arXiv papers**: 46 first submitted in 2026 and 35 in 2025. Editorial primary relations are External (30), Internal (25) and Normative (26). A method, dataset and benchmark appearing in one paper are counted once, not as independent publications.

The register covers image and multi-image editing, compositional and spatial grounding, typography, structural and camera control, video editing, subject identity, multi-view geometry, multi-shot narratives, persistent memory, long video, preference learning, safety and concept erasure, capability retention, physics and causal evaluation. Related unified or autoregressive systems are included only for their relevant generation mechanisms or diagnostics; not every entry is claimed to be a pure diffusion model. Consistency refers to generated content, not only fast Consistency Models.

## Evidence and limitations

Titles, first submission dates and short descriptions were checked against primary arXiv records or their indexed abstracts in the research pass. The publication integration rechecked several of the newest records, including [GRACE](https://arxiv.org/abs/2609.12731), [StreetDiff](https://arxiv.org/abs/2609.09890), [Discrete Diffusion Bridges](https://arxiv.org/abs/2608.29997) and [Qwen-Image-2.0-RL](https://arxiv.org/abs/2606.27608).

This is **abstract/metadata-level verification**, not a claim of full-text review, experimental reproduction, comprehensive venue verification, or successful execution of linked code. Dates in the catalog are first arXiv submission dates, not conference dates, crawl dates or dates of acceptance. Results and state-of-the-art claims are not reproduced as independently established findings.

The full-title evidence register is in [recent-papers.md](recent-papers.md#evidence-register). JSON records retain a primary source URL, checked-on date, verification level and editorial scope. Classification follows the survey taxonomy; it is an editorial annotation, not necessarily the original authors' terminology. Optional code and project links are author-provided discovery links, not a guarantee of current availability. Blank links mean not recorded in this pass.

## Preserving the existing collection

The current, topic-oriented resource list remains **fully expanded in the README**. Its existing entries are preserved except for the nine explicitly scoped paper-link corrections below. The exact pre-update README is archived at [README.before-2026-09-16.md](archive/README.before-2026-09-16.md). This byte-for-byte archive preserves the original relative links as historical source, rather than acting as a relocated live homepage.

The [integration report](literature-update-report.json) records the actual base commit, preserved entry count, image paths and identifier/name overlaps. Neither 355 legacy entries nor the sum of old and new records is presented as a verified unique-paper total. Existing placeholders and other uncertain legacy metadata have not been silently re-certified. Existing benchmark coverage scores and older bibliography files are not changed by this pass.

<a id="targeted-corrections"></a>
## Targeted paper-link corrections

Corrections are restricted to the named entry and its indented description. Shared erroneous identifiers are never replaced globally. Old venue labels and author metadata are outside the scope of these corrections.

| Entry | Correct primary record |
|:--|:--|
| TIFA | [2303.11897](https://arxiv.org/abs/2303.11897) |
| GenEval | [2310.11513](https://arxiv.org/abs/2310.11513) |
| T2I-CompBench | [2307.06350](https://arxiv.org/abs/2307.06350) |
| HumanSD | [2304.04269](https://arxiv.org/abs/2304.04269) |
| FreeDoM | [2303.09833](https://arxiv.org/abs/2303.09833) |
| FastComposer | [2305.10431](https://arxiv.org/abs/2305.10431) |
| Video-P2P | [2303.04761](https://arxiv.org/abs/2303.04761) |
| VideoCrafter2 | [2401.09047](https://arxiv.org/abs/2401.09047) |
| ShotAdapter | [2505.07652](https://arxiv.org/abs/2505.07652) |

## Bibliography and presentation

The survey retains its complete supplied author list, version-1 DOI and actual Preprints.org platform. A red badge does not imply an arXiv publication. The recent-paper BibTeX is a **discovery bibliography with abbreviated authors** (first author followed by `and others`); replace these author fields with official full-author exports before manuscript submission.

Stars are dynamic. The visitor badge is a third-party request counter, not audited unique visitors or historical GitHub traffic. No count is manually seeded. Existing PNG paths are preserved. The original validation and star-history workflows remain intact.

## Updating the register

Edit `resources/recent_papers.json`, then run:

```bash
python scripts/render_recent_papers.py --update-readme
python scripts/validate_recent_papers.py
python -m unittest discover -s tests -p 'test_recent_papers.py' -v
python scripts/check_resource_table.py
```

The renderer replaces only the marked recent-paper block and its exports. It does not regenerate the manually maintained introduction, figures or earlier resource list. Validation is offline: identifiers, duplicate titles, date bounds, relations, source URL syntax, CSV/BibTeX/Markdown agreement and regression tests. It is not a live-link or scientific-validity check.
