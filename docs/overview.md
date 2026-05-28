# Project Overview

This document provides a compact overview of the repository structure, taxonomy, resource organization, and maintenance conventions for **Awesome Consistency in Diffusion-Based Visual Generation**.

The repository accompanies the survey:

> **Consistency in Diffusion-Based Visual Generation: A Survey**
> Song Yan, Wei Zhai, Chenfeng Wang, Ruixuan Li, Zhangping Yang, Yancheng Cai, Tao Zhang, Ling Wang, Yunwei Lan, Yujie He, Yang Cao, Min Li, Zheng-Jun Zha.

The goal of this repository is to collect representative papers, methods, benchmarks, datasets, evaluators, and diagnostic resources related to consistency problems in diffusion-based visual generation.

---

## 1. Scope

This repository focuses on **consistency as a generation-time requirement** in diffusion-based visual generation.

Here, consistency does not refer only to consistency models for fast sampling. Instead, it denotes whether generated visual content remains compatible with a target condition, a related generated state, or an evaluative principle.

Typical questions include:

* Does the generated image follow the prompt, layout, pose, mask, reference image, or edit instruction?
* Does the same subject, scene, geometry, motion, or narrative state remain stable across images, views, frames, or shots?
* Does the generated content satisfy safety, human preference, physical plausibility, commonsense, or world-state constraints?

The repository is therefore organized around **agreement relations**, rather than only around tasks or modalities.

---

## 2. Core Taxonomy

The survey and repository use three primary consistency relations.

| Relation                  | Agreement target                                                                                                | Typical failures                                                                          | Typical settings                                                                                               |
| ------------------------- | --------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **External consistency**  | Agreement with prompts, references, controls, masks, layouts, poses, or edit instructions                       | Prompt omission, attribute binding error, counting error, control mismatch, over-editing  | Text-to-image generation, controllable generation, instruction editing, inpainting, virtual try-on, typography |
| **Internal consistency**  | Agreement among generated subjects, views, frames, shots, or story states                                       | Identity drift, view inconsistency, flicker, state forgetting, narrative discontinuity    | Personalization, multi-view generation, 3D generation, video generation, story visualization                   |
| **Normative consistency** | Agreement with preference, safety, fairness, physical plausibility, commonsense, or causal/world-state criteria | Low preference, unsafe output, benign capability loss, physical violation, causal failure | Preference optimization, safety editing, concept erasure, physical/world-model evaluation                      |

These relations are not mutually exclusive. A single method may involve several relations at the same time. For example, an image editor may need to follow a text instruction, preserve source identity, and avoid unsafe or low-quality outputs. The repository places each method under its dominant consistency requirement while noting secondary relevance where appropriate.

---

## 3. Repository Organization

The repository is organized around the following top-level components.

```text
.
├── README.md
├── LICENSE
├── docs/
│   ├── overview.md
│   └── logos / figures / supplementary notes
├── resources/
│   ├── benchmark_coverage.csv
│   ├── related_surveys.csv
│   ├── taxonomy_methods.csv
│   └── selected_bibtex.bib
├── scripts/
│   └── verification / formatting utilities
└── .github/
    ├── workflows/
    └── ISSUE_TEMPLATE/
```

The main README serves as the public-facing paper list. The `docs/` directory should contain explanatory materials, figures, taxonomy notes, and auxiliary documentation. The `resources/` directory should contain machine-readable tables and BibTeX files. Scripts and workflows should support validation, link checking, and metadata consistency.

---

## 4. Main README

The README is the primary entry point for users. It should remain readable and navigable.

The recommended README structure is:

```text
1. Logo block and badges
2. Survey title and author list
3. Short repository description
4. Table of contents
5. Taxonomy table
6. External consistency resources
7. Internal consistency resources
8. Normative consistency resources
9. Machine-readable resources
10. Coverage labels
11. Contribution guide
12. Citation
13. License
14. Star history
```

The README should avoid long methodological explanations. Those should be moved to `docs/` when they are useful but interrupt the reading flow.

---

## 5. External Consistency

External consistency concerns whether a generated output satisfies an externally specified condition.

