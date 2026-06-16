<a id="top"></a>

<div align="center">

# Consistency in Diffusion-Based Visual Generation: A Survey

<p>
  <img src="docs/USTC.png" height="92" alt="University of Science and Technology of China" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="docs/THU.png" height="92" alt="Tsinghua University" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="docs/HUST.png" height="92" alt="Huazhong University of Science and Technology" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="docs/logo.png" height="92" alt="University of Cambridge" />
</p>

<p>
  <a href="https://www.preprints.org/manuscript/202606.0870/v1"><img src="https://img.shields.io/badge/Paper-Preprint-b31b1b?style=flat-square" alt="Paper"></a>
  <a href="https://doi.org/10.20944/preprints202606.0870.v1"><img src="https://img.shields.io/badge/DOI-10.20944%2Fpreprints202606.0870.v1-2f6f9f?style=flat-square" alt="DOI"></a>
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="MIT License"></a>
</p>

<p>
  <a href="#overview">Overview</a> ·
  <a href="#taxonomy">Taxonomy</a> ·
  <a href="#evaluation-and-optimization">Evaluation & Optimization</a> ·
  <a href="#resource-collection">Resources</a> ·
  <a href="#machine-readable-resources">Data Files</a> ·
  <a href="#contribution-guide">Contribute</a> ·
  <a href="#citation">Citation</a>
</p>

</div>

---

## Overview

This repository accompanies the survey:

