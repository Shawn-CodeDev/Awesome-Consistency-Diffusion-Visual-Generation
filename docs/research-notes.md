# Literature update: scope, provenance and maintenance

[Survey home](../README.md) · [Recent register](recent-papers.md) · [Application report](literature-update-report.json)

## Research snapshot

The **2026-11-05** register contains **168 distinct arXiv papers**: 113 first submitted in 2026 and 55 in 2025. Editorial primary relations are External (50), Internal (66) and Normative (52). This gap-filling pass adds 73 papers to the November 4 register: 53 first posted in 2026 and 20 in 2025. The additions span February 18, 2025 through November 2, 2026; they are not all newly published papers. The 95 earlier records retain their original metadata and checked-on dates; they were not silently re-certified. A method and associated benchmark in one paper count once.

The register covers image and multi-image editing, compositional and spatial grounding, typography, structural and camera control, video editing, subject identity, multi-view geometry, multi-shot narratives, persistent memory, long video, preference learning, safety and concept erasure, capability retention, physics and causal evaluation. Related unified or autoregressive systems are included only for their relevant generation mechanisms or diagnostics; not every entry is claimed to be a pure diffusion model. Consistency refers to generated content, not only fast Consistency Models.

## November 4 incremental search

The search focused on September 17–November 4, 2026 and covered editing and prompt alignment, persistent identity and video memory, and physical plausibility and reward alignment. Fourteen new arXiv primary-source records were retained after identifier/title checks against the existing catalog and Markdown collection. AdvDPO (Electronics, October 25) is additionally included in the topic-oriented normative methods list and selected bibliography, because the dated catalog schema uses arXiv identifiers. Its title, authors, publication date and scope were checked against the publisher-indexed abstract. This is a curated search, not a claim of exhaustive coverage. The diffusion-video reasoning paper arXiv:2609.36826 was excluded because task-prediction consensus is not a direct fit to generated-content consistency. Optional code links were omitted when not verified. The earlier integration report below describes the historical September pass; current additions are recorded in `literature-update-2026-11-04.json`.

## November 5 gap-filling search

The broader pass revisits 2025–2026 literature rather than restricting discovery to papers posted since the last update. It adds 15 External, 36 Internal and 22 Normative records, covering localized and multi-turn editing, multi-reference and identity preservation, multi-view geometry, long-video and narrative memory, safety alignment, reward modeling and physical/world-state evaluation. [The November 5 report](literature-update-2026-11-05.json) lists every added identifier and the final counts.

All 73 new titles, first-submission dates and first authors were checked against primary arXiv metadata, and each short description was checked against its abstract. Identifiers, normalized full titles and short names were compared with all tracked text catalogs and the recoverable historical ninth additional-paper batch. Older records were preserved. GuardPaint's metadata title has only its missing whitespace restored. Memory Forcing uses its active October 19 version 3; the withdrawn version 2 is recorded as a history caveat. LongVie and LongVie 2 are separate papers, but their shared benchmark is not counted as another paper.

Scope is based on the generated output's agreement target. RobotAPO qualifies because it trains a flow-matching manipulation-video generator for physical consistency, rather than being an action-only robot policy. Learning-to-Memorize is included as related autoregressive context-memory work, and the persistent-identity benchmark compares mixed generator families; neither is labeled a pure diffusion architecture. The metadata records these distinctions. Benchmark and evaluator papers may assess multiple model families. Speed-only consistency distillation and action-policy-only work are not included merely for using the word consistency.

The legacy additional-200 index currently points to two files absent from main: batches 09 and 10. Batch 09 is recoverable from an unmerged historical branch, while no complete batch 10 was found in fetched history and its staged package is truncated. This pass does not silently restore unmerged content, invent missing entries or count those pages as new findings. The available batch pages, rather than the advertised 200 total, define the legacy deduplication evidence.

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
python -m unittest discover -s tests -p 'test_*.py' -v
python scripts/check_resource_table.py
```

The renderer replaces only the marked recent-paper block and its exports. It does not regenerate the manually maintained introduction, figures or earlier resource list. Validation is offline: identifiers, duplicate titles, date bounds, relations, source URL syntax, CSV/BibTeX/Markdown agreement and regression tests. It is not a live-link or scientific-validity check.
