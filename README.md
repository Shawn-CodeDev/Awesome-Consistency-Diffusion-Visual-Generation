# Awesome Consistency in Diffusion-Based Visual Generation

<p align="center">
  <img src="docs/校徽_ustc校徽%20科大蓝.svg" height="100" align="middle" alt="University of Science and Technology of China" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="docs/清华大学-logo.svg" height="100" align="middle" alt="Tsinghua University" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="docs/华中科技大学-logo.svg" height="180" align="middle" alt="Huazhong University of Science and Technology" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="docs/logo.png" height="110" align="middle" alt="University of Cambridge" />
</p>

<p align="center">
  <img src="https://commons.wikimedia.org/wiki/Special:Redirect/file/Li%20Auto%20English%20logo.svg" height="40" align="middle" alt="Li Auto" />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://commons.wikimedia.org/wiki/Special:Redirect/file/ByteDance%20logo%20English.svg" height="40" align="middle" alt="ByteDance" />
</p>

[![Validate resource tables](https://github.com/Shawn-CodeDev/Awesome-Consistency-Diffusion-Visual-Generation/actions/workflows/validate-resources.yml/badge.svg)](https://github.com/Shawn-CodeDev/Awesome-Consistency-Diffusion-Visual-Generation/actions/workflows/validate-resources.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

This repository accompanies the survey:

> **Consistency in Diffusion-Based Visual Generation: A Survey**  
> Song Yan, Wei Zhai, Chenfeng Wang, Ruixuan Li, Zhangping Yang, Yancheng Cai, Tao Zhang, Ling Wang, Yunwei Lan, Yujie He, Yang Cao, Min Li, Zheng-Jun Zha.

This repository collects papers, methods, benchmarks, datasets, evaluators, and diagnostic resources for **consistency in diffusion-based visual generation**. The main organization follows the survey taxonomy: **External Consistency**, **Internal Consistency**, and **Normative Consistency**. Within each relation, entries are grouped into **Methods**, **Benchmarks & Evaluators**, and **Datasets & Data Resources**.

Each entry follows this format:

> **Title** *(venue/year or source)* — short explanation of what consistency issue it helps study.

For very recent or not-yet-proceedings papers, the venue is marked as **arXiv / project / venue TBD** rather than guessed.

## Table of contents

- [Taxonomy](#taxonomy)
- [External consistency](#external-consistency)
- [Internal consistency](#internal-consistency)
- [Normative consistency](#normative-consistency)
- [Machine-readable resources](#machine-readable-resources)
- [Coverage labels](#coverage-labels)
- [Contribution guide](#contribution-guide)
- [Citation](#citation)

## Taxonomy

| Relation | Agreement target | Typical failures | Typical settings |
|---|---|---|---|
| **External consistency** | Agreement with prompts, references, controls, masks, layouts, poses, or edit instructions | prompt omission, attribute binding error, counting error, control mismatch, over-editing | text-to-image, structural control, instruction editing, inpainting, virtual try-on, typography |
| **Internal consistency** | Agreement among generated subjects, views, frames, shots, or story states | identity drift, view inconsistency, flicker, state forgetting, narrative discontinuity | personalization, multi-view/3D generation, video generation, story visualization |
| **Normative consistency** | Agreement with preference, safety, fairness, physical plausibility, commonsense, or causal/world-state criteria | low preference, unsafe output, erased benign concepts, physical violation, causal failure | preference optimization, safety editing, concept erasure, physical/world-model evaluation |

---

## External consistency

External consistency asks whether generated content follows externally specified conditions: text prompts, layouts, boxes, masks, depth maps, poses, reference images, editing instructions, or other user/task controls.

### Methods

- [GLIDE](https://arxiv.org/abs/2112.10741) *(ICML 2022)* — Early text-guided diffusion model supporting prompt-conditioned generation and editing.
- [Imagen](https://arxiv.org/abs/2205.11487) *(NeurIPS 2022 / arXiv)* — High-fidelity text-to-image diffusion model emphasizing language understanding.
- [Latent Diffusion Models](https://arxiv.org/abs/2112.10752) *(CVPR 2022)* — Latent-space diffusion backbone widely used for controllable generation and editing.
- [Composable Diffusion Models](https://arxiv.org/abs/2206.01714) *(ECCV 2022)* — Combines multiple diffusion score functions for compositional generation.
- [Structured Diffusion Guidance](https://arxiv.org/search/?query=Structured+Diffusion+Guidance&searchtype=all) *(arXiv / project)* — Uses structured guidance signals to improve prompt-object alignment.
- [StructureDiffusion](https://arxiv.org/abs/2212.05032) *(arXiv 2022)* — Parses prompts into structured representations to improve compositional text-to-image generation.
- [Attend-and-Excite](https://github.com/yuval-alaluf/Attend-and-Excite) *(SIGGRAPH 2023)* — Manipulates cross-attention maps to reduce missing objects and improve prompt coverage.
- [BoxDiff](https://github.com/showlab/BoxDiff) *(ICCV 2023)* — Training-free box-constrained generation for spatially grounded text-to-image synthesis.
- [Composer](https://github.com/damo-vilab/composer) *(ICML 2023)* — Composes heterogeneous visual conditions for controllable image synthesis.
- [MultiDiffusion](https://multidiffusion.github.io/) *(ICML 2023)* — Fuses multiple diffusion paths to satisfy spatial and regional generation constraints.
- [LLM-grounded Diffusion](https://llm-grounded-diffusion.github.io/) *(ICLR 2024)* — Uses LLM planning to turn complex prompts into layout-grounded generation constraints.
- [SynGen](https://arxiv.org/abs/2308.07037) *(ICCV 2023)* — Uses syntactic guidance to improve compositional text-to-image generation.
- [RPG: Recaption, Plan, and Generate](https://github.com/YangLing0818/RPG-DiffusionMaster) *(arXiv 2024)* — Uses MLLM-based recaptioning and planning for complex prompt following.
- [CONFORM](https://arxiv.org/search/?query=CONFORM+text+to+image+diffusion&searchtype=all) *(arXiv / venue TBD)* — Improves object-attribute alignment through contrastive or correspondence-driven prompt grounding.
- [Divide-and-Bind](https://arxiv.org/search/?query=Divide+and+Bind+text+to+image&searchtype=all) *(arXiv / venue TBD)* — Decomposes complex prompts and binds objects to attributes or relations.
- [Linguistic Binding in Diffusion](https://arxiv.org/search/?query=linguistic+binding+text+to+image+diffusion&searchtype=all) *(arXiv / venue TBD)* — Studies or improves language-binding failures in text-to-image diffusion.
- [Promptist](https://arxiv.org/search/?query=Promptist+text+to+image&searchtype=all) *(arXiv 2022)* — Optimizes prompts to improve text-to-image generation quality and alignment.
- [BeautifulPrompt](https://arxiv.org/search/?query=BeautifulPrompt+text+to+image&searchtype=all) *(AAAI 2024 / arXiv)* — Refines user prompts for stronger image generation quality and faithfulness.
- [Prompt Expansion for Text-to-Image](https://arxiv.org/search/?query=prompt+expansion+text+to+image+diffusion&searchtype=all) *(topic / resource)* — Expands underspecified prompts to reduce ambiguity in generation.
- [Prompt Decomposition for T2I](https://arxiv.org/search/?query=prompt+decomposition+text-to-image+evaluation&searchtype=all) *(topic / resource)* — Decomposes prompts into atomic semantic constraints for evaluation or guidance.
- [ControlNet](https://github.com/lllyasviel/ControlNet) *(ICCV 2023)* — Adds trainable side branches for depth, edge, pose, segmentation, and other controls.
- [GLIGEN](https://github.com/gligen/GLIGEN) *(CVPR 2023)* — Grounds generation with boxes and phrase-level grounding tokens.
- [T2I-Adapter](https://github.com/TencentARC/T2I-Adapter) *(AAAI 2024)* — Uses lightweight adapters for structural conditions such as sketch, depth, and pose.
- [IP-Adapter](https://github.com/tencent-ailab/IP-Adapter) *(arXiv 2023)* — Adds image-prompt conditioning while preserving text compatibility.
- [AnyDoor](https://github.com/ali-vilab/AnyDoor) *(CVPR 2024)* — Performs zero-shot object-level customization and insertion.
- [FreeDoM](https://github.com/vvictoryuki/FreeDoM) *(ICCV 2023)* — Applies training-free energy guidance for conditional diffusion tasks.
- [HumanSD](https://github.com/IDEA-Research/HumanSD) *(ICCV 2023)* — Generates human images under native skeleton guidance.
- [UniControl](https://arxiv.org/abs/2305.11147) *(NeurIPS 2023 / arXiv)* — Provides a unified framework for multiple controllable generation signals.
- [Uni-ControlNet](https://arxiv.org/abs/2305.16322) *(arXiv 2023)* — Unifies multi-condition ControlNet-style conditioning.
- [Ctrl-Adapter](https://openreview.net/forum?id=ny8T8OuNHe) *(ICLR 2025)* — Uses efficient adapters for diverse spatial and structural controls.
- [UniCon](https://openreview.net/forum?id=8jb0e1gLyd) *(ICLR 2025)* — Designs unidirectional information flow for stronger large-scale condition control.
- [InstanceDiffusion](https://people.eecs.berkeley.edu/~xdwang/projects/instancediffusion/) *(CVPR 2024)* — Supports instance-level control over object placement and attributes.
- [ControlNet++](https://arxiv.org/search/?query=ControlNet%2B%2B+diffusion&searchtype=all) *(arXiv / venue TBD)* — Improves ControlNet-style conditioning quality and efficiency.
- [ControlNet-XS](https://arxiv.org/search/?query=ControlNet-XS&searchtype=all) *(arXiv / venue TBD)* — Compresses controllable generation modules for efficient deployment.
- [ControlLoRA](https://arxiv.org/search/?query=ControlLoRA+diffusion&searchtype=all) *(arXiv / venue TBD)* — Uses LoRA-style lightweight control adaptation.
- [SparseCtrl](https://arxiv.org/search/?query=SparseCtrl&searchtype=all) *(arXiv / venue TBD)* — Controls image/video generation from sparse visual conditions.
- [SemanticControl](https://arxiv.org/search/?query=SemanticControl+diffusion&searchtype=all) *(arXiv / venue TBD)* — Handles loose or weakly aligned semantic controls.
- [LayoutDiffusion](https://arxiv.org/search/?query=LayoutDiffusion&searchtype=all) *(CVPR 2023 / arXiv)* — Conditions diffusion generation on layout annotations.
- [LayoutDM](https://arxiv.org/search/?query=LayoutDM+diffusion&searchtype=all) *(CVPR 2023 / arXiv)* — Models layout-to-image synthesis through diffusion.
- [SceneComposer](https://arxiv.org/search/?query=SceneComposer+text+to+image&searchtype=all) *(arXiv / venue TBD)* — Composes scene-level controls for complex generation.
- [Scene Graph Diffusion](https://arxiv.org/search/?query=scene+graph+diffusion+text+to+image&searchtype=all) *(arXiv / venue TBD)* — Uses scene graphs for relation-aware image synthesis.
- [DetDiffusion](https://arxiv.org/search/?query=DetDiffusion&searchtype=all) *(arXiv / venue TBD)* — Integrates detection-like constraints into image generation.
- [Grounded Diffusion](https://arxiv.org/search/?query=grounded+diffusion+text+to+image&searchtype=all) *(topic / resource)* — General family of grounding-based diffusion methods.
- [SAM-guided Diffusion Editing](https://arxiv.org/search/?query=SAM+guided+diffusion+editing&searchtype=all) *(topic / resource)* — Uses segmentation masks to localize editing constraints.
- [Diffusion Posterior Sampling](https://arxiv.org/search/?query=Diffusion+Posterior+Sampling&searchtype=all) *(ICLR 2023)* — Uses measurement likelihoods to guide inverse-problem diffusion.
- [Universal Guidance for Diffusion Models](https://arxiv.org/search/?query=Universal+Guidance+for+Diffusion+Models&searchtype=all) *(CVPR 2023 / arXiv)* — Applies generic guidance losses during sampling.
- [Classifier Guidance](https://arxiv.org/search/?query=classifier+guidance+diffusion+models&searchtype=all) *(NeurIPS 2021)* — Uses classifier gradients to steer diffusion samples.
- [Classifier-Free Guidance](https://arxiv.org/search/?query=classifier-free+diffusion+guidance&searchtype=all) *(NeurIPS 2021 workshop / arXiv)* — Steers conditional generation without an external classifier.
- [SDEdit](https://arxiv.org/abs/2108.01073) *(ICLR 2022)* — Edits images by adding noise and denoising under new guidance.
- [Prompt-to-Prompt](https://github.com/google/prompt-to-prompt) *(ICLR 2023)* — Controls cross-attention to edit prompts while preserving layout/content.
- [Null-Text Inversion](https://null-text-inversion.github.io/) *(CVPR 2023)* — Inverts real images for more faithful prompt-based editing.
- [DiffEdit](https://github.com/Xiang-cd/DiffEdit-stable-diffusion) *(ICLR 2023)* — Computes semantic edit masks from prompt differences.
- [InstructPix2Pix](https://github.com/timothybrooks/instruct-pix2pix) *(CVPR 2023)* — Trains a diffusion editor to follow natural-language instructions.
- [InstructDiffusion](https://github.com/cientgu/InstructDiffusion) *(CVPR 2024)* — Unifies several visual instruction tasks in diffusion models.
- [Imagic](https://imagic-editing.github.io/) *(CVPR 2023)* — Edits real images by optimizing text embeddings and model weights.
- [Paint-by-Example](https://github.com/Fantasy-Studio/Paint-by-Example) *(CVPR 2023)* — Uses exemplar images to guide localized editing.
- [Plug-and-Play Diffusion Features](https://pnp-diffusion.github.io/) *(CVPR 2023)* — Injects diffusion features to preserve structure during editing.
- [Pix2Pix-Zero](https://pix2pixzero.github.io/) *(ICCV 2023)* — Performs zero-shot image-to-image translation through cross-attention guidance.
- [MasaCtrl](https://github.com/TencentARC/MasaCtrl) *(ICCV 2023)* — Uses mutual self-attention to preserve structure across synthesis/editing.
- [LEDITS++](https://arxiv.org/abs/2311.16711) *(arXiv 2023)* — Performs lightweight semantic editing and concept erasure.
- [DragonDiffusion](https://github.com/MC-E/DragonDiffusion) *(ICLR 2024 / arXiv)* — Supports object moving, resizing, and fine-grained interactive editing.
- [DragDiffusion](https://github.com/Yujun-Shi/DragDiffusion) *(CVPR 2024)* — Enables point-based drag editing with diffusion priors.
- [FreeDrag](https://arxiv.org/search/?query=FreeDrag+diffusion&searchtype=all) *(CVPR 2024 / arXiv)* — Improves drag editing without model finetuning.
- [DiffEditor](https://arxiv.org/search/?query=DiffEditor+diffusion&searchtype=all) *(arXiv / venue TBD)* — Provides an editing pipeline for localized diffusion modifications.
- [SEGA](https://arxiv.org/search/?query=SEGA+semantic+guidance+diffusion&searchtype=all) *(arXiv 2023)* — Steers semantic directions during diffusion sampling.
- [Emu Edit](https://arxiv.org/search/?query=Emu+Edit+image+editing&searchtype=all) *(CVPR 2024 / arXiv)* — Uses instruction data for high-quality image editing.
- [SmartEdit](https://arxiv.org/search/?query=SmartEdit+diffusion&searchtype=all) *(CVPR 2024 / arXiv)* — Combines MLLMs and diffusion for instruction-based editing.
- [BrushNet](https://arxiv.org/search/?query=BrushNet+diffusion+inpainting&searchtype=all) *(ECCV 2024 / arXiv)* — Adds a dedicated inpainting branch for masked image editing.
- [PowerPaint](https://arxiv.org/search/?query=PowerPaint+diffusion&searchtype=all) *(ECCV 2024 / arXiv)* — Supports versatile object removal, insertion, and inpainting.
- [Inpaint Anything](https://arxiv.org/search/?query=Inpaint+Anything+diffusion&searchtype=all) *(arXiv 2023)* — Combines segmentation and diffusion inpainting.
- [TextDiffuser](https://arxiv.org/search/?query=TextDiffuser&searchtype=all) *(NeurIPS 2023)* — Improves text rendering inside generated images.
- [TextDiffuser-2](https://arxiv.org/search/?query=TextDiffuser-2&searchtype=all) *(arXiv 2023)* — Improves multilingual and layout-aware text rendering.
- [AnyText](https://arxiv.org/search/?query=AnyText+diffusion&searchtype=all) *(CVPR 2024)* — Generates and edits multilingual text in images.
- [GlyphDraw](https://arxiv.org/search/?query=GlyphDraw&searchtype=all) *(NeurIPS 2023 / arXiv)* — Uses glyph-level information for visual text generation.
- [GlyphControl](https://arxiv.org/search/?query=GlyphControl&searchtype=all) *(arXiv / venue TBD)* — Adds explicit glyph constraints for controllable typography.
- [TryOnDiffusion](https://arxiv.org/search/?query=TryOnDiffusion&searchtype=all) *(CVPR 2023)* — Uses diffusion for virtual try-on with garment-person consistency.
- [StableVITON](https://github.com/rlawjdghek/StableVITON) *(CVPR 2024)* — Adapts stable diffusion to virtual try-on.
- [IDM-VTON](https://github.com/yisol/IDM-VTON) *(ECCV 2024)* — Improves image-based virtual try-on with diffusion.
- [CatVTON](https://github.com/Zheng-Chong/CatVTON) *(arXiv 2024)* — Provides a lightweight virtual try-on framework.
- [OOTDiffusion](https://github.com/levihsu/OOTDiffusion) *(arXiv 2024)* — Generates outfits and try-on images under reference constraints.
- [LaDI-VTON](https://arxiv.org/search/?query=LaDI-VTON&searchtype=all) *(ACM MM 2023 / arXiv)* — Uses latent diffusion for virtual try-on.
- [AnyDressing](https://arxiv.org/search/?query=AnyDressing&searchtype=all) *(arXiv / venue TBD)* — Handles generalized dressing and garment transfer constraints.
- [PosterCraft](https://arxiv.org/search/?query=PosterCraft&searchtype=all) *(arXiv / venue TBD)* — Studies layout- and text-aware poster generation.
- [CreatiPoster](https://arxiv.org/search/?query=CreatiPoster&searchtype=all) *(arXiv / venue TBD)* — Generates visually structured poster layouts.
- [PosterMaker](https://arxiv.org/search/?query=PosterMaker+diffusion&searchtype=all) *(arXiv / venue TBD)* — Uses diffusion for controllable poster design.

### Benchmarks & Evaluators

- [TIFA](https://github.com/Yushi-Hu/tifa) *(ICCV 2023)* — Evaluates prompt faithfulness using generated question-answer pairs.
- [GenEval](https://github.com/djghosh13/geneval) *(NeurIPS 2023 workshop / arXiv)* — Tests object presence, counting, colors, positions, and attribute binding.
- [T2I-CompBench](https://github.com/Karine-Huang/T2I-CompBench) *(NeurIPS 2023)* — Measures compositional alignment across attributes, relations, and complex prompts.
- [GenEval2](https://github.com/facebookresearch/GenEval2) *(arXiv / venue TBD)* — Extends prompt-following evaluation with harder and less saturated cases.
- [HRS-Bench](https://github.com/eslambakr/HRS_benchmark) *(ICCV 2023)* — Provides holistic evaluation of T2I capabilities, robustness, fairness, and bias.
- [DPG-Bench](https://github.com/TencentQQGYLab/ELLA) *(arXiv 2024)* — Uses dense prompts to evaluate semantic and relation following.
- [GenAI-Bench / VQAScore](https://github.com/linzhiqiu/t2v_metrics) *(ECCV 2024)* — Evaluates text-to-visual generation through VQA-style image/video scoring.
- [DrawBench](https://arxiv.org/search/?query=DrawBench+text+to+image&searchtype=all) *(Imagen / NeurIPS 2022 resource)* — Human-evaluation prompt suite for text-to-image generation.
- [PartiPrompts](https://arxiv.org/search/?query=PartiPrompts&searchtype=all) *(arXiv 2022)* — Large prompt set for evaluating compositional and high-level prompt following.
- [DSG: Davidsonian Scene Graph evaluation](https://arxiv.org/search/?query=Davidsonian+Scene+Graph+text+to+image&searchtype=all) *(arXiv / venue TBD)* — Converts prompts to scene-graph-like checks for semantic consistency.
- [VIEScore](https://arxiv.org/search/?query=VIEScore&searchtype=all) *(arXiv / venue TBD)* — Uses vision-language evaluators for image-text alignment.
- [EditBench](https://arxiv.org/search/?query=Imagen+Editor+EditBench&searchtype=all) *(CVPR 2023)* — Benchmarks text-guided image inpainting and edit preservation.
- [ConceptBed](https://github.com/ConceptBed/evaluations) *(arXiv / venue TBD)* — Evaluates concept learning and reusable concept binding.
- [CountBench](https://arxiv.org/search/?query=counting+benchmark+text+to+image&searchtype=all) *(resource / venue TBD)* — Tests numerical object-counting consistency in generated images.
- [SpatialBench](https://arxiv.org/search/?query=spatial+relation+benchmark+text+to+image&searchtype=all) *(resource / venue TBD)* — Tests spatial relation following.
- [ObjectAttributeBench](https://arxiv.org/search/?query=object+attribute+benchmark+text+to+image&searchtype=all) *(resource / venue TBD)* — Tests object-attribute binding.
- [RelationBench](https://arxiv.org/search/?query=relation+benchmark+text+to+image+diffusion&searchtype=all) *(resource / venue TBD)* — Tests relational semantics in text-to-image generation.
- [TypographyBench](https://arxiv.org/search/?query=text+rendering+benchmark+diffusion&searchtype=all) *(resource / venue TBD)* — Evaluates rendered text accuracy in generated images.
- [VTON evaluation suites](https://arxiv.org/search/?query=virtual+try-on+benchmark+diffusion&searchtype=all) *(resource)* — Evaluate garment preservation and person-garment alignment.
- [Human pose generation evaluation](https://arxiv.org/search/?query=human+pose+conditioned+diffusion+benchmark&searchtype=all) *(resource)* — Evaluates pose-conditioned human generation.

### Datasets & Data Resources

- [MagicBrush](https://github.com/OSU-NLP-Group/MagicBrush) *(NeurIPS 2023 Datasets and Benchmarks)* — Instruction-guided image editing dataset with multi-turn annotations.
- [InstructPix2Pix dataset](https://github.com/timothybrooks/instruct-pix2pix) *(CVPR 2023 resource)* — Synthetic instruction-edit pairs for image editing.
- [COCO Captions](https://cocodataset.org/) *(ECCV 2014 / dataset)* — Common image-caption source for prompt grounding.
- [Visual Genome](https://homes.cs.washington.edu/~ranjay/visualgenome/) *(IJCV 2017 / dataset)* — Dense object, attribute, and relation annotations.
- [OpenImages](https://storage.googleapis.com/openimages/web/index.html) *(dataset)* — Large-scale object and visual relationship annotations.
- [ADE20K](https://groups.csail.mit.edu/vision/datasets/ADE20K/) *(CVPR 2017 / dataset)* — Scene parsing annotations for structural control.
- [LAION-5B](https://laion.ai/blog/laion-5b/) *(NeurIPS 2022 Datasets and Benchmarks)* — Web-scale image-text pretraining data.
- [LAION-Aesthetics](https://laion.ai/blog/laion-aesthetics/) *(dataset resource)* — Aesthetic-filtered image-text data.
- [CC3M](https://ai.google.com/research/ConceptualCaptions/) *(ACL 2018 / dataset)* — Web image-caption data for vision-language pretraining.
- [CC12M](https://github.com/google-research-datasets/conceptual-12m) *(CVPR 2021 / dataset)* — Larger conceptual-caption dataset.
- [SA-1B](https://segment-anything.com/dataset/index.html) *(ICCV 2023 / dataset)* — Large-scale segmentation masks for editing and control.
- [LVIS](https://www.lvisdataset.org/) *(CVPR 2019 / dataset)* — Long-tail instance annotations for object-level diagnostics.
- [DeepFashion](http://mmlab.ie.cuhk.edu.hk/projects/DeepFashion.html) *(CVPR 2016 / dataset)* — Fashion data for virtual try-on and garment consistency.
- [VITON-HD](https://github.com/shadow2496/VITON-HD) *(CVPR 2021 workshop / dataset)* — High-resolution virtual try-on data.
- [DressCode](https://github.com/aimagelab/dress-code) *(CVPR 2022 / dataset)* — Multi-category virtual try-on dataset.
- [OpenPose / pose datasets](https://arxiv.org/search/?query=pose+dataset+human+image+generation&searchtype=all) *(resource)* — Pose supervision for human-conditioned generation.
- [RefCOCO](https://arxiv.org/search/?query=RefCOCO+referring+expression&searchtype=all) *(dataset)* — Referring-expression grounding resource.
- [GQA](https://cs.stanford.edu/people/dorarad/gqa/) *(CVPR 2019 / dataset)* — Visual-question-answering resource for compositional reasoning.
- [CLEVR](https://cs.stanford.edu/people/jcjohns/clevr/) *(CVPR 2017 / dataset)* — Synthetic compositional reasoning dataset.
- [OCR/text rendering corpora](https://arxiv.org/search/?query=text+rendering+dataset+image+generation&searchtype=all) *(resource)* — Text-image data for typography generation.

## Internal consistency

Internal consistency asks whether generated states remain mutually compatible across identities, subjects, views, frames, videos, or story sequences.

### Methods

- [Textual Inversion](https://github.com/rinongal/textual_inversion) *(ICLR 2023)* — Learns new textual tokens for personalized concepts.
- [DreamBooth](https://dreambooth.github.io/) *(CVPR 2023)* — Finetunes T2I models for subject-driven generation.
- [Custom Diffusion](https://github.com/adobe-research/custom-diffusion) *(CVPR 2023)* — Efficiently customizes multiple concepts through parameter-efficient updates.
- [Perfusion](https://research.nvidia.com/labs/par/Perfusion/) *(SIGGRAPH 2023)* — Uses key-locking to preserve personalized concept identity.
- [SVDiff](https://arxiv.org/search/?query=SVDiff+personalization&searchtype=all) *(arXiv 2023)* — Parameter-efficient personalization via singular-vector updates.
- [P+](https://arxiv.org/search/?query=P%2B+textual+inversion&searchtype=all) *(arXiv 2023)* — Expands textual inversion representation capacity.
- [NeTI](https://arxiv.org/search/?query=NeTI+textual+inversion&searchtype=all) *(arXiv 2023)* — Uses neural textual inversion for richer concept embedding.
- [ProSpect](https://arxiv.org/search/?query=ProSpect+personalized+diffusion&searchtype=all) *(SIGGRAPH 2023 / arXiv)* — Personalizes without heavy finetuning.
- [DisenBooth](https://arxiv.org/search/?query=DisenBooth&searchtype=all) *(arXiv 2023)* — Disentangles identity and context for personalization.
- [SuTI](https://arxiv.org/search/?query=SuTI+subject+driven+text+to+image&searchtype=all) *(arXiv 2023)* — Scalable subject-driven text-to-image personalization.
- [BLIP-Diffusion](https://github.com/salesforce/LAVIS/tree/main/projects/blip-diffusion) *(NeurIPS 2023)* — Uses pretrained subject representations for controllable subject generation.
- [ELITE](https://github.com/csyxwei/ELITE) *(ICCV 2023)* — Encodes visual concepts into textual embeddings for fast personalization.
- [FastComposer](https://github.com/mit-han-lab/fastcomposer) *(NeurIPS 2023)* — Enables tuning-free multi-subject generation.
- [Subject-Diffusion](https://github.com/OPPO-Mente-Lab/Subject-Diffusion) *(ICCV 2023)* — Supports open-domain personalized subject generation.
- [PhotoMaker](https://github.com/TencentARC/PhotoMaker) *(CVPR 2024)* — Uses stacked ID embeddings for realistic human personalization.
- [InstantID](https://github.com/InstantID/InstantID) *(arXiv 2024)* — Provides zero-shot identity-preserving generation.
- [IP-Adapter-FaceID](https://github.com/tencent-ailab/IP-Adapter) *(arXiv 2023/2024)* — Preserves face identity through image-prompt adapters.
- [PuLID](https://github.com/ToTheBeginning/PuLID) *(arXiv 2024)* — Supports pure and lightning ID customization.
- [InfiniteYou](https://arxiv.org/search/?query=InfiniteYou+identity+diffusion&searchtype=all) *(arXiv / venue TBD)* — Explores scalable identity-consistent personalization.
- [RealCustom](https://arxiv.org/search/?query=RealCustom+personalized+diffusion&searchtype=all) *(arXiv / venue TBD)* — Focuses on realistic personalized concept generation.
- [InstantCharacter](https://arxiv.org/search/?query=InstantCharacter+diffusion&searchtype=all) *(arXiv / venue TBD)* — Builds fast character-consistent generation.
- [ConsiStory](https://github.com/NVlabs/consistory) *(arXiv 2024)* — Training-free consistent character generation across images.
- [StoryDiffusion](https://github.com/HVision-NKU/StoryDiffusion) *(NeurIPS 2024)* — Uses consistent self-attention for long-range image/video generation.
- [StyleAligned](https://style-aligned-gen.github.io/) *(SIGGRAPH 2024)* — Shares attention to preserve style across generated sets.
- [The Chosen One](https://omriavrahami.com/the-chosen-one/) *(SIGGRAPH Asia 2024)* — Generates consistent characters across text-to-image outputs.
- [ConsistentID](https://arxiv.org/abs/2404.16771) *(arXiv 2024)* — Preserves identity in portrait and character generation.
- [CharaConsist](https://arxiv.org/search/?query=CharaConsist&searchtype=all) *(arXiv / venue TBD)* — Studies fine-grained character consistency.
- [MagicID](https://arxiv.org/search/?query=MagicID+video+customization&searchtype=all) *(arXiv / venue TBD)* — Provides ID-conditioned video customization.
- [PersonalVideo](https://arxiv.org/search/?query=PersonalVideo+video+customization&searchtype=all) *(arXiv / venue TBD)* — Customizes video generation with personalized identity.
- [Phantom](https://arxiv.org/search/?query=Phantom+subject+consistent+video&searchtype=all) *(arXiv / venue TBD)* — Explores subject-consistent video generation.
- [Preserve and Personalize](https://rlgnswk.github.io/PreserveAndPersonalize_ProjectPage/) *(ICLR 2026)* — Preserves distributional behavior while personalizing concepts.
- [ConceptPrism](https://arxiv.org/search/?query=ConceptPrism&searchtype=all) *(CVPR 2026 / project)* — Disentangles concepts for personalized diffusion.
- [Zero-1-to-3](https://github.com/cvlab-columbia/zero123) *(ICCV 2023)* — Generates novel views from one image.
- [One-2-3-45](https://github.com/One-2-3-45/One-2-3-45) *(arXiv 2023)* — Produces multi-view images and 3D assets from a single image.
- [Zero123++](https://arxiv.org/search/?query=Zero123%2B%2B&searchtype=all) *(arXiv 2023)* — Improves single-image novel-view generation.
- [Cascade-Zero123](https://github.com/EnVision-Research/Cascade-Zero123) *(arXiv 2023)* — Cascades view generation for stronger 3D consistency.
- [Consistent123](https://arxiv.org/abs/2309.17261) *(arXiv 2023)* — Encourages cross-view consistency in novel-view synthesis.
- [SyncDreamer](https://github.com/liuyuan-pal/SyncDreamer) *(ICLR 2024)* — Synchronizes multi-view diffusion generation.
- [MVDream](https://github.com/bytedance/MVDream) *(ICLR 2024)* — Generates multi-view images with 3D-aware diffusion.
- [Wonder3D](https://github.com/xxlong0/Wonder3D) *(CVPR 2024)* — Reconstructs 3D assets from single images through multi-view diffusion.
- [ViewDiff](https://lukashoel.github.io/ViewDiff/) *(CVPR 2024)* — Enforces 3D consistency for text-to-image multi-view generation.
- [EscherNet](https://kxhit.github.io/EscherNet/) *(CVPR 2024)* — Performs scalable view synthesis under camera changes.
- [DreamGaussian](https://github.com/dreamgaussian/dreamgaussian) *(ICLR 2024)* — Uses 3D Gaussians for fast text/image-to-3D generation.
- [LGM](https://github.com/3DTopia/LGM) *(ECCV 2024)* — Reconstructs 3D Gaussians from sparse or generated views.
- [GRM](https://justimyhxu.github.io/projects/grm/) *(ECCV 2024)* — Builds large Gaussian reconstruction models.
- [Instant3D](https://arxiv.org/search/?query=Instant3D+diffusion&searchtype=all) *(arXiv / venue TBD)* — Accelerates 3D generation from sparse visual evidence.
- [TripoSR](https://github.com/VAST-AI-Research/TripoSR) *(arXiv 2024)* — Fast feed-forward 3D reconstruction from a single image.
- [CRM](https://arxiv.org/search/?query=CRM+3D+reconstruction+diffusion&searchtype=all) *(arXiv / venue TBD)* — Uses reconstruction priors for consistent 3D asset generation.
- [LRM](https://arxiv.org/search/?query=Large+Reconstruction+Model+3D&searchtype=all) *(ICLR 2024 / arXiv)* — Learns large reconstruction models for image-to-3D.
- [VideoLDM](https://research.nvidia.com/labs/toronto-ai/VideoLDM/) *(CVPR 2023)* — Extends latent diffusion to video generation.
- [Text2Video-Zero](https://github.com/Picsart-AI-Research/Text2Video-Zero) *(ICCV 2023)* — Adapts image diffusion to zero-shot video generation.
- [Tune-A-Video](https://github.com/showlab/Tune-A-Video) *(ICCV 2023)* — Tunes a T2I model for video generation from one video.
- [AnimateDiff](https://github.com/guoyww/AnimateDiff) *(ICLR 2024)* — Adds motion modules to personalized image diffusion models.
- [FateZero](https://github.com/ChenyangQiQi/FateZero) *(ICCV 2023)* — Uses attention fusion for zero-shot video editing.
- [Video-P2P](https://github.com/ShaoTengLiu/Video-P2P) *(arXiv 2023)* — Extends Prompt-to-Prompt-style editing to videos.
- [TokenFlow](https://diffusion-tokenflow.github.io/) *(ICLR 2024)* — Propagates diffusion features to improve temporal video editing consistency.
- [CoDeF](https://qiuyu96.github.io/CoDeF/) *(CVPR 2024)* — Uses content deformation fields for temporally consistent video processing.
- [Rerender A Video](https://www.mmlab-ntu.com/project/rerender/) *(SIGGRAPH Asia 2023)* — Performs zero-shot text-guided video-to-video translation.
- [COVE](https://github.com/wangjiangshan0725/COVE) *(arXiv 2024)* — Uses correspondence guidance for video editing.
- [VideoCrafter](https://github.com/AILab-CVC/VideoCrafter) *(arXiv 2023)* — Open video diffusion framework.
- [VideoCrafter2](https://github.com/AILab-CVC/VideoCrafter) *(CVPR 2024)* — Improves high-quality video diffusion generation.
- [ModelScopeT2V](https://github.com/modelscope/modelscope) *(project / 2023)* — Open text-to-video generation system.
- [Make-A-Video](https://arxiv.org/search/?query=Make-A-Video&searchtype=all) *(ICLR 2023 / arXiv)* — Generates videos from text using image-text and video data.
- [Imagen Video](https://arxiv.org/search/?query=Imagen+Video&searchtype=all) *(arXiv 2022)* — Cascaded video diffusion model.
- [Phenaki](https://arxiv.org/search/?query=Phenaki+video&searchtype=all) *(ICLR 2023 / arXiv)* — Generates long videos from open-domain prompts.
- [VideoFusion](https://arxiv.org/search/?query=VideoFusion+diffusion&searchtype=all) *(CVPR 2023 / arXiv)* — Uses decomposed diffusion for video generation.
- [Latte](https://arxiv.org/search/?query=Latte+video+diffusion&searchtype=all) *(TMLR / arXiv)* — Applies latent diffusion transformers to video generation.
- [VideoPoet](https://arxiv.org/search/?query=VideoPoet&searchtype=all) *(ICML 2024 / arXiv)* — Multimodal video generation and editing model.
- [Lumiere](https://arxiv.org/search/?query=Lumiere+video+diffusion&searchtype=all) *(SIGGRAPH 2024 / arXiv)* — Space-time diffusion model for coherent video generation.
- [Sora technical report](https://openai.com/research/video-generation-models-as-world-simulators) *(technical report 2024)* — Large-scale video generation model emphasizing world simulation properties.
- [MovieDreamer](https://arxiv.org/search/?query=MovieDreamer&searchtype=all) *(arXiv / venue TBD)* — Studies hierarchical long visual sequence generation.
- [TaleCrafter](https://arxiv.org/search/?query=TaleCrafter&searchtype=all) *(arXiv / venue TBD)* — Generates multi-character visual stories.
- [One-Prompt-One-Story](https://arxiv.org/search/?query=One-Prompt-One-Story&searchtype=all) *(arXiv / venue TBD)* — Aims at consistent story generation from a single prompt.
- [Animate-A-Story](https://github.com/AILab-CVC/Animate-A-Story) *(arXiv 2023)* — Generates storytelling videos with retrieval and control signals.
- [MotionStream](https://openreview.net/forum?id=v1DKz5Vxr7) *(ICLR 2026)* — Supports real-time video generation with interactive motion control.
- [VideoDirectorGPT](https://arxiv.org/search/?query=VideoDirectorGPT&searchtype=all) *(arXiv 2023)* — Uses LLM planning for multi-scene video generation.
- [ShotAdapter](https://arxiv.org/search/?query=ShotAdapter+text+to+multi-shot+video&searchtype=all) *(arXiv / venue TBD)* — Adapts video generation for multi-shot consistency.
- [VideoBooth](https://arxiv.org/search/?query=VideoBooth&searchtype=all) *(arXiv 2023)* — Customizes video generation to a subject or concept.
- [DreamVideo](https://arxiv.org/search/?query=DreamVideo&searchtype=all) *(arXiv 2023)* — Personalizes video generation with subject-aware priors.
- [Vlogger](https://arxiv.org/search/?query=Vlogger+video+generation&searchtype=all) *(arXiv 2024)* — Generates talking/head or human-centric video content.
- [MagicAnimate](https://github.com/magic-research/magic-animate) *(CVPR 2024)* — Animates human images under motion guidance.
- [AnimateAnyone](https://arxiv.org/search/?query=AnimateAnyone&searchtype=all) *(CVPR 2024 / arXiv)* — Animates reference characters with strong identity preservation.
- [Champ](https://arxiv.org/search/?query=Champ+controllable+human+image+animation&searchtype=all) *(arXiv 2024)* — Enables controllable and consistent human animation.

### Benchmarks & Evaluators

- [MVG-Bench](https://github.com/xiexh20/MVGBench) *(arXiv 2024)* — Evaluates multi-view generation consistency.
- [MET3R](https://github.com/mohammadasim98/met3r) *(arXiv 2024)* — Measures 3D-aware multi-view consistency from generated images.
- [VBench](https://github.com/Vchitect/VBench) *(CVPR 2024)* — Comprehensive video generation benchmark including subject/background and temporal consistency.
- [Video-Bench](https://github.com/Video-Bench/Video-Bench) *(CVPR 2025)* — Human-aligned video generation benchmark.
- [EvalCrafter](https://github.com/evalcrafter/EvalCrafter) *(CVPR 2024)* — Evaluates generated videos along visual, text-video, and motion dimensions.
- [FETV](https://github.com/llyx97/FETV) *(NeurIPS 2023 Datasets and Benchmarks)* — Fine-grained open-domain text-to-video evaluation benchmark.
- [ViStoryBench](https://github.com/ViStoryBench/ViStoryBench) *(CVPR 2026 / preprint)* — Evaluates story visualization, character consistency, and narrative coherence.
- [T2V-CompBench](https://arxiv.org/search/?query=T2V-CompBench&searchtype=all) *(arXiv / venue TBD)* — Tests compositional text-to-video generation.
- [VideoScore](https://arxiv.org/search/?query=VideoScore+video+generation+evaluation&searchtype=all) *(arXiv / venue TBD)* — Provides learned or automatic video generation quality scoring.
- [VideoPhy temporal subset](https://github.com/Hritikbansal/videophy) *(ICLR 2025)* — Uses physical video checks as temporal/world consistency diagnostics.
- [Long-video consistency evaluation](https://arxiv.org/search/?query=long+video+consistency+benchmark&searchtype=all) *(resource)* — Focuses on long-horizon entity and scene persistence.
- [Character consistency benchmark](https://arxiv.org/search/?query=character+consistency+benchmark+text+to+image&searchtype=all) *(resource)* — Tests identity preservation across generated sets.
- [Multi-view consistency metrics](https://arxiv.org/search/?query=multi-view+consistency+metric+generated+images&searchtype=all) *(resource)* — Measures cross-view geometric compatibility.
- [Story visualization benchmark](https://arxiv.org/search/?query=story+visualization+benchmark+consistency&searchtype=all) *(resource)* — Tests narrative and character persistence in story sequences.
- [Video editing consistency metrics](https://arxiv.org/search/?query=video+editing+consistency+metric+diffusion&searchtype=all) *(resource)* — Measures preservation and temporal stability after video editing.
- [CLIP frame consistency](https://arxiv.org/search/?query=CLIP+frame+consistency+video+generation&searchtype=all) *(metric family)* — Uses semantic features to estimate cross-frame consistency.
- [DINO tracking consistency](https://arxiv.org/search/?query=DINO+tracking+consistency+video+generation&searchtype=all) *(metric family)* — Uses self-supervised features for object/region persistence.
- [Identity similarity metrics](https://arxiv.org/search/?query=identity+similarity+metric+personalized+generation&searchtype=all) *(metric family)* — Evaluates subject or face identity preservation.
- [Face recognition metrics](https://arxiv.org/search/?query=face+identity+metric+diffusion+generation&searchtype=all) *(metric family)* — Uses face recognition models for identity consistency.
- [LPIPS temporal smoothness](https://arxiv.org/search/?query=LPIPS+temporal+smoothness+video+generation&searchtype=all) *(metric family)* — Measures perceptual smoothness across frames.

### Datasets & Data Resources

- [MeViS](https://github.com/henghuiding/MeViS) *(ICCV 2023)* — Motion-expression video segmentation data useful for temporal grounding.
- [MOSE](https://github.com/henghuiding/MOSE-api) *(ICCV 2023 / dataset)* — Video object segmentation data with complex occlusions.
- [TAO](https://github.com/TAO-Dataset/tao) *(ECCV 2020)* — Long-tail tracking data for object persistence diagnostics.
- [VSPW](https://github.com/VSPW-dataset/VSPW_code) *(CVPR 2021)* — Video scene parsing dataset for scene-state continuity.
- [nuScenes](https://github.com/nutonomy/nuscenes-devkit) *(CVPR 2020)* — Driving dataset useful for dynamic-scene consistency.
- [KITTI](https://www.cvlibs.net/datasets/kitti/) *(IJRR 2013 / dataset)* — Autonomous-driving visual dataset for geometry and temporal checks.
- [Waymo Open Dataset](https://waymo.com/open/) *(CVPR 2020 / dataset)* — Large-scale driving data for world and motion consistency.
- [DAVIS](https://davischallenge.org/) *(CVPR 2016 / dataset)* — Video object segmentation data for temporal preservation.
- [YouTube-VOS](https://youtube-vos.org/) *(ECCV 2018 / dataset)* — Large-scale video object segmentation data.
- [LaSOT](https://cis.temple.edu/lasot/) *(CVPR 2019 / dataset)* — Long-term single-object tracking dataset.
- [TrackingNet](https://tracking-net.org/) *(ECCV 2018 / dataset)* — Large-scale object tracking data.
- [Objaverse](https://objaverse.allenai.org/) *(CVPR 2023 / dataset)* — Large 3D object dataset for view and 3D generation.
- [Objaverse-XL](https://objaverse.allenai.org/objaverse-xl/) *(NeurIPS 2023 Datasets and Benchmarks)* — Web-scale 3D object data.
- [CO3D](https://github.com/facebookresearch/co3d) *(ICCV 2021 / dataset)* — Common objects in 3D data for view consistency.
- [RealEstate10K](https://google.github.io/realestate10k/) *(dataset)* — Camera-trajectory video data for novel-view synthesis.
- [ScanNet](http://www.scan-net.org/) *(CVPR 2017 / dataset)* — RGB-D scene data for geometry-aware generation.
- [ShapeNet](https://shapenet.org/) *(arXiv 2015 / dataset)* — 3D shape dataset for object-level 3D generation.
- [Google Scanned Objects](https://research.google/tools/datasets/google-scanned-objects/) *(dataset)* — High-quality scanned object assets.
- [MVImgNet](https://github.com/GAP-LAB-CUHK-SZ/MVImgNet) *(CVPR 2023 / dataset)* — Multi-view image dataset for object-centric reconstruction.
- [Kubric](https://github.com/google-research/kubric) *(CVPR 2022 / dataset generator)* — Synthetic video/scene data generation for controlled temporal diagnostics.

## Normative consistency

Normative consistency asks whether generated content satisfies evaluative principles such as preference, aesthetics, safety, fairness, concept restrictions, physical plausibility, commonsense, action consequence, and world-state validity.

### Methods

- [Pick-a-Pic / PickScore](https://github.com/yuvalkirstain/PickScore) *(NeurIPS 2023)* — Collects pairwise preferences and trains a preference scorer.
- [ImageReward](https://github.com/zai-org/ImageReward) *(NeurIPS 2023)* — Learns a general human preference reward model for T2I images.
- [HPS](https://arxiv.org/search/?query=Human+Preference+Score+text+to+image&searchtype=all) *(ICCV 2023 / arXiv)* — Scores generated images according to human preference.
- [HPSv2](https://github.com/tgxs002/HPSv2) *(arXiv 2023)* — Refines human preference scoring and benchmark coverage.
- [HPSv3](https://github.com/MizzenAI/HPSv3) *(arXiv 2025)* — Extends preference evaluation to broader text-image distributions.
- [MPS](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Learning_Multi-Dimensional_Human_Preference_for_Text-to-Image_Generation_CVPR_2024_paper.html) *(CVPR 2024)* — Models multi-dimensional human preferences for T2I generation.
- [VisionReward](https://github.com/zai-org/VisionReward) *(AAAI 2026)* — Learns multi-dimensional reward signals for image and video generation.
- [Diffusion-DPO](https://github.com/SalesforceAIResearch/DiffusionDPO) *(NeurIPS 2023 / arXiv)* — Applies direct preference optimization to diffusion models.
- [DDPO](https://github.com/jannerm/ddpo) *(ICLR 2024)* — Trains diffusion models with reinforcement learning rewards.
- [AlignProp](https://arxiv.org/abs/2310.03739) *(ICLR 2024 / arXiv)* — Backpropagates reward gradients through diffusion sampling.
- [DPOK](https://arxiv.org/abs/2305.16381) *(arXiv 2023)* — Applies KL-regularized policy optimization to diffusion models.
- [D3PO](https://arxiv.org/abs/2402.08385) *(arXiv 2024)* — Optimizes diffusion policies from preference data.
- [SPO](https://openaccess.thecvf.com/content/CVPR2025/html/Liang_Aesthetic_Post-Training_Diffusion_Models_from_Generic_Preferences_with_Step-by-step_Preference_CVPR_2025_paper.html) *(CVPR 2025)* — Performs step-by-step preference optimization for aesthetic post-training.
- [DSPO](https://openreview.net/forum?id=7f70331dbe58ad59d83941dfa7d975aa) *(ICLR 2025)* — Aligns diffusion models using direct score preference optimization.
- [RankDPO](https://openaccess.thecvf.com/content/ICCV2025/papers/Karthik_Scalable_Ranked_Preference_Optimization_for_Text-to-Image_Generation_ICCV_2025_paper.pdf) *(ICCV 2025)* — Uses ranked preference data for scalable T2I preference optimization.
- [CMPO / CaPO](https://openaccess.thecvf.com/content/CVPR2025/html/Lee_Calibrated_Multi-Preference_Optimization_for_Aligning_Diffusion_Models_CVPR_2025_paper.html) *(CVPR 2025)* — Calibrates multiple preferences for diffusion alignment.
- [Diffusion-NPO](https://openreview.net/forum?id=BADtQ9p1T2) *(ICLR 2026)* — Performs negative preference optimization for diffusion alignment.
- [BranchGRPO](https://openreview.net/forum?id=93N8hU2q5V) *(ICLR 2026)* — Uses branch-level GRPO-style optimization for diffusion generation.
- [Flow-GRPO](https://arxiv.org/search/?query=Flow-GRPO+diffusion&searchtype=all) *(arXiv / venue TBD)* — Applies GRPO-like preference learning to flow/diffusion sampling.
- [RLAIF for Diffusion](https://arxiv.org/search/?query=RLAIF+diffusion+text+to+image&searchtype=all) *(topic / resource)* — Uses AI feedback instead of human feedback for diffusion alignment.
- [Safe Latent Diffusion](https://github.com/ml-research/safe-latent-diffusion) *(CVPR 2023)* — Adds safety guidance during latent diffusion sampling.
- [Erasing Concepts from Diffusion Models](https://github.com/rohitgandikota/erasing) *(ICCV 2023)* — Removes undesirable concepts from diffusion weights.
- [Ablating Concepts](https://www.cs.cmu.edu/~concept-ablation/) *(ICCV 2023)* — Ablates target concepts while retaining general model behavior.
- [Unified Concept Editing](https://github.com/rohitgandikota/unified-concept-editing) *(WACV 2024 / arXiv)* — Edits multiple concepts in diffusion models.
- [MACE](https://arxiv.org/abs/2403.06135) *(CVPR 2024 / arXiv)* — Scales concept erasure to many concepts.
- [Forget-Me-Not](https://arxiv.org/abs/2303.17591) *(arXiv 2023)* — Uses attention control to forget concepts.
- [Ring-A-Bell](https://github.com/chiayi-hsu/Ring-A-Bell) *(NeurIPS 2023 workshop / arXiv)* — Red-teams concept erasure using adversarial prompts.
- [ACE](https://arxiv.org/search/?query=anti+editing+concept+erasure+diffusion&searchtype=all) *(arXiv / venue TBD)* — Studies robust anti-editing concept erasure.
- [Editing Massive Concepts](https://arxiv.org/search/?query=editing+massive+concepts+text+to+image+diffusion&searchtype=all) *(arXiv / venue TBD)* — Edits or suppresses many concepts at scale.
- [SalUn](https://arxiv.org/search/?query=SalUn+machine+unlearning+diffusion&searchtype=all) *(ICLR 2024 / arXiv)* — Uses saliency-guided unlearning for generative models.
- [ESD](https://arxiv.org/search/?query=ESD+erasing+stable+diffusion&searchtype=all) *(arXiv 2023)* — Erases stable-diffusion concepts through targeted training.
- [ConceptPrune](https://arxiv.org/search/?query=ConceptPrune+diffusion&searchtype=all) *(arXiv / venue TBD)* — Removes concepts by pruning or editing model components.
- [Responsible Text-to-Image Diffusion](https://arxiv.org/search/?query=Responsible+Text-to-Image+Diffusion&searchtype=all) *(ICML 2026 / project)* — Studies controllable and interpretable safe/fair generation.
- [T2VSafetyBench methods](https://arxiv.org/abs/2409.08615) *(arXiv 2024)* — Studies safety evaluation and intervention for text-to-video models.
- [SafeGen](https://arxiv.org/search/?query=SafeGen+diffusion&searchtype=all) *(arXiv / venue TBD)* — Improves safety during generative sampling.
- [Safety Checker / post-hoc filters](https://arxiv.org/search/?query=diffusion+safety+checker+post-hoc+filter&searchtype=all) *(system resource)* — Filters generated outputs after sampling.
- [NSFW prompt filtering](https://arxiv.org/search/?query=NSFW+prompt+filtering+text+to+image&searchtype=all) *(system resource)* — Screens prompts before generation.
- [Adversarial prompt defense](https://arxiv.org/search/?query=adversarial+prompt+defense+text-to-image+diffusion&searchtype=all) *(topic / resource)* — Defends against jailbreak prompts in visual generation.
- [Jailbreak-resistant diffusion](https://arxiv.org/search/?query=jailbreak+text-to-image+diffusion+safety&searchtype=all) *(topic / resource)* — Studies robust safety under prompt attacks.
- [Concept restoration after erasure](https://arxiv.org/search/?query=concept+erasure+benign+retention+diffusion&searchtype=all) *(topic / resource)* — Diagnoses benign capability loss after safety editing.
- [UniSim](https://openreview.net/forum?id=sFyTZEqmUY) *(ICLR 2024)* — Learns interactive real-world simulators for action-conditioned generation.
- [Genie](https://proceedings.mlr.press/v235/bruce24a.html) *(ICML 2024)* — Generates interactive environments from videos.
- [GAIA-1](https://wayve.ai/thinking/gaia-1/) *(arXiv / technical report 2023)* — Builds a generative world model for autonomous driving.
- [WorldDreamer](https://arxiv.org/abs/2401.09985) *(arXiv 2024)* — Generates driving videos with world-model priors.
- [DriveDreamer](https://arxiv.org/search/?query=DriveDreamer&searchtype=all) *(ECCV 2024 / arXiv)* — Generates driving scenarios with structured controls.
- [DriveDreamer-2](https://arxiv.org/search/?query=DriveDreamer-2&searchtype=all) *(arXiv / venue TBD)* — Extends driving world generation to longer/higher-quality videos.
- [Vista](https://arxiv.org/search/?query=Vista+world+model+video+generation&searchtype=all) *(arXiv / venue TBD)* — Studies video world models for controllable environments.
- [Pandora](https://arxiv.org/search/?query=Pandora+world+model+video+generation&searchtype=all) *(arXiv / venue TBD)* — Explores world modeling through video generation.
- [Cosmos World Foundation Models](https://arxiv.org/search/?query=Cosmos+world+foundation+models&searchtype=all) *(technical report / arXiv)* — Studies large-scale world foundation models.
- [HunyuanWorld / Hunyuan World](https://arxiv.org/search/?query=Hunyuan+World+world+model&searchtype=all) *(technical report / arXiv)* — Generates 3D/world environments using generative world modeling.
- [World-consistent Video Diffusion](https://arxiv.org/search/?query=world+consistent+video+diffusion&searchtype=all) *(topic / resource)* — Enforces geometry, dynamics, and state consistency in video generation.
- [Physics-guided Diffusion](https://arxiv.org/search/?query=physics-guided+diffusion+generation&searchtype=all) *(topic / resource)* — Injects physical constraints into diffusion sampling or training.
- [Simulator-guided Diffusion](https://arxiv.org/search/?query=simulator-guided+diffusion+generation&searchtype=all) *(topic / resource)* — Uses simulators or constraints to steer generation.
- [Verifier-guided Generation](https://arxiv.org/search/?query=verifier-guided+diffusion+generation&searchtype=all) *(topic / resource)* — Uses post-hoc or in-loop verifiers to reject inconsistent samples.
- [Causal Video Generation](https://arxiv.org/search/?query=causal+video+generation+diffusion&searchtype=all) *(topic / resource)* — Studies causal state transitions in generated videos.
- [Object-state-change Generation](https://arxiv.org/search/?query=object+state+change+text-to-video+generation&searchtype=all) *(topic / resource)* — Focuses on object state changes and action consequences.
- [Embodied Diffusion World Models](https://arxiv.org/search/?query=embodied+world+model+diffusion&searchtype=all) *(topic / resource)* — Connects diffusion generation with embodied planning and control.

### Benchmarks & Evaluators

- [Pick-a-Pic / PickScore](https://github.com/yuvalkirstain/PickScore) *(NeurIPS 2023)* — Pairwise preference data and reward model for T2I outputs.
- [ImageReward](https://github.com/zai-org/ImageReward) *(NeurIPS 2023)* — Learned reward model for human preference evaluation.
- [HPSv2](https://github.com/tgxs002/HPSv2) *(arXiv 2023)* — Human preference benchmark for T2I evaluation.
- [HPSv3](https://github.com/MizzenAI/HPSv3) *(arXiv 2025)* — Wide-spectrum preference benchmark and reward model.
- [VisionReward](https://github.com/zai-org/VisionReward) *(AAAI 2026)* — Multi-dimensional image/video preference evaluator.
- [MPS evaluation](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Learning_Multi-Dimensional_Human_Preference_for_Text-to-Image_Generation_CVPR_2024_paper.html) *(CVPR 2024)* — Evaluates multiple dimensions of human preference.
- [Aesthetic score models](https://arxiv.org/search/?query=aesthetic+score+text-to-image+diffusion&searchtype=all) *(metric family)* — Score visual aesthetics for generated images.
- [LAION aesthetic predictor](https://laion.ai/blog/laion-aesthetics/) *(dataset/model resource)* — Provides aesthetic scores for LAION-like data.
- [Six-CD](https://github.com/Artanisax/Six-CD) *(arXiv / venue TBD)* — Evaluates concept removal and benign retention.
- [I2P](https://arxiv.org/search/?query=I2P+inappropriate+image+prompts&searchtype=all) *(arXiv 2023)* — Prompt benchmark for inappropriate image generation risks.
- [Unsafe Diffusion benchmark](https://arxiv.org/search/?query=unsafe+diffusion+benchmark&searchtype=all) *(resource)* — Evaluates unsafe output generation.
- [T2VSafetyBench](https://arxiv.org/abs/2409.08615) *(arXiv 2024)* — Safety benchmark for text-to-video generation.
- [Concept removal benchmarks](https://arxiv.org/search/?query=concept+removal+benchmark+diffusion&searchtype=all) *(resource)* — Measures erasure success and collateral damage.
- [Benign retention benchmarks](https://arxiv.org/search/?query=benign+retention+concept+erasure+diffusion&searchtype=all) *(resource)* — Tests whether safe editing harms benign generations.
- [Red-teaming prompts](https://arxiv.org/search/?query=red+teaming+text-to-image+diffusion+prompts&searchtype=all) *(resource)* — Stress-tests safety filters and concept removal.
- [PhyBench](https://github.com/OpenGVLab/PhyBench) *(arXiv 2024)* — Static physical commonsense benchmark for T2I.
- [VideoPhy](https://github.com/Hritikbansal/videophy) *(ICLR 2025)* — Physical commonsense benchmark for generated videos.
- [PhyCoBench](https://github.com/Jeckinchen/PhyCoBench) *(arXiv 2024)* — Optical-flow-guided physical coherence benchmark.
- [PhyGenBench](https://github.com/OpenGVLab/PhyGenBench) *(arXiv 2024)* — Physical-law benchmark for video generation.
- [VideoPhy-2](https://videophy2.github.io/) *(ICLR 2026)* — Action-centric physical commonsense benchmark.
- [T2VPhysBench](https://arxiv.org/search/?query=T2VPhysBench&searchtype=all) *(arXiv / venue TBD)* — Tests first-principles physical consistency in T2V.
- [T2VWorldBench](https://arxiv.org/search/?query=T2VWorldBench&searchtype=all) *(arXiv / venue TBD)* — Evaluates world knowledge, commonsense, and causal plausibility.
- [Physics-IQ](https://github.com/google-deepmind/physics-IQ-benchmark) *(WACV 2026)* — Tests physical principles in generative video models.
- [PhyWorldBench](https://github.com/g-jing/phy-world-bench) *(arXiv 2025)* — Benchmarks physical realism in text-to-video generation.
- [VideoVerse](https://github.com/Zeqing-Wang/VideoVerse) *(arXiv 2025)* — World-model-oriented T2V evaluation.
- [PhyEduVideo](https://github.com/meghamariamkm/PhyEduVideo) *(WACV 2026)* — Physics-education-oriented video benchmark.
- [PhyWorld](https://proceedings.mlr.press/v267/kang25g.html) *(ICML 2025)* — Studies how far video generation is from physical world models.
- [OSCBench](https://arxiv.org/search/?query=OSCBench+Object+State+Change+Text-to-Video&searchtype=all) *(arXiv / venue TBD)* — Tests object state change and action consequence.
- [Morpheus](https://arxiv.org/search/?query=Morpheus+physical+reasoning+video+generative+models&searchtype=all) *(arXiv / venue TBD)* — Evaluates physical reasoning in video generation.
- [World-model Video Evaluation](https://arxiv.org/search/?query=world+model+evaluation+video+generation+benchmark&searchtype=all) *(resource)* — General benchmarks for video-as-world-model behavior.

### Datasets & Data Resources

- [Pick-a-Pic dataset](https://github.com/yuvalkirstain/PickScore) *(NeurIPS 2023)* — Pairwise human preferences for generated images.
- [ImageRewardDB](https://github.com/zai-org/ImageReward) *(NeurIPS 2023 resource)* — Human preference annotations for reward training.
- [HPD / HPSv2 data](https://github.com/tgxs002/HPSv2) *(arXiv 2023 resource)* — Human preference data for T2I evaluation.
- [HPDv3 / HPSv3 data](https://github.com/MizzenAI/HPSv3) *(arXiv 2025 resource)* — Larger preference dataset for wide-spectrum evaluation.
- [MPS preference data](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Learning_Multi-Dimensional_Human_Preference_for_Text-to-Image_Generation_CVPR_2024_paper.html) *(CVPR 2024)* — Multi-dimensional preference labels.
- [LAION-Aesthetics](https://laion.ai/blog/laion-aesthetics/) *(dataset resource)* — Image-text data filtered by aesthetic scores.
- [AVA Aesthetics](https://arxiv.org/search/?query=AVA+dataset+aesthetics&searchtype=all) *(CVPR 2012 / dataset)* — Aesthetic image-quality annotations.
- [I2P prompts](https://arxiv.org/search/?query=I2P+inappropriate+image+prompts&searchtype=all) *(arXiv 2023 resource)* — Inappropriate prompt set for safety testing.
- [NSFW prompt resources](https://arxiv.org/search/?query=NSFW+prompt+dataset+text+to+image&searchtype=all) *(resource)* — Prompts for unsafe content testing.
- [Concept erasure prompt sets](https://arxiv.org/search/?query=concept+erasure+prompt+set+diffusion&searchtype=all) *(resource)* — Prompts for target concept removal.
- [Physical commonsense prompts](https://arxiv.org/search/?query=physical+commonsense+prompts+text+to+image&searchtype=all) *(resource)* — Prompts testing static physical plausibility.
- [Video physical prompts](https://arxiv.org/search/?query=physical+commonsense+prompts+text+to+video&searchtype=all) *(resource)* — Prompts testing dynamic physical plausibility.
- [Driving world-model datasets](https://arxiv.org/search/?query=driving+world+model+dataset+video+generation&searchtype=all) *(resource)* — Driving data for action-conditioned world models.
- [Ego4D](https://ego4d-data.org/) *(CVPR 2022 / dataset)* — Egocentric video data for embodied and action reasoning.
- [Something-Something V2](https://developer.qualcomm.com/software/ai-datasets/something-something) *(ICCV 2017 / dataset)* — Human-object interaction videos for action/state understanding.
- [CLEVRER](https://clevrer.csail.mit.edu/) *(ICLR 2020 / dataset)* — Synthetic videos for physical and causal reasoning.
- [PHYRE](https://phyre.ai/) *(NeurIPS 2019 / benchmark)* — Physical reasoning environments.
- [IntPhys](https://arxiv.org/search/?query=IntPhys+physical+reasoning+dataset&searchtype=all) *(arXiv 2018 / dataset)* — Intuitive physics video dataset.
- [CLEVR](https://cs.stanford.edu/people/jcjohns/clevr/) *(CVPR 2017 / dataset)* — Synthetic visual reasoning data.
- [Kubric](https://github.com/google-research/kubric) *(CVPR 2022)* — Synthetic scene/video generator useful for controlled physical diagnostics.

## Machine-readable resources

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

Contributions are welcome. Please include the resource title, BibTeX key, venue/year, official paper URL, official project/code URL if available, resource type, modality, primary consistency relation, coverage values, and a short diagnostic-use/blind-spot description.

Use the issue template: [Add or correct a resource](.github/ISSUE_TEMPLATE/resource_addition.yml).

## Maintenance notes

Some 2025--2026 papers may initially appear as arXiv or project-page entries before official proceedings metadata is stable. When official BibTeX becomes available, please update [`resources/selected_bibtex.bib`](resources/selected_bibtex.bib) and any corresponding table entries.

When adding links, prefer official repositories or project pages over unofficial reimplementations. If no stable official repository exists, leave the code URL blank in the CSV table. Entries with arXiv-search links are included as expansion placeholders and should be replaced by stable paper/project links when available.

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