Representative condition types include:

* Text prompts
* Layouts and bounding boxes
* Segmentation masks
* Human poses
* Depth maps
* Edge maps
* Reference images
* Editing instructions
* Inpainting masks
* Multi-condition inputs

Typical method families include:

* Prompt-following and compositional generation
* Attention-based prompt repair
* Layout- or box-grounded generation
* Structural control branches and adapters
* Reference-image conditioning
* Instruction-guided image editing
* Masked editing and inpainting
* Typography and visual text rendering
* Virtual try-on and human-conditioned generation

Typical benchmarks and evaluators include prompt-faithfulness benchmarks, compositional text-to-image benchmarks, dense-prompt evaluation, VQA-based evaluation, and instruction-editing datasets.

External consistency resources should answer the question:

> Does the output match the user-provided or task-provided condition?

---

## 6. Internal Consistency

Internal consistency concerns whether related generated states remain mutually compatible.

Representative internal states include:

* Subject identity
* Character appearance
* Clothing and accessories
* Style
* Geometry
* Viewpoint
* Camera trajectory
* Object permanence
* Motion
* Scene state
* Narrative state

Typical method families include:

* Textual inversion and subject personalization
* DreamBooth-style finetuning
* Adapter-based identity conditioning
* Training-free character consistency
* Multi-subject personalization
* Multi-view diffusion
* Image-to-3D generation
* Video diffusion
* Video editing with temporal feature propagation
* Human image animation
* Story visualization and long-range image/video generation

Typical benchmarks and evaluators include identity similarity metrics, multi-view consistency metrics, video generation benchmarks, object tracking datasets, segmentation datasets, and story-level consistency benchmarks.

Internal consistency resources should answer the question:

> Do related generated outputs remain compatible with one another across identity, view, time, or narrative state?

---

## 7. Normative Consistency

Normative consistency concerns whether generated content satisfies evaluative principles that are not fully specified by a single prompt.

Representative normative targets include:

* Human preference
* Aesthetic quality
* Safety
* Fairness
* Value alignment
* Concept restriction
* Benign capability retention
* Physical plausibility
* Commonsense
* Causal state transitions
* World-model validity

Typical method families include:

* Preference reward models
* Direct preference optimization for diffusion
* Reinforcement learning for diffusion models
* Multi-dimensional preference modeling
* Safety guidance
* Concept erasure
* Concept editing
* Machine unlearning
* Safety benchmarks
* Physical commonsense benchmarks
* World-model and simulation-oriented video generation

Normative consistency resources should answer the question:

> Does the output satisfy broader evaluative constraints such as preference, safety, or physical plausibility?

---

## 8. Resource Types

Each resource should be categorized by its role.

| Type          | Meaning                                                                            |
| ------------- | ---------------------------------------------------------------------------------- |
| **Method**    | A generation, editing, alignment, control, personalization, or verification method |
| **Benchmark** | A task suite designed to evaluate a specific consistency property                  |
| **Evaluator** | A metric, reward model, VQA/MLLM evaluator, or learned scoring function            |
| **Dataset**   | A dataset used for training, evaluation, or diagnostic probing                     |
| **Survey**    | A review paper related to a task, modality, or consistency relation                |
| **Tool**      | A script, validation utility, or repository-supporting component                   |

A resource may serve more than one role. For example, a preference dataset may also provide an evaluator, and a benchmark may include both prompts and scoring scripts.

---

## 9. Coverage Labels

The repository uses compact coverage labels to indicate which consistency claims a resource can diagnose.

| Label   | Meaning                                          |
| ------- | ------------------------------------------------ |
| **P/C** | Prompt and compositional faithfulness            |
| **S/E** | Structural control and edit preservation         |
| **ID**  | Subject or identity persistence                  |
| **V/T** | Multi-view, temporal, or narrative coherence     |
| **N/S** | Preference, safety, or value alignment           |
| **P/W** | Physical, causal, or world-grounded plausibility |

Coverage strength can be marked as:

