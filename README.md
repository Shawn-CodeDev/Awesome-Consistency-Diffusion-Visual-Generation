# Awesome Consistency in Diffusion-Based Visual Generation

[![Validate resource tables](https://github.com/Shawn-CodeDev/Awesome-Consistency-Diffusion-Visual-Generation/actions/workflows/validate-resources.yml/badge.svg)](https://github.com/Shawn-CodeDev/Awesome-Consistency-Diffusion-Visual-Generation/actions/workflows/validate-resources.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

This repository accompanies the survey:

> **Consistency in Diffusion-Based Visual Generation: A Survey**  
> Song Yan, Wei Zhai, Chenfeng Wang, Ruixuan Li, Zhangping Yang, Yancheng Cai, Tao Zhang, Ling Wang, Yunwei Lan, Yujie He, Yang Cao, Min Li, Zheng-Jun Zha.

This repository provides a curated and structured resource map for **consistency problems in diffusion-based visual generation**. Instead of organizing the literature only by task names such as text-to-image generation, editing, personalization, video generation, or 3D generation, this project organizes methods and resources by the **agreement relation** they try to enforce.

## Why this repository exists

Diffusion models now generate high-quality images, videos, 3D-aware assets, and interactive visual content. However, perceptual quality alone does not guarantee consistency. A visually realistic sample may still ignore objects, attributes, counts, or relations in the prompt; fail to preserve unedited content during editing; lose subject identity across images or scenes; disagree across viewpoints; flicker across frames; forget narrative entities; or violate preference, safety, physical, or causal constraints.

Existing surveys usually follow task or modality boundaries. This repository instead treats consistency as a family of **generation-time agreement requirements**, making it easier to compare methods, benchmarks, diagnostic resources, and trade-offs across tasks.

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

| Relation | Agreement target | Representative failures | Representative settings |
|---|---|---|---|
| **External consistency** | Agreement with conditions specified outside the generated sample | prompt omission, attribute misbinding, counting error, control mismatch, over-editing | prompt following, compositional generation, structural control, layout/pose/depth conditioning, instruction-based editing |
| **Internal consistency** | Agreement among generated parts, views, instances, frames, or story states | identity drift, cross-view disagreement, temporal flicker, narrative forgetting | personalization, multi-view generation, 3D-aware generation, video generation, story visualization |
| **Normative consistency** | Agreement with evaluative principles not fully specified by the prompt | low preference, unsafe output, physical implausibility, causal violation | preference alignment, safety editing, concept removal, physical commonsense evaluation, world-model diagnostics |

The survey also uses four auxiliary axes: observation unit, agreement target, optimization locus, and evidence source. See [`docs/taxonomy.md`](docs/taxonomy.md) and [`resources/taxonomy_methods.csv`](resources/taxonomy_methods.csv) for the machine-readable taxonomy map.

## Curated papers and resources

Links point to an official paper, project page, OpenReview page, arXiv page, or code repository when a stable public link is available. The machine-readable benchmark/evaluator table is maintained in [`resources/benchmark_coverage.csv`](resources/benchmark_coverage.csv).

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
| LLM-grounded Diffusion | 2023 | LLM-generated layout and grounded prompt understanding | [Project](https://llm-grounded-diffusion.github.io/) |
| MultiDiffusion: Fusing Diffusion Paths for Controlled Image Generation | 2023 | optimization-based fusion of regional diffusion paths | [Project](https://multidiffusion.github.io/) |
| RPG: Recaption, Plan, and Generate | 2024 | MLLM-based planning for complex compositional prompts | [Code](https://github.com/YangLing0818/RPG-DiffusionMaster) |
| StructureDiffusion | 2022/2023 | structured prompt understanding for compositional generation | [Paper](https://arxiv.org/abs/2212.05032) |
| SynGen | 2023 | syntactic guidance for compositional text-to-image synthesis | [Paper](https://arxiv.org/abs/2308.07037) |
| Make-It-Count | 2024 | count-aware text-to-image generation | Link to be added |
| CountDiffusion | 2024 | training-free counting guidance | Link to be added |
| YOLO-Count | 2024 | differentiable object counting for T2I | Link to be added |

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
| UniControl | 2023/2024 | unified controllable text-to-image generation | [Paper](https://arxiv.org/abs/2305.11147) |
| Uni-ControlNet | 2023/2024 | unified multi-condition control with ControlNet-style branches | [Paper](https://arxiv.org/abs/2305.16322) |
| Ctrl-Adapter | ICLR 2025 | efficient adapters for diverse controls | [OpenReview](https://openreview.net/forum?id=ny8T8OuNHe) |
| UniCon | ICLR 2025 | unidirectional information flow for effective large-scale control | [OpenReview](https://openreview.net/forum?id=8jb0e1gLyd) |
| InstanceDiffusion | CVPR 2024 | instance-level text-to-image generation | [Project](https://people.eecs.berkeley.edu/~xdwang/projects/instancediffusion/) |
| SemanticControl | 2024 | training-free semantic condition control | Link to be added |
| LayoutDM / LayoutDiffusion / layout-generation resources | 2023--2024 | layout-centric generation and structural design | Links to be added |
| PosterCraft / CreatiPoster / PosterMaker | 2024--2025 | poster and graphic-layout applications | Links to be added |
| TryOnDiffusion / StableVITON / AnyDressing | 2023--2025 | virtual try-on and dressing applications | Links to be added |

#### Edit consistency and preservation

| Paper / resource | Year / venue | Role | Links |
|---|---:|---|---|
| SDEdit: Guided Image Synthesis and Editing with Stochastic Differential Equations | ICLR 2022 | noise-and-denoise image editing prior | [Paper](https://arxiv.org/abs/2108.01073) |
| Prompt-to-Prompt Image Editing with Cross-Attention Control | ICLR 2023 | cross-attention control for edit preservation | [Code](https://github.com/google/prompt-to-prompt) |
| DiffEdit: Diffusion-Based Semantic Image Editing with Mask Guidance | ICLR 2023 | prompt-difference mask and localized editing | [Project](https://github.com/Xiang-cd/DiffEdit-stable-diffusion) |
| InstructPix2Pix: Learning to Follow Image Editing Instructions | CVPR 2023 | instruction-guided image editing | [Code](https://github.com/timothybrooks/instruct-pix2pix) |
| InstructDiffusion | 2023/2024 | unified instruction-based diffusion editing | [Code](https://github.com/cientgu/InstructDiffusion) |
| Null-Text Inversion for Editing Real Images using Guided Diffusion Models | CVPR 2023 | inversion-based real-image editing | [Project](https://null-text-inversion.github.io/) |
| Imagic: Text-Based Real Image Editing with Diffusion Models | CVPR 2023 | text-based real-image editing | [Project](https://imagic-editing.github.io/) |
| Paint-by-Example: Exemplar-based Image Editing with Diffusion Models | CVPR 2023 | exemplar-guided editing | [Code](https://github.com/Fantasy-Studio/Paint-by-Example) |
| Plug-and-Play Diffusion Features | CVPR 2023 | feature injection for semantic image editing | [Project](https://pnp-diffusion.github.io/) |
| Pix2Pix-Zero: Zero-shot Image-to-Image Translation | ICCV 2023 | zero-shot editing with cross-attention guidance | [Project](https://pix2pixzero.github.io/) |
| MasaCtrl: Mutual Self-Attention Control | ICCV 2023 | mutual self-attention for consistent synthesis and editing | [Code](https://github.com/TencentARC/MasaCtrl) |
| LEDITS++ | 2024 | inversion-free semantic editing and erasure | [Paper](https://arxiv.org/abs/2311.16711) |
| DragonDiffusion / DiffEditor | 2024 | fine-grained object moving, resizing, and content dragging | [Code](https://github.com/MC-E/DragonDiffusion) |
| DragDiffusion: Interactive Point-based Image Editing | CVPR 2024 | drag-based point editing | [Code](https://github.com/Yujun-Shi/DragDiffusion) |
| EditBench / Imagen Editor | CVPR 2023 | text-guided image inpainting benchmark | Paper / official code unavailable |
| MagicBrush | NeurIPS 2023 Datasets and Benchmarks | instruction-guided editing dataset | [Code](https://github.com/OSU-NLP-Group/MagicBrush) |
| ConceptBed | 2024 | concept-learning and concept-binding evaluation | [Code](https://github.com/ConceptBed/evaluations) |

### Internal consistency

Internal consistency asks whether generated states remain mutually compatible across subjects, instances, views, frames, or story sequences.

#### Subject and identity consistency

| Paper / resource | Year / venue | Role | Links |
|---|---:|---|---|
| Textual Inversion: An Image is Worth One Word | ICLR 2023 | token-level personalization | [Code](https://github.com/rinongal/textual_inversion) |
| DreamBooth | CVPR 2023 | subject-specific finetuning | [Project](https://dreambooth.github.io/) |
| Custom Diffusion | CVPR 2023 | parameter-efficient multi-concept customization | [Code](https://github.com/adobe-research/custom-diffusion) |
| Perfusion | SIGGRAPH 2023 | lightweight personalization and concept locking | [Project](https://research.nvidia.com/labs/par/Perfusion/) |
| BLIP-Diffusion | NeurIPS 2023 | subject representation and reference-aware generation | [Code](https://github.com/salesforce/LAVIS/tree/main/projects/blip-diffusion) |
| ELITE: Encoding Visual Concepts into Textual Embeddings | ICCV 2023 | encoder-based concept personalization | [Code](https://github.com/csyxwei/ELITE) |
| FastComposer | NeurIPS 2023 | tuning-free multi-subject generation | [Code](https://github.com/mit-han-lab/fastcomposer) |
| Subject-Diffusion | ICCV 2023 | open-domain personalized subject generation | [Code](https://github.com/OPPO-Mente-Lab/Subject-Diffusion) |
| PhotoMaker | CVPR 2024 | ID-embedding-based human personalization | [Code](https://github.com/TencentARC/PhotoMaker) |
| InstantID | 2024 | instant identity-preserving generation | [Code](https://github.com/InstantID/InstantID) |
| IP-Adapter-FaceID | 2024 | face identity adapter for text-to-image diffusion | [Code](https://github.com/tencent-ailab/IP-Adapter) |
| ConsiStory | 2024 | training-free character/subject consistency | [Code](https://github.com/NVlabs/consistory) |
| StoryDiffusion | NeurIPS 2024 | long-range character and story consistency | [Code](https://github.com/HVision-NKU/StoryDiffusion) |
| StyleAligned | 2024 | shared-attention style and set-level consistency | [Project](https://style-aligned-gen.github.io/) |
| The Chosen One | SIGGRAPH 2024 | consistent characters in text-to-image diffusion | [Project](https://omriavrahami.com/the-chosen-one/) |
| ConsistentID | 2024 | identity-consistent portrait and character generation | [Paper](https://arxiv.org/abs/2404.16771) |
| Preserve and Personalize | ICLR 2026 | personalization without distributional drift | [Project](https://rlgnswk.github.io/PreserveAndPersonalize_ProjectPage/) |
| ConceptPrism | CVPR 2026 | concept disentanglement in personalized diffusion | Link to be added |

#### Multi-view and 3D consistency

| Paper / resource | Year / venue | Role | Links |
|---|---:|---|---|
| Zero-1-to-3 | ICCV 2023 | view-conditioned novel-view generation | [Code](https://github.com/cvlab-columbia/zero123) |
| One-2-3-45 | 2023/2024 | single-image to 3D generation via generated views | [Code](https://github.com/One-2-3-45/One-2-3-45) |
| Cascade-Zero123 | 2023/2024 | cascaded single-image-to-3D view synthesis | [Code](https://github.com/EnVision-Research/Cascade-Zero123) |
| Consistent123 | 2023/2024 | consistency-aware novel-view generation | [Paper](https://arxiv.org/abs/2309.17261) |
| SyncDreamer | ICLR 2024 | synchronized multi-view diffusion | [Code](https://github.com/liuyuan-pal/SyncDreamer) |
| MVDream | ICLR 2024 | text/image-conditioned multi-view diffusion | [Code](https://github.com/bytedance/MVDream) |
| Wonder3D | CVPR 2024 | cross-domain multi-view generation | [Code](https://github.com/xxlong0/Wonder3D) |
| ViewDiff | CVPR 2024 | 3D-consistent multi-view generation | [Project](https://lukashoel.github.io/ViewDiff/) |
| EscherNet | CVPR 2024 | scalable arbitrary-view synthesis | [Project](https://kxhit.github.io/EscherNet/) |
| DreamGaussian | ICLR 2024 | efficient 3D Gaussian generation from single image/text | [Code](https://github.com/dreamgaussian/dreamgaussian) |
| LGM: Large Multi-View Gaussian Model | ECCV 2024 | feed-forward multi-view Gaussian reconstruction/generation | [Code](https://github.com/3DTopia/LGM) |
| GRM: Large Gaussian Reconstruction Model | ECCV 2024 | large-scale Gaussian reconstruction from sparse views | [Project](https://justimyhxu.github.io/projects/grm/) |
| MVG-Bench | 2024 | multi-view generation benchmark | [Code](https://github.com/xiexh20/MVGBench) |
| MET3R | 2024 | multi-view consistency metric | [Code](https://github.com/mohammadasim98/met3r) |

#### Temporal, video, and narrative consistency

| Paper / resource | Year / venue | Role | Links |
|---|---:|---|---|
| VideoLDM: Align Your Latents | CVPR 2023 | latent video diffusion baseline | [Project](https://research.nvidia.com/labs/toronto-ai/VideoLDM/) |
| Text2Video-Zero | ICCV 2023 | zero-shot video generation from image diffusion | [Code](https://github.com/Picsart-AI-Research/Text2Video-Zero) |
| Tune-A-Video | ICCV 2023 | one-shot tuning for text-to-video generation | [Code](https://github.com/showlab/Tune-A-Video) |
| AnimateDiff | ICLR 2024 | motion module for personalized T2I backbones | [Code](https://github.com/guoyww/AnimateDiff) |
| FateZero | ICCV 2023 | attention-based video editing consistency | [Code](https://github.com/ChenyangQiQi/FateZero) |
| Video-P2P | 2023 | Prompt-to-Prompt-style video editing | [Code](https://github.com/ShaoTengLiu/Video-P2P) |
| TokenFlow | ICLR 2024 | diffusion-feature propagation for consistent video editing | [Project](https://diffusion-tokenflow.github.io/) |
| CoDeF | CVPR 2024 | content deformation fields for temporally consistent video processing | [Project](https://qiuyu96.github.io/CoDeF/) |
| Rerender A Video | SIGGRAPH Asia 2023 | zero-shot text-guided video-to-video translation | [Project](https://www.mmlab-ntu.com/project/rerender/) |
| COVE | 2024 | correspondence-guided video editing | [Code](https://github.com/wangjiangshan0725/COVE) |
| VideoCrafter2 | CVPR 2024 | high-quality video diffusion generation | [Code](https://github.com/AILab-CVC/VideoCrafter) |
| TaleCrafter | 2024 | interactive story visualization with multiple characters | Link to be added |
| One-Prompt-One-Story | 2024 | consistent text-to-image story generation | Link to be added |
| MovieDreamer | 2024/2025 | hierarchical long visual sequence generation | Link to be added |
| MotionStream | ICLR 2026 | real-time interactive video control | [OpenReview](https://openreview.net/forum?id=v1DKz5Vxr7) |
| VBench | CVPR 2024 | video generation benchmark with temporal diagnostics | [Code](https://github.com/Vchitect/VBench) |
| Video-Bench | CVPR 2025 | human-aligned video generation evaluation | [Code](https://github.com/Video-Bench/Video-Bench) |
| EvalCrafter | CVPR 2024 | video generation evaluation toolkit | [Code](https://github.com/evalcrafter/EvalCrafter) |
| FETV | NeurIPS 2023 Datasets and Benchmarks | fine-grained T2V benchmark | [Code](https://github.com/llyx97/FETV) |
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
| Pick-a-Pic | NeurIPS 2023 | pairwise preference dataset / PickScore | [Code](https://github.com/yuvalkirstain/PickScore) |
| ImageReward | NeurIPS 2023 | learned human preference reward | [Code](https://github.com/zai-org/ImageReward) |
| HPS: Human Preference Score | 2023 | human preference scoring | Link to be added |
| HPSv2 | 2024 | refined human-preference benchmark | [Code](https://github.com/tgxs002/HPSv2) |
| HPSv3 | 2025 | wide-spectrum human preference benchmark | [Code](https://github.com/MizzenAI/HPSv3) |
| MPS: Learning Multi-Dimensional Human Preference | CVPR 2024 | multi-dimensional preference modeling | [Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Learning_Multi-Dimensional_Human_Preference_for_Text-to-Image_Generation_CVPR_2024_paper.html) |
| VisionReward | AAAI 2026 | image/video preference evaluator | [Code](https://github.com/zai-org/VisionReward) |
| Diffusion-DPO | NeurIPS 2023/2024 | preference optimization for diffusion | [Code](https://github.com/SalesforceAIResearch/DiffusionDPO) |
| DDPO: Training Diffusion Models with Reinforcement Learning | 2023 | reward-driven diffusion finetuning | [Code](https://github.com/jannerm/ddpo) |
| AlignProp | 2023 | direct reward backpropagation through diffusion sampling | [Paper](https://arxiv.org/abs/2310.03739) |
| DPOK | 2023/2024 | diffusion policy optimization with KL regularization | [Paper](https://arxiv.org/abs/2305.16381) |
| D3PO | 2024 | direct preference optimization for diffusion policies | [Paper](https://arxiv.org/abs/2402.08385) |
| SPO | CVPR 2025 | aesthetic post-training | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Liang_Aesthetic_Post-Training_Diffusion_Models_from_Generic_Preferences_with_Step-by-step_Preference_CVPR_2025_paper.html) |
| DSPO | ICLR 2025 | score-level preference optimization | [OpenReview](https://openreview.net/forum?id=7f70331dbe58ad59d83941dfa7d975aa) |
| RankDPO | ICCV 2025 | ranked preference optimization | [Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Karthik_Scalable_Ranked_Preference_Optimization_for_Text-to-Image_Generation_ICCV_2025_paper.pdf) |
| CMPO / CaPO | CVPR 2025 | multi-preference calibration | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Lee_Calibrated_Multi-Preference_Optimization_for_Aligning_Diffusion_Models_CVPR_2025_paper.html) |

#### Safety, value alignment, and concept editing

| Paper / resource | Year / venue | Role | Links |
|---|---:|---|---|
| Safe Latent Diffusion | CVPR 2023 | inference-time safe guidance | [Code](https://github.com/ml-research/safe-latent-diffusion) |
| Erasing Concepts from Diffusion Models | ICCV 2023 | concept erasure | [Code](https://github.com/rohitgandikota/erasing) |
| Ablating Concepts in Text-to-Image Diffusion Models | ICCV 2023 | concept ablation | [Project](https://www.cs.cmu.edu/~concept-ablation/) |
| Unified Concept Editing | 2023/2024 | multi-concept editing / safety intervention | [Code](https://github.com/rohitgandikota/unified-concept-editing) |
| MACE: Mass Concept Erasure in Diffusion Models | CVPR 2024 | scalable concept erasure | [Paper](https://arxiv.org/abs/2403.06135) |
| Forget-Me-Not | 2023/2024 | attention-based concept forgetting | [Paper](https://arxiv.org/abs/2303.17591) |
| Ring-A-Bell | 2023/2024 | identifying and red-teaming concept removal failures | [Code](https://github.com/chiayi-hsu/Ring-A-Bell) |
| ACE: Anti-Editing Concept Erasure | 2024/2025 | robust concept erasure | Link to be added |
| Editing Massive Concepts in Text-to-Image Diffusion Models | 2024/2025 | large-scale concept editing | Link to be added |
| Six-CD | 2024/2025 | concept suppression and benign retention benchmark | [Code](https://github.com/Artanisax/Six-CD) |
| Responsible Text-to-Image Diffusion | ICML 2026 | interpretable and controllable safe/fair semantics | Link to be added |
| T2VSafetyBench | 2024/2025 | safety benchmark for text-to-video generation | [Paper](https://arxiv.org/abs/2409.08615) |

#### Physical, commonsense, and causal consistency

| Paper / resource | Year / venue | Role | Links |
|---|---:|---|---|
| PhyBench | 2024 | static physical commonsense evaluation | [Code](https://github.com/OpenGVLab/PhyBench) |
| VideoPhy | ICLR 2025 | physical commonsense evaluation for videos | [Code](https://github.com/Hritikbansal/videophy) |
| PhyCoBench | 2024/2025 | optical-flow-based physical coherence benchmark | [Code](https://github.com/Jeckinchen/PhyCoBench) |
| PhyGenBench | 2024/2025 | physical commonsense benchmark for video generation | [Code](https://github.com/OpenGVLab/PhyGenBench) |
| VideoPhy-2 | ICLR 2026 | action-centric physical commonsense benchmark | [Project](https://videophy2.github.io/) |
| T2VPhysBench | 2025 | first-principles physical consistency benchmark | Link to be added |
| T2VWorldBench | 2025 | world-knowledge, commonsense, and causal evaluation | Link to be added |
| Physics-IQ | WACV 2026 | physical-principle benchmark for video generation | [Code](https://github.com/google-deepmind/physics-IQ-benchmark) |
| PhyWorldBench | 2025 | physical realism benchmark for text-to-video | [Code](https://github.com/g-jing/phy-world-bench) |
| VideoVerse | 2025/2026 | world-model-oriented text-to-video evaluation | [Code](https://github.com/Zeqing-Wang/VideoVerse) |
| PhyEduVideo | WACV 2026 | physics-education-oriented video benchmark | [Code](https://github.com/meghamariamkm/PhyEduVideo) |
| PhyWorld | ICML 2025 | physical-law perspective on world models | [Paper](https://proceedings.mlr.press/v267/kang25g.html) |
| OSCBench | 2026 | object-state change and action consequence benchmark | Link to be added |
| UniSim: Learning Interactive Real-World Simulators | ICLR 2024 | action-conditioned real-world simulation | [OpenReview](https://openreview.net/forum?id=sFyTZEqmUY) |
| Genie: Generative Interactive Environments | ICML 2024 | generative interactive world environments | [Paper](https://proceedings.mlr.press/v235/bruce24a.html) |
| GAIA-1 | 2023/2024 | generative world model for autonomous driving | [Project](https://wayve.ai/thinking/gaia-1/) |
| WorldDreamer | 2024/2025 | video-based world generation for driving scenes | [Paper](https://arxiv.org/abs/2401.09985) |

## Resource maps

This repository currently tracks three resource maps.

1. [`resources/benchmark_coverage.csv`](resources/benchmark_coverage.csv): benchmark, dataset, evaluator, and diagnostic-resource coverage map.
2. [`resources/related_surveys.csv`](resources/related_surveys.csv): prior survey positioning.
3. [`resources/taxonomy_methods.csv`](resources/taxonomy_methods.csv): compact mapping from taxonomy nodes to representative methods and resources.

The benchmark table is not intended to rank resources by overall quality. It instead asks: **which consistency claim can this resource diagnose?**

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

Start with [`docs/taxonomy.md`](docs/taxonomy.md) for the conceptual structure. Use [`resources/benchmark_coverage.csv`](resources/benchmark_coverage.csv) if you need a benchmark, dataset, evaluator, or diagnostic protocol for a specific consistency claim.

Examples:

- Need prompt compositionality? Filter `P/C = H`.
- Need video temporal coherence? Filter `V/T = H` or `V/T = M`.
- Need safety or preference evaluation? Filter `N/S = H`.
- Need physical plausibility diagnostics? Filter `P/W = H`.

After editing `resources/benchmark_coverage.csv`, run:

```bash
python scripts/check_resource_table.py
```

The same check is also run automatically by GitHub Actions on every push and pull request.

## Contributing

Contributions are welcome. Please include the resource title, BibTeX key, venue/year, official paper URL, official project/code URL if available, resource type, modality, primary consistency relation, coverage values, and a short diagnostic-use/blind-spot description.

Use the issue template: [Add or correct a resource](.github/ISSUE_TEMPLATE/resource_addition.yml).

## Maintenance notes

Some 2025--2026 papers may initially appear as arXiv or project-page entries before official proceedings metadata is stable. When official BibTeX becomes available, please update [`resources/selected_bibtex.bib`](resources/selected_bibtex.bib) and any corresponding table entries.

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
