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

## Multi-source verification policy

The main README now uses a **multi-source verification rule** rather than DBLP-only metadata. For each formal paper or benchmark, the table should include:

1. **Paper page**: arXiv, CVF OpenAccess, OpenReview, ACM, PMLR, or another stable official paper page.
2. **Code / Project**: official GitHub repository or official project page, when one can be verified. If no official source is confirmed, the field is `--`.
3. **DBLP**: DBLP record URL when available. If DBLP only has a CoRR/arXiv record, the venue/source field should say `CoRR/arXiv`, not an invented conference venue.

Broad topics, metric families, and search starting points are not mixed into the verified paper tables. They should be placed in a separate candidate file until they can be associated with a specific paper and stable sources.

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

| Paper | Venue/source | Paper page | Code / Project | DBLP | Why it matters |
|---|---|---|---|---|---|
| GLIDE: Towards Photorealistic Image Generation and Editing with Text-Guided Diffusion Models | CoRR/arXiv 2021 | [arXiv](https://arxiv.org/abs/2112.10741) | [GitHub](https://github.com/openai/glide-text2im) | [DBLP](https://dblp.org/rec/journals/corr/abs-2112-10741.html) | Early text-guided diffusion generation and editing baseline. |
| High-Resolution Image Synthesis with Latent Diffusion Models | CVPR 2022 | [CVF](https://openaccess.thecvf.com/content/CVPR2022/html/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.html) / [arXiv](https://arxiv.org/abs/2112.10752) | [GitHub](https://github.com/CompVis/latent-diffusion) | [DBLP](https://dblp.org/rec/conf/cvpr/RombachBLEO22.html) | Latent-space diffusion backbone for prompt-, layout-, mask-, and image-conditioned generation. |
| Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding | CoRR/arXiv 2022 | [arXiv](https://arxiv.org/abs/2205.11487) | -- | [DBLP](https://dblp.org/rec/journals/corr/abs-2205-11487.html) | Strong text-to-image baseline emphasizing prompt semantics. |
| Composable Diffusion Models | CoRR/arXiv 2022 | [arXiv](https://arxiv.org/abs/2206.01714) | [Project](https://energy-based-model.github.io/Compositional-Visual-Generation-with-Composable-Diffusion-Models/) | [DBLP](https://dblp.org/rec/journals/corr/abs-2206-01714.html) | Combines multiple diffusion conditions, useful for compositional constraints. |
| StructureDiffusion: Language-Guided Creation of Physically-Valid Structures using Unseen Objects | CoRR/arXiv 2022 | [arXiv](https://arxiv.org/abs/2212.05032) | -- | [DBLP](https://dblp.org/rec/journals/corr/abs-2212-05032.html) | Uses structured prompt representations to improve compositional generation. |
| Attend-and-Excite: Attention-Based Semantic Guidance for Text-to-Image Diffusion Models | SIGGRAPH 2023 / CoRR | [arXiv](https://arxiv.org/abs/2301.13826) | [GitHub](https://github.com/yuval-alaluf/Attend-and-Excite) | [DBLP](https://dblp.org/rec/journals/corr/abs-2301-13826.html) | Manipulates cross-attention maps to reduce missing objects and improve prompt coverage. |
| GLIGEN: Open-Set Grounded Text-to-Image Generation | CVPR 2023 | [CVF](https://openaccess.thecvf.com/content/CVPR2023/html/Li_GLIGEN_Open-Set_Grounded_Text-to-Image_Generation_CVPR_2023_paper.html) / [arXiv](https://arxiv.org/abs/2301.07093) | [GitHub](https://github.com/gligen/GLIGEN) | [DBLP](https://dblp.org/rec/conf/cvpr/Li0CLS0V23.html) | Grounds generated objects using boxes and phrase-level conditions. |
| Adding Conditional Control to Text-to-Image Diffusion Models | ICCV 2023 | [CVF](https://openaccess.thecvf.com/content/ICCV2023/html/Zhang_Adding_Conditional_Control_to_Text-to-Image_Diffusion_Models_ICCV_2023_paper.html) / [arXiv](https://arxiv.org/abs/2302.05543) | [GitHub](https://github.com/lllyasviel/ControlNet) | [DBLP](https://dblp.org/rec/conf/iccv/ZhangRA23.html) | ControlNet introduces trainable side branches for spatial and structural control. |
| T2I-Adapter: Learning Adapters to Dig out More Controllable Ability for Text-to-Image Diffusion Models | CoRR/arXiv 2023 | [arXiv](https://arxiv.org/abs/2302.08453) | [GitHub](https://github.com/TencentARC/T2I-Adapter) | [DBLP](https://dblp.org/rec/journals/corr/abs-2302-08453.html) | Lightweight adapters for sketch, depth, pose, and other control signals. |
| IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models | CoRR/arXiv 2023 | [arXiv](https://arxiv.org/abs/2308.06721) | [GitHub](https://github.com/tencent-ailab/IP-Adapter) | [DBLP](https://dblp.org/rec/journals/corr/abs-2308-06721.html) | Adds reference-image conditioning while keeping text compatibility. |
| FreeDoM: Training-Free Energy-Guided Conditional Diffusion Model | ICCV 2023 / CoRR | [arXiv](https://arxiv.org/abs/2303.09833) | [GitHub](https://github.com/vvictoryuki/FreeDoM) | [DBLP](https://dblp.org/rec/journals/corr/abs-2303-09833.html) | Uses external energy functions for training-free conditional guidance. |
| UniControl: A Unified Diffusion Model for Controllable Visual Generation in the Wild | NeurIPS 2023 / CoRR | [arXiv](https://arxiv.org/abs/2305.11147) | [GitHub](https://github.com/ShihaoZhaoZSH/Uni-ControlNet) | [DBLP](https://dblp.org/rec/journals/corr/abs-2305-11147.html) | Unifies multiple visual control types in one diffusion framework. |
| Uni-ControlNet: All-in-One Control to Text-to-Image Diffusion Models | CoRR/arXiv 2023 | [arXiv](https://arxiv.org/abs/2305.16322) | -- | [DBLP](https://dblp.org/rec/journals/corr/abs-2305-16322.html) | Consolidates multiple ControlNet-style conditions. |
| Prompt-to-Prompt Image Editing with Cross-Attention Control | ICLR 2023 / CoRR | [OpenReview](https://openreview.net/forum?id=_CDixzkzeyb) / [arXiv](https://arxiv.org/abs/2208.01626) | [GitHub](https://github.com/google/prompt-to-prompt) | [DBLP](https://dblp.org/rec/journals/corr/abs-2208-01626.html) | Edits prompts while preserving non-edited content through attention control. |
| Null-Text Inversion for Editing Real Images using Guided Diffusion Models | CVPR 2023 | [CVF](https://openaccess.thecvf.com/content/CVPR2023/html/Mokady_NULL-Text_Inversion_for_Editing_Real_Images_Using_Guided_Diffusion_Models_CVPR_2023_paper.html) / [arXiv](https://arxiv.org/abs/2211.09794) | [Project](https://null-text-inversion.github.io/) | [DBLP](https://dblp.org/rec/journals/corr/abs-2211-09794.html) | Inverts real images to enable more faithful prompt-based editing. |
| DiffEdit: Diffusion-Based Semantic Image Editing with Mask Guidance | ICLR 2023 / CoRR | [OpenReview](https://openreview.net/forum?id=3lge0p5o-M-) / [arXiv](https://arxiv.org/abs/2210.11427) | -- | [DBLP](https://dblp.org/rec/journals/corr/abs-2210-11427.html) | Derives semantic masks from prompt differences for localized editing. |
| InstructPix2Pix: Learning to Follow Image Editing Instructions | CVPR 2023 | [CVF](https://openaccess.thecvf.com/content/CVPR2023/html/Brooks_InstructPix2Pix_Learning_To_Follow_Image_Editing_Instructions_CVPR_2023_paper.html) / [arXiv](https://arxiv.org/abs/2211.09800) | [GitHub](https://github.com/timothybrooks/instruct-pix2pix) | [DBLP](https://dblp.org/rec/journals/corr/abs-2211-09800.html) | Trains instruction-following image editing from synthetic edit pairs. |
| Imagic: Text-Based Real Image Editing with Diffusion Models | CVPR 2023 | [CVF](https://openaccess.thecvf.com/content/CVPR2023/html/Kawar_Imagic_Text-Based_Real_Image_Editing_With_Diffusion_Models_CVPR_2023_paper.html) / [arXiv](https://arxiv.org/abs/2210.09276) | [Project](https://imagic-editing.github.io/) | [DBLP](https://dblp.org/rec/journals/corr/abs-2210-09276.html) | Optimizes embeddings/model weights for real-image editing. |
| Paint by Example: Exemplar-Based Image Editing with Diffusion Models | CVPR 2023 | [CVF](https://openaccess.thecvf.com/content/CVPR2023/html/Yang_Paint_by_Example_Exemplar-Based_Image_Editing_With_Diffusion_Models_CVPR_2023_paper.html) / [arXiv](https://arxiv.org/abs/2211.13227) | [GitHub](https://github.com/Fantasy-Studio/Paint-by-Example) | [DBLP](https://dblp.org/rec/journals/corr/abs-2211-13227.html) | Uses exemplar images as external edit references. |
| Pix2Pix-Zero: Zero-shot Image-to-Image Translation | ICCV 2023 / CoRR | [arXiv](https://arxiv.org/abs/2302.03027) | [Project](https://pix2pixzero.github.io/) | [DBLP](https://dblp.org/rec/journals/corr/abs-2302-03027.html) | Performs zero-shot translation while preserving source-image structure. |
| DragonDiffusion: Enabling Drag-style Manipulation on Diffusion Models | ICLR 2024 / CoRR | [arXiv](https://arxiv.org/abs/2307.02421) | [GitHub](https://github.com/MC-E/DragonDiffusion) | [DBLP](https://dblp.org/rec/journals/corr/abs-2307-02421.html) | Supports interactive object moving and resizing under preservation constraints. |
| DragDiffusion: Harnessing Diffusion Models for Interactive Point-based Image Editing | CVPR 2024 / CoRR | [arXiv](https://arxiv.org/abs/2306.14435) | [GitHub](https://github.com/Yujun-Shi/DragDiffusion) | [DBLP](https://dblp.org/rec/journals/corr/abs-2306-14435.html) | Point-based image editing with diffusion priors. |
| TextDiffuser: Diffusion Models as Text Painters | NeurIPS 2023 / CoRR | [arXiv](https://arxiv.org/abs/2305.10855) | [GitHub](https://github.com/microsoft/unilm/tree/master/textdiffuser) | [DBLP](https://dblp.org/rec/journals/corr/abs-2305-10855.html) | Improves rendered text consistency in generated images. |

### Benchmarks and evaluators

| Resource | Venue/source | Paper page | Code / Project | DBLP | Diagnostic role |
|---|---|---|---|---|---|
| TIFA: Accurate and Interpretable Text-to-Image Faithfulness Evaluation with Question Answering | ICCV 2023 / CoRR | [arXiv](https://arxiv.org/abs/2303.11897) | [GitHub](https://github.com/Yushi-Hu/tifa) | [DBLP](https://dblp.org/rec/journals/corr/abs-2303-11897.html) | QA-based prompt-faithfulness evaluation. |
| T2I-CompBench: A Comprehensive Benchmark for Open-world Compositional Text-to-image Generation | NeurIPS 2023 / CoRR | [arXiv](https://arxiv.org/abs/2307.06350) | [GitHub](https://github.com/Karine-Huang/T2I-CompBench) | [DBLP](https://dblp.org/rec/journals/corr/abs-2307-06350.html) | Measures compositional relations, attributes, and complex prompt following. |
| GenEval: An Object-Focused Framework for Evaluating Text-to-Image Alignment | CoRR/arXiv 2023 | [arXiv](https://arxiv.org/abs/2310.11513) | [GitHub](https://github.com/djghosh13/geneval) | [DBLP](https://dblp.org/rec/journals/corr/abs-2310-11513.html) | Object-centric evaluation for counting, attributes, colors, and positions. |
| HRS-Bench: Holistic, Reliable and Scalable Benchmark for Text-to-Image Models | ICCV 2023 / CoRR | [arXiv](https://arxiv.org/abs/2304.05390) | [GitHub](https://github.com/eslambakr/HRS_benchmark) | [DBLP](https://dblp.org/rec/journals/corr/abs-2304-05390.html) | Broad T2I evaluation with robustness and bias dimensions. |
| MagicBrush: A Manually Annotated Dataset for Instruction-Guided Image Editing | NeurIPS Datasets and Benchmarks 2023 / CoRR | [arXiv](https://arxiv.org/abs/2306.10012) | [GitHub](https://github.com/OSU-NLP-Group/MagicBrush) | [DBLP](https://dblp.org/rec/journals/corr/abs-2306-10012.html) | Multi-turn instruction editing data and evaluation. |

---

## Internal consistency

Internal consistency asks whether generated states remain mutually compatible across identities, subjects, views, frames, videos, or story sequences.

### Personalization, identity, and subject consistency

| Paper | Venue/source | Paper page | Code / Project | DBLP | Why it matters |
|---|---|---|---|---|---|
| An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion | ICLR 2023 / CoRR | [OpenReview](https://openreview.net/forum?id=NAQvF08TcyG) / [arXiv](https://arxiv.org/abs/2208.01618) | [GitHub](https://github.com/rinongal/textual_inversion) | [DBLP](https://dblp.org/rec/journals/corr/abs-2208-01618.html) | Learns new token embeddings for reusable personalized concepts. |
| DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation | CVPR 2023 / CoRR | [CVF](https://openaccess.thecvf.com/content/CVPR2023/html/Ruiz_DreamBooth_Fine_Tuning_Text-to-Image_Diffusion_Models_for_Subject-Driven_Generation_CVPR_2023_paper.html) / [arXiv](https://arxiv.org/abs/2208.12242) | [Project](https://dreambooth.github.io/) | [DBLP](https://dblp.org/rec/journals/corr/abs-2208-12242.html) | Finetunes diffusion models for subject identity persistence. |
| Custom Diffusion: Multi-Concept Customization of Text-to-Image Diffusion | CVPR 2023 / CoRR | [CVF](https://openaccess.thecvf.com/content/CVPR2023/html/Kumari_Multi-Concept_Customization_of_Text-to-Image_Diffusion_CVPR_2023_paper.html) / [arXiv](https://arxiv.org/abs/2212.04488) | [GitHub](https://github.com/adobe-research/custom-diffusion) | [DBLP](https://dblp.org/rec/journals/corr/abs-2212-04488.html) | Parameter-efficient multi-concept personalization. |
| Perfusion: Personalizing Text-to-Image Diffusion with Key-Locking | SIGGRAPH 2023 / CoRR | [arXiv](https://arxiv.org/abs/2305.01644) | [Project](https://research.nvidia.com/labs/par/Perfusion/) | [DBLP](https://dblp.org/rec/journals/corr/abs-2305-01644.html) | Lightweight personalization while controlling concept overfitting. |
| BLIP-Diffusion: Pre-trained Subject Representation for Controllable Text-to-Image Generation and Editing | NeurIPS 2023 / CoRR | [arXiv](https://arxiv.org/abs/2305.14720) | [GitHub](https://github.com/salesforce/LAVIS/tree/main/projects/blip-diffusion) | [DBLP](https://dblp.org/rec/journals/corr/abs-2305-14720.html) | Uses pretrained subject representations for identity-conditioned generation. |
| FastComposer: Tuning-Free Multi-Subject Image Generation with Localized Attention | NeurIPS 2023 / CoRR | [arXiv](https://arxiv.org/abs/2305.10431) | [GitHub](https://github.com/mit-han-lab/fastcomposer) | [DBLP](https://dblp.org/rec/journals/corr/abs-2305-10431.html) | Multi-subject identity preservation without per-subject finetuning. |
| PhotoMaker: Customizing Realistic Human Photos via Stacked ID Embedding | CVPR 2024 / CoRR | [arXiv](https://arxiv.org/abs/2312.04461) | [GitHub](https://github.com/TencentARC/PhotoMaker) | [DBLP](https://dblp.org/rec/journals/corr/abs-2312-04461.html) | Zero-shot human identity customization. |
| InstantID: Zero-shot Identity-Preserving Generation in Seconds | CoRR/arXiv 2024 | [arXiv](https://arxiv.org/abs/2401.07519) | [GitHub](https://github.com/InstantID/InstantID) | [DBLP](https://dblp.org/rec/journals/corr/abs-2401-07519.html) | Fast identity-preserving generation using ID conditioning. |
| StoryDiffusion: Consistent Self-Attention for Long-Range Image and Video Generation | NeurIPS 2024 / CoRR | [arXiv](https://arxiv.org/abs/2405.01434) | [GitHub](https://github.com/HVision-NKU/StoryDiffusion) | [DBLP](https://dblp.org/rec/journals/corr/abs-2405-01434.html) | Long-range character consistency for stories and videos. |

### Multi-view, 3D, and video consistency

| Paper | Venue/source | Paper page | Code / Project | DBLP | Why it matters |
|---|---|---|---|---|---|
| Zero-1-to-3: Zero-shot One Image to 3D Object | ICCV 2023 / CoRR | [CVF](https://openaccess.thecvf.com/content/ICCV2023/html/Liu_Zero-1-to-3_Zero-shot_One_Image_to_3D_Object_ICCV_2023_paper.html) / [arXiv](https://arxiv.org/abs/2303.11328) | [GitHub](https://github.com/cvlab-columbia/zero123) | [DBLP](https://dblp.org/rec/journals/corr/abs-2303-11328.html) | Novel-view generation from one image. |
| Consistent123: Improve Consistency for One Image to 3D Object Synthesis | CoRR/arXiv 2023 | [arXiv](https://arxiv.org/abs/2309.17261) | [GitHub](https://github.com/florinshen/Consistent123) | [DBLP](https://dblp.org/rec/journals/corr/abs-2309-17261.html) | Improves cross-view consistency for image-to-3D generation. |
| SyncDreamer: Generating Multiview-consistent Images from a Single-view Image | ICLR 2024 / CoRR | [OpenReview](https://openreview.net/forum?id=KmHUlkV1jP) / [arXiv](https://arxiv.org/abs/2309.03453) | [GitHub](https://github.com/liuyuan-pal/SyncDreamer) | [DBLP](https://dblp.org/rec/journals/corr/abs-2309-03453.html) | Synchronizes multi-view diffusion predictions. |
| MVDream: Multi-view Diffusion for 3D Generation | ICLR 2024 / CoRR | [OpenReview](https://openreview.net/forum?id=FUgrjq2pbB) / [arXiv](https://arxiv.org/abs/2308.16512) | [GitHub](https://github.com/bytedance/MVDream) | [DBLP](https://dblp.org/rec/journals/corr/abs-2308-16512.html) | Text/image-conditioned multi-view diffusion for 3D generation. |
| Wonder3D: Single Image to 3D using Cross-Domain Diffusion | CVPR 2024 / CoRR | [arXiv](https://arxiv.org/abs/2310.15008) | [GitHub](https://github.com/xxlong0/Wonder3D) | [DBLP](https://dblp.org/rec/journals/corr/abs-2310-15008.html) | Generates normal/color multi-views for 3D reconstruction. |
| DreamGaussian: Generative Gaussian Splatting for Efficient 3D Content Creation | ICLR 2024 / CoRR | [OpenReview](https://openreview.net/forum?id=UyNXMqnN3c) / [arXiv](https://arxiv.org/abs/2309.16653) | [GitHub](https://github.com/dreamgaussian/dreamgaussian) | [DBLP](https://dblp.org/rec/journals/corr/abs-2309-16653.html) | Fast text/image-to-3D using Gaussian splatting. |
| Align your Latents: High-Resolution Video Synthesis with Latent Diffusion Models | CVPR 2023 / CoRR | [CVF](https://openaccess.thecvf.com/content/CVPR2023/html/Blattmann_Align_Your_Latents_High-Resolution_Video_Synthesis_With_Latent_Diffusion_Models_CVPR_2023_paper.html) / [arXiv](https://arxiv.org/abs/2304.08818) | [Project](https://research.nvidia.com/labs/toronto-ai/VideoLDM/) | [DBLP](https://dblp.org/rec/journals/corr/abs-2304-08818.html) | Video latent diffusion baseline for temporal consistency studies. |
| Text2Video-Zero: Text-to-Image Diffusion Models are Zero-Shot Video Generators | ICCV 2023 / CoRR | [CVF](https://openaccess.thecvf.com/content/ICCV2023/html/Khachatryan_Text2Video-Zero_Text-to-Image_Diffusion_Models_are_Zero-Shot_Video_Generators_ICCV_2023_paper.html) / [arXiv](https://arxiv.org/abs/2303.13439) | [GitHub](https://github.com/Picsart-AI-Research/Text2Video-Zero) | [DBLP](https://dblp.org/rec/journals/corr/abs-2303-13439.html) | Adapts image diffusion to videos with temporal constraints. |
| Tune-A-Video: One-Shot Tuning of Image Diffusion Models for Text-to-Video Generation | ICCV 2023 / CoRR | [CVF](https://openaccess.thecvf.com/content/ICCV2023/html/Wu_Tune-A-Video_One-Shot_Tuning_of_Image_Diffusion_Models_for_Text-to-Video_Generation_ICCV_2023_paper.html) / [arXiv](https://arxiv.org/abs/2212.11565) | [GitHub](https://github.com/showlab/Tune-A-Video) | [DBLP](https://dblp.org/rec/journals/corr/abs-2212-11565.html) | One-shot video tuning and temporal preservation. |
| FateZero: Fusing Attentions for Zero-shot Text-based Video Editing | ICCV 2023 / CoRR | [arXiv](https://arxiv.org/abs/2303.09535) | [GitHub](https://github.com/ChenyangQiQi/FateZero) | [DBLP](https://dblp.org/rec/journals/corr/abs-2303-09535.html) | Attention fusion for temporally consistent video editing. |
| TokenFlow: Consistent Diffusion Features for Consistent Video Editing | ICLR 2024 / CoRR | [OpenReview](https://openreview.net/forum?id=lKK50q2MtV) / [arXiv](https://arxiv.org/abs/2307.10373) | [Project](https://diffusion-tokenflow.github.io/) | [DBLP](https://dblp.org/rec/journals/corr/abs-2307-10373.html) | Feature propagation for cross-frame consistency. |
| CoDeF: Content Deformation Fields for Temporally Consistent Video Processing | CVPR 2024 / CoRR | [arXiv](https://arxiv.org/abs/2308.07926) | [Project](https://qiuyu96.github.io/CoDeF/) | [DBLP](https://dblp.org/rec/journals/corr/abs-2308-07926.html) | Uses deformation fields to preserve video content across time. |
| AnimateDiff: Animate Your Personalized Text-to-Image Diffusion Models without Specific Tuning | ICLR 2024 / CoRR | [OpenReview](https://openreview.net/forum?id=Fx2SbBgcte) / [arXiv](https://arxiv.org/abs/2307.04725) | [GitHub](https://github.com/guoyww/AnimateDiff) | [DBLP](https://dblp.org/rec/journals/corr/abs-2307-04725.html) | Adds motion modules to personalized T2I backbones. |

### Benchmarks and datasets

| Resource | Venue/source | Paper page | Code / Project | DBLP | Diagnostic role |
|---|---|---|---|---|---|
| VBench: Comprehensive Benchmark Suite for Video Generative Models | CVPR 2024 / CoRR | [arXiv](https://arxiv.org/abs/2311.17982) | [GitHub](https://github.com/Vchitect/VBench) | [DBLP](https://dblp.org/rec/journals/corr/abs-2311-17982.html) | Multi-dimensional video generation evaluation, including temporal and subject consistency. |
| FETV: A Benchmark for Fine-Grained Evaluation of Open-Domain Text-to-Video Generation | NeurIPS Datasets and Benchmarks 2023 / CoRR | [arXiv](https://arxiv.org/abs/2311.01813) | [GitHub](https://github.com/llyx97/FETV) | [DBLP](https://dblp.org/rec/journals/corr/abs-2311-01813.html) | Fine-grained T2V prompt and temporal evaluation. |
| MeViS: A Large-scale Benchmark for Video Segmentation with Motion Expressions | ICCV 2023 | [CVF](https://openaccess.thecvf.com/content/ICCV2023/html/Ding_MeViS_A_Large-scale_Benchmark_for_Video_Segmentation_with_Motion_Expressions_ICCV_2023_paper.html) | [GitHub](https://github.com/henghuiding/MeViS) | [DBLP](https://dblp.org/rec/conf/iccv/DingLWWL23.html) | Motion-expression video segmentation for temporal grounding diagnostics. |
| MOSE: A New Dataset for Video Object Segmentation in Complex Scenes | ICCV 2023 | [CVF](https://openaccess.thecvf.com/content/ICCV2023/html/Ding_MOSE_A_New_Dataset_for_Video_Object_Segmentation_in_Complex_Scenes_ICCV_2023_paper.html) | [GitHub](https://github.com/henghuiding/MOSE-api) | [DBLP](https://dblp.org/rec/conf/iccv/DingLWX23.html) | Video object segmentation under occlusion and complex motion. |
| Tracking Any Object Amodally | ECCV 2020 | [ECCV](https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/1475_ECCV_2020_paper.php) | [GitHub](https://github.com/TAO-Dataset/tao) | [DBLP](https://dblp.org/rec/conf/eccv/DaveRKOP20.html) | Long-tail object tracking dataset for persistence diagnostics. |
| Video Scene Parsing in the Wild | CVPR 2021 | [CVF](https://openaccess.thecvf.com/content/CVPR2021/html/Miao_Video_Scene_Parsing_in_the_Wild_CVPR_2021_paper.html) | [GitHub](https://github.com/VSPW-dataset/VSPW_code) | [DBLP](https://dblp.org/rec/conf/cvpr/MiaoW0XY21.html) | Video scene parsing for scene-state continuity checks. |
| nuScenes: A Multimodal Dataset for Autonomous Driving | CVPR 2020 | [CVF](https://openaccess.thecvf.com/content_CVPR_2020/html/Caesar_nuScenes_A_Multimodal_Dataset_for_Autonomous_Driving_CVPR_2020_paper.html) | [GitHub](https://github.com/nutonomy/nuscenes-devkit) | [DBLP](https://dblp.org/rec/conf/cvpr/CaesarBVPDRF20.html) | Driving scene data for geometry and dynamic-state consistency. |

---

## Normative consistency

Normative consistency asks whether generated content satisfies evaluative principles such as preference, aesthetics, safety, fairness, concept restrictions, physical plausibility, commonsense, action consequence, and world-state validity.

### Preference and aesthetics

| Paper/resource | Venue/source | Paper page | Code / Project | DBLP | Why it matters |
|---|---|---|---|---|---|
| Pick-a-Pic: An Open Dataset of User Preferences for Text-to-Image Generation | NeurIPS 2023 / CoRR | [arXiv](https://arxiv.org/abs/2305.01569) | [GitHub](https://github.com/yuvalkirstain/PickScore) | [DBLP](https://dblp.org/rec/journals/corr/abs-2305-01569.html) | Pairwise preference data and PickScore-style evaluation. |
| ImageReward: Learning and Evaluating Human Preferences for Text-to-Image Generation | NeurIPS 2023 / CoRR | [arXiv](https://arxiv.org/abs/2304.05977) | [GitHub](https://github.com/THUDM/ImageReward) | [DBLP](https://dblp.org/rec/journals/corr/abs-2304-05977.html) | Learned preference reward for ranking and optimization. |
| HPSv2: Human Preference Score v2 | CoRR/arXiv 2023 | [arXiv](https://arxiv.org/abs/2306.09341) | [GitHub](https://github.com/tgxs002/HPSv2) | [DBLP](https://dblp.org/rec/journals/corr/abs-2306-09341.html) | Human-preference benchmark and scoring for T2I outputs. |
| Diffusion Model Alignment Using Direct Preference Optimization | CoRR/arXiv 2023 | [arXiv](https://arxiv.org/abs/2311.12908) | [GitHub](https://github.com/SalesforceAIResearch/DiffusionDPO) | [DBLP](https://dblp.org/rec/journals/corr/abs-2311-12908.html) | Direct preference optimization for diffusion models. |
| Training Diffusion Models with Reinforcement Learning | ICLR 2024 / CoRR | [OpenReview](https://openreview.net/forum?id=YCWjhGrJFD) / [arXiv](https://arxiv.org/abs/2305.13301) | [GitHub](https://github.com/jannerm/ddpo) | [DBLP](https://dblp.org/rec/journals/corr/abs-2305-13301.html) | Reward-driven diffusion policy optimization. |
| AlignProp: Aligning Diffusion Models with Human Feedback | ICLR 2024 / CoRR | [arXiv](https://arxiv.org/abs/2310.03739) | -- | [DBLP](https://dblp.org/rec/journals/corr/abs-2310-03739.html) | Backpropagates reward signals through diffusion sampling. |
| Diffusion Model Alignment Using Direct Preference Optimization with KL Regularization | CoRR/arXiv 2023 | [arXiv](https://arxiv.org/abs/2305.16381) | -- | [DBLP](https://dblp.org/rec/journals/corr/abs-2305-16381.html) | KL-regularized preference optimization for diffusion generation. |

### Safety, concept editing, and erasure

| Paper/resource | Venue/source | Paper page | Code / Project | DBLP | Why it matters |
|---|---|---|---|---|---|
| Safe Latent Diffusion: Mitigating Inappropriate Degeneration in Diffusion Models | CVPR 2023 / CoRR | [CVF](https://openaccess.thecvf.com/content/CVPR2023/html/Schramowski_Safe_Latent_Diffusion_Mitigating_Inappropriate_Degeneration_in_Diffusion_Models_CVPR_2023_paper.html) / [arXiv](https://arxiv.org/abs/2211.05105) | [GitHub](https://github.com/ml-research/safe-latent-diffusion) | [DBLP](https://dblp.org/rec/journals/corr/abs-2211-05105.html) | Inference-time safety guidance for latent diffusion. |
| Erasing Concepts from Diffusion Models | ICCV 2023 / CoRR | [CVF](https://openaccess.thecvf.com/content/ICCV2023/html/Gandikota_Erasing_Concepts_from_Diffusion_Models_ICCV_2023_paper.html) / [arXiv](https://arxiv.org/abs/2303.07345) | [Project](https://erasing.baulab.info/) | [DBLP](https://dblp.org/rec/journals/corr/abs-2303-07345.html) | Removes undesirable concepts from diffusion models. |
| Ablating Concepts in Text-to-Image Diffusion Models | ICCV 2023 / CoRR | [CVF](https://openaccess.thecvf.com/content/ICCV2023/html/Kumari_Ablating_Concepts_in_Text-to-Image_Diffusion_Models_ICCV_2023_paper.html) / [arXiv](https://arxiv.org/abs/2303.13516) | [Project](https://www.cs.cmu.edu/~concept-ablation/) | [DBLP](https://dblp.org/rec/journals/corr/abs-2303-13516.html) | Edits or ablates concepts while retaining general model behavior. |
| Unified Concept Editing in Diffusion Models | WACV 2024 / CoRR | [arXiv](https://arxiv.org/abs/2308.14761) | [GitHub](https://github.com/rohitgandikota/unified-concept-editing) | [DBLP](https://dblp.org/rec/journals/corr/abs-2308-14761.html) | Multi-concept editing and safety intervention. |
| MACE: Mass Concept Erasure in Diffusion Models | CVPR 2024 / CoRR | [arXiv](https://arxiv.org/abs/2403.06135) | [GitHub](https://github.com/Shilin-LU/MACE) | [DBLP](https://dblp.org/rec/journals/corr/abs-2403-06135.html) | Scalable concept erasure for many target concepts. |
| Forget-Me-Not: Learning to Forget in Text-to-Image Diffusion Models | CoRR/arXiv 2023 | [arXiv](https://arxiv.org/abs/2303.17591) | -- | [DBLP](https://dblp.org/rec/journals/corr/abs-2303-17591.html) | Attention-based concept forgetting. |
| T2VSafetyBench: Evaluating the Safety of Text-to-Video Generative Models | CoRR/arXiv 2024 | [arXiv](https://arxiv.org/abs/2409.08615) | -- | [DBLP](https://dblp.org/rec/journals/corr/abs-2409-08615.html) | Safety benchmark for text-to-video generation. |

### Physical, causal, and world consistency

| Paper/resource | Venue/source | Paper page | Code / Project | DBLP | Why it matters |
|---|---|---|---|---|---|
| WorldDreamer: Towards General World Models for Video Generation via Predicting Masked Tokens | CoRR/arXiv 2024 | [arXiv](https://arxiv.org/abs/2401.09985) | -- | [DBLP](https://dblp.org/rec/journals/corr/abs-2401-09985.html) | Driving/world video generation with structured world priors. |
| Genie: Generative Interactive Environments | ICML 2024 | [PMLR](https://proceedings.mlr.press/v235/bruce24a.html) | [Project](https://sites.google.com/view/genie-2024/) | [DBLP](https://dblp.org/rec/conf/icml/BruceDDLBGDE24.html) | Interactive generative environments from video data. |
| Learning Interactive Real-World Simulators | ICLR 2024 | [OpenReview](https://openreview.net/forum?id=sFyTZEqmUY) | [Project](https://universal-simulator.github.io/unisim/) | [DBLP](https://dblp.org/rec/conf/iclr/YangYCW0L0RD24.html) | Action-conditioned real-world simulation for interactive world modeling. |
| VideoPhy: Evaluating Physical Commonsense for Video Generation | ICLR 2025 / CoRR | [arXiv](https://arxiv.org/abs/2406.03520) | [GitHub](https://github.com/Hritikbansal/videophy) | [DBLP](https://dblp.org/rec/journals/corr/abs-2406-03520.html) | Physical commonsense diagnostics for generated videos. |
| PhyGenBench: Towards World Simulator | CoRR/arXiv 2024 | [arXiv](https://arxiv.org/abs/2407.08024) | [GitHub](https://github.com/OpenGVLab/PhyGenBench) | [DBLP](https://dblp.org/rec/journals/corr/abs-2407-08024.html) | Benchmarking physical-law consistency in generated videos. |

---

## Candidate and maintenance policy

The previous README contained many useful but unverified or non-bibliographic entries, including broad topics such as prompt expansion, verifier-guided generation, world-consistent video diffusion, and metric families. These are intentionally not mixed into the verified main tables.

To add a new item to the main README:

1. Search arXiv / CVF OpenAccess / OpenReview / ACM / PMLR for a stable paper page.
2. Search GitHub or the official project page for code or demos; do not use unofficial reimplementations unless explicitly marked as such.
3. Search DBLP and add the DBLP record URL when available.
4. Use the venue/source supported by the verified sources. If the only bibliographic record is CoRR/arXiv, write `CoRR/arXiv YEAR`.
5. Add a one-sentence explanation of the consistency issue it addresses.
6. Run:

```bash
python scripts/verify_dblp_links.py --readme README.md --out resources/dblp_verification.csv
```

If a paper is important but one of the required sources is missing, keep it in a separate candidate file until it can be verified or mark the missing source as `--` with a clear reason.

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
