# Awesome Consistency in Diffusion-Based Visual Generation

[![Validate resource tables](https://github.com/Shawn-CodeDev/Awesome-Consistency-Diffusion-Visual-Generation/actions/workflows/validate-resources.yml/badge.svg)](https://github.com/Shawn-CodeDev/Awesome-Consistency-Diffusion-Visual-Generation/actions/workflows/validate-resources.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

This repository accompanies the survey:

> **Consistency in Diffusion-Based Visual Generation: A Survey**  
> Song Yan, Wei Zhai, Ruixuan Li, Zhangping Yang, Chenfeng Wang, Yancheng Cai, Tao Zhang, Ling Wang, Yunwei Lan, Yujie He, Min Li, Zheng-Jun Zha.

The repository provides a curated and structured resource map for **consistency problems in diffusion-based visual generation**. Instead of organizing the literature only by task names such as text-to-image generation, editing, personalization, video generation, or 3D generation, this project organizes methods and resources by the **agreement relation** they try to enforce.

## Why this repository exists

Diffusion models now generate high-quality images, videos, 3D-aware assets, and interactive visual content. However, perceptual quality alone does not guarantee consistency. A visually realistic sample may still:

- ignore objects, attributes, counts, or relations in the prompt;
- fail to preserve unedited content during image editing;
- lose subject identity across images, scenes, or prompts;
- disagree across views in multi-view or 3D-aware generation;
- flicker or forget entities in video and story generation;
- violate human preference, safety constraints, or physical plausibility.

Existing surveys usually follow task or modality boundaries. This repository instead treats consistency as a family of **generation-time agreement requirements**, making it easier to compare methods, benchmarks, and trade-offs across tasks.

## Table of contents

- [Core taxonomy](#core-taxonomy)
- [Resource maps](#resource-maps)
- [Coverage labels](#coverage-labels)
- [Repository structure](#repository-structure)
- [How to use this repository](#how-to-use-this-repository)
- [Contributing](#contributing)
- [Citation](#citation)
- [License](#license)

## Core taxonomy

We organize consistency into three primary relations.

| Relation | Agreement target | Representative failures | Representative settings |
|---|---|---|---|
| **External consistency** | Agreement with conditions specified outside the generated sample | prompt omission, attribute misbinding, counting error, control mismatch, over-editing | prompt following, compositional generation, structural control, layout/pose/depth conditioning, instruction-based editing |
| **Internal consistency** | Agreement among generated parts, views, instances, frames, or story states | identity drift, cross-view disagreement, temporal flicker, narrative forgetting | personalization, multi-view generation, 3D-aware generation, video generation, story visualization |
| **Normative consistency** | Agreement with evaluative principles not fully specified by the prompt | low human preference, unsafe output, physical implausibility, causal violation | preference alignment, safety editing, concept removal, physical commonsense evaluation, world-model diagnostics |

The survey also uses four auxiliary axes:

1. **Observation unit**: single image, edited pair, identity-conditioned set, multi-view bundle, video/story sequence.
2. **Agreement target**: prompt semantics, structure, reference appearance, identity, geometry, temporal state, safety, preference, physical plausibility.
3. **Optimization locus**: data/objective design, condition-path design, trajectory-time intervention, cross-instance coupling, post-hoc filtering.
4. **Evidence source**: VQA/MLLM checks, similarity metrics, geometric signals, tracking diagnostics, reward models, safety classifiers, human judgments, stress tests.

See [`docs/taxonomy.md`](docs/taxonomy.md) and [`resources/taxonomy_methods.csv`](resources/taxonomy_methods.csv) for the current taxonomy map.

## Resource maps

This repository currently tracks three resource maps.

### 1. Benchmark, dataset, and evaluator coverage

[`resources/benchmark_coverage.csv`](resources/benchmark_coverage.csv) summarizes benchmarks, datasets, evaluators, and diagnostic resources according to six consistency dimensions.

Current coverage includes:

- **External consistency resources**: TIFA, GenEval, T2I-CompBench, GenEval2, HRS-Bench, DPG-Bench, GenAI-Bench, EditBench, MagicBrush, ConceptBed.
- **Internal consistency resources**: MVG-Bench, MET3R, VBench, Video-Bench, EvalCrafter, FETV, ViStoryBench, MeViS, MOSE, TAO, VSPW, nuScenes.
- **Normative consistency resources**: Pick-a-Pic, ImageReward, HPS, HPSv2, HPSv3, VisionReward, Six-CD, PhyBench, VideoPhy, PhyCoBench, PhyGenBench, VideoPhy-2, T2VPhysBench, T2VWorldBench, Physics-IQ, PhyWorldBench, VideoVerse, PhyEduVideo.

The table is not intended to rank resources by overall quality. It instead asks: **which consistency claim can this resource diagnose?**

### 2. Related survey positioning

[`resources/related_surveys.csv`](resources/related_surveys.csv) compares prior surveys with this survey using the current five-category grouping:

- text-to-image and controllable generation;
- editing and personalization;
- video and long-form generation;
- alignment and safety;
- 3D, 4D, and physical generation.

The key distinction is that this survey organizes the field by agreement relations and enforcement loci rather than by application categories alone.

### 3. Method taxonomy map

[`resources/taxonomy_methods.csv`](resources/taxonomy_methods.csv) provides a compact mapping from each consistency subsection to representative methods and benchmarks.

## Coverage labels

The benchmark coverage table uses six diagnostic dimensions.

| Label | Meaning |
|---|---|
| **P/C** | prompt and compositional faithfulness |
| **S/E** | structural control and edit preservation |
| **ID** | subject/identity persistence |
| **V/T** | multi-view, temporal, or narrative coherence |
| **N/S** | preference, safety, or value alignment |
| **P/W** | physical, causal, or world-grounded plausibility |

Coverage values:

| Value | Meaning |
|---|---|
| **H** | direct evaluation with dedicated tasks, annotations, or metrics |
| **M** | partial support or adaptable evidence |
| **L** | only indirect relevance |

For example, a video benchmark may have high coverage for temporal coherence but low coverage for safety. A reward model may have high coverage for preference alignment but low coverage for edit preservation or physical causality.

## Repository structure

```text
.
├── README.md
├── CITATION.cff
├── LICENSE
├── docs/
│   ├── taxonomy.md
│   ├── benchmark_coverage.md
│   ├── related_surveys.md
│   └── contribution_guide.md
├── resources/
│   ├── benchmark_coverage.csv
│   ├── related_surveys.csv
│   ├── taxonomy_methods.csv
│   └── selected_bibtex.bib
├── scripts/
│   └── check_resource_table.py
├── paper/
│   └── README.md
└── .github/
    ├── ISSUE_TEMPLATE/
    │   └── resource_addition.yml
    └── workflows/
        └── validate-resources.yml
```

## How to use this repository

### Browse the taxonomy

Start with [`docs/taxonomy.md`](docs/taxonomy.md) if you want the conceptual structure. This is the best entry point for understanding how external, internal, and normative consistency differ.

### Find evaluation resources

Use [`resources/benchmark_coverage.csv`](resources/benchmark_coverage.csv) if you need a benchmark, dataset, evaluator, or diagnostic protocol for a specific consistency claim.

Examples:

- Need prompt compositionality? Filter `P/C = H`.
- Need video temporal coherence? Filter `V/T = H` or `V/T = M`.
- Need safety or preference evaluation? Filter `N/S = H`.
- Need physical plausibility diagnostics? Filter `P/W = H`.

### Validate table edits

After editing `resources/benchmark_coverage.csv`, run:

```bash
python scripts/check_resource_table.py
```

The script checks:

- required columns;
- duplicate BibTeX keys;
- valid coverage labels (`H`, `M`, `L`);
- URL formatting for public code or project links.

The same check is also run automatically by GitHub Actions on every push and pull request.

## Contributing

Contributions are welcome. Good contributions include:

- adding a missing benchmark, dataset, evaluator, method, or survey;
- correcting an official code/project link;
- improving a diagnostic-use or blind-spot description;
- updating a BibTeX entry after proceedings metadata becomes available;
- refining coverage labels when a resource is misclassified.

For a new resource, please provide:

1. resource title;
2. BibTeX key;
3. venue and year;
4. official paper URL;
5. official project/code URL, if available;
6. resource type;
7. modality;
8. primary consistency relation;
9. coverage values for `P/C`, `S/E`, `ID`, `V/T`, `N/S`, and `P/W`;
10. one-sentence diagnostic use and one-sentence blind spot.

Use the issue template: [Add or correct a resource](.github/ISSUE_TEMPLATE/resource_addition.yml).

## Maintenance notes

Some resources, especially 2025--2026 benchmark papers, may initially appear as arXiv or project-page entries before official proceedings metadata is stable. When official BibTeX becomes available, please update [`resources/selected_bibtex.bib`](resources/selected_bibtex.bib) and any corresponding table entries.

When adding links, prefer official repositories or project pages over unofficial reimplementations. If no stable official repository exists, leave the code URL blank in the CSV table.

## Citation

If this survey or resource list is useful, please cite:

```bibtex
@misc{consistency_diffusion_survey,
  title  = {Consistency in Diffusion-Based Visual Generation: A Survey},
  author = {Yan, Song and Zhai, Wei and Li, Ruixuan and Yang, Zhangping and Wang, Chenfeng and Cai, Yancheng and Zhang, Tao and Wang, Ling and Lan, Yunwei and He, Yujie and Li, Min and Zha, Zheng-Jun},
  year   = {2026},
  note   = {Manuscript}
}
```

## License

This repository is released under the [MIT License](LICENSE).