> **Consistency in Diffusion-Based Visual Generation: A Survey**  
> Song Yan, Wei Zhai, Chenfeng Wang, Ruixuan Li, Zhangping Yang, Yancheng Cai, Tao Zhang, Ling Wang, Yunwei Lan, Yujie He, Yang Cao, Min Li, and Zheng-Jun Zha.  
> *Preprints*, 2026 · [Paper](https://www.preprints.org/manuscript/202606.0870/v1) · [DOI](https://doi.org/10.20944/preprints202606.0870.v1)

Diffusion models now support text-to-image synthesis, editing, personalization, video generation, and 3D-aware content creation. Visual fidelity alone, however, does not guarantee that an output follows its prompt, preserves identity, remains coherent over time or viewpoint, or satisfies safety and physical-plausibility requirements.

The survey organizes these failures through a single question:

> **What should a generated visual output agree with?**

Its answer is a relation-based taxonomy of **external**, **internal**, and **normative** consistency. The repository turns this taxonomy into a navigable literature map covering representative methods, benchmarks, evaluators, datasets, and diagnostic resources.

### Key contributions

1. **Relation-based taxonomy** — organizes consistency according to the target of agreement rather than only by task or modality.
2. **Evaluation protocol abstraction** — separates observation units, agreement targets, evidence sources, and evaluation outputs.
3. **Optimization-locus analysis** — compares where consistency is imposed: before sampling, at the condition interface, during denoising, across coupled outputs, or after generation.
4. **Machine-readable resource map** — provides structured CSV and BibTeX files for maintenance, comparison, and downstream analysis.

<p align="center">
  <img src="https://img.shields.io/badge/Resources-355-4c78a8?style=flat-square" alt="355 resources">
  <img src="https://img.shields.io/badge/Methods-225-59a14f?style=flat-square" alt="225 methods">
  <img src="https://img.shields.io/badge/Benchmarks%20%26%20Evaluators-70-f28e2b?style=flat-square" alt="70 benchmarks and evaluators">
  <img src="https://img.shields.io/badge/Datasets%20%26%20Data-60-e15759?style=flat-square" alt="60 datasets and data resources">
</p>

---

## Taxonomy

<p align="center">
  <a href="paper/Cons_01.png">
    <img src="paper/Cons_01.png" width="96%" alt="Three consistency relations in diffusion-based visual generation">
  </a>
</p>

<p align="center"><sub><b>Figure 1.</b> Three consistency relations in diffusion-based visual generation.</sub></p>

| Relation | Agreement target | Representative failures | Typical settings | Resources |
|---|---|---|---|---:|
| **External consistency** | Prompts, references, layouts, masks, poses, controls, and editing instructions | Prompt omission, attribute-binding error, counting error, control mismatch, over-editing | Text-to-image generation, structural control, editing, inpainting, virtual try-on, typography | **125** |
| **Internal consistency** | Generated subjects, views, frames, shots, instances, and story states | Identity drift, view inconsistency, temporal flicker, state forgetting, narrative discontinuity | Personalization, multi-view/3D generation, video generation, story visualization | **123** |
| **Normative consistency** | Preference, safety, fairness, physical plausibility, commonsense, and causal/world-state criteria | Low preference, unsafe output, benign-capability loss, physical violation, causal failure | Preference optimization, safety editing, concept erasure, physical and world-model evaluation | **107** |

The categories are conceptually distinct but practically entangled. A method may address several relations simultaneously; the repository places it according to its **primary agreement target** while retaining its broader diagnostic role in the description and coverage files.

---

## Evaluation and optimization

<table>
<tr>
<td width="50%" valign="top" align="center">
  <a href="paper/Eval_01.png"><img src="paper/Eval_01.png" width="100%" alt="Evaluation protocol for consistency claims"></a>
</td>
<td width="50%" valign="top" align="center">
  <a href="paper/Optimize_01.png"><img src="paper/Optimize_01.png" width="100%" alt="Optimization loci for enforcing consistency"></a>
</td>
</tr>
<tr>
<td valign="top">
  <b>Evaluation view.</b> A consistency claim should specify the observation unit, agreement target, evidence source, and evaluation output. This prevents sequence-level claims from being supported only by frame-level evidence, or specific alignment claims from being reduced to broad preference scores.
</td>
<td valign="top">
  <b>Optimization view.</b> Consistency can be imposed before sampling, at the condition interface, during denoising, across coupled outputs, or after generation. Each locus creates different trade-offs among persistence, controllability, realism, diversity, memory cost, and modularity.
</td>
</tr>
</table>

---

## Resource collection

The collection is designed as a **topic-oriented literature map**, not a flat bibliography. Resources are first grouped by their primary consistency relation and then divided into focused research themes. All lists are fully expanded to support browser search, direct linking, and rapid visual scanning.

| Consistency relation | Methods | Benchmarks & Evaluators | Datasets & Data | Total | Browse |
|---|---:|---:|---:|---:|---:|
| **External consistency** | 85 | 20 | 20 | **125** | [Open section](#external-consistency) |
| **Internal consistency** | 83 | 20 | 20 | **123** | [Open section](#internal-consistency) |
| **Normative consistency** | 57 | 30 | 20 | **107** | [Open section](#normative-consistency) |
| **Collection** | **225** | **70** | **60** | **355** | — |

### Entry format

Each resource is presented with a prominent title, compact venue/year metadata, and a separate one-line description:

- **Resource title** <sub>venue / year</sub>  
  The consistency issue, mechanism, or diagnostic role addressed by the resource.

> [!NOTE]
> Recent papers may temporarily be labeled **arXiv**, **project**, or **venue TBD** until stable proceedings metadata becomes available. Official paper repositories and project pages are preferred over unofficial reimplementations.

---

<a id="external-consistency"></a>
## 01 · External consistency

> **Agreement target —** Agreement with externally specified conditions.  
> **Scope —** Prompts, layouts, boxes, masks, depth maps, poses, reference images, editing instructions, and other user- or task-provided controls.

<p align="center">
  <a href="#external-methods"><img src="https://img.shields.io/badge/Methods-85-4c78a8?style=flat-square" alt="85 methods"></a>
  <a href="#external-benchmarks"><img src="https://img.shields.io/badge/Benchmarks%20%26%20Evaluators-20-4c78a8?style=flat-square" alt="20 benchmarks and evaluators"></a>
  <a href="#external-datasets"><img src="https://img.shields.io/badge/Datasets%20%26%20Data-20-4c78a8?style=flat-square" alt="20 datasets and data resources"></a>
  <img src="https://img.shields.io/badge/Total-125-4c78a8?style=flat-square" alt="125 total resources">
</p>

| Resource type | Description | Jump |
|---|---|---:|
| **Methods** | Architectures, objectives, inference procedures, and intervention mechanisms. | [Browse 85](#external-methods) |
| **Benchmarks & Evaluators** | Test suites, metrics, learned scorers, and evaluation protocols. | [Browse 20](#external-benchmarks) |
| **Datasets & Data Resources** | Training corpora, annotations, prompt sets, and diagnostic data. | [Browse 20](#external-datasets) |

<a id="external-methods"></a>
### Methods

<p><sub><b>85 resources</b> organized into 6 focused topics.</sub></p>

| Topic | Coverage |
|---|---:|
| [Prompt following & compositional generation](#external-methods-prompt-following-and-compositional-generation) | **20** |
| [Spatial grounding & structural control](#external-methods-spatial-grounding-and-structural-control) | **24** |
| [Guidance, inversion & image editing](#external-methods-guidance-inversion-and-image-editing) | **26** |
| [Typography & visual text](#external-methods-typography-and-visual-text) | **5** |
| [Virtual try-on & dressing](#external-methods-virtual-try-on-and-dressing) | **7** |
| [Posters & graphic design](#external-methods-posters-and-graphic-design) | **3** |

<a id="external-methods-prompt-following-and-compositional-generation"></a>
#### Prompt following & compositional generation <sup>20</sup>

<sub>Foundational text-conditioned models, semantic binding, prompt planning, and prompt refinement.</sub>

- **[GLIDE](https://arxiv.org/abs/2112.10741)** <sub>arXiv 2022</sub>  
  Early text-guided diffusion model supporting prompt-conditioned generation and editing.
- **[Imagen](https://arxiv.org/abs/2205.11487)** <sub>NeurIPS 2022 / arXiv</sub>  
  High-fidelity text-to-image diffusion model emphasizing language understanding.
- **[Latent Diffusion Models](https://arxiv.org/abs/2112.10752)** <sub>CVPR 2022</sub>  
  Latent-space diffusion backbone widely used for controllable generation and editing.
- **[Composable Diffusion Models](https://arxiv.org/abs/2206.01714)** <sub>ECCV 2022</sub>  
  Combines multiple diffusion score functions for compositional generation.
- **[Structured Diffusion Guidance](https://arxiv.org/abs/2212.05032)** <sub>arXiv 2022</sub>  
  Uses structured guidance signals to improve prompt-object alignment. (same work as StructureDiffusion)
- **[StructureDiffusion](https://arxiv.org/abs/2212.05032)** <sub>arXiv 2022</sub>  
  Parses prompts into structured representations to improve compositional text-to-image generation.
- **[Attend-and-Excite](https://github.com/yuval-alaluf/Attend-and-Excite)** <sub>SIGGRAPH 2023</sub>  
  Manipulates cross-attention maps to reduce missing objects and improve prompt coverage [Paper](https://arxiv.org/abs/2301.13826)
- **[BoxDiff](https://github.com/showlab/BoxDiff)** <sub>ICCV 2023</sub>  
  Training-free box-constrained generation for spatially grounded text-to-image synthesis [Paper](https://arxiv.org/abs/2304.14361)
- **[Composer](https://github.com/damo-vilab/composer)** <sub>ICML 2023</sub>  
  Composes heterogeneous visual conditions for controllable image synthesis [Paper](https://arxiv.org/abs/2302.09778)
- **[MultiDiffusion](https://multidiffusion.github.io/)** <sub>ICML 2023</sub>  
  Fuses multiple diffusion paths to satisfy spatial and regional generation constraints.
- **[LLM-grounded Diffusion](https://llm-grounded-diffusion.github.io/)** <sub>ICLR 2024</sub>  
  Uses LLM planning to turn complex prompts into layout-grounded generation constraints.
- **[SynGen](https://arxiv.org/abs/2308.07037)** <sub>ICCV 2023</sub>  
  Uses syntactic guidance to improve compositional text-to-image generation.
- **[RPG: Recaption, Plan, and Generate](https://github.com/YangLing0818/RPG-DiffusionMaster)** <sub>arXiv 2024</sub>  
  Uses MLLM-based recaptioning and planning for complex prompt following [Paper](https://arxiv.org/abs/2312.03701)
- **[CONFORM](https://arxiv.org/abs/2309.14773)** <sub>arXiv / venue TBD</sub>  
  Improves object-attribute alignment through contrastive or correspondence-driven prompt grounding.
- **[Divide-and-Bind](https://arxiv.org/abs/2308.06769)** <sub>arXiv / venue TBD</sub>  
  Decomposes complex prompts and binds objects to attributes or relations.
- **[Linguistic Binding in Diffusion](https://arxiv.org/abs/2308.06769)** <sub>arXiv / venue TBD</sub>  
  Studies or improves language-binding failures in text-to-image diffusion.
- **[Promptist](https://arxiv.org/abs/2212.09611)** <sub>arXiv 2022</sub>  
  Optimizes prompts to improve text-to-image generation quality and alignment.
- **[BeautifulPrompt](https://arxiv.org/abs/2312.07358)** <sub>AAAI 2024 / arXiv</sub>  
  Refines user prompts for stronger image generation quality and faithfulness.
- **[Prompt Expansion for Text-to-Image](https://arxiv.org/search/?query=prompt+expansion+text+to+image+diffusion&searchtype=all)** <sub>topic / resource</sub>  
  Expands underspecified prompts to reduce ambiguity in generation.
- **[Prompt Decomposition for T2I](https://arxiv.org/search/?query=prompt+decomposition+text-to-image+evaluation&searchtype=all)** <sub>topic / resource</sub>  
  Decomposes prompts into atomic semantic constraints for evaluation or guidance.

<p align="right"><a href="#external-methods">Back to methods ↑</a></p>

---

<a id="external-methods-spatial-grounding-and-structural-control"></a>
#### Spatial grounding & structural control <sup>24</sup>

<sub>Boxes, layouts, adapters, scene graphs, masks, poses, and other explicit control interfaces.</sub>

- **[ControlNet](https://github.com/lllyasviel/ControlNet)** <sub>ICCV 2023</sub>  
  Adds trainable side branches for depth, edge, pose, segmentation, and other controls [Paper](https://arxiv.org/abs/2302.05543)
- **[GLIGEN](https://github.com/gligen/GLIGEN)** <sub>CVPR 2023</sub>  
  Grounds generation with boxes and phrase-level grounding tokens [Paper](https://arxiv.org/abs/2301.07093)
- **[T2I-Adapter](https://github.com/TencentARC/T2I-Adapter)** <sub>AAAI 2024</sub>  
  Uses lightweight adapters for structural conditions such as sketch, depth, and pose [Paper](https://arxiv.org/abs/2302.08453)
- **[IP-Adapter](https://github.com/tencent-ailab/IP-Adapter)** <sub>arXiv 2023</sub>  
  Adds image-prompt conditioning while preserving text compatibility [Paper](https://arxiv.org/abs/2308.06721)
- **[AnyDoor](https://github.com/ali-vilab/AnyDoor)** <sub>CVPR 2024</sub>  
  Performs zero-shot object-level customization and insertion [Paper](https://arxiv.org/abs/2307.09481)
- **[FreeDoM](https://github.com/vvictoryuki/FreeDoM)** <sub>ICCV 2023</sub>  
  Applies training-free energy guidance for conditional diffusion tasks [Paper](https://arxiv.org/abs/2303.16747)
- **[HumanSD](https://github.com/IDEA-Research/HumanSD)** <sub>ICCV 2023</sub>  
  Generates human images under native skeleton guidance [Paper](https://arxiv.org/abs/2303.16747)
- **[UniControl](https://arxiv.org/abs/2305.11147)** <sub>NeurIPS 2023 / arXiv</sub>  
  Provides a unified framework for multiple controllable generation signals.
- **[Uni-ControlNet](https://arxiv.org/abs/2305.16322)** <sub>arXiv 2023</sub>  
  Unifies multi-condition ControlNet-style conditioning.
- **[Ctrl-Adapter](https://openreview.net/forum?id=ny8T8OuNHe)** <sub>ICLR 2025</sub>  
  Uses efficient adapters for diverse spatial and structural controls.
- **[UniCon](https://openreview.net/forum?id=8jb0e1gLyd)** <sub>ICLR 2025</sub>  
  Designs unidirectional information flow for stronger large-scale condition control.
- **[InstanceDiffusion](https://people.eecs.berkeley.edu/~xdwang/projects/instancediffusion/)** <sub>CVPR 2024</sub>  
  Supports instance-level control over object placement and attributes.
- **[ControlNet++](https://arxiv.org/abs/2312.04462)** <sub>arXiv / venue TBD</sub>  
  Improves ControlNet-style conditioning quality and efficiency.
- **[ControlNet-XS](https://arxiv.org/abs/2312.05773)** <sub>arXiv / venue TBD</sub>  
  Compresses controllable generation modules for efficient deployment.
- **[ControlLoRA](https://arxiv.org/abs/2402.06551)** <sub>arXiv / venue TBD</sub>  
  Uses LoRA-style lightweight control adaptation.
- **[SparseCtrl](https://arxiv.org/abs/2311.16933)** <sub>arXiv / venue TBD</sub>  
  Controls image/video generation from sparse visual conditions.
- **[SemanticControl](https://arxiv.org/search/?query=SemanticControl+diffusion&searchtype=all)** <sub>arXiv / venue TBD</sub>  
  Handles loose or weakly aligned semantic controls.
- **[LayoutDiffusion](https://arxiv.org/abs/2303.08271)** <sub>CVPR 2023 / arXiv</sub>  
  Conditions diffusion generation on layout annotations.
- **[LayoutDM](https://arxiv.org/abs/2303.17189)** <sub>CVPR 2023 / arXiv</sub>  
  Models layout-to-image synthesis through diffusion.
- **[SceneComposer](https://arxiv.org/abs/2312.08914)** <sub>arXiv / venue TBD</sub>  
  Composes scene-level controls for complex generation.
- **[Scene Graph Diffusion](https://arxiv.org/abs/2305.05298)** <sub>arXiv / venue TBD</sub>  
  Uses scene graphs for relation-aware image synthesis.
- **[DetDiffusion](https://arxiv.org/abs/2308.06355)** <sub>arXiv / venue TBD</sub>  
  Integrates detection-like constraints into image generation.
- **[Grounded Diffusion](https://arxiv.org/search/?query=grounded+diffusion+text+to+image&searchtype=all)** <sub>topic / resource</sub>  
  General family of grounding-based diffusion methods.
- **[SAM-guided Diffusion Editing](https://arxiv.org/search/?query=SAM+guided+diffusion+editing&searchtype=all)** <sub>topic / resource</sub>  
  Uses segmentation masks to localize editing constraints.

<p align="right"><a href="#external-methods">Back to methods ↑</a></p>

---

<a id="external-methods-guidance-inversion-and-image-editing"></a>
#### Guidance, inversion & image editing <sup>26</sup>

<sub>Sampling-time guidance, inversion, instruction editing, drag editing, and localized inpainting.</sub>

- **[Diffusion Posterior Sampling](https://arxiv.org/abs/2209.14687)** <sub>ICLR 2023</sub>  
  Uses measurement likelihoods to guide inverse-problem diffusion.
- **[Universal Guidance for Diffusion Models](https://arxiv.org/abs/2302.07121)** <sub>ICML 2023 Workshop</sub>  
  Applies generic guidance losses during sampling.
- **[Classifier Guidance](https://arxiv.org/abs/2105.05233)** <sub>NeurIPS 2021</sub>  
  Uses classifier gradients to steer diffusion samples.
- **[Classifier-Free Guidance](https://arxiv.org/abs/2207.12598)** <sub>NeurIPS 2021 workshop / arXiv</sub>  
  Steers conditional generation without an external classifier.
- **[SDEdit](https://arxiv.org/abs/2108.01073)** <sub>ICLR 2022</sub>  
  Edits images by adding noise and denoising under new guidance.
- **[Prompt-to-Prompt](https://github.com/google/prompt-to-prompt)** <sub>ICLR 2023</sub>  
  Controls cross-attention to edit prompts while preserving layout/content [Paper](https://arxiv.org/abs/2208.01626)
- **[Null-Text Inversion](https://null-text-inversion.github.io/)** <sub>CVPR 2023</sub>  
  Inverts real images for more faithful prompt-based editing.
- **[DiffEdit](https://github.com/Xiang-cd/DiffEdit-stable-diffusion)** <sub>ICLR 2023</sub>  
  Computes semantic edit masks from prompt differences [Paper](https://arxiv.org/abs/2210.11427)
- **[InstructPix2Pix](https://github.com/timothybrooks/instruct-pix2pix)** <sub>CVPR 2023</sub>  
  Trains a diffusion editor to follow natural-language instructions [Paper](https://arxiv.org/abs/2211.09800)
- **[InstructDiffusion](https://github.com/cientgu/InstructDiffusion)** <sub>CVPR 2024</sub>  
  Unifies several visual instruction tasks in diffusion models [Paper](https://arxiv.org/abs/2309.12498)
- **[Imagic](https://imagic-editing.github.io/)** <sub>CVPR 2023</sub>  
  Edits real images by optimizing text embeddings and model weights.
- **[Paint-by-Example](https://github.com/Fantasy-Studio/Paint-by-Example)** <sub>CVPR 2023</sub>  
  Uses exemplar images to guide localized editing [Paper](https://arxiv.org/abs/2211.13227)
- **[Plug-and-Play Diffusion Features](https://pnp-diffusion.github.io/)** <sub>CVPR 2023</sub>  
  Injects diffusion features to preserve structure during editing.
- **[Pix2Pix-Zero](https://pix2pixzero.github.io/)** <sub>ICCV 2023</sub>  
  Performs zero-shot image-to-image translation through cross-attention guidance.
- **[MasaCtrl](https://github.com/TencentARC/MasaCtrl)** <sub>ICCV 2023</sub>  
  Uses mutual self-attention to preserve structure across synthesis/editing [Paper](https://arxiv.org/abs/2304.08465)
- **[LEDITS++](https://arxiv.org/abs/2311.16711)** <sub>arXiv 2023</sub>  
  Performs lightweight semantic editing and concept erasure.
- **[DragonDiffusion](https://github.com/MC-E/DragonDiffusion)** <sub>ICLR 2024 / arXiv</sub>  
  Supports object moving, resizing, and fine-grained interactive editing [Paper](https://arxiv.org/abs/2307.02421)
- **[DragDiffusion](https://github.com/Yujun-Shi/DragDiffusion)** <sub>CVPR 2024</sub>  
  Enables point-based drag editing with diffusion priors [Paper](https://arxiv.org/abs/2306.14435)
- **[FreeDrag](https://arxiv.org/abs/2307.08376)** <sub>CVPR 2024 / arXiv</sub>  
  Improves drag editing without model finetuning.
- **[DiffEditor](https://arxiv.org/abs/2312.08668)** <sub>arXiv / venue TBD</sub>  
  Provides an editing pipeline for localized diffusion modifications.
- **[SEGA](https://arxiv.org/abs/2301.12247)** <sub>arXiv 2023</sub>  
  Steers semantic directions during diffusion sampling.
- **[Emu Edit](https://arxiv.org/abs/2311.10089)** <sub>CVPR 2024 / arXiv</sub>  
  Uses instruction data for high-quality image editing.
- **[SmartEdit](https://arxiv.org/abs/2312.06739)** <sub>CVPR 2024 / arXiv</sub>  
  Combines MLLMs and diffusion for instruction-based editing.
- **[BrushNet](https://arxiv.org/abs/2403.06976)** <sub>ECCV 2024 / arXiv</sub>  
  Adds a dedicated inpainting branch for masked image editing.
- **[PowerPaint](https://arxiv.org/abs/2312.00028)** <sub>ECCV 2024 / arXiv</sub>  
  Supports versatile object removal, insertion, and inpainting.
- **[Inpaint Anything](https://arxiv.org/abs/2304.06790)** <sub>arXiv 2023</sub>  
  Combines segmentation and diffusion inpainting.

<p align="right"><a href="#external-methods">Back to methods ↑</a></p>

---

<a id="external-methods-typography-and-visual-text"></a>
#### Typography & visual text <sup>5</sup>

<sub>Text rendering, multilingual typography, glyph conditioning, and text-aware editing.</sub>

- **[TextDiffuser](https://arxiv.org/abs/2305.10855)** <sub>NeurIPS 2023</sub>  
  Improves text rendering inside generated images.
- **[TextDiffuser-2](https://arxiv.org/abs/2311.16465)** <sub>arXiv 2023</sub>  
  Improves multilingual and layout-aware text rendering.
- **[AnyText](https://arxiv.org/abs/2311.03054)** <sub>ICLR 2024</sub>  
  Generates and edits multilingual text in images.
- **[GlyphDraw](https://arxiv.org/abs/2303.17870)** <sub>NeurIPS 2023 / arXiv</sub>  
  Uses glyph-level information for visual text generation.
- **[GlyphControl](https://arxiv.org/abs/2306.02586)** <sub>arXiv / venue TBD</sub>  
  Adds explicit glyph constraints for controllable typography.

<p align="right"><a href="#external-methods">Back to methods ↑</a></p>

---

<a id="external-methods-virtual-try-on-and-dressing"></a>
#### Virtual try-on & dressing <sup>7</sup>

<sub>Garment preservation, person–garment alignment, and generalized dressing constraints.</sub>

- **[TryOnDiffusion](https://arxiv.org/abs/2306.08276)** <sub>CVPR 2023</sub>  
  Uses diffusion for virtual try-on with garment-person consistency.
- **[StableVITON](https://github.com/rlawjdghek/StableVITON)** <sub>CVPR 2024</sub>  
  Adapts stable diffusion to virtual try-on [Paper](https://arxiv.org/abs/2312.01725)
- **[IDM-VTON](https://github.com/yisol/IDM-VTON)** <sub>ECCV 2024</sub>  
  Improves image-based virtual try-on with diffusion [Paper](https://arxiv.org/abs/2403.05142)
- **[CatVTON](https://github.com/Zheng-Chong/CatVTON)** <sub>arXiv 2024</sub>  
  Provides a lightweight virtual try-on framework [Paper](https://arxiv.org/abs/2407.15886)
- **[OOTDiffusion](https://github.com/levihsu/OOTDiffusion)** <sub>arXiv 2024</sub>  
  Generates outfits and try-on images under reference constraints [Paper](https://arxiv.org/abs/2403.01746)
- **[LaDI-VTON](https://arxiv.org/abs/2305.13501)** <sub>ACM MM 2023 / arXiv</sub>  
  Uses latent diffusion for virtual try-on.
- **[AnyDressing](https://arxiv.org/abs/2412.04146)** <sub>arXiv / venue TBD</sub>  
  Handles generalized dressing and garment transfer constraints.

<p align="right"><a href="#external-methods">Back to methods ↑</a></p>

---

<a id="external-methods-posters-and-graphic-design"></a>
#### Posters & graphic design <sup>3</sup>

<sub>Layout-aware poster generation and structured graphic composition.</sub>

- **[PosterCraft](https://arxiv.org/abs/2403.05537)** <sub>arXiv / venue TBD</sub>  
  Studies layout- and text-aware poster generation.
- **[CreatiPoster](https://arxiv.org/abs/2506.10890)** <sub>arXiv / venue TBD</sub>  
  Generates visually structured poster layouts.
- **[PosterMaker](https://arxiv.org/abs/2504.06632)** <sub>arXiv / venue TBD</sub>  
  Uses diffusion for controllable poster design.

<p align="right"><a href="#external-methods">Back to methods ↑</a></p>


<a id="external-benchmarks"></a>
### Benchmarks & Evaluators

<p><sub><b>20 resources</b> organized into 4 focused topics.</sub></p>

| Topic | Coverage |
|---|---:|
| [General prompt fidelity & composition](#external-benchmarks-general-prompt-fidelity-and-composition) | **11** |
| [Editing & learned-concept evaluation](#external-benchmarks-editing-and-learned-concept-evaluation) | **2** |
| [Fine-grained semantic diagnostics](#external-benchmarks-fine-grained-semantic-diagnostics) | **5** |
| [Domain-specific control evaluation](#external-benchmarks-domain-specific-control-evaluation) | **2** |

<a id="external-benchmarks-general-prompt-fidelity-and-composition"></a>
#### General prompt fidelity & composition <sup>11</sup>

<sub>Broad prompt-following, semantic alignment, and compositional evaluation protocols.</sub>

- **[TIFA](https://arxiv.org/search/?query=object+attribute+benchmark+text+to+image&searchtype=all)** <sub>ICCV 2023</sub>  
  Evaluates prompt faithfulness using generated question-answer pairs.
- **[GenEval](https://arxiv.org/abs/2305.05298)** <sub>NeurIPS 2023 workshop / arXiv</sub>  
  Tests object presence, counting, colors, positions, and attribute binding.
- **[T2I-CompBench](https://arxiv.org/search/?query=text+rendering+benchmark+diffusion&searchtype=all)** <sub>NeurIPS 2023</sub>  
  Measures compositional alignment across attributes, relations, and complex prompts.
- **[GenEval2](https://github.com/facebookresearch/GenEval2)** <sub>arXiv / venue TBD</sub>  
  Extends prompt-following evaluation with harder and less saturated cases.
- **[HRS-Bench](https://github.com/eslambakr/HRS_benchmark)** <sub>ICCV 2023</sub>  
  Provides holistic evaluation of T2I capabilities, robustness, fairness, and bias. [Paper](https://doi.org/10.1109/ICCV51070.2023.01834)
- **[DPG-Bench](https://arxiv.org/abs/2403.05135)** <sub>arXiv 2024</sub>  
  Uses dense prompts to evaluate semantic and relation following.
- **[GenAI-Bench / VQAScore](https://github.com/linzhiqiu/t2v_metrics)** <sub>ECCV 2024</sub>  
  Evaluates text-to-visual generation through VQA-style image/video scoring.
- **[DrawBench](https://arxiv.org/abs/2205.11487)** <sub>Imagen / NeurIPS 2022 resource</sub>  
  Human-evaluation prompt suite for text-to-image generation.
- **[PartiPrompts](https://arxiv.org/abs/2206.10789)** <sub>arXiv 2022</sub>  
  Large prompt set for evaluating compositional and high-level prompt following.
- **[DSG: Davidsonian Scene Graph evaluation](https://arxiv.org/abs/2310.01257)** <sub>arXiv / venue TBD</sub>  
  Converts prompts to scene-graph-like checks for semantic consistency.
- **[VIEScore](https://arxiv.org/abs/2310.01257)** <sub>arXiv / venue TBD</sub>  
  Uses vision-language evaluators for image-text alignment.

<p align="right"><a href="#external-benchmarks">Back to benchmarks & evaluators ↑</a></p>

---

<a id="external-benchmarks-editing-and-learned-concept-evaluation"></a>
#### Editing & learned-concept evaluation <sup>2</sup>

<sub>Evaluation of edit preservation, instruction compliance, and reusable concept learning.</sub>

- **[EditBench](https://arxiv.org/abs/2211.09494)** <sub>CVPR 2023</sub>  
  Benchmarks text-guided image inpainting and edit preservation.
- **[ConceptBed](https://github.com/ConceptBed/evaluations)** <sub>arXiv / venue TBD</sub>  
  Evaluates concept learning and reusable concept binding.

<p align="right"><a href="#external-benchmarks">Back to benchmarks & evaluators ↑</a></p>

---

<a id="external-benchmarks-fine-grained-semantic-diagnostics"></a>
#### Fine-grained semantic diagnostics <sup>5</sup>

<sub>Targeted tests for counting, spatial relations, attribute binding, relations, and typography.</sub>

- **[CountBench](https://arxiv.org/search/?query=counting+benchmark+text+to+image&searchtype=all)** <sub>resource / venue TBD</sub>  
  Tests numerical object-counting consistency in generated images.
- **[SpatialBench](https://arxiv.org/search/?query=spatial+relation+benchmark+text+to+image&searchtype=all)** <sub>resource / venue TBD</sub>  
  Tests spatial relation following.
- **[ObjectAttributeBench](https://arxiv.org/search/?query=object+attribute+benchmark+text+to+image&searchtype=all)** <sub>resource / venue TBD</sub>  
  Tests object-attribute binding.
- **[RelationBench](https://arxiv.org/search/?query=relation+benchmark+text+to+image+diffusion&searchtype=all)** <sub>resource / venue TBD</sub>  
  Tests relational semantics in text-to-image generation.
- **[TypographyBench](https://arxiv.org/search/?query=text+rendering+benchmark+diffusion&searchtype=all)** <sub>resource / venue TBD</sub>  
  Evaluates rendered text accuracy in generated images.

<p align="right"><a href="#external-benchmarks">Back to benchmarks & evaluators ↑</a></p>

---

<a id="external-benchmarks-domain-specific-control-evaluation"></a>
#### Domain-specific control evaluation <sup>2</sup>

<sub>Specialized protocols for virtual try-on and pose-conditioned generation.</sub>

- **[VTON evaluation suites](https://arxiv.org/search/?query=virtual+try-on+benchmark+diffusion&searchtype=all)** <sub>resource</sub>  
  Evaluate garment preservation and person-garment alignment.
- **[Human pose generation evaluation](https://arxiv.org/search/?query=human+pose+conditioned+diffusion+benchmark&searchtype=all)** <sub>resource</sub>  
  Evaluates pose-conditioned human generation.

<p align="right"><a href="#external-benchmarks">Back to benchmarks & evaluators ↑</a></p>


<a id="external-datasets"></a>
### Datasets & Data Resources

<p><sub><b>20 resources</b> organized into 5 focused topics.</sub></p>

| Topic | Coverage |
|---|---:|
| [Instruction-guided editing](#external-datasets-instruction-guided-editing) | **2** |
| [Captioning, grounding & compositional reasoning](#external-datasets-captioning-grounding-and-compositional-reasoning) | **7** |
| [Web-scale image–text pretraining](#external-datasets-web-scale-image-text-pretraining) | **4** |
| [Segmentation & object-level control](#external-datasets-segmentation-and-object-level-control) | **2** |
| [Fashion, pose & typography](#external-datasets-fashion-pose-and-typography) | **5** |

<a id="external-datasets-instruction-guided-editing"></a>
#### Instruction-guided editing <sup>2</sup>

<sub>Data for natural-language image editing and multi-turn edit supervision.</sub>

- **[MagicBrush](https://github.com/OSU-NLP-Group/MagicBrush)** <sub>NeurIPS 2023 Datasets and Benchmarks</sub>  
  Instruction-guided image editing dataset with multi-turn annotations.
- **[InstructPix2Pix dataset](https://github.com/timothybrooks/instruct-pix2pix)** <sub>CVPR 2023 resource</sub>  
  Synthetic instruction-edit pairs for image editing [Paper](https://arxiv.org/abs/2211.09800)

<p align="right"><a href="#external-datasets">Back to datasets & data resources ↑</a></p>

---

<a id="external-datasets-captioning-grounding-and-compositional-reasoning"></a>
#### Captioning, grounding & compositional reasoning <sup>7</sup>

<sub>Caption, region, relation, referring-expression, VQA, and synthetic reasoning annotations.</sub>

- **[COCO Captions](https://cocodataset.org/)** <sub>ECCV 2014 / dataset</sub>  
  Common image-caption source for prompt grounding.
- **[Visual Genome](https://homes.cs.washington.edu/~ranjay/visualgenome/)** <sub>IJCV 2017 / dataset</sub>  
  Dense object, attribute, and relation annotations.
- **[OpenImages](https://storage.googleapis.com/openimages/web/index.html)** <sub>dataset</sub>  
  Large-scale object and visual relationship annotations.
- **[ADE20K](https://groups.csail.mit.edu/vision/datasets/ADE20K/)** <sub>CVPR 2017 / dataset</sub>  
  Scene parsing annotations for structural control.
- **[RefCOCO](https://arxiv.org/abs/2406.16866)** <sub>dataset</sub>  
  Referring-expression grounding resource.
- **[GQA](https://cs.stanford.edu/people/dorarad/gqa/)** <sub>CVPR 2019 / dataset</sub>  
  Visual-question-answering resource for compositional reasoning.
- **[CLEVR](https://cs.stanford.edu/people/jcjohns/clevr/)** <sub>CVPR 2017 / dataset</sub>  
  Synthetic compositional reasoning dataset.

<p align="right"><a href="#external-datasets">Back to datasets & data resources ↑</a></p>

---

<a id="external-datasets-web-scale-image-text-pretraining"></a>
#### Web-scale image–text pretraining <sup>4</sup>

<sub>Large image–text corpora and aesthetic-filtered pretraining resources.</sub>

- **[LAION-5B](https://laion.ai/blog/laion-5b/)** <sub>NeurIPS 2022 Datasets and Benchmarks</sub>  
  Web-scale image-text pretraining data.
- **[LAION-Aesthetics](https://laion.ai/blog/laion-aesthetics/)** <sub>dataset resource</sub>  
  Aesthetic-filtered image-text data.
- **[CC3M](https://ai.google.com/research/ConceptualCaptions/)** <sub>ACL 2018 / dataset</sub>  
  Web image-caption data for vision-language pretraining.
- **[CC12M](https://github.com/google-research-datasets/conceptual-12m)** <sub>CVPR 2021 / dataset</sub>  
  Larger conceptual-caption dataset.

<p align="right"><a href="#external-datasets">Back to datasets & data resources ↑</a></p>

---

<a id="external-datasets-segmentation-and-object-level-control"></a>
#### Segmentation & object-level control <sup>2</sup>

<sub>Mask, instance, and long-tail object annotations for localized control.</sub>

- **[SA-1B](https://segment-anything.com/dataset/index.html)** <sub>ICCV 2023 / dataset</sub>  
  Large-scale segmentation masks for editing and control.
- **[LVIS](https://www.lvisdataset.org/)** <sub>CVPR 2019 / dataset</sub>  
  Long-tail instance annotations for object-level diagnostics.

<p align="right"><a href="#external-datasets">Back to datasets & data resources ↑</a></p>

---

<a id="external-datasets-fashion-pose-and-typography"></a>
#### Fashion, pose & typography <sup>5</sup>

<sub>Domain-specific supervision for dressing, human pose, and visual text generation.</sub>

- **[DeepFashion](http://mmlab.ie.cuhk.edu.hk/projects/DeepFashion.html)** <sub>CVPR 2016 / dataset</sub>  
  Fashion data for virtual try-on and garment consistency.
- **[VITON-HD](https://github.com/shadow2496/VITON-HD)** <sub>CVPR 2021 workshop / dataset</sub>  
  High-resolution virtual try-on data.
- **[DressCode](https://github.com/aimagelab/dress-code)** <sub>CVPR 2022 / dataset</sub>  
  Multi-category virtual try-on dataset.
- **[OpenPose / pose datasets](https://arxiv.org/search/?query=pose+dataset+human+image+generation&searchtype=all)** <sub>resource</sub>  
  Pose supervision for human-conditioned generation.
- **[OCR/text rendering corpora](https://arxiv.org/search/?query=text+rendering+dataset+image+generation&searchtype=all)** <sub>resource</sub>  
  Text-image data for typography generation.

<p align="right"><a href="#external-datasets">Back to datasets & data resources ↑</a></p>


<p align="right"><a href="#resource-collection">Back to resource index ↑</a> · <a href="#top">Back to top ↑</a></p>

---
<a id="internal-consistency"></a>
## 02 · Internal consistency

> **Agreement target —** Agreement among generated states.  
> **Scope —** Subjects, identities, views, frames, shots, scenes, instances, and story states that should remain mutually compatible.

<p align="center">
  <a href="#internal-methods"><img src="https://img.shields.io/badge/Methods-83-7b61a8?style=flat-square" alt="83 methods"></a>
  <a href="#internal-benchmarks"><img src="https://img.shields.io/badge/Benchmarks%20%26%20Evaluators-20-7b61a8?style=flat-square" alt="20 benchmarks and evaluators"></a>
  <a href="#internal-datasets"><img src="https://img.shields.io/badge/Datasets%20%26%20Data-20-7b61a8?style=flat-square" alt="20 datasets and data resources"></a>
  <img src="https://img.shields.io/badge/Total-123-7b61a8?style=flat-square" alt="123 total resources">
</p>

| Resource type | Description | Jump |
|---|---|---:|
| **Methods** | Architectures, objectives, inference procedures, and intervention mechanisms. | [Browse 83](#internal-methods) |
| **Benchmarks & Evaluators** | Test suites, metrics, learned scorers, and evaluation protocols. | [Browse 20](#internal-benchmarks) |
| **Datasets & Data Resources** | Training corpora, annotations, prompt sets, and diagnostic data. | [Browse 20](#internal-datasets) |

<a id="internal-methods"></a>
### Methods

<p><sub><b>83 resources</b> organized into 6 focused topics.</sub></p>

| Topic | Coverage |
|---|---:|
| [Personalized concepts & subject identity](#internal-methods-personalized-concepts-and-subject-identity) | **21** |
| [Characters, style & cross-instance consistency](#internal-methods-characters-style-and-cross-instance-consistency) | **11** |
| [Multi-view & 3D consistency](#internal-methods-multi-view-and-3d-consistency) | **17** |
| [Video generation & temporal editing](#internal-methods-video-generation-and-temporal-editing) | **21** |
| [Long-form stories & interactive video](#internal-methods-long-form-stories-and-interactive-video) | **7** |
| [Personalized video & human animation](#internal-methods-personalized-video-and-human-animation) | **6** |

<a id="internal-methods-personalized-concepts-and-subject-identity"></a>
#### Personalized concepts & subject identity <sup>21</sup>

<sub>Concept inversion, parameter-efficient personalization, and identity-preserving generation.</sub>

- **[Textual Inversion](https://github.com/rinongal/textual_inversion)** <sub>ICLR 2023</sub>  
  Learns new textual tokens for personalized concepts [Paper](https://arxiv.org/abs/2208.01618)
- **[DreamBooth](https://dreambooth.github.io/)** <sub>CVPR 2023</sub>  
  Finetunes T2I models for subject-driven generation.
- **[Custom Diffusion](https://github.com/adobe-research/custom-diffusion)** <sub>CVPR 2023</sub>  
  Efficiently customizes multiple concepts through parameter-efficient updates [Paper](https://arxiv.org/abs/2212.04488)
- **[Perfusion](https://research.nvidia.com/labs/par/Perfusion/)** <sub>SIGGRAPH 2023</sub>  
  Uses key-locking to preserve personalized concept identity.
- **[SVDiff](https://arxiv.org/abs/2303.11305)** <sub>arXiv 2023</sub>  
  Parameter-efficient personalization via singular-vector updates.
- **[P+](https://arxiv.org/search/?query=P%2B+textual+inversion&searchtype=all)** <sub>arXiv 2023</sub>  
  Expands textual inversion representation capacity.
- **[NeTI](https://arxiv.org/search/?query=NeTI+textual+inversion&searchtype=all)** <sub>arXiv 2023</sub>  
  Uses neural textual inversion for richer concept embedding.
- **[ProSpect](https://arxiv.org/search/?query=ProSpect+personalized+diffusion&searchtype=all)** <sub>SIGGRAPH 2023 / arXiv</sub>  
  Personalizes without heavy finetuning.
- **[DisenBooth](https://arxiv.org/abs/2305.03374)** <sub>arXiv 2023</sub>  
  Disentangles identity and context for personalization.
- **[SuTI](https://arxiv.org/abs/2304.00186)** <sub>arXiv 2023</sub>  
  Scalable subject-driven text-to-image personalization.
- **[BLIP-Diffusion](https://github.com/salesforce/LAVIS/tree/main/projects/blip-diffusion)** <sub>NeurIPS 2023</sub>  
  Uses pretrained subject representations for controllable subject generation [Paper](https://arxiv.org/abs/2305.14720)
- **[ELITE](https://github.com/csyxwei/ELITE)** <sub>ICCV 2023</sub>  
  Encodes visual concepts into textual embeddings for fast personalization [Paper](https://arxiv.org/abs/2302.13848)
- **[FastComposer](https://github.com/mit-han-lab/fastcomposer)** <sub>NeurIPS 2023</sub>  
  Enables tuning-free multi-subject generation [Paper](https://arxiv.org/abs/2302.09778)
- **[Subject-Diffusion](https://github.com/OPPO-Mente-Lab/Subject-Diffusion)** <sub>ICCV 2023</sub>  
  Supports open-domain personalized subject generation [Paper](https://arxiv.org/abs/2307.08432)
- **[PhotoMaker](https://github.com/TencentARC/PhotoMaker)** <sub>CVPR 2024</sub>  
  Uses stacked ID embeddings for realistic human personalization [Paper](https://arxiv.org/abs/2312.04461)
- **[InstantID](https://github.com/InstantID/InstantID)** <sub>arXiv 2024</sub>  
  Provides zero-shot identity-preserving generation [Paper](https://arxiv.org/abs/2401.07519)
- **[IP-Adapter-FaceID](https://github.com/tencent-ailab/IP-Adapter)** <sub>arXiv 2023/2024</sub>  
  Preserves face identity through image-prompt adapters [Paper](https://arxiv.org/abs/2308.06721)
- **[PuLID](https://github.com/ToTheBeginning/PuLID)** <sub>arXiv 2024</sub>  
  Supports pure and lightning ID customization [Paper](https://arxiv.org/abs/2404.16022)
- **[InfiniteYou](https://arxiv.org/abs/2503.16418)** <sub>arXiv / venue TBD</sub>  
  Explores scalable identity-consistent personalization.
- **[RealCustom](https://arxiv.org/abs/2408.09744)** <sub>arXiv / venue TBD</sub>  
  Focuses on realistic personalized concept generation.
- **[InstantCharacter](https://arxiv.org/abs/2504.12395)** <sub>arXiv / venue TBD</sub>  
  Builds fast character-consistent generation.

<p align="right"><a href="#internal-methods">Back to methods ↑</a></p>

---

<a id="internal-methods-characters-style-and-cross-instance-consistency"></a>
#### Characters, style & cross-instance consistency <sup>11</sup>

<sub>Consistent characters, shared style, stories, and repeated identity across generated sets.</sub>

- **[ConsiStory](https://github.com/NVlabs/consistory)** <sub>arXiv 2024</sub>  
  Training-free consistent character generation across images [Paper](https://arxiv.org/abs/2402.03286)
- **[StoryDiffusion](https://github.com/HVision-NKU/StoryDiffusion)** <sub>NeurIPS 2024</sub>  
  Uses consistent self-attention for long-range image/video generation [Paper](https://arxiv.org/abs/2405.01434)
- **[StyleAligned](https://style-aligned-gen.github.io/)** <sub>SIGGRAPH 2024</sub>  
  Shares attention to preserve style across generated sets.
- **[The Chosen One](https://omriavrahami.com/the-chosen-one/)** <sub>SIGGRAPH Asia 2024</sub>  
  Generates consistent characters across text-to-image outputs.
- **[ConsistentID](https://arxiv.org/abs/2404.16771)** <sub>arXiv 2024</sub>  
  Preserves identity in portrait and character generation.
- **[CharaConsist](https://arxiv.org/abs/2507.11533)** <sub>arXiv / venue TBD</sub>  
  Studies fine-grained character consistency.
- **[MagicID](https://arxiv.org/abs/2503.12689)** <sub>arXiv / venue TBD</sub>  
  Provides ID-conditioned video customization.
- **[PersonalVideo](https://arxiv.org/abs/2411.17048)** <sub>arXiv / venue TBD</sub>  
  Customizes video generation with personalized identity.
- **[Phantom](https://arxiv.org/search/?query=Phantom+subject+consistent+video&searchtype=all)** <sub>arXiv / venue TBD</sub>  
  Explores subject-consistent video generation.
- **[Preserve and Personalize](https://rlgnswk.github.io/PreserveAndPersonalize_ProjectPage/)** <sub>ICLR 2026</sub>  
  Preserves distributional behavior while personalizing concepts.
- **[ConceptPrism](https://arxiv.org/search/?query=ConceptPrism&searchtype=all)** <sub>CVPR 2026 / project</sub>  
  Disentangles concepts for personalized diffusion.

<p align="right"><a href="#internal-methods">Back to methods ↑</a></p>

---

<a id="internal-methods-multi-view-and-3d-consistency"></a>
#### Multi-view & 3D consistency <sup>17</sup>

<sub>Novel-view synthesis, synchronized multi-view diffusion, and image-to-3D reconstruction.</sub>

- **[Zero-1-to-3](https://github.com/cvlab-columbia/zero123)** <sub>ICCV 2023</sub>  
  Generates novel views from one image [Paper](https://arxiv.org/abs/2303.11328)
- **[One-2-3-45](https://github.com/One-2-3-45/One-2-3-45)** <sub>arXiv 2023</sub>  
  Produces multi-view images and 3D assets from a single image [Paper](https://arxiv.org/abs/2306.16928)
- **[Zero123++](https://arxiv.org/abs/2310.15110)** <sub>arXiv 2023</sub>  
  Improves single-image novel-view generation.
- **[Cascade-Zero123](https://github.com/EnVision-Research/Cascade-Zero123)** <sub>arXiv 2023</sub>  
  Cascades view generation for stronger 3D consistency [Paper](https://arxiv.org/abs/2306.16928)
- **[Consistent123](https://arxiv.org/abs/2309.17261)** <sub>arXiv 2023</sub>  
  Encourages cross-view consistency in novel-view synthesis.
- **[SyncDreamer](https://github.com/liuyuan-pal/SyncDreamer)** <sub>ICLR 2024</sub>  
  Synchronizes multi-view diffusion generation [Paper](https://arxiv.org/abs/2309.03453)
- **[MVDream](https://github.com/bytedance/MVDream)** <sub>ICLR 2024</sub>  
  Generates multi-view images with 3D-aware diffusion [Paper](https://arxiv.org/abs/2308.16512)
- **[Wonder3D](https://github.com/xxlong0/Wonder3D)** <sub>CVPR 2024</sub>  
  Reconstructs 3D assets from single images through multi-view diffusion [Paper](https://arxiv.org/abs/2310.15008)
- **[ViewDiff](https://lukashoel.github.io/ViewDiff/)** <sub>CVPR 2024</sub>  
  Enforces 3D consistency for text-to-image multi-view generation.
- **[EscherNet](https://kxhit.github.io/EscherNet/)** <sub>CVPR 2024</sub>  
  Performs scalable view synthesis under camera changes.
- **[DreamGaussian](https://github.com/dreamgaussian/dreamgaussian)** <sub>ICLR 2024</sub>  
  Uses 3D Gaussians for fast text/image-to-3D generation [Paper](https://arxiv.org/abs/2309.16653)
- **[LGM](https://github.com/3DTopia/LGM)** <sub>ECCV 2024</sub>  
  Reconstructs 3D Gaussians from sparse or generated views [Paper](https://arxiv.org/abs/2403.14540)
- **[GRM](https://justimyhxu.github.io/projects/grm/)** <sub>ECCV 2024</sub>  
  Builds large Gaussian reconstruction models.
- **[Instant3D](https://arxiv.org/abs/2311.08403)** <sub>arXiv / venue TBD</sub>  
  Accelerates 3D generation from sparse visual evidence.
- **[TripoSR](https://github.com/VAST-AI-Research/TripoSR)** <sub>arXiv 2024</sub>  
  Fast feed-forward 3D reconstruction from a single image [Paper](https://arxiv.org/abs/2403.02151)
- **[CRM](https://arxiv.org/search/?query=CRM+3D+reconstruction+diffusion&searchtype=all)** <sub>arXiv / venue TBD</sub>  
  Uses reconstruction priors for consistent 3D asset generation.
- **[LRM](https://arxiv.org/search/?query=Large+Reconstruction+Model+3D&searchtype=all)** <sub>ICLR 2024 / arXiv</sub>  
  Learns large reconstruction models for image-to-3D.

<p align="right"><a href="#internal-methods">Back to methods ↑</a></p>

---

<a id="internal-methods-video-generation-and-temporal-editing"></a>
#### Video generation & temporal editing <sup>21</sup>

<sub>Text-to-video models, motion modules, temporal feature propagation, and video editing.</sub>

- **[VideoLDM](https://research.nvidia.com/labs/toronto-ai/VideoLDM/)** <sub>CVPR 2023</sub>  
  Extends latent diffusion to video generation.
- **[Text2Video-Zero](https://github.com/Picsart-AI-Research/Text2Video-Zero)** <sub>ICCV 2023</sub>  
  Adapts image diffusion to zero-shot video generation [Paper](https://arxiv.org/abs/2303.13439)
- **[Tune-A-Video](https://github.com/showlab/Tune-A-Video)** <sub>ICCV 2023</sub>  
  Tunes a T2I model for video generation from one video [Paper](https://arxiv.org/abs/2212.11565)
- **[AnimateDiff](https://github.com/guoyww/AnimateDiff)** <sub>ICLR 2024</sub>  
  Adds motion modules to personalized image diffusion models [Paper](https://arxiv.org/abs/2307.04725)
- **[FateZero](https://github.com/ChenyangQiQi/FateZero)** <sub>ICCV 2023</sub>  
  Uses attention fusion for zero-shot video editing [Paper](https://arxiv.org/abs/2303.09538)
- **[Video-P2P](https://github.com/ShaoTengLiu/Video-P2P)** <sub>arXiv 2023</sub>  
  Extends Prompt-to-Prompt-style editing to videos [Paper](https://arxiv.org/abs/2303.09538)
- **[TokenFlow](https://diffusion-tokenflow.github.io/)** <sub>ICLR 2024</sub>  
  Propagates diffusion features to improve temporal video editing consistency.
- **[CoDeF](https://qiuyu96.github.io/CoDeF/)** <sub>CVPR 2024</sub>  
  Uses content deformation fields for temporally consistent video processing.
- **[Rerender A Video](https://www.mmlab-ntu.com/project/rerender/)** <sub>SIGGRAPH Asia 2023</sub>  
  Performs zero-shot text-guided video-to-video translation.
- **[COVE](https://github.com/wangjiangshan0725/COVE)** <sub>arXiv 2024</sub>  
  Uses correspondence guidance for video editing [Paper](https://arxiv.org/abs/2401.12345)
- **[VideoCrafter](https://github.com/AILab-CVC/VideoCrafter)** <sub>arXiv 2023</sub>  
  Open video diffusion framework [Paper](https://arxiv.org/abs/2311.10125)
- **[VideoCrafter2](https://github.com/AILab-CVC/VideoCrafter)** <sub>CVPR 2024</sub>  
  Improves high-quality video diffusion generation [Paper](https://arxiv.org/abs/2311.10125)
- **[ModelScopeT2V](https://github.com/modelscope/modelscope)** <sub>project / 2023</sub>  
  Open text-to-video generation system.
- **[Make-A-Video](https://arxiv.org/abs/2209.14792)** <sub>arXiv 2022</sub>  
  Generates videos from text using image-text and video data.
- **[Imagen Video](https://arxiv.org/abs/2210.02303)** <sub>arXiv 2022</sub>  
  Cascaded video diffusion model.
- **[Phenaki](https://arxiv.org/abs/2210.02399)** <sub>ICLR 2023 / arXiv</sub>  
  Generates long videos from open-domain prompts.
- **[VideoFusion](https://arxiv.org/abs/2301.02194)** <sub>CVPR 2023 / arXiv</sub>  
  Uses decomposed diffusion for video generation.
- **[Latte](https://arxiv.org/abs/2401.03048)** <sub>TMLR / arXiv</sub>  
  Applies latent diffusion transformers to video generation.
- **[VideoPoet](https://arxiv.org/abs/2312.14125)** <sub>ICML 2024 / arXiv</sub>  
  Multimodal video generation and editing model.
- **[Lumiere](https://arxiv.org/abs/2401.12945)** <sub>SIGGRAPH 2024 / arXiv</sub>  
  Space-time diffusion model for coherent video generation.
- **[Sora technical report](https://openai.com/research/video-generation-models-as-world-simulators)** <sub>technical report 2024</sub>  
  Large-scale video generation model emphasizing world simulation properties.

<p align="right"><a href="#internal-methods">Back to methods ↑</a></p>

---

<a id="internal-methods-long-form-stories-and-interactive-video"></a>
#### Long-form stories & interactive video <sup>7</sup>

<sub>Long-horizon narratives, multi-scene planning, interactive control, and shot consistency.</sub>

- **[MovieDreamer](https://arxiv.org/abs/2407.16655)** <sub>arXiv / venue TBD</sub>  
  Studies hierarchical long visual sequence generation.
- **[TaleCrafter](https://arxiv.org/abs/2305.18247)** <sub>arXiv / venue TBD</sub>  
  Generates multi-character visual stories.
- **[One-Prompt-One-Story](https://arxiv.org/abs/2402.10603)** <sub>arXiv / venue TBD</sub>  
  Aims at consistent story generation from a single prompt.
- **[Animate-A-Story](https://github.com/AILab-CVC/Animate-A-Story)** <sub>arXiv 2023</sub>  
  Generates storytelling videos with retrieval and control signals [Paper](https://arxiv.org/abs/2310.08428)
- **[MotionStream](https://openreview.net/forum?id=v1DKz5Vxr7)** <sub>ICLR 2026</sub>  
  Supports real-time video generation with interactive motion control.
- **[VideoDirectorGPT](https://arxiv.org/abs/2306.02424)** <sub>arXiv 2023</sub>  
  Uses LLM planning for multi-scene video generation.
- **[ShotAdapter](https://arxiv.org/abs/2406.12698)** <sub>arXiv / venue TBD</sub>  
  Adapts video generation for multi-shot consistency.

<p align="right"><a href="#internal-methods">Back to methods ↑</a></p>

---

<a id="internal-methods-personalized-video-and-human-animation"></a>
#### Personalized video & human animation <sup>6</sup>

<sub>Subject-aware video customization, talking-human generation, and reference-driven animation.</sub>

- **[VideoBooth](https://arxiv.org/abs/2307.11056)** <sub>arXiv 2023</sub>  
  Customizes video generation to a subject or concept.
- **[DreamVideo](https://arxiv.org/abs/2312.04434)** <sub>arXiv 2023</sub>  
  Personalizes video generation with subject-aware priors.
- **[Vlogger](https://arxiv.org/abs/2401.13384)** <sub>arXiv 2024</sub>  
  Generates talking/head or human-centric video content.
- **[MagicAnimate](https://github.com/magic-research/magic-animate)** <sub>CVPR 2024</sub>  
  Animates human images under motion guidance [Paper](https://arxiv.org/abs/2311.16498)
- **[AnimateAnyone](https://arxiv.org/abs/2311.17117)** <sub>CVPR 2024 / arXiv</sub>  
  Animates reference characters with strong identity preservation.
- **[Champ](https://arxiv.org/abs/2403.12522)** <sub>arXiv 2024</sub>  
  Enables controllable and consistent human animation.

<p align="right"><a href="#internal-methods">Back to methods ↑</a></p>


<a id="internal-benchmarks"></a>
### Benchmarks & Evaluators

<p><sub><b>20 resources</b> organized into 4 focused topics.</sub></p>

| Topic | Coverage |
|---|---:|
| [Multi-view & 3D consistency](#internal-benchmarks-multi-view-and-3d-consistency) | **3** |
| [Video generation quality & temporal coherence](#internal-benchmarks-video-generation-quality-and-temporal-coherence) | **7** |
| [Story, character & long-horizon consistency](#internal-benchmarks-story-character-and-long-horizon-consistency) | **4** |
| [Editing, tracking & feature-based metrics](#internal-benchmarks-editing-tracking-and-feature-based-metrics) | **6** |

<a id="internal-benchmarks-multi-view-and-3d-consistency"></a>
#### Multi-view & 3D consistency <sup>3</sup>

<sub>Benchmarks and metrics for geometric compatibility across generated viewpoints.</sub>

- **[MVG-Bench](https://github.com/xiexh20/MVGBench)** <sub>arXiv 2024</sub>  
  Evaluates multi-view generation consistency.
- **[MET3R](https://github.com/mohammadasim98/met3r)** <sub>arXiv 2024</sub>  
  Measures 3D-aware multi-view consistency from generated images.
- **[Multi-view consistency metrics](https://arxiv.org/abs/2501.06336)** <sub>resource</sub>  
  Measures cross-view geometric compatibility.

<p align="right"><a href="#internal-benchmarks">Back to benchmarks & evaluators ↑</a></p>

---

<a id="internal-benchmarks-video-generation-quality-and-temporal-coherence"></a>
#### Video generation quality & temporal coherence <sup>7</sup>

<sub>General video quality, text–video alignment, motion, and physical-temporal diagnostics.</sub>

- **[VBench](https://github.com/Vchitect/VBench)** <sub>CVPR 2024</sub>  
  Comprehensive video generation benchmark including subject/background and temporal consistency.
- **[Video-Bench](https://github.com/Video-Bench/Video-Bench)** <sub>CVPR 2025</sub>  
  Human-aligned video generation benchmark.
- **[EvalCrafter](https://github.com/evalcrafter/EvalCrafter)** <sub>CVPR 2024</sub>  
  Evaluates generated videos along visual, text-video, and motion dimensions.
- **[FETV](https://github.com/llyx97/FETV)** <sub>NeurIPS 2023 Datasets and Benchmarks</sub>  
  Fine-grained open-domain text-to-video evaluation benchmark. [Paper](http://papers.nips.cc/paper_files/paper/2023/hash/c481049f7410f38e788f67c171c64ad5-Abstract-Datasets_and_Benchmarks.html)
- **[T2V-CompBench](https://arxiv.org/abs/2402.14687)** <sub>arXiv / venue TBD</sub>  
  Tests compositional text-to-video generation.
- **[VideoScore](https://arxiv.org/abs/2406.15283)** <sub>arXiv / venue TBD</sub>  
  Provides learned or automatic video generation quality scoring.
- **[VideoPhy temporal subset](https://github.com/Hritikbansal/videophy)** <sub>ICLR 2025</sub>  
  Uses physical video checks as temporal/world consistency diagnostics.

<p align="right"><a href="#internal-benchmarks">Back to benchmarks & evaluators ↑</a></p>

---

<a id="internal-benchmarks-story-character-and-long-horizon-consistency"></a>
#### Story, character & long-horizon consistency <sup>4</sup>

<sub>Identity persistence, story continuity, and long-video evaluation.</sub>

- **[ViStoryBench](https://github.com/ViStoryBench/ViStoryBench)** <sub>CVPR 2026 / preprint</sub>  
  Evaluates story visualization, character consistency, and narrative coherence. [Paper](https://doi.org/10.48550/arXiv.2505.24862)
- **[Long-video consistency evaluation](https://arxiv.org/search/?query=long+video+consistency+benchmark&searchtype=all)** <sub>resource</sub>  
  Focuses on long-horizon entity and scene persistence.
- **[Character consistency benchmark](https://arxiv.org/abs/2505.11425)** <sub>resource</sub>  
  Tests identity preservation across generated sets.
- **[Story visualization benchmark](https://arxiv.org/abs/2604.18575)** <sub>resource</sub>  
  Tests narrative and character persistence in story sequences.

<p align="right"><a href="#internal-benchmarks">Back to benchmarks & evaluators ↑</a></p>

---

<a id="internal-benchmarks-editing-tracking-and-feature-based-metrics"></a>
#### Editing, tracking & feature-based metrics <sup>6</sup>

<sub>Preservation metrics based on editing stability, CLIP/DINO features, face identity, and LPIPS.</sub>

- **[Video editing consistency metrics](https://arxiv.org/abs/2409.20500)** <sub>resource</sub>  
  Measures preservation and temporal stability after video editing.
- **[CLIP frame consistency](https://arxiv.org/search/?query=CLIP+frame+consistency+video+generation&searchtype=all)** <sub>metric family</sub>  
  Uses semantic features to estimate cross-frame consistency.
- **[DINO tracking consistency](https://arxiv.org/search/?query=DINO+tracking+consistency+video+generation&searchtype=all)** <sub>metric family</sub>  
  Uses self-supervised features for object/region persistence.
- **[Identity similarity metrics](https://arxiv.org/search/?query=identity+similarity+metric+personalized+generation&searchtype=all)** <sub>metric family</sub>  
  Evaluates subject or face identity preservation.
- **[Face recognition metrics](https://arxiv.org/search/?query=face+identity+metric+diffusion+generation&searchtype=all)** <sub>metric family</sub>  
  Uses face recognition models for identity consistency.
- **[LPIPS temporal smoothness](https://arxiv.org/search/?query=LPIPS+temporal+smoothness+video+generation&searchtype=all)** <sub>metric family</sub>  
  Measures perceptual smoothness across frames.

<p align="right"><a href="#internal-benchmarks">Back to benchmarks & evaluators ↑</a></p>


<a id="internal-datasets"></a>
### Datasets & Data Resources

<p><sub><b>20 resources</b> organized into 4 focused topics.</sub></p>

| Topic | Coverage |
|---|---:|
| [Video segmentation & tracking](#internal-datasets-video-segmentation-and-tracking) | **8** |
| [Driving & dynamic scenes](#internal-datasets-driving-and-dynamic-scenes) | **3** |
| [3D objects & multi-view reconstruction](#internal-datasets-3d-objects-and-multi-view-reconstruction) | **8** |
| [Synthetic controlled environments](#internal-datasets-synthetic-controlled-environments) | **1** |

<a id="internal-datasets-video-segmentation-and-tracking"></a>
#### Video segmentation & tracking <sup>8</sup>

<sub>Object persistence, occlusion, scene parsing, and long-term tracking supervision.</sub>

- **[MeViS](https://github.com/henghuiding/MeViS)** <sub>ICCV 2023</sub>  
  Motion-expression video segmentation data useful for temporal grounding.
- **[MOSE](https://github.com/henghuiding/MOSE-api)** <sub>ICCV 2023 / dataset</sub>  
  Video object segmentation data with complex occlusions.
- **[TAO](https://github.com/TAO-Dataset/tao)** <sub>ECCV 2020</sub>  
  Long-tail tracking data for object persistence diagnostics.
- **[VSPW](https://github.com/VSPW-dataset/VSPW_code)** <sub>CVPR 2021</sub>  
  Video scene parsing dataset for scene-state continuity.
- **[DAVIS](https://davischallenge.org/)** <sub>CVPR 2016</sub>  
  Video object segmentation data for temporal preservation.
- **[YouTube-VOS](https://youtube-vos.org/)** <sub>ECCV 2018 / dataset</sub>  
  Large-scale video object segmentation data.
- **[LaSOT](https://cis.temple.edu/lasot/)** <sub>CVPR 2019</sub>  
  Long-term single-object tracking dataset.
- **[TrackingNet](https://tracking-net.org/)** <sub>ECCV 2018 / dataset</sub>  
  Large-scale object tracking data.

<p align="right"><a href="#internal-datasets">Back to datasets & data resources ↑</a></p>

---

<a id="internal-datasets-driving-and-dynamic-scenes"></a>
#### Driving & dynamic scenes <sup>3</sup>

<sub>Large-scale autonomous-driving data for geometry, motion, and state continuity.</sub>

- **[nuScenes](https://github.com/nutonomy/nuscenes-devkit)** <sub>CVPR 2020</sub>  
  Driving dataset useful for dynamic-scene consistency.
- **[KITTI](https://www.cvlibs.net/datasets/kitti/)** <sub>IJRR 2013 / dataset</sub>  
  Autonomous-driving visual dataset for geometry and temporal checks.
- **[Waymo Open Dataset](https://waymo.com/open/)** <sub>CVPR 2020 / dataset</sub>  
  Large-scale driving data for world and motion consistency.

<p align="right"><a href="#internal-datasets">Back to datasets & data resources ↑</a></p>

---

<a id="internal-datasets-3d-objects-and-multi-view-reconstruction"></a>
#### 3D objects & multi-view reconstruction <sup>8</sup>

<sub>Object assets, camera trajectories, RGB-D scenes, scans, and multi-view imagery.</sub>

- **[Objaverse](https://objaverse.allenai.org/)** <sub>CVPR 2023 / dataset</sub>  
  Large 3D object dataset for view and 3D generation.
- **[Objaverse-XL](https://objaverse.allenai.org/objaverse-xl/)** <sub>NeurIPS 2023 Datasets and Benchmarks</sub>  
  Web-scale 3D object data.
- **[CO3D](https://github.com/facebookresearch/co3d)** <sub>ICCV 2021 / dataset</sub>  
  Common objects in 3D data for view consistency.
- **[RealEstate10K](https://google.github.io/realestate10k/)** <sub>dataset</sub>  
  Camera-trajectory video data for novel-view synthesis.
- **[ScanNet](http://www.scan-net.org/)** <sub>CVPR 2017 / dataset</sub>  
  RGB-D scene data for geometry-aware generation.
- **[ShapeNet](https://shapenet.org/)** <sub>arXiv 2015 / dataset</sub>  
  3D shape dataset for object-level 3D generation.
- **[Google Scanned Objects](https://research.google/tools/datasets/google-scanned-objects/)** <sub>dataset</sub>  
  High-quality scanned object assets.
- **[MVImgNet](https://github.com/GAP-LAB-CUHK-SZ/MVImgNet)** <sub>CVPR 2023 / dataset</sub>  
  Multi-view image dataset for object-centric reconstruction.

<p align="right"><a href="#internal-datasets">Back to datasets & data resources ↑</a></p>

---

<a id="internal-datasets-synthetic-controlled-environments"></a>
#### Synthetic controlled environments <sup>1</sup>

<sub>Procedural data generation for controlled scene and temporal diagnostics.</sub>

- **[Kubric](https://github.com/google-research/kubric)** <sub>CVPR 2022 / dataset generator</sub>  
  Synthetic video/scene data generation for controlled temporal diagnostics. [Paper](https://doi.org/10.1109/ICDMW69685.2025.00072)

<p align="right"><a href="#internal-datasets">Back to datasets & data resources ↑</a></p>


<p align="right"><a href="#resource-collection">Back to resource index ↑</a> · <a href="#top">Back to top ↑</a></p>

---
<a id="normative-consistency"></a>
## 03 · Normative consistency

> **Agreement target —** Agreement with evaluative or world-level criteria.  
> **Scope —** Human preference, aesthetics, safety, fairness, concept restrictions, physical plausibility, commonsense, causality, and world-state validity.

<p align="center">
  <a href="#normative-methods"><img src="https://img.shields.io/badge/Methods-57-d17c2f?style=flat-square" alt="57 methods"></a>
  <a href="#normative-benchmarks"><img src="https://img.shields.io/badge/Benchmarks%20%26%20Evaluators-30-d17c2f?style=flat-square" alt="30 benchmarks and evaluators"></a>
  <a href="#normative-datasets"><img src="https://img.shields.io/badge/Datasets%20%26%20Data-20-d17c2f?style=flat-square" alt="20 datasets and data resources"></a>
  <img src="https://img.shields.io/badge/Total-107-d17c2f?style=flat-square" alt="107 total resources">
</p>

| Resource type | Description | Jump |
|---|---|---:|
| **Methods** | Architectures, objectives, inference procedures, and intervention mechanisms. | [Browse 57](#normative-methods) |
| **Benchmarks & Evaluators** | Test suites, metrics, learned scorers, and evaluation protocols. | [Browse 30](#normative-benchmarks) |
| **Datasets & Data Resources** | Training corpora, annotations, prompt sets, and diagnostic data. | [Browse 20](#normative-datasets) |

<a id="normative-methods"></a>
### Methods

<p><sub><b>57 resources</b> organized into 3 focused topics.</sub></p>

| Topic | Coverage |
|---|---:|
| [Preference models & reward optimization](#normative-methods-preference-models-and-reward-optimization) | **20** |
| [Safety, unlearning & concept control](#normative-methods-safety-unlearning-and-concept-control) | **20** |
| [World models & physical consistency](#normative-methods-world-models-and-physical-consistency) | **17** |

<a id="normative-methods-preference-models-and-reward-optimization"></a>
#### Preference models & reward optimization <sup>20</sup>

<sub>Human-preference scorers, direct preference optimization, reinforcement learning, and multi-reward alignment.</sub>

- **[Pick-a-Pic / PickScore](https://github.com/yuvalkirstain/PickScore)** <sub>NeurIPS 2023</sub>  
  Collects pairwise preferences and trains a preference scorer.
- **[ImageReward](https://github.com/zai-org/ImageReward)** <sub>NeurIPS 2023</sub>  
  Learns a general human preference reward model for T2I images. [Paper](http://papers.nips.cc/paper_files/paper/2023/hash/33646ef0ed554145eab65f6250fab0c9-Abstract-Conference.html)
- **[HPS](https://arxiv.org/search/?query=Human+Preference+Score+text+to+image&searchtype=all)** <sub>ICCV 2023 / arXiv</sub>  
  Scores generated images according to human preference.
- **[HPSv2](https://github.com/tgxs002/HPSv2)** <sub>arXiv 2023</sub>  
  Refines human preference scoring and benchmark coverage.
- **[HPSv3](https://github.com/MizzenAI/HPSv3)** <sub>arXiv 2025</sub>  
  Extends preference evaluation to broader text-image distributions. [Paper](https://doi.org/10.1109/ICCV51701.2025.01400)
- **[MPS](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Learning_Multi-Dimensional_Human_Preference_for_Text-to-Image_Generation_CVPR_2024_paper.html)** <sub>CVPR 2024</sub>  
  Models multi-dimensional human preferences for T2I generation.
- **[VisionReward](https://github.com/zai-org/VisionReward)** <sub>AAAI 2026</sub>  
  Learns multi-dimensional reward signals for image and video generation.
- **[Diffusion-DPO](https://github.com/SalesforceAIResearch/DiffusionDPO)** <sub>NeurIPS 2023 / arXiv</sub>  
  Applies direct preference optimization to diffusion models.
- **[DDPO](https://github.com/jannerm/ddpo)** <sub>ICLR 2024</sub>  
  Trains diffusion models with reinforcement learning rewards.
- **[AlignProp](https://arxiv.org/abs/2310.03739)** <sub>ICLR 2024 / arXiv</sub>  
  Backpropagates reward gradients through diffusion sampling.
- **[DPOK](https://arxiv.org/abs/2305.16381)** <sub>arXiv 2023</sub>  
  Applies KL-regularized policy optimization to diffusion models.
- **[D3PO](https://arxiv.org/abs/2402.08385)** <sub>arXiv 2024</sub>  
  Optimizes diffusion policies from preference data.
- **[SPO](https://openaccess.thecvf.com/content/CVPR2025/html/Liang_Aesthetic_Post-Training_Diffusion_Models_from_Generic_Preferences_with_Step-by-step_Preference_CVPR_2025_paper.html)** <sub>CVPR 2025</sub>  
  Performs step-by-step preference optimization for aesthetic post-training.
- **[DSPO](https://openreview.net/forum?id=7f70331dbe58ad59d83941dfa7d975aa)** <sub>ICLR 2025</sub>  
  Aligns diffusion models using direct score preference optimization.
- **[RankDPO](https://openaccess.thecvf.com/content/ICCV2025/papers/Karthik_Scalable_Ranked_Preference_Optimization_for_Text-to-Image_Generation_ICCV_2025_paper.pdf)** <sub>ICCV 2025</sub>  
  Uses ranked preference data for scalable T2I preference optimization.
- **[CMPO / CaPO](https://openaccess.thecvf.com/content/CVPR2025/html/Lee_Calibrated_Multi-Preference_Optimization_for_Aligning_Diffusion_Models_CVPR_2025_paper.html)** <sub>CVPR 2025</sub>  
  Calibrates multiple preferences for diffusion alignment.
- **[Diffusion-NPO](https://openreview.net/forum?id=BADtQ9p1T2)** <sub>ICLR 2026</sub>  
  Performs negative preference optimization for diffusion alignment.
- **[BranchGRPO](https://openreview.net/forum?id=93N8hU2q5V)** <sub>ICLR 2026</sub>  
  Uses branch-level GRPO-style optimization for diffusion generation.
- **[Flow-GRPO](https://arxiv.org/abs/2505.05470)** <sub>arXiv / venue TBD</sub>  
  Applies GRPO-like preference learning to flow/diffusion sampling.
- **[RLAIF for Diffusion](https://arxiv.org/search/?query=RLAIF+diffusion+text+to+image&searchtype=all)** <sub>topic / resource</sub>  
  Uses AI feedback instead of human feedback for diffusion alignment.

<p align="right"><a href="#normative-methods">Back to methods ↑</a></p>

---

<a id="normative-methods-safety-unlearning-and-concept-control"></a>
#### Safety, unlearning & concept control <sup>20</sup>

<sub>Safety guidance, concept erasure, unlearning, red teaming, filtering, and adversarial robustness.</sub>

- **[Safe Latent Diffusion](https://github.com/ml-research/safe-latent-diffusion)** <sub>CVPR 2023</sub>  
  Adds safety guidance during latent diffusion sampling.
- **[Erasing Concepts from Diffusion Models](https://github.com/rohitgandikota/erasing)** <sub>ICCV 2023</sub>  
  Removes undesirable concepts from diffusion weights.
- **[Ablating Concepts](https://www.cs.cmu.edu/~concept-ablation/)** <sub>ICCV 2023</sub>  
  Ablates target concepts while retaining general model behavior.
- **[Unified Concept Editing](https://github.com/rohitgandikota/unified-concept-editing)** <sub>WACV 2024 / arXiv</sub>  
  Edits multiple concepts in diffusion models.
- **[MACE](https://arxiv.org/abs/2403.06135)** <sub>CVPR 2024 / arXiv</sub>  
  Scales concept erasure to many concepts.
- **[Forget-Me-Not](https://arxiv.org/abs/2303.17591)** <sub>arXiv 2023</sub>  
  Uses attention control to forget concepts.
- **[Ring-A-Bell](https://github.com/chiayi-hsu/Ring-A-Bell)** <sub>NeurIPS 2023 workshop / arXiv</sub>  
  Red-teams concept erasure using adversarial prompts.
- **[ACE](https://arxiv.org/search/?query=anti+editing+concept+erasure+diffusion&searchtype=all)** <sub>arXiv / venue TBD</sub>  
  Studies robust anti-editing concept erasure.
- **[Editing Massive Concepts](https://arxiv.org/abs/2403.13807)** <sub>arXiv / venue TBD</sub>  
  Edits or suppresses many concepts at scale.
- **[SalUn](https://arxiv.org/abs/2310.12508)** <sub>ICLR 2024 / arXiv</sub>  
  Uses saliency-guided unlearning for generative models.
- **[ESD](https://arxiv.org/search/?query=ESD+erasing+stable+diffusion&searchtype=all)** <sub>arXiv 2023</sub>  
  Erases stable-diffusion concepts through targeted training.
- **[ConceptPrune](https://arxiv.org/abs/2405.19237)** <sub>arXiv / venue TBD</sub>  
  Removes concepts by pruning or editing model components.
- **[Responsible Text-to-Image Diffusion](https://arxiv.org/abs/2311.17216)** <sub>ICML 2026 / project</sub>  
  Studies controllable and interpretable safe/fair generation.
- **[T2VSafetyBench methods](https://arxiv.org/abs/2409.08615)** <sub>arXiv 2024</sub>  
  Studies safety evaluation and intervention for text-to-video models.
- **[SafeGen](https://arxiv.org/abs/2512.12501)** <sub>arXiv / venue TBD</sub>  
  Improves safety during generative sampling.
- **[Safety Checker / post-hoc filters](https://arxiv.org/search/?query=diffusion+safety+checker+post-hoc+filter&searchtype=all)** <sub>system resource</sub>  
  Filters generated outputs after sampling.
- **[NSFW prompt filtering](https://arxiv.org/search/?query=NSFW+prompt+filtering+text+to+image&searchtype=all)** <sub>system resource</sub>  
  Screens prompts before generation.
- **[Adversarial prompt defense](https://arxiv.org/search/?query=adversarial+prompt+defense+text-to-image+diffusion&searchtype=all)** <sub>topic / resource</sub>  
  Defends against jailbreak prompts in visual generation.
- **[Jailbreak-resistant diffusion](https://arxiv.org/search/?query=jailbreak+text-to-image+diffusion+safety&searchtype=all)** <sub>topic / resource</sub>  
  Studies robust safety under prompt attacks.
- **[Concept restoration after erasure](https://arxiv.org/search/?query=concept+erasure+benign+retention+diffusion&searchtype=all)** <sub>topic / resource</sub>  
  Diagnoses benign capability loss after safety editing.

<p align="right"><a href="#normative-methods">Back to methods ↑</a></p>

---

<a id="normative-methods-world-models-and-physical-consistency"></a>
#### World models & physical consistency <sup>17</sup>

<sub>Interactive world models, driving simulation, physics-aware guidance, causality, and state transitions.</sub>

- **[UniSim](https://openreview.net/forum?id=sFyTZEqmUY)** <sub>ICLR 2024</sub>  
  Learns interactive real-world simulators for action-conditioned generation.
- **[Genie](https://proceedings.mlr.press/v235/bruce24a.html)** <sub>ICML 2024</sub>  
  Generates interactive environments from videos.
- **[GAIA-1](https://wayve.ai/thinking/gaia-1/)** <sub>arXiv / technical report 2023</sub>  
  Builds a generative world model for autonomous driving.
- **[WorldDreamer](https://arxiv.org/abs/2401.09985)** <sub>arXiv 2024</sub>  
  Generates driving videos with world-model priors.
- **[DriveDreamer](https://arxiv.org/abs/2309.09777)** <sub>ECCV 2024 / arXiv</sub>  
  Generates driving scenarios with structured controls.
- **[DriveDreamer-2](https://arxiv.org/abs/2403.06845)** <sub>arXiv / venue TBD</sub>  
  Extends driving world generation to longer/higher-quality videos.
- **[Vista](https://arxiv.org/search/?query=Vista+world+model+video+generation&searchtype=all)** <sub>arXiv / venue TBD</sub>  
  Studies video world models for controllable environments.
- **[Pandora](https://arxiv.org/search/?query=Pandora+world+model+video+generation&searchtype=all)** <sub>arXiv / venue TBD</sub>  
  Explores world modeling through video generation.
- **[Cosmos World Foundation Models](https://arxiv.org/abs/2501.03575)** <sub>technical report / arXiv</sub>  
  Studies large-scale world foundation models.
- **[HunyuanWorld / Hunyuan World](https://arxiv.org/abs/2501.03575)** <sub>technical report / arXiv</sub>  
  Generates 3D/world environments using generative world modeling.
- **[World-consistent Video Diffusion](https://arxiv.org/search/?query=world+consistent+video+diffusion&searchtype=all)** <sub>topic / resource</sub>  
  Enforces geometry, dynamics, and state consistency in video generation.
- **[Physics-guided Diffusion](https://arxiv.org/search/?query=physics-guided+diffusion+generation&searchtype=all)** <sub>topic / resource</sub>  
  Injects physical constraints into diffusion sampling or training.
- **[Simulator-guided Diffusion](https://arxiv.org/search/?query=simulator-guided+diffusion+generation&searchtype=all)** <sub>topic / resource</sub>  
  Uses simulators or constraints to steer generation.
- **[Verifier-guided Generation](https://arxiv.org/search/?query=verifier-guided+diffusion+generation&searchtype=all)** <sub>topic / resource</sub>  
  Uses post-hoc or in-loop verifiers to reject inconsistent samples.
- **[Causal Video Generation](https://arxiv.org/search/?query=causal+video+generation+diffusion&searchtype=all)** <sub>topic / resource</sub>  
  Studies causal state transitions in generated videos.
- **[Object-state-change Generation](https://arxiv.org/search/?query=object+state+change+text-to-video+generation&searchtype=all)** <sub>topic / resource</sub>  
  Focuses on object state changes and action consequences.
- **[Embodied Diffusion World Models](https://arxiv.org/search/?query=embodied+world+model+diffusion&searchtype=all)** <sub>topic / resource</sub>  
  Connects diffusion generation with embodied planning and control.

<p align="right"><a href="#normative-methods">Back to methods ↑</a></p>


<a id="normative-benchmarks"></a>
### Benchmarks & Evaluators

<p><sub><b>30 resources</b> organized into 3 focused topics.</sub></p>

| Topic | Coverage |
|---|---:|
| [Preference & aesthetics](#normative-benchmarks-preference-and-aesthetics) | **8** |
| [Safety & concept erasure](#normative-benchmarks-safety-and-concept-erasure) | **7** |
| [Physics, causality & world-model evaluation](#normative-benchmarks-physics-causality-and-world-model-evaluation) | **15** |

<a id="normative-benchmarks-preference-and-aesthetics"></a>
#### Preference & aesthetics <sup>8</sup>

<sub>Learned reward models and multidimensional evaluators for human preference and visual quality.</sub>

- **[Pick-a-Pic / PickScore](https://github.com/yuvalkirstain/PickScore)** <sub>NeurIPS 2023</sub>  
  Pairwise preference data and reward model for T2I outputs.
- **[ImageReward](https://github.com/zai-org/ImageReward)** <sub>NeurIPS 2023</sub>  
  Learned reward model for human preference evaluation.
- **[HPSv2](https://github.com/tgxs002/HPSv2)** <sub>arXiv 2023</sub>  
  Human preference benchmark for T2I evaluation.
- **[HPSv3](https://github.com/MizzenAI/HPSv3)** <sub>arXiv 2025</sub>  
  Wide-spectrum preference benchmark and reward model.
- **[VisionReward](https://github.com/zai-org/VisionReward)** <sub>AAAI 2026</sub>  
  Multi-dimensional image/video preference evaluator.
- **[MPS evaluation](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Learning_Multi-Dimensional_Human_Preference_for_Text-to-Image_Generation_CVPR_2024_paper.html)** <sub>CVPR 2024</sub>  
  Evaluates multiple dimensions of human preference.
- **[Aesthetic score models](https://arxiv.org/search/?query=aesthetic+score+text-to-image+diffusion&searchtype=all)** <sub>metric family</sub>  
  Score visual aesthetics for generated images.
- **[LAION aesthetic predictor](https://laion.ai/blog/laion-aesthetics/)** <sub>dataset/model resource</sub>  
  Provides aesthetic scores for LAION-like data.

<p align="right"><a href="#normative-benchmarks">Back to benchmarks & evaluators ↑</a></p>

---

<a id="normative-benchmarks-safety-and-concept-erasure"></a>
#### Safety & concept erasure <sup>7</sup>

<sub>Unsafe-generation, concept-removal, benign-retention, and red-teaming protocols.</sub>

- **[Six-CD](https://github.com/Artanisax/Six-CD)** <sub>arXiv / venue TBD</sub>  
  Evaluates concept removal and benign retention.
- **[I2P](https://arxiv.org/search/?query=I2P+inappropriate+image+prompts&searchtype=all)** <sub>arXiv 2023</sub>  
  Prompt benchmark for inappropriate image generation risks.
- **[Unsafe Diffusion benchmark](https://arxiv.org/abs/2511.19558)** <sub>resource</sub>  
  Evaluates unsafe output generation.
- **[T2VSafetyBench](https://arxiv.org/abs/2409.08615)** <sub>arXiv 2024</sub>  
  Safety benchmark for text-to-video generation.
- **[Concept removal benchmarks](https://arxiv.org/abs/2406.14855)** <sub>resource</sub>  
  Measures erasure success and collateral damage.
- **[Benign retention benchmarks](https://arxiv.org/abs/2511.20196)** <sub>resource</sub>  
  Tests whether safe editing harms benign generations.
- **[Red-teaming prompts](https://arxiv.org/abs/2401.00290)** <sub>resource</sub>  
  Stress-tests safety filters and concept removal.

<p align="right"><a href="#normative-benchmarks">Back to benchmarks & evaluators ↑</a></p>

---

<a id="normative-benchmarks-physics-causality-and-world-model-evaluation"></a>
#### Physics, causality & world-model evaluation <sup>15</sup>

<sub>Static and dynamic physical reasoning, action consequences, and world-state validity.</sub>

- **[PhyBench](https://github.com/OpenGVLab/PhyBench)** <sub>arXiv 2024</sub>  
  Static physical commonsense benchmark for T2I.
- **[VideoPhy](https://github.com/Hritikbansal/videophy)** <sub>ICLR 2025</sub>  
  Physical commonsense benchmark for generated videos.
- **[PhyCoBench](https://github.com/Jeckinchen/PhyCoBench)** <sub>arXiv 2024</sub>  
  Optical-flow-guided physical coherence benchmark.
- **[PhyGenBench](https://github.com/OpenGVLab/PhyGenBench)** <sub>arXiv 2024</sub>  
  Physical-law benchmark for video generation.
- **[VideoPhy-2](https://videophy2.github.io/)** <sub>ICLR 2026</sub>  
  Action-centric physical commonsense benchmark.
- **[T2VPhysBench](https://arxiv.org/abs/2505.00337)** <sub>arXiv / venue TBD</sub>  
  Tests first-principles physical consistency in T2V.
- **[T2VWorldBench](https://arxiv.org/abs/2507.18107)** <sub>arXiv / venue TBD</sub>  
  Evaluates world knowledge, commonsense, and causal plausibility.
- **[Physics-IQ](https://github.com/google-deepmind/physics-IQ-benchmark)** <sub>WACV 2026</sub>  
  Tests physical principles in generative video models.
- **[PhyWorldBench](https://github.com/g-jing/phy-world-bench)** <sub>arXiv 2025</sub>  
  Benchmarks physical realism in text-to-video generation.
- **[VideoVerse](https://github.com/Zeqing-Wang/VideoVerse)** <sub>arXiv 2025</sub>  
  World-model-oriented T2V evaluation.
- **[PhyEduVideo](https://github.com/meghamariamkm/PhyEduVideo)** <sub>WACV 2026</sub>  
  Physics-education-oriented video benchmark.
- **[PhyWorld](https://proceedings.mlr.press/v267/kang25g.html)** <sub>ICML 2025</sub>  
  Studies how far video generation is from physical world models.
- **[OSCBench](https://arxiv.org/abs/2603.11698)** <sub>arXiv / venue TBD</sub>  
  Tests object state change and action consequence.
- **[Morpheus](https://arxiv.org/search/?query=Morpheus+physical+reasoning+video+generative+models&searchtype=all)** <sub>arXiv / venue TBD</sub>  
  Evaluates physical reasoning in video generation.
- **[World-model Video Evaluation](https://arxiv.org/abs/2506.00613)** <sub>resource</sub>  
  General benchmarks for video-as-world-model behavior.

<p align="right"><a href="#normative-benchmarks">Back to benchmarks & evaluators ↑</a></p>


<a id="normative-datasets"></a>
### Datasets & Data Resources

<p><sub><b>20 resources</b> organized into 3 focused topics.</sub></p>

| Topic | Coverage |
|---|---:|
| [Preference & aesthetics](#normative-datasets-preference-and-aesthetics) | **7** |
| [Safety & concept control](#normative-datasets-safety-and-concept-control) | **3** |
| [Physical reasoning & world dynamics](#normative-datasets-physical-reasoning-and-world-dynamics) | **10** |

<a id="normative-datasets-preference-and-aesthetics"></a>
#### Preference & aesthetics <sup>7</sup>

<sub>Pairwise preference annotations, reward-model training data, and aesthetic ratings.</sub>

- **[Pick-a-Pic dataset](https://github.com/yuvalkirstain/PickScore)** <sub>NeurIPS 2023</sub>  
  Pairwise human preferences for generated images.
- **[ImageRewardDB](https://github.com/zai-org/ImageReward)** <sub>NeurIPS 2023 resource</sub>  
  Human preference annotations for reward training.
- **[HPD / HPSv2 data](https://github.com/tgxs002/HPSv2)** <sub>arXiv 2023 resource</sub>  
  Human preference data for T2I evaluation.
- **[HPDv3 / HPSv3 data](https://github.com/MizzenAI/HPSv3)** <sub>arXiv 2025 resource</sub>  
  Larger preference dataset for wide-spectrum evaluation.
- **[MPS preference data](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Learning_Multi-Dimensional_Human_Preference_for_Text-to-Image_Generation_CVPR_2024_paper.html)** <sub>CVPR 2024</sub>  
  Multi-dimensional preference labels.
- **[LAION-Aesthetics](https://laion.ai/blog/laion-aesthetics/)** <sub>dataset resource</sub>  
  Image-text data filtered by aesthetic scores.
- **[AVA Aesthetics](https://arxiv.org/abs/1412.4940)** <sub>CVPR 2012 / dataset</sub>  
  Aesthetic image-quality annotations.

<p align="right"><a href="#normative-datasets">Back to datasets & data resources ↑</a></p>

---

<a id="normative-datasets-safety-and-concept-control"></a>
#### Safety & concept control <sup>3</sup>

<sub>Unsafe prompt sets, NSFW resources, and concept-erasure diagnostics.</sub>

- **[I2P prompts](https://arxiv.org/search/?query=I2P+inappropriate+image+prompts&searchtype=all)** <sub>arXiv 2023 resource</sub>  
  Inappropriate prompt set for safety testing.
- **[NSFW prompt resources](https://arxiv.org/abs/2501.05359)** <sub>resource</sub>  
  Prompts for unsafe content testing.
- **[Concept erasure prompt sets](https://arxiv.org/abs/2404.03631)** <sub>resource</sub>  
  Prompts for target concept removal.

<p align="right"><a href="#normative-datasets">Back to datasets & data resources ↑</a></p>

---

<a id="normative-datasets-physical-reasoning-and-world-dynamics"></a>
#### Physical reasoning & world dynamics <sup>10</sup>

<sub>Physical commonsense, video dynamics, driving, egocentric interaction, and synthetic physics data.</sub>

- **[Physical commonsense prompts](https://arxiv.org/abs/2406.11802)** <sub>resource</sub>  
  Prompts testing static physical plausibility.
- **[Video physical prompts](https://arxiv.org/abs/2604.21873)** <sub>resource</sub>  
  Prompts testing dynamic physical plausibility.
- **[Driving world-model datasets](https://arxiv.org/abs/2502.10498)** <sub>resource</sub>  
  Driving data for action-conditioned world models.
- **[Ego4D](https://ego4d-data.org/)** <sub>CVPR 2022 / dataset</sub>  
  Egocentric video data for embodied and action reasoning.
- **[Something-Something V2](https://developer.qualcomm.com/software/ai-datasets/something-something)** <sub>ICCV 2017 / dataset</sub>  
  Human-object interaction videos for action/state understanding.
- **[CLEVRER](https://clevrer.csail.mit.edu/)** <sub>ICLR 2020 / dataset</sub>  
  Synthetic videos for physical and causal reasoning.
- **[PHYRE](https://phyre.ai/)** <sub>NeurIPS 2019 / benchmark</sub>  
  Physical reasoning environments.
- **[IntPhys](https://arxiv.org/abs/1803.07616)** <sub>arXiv 2018 / dataset</sub>  
  Intuitive physics video dataset.
- **[CLEVR](https://cs.stanford.edu/people/jcjohns/clevr/)** <sub>CVPR 2017 / dataset</sub>  
  Synthetic visual reasoning data.
- **[Kubric](https://github.com/google-research/kubric)** <sub>CVPR 2022</sub>  
  Synthetic scene/video generator useful for controlled physical diagnostics.

<p align="right"><a href="#normative-datasets">Back to datasets & data resources ↑</a></p>


<p align="right"><a href="#resource-collection">Back to resource index ↑</a> · <a href="#top">Back to top ↑</a></p>

---
## Machine-readable resources

The repository includes structured companion files for programmatic analysis and maintenance:

- [`resources/benchmark_coverage.csv`](resources/benchmark_coverage.csv): benchmark, dataset, evaluator, and diagnostic-resource coverage map.
- [`resources/related_surveys.csv`](resources/related_surveys.csv): prior survey positioning.
- [`resources/taxonomy_methods.csv`](resources/taxonomy_methods.csv): compact mapping from taxonomy nodes to representative methods and resources.
- [`resources/selected_bibtex.bib`](resources/selected_bibtex.bib): selected BibTeX entries.

## Coverage labels

| Label | Meaning |
|---|---|
| **P/C** | prompt and compositional faithfulness |
| **S/E** | structural control and edit preservation |
| **ID** | subject/identity persistence |
| **V/T** | multi-view, temporal, or narrative coherence |
| **N/S** | preference, safety, or value alignment |
| **P/W** | physical, causal, or world-grounded plausibility |

Coverage values: **H** = direct/dedicated coverage, **M** = partial/adaptable coverage, **L** = indirect/low coverage.

## Contribution guide

Contributions are welcome. Please keep additions concise, verifiable, and aligned with the relation-based taxonomy. Please include the resource title, BibTeX key, venue/year, official paper URL, official project/code URL if available, resource type, modality, primary consistency relation, coverage values, and a short diagnostic-use/blind-spot description.

Use the issue template: **[Add or correct a resource](.github/ISSUE_TEMPLATE/resource_addition.yml)**.

> [!TIP]
> Prefer official paper pages, author-maintained repositories, and stable proceedings links. Include enough information for another maintainer to verify the entry without additional searching.

## Maintenance notes

Some 2025--2026 papers may initially appear as arXiv or project-page entries before official proceedings metadata is stable. When official BibTeX becomes available, please update [`resources/selected_bibtex.bib`](resources/selected_bibtex.bib) and any corresponding table entries. 

When adding links, prefer official repositories or project pages over unofficial reimplementations. If no stable official repository exists, leave the code URL blank in the CSV table. Entries with arXiv-search links are included as expansion placeholders and should be replaced by stable paper/project links when available.

## Citation

If this survey or resource collection is useful in your research, please cite:

```bibtex
@article{yan2026consistency,
  title        = {Consistency in Diffusion-Based Visual Generation: A Survey},
  author       = {Yan, Song and Zhai, Wei and Wang, Chenfeng and Li, Ruixuan and Yang, Zhangping and Cai, Yancheng and Zhang, Tao and Wang, Ling and Lan, Yunwei and He, Yujie and Cao, Yang and Li, Min and Zha, Zheng-Jun},
  year         = {2026},
  doi          = {10.20944/preprints202606.0870.v1},
  url          = {https://www.preprints.org/manuscript/202606.0870/v1},
  note         = {Preprints}
}
```

## License

This repository is released under the [MIT License](LICENSE).

<p align="right"><a href="#top">Back to top ↑</a></p>
