# Awesome Consistency in Diffusion-Based Visual Generation

[![Validate resource tables](https://github.com/Shawn-CodeDev/Awesome-Consistency-Diffusion-Visual-Generation/actions/workflows/validate-resources.yml/badge.svg)](https://github.com/Shawn-CodeDev/Awesome-Consistency-Diffusion-Visual-Generation/actions/workflows/validate-resources.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

This repository accompanies the survey:

> **Consistency in Diffusion-Based Visual Generation: A Survey**  
> Song Yan, Wei Zhai, Chenfeng Wang, Ruixuan Li, Zhangping Yang, Yancheng Cai, Tao Zhang, Ling Wang, Yunwei Lan, Yujie He, Yang Cao, Min Li, Zheng-Jun Zha.

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
- [Curated papers and resources](#curated-papers-and-resources)
  - [External consistency](#external-consistency)
  - [Internal consistency](#internal-consistency)
  - [Normative consistency](#normative-consistency)
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

See [`docs/taxonomy.md`](docs/taxonomy.md) and [`resources/taxonomy_methods.csv`](resources/taxonomy_methods.csv) for the machine-readable taxonomy map.

## Curated papers and resources

Links point to an official paper, project page, or code repository when a stable public link is available. The machine-readable benchmark/evaluator table is maintained in [`resources/benchmark_coverage.csv`](resources/benchmark_coverage.csv).

### External consistency

External consistency asks whether the output follows user- or task-provided conditions, including prompts, layouts, masks, poses, reference images, and editing instructions.

#### Prompt and compositional faithfulness

| Paper / resource | Year / venue | Role | Links |
|---|---:|---|---|
| TIFA: Accurate and Interpretable Text-to-Image Faithfulness Evaluation with Question Answering | 2023 | QA-based prompt-faithfulness evaluator | [Code](https://github.com/Yushi-Hu/tifa) |
| GenEval: An Object-Focused Framework for Evaluating Text-to-Image Alignment | 2023 | object, attribute, counting, and relation benchmark | [Code](https://github.com/djghosh13/geneval) |
| T2I-CompBench: A Comprehensive Benchmark for Open-world Compositional Text-to-image Generation | 2023 | compositional prompt benchmark | [Code](https://github.com/Karine-Huang/T2I-CompBench) |
| GenEval 2 | 2025/2026 | harder prompt-following benchmark | [Code](https://github.com/facebookresearch/GenEval2) |
| HRS-Bench: Holistic, Reliable and Scalable Benchmark for Text-to-Image Models | ICCV 2023 | holistic T2I capability benchmark | [Code](https://github.com/eslambakr/HRS_benchmark) |
| DPG-Bench / ELLA: Equip Diffusion Models with LLM for Enhanced Semantic Alignment | 2024 | dense-prompt following benchmark and semantic-alignment resource | [Code](https://github.com/TencentQQGYLab/ELLA) |
| GenAI-Bench / VQAScore: Evaluating Text-to-Visual Generation with Image-to-Text Generation | ECCV 2024 | compositional text-to-image/video/3D evaluation | [Code](https://github.com/linzhiqiu/t2v_metrics) |
| Attend-and-Excite: Attention-Based Semantic Guidance for Text-to-Image Diffusion Models | 2023 | token-level prompt repair during denoising | [Code](https://github.com/yuval-alaluf/Attend-and-Excite) |
| BoxDiff: Text-to-Image Synthesis with Training-Free Box-Constrained Diffusion | ICCV 2023 | spatial constraint and layout-aware guidance | [Code](https://github.com/showlab/BoxDiff) |
| Composer: Creative and Controllable Image Synthesis with Composable Conditions | ICML 2023 | compositional condition design | [Code](https://github.com/damo-vilab/composer) |
| Make-It-Count | 2024 | count-aware text-to-image generation | Paper / project link to be added |
| CountDiffusion | 2024 | training-free counting guidance | Paper / project link to be added |
| YOLO-Count | 2024 | differentiable object counting for T2I | Paper / project link to be added |

#### Grounded, structural, and multi-condition control

| Paper / resource | Year / venue | Role | Links |
|---|---:|---|---|
| ControlNet: Adding Conditional Control to Text-to-Image Diffusion Models | ICCV 2023 | trainable control branch for structure-conditioned generation | [Code](https://github.com/lllyasviel/ControlNet) |
| GLIGEN: Open-Set Grounded Text-to-Image Generation | CVPR 2023 | grounded generation with boxes and grounding tokens | [Code](https://github.com/gligen/GLIGEN) |
| T2I-Adapter: Learning Adapters to Dig out More Controllable Ability for Text-to-Image Diffusion Models | AAAI 2024 | lightweight structural adapters | [Code](https://github.com/TencentARC/T2I-Adapter) |
| IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models | 2023/2024 | reference-image conditioning | [Code](https://github.com/tencent-ailab/IP-Adapter) |
| AnyDoor: Zero-shot Object-level Image Customization | CVPR 2024 | object-level reference insertion and customization | [Code](https://github.com/ali-vilab/AnyDoor) |
| FreeDoM: Training-Free Energy-Guided Conditional Diffusion Model | ICCV 2023 | energy-guided conditional generation | [Code](https://github.com/vvictoryuki/FreeDoM) |
| HumanSD: A Native Skeleton-Guided Diffusion Model for Human Image Generation | ICCV 2023 | skeleton-guided human generation | [Code](https://github.com/IDEA-Research/HumanSD) |
| SemanticControl: A Training-Free Approach for Handling Loosely Aligned Visual Conditions | 2024 | training-free semantic condition control | Paper / project link to be added |
| LayoutDM / LayoutDiffusion / layout-generation resources | 2023--2024 | layout-centric generation and structural design | Links to be added |
| PosterCraft / CreatiPoster / PosterMaker | 2024--2025 | poster and graphic-layout applications | Links to be added |
| TryOnDiffusion / StableVITON / AnyDressing | 2023--2025 | virtual try-on and dressing applications | Links to be added |

#### Edit consistency and preservation

| Paper / resource | Year / venue | Role | Links |
|---|---:|---|---|
| Prompt-to-Prompt Image Editing with Cross-Attention Control | ICLR 2023 | cross-attention control for edit preservation | [Code](https://github.com/google/prompt-to-prompt) |
| DiffEdit: Diffusion-Based Semantic Image Editing with Mask Guidance | ICLR 2023 | prompt-difference mask and localized editing | [Project](https://github.com/Xiang-cd/DiffEdit-stable-diffusion) |
| InstructPix2Pix: Learning to Follow Image Editing Instructions | CVPR 2023 | instruction-guided image editing | [Code](https://github.com/timothybrooks/instruct-pix2pix) |
| InstructDiffusion | 2023/2024 | unified instruction-based diffusion editing | [Code](https://github.com/cientgu/InstructDiffusion) |
| Null-Text Inversion for Editing Real Images using Guided Diffusion Models | CVPR 2023 | inversion-based real-image editing | [Project](https://null-text-inversion.github.io/) |
| Imagic: Text-Based Real Image Editing with Diffusion Models | CVPR 2023 | text-based real-image editing | [Project](https://imagic-editing.github.io/) |
| Paint-by-Example: Exemplar-based Image Editing with Diffusion Models | CVPR 2023 | exemplar-guided editing | [Code](https://github.com/Fantasy-Studio/Paint-by-Example) |
| DragDiffusion: Harnessing Diffusion Models for Interactive Point-based Image Editing | CVPR 2024 | drag-based point editing | [Code](https://github.com/Yujun-Shi/DragDiffusion) |
| EditBench / Imagen Editor | CVPR 2023 | text-guided image inpainting benchmark | Paper / official code unavailable |
| MagicBrush: A Manually Annotated Dataset for Instruction-Guided Image Editing | NeurIPS 2023 Datasets and Benchmarks | instruction-guided editing dataset | [Code](https://github.com/OSU-NLP-Group/MagicBrush) |
| ConceptBed | 2024 | concept-learning and concept-binding evaluation | [Code](https://github.com/ConceptBed/evaluations) |

### Internal consistency

Internal consistency asks whether generated states remain mutually compatible across subjects, instances, views, frames, or story sequences.

#### Subject and identity consistency

| Paper / resource | Year / venue | Role | Links |
|---|---:|---|---|
| Textual Inversion: An Image is Worth One Word | ICLR 2023 | token-level personalization | [Code](https://github.com/rinongal/textual_inversion) |
| DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation | CVPR 2023 | subject-specific finetuning | [Project](https://dreambooth.github.io/) |
| Custom Diffusion: Multi-Concept Customization of Text-to-Image Diffusion | CVPR 2023 | parameter-efficient multi-concept customization | [Code](https://github.com/adobe-research/custom-diffusion) |
| Perfusion: Key-Locked Rank One Editing for Text-to-Image Personalization | SIGGRAPH 2023 | lightweight personalization and concept locking | [Project](https://research.nvidia.com/labs/par/Perfusion/) |
| BLIP-Diffusion: Pre-trained Subject Representation for Controllable Text-to-Image Generation | NeurIPS 2023 | subject representation and reference-aware generation | [Code](https://github.com/salesforce/LAVIS/tree/main/projects/blip-diffusion) |
| PhotoMaker: Customizing Realistic Human Photos via Stacked ID Embedding | CVPR 2024 | ID-embedding-based human personalization | [Code](https://github.com/TencentARC/PhotoMaker) |
| InstantID: Zero-shot Identity-Preserving Generation in Seconds | 2024 | instant identity-preserving generation | [Code](https://github.com/InstantID/InstantID) |
| ConsiStory: Training-Free Consistent Text-to-Image Generation | 2024 | training-free character/subject consistency | [Code](https://github.com/NVlabs/consistory) |
| StoryDiffusion: Consistent Self-Attention for Long-Range Image and Video Generation | NeurIPS 2024 | long-range character and story consistency | [Code](https://github.com/HVision-NKU/StoryDiffusion) |
| CharaConsist | 2024/2025 | fine-grained consistent character generation | Link to be added |
| Preserve and Personalize | ICLR 2026 | personalization without distributional drift | [Project](https://rlgnswk.github.io/PreserveAndPersonalize_ProjectPage/) |
| ConceptPrism | CVPR 2026 | concept disentanglement in personalized diffusion | Link to be added |

#### Multi-view and 3D consistency

| Paper / resource | Year / venue | Role | Links |
|---|---:|---|---|
| Zero-1-to-3: Zero-shot One Image to 3D Object | ICCV 2023 | view-conditioned novel-view generation | [Code](https://github.com/cvlab-columbia/zero123) |
| Cascade-Zero123 | 2023/2024 | cascaded single-image-to-3D view synthesis | [Code](https://github.com/EnVision-Research/Cascade-Zero123) |
| SyncDreamer: Generating Multiview-consistent Images from a Single-view Image | ICLR 2024 | synchronized multi-view diffusion | [Code](https://github.com/liuyuan-pal/SyncDreamer) |
| MVDream: Multi-view Diffusion for 3D Generation | ICLR 2024 | text/image-conditioned multi-view diffusion | [Code](https://github.com/bytedance/MVDream) |
| Wonder3D: Single Image to 3D using Cross-Domain Diffusion | CVPR 2024 | cross-domain multi-view generation | [Code](https://github.com/xxlong0/Wonder3D) |
| ViewDiff: 3D-Consistent Image Generation with Text-to-Image Models | CVPR 2024 | 3D-consistent multi-view generation | [Project](https://lukashoel.github.io/ViewDiff/) |
| EscherNet: A Generative Model for Scalable View Synthesis | CVPR 2024 | scalable arbitrary-view synthesis | [Project](https://kxhit.github.io/EscherNet/) |
| MVG-Bench | 2024 | multi-view generation benchmark | [Code](https://github.com/xiexh20/MVGBench) |
| MET3R: Measuring Multi-View Consistency in Generated Images | 2024 | multi-view consistency metric | [Code](https://github.com/mohammadasim98/met3r) |

#### Temporal, video, and narrative consistency

| Paper / resource | Year / venue | Role | Links |
|---|---:|---|---|
| VideoLDM: Align Your Latents | CVPR 2023 | latent video diffusion baseline | [Project](https://research.nvidia.com/labs/toronto-ai/VideoLDM/) |
| AnimateDiff: Animate Your Personalized Text-to-Image Diffusion Models without Specific Tuning | ICLR 2024 | motion module for personalized T2I backbones | [Code](https://github.com/guoyww/AnimateDiff) |
| FateZero: Fusing Attentions for Zero-shot Text-based Video Editing | ICCV 2023 | attention-based video editing consistency | [Code](https://github.com/ChenyangQiQi/FateZero) |
| Video-P2P: Video Editing with Cross-Attention Control | 2023 | Prompt-to-Prompt-style video editing | [Code](https://github.com/ShaoTengLiu/Video-P2P) |
| VideoCrafter2: Overcoming Data Limitations for High-Quality Video Diffusion Models | CVPR 2024 | high-quality video diffusion generation | [Code](https://github.com/AILab-CVC/VideoCrafter) |
| TaleCrafter | 2024 | interactive story visualization with multiple characters | Link to be added |
| One-Prompt-One-Story | 2024 | consistent text-to-image story generation | Link to be added |
| MovieDreamer | 2024/2025 | hierarchical long visual sequence generation | Link to be added |
| MotionStream: Real-Time Video Generation with Interactive Motion Controls | ICLR 2026 | real-time interactive video control | [OpenReview](https://openreview.net/forum?id=v1DKz5Vxr7) |
| VBench: Comprehensive Benchmark Suite for Video Generative Models | CVPR 2024 | video generation benchmark with temporal diagnostics | [Code](https://github.com/Vchitect/VBench) |
| Video-Bench: Human-Aligned Video Generation Benchmark | CVPR 2025 | human-aligned video generation evaluation | [Code](https://github.com/Video-Bench/Video-Bench) |
| EvalCrafter: Benchmarking and Evaluating Large Video Generation Models | CVPR 2024 | video generation evaluation toolkit | [Code](https://github.com/evalcrafter/EvalCrafter) |
| FETV: Fine-Grained Evaluation of Open-Domain Text-to-Video Generation | NeurIPS 2023 Datasets and Benchmarks | fine-grained T2V benchmark | [Code](https://github.com/llyx97/FETV) |
| ViStoryBench | CVPR 2026 / 2025 preprint | story visualization benchmark | [Code](https://github.com/ViStoryBench/ViStoryBench) |
| MeViS | ICCV 2023 | motion-expression video segmentation dataset | [Code](https://github.com/henghuiding/MeViS) |
| MOSE | 2023/2024 | video object segmentation dataset | [Code](https://github.com/henghuiding/MOSE-api) |
| TAO | ECCV 2020 | long-tail object tracking dataset | [Code](https://github.com/TAO-Dataset/tao) |
| VSPW | CVPR 2021 | video scene parsing dataset | [Code](https://github.com/VSPW-dataset/VSPW_code) |
| nuScenes | CVPR 2020 | autonomous-driving multi-sensor dataset | [Code](https://github.com/nutonomy/nuscenes-devkit) |

### Normative consistency

Normative consistency asks whether outputs satisfy evaluative criteria such as preference, aesthetics, safety, value alignment, physical plausibility, commonsense, and causal/world-state validity.

#### Preference and aesthetics

| Paper / resource | Year / venue | Role | Links |
|---|---:|---|---|
| Pick-a-Pic: An Open Dataset of User Preferences for Text-to-Image Generation | NeurIPS 2023 | pairwise preference dataset / PickScore | [Code](https://github.com/yuvalkirstain/PickScore) |
| ImageReward: Learning and Evaluating Human Preferences for Text-to-Image Generation | NeurIPS 2023 | learned human preference reward | [Code](https://github.com/zai-org/ImageReward) |
| HPS: Human Preference Score | 2023 | human preference scoring | Link to be added |
| HPSv2 | 2024 | refined human-preference benchmark | [Code](https://github.com/tgxs002/HPSv2) |
| HPSv3 | 2025 | wide-spectrum human preference benchmark | [Code](https://github.com/MizzenAI/HPSv3) |
| MPS: Learning Multi-Dimensional Human Preference for Text-to-Image Generation | CVPR 2024 | multi-dimensional preference modeling | Link to be added |
| VisionReward: Fine-Grained Multi-Dimensional Human Preference Learning for Image and Video Generation | AAAI 2026 | image/video preference evaluator | [Code](https://github.com/zai-org/VisionReward) |
| Diffusion-DPO: Diffusion Model Alignment Using Direct Preference Optimization | NeurIPS 2023/2024 | preference optimization for diffusion | [Code](https://github.com/SalesforceAIResearch/DiffusionDPO) |
| SPO: Aesthetic Post-Training Diffusion Models from Generic Preferences with Step-by-step Preference Optimization | CVPR 2025 | aesthetic post-training | Link to be added |
| DSPO: Direct Score Preference Optimization for Diffusion Model Alignment | ICLR 2025 | score-level preference optimization | Link to be added |
| RankDPO: Scalable Ranked Preference Optimization for Text-to-Image Generation | ICCV 2025 | ranked preference optimization | Link to be added |
| CMPO / CaPO: Calibrated Multi-Preference Optimization for Aligning Diffusion Models | CVPR 2025 | multi-preference calibration | Link to be added |

#### Safety, value alignment, and concept editing

| Paper / resource | Year / venue | Role | Links |
|---|---:|---|---|
| Safe Latent Diffusion | CVPR 2023 | inference-time safe guidance | [Code](https://github.com/ml-research/safe-latent-diffusion) |
| Erasing Concepts from Diffusion Models | ICCV 2023 | concept erasure | [Code](https://github.com/rohitgandikota/erasing) |
| Ablating Concepts in Text-to-Image Diffusion Models | ICCV 2023 | concept ablation | [Project](https://www.cs.cmu.edu/~concept-ablation/) |
| Unified Concept Editing | 2023/2024 | multi-concept editing / safety intervention | [Code](https://github.com/rohitgandikota/unified-concept-editing) |
| ACE: Anti-Editing Concept Erasure | 2024/2025 | robust concept erasure | Link to be added |
| Editing Massive Concepts in Text-to-Image Diffusion Models | 2024/2025 | large-scale concept editing | Link to be added |
| Six-CD: Benchmarking Concept Removals for Benign Text-to-Image Diffusion Models | 2024/2025 | concept suppression and benign retention benchmark | [Code](https://github.com/Artanisax/Six-CD) |
| Responsible Text-to-Image Diffusion | ICML 2026 | interpretable and controllable safe/fair semantics | Link to be added |

#### Physical, commonsense, and causal consistency

| Paper / resource | Year / venue | Role | Links |
|---|---:|---|---|
| PhyBench: A Physical Commonsense Benchmark for Text-to-Image Models | 2024 | static physical commonsense evaluation | [Code](https://github.com/OpenGVLab/PhyBench) |
| VideoPhy: Evaluating Physical Commonsense for Video Generation | ICLR 2025 | physical commonsense evaluation for videos | [Code](https://github.com/Hritikbansal/videophy) |
| PhyCoBench | 2024/2025 | optical-flow-based physical coherence benchmark | [Code](https://github.com/Jeckinchen/PhyCoBench) |
| PhyGenBench | 2024/2025 | physical commonsense benchmark for video generation | [Code](https://github.com/OpenGVLab/PhyGenBench) |
| VideoPhy-2 | ICLR 2026 | action-centric physical commonsense benchmark | [Project](https://videophy2.github.io/) |
| T2VPhysBench | 2025 | first-principles physical consistency benchmark | Link to be added |
| T2VWorldBench | 2025 | world-knowledge, commonsense, and causal evaluation | Link to be added |
| Physics-IQ: Do Generative Video Models Understand Physical Principles? | WACV 2026 | physical-principle benchmark for video generation | [Code](https://github.com/google-deepmind/physics-IQ-benchmark) |
| PhyWorldBench | 2025 | physical realism benchmark for text-to-video | [Code](https://github.com/g-jing/phy-world-bench) |
| VideoVerse | 2025/2026 | world-model-oriented text-to-video evaluation | [Code](https://github.com/Zeqing-Wang/VideoVerse) |
| PhyEduVideo | WACV 2026 | physics-education-oriented video benchmark | [Code](https://github.com/meghamariamkm/PhyEduVideo) |
| PhyWorld: How Far Is Video Generation from World Model? | ICML 2025 | physical-law perspective on world models | [Paper](https://proceedings.mlr.press/v267/kang25g.html) |
| OSCBench: Benchmarking Object State Change in Text-to-Video Generation | 2026 | object-state change and action consequence benchmark | Link to be added |

## Resource maps

This repository currently tracks three resource maps.

### 1. Benchmark, dataset, and evaluator coverage

[`resources/benchmark_coverage.csv`](resources/benchmark_coverage.csv) summarizes benchmarks, datasets, evaluators, and diagnostic resources according to six consistency dimensions.

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
  author = {Yan, Song and Zhai, Wei and Wang, Chenfeng and Li, Ruixuan and Yang, Zhangping and Cai, Yancheng and Zhang, Tao and Wang, Ling and Lan, Yunwei and He, Yujie and Cao, Yang and Li, Min and Zha, Zheng-Jun},
  year   = {2026},
  note   = {Manuscript}
}
```

## License

This repository is released under the [MIT License](LICENSE).