| Strength | Meaning                                                         |
| -------- | --------------------------------------------------------------- |
| **H**    | Direct evaluation with dedicated tasks, annotations, or metrics |
| **M**    | Partial support or adaptable evidence                           |
| **L**    | Only indirect relevance                                         |

These labels describe diagnostic relevance to a consistency claim, not the overall quality of the paper or benchmark.

---

## 10. Machine-Readable Resources

The `resources/` directory should contain structured files that make the repository easy to audit and extend.

Recommended files include:

```text
resources/
├── benchmark_coverage.csv
├── related_surveys.csv
├── taxonomy_methods.csv
└── selected_bibtex.bib
```

### `benchmark_coverage.csv`

This file maps benchmarks, datasets, and evaluators to consistency coverage labels.

Recommended columns:

```text
resource,type,modality,primary_relation,prompt_composition,structure_edit,identity,view_temporal,normative,physical_world,code_url,paper_url,notes
```

### `related_surveys.csv`

This file compares this survey with related surveys.

Recommended columns:

```text
scope,refs,focus,external,internal,normative,cross_relation,notes
```

### `taxonomy_methods.csv`

This file maps representative methods to taxonomy nodes.

Recommended columns:

```text
method,year,venue,primary_relation,secondary_relation,task,optimization_locus,evidence_source,paper_url,code_url,bibtex_key
```

### `selected_bibtex.bib`

This file stores selected BibTeX entries used in the survey and repository.

---

## 11. Recommended Documentation Files

The `docs/` directory can contain short, focused notes rather than another long README.

Recommended files:

```text
docs/
├── overview.md
├── taxonomy.md
├── benchmark_coverage.md
├── contribution_guide.md
├── metadata_policy.md
├── figures.md
└── faq.md
```

### `taxonomy.md`

Detailed explanation of the three consistency relations and their overlap.

### `benchmark_coverage.md`

Detailed explanation of benchmark coverage labels and diagnostic blind spots.

### `contribution_guide.md`

Instructions for adding papers, benchmarks, datasets, and evaluators.

### `metadata_policy.md`

Rules for paper titles, venue names, arXiv links, CVF/OpenReview/PMLR links, GitHub links, DBLP records, and BibTeX keys.

### `figures.md`

Notes about repository figures, logos, taxonomy diagrams, and star-history charts.

### `faq.md`

Short answers to common questions about the taxonomy and repository scope.

---

## 12. Entry Format

For README entries, use a compact and consistent format.

Recommended format:

```md
- [Title](paper_url) *(venue/year or source)* — short explanation of what consistency issue it helps study. [Code](code_url)
```

For table-based entries, use:

```md
| Paper | Venue/source | Paper page | Code / Project | DBLP | Why it matters |
|---|---|---|---|---|---|
| Example Paper | CVPR 2024 | [CVF](...) / [arXiv](...) | [GitHub](...) | [DBLP](...) | One-sentence relevance explanation. |
```

Avoid generic search links in main entries when a stable paper page exists.

---

## 13. Metadata Guidelines

Use stable and verifiable metadata whenever possible.

### Paper title

Use the official paper title from the paper page, proceedings page, arXiv page, or DBLP.

### Venue

Use the official venue if the paper has appeared in proceedings. If the paper is only available as a preprint, use:

```text
arXiv YEAR
```

If the official venue is not yet confirmed, use:

```text
arXiv / venue TBD
```

Do not guess a conference venue.

### Paper page

Prefer stable links in this order:

1. Official proceedings page
2. arXiv page
3. OpenReview page
4. PMLR page
5. ACM / IEEE / Springer page
6. Official project page

### Code link

Prefer official repositories or official project pages. Avoid unofficial reimplementations unless explicitly marked.

### DBLP

Use DBLP when available. If a paper is too recent and not yet indexed, leave the DBLP field blank or mark it as unavailable.

### BibTeX key

Use stable, readable keys. Recommended pattern:

```text
relation_task_shorttitle_year
```

Examples:

```text
external_control_controlnet_2023
internal_identity_dreambooth_2023
normative_preference_imagereward_2023
```

---

## 14. Quality Control Checklist

Before adding a new resource, check:

