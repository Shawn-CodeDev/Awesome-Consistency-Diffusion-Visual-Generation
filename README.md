# Awesome Consistency in Diffusion-Based Visual Generation

<p align="center">
  <img src="docs/USTC.png" height="120" align="middle" alt="University of Science and Technology of China" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="docs/THU.png" height="120" align="middle" alt="Tsinghua University" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="docs/HUST.png" height="120" align="middle" alt="Huazhong University of Science and Technology" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="docs/logo.png" height="120" align="middle" alt="University of Cambridge" />
</p>

<p align="center">
  <img src="https://commons.wikimedia.org/wiki/Special:Redirect/file/Li%20Auto%20English%20logo.svg" height="50" align="middle" alt="Li Auto" />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://commons.wikimedia.org/wiki/Special:Redirect/file/ByteDance%20logo%20English.svg" height="40" align="middle" alt="ByteDance" />
</p>

[![Validate resource tables](https://github.com/Shawn-CodeDev/Awesome-Consistency-Diffusion-Visual-Generation/actions/workflows/validate-resources.yml/badge.svg)](https://github.com/Shawn-CodeDev/Awesome-Consistency-Diffusion-Visual-Generation/actions/workflows/validate-resources.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

This repository accompanies the survey:

> **Consistency in Diffusion-Based Visual Generation: A Survey**  
> Song Yan, Wei Zhai, Chenfeng Wang, Ruixuan Li, Zhangping Yang, Yancheng Cai, Tao Zhang, Ling Wang, Yunwei Lan, Yujie He, Yang Cao, Min Li, Zheng-Jun Zha.

This repository collects papers, methods, benchmarks, datasets, evaluators, and diagnostic resources for **consistency in diffusion-based visual generation**. The main organization follows the survey taxonomy: **External Consistency**, **Internal Consistency**, and **Normative Consistency**.

## DBLP-first policy

The main literature tables below are now **DBLP-first**. A paper is kept in the main README only when a DBLP record URL can be attached. Entries that are only broad topics, search starting points, project pages, or papers whose DBLP record still needs manual verification should be placed in a separate candidate file rather than mixed into the verified list.

Each verified entry follows this format:

> **Title** *(venue/source and year)* — short explanation. **DBLP:** link.

When DBLP contains only a CoRR/arXiv record, the source is marked as **CoRR/arXiv** instead of inventing a conference venue. When a stable conference DBLP record is known, the venue field uses that venue.

The helper script [`scripts/verify_dblp_links.py`](scripts/verify_dblp_links.py) can be used to re-check README entries through DBLP's publication search API and write `resources/dblp_verification.csv`.

## Table of contents

- [Taxonomy](#taxonomy)
- [External consistency](#external-consistency)
- [Internal consistency](#internal-consistency)
- [Normative consistency](#normative-consistency)
- [Candidate and maintenance policy](#candidate-and-maintenance-policy)
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

### Methods and systems

| Paper | Venue/source | Why it matters for consistency | DBLP |
|---|---|---|---|
| GLIDE: Towards Photorealistic Image Generation and Editing with Text-Guided Diffusion Models | CoRR/arXiv 2021 | Early text-guided diffusion generation and editing baseline. | [DBLP](https://dblp.org/rec/journals/corr/abs-2112-10741.html) |
| High-Resolution Image Synthesis with Latent Diffusion Models | CVPR 2022 | Latent-space diffusion backbone for prompt-, layout-, mask-, and image-conditioned generation. | [DBLP](https://dblp.org/rec/conf/cvpr/RombachBLEO22.html) |
| Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding | CoRR/arXiv 2022 | Strong text-to-image baseline emphasizing prompt semantics. | [DBLP](https://dblp.org/rec/journals/corr/abs-2205-11487.html) |
| Composable Diffusion Models | CoRR/arXiv 2022 | Combines multiple diffusion conditions, useful for compositional constraints. | [DBLP](https://dblp.org/rec/journals/corr/abs-2206-01714.html) |
| StructureDiffusion: Language-Guided Creation of Physically-Valid Structures using Unseen Objects | CoRR/arXiv 2022 | Uses structured prompt representations to improve compositional generation. | [DBLP](https://dblp.org/rec/journals/corr/abs-2212-05032.html) |
| Attend-and-Excite: Attention-Based Semantic Guidance for Text-to-Image Diffusion Models | CoRR/arXiv 2023 | Manipulates cross-attention to reduce missing objects and improve prompt coverage. | [DBLP](https://dblp.org/rec/journals/corr/abs-2301-13826.html) |
| Adding Conditional Control to Text-to-Image Diffusion Models | ICCV 2023 | ControlNet introduces trainable side branches for spatial and structural control. | [DBLP](https://dblp.org/rec/conf/iccv/ZhangRA23.html) |
| T2I-Adapter: Learning Adapters to Dig out More Controllable Ability for Text-to-Image Diffusion Models | CoRR/arXiv 2023 | Lightweight adapters for sketch, depth, pose, and other control signals. | [DBLP](https://dblp.org/rec/journals/corr/abs-2302-08453.html) |
| IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models | CoRR/arXiv 2023 | Adds reference-image conditioning while keeping text compatibility. | [DBLP](https://dblp.org/rec/journals/corr/abs-2308-06721.html) |
| FreeDoM: Training-Free Energy-Guided Conditional Diffusion Model | CoRR/arXiv 2023 | Uses external energy functions for training-free conditional guidance. | [DBLP](https://dblp.org/rec/journals/corr/abs-2303-09833.html) |
| UniControl: A Unified Diffusion Model for Controllable Visual Generation in the Wild | CoRR/arXiv 2023 | Unifies multiple visual control types in one diffusion framework. | [DBLP](https://dblp.org/rec/journals/corr/abs-2305-11147.html) |
| Uni-ControlNet: All-in-One Control to Text-to-Image Diffusion Models | CoRR/arXiv 2023 | Consolidates multiple ControlNet-style conditions. | [DBLP](https://dblp.org/rec/journals/corr/abs-2305-16322.html) |
| Prompt-to-Prompt Image Editing with Cross-Attention Control | CoRR/arXiv 2022 | Edits prompts while preserving non-edited content through attention control. | [DBLP](https://dblp.org/rec/journals/corr/abs-2208-01626.html) |
| Null-Text Inversion for Editing Real Images using Guided Diffusion Models | CoRR/arXiv 2022 | Inverts real images to enable more faithful edit preservation. | [DBLP](https://dblp.org/rec/journals/corr/abs-2211-09794.html) |
| DiffEdit: Diffusion-Based Semantic Image Editing with Mask Guidance | CoRR/arXiv 2022 | Derives semantic masks from prompt differences for localized editing. | [DBLP](https://dblp.org/rec/journals/corr/abs-2210-11427.html) |
| InstructPix2Pix: Learning to Follow Image Editing Instructions | CoRR/arXiv 2022 | Trains instruction-following image editing from synthetic edit pairs. | [DBLP](https://dblp.org/rec/journals/corr/abs-2211-09800.html) |
| Imagic: Text-Based Real Image Editing with Diffusion Models | CoRR/arXiv 2022 | Optimizes embeddings/model weights for real-image editing. | [DBLP](https://dblp.org/rec/journals/corr/abs-2210-09276.html) |
| Paint by Example: Exemplar-Based Image Editing with Diffusion Models | CoRR/arXiv 2022 | Uses exemplar images as external edit references. | [DBLP](https://dblp.org/rec/journals/corr/abs-2211-13227.html) |
| Pix2Pix-Zero: Zero-shot Image-to-Image Translation | CoRR/arXiv 2023 | Performs zero-shot translation while preserving source-image structure. | [DBLP](https://dblp.org/rec/journals/corr/abs-2302-03027.html) |
| DragonDiffusion: Enabling Drag-style Manipulation on Diffusion Models | CoRR/arXiv 2023 | Supports interactive object moving and resizing under preservation constraints. | [DBLP](https://dblp.org/rec/journals/corr/abs-2307-02421.html) |
| DragDiffusion: Harnessing Diffusion Models for Interactive Point-based Image Editing | CoRR/arXiv 2023 | Point-based image editing with diffusion priors. | [DBLP](https://dblp.org/rec/journals/corr/abs-2306-14435.html) |
| TextDiffuser: Diffusion Models as Text Painters | CoRR/arXiv 2023 | Improves rendered text consistency in generated images. | [DBLP](https://dblp.org/rec/journals/corr/abs-2305-10855.html) |

### Benchmarks and evaluators

| Resource | Venue/source | Diagnostic role | DBLP |
|---|---|---|---|
| TIFA: Accurate and Interpretable Text-to-Image Faithfulness Evaluation with Question Answering | CoRR/arXiv 2023 | QA-based prompt-faithfulness evaluation. | [DBLP](https://dblp.org/rec/journals/corr/abs-2303-11897.html) |
| T2I-CompBench: A Comprehensive Benchmark for Open-world Compositional Text-to-image Generation | CoRR/arXiv 2023 | Measures compositional relations, attributes, and complex prompt following. | [DBLP](https://dblp.org/rec/journals/corr/abs-2307-06350.html) |
| GenEval: An Object-Focused Framework for Evaluating Text-to-Image Alignment | CoRR/arXiv 2023 | Object-centric evaluation for counting, attributes, colors, and positions. | [DBLP](https://dblp.org/rec/journals/corr/abs-2310-11513.html) |
| HRS-Bench: Holistic, Reliable and Scalable Benchmark for Text-to-Image Models | CoRR/arXiv 2023 | Broad T2I evaluation with robustness and bias dimensions. | [DBLP](https://dblp.org/rec/journals/corr/abs-2304-05390.html) |
| MagicBrush: A Manually Annotated Dataset for Instruction-Guided Image Editing | CoRR/arXiv 2023 | Multi-turn instruction editing data and evaluation. | [DBLP](https://dblp.org/rec/journals/corr/abs-2306-10012.html) |

---

## Internal consistency

Internal consistency asks whether generated states remain mutually compatible across identities, subjects, views, frames, videos, or story sequences.

### Personalization, identity, and subject consistency

| Paper | Venue/source | Why it matters for consistency | DBLP |
|---|---|---|---|
| An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion | CoRR/arXiv 2022 | Learns new token embeddings for reusable personalized concepts. | [DBLP](https://dblp.org/rec/journals/corr/abs-2208-01618.html) |
| DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation | CoRR/arXiv 2022 | Finetunes diffusion models for subject identity persistence. | [DBLP](https://dblp.org/rec/journals/corr/abs-2208-12242.html) |
| Custom Diffusion: Multi-Concept Customization of Text-to-Image Diffusion | CoRR/arXiv 2022 | Parameter-efficient multi-concept personalization. | [DBLP](https://dblp.org/rec/journals/corr/abs-2212-04488.html) |
| Perfusion: Personalizing Text-to-Image Diffusion with Key-Locking | CoRR/arXiv 2023 | Lightweight personalization while controlling concept overfitting. | [DBLP](https://dblp.org/rec/journals/corr/abs-2305-01644.html) |
| BLIP-Diffusion: Pre-trained Subject Representation for Controllable Text-to-Image Generation and Editing | CoRR/arXiv 2023 | Uses pretrained subject representations for identity-conditioned generation. | [DBLP](https://dblp.org/rec/journals/corr/abs-2305-14720.html) |
| FastComposer: Tuning-Free Multi-Subject Image Generation with Localized Attention | CoRR/arXiv 2023 | Multi-subject identity preservation without per-subject finetuning. | [DBLP](https://dblp.org/rec/journals/corr/abs-2305-10431.html) |
| PhotoMaker: Customizing Realistic Human Photos via Stacked ID Embedding | CoRR/arXiv 2023 | Zero-shot human identity customization. | [DBLP](https://dblp.org/rec/journals/corr/abs-2312-04461.html) |
| InstantID: Zero-shot Identity-Preserving Generation in Seconds | CoRR/arXiv 2024 | Fast identity-preserving generation using ID conditioning. | [DBLP](https://dblp.org/rec/journals/corr/abs-2401-07519.html) |
| StoryDiffusion: Consistent Self-Attention for Long-Range Image and Video Generation | CoRR/arXiv 2024 | Long-range character consistency for stories and videos. | [DBLP](https://dblp.org/rec/journals/corr/abs-2405-01434.html) |

### Multi-view, 3D, and video consistency

| Paper | Venue/source | Why it matters for consistency | DBLP |
|---|---|---|---|
| Zero-1-to-3: Zero-shot One Image to 3D Object | CoRR/arXiv 2023 | Novel-view generation from one image. | [DBLP](https://dblp.org/rec/journals/corr/abs-2303-11328.html) |
| Consistent123: Improve Consistency for One Image to 3D Object Synthesis | CoRR/arXiv 2023 | Improves cross-view consistency for image-to-3D generation. | [DBLP](https://dblp.org/rec/journals/corr/abs-2309-17261.html) |
| SyncDreamer: Generating Multiview-consistent Images from a Single-view Image | CoRR/arXiv 2023 | Synchronizes multi-view diffusion predictions. | [DBLP](https://dblp.org/rec/journals/corr/abs-2309-03453.html) |
| MVDream: Multi-view Diffusion for 3D Generation | CoRR/arXiv 2023 | Text/image-conditioned multi-view diffusion for 3D generation. | [DBLP](https://dblp.org/rec/journals/corr/abs-2308-16512.html) |
| Wonder3D: Single Image to 3D using Cross-Domain Diffusion | CoRR/arXiv 2023 | Generates normal/color multi-views for 3D reconstruction. | [DBLP](https://dblp.org/rec/journals/corr/abs-2310-15008.html) |
| DreamGaussian: Generative Gaussian Splatting for Efficient 3D Content Creation | CoRR/arXiv 2023 | Fast text/image-to-3D using Gaussian splatting. | [DBLP](https://dblp.org/rec/journals/corr/abs-2309-16653.html) |
| Align your Latents: High-Resolution Video Synthesis with Latent Diffusion Models | CoRR/arXiv 2023 | Video latent diffusion baseline for temporal consistency studies. | [DBLP](https://dblp.org/rec/journals/corr/abs-2304-08818.html) |
| Text2Video-Zero: Text-to-Image Diffusion Models are Zero-Shot Video Generators | CoRR/arXiv 2023 | Adapts image diffusion to videos with temporal constraints. | [DBLP](https://dblp.org/rec/journals/corr/abs-2303-13439.html) |
| Tune-A-Video: One-Shot Tuning of Image Diffusion Models for Text-to-Video Generation | CoRR/arXiv 2022 | One-shot video tuning and temporal preservation. | [DBLP](https://dblp.org/rec/journals/corr/abs-2212-11565.html) |
| FateZero: Fusing Attentions for Zero-shot Text-based Video Editing | CoRR/arXiv 2023 | Attention fusion for temporally consistent video editing. | [DBLP](https://dblp.org/rec/journals/corr/abs-2303-09535.html) |
| TokenFlow: Consistent Diffusion Features for Consistent Video Editing | CoRR/arXiv 2023 | Feature propagation for cross-frame consistency. | [DBLP](https://dblp.org/rec/journals/corr/abs-2307-10373.html) |
| CoDeF: Content Deformation Fields for Temporally Consistent Video Processing | CoRR/arXiv 2023 | Uses deformation fields to preserve video content across time. | [DBLP](https://dblp.org/rec/journals/corr/abs-2308-07926.html) |
| AnimateDiff: Animate Your Personalized Text-to-Image Diffusion Models without Specific Tuning | CoRR/arXiv 2023 | Adds motion modules to personalized T2I backbones. | [DBLP](https://dblp.org/rec/journals/corr/abs-2307-04725.html) |

### Benchmarks and datasets

| Resource | Venue/source | Diagnostic role | DBLP |
|---|---|---|---|
| VBench: Comprehensive Benchmark Suite for Video Generative Models | CoRR/arXiv 2023 | Multi-dimensional video generation evaluation, including temporal and subject consistency. | [DBLP](https://dblp.org/rec/journals/corr/abs-2311-17982.html) |
| FETV: A Benchmark for Fine-Grained Evaluation of Open-Domain Text-to-Video Generation | CoRR/arXiv 2023 | Fine-grained T2V prompt and temporal evaluation. | [DBLP](https://dblp.org/rec/journals/corr/abs-2311-01813.html) |
| MeViS: A Large-scale Benchmark for Video Segmentation with Motion Expressions | ICCV 2023 | Motion-expression video segmentation for temporal grounding diagnostics. | [DBLP](https://dblp.org/rec/conf/iccv/DingLWWL23.html) |
| MOSE: A New Dataset for Video Object Segmentation in Complex Scenes | ICCV 2023 | Video object segmentation under occlusion and complex motion. | [DBLP](https://dblp.org/rec/conf/iccv/DingLWX23.html) |
| Tracking Any Object Amodally | ECCV 2020 | Long-tail object tracking dataset for persistence diagnostics. | [DBLP](https://dblp.org/rec/conf/eccv/DaveRKOP20.html) |
| Video Scene Parsing in the Wild | CVPR 2021 | Video scene parsing for scene-state continuity checks. | [DBLP](https://dblp.org/rec/conf/cvpr/MiaoW0XY21.html) |
| nuScenes: A Multimodal Dataset for Autonomous Driving | CVPR 2020 | Driving scene data for geometry and dynamic-state consistency. | [DBLP](https://dblp.org/rec/conf/cvpr/CaesarBVPDRF20.html) |

---

## Normative consistency

Normative consistency asks whether generated content satisfies evaluative principles such as preference, aesthetics, safety, fairness, concept restrictions, physical plausibility, commonsense, action consequence, and world-state validity.

### Preference and aesthetics

| Paper/resource | Venue/source | Why it matters for consistency | DBLP |
|---|---|---|---|
| Pick-a-Pic: An Open Dataset of User Preferences for Text-to-Image Generation | CoRR/arXiv 2023 | Pairwise preference data and PickScore-style evaluation. | [DBLP](https://dblp.org/rec/journals/corr/abs-2305-01569.html) |
| ImageReward: Learning and Evaluating Human Preferences for Text-to-Image Generation | CoRR/arXiv 2023 | Learned preference reward for ranking and optimization. | [DBLP](https://dblp.org/rec/journals/corr/abs-2304-05977.html) |
| HPSv2: Human Preference Score v2 | CoRR/arXiv 2023 | Human-preference benchmark and scoring for T2I outputs. | [DBLP](https://dblp.org/rec/journals/corr/abs-2306-09341.html) |
| Diffusion Model Alignment Using Direct Preference Optimization | CoRR/arXiv 2023 | Direct preference optimization for diffusion models. | [DBLP](https://dblp.org/rec/journals/corr/abs-2311-12908.html) |
| Training Diffusion Models with Reinforcement Learning | CoRR/arXiv 2023 | Reward-driven diffusion policy optimization. | [DBLP](https://dblp.org/rec/journals/corr/abs-2305-13301.html) |
| AlignProp: Aligning Diffusion Models with Human Feedback | CoRR/arXiv 2023 | Backpropagates reward signals through diffusion sampling. | [DBLP](https://dblp.org/rec/journals/corr/abs-2310-03739.html) |
| Diffusion Model Alignment Using Direct Preference Optimization with KL Regularization | CoRR/arXiv 2023 | KL-regularized preference optimization for diffusion generation. | [DBLP](https://dblp.org/rec/journals/corr/abs-2305-16381.html) |

### Safety, concept editing, and erasure

| Paper/resource | Venue/source | Why it matters for consistency | DBLP |
|---|---|---|---|
| Safe Latent Diffusion: Mitigating Inappropriate Degeneration in Diffusion Models | CoRR/arXiv 2022 | Inference-time safety guidance for latent diffusion. | [DBLP](https://dblp.org/rec/journals/corr/abs-2211-05105.html) |
| Erasing Concepts from Diffusion Models | CoRR/arXiv 2023 | Removes undesirable concepts from diffusion models. | [DBLP](https://dblp.org/rec/journals/corr/abs-2303-07345.html) |
| Ablating Concepts in Text-to-Image Diffusion Models | CoRR/arXiv 2023 | Edits or ablates concepts while preserving general generation. | [DBLP](https://dblp.org/rec/journals/corr/abs-2303-13516.html) |
| Unified Concept Editing in Diffusion Models | CoRR/arXiv 2023 | Multi-concept editing and safety intervention. | [DBLP](https://dblp.org/rec/journals/corr/abs-2308-14761.html) |
| MACE: Mass Concept Erasure in Diffusion Models | CoRR/arXiv 2024 | Scalable concept erasure for many target concepts. | [DBLP](https://dblp.org/rec/journals/corr/abs-2403-06135.html) |
| Forget-Me-Not: Learning to Forget in Text-to-Image Diffusion Models | CoRR/arXiv 2023 | Attention-based concept forgetting. | [DBLP](https://dblp.org/rec/journals/corr/abs-2303-17591.html) |
| T2VSafetyBench: Evaluating the Safety of Text-to-Video Generative Models | CoRR/arXiv 2024 | Safety benchmark for text-to-video generation. | [DBLP](https://dblp.org/rec/journals/corr/abs-2409-08615.html) |

### Physical, causal, and world consistency

| Paper/resource | Venue/source | Why it matters for consistency | DBLP |
|---|---|---|---|
| WorldDreamer: Towards General World Models for Video Generation via Predicting Masked Tokens | CoRR/arXiv 2024 | Driving/world video generation with structured world priors. | [DBLP](https://dblp.org/rec/journals/corr/abs-2401-09985.html) |
| Genie: Generative Interactive Environments | ICML 2024 | Interactive generative environments from video data. | [DBLP](https://dblp.org/rec/conf/icml/BruceDDLBGDE24.html) |
| Learning Interactive Real-World Simulators | ICLR 2024 | Action-conditioned real-world simulation for interactive world modeling. | [DBLP](https://dblp.org/rec/conf/iclr/YangYCW0L0RD24.html) |
| VideoPhy: Evaluating Physical Commonsense for Video Generation | CoRR/arXiv 2024 | Physical commonsense diagnostics for generated videos. | [DBLP](https://dblp.org/rec/journals/corr/abs-2406-03520.html) |
| PhyGenBench: Towards World Simulator | CoRR/arXiv 2024 | Benchmarking physical-law consistency in generated videos. | [DBLP](https://dblp.org/rec/journals/corr/abs-2407-08024.html) |

---

## Candidate and maintenance policy

The previous README contained many useful but unverified or non-bibliographic entries, including broad topics such as prompt expansion, verifier-guided generation, world-consistent video diffusion, and metric families. These are intentionally not mixed into the verified main tables.

To add a new item to the main README:

1. Find the paper on DBLP.
2. Add the exact DBLP record URL.
3. Use the venue/source shown by DBLP. If DBLP only has a CoRR record, write `CoRR/arXiv YEAR`.
4. Add a one-sentence explanation of the consistency issue it addresses.
5. Run:

```bash
python scripts/verify_dblp_links.py --readme README.md --out resources/dblp_verification.csv
```

If a paper is important but has no DBLP record yet, keep it in a separate candidate file until it can be verified.

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