* The title is official.
* The venue/year is not guessed.
* The paper URL is stable.
* The code/project URL is official or clearly marked.
* The resource is placed under the correct primary consistency relation.
* The one-sentence explanation states why it matters for consistency.
* The entry is not a duplicate under another name.
* The BibTeX key is unique.
* The resource type is clear: method, benchmark, evaluator, dataset, survey, or tool.
* The coverage labels are consistent with the resource's actual diagnostic ability.

---

## 15. Common Failure Cases

### Duplicate paper under different names

Some works appear under a method name, project name, and full paper title. Keep one canonical entry and redirect related names only when needed.

### Topic placeholders mixed with papers

Broad topics such as “prompt expansion,” “world-consistent video diffusion,” or “verifier-guided generation” should not be mixed into paper lists unless linked to a specific paper.

### Venue overclaiming

Do not mark a paper as CVPR, ICCV, ICLR, ICML, NeurIPS, or SIGGRAPH unless the official record confirms it.

### Unofficial code links

Avoid linking to third-party reimplementations as if they were official. If a reimplementation is useful, mark it explicitly.

### Metric overgeneralization

A metric may evaluate one slice of consistency but fail on others. For example, prompt-faithfulness metrics do not necessarily diagnose identity persistence or physical plausibility.

---

## 16. Suggested Reading Routes

Different readers may use the repository in different ways.

### For prompt-following and controllable generation

Start with External Consistency:

* Prompt and compositional generation
* Layout, box, pose, depth, and mask control
* Multi-condition generation
* Instruction-guided editing
* Prompt-faithfulness benchmarks

### For personalization and character consistency

Start with Internal Consistency:

* Textual inversion
* Subject-driven generation
* Identity-preserving adapters
* Multi-subject personalization
* Story and character consistency

### For video and 3D generation

Start with Internal Consistency:

* Multi-view generation
* Image-to-3D generation
* Video diffusion
* Video editing
* Human animation
* Temporal and multi-view benchmarks

### For preference and safety

Start with Normative Consistency:

* Reward models
* Preference optimization
* Safety guidance
* Concept erasure
* Benign retention benchmarks

### For physical and world consistency

Start with Normative Consistency:

* Physical commonsense benchmarks
* Video world models
* Driving world generation
* Action-conditioned simulation
* Causal and state-transition evaluation

---

## 17. Relationship to the Survey

The repository is designed to support the survey in three ways.

First, it provides a continuously updated resource list beyond the static paper bibliography.

Second, it makes the taxonomy operational by mapping methods, benchmarks, datasets, and evaluators to consistency relations.

Third, it exposes diagnostic blind spots. A resource may be strong for prompt alignment but weak for temporal coherence; another may be useful for physical plausibility but irrelevant to edit preservation.

The repository should therefore be read as an evolving companion to the survey rather than as a fixed bibliography.

---

## 18. Star History

The README includes a dynamic star-history chart for repository growth tracking.

The chart uses the repository path:

```text
Shawn-CodeDev/Awesome-Consistency-Diffusion-Visual-Generation
```

The corresponding Markdown/HTML block is:

```html
<p align="center">
  <a href="https://star-history.com/#Shawn-CodeDev/Awesome-Consistency-Diffusion-Visual-Generation&Date">
    <img src="https://api.star-history.com/svg?repos=Shawn-CodeDev/Awesome-Consistency-Diffusion-Visual-Generation&type=Date" alt="Star History Chart" />
  </a>
</p>
```

---

## 19. Citation

If this survey or resource list is useful, please cite:

```bibtex
@misc{consistency_diffusion_survey,
  title  = {Consistency in Diffusion-Based Visual Generation: A Survey},
  author = {Yan, Song and Zhai, Wei and Wang, Chenfeng and Li, Ruixuan and Yang, Zhangping and Cai, Yancheng and Zhang, Tao and Wang, Ling and Lan, Yunwei and He, Yujie and Cao, Yang and Li, Min and Zha, Zheng-Jun},
  year   = {2026},
  note   = {Manuscript}
}
```

---

## 20. License

This repository is released under the MIT License.
