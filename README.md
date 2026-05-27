# Awesome Consistency in Diffusion-Based Visual Generation

[![USTC](https://img.shields.io/badge/USTC-University%20of%20Science%20and%20Technology%20of%20China-005BAC?style=for-the-badge)](https://en.ustc.edu.cn/)
[![Tsinghua](https://img.shields.io/badge/Tsinghua-University-7A1FA2?style=for-the-badge)](https://www.tsinghua.edu.cn/en/)
[![HUST](https://img.shields.io/badge/HUST-Huazhong%20University%20of%20Science%20and%20Technology-0055A4?style=for-the-badge)](https://english.hust.edu.cn/)
[![Cambridge](https://img.shields.io/badge/Cambridge-University%20of%20Cambridge-A3C1AD?style=for-the-badge)](https://www.cam.ac.uk/)
[![Li Auto](https://img.shields.io/badge/Li%20Auto-Industry%20Partner-111111?style=for-the-badge)](https://www.lixiang.com/en)
[![ByteDance](https://img.shields.io/badge/ByteDance-Industry%20Partner-111111?style=for-the-badge)](https://www.bytedance.com/)

[![Validate resource tables](https://github.com/Shawn-CodeDev/Awesome-Consistency-Diffusion-Visual-Generation/actions/workflows/validate-resources.yml/badge.svg)](https://github.com/Shawn-CodeDev/Awesome-Consistency-Diffusion-Visual-Generation/actions/workflows/validate-resources.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

This repository accompanies the survey:

> **Consistency in Diffusion-Based Visual Generation: A Survey**  
> Song Yan, Wei Zhai, Chenfeng Wang, Ruixuan Li, Zhangping Yang, Yancheng Cai, Tao Zhang, Ling Wang, Yunwei Lan, Yujie He, Yang Cao, Min Li, Zheng-Jun Zha.

This repository collects papers, methods, benchmarks, datasets, evaluators, and diagnostic resources for **consistency in diffusion-based visual generation**. The main organization follows the survey taxonomy: **External Consistency**, **Internal Consistency**, and **Normative Consistency**. Within each relation, entries are grouped into **Methods**, **Benchmarks & Evaluators**, and **Datasets & Data Resources**.

Note: the top affiliation strip now uses stable Shields SVG badges instead of hot-linked logo files, because remote institutional logo image URLs often break in GitHub Markdown rendering.

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

## External consistency

External consistency asks whether generated content follows externally specified conditions: text prompts, layouts, boxes, masks, depth maps, poses, reference images, editing instructions, or other user/task controls.

**Current coverage: 125 entries.**

### Methods

- [GLIDE](https://arxiv.org/abs/2112.10741)
- [Imagen](https://arxiv.org/abs/2205.11487)
- [Latent Diffusion Models](https://arxiv.org/abs/2112.10752)
- [Composable Diffusion Models](https://arxiv.org/abs/2206.01714)
- [Structured Diffusion Guidance](https://arxiv.org/search/?query=Structured+Diffusion+Guidance&searchtype=all)
- [StructureDiffusion](https://arxiv.org/abs/2212.05032)
- [Attend-and-Excite](https://github.com/yuval-alaluf/Attend-and-Excite)
- [BoxDiff](https://github.com/showlab/BoxDiff)
- [Composer](https://github.com/damo-vilab/composer)
- [MultiDiffusion](https://multidiffusion.github.io/)
- [LLM-grounded Diffusion](https://llm-grounded-diffusion.github.io/)
- [SynGen](https://arxiv.org/abs/2308.07037)
- [RPG: Recaption, Plan, and Generate](https://github.com/YangLing0818/RPG-DiffusionMaster)
- [CONFORM](https://arxiv.org/search/?query=CONFORM+text+to+image+diffusion&searchtype=all)
- [Divide-and-Bind](https://arxiv.org/search/?query=Divide+and+Bind+text+to+image&searchtype=all)
- [Linguistic Binding in Diffusion](https://arxiv.org/search/?query=linguistic+binding+text+to+image+diffusion&searchtype=all)
- [Promptist](https://arxiv.org/search/?query=Promptist+text+to+image&searchtype=all)
- [BeautifulPrompt](https://arxiv.org/search/?query=BeautifulPrompt+text+to+image&searchtype=all)
- [Prompt Expansion for Text-to-Image](https://arxiv.org/search/?query=prompt+expansion+text+to+image+diffusion&searchtype=all)
- [Prompt Decomposition for T2I](https://arxiv.org/search/?query=prompt+decomposition+text-to-image+evaluation&searchtype=all)
- [ControlNet](https://github.com/lllyasviel/ControlNet)
- [GLIGEN](https://github.com/gligen/GLIGEN)
- [T2I-Adapter](https://github.com/TencentARC/T2I-Adapter)
- [IP-Adapter](https://github.com/tencent-ailab/IP-Adapter)
- [AnyDoor](https://github.com/ali-vilab/AnyDoor)
- [FreeDoM](https://github.com/vvictoryuki/FreeDoM)
- [HumanSD](https://github.com/IDEA-Research/HumanSD)
- [UniControl](https://arxiv.org/abs/2305.11147)
- [Uni-ControlNet](https://arxiv.org/abs/2305.16322)
- [Ctrl-Adapter](https://openreview.net/forum?id=ny8T8OuNHe)
- [UniCon](https://openreview.net/forum?id=8jb0e1gLyd)
- [InstanceDiffusion](https://people.eecs.berkeley.edu/~xdwang/projects/instancediffusion/)
- [ControlNet++](https://arxiv.org/search/?query=ControlNet%2B%2B+diffusion&searchtype=all)
- [ControlNet-XS](https://arxiv.org/search/?query=ControlNet-XS&searchtype=all)
- [ControlLoRA](https://arxiv.org/search/?query=ControlLoRA+diffusion&searchtype=all)
- [SparseCtrl](https://arxiv.org/search/?query=SparseCtrl&searchtype=all)
- [SemanticControl](https://arxiv.org/search/?query=SemanticControl+diffusion&searchtype=all)
- [LayoutDiffusion](https://arxiv.org/search/?query=LayoutDiffusion&searchtype=all)
- [LayoutDM](https://arxiv.org/search/?query=LayoutDM+diffusion&searchtype=all)
- [SceneComposer](https://arxiv.org/search/?query=SceneComposer+text+to+image&searchtype=all)
- [Scene Graph Diffusion](https://arxiv.org/search/?query=scene+graph+diffusion+text+to+image&searchtype=all)
- [DetDiffusion](https://arxiv.org/search/?query=DetDiffusion&searchtype=all)
- [Grounded Diffusion](https://arxiv.org/search/?query=grounded+diffusion+text+to+image&searchtype=all)
- [SAM-guided Diffusion Editing](https://arxiv.org/search/?query=SAM+guided+diffusion+editing&searchtype=all)
- [Diffusion Posterior Sampling](https://arxiv.org/search/?query=Diffusion+Posterior+Sampling&searchtype=all)
- [Universal Guidance for Diffusion Models](https://arxiv.org/search/?query=Universal+Guidance+for+Diffusion+Models&searchtype=all)
- [Classifier Guidance](https://arxiv.org/search/?query=classifier+guidance+diffusion+models&searchtype=all)
- [Classifier-Free Guidance](https://arxiv.org/search/?query=classifier-free+diffusion+guidance&searchtype=all)
- [SDEdit](https://arxiv.org/abs/2108.01073)
- [Prompt-to-Prompt](https://github.com/google/prompt-to-prompt)
- [Null-Text Inversion](https://null-text-inversion.github.io/)
- [DiffEdit](https://github.com/Xiang-cd/DiffEdit-stable-diffusion)
- [InstructPix2Pix](https://github.com/timothybrooks/instruct-pix2pix)
- [InstructDiffusion](https://github.com/cientgu/InstructDiffusion)
- [Imagic](https://imagic-editing.github.io/)
- [Paint-by-Example](https://github.com/Fantasy-Studio/Paint-by-Example)
- [Plug-and-Play Diffusion Features](https://pnp-diffusion.github.io/)
- [Pix2Pix-Zero](https://pix2pixzero.github.io/)
- [MasaCtrl](https://github.com/TencentARC/MasaCtrl)
- [LEDITS++](https://arxiv.org/abs/2311.16711)
- [DragonDiffusion](https://github.com/MC-E/DragonDiffusion)
- [DragDiffusion](https://github.com/Yujun-Shi/DragDiffusion)
- [FreeDrag](https://arxiv.org/search/?query=FreeDrag+diffusion&searchtype=all)
- [DiffEditor](https://arxiv.org/search/?query=DiffEditor+diffusion&searchtype=all)
- [SEGA](https://arxiv.org/search/?query=SEGA+semantic+guidance+diffusion&searchtype=all)
- [Emu Edit](https://arxiv.org/search/?query=Emu+Edit+image+editing&searchtype=all)
- [SmartEdit](https://arxiv.org/search/?query=SmartEdit+diffusion&searchtype=all)
- [BrushNet](https://arxiv.org/search/?query=BrushNet+diffusion+inpainting&searchtype=all)
- [PowerPaint](https://arxiv.org/search/?query=PowerPaint+diffusion&searchtype=all)
- [Inpaint Anything](https://arxiv.org/search/?query=Inpaint+Anything+diffusion&searchtype=all)
- [TextDiffuser](https://arxiv.org/search/?query=TextDiffuser&searchtype=all)
- [TextDiffuser-2](https://arxiv.org/search/?query=TextDiffuser-2&searchtype=all)
- [AnyText](https://arxiv.org/search/?query=AnyText+diffusion&searchtype=all)
- [GlyphDraw](https://arxiv.org/search/?query=GlyphDraw&searchtype=all)
- [GlyphControl](https://arxiv.org/search/?query=GlyphControl&searchtype=all)
- [TryOnDiffusion](https://arxiv.org/search/?query=TryOnDiffusion&searchtype=all)
- [StableVITON](https://github.com/rlawjdghek/StableVITON)
- [IDM-VTON](https://github.com/yisol/IDM-VTON)
- [CatVTON](https://github.com/Zheng-Chong/CatVTON)
- [OOTDiffusion](https://github.com/levihsu/OOTDiffusion)
- [LaDI-VTON](https://arxiv.org/search/?query=LaDI-VTON&searchtype=all)
- [AnyDressing](https://arxiv.org/search/?query=AnyDressing&searchtype=all)
- [PosterCraft](https://arxiv.org/search/?query=PosterCraft&searchtype=all)
- [CreatiPoster](https://arxiv.org/search/?query=CreatiPoster&searchtype=all)
- [PosterMaker](https://arxiv.org/search/?query=PosterMaker+diffusion&searchtype=all)

### Benchmarks & Evaluators

- [TIFA](https://github.com/Yushi-Hu/tifa)
- [GenEval](https://github.com/djghosh13/geneval)
- [T2I-CompBench](https://github.com/Karine-Huang/T2I-CompBench)
- [GenEval2](https://github.com/facebookresearch/GenEval2)
- [HRS-Bench](https://github.com/eslambakr/HRS_benchmark)
- [DPG-Bench](https://github.com/TencentQQGYLab/ELLA)
- [GenAI-Bench / VQAScore](https://github.com/linzhiqiu/t2v_metrics)
- [DrawBench](https://arxiv.org/search/?query=DrawBench+text+to+image&searchtype=all)
- [PartiPrompts](https://arxiv.org/search/?query=PartiPrompts&searchtype=all)
- [DSG: Davidsonian Scene Graph evaluation](https://arxiv.org/search/?query=Davidsonian+Scene+Graph+text+to+image&searchtype=all)
- [VIEScore](https://arxiv.org/search/?query=VIEScore&searchtype=all)
- [EditBench](https://arxiv.org/search/?query=Imagen+Editor+EditBench&searchtype=all)
- [ConceptBed](https://github.com/ConceptBed/evaluations)
- [CountBench](https://arxiv.org/search/?query=counting+benchmark+text+to+image&searchtype=all)
- [SpatialBench](https://arxiv.org/search/?query=spatial+relation+benchmark+text+to+image&searchtype=all)
- [ObjectAttributeBench](https://arxiv.org/search/?query=object+attribute+benchmark+text+to+image&searchtype=all)
- [RelationBench](https://arxiv.org/search/?query=relation+benchmark+text+to+image+diffusion&searchtype=all)
- [TypographyBench](https://arxiv.org/search/?query=text+rendering+benchmark+diffusion&searchtype=all)
- [VTON evaluation suites](https://arxiv.org/search/?query=virtual+try-on+benchmark+diffusion&searchtype=all)
- [Human pose generation evaluation](https://arxiv.org/search/?query=human+pose+conditioned+diffusion+benchmark&searchtype=all)

### Datasets & Data Resources

- [MagicBrush](https://github.com/OSU-NLP-Group/MagicBrush)
- [InstructPix2Pix dataset](https://github.com/timothybrooks/instruct-pix2pix)
- [COCO Captions](https://cocodataset.org/)
- [Visual Genome](https://homes.cs.washington.edu/~ranjay/visualgenome/)
- [OpenImages](https://storage.googleapis.com/openimages/web/index.html)
- [ADE20K](https://groups.csail.mit.edu/vision/datasets/ADE20K/)
- [LAION-5B](https://laion.ai/blog/laion-5b/)
- [LAION-Aesthetics](https://laion.ai/blog/laion-aesthetics/)
- [CC3M](https://ai.google.com/research/ConceptualCaptions/)
- [CC12M](https://github.com/google-research-datasets/conceptual-12m)
- [SA-1B](https://segment-anything.com/dataset/index.html)
- [LVIS](https://www.lvisdataset.org/)
- [DeepFashion](http://mmlab.ie.cuhk.edu.hk/projects/DeepFashion.html)
- [VITON-HD](https://github.com/shadow2496/VITON-HD)
- [DressCode](https://github.com/aimagelab/dress-code)
- [OpenPose / pose datasets](https://arxiv.org/search/?query=pose+dataset+human+image+generation&searchtype=all)
- [RefCOCO](https://arxiv.org/search/?query=RefCOCO+referring+expression&searchtype=all)
- [GQA](https://cs.stanford.edu/people/dorarad/gqa/)
- [CLEVR](https://cs.stanford.edu/people/jcjohns/clevr/)
- [OCR/text rendering corpora](https://arxiv.org/search/?query=text+rendering+dataset+image+generation&searchtype=all)

## Internal consistency

Internal consistency asks whether generated states remain mutually compatible across identities, subjects, views, frames, videos, or story sequences.

**Current coverage: 123 entries.**

### Methods

- [Textual Inversion](https://github.com/rinongal/textual_inversion)
- [DreamBooth](https://dreambooth.github.io/)
- [Custom Diffusion](https://github.com/adobe-research/custom-diffusion)
- [Perfusion](https://research.nvidia.com/labs/par/Perfusion/)
- [SVDiff](https://arxiv.org/search/?query=SVDiff+personalization&searchtype=all)
- [P+](https://arxiv.org/search/?query=P%2B+textual+inversion&searchtype=all)
- [NeTI](https://arxiv.org/search/?query=NeTI+textual+inversion&searchtype=all)
- [ProSpect](https://arxiv.org/search/?query=ProSpect+personalized+diffusion&searchtype=all)
- [DisenBooth](https://arxiv.org/search/?query=DisenBooth&searchtype=all)
- [SuTI](https://arxiv.org/search/?query=SuTI+subject+driven+text+to+image&searchtype=all)
- [BLIP-Diffusion](https://github.com/salesforce/LAVIS/tree/main/projects/blip-diffusion)
- [ELITE](https://github.com/csyxwei/ELITE)
- [FastComposer](https://github.com/mit-han-lab/fastcomposer)
- [Subject-Diffusion](https://github.com/OPPO-Mente-Lab/Subject-Diffusion)
- [PhotoMaker](https://github.com/TencentARC/PhotoMaker)
- [InstantID](https://github.com/InstantID/InstantID)
- [IP-Adapter-FaceID](https://github.com/tencent-ailab/IP-Adapter)
- [PuLID](https://github.com/ToTheBeginning/PuLID)
- [InfiniteYou](https://arxiv.org/search/?query=InfiniteYou+identity+diffusion&searchtype=all)
- [RealCustom](https://arxiv.org/search/?query=RealCustom+personalized+diffusion&searchtype=all)
- [InstantCharacter](https://arxiv.org/search/?query=InstantCharacter+diffusion&searchtype=all)
- [ConsiStory](https://github.com/NVlabs/consistory)
- [StoryDiffusion](https://github.com/HVision-NKU/StoryDiffusion)
- [StyleAligned](https://style-aligned-gen.github.io/)
- [The Chosen One](https://omriavrahami.com/the-chosen-one/)
- [ConsistentID](https://arxiv.org/abs/2404.16771)
- [CharaConsist](https://arxiv.org/search/?query=CharaConsist&searchtype=all)
- [MagicID](https://arxiv.org/search/?query=MagicID+video+customization&searchtype=all)
- [PersonalVideo](https://arxiv.org/search/?query=PersonalVideo+video+customization&searchtype=all)
- [Phantom](https://arxiv.org/search/?query=Phantom+subject+consistent+video&searchtype=all)
- [Preserve and Personalize](https://rlgnswk.github.io/PreserveAndPersonalize_ProjectPage/)
- [ConceptPrism](https://arxiv.org/search/?query=ConceptPrism&searchtype=all)
- [Zero-1-to-3](https://github.com/cvlab-columbia/zero123)
- [One-2-3-45](https://github.com/One-2-3-45/One-2-3-45)
- [Zero123++](https://arxiv.org/search/?query=Zero123%2B%2B&searchtype=all)
- [Cascade-Zero123](https://github.com/EnVision-Research/Cascade-Zero123)
- [Consistent123](https://arxiv.org/abs/2309.17261)
- [SyncDreamer](https://github.com/liuyuan-pal/SyncDreamer)
- [MVDream](https://github.com/bytedance/MVDream)
- [Wonder3D](https://github.com/xxlong0/Wonder3D)
- [ViewDiff](https://lukashoel.github.io/ViewDiff/)
- [EscherNet](https://kxhit.github.io/EscherNet/)
- [DreamGaussian](https://github.com/dreamgaussian/dreamgaussian)
- [LGM](https://github.com/3DTopia/LGM)
- [GRM](https://justimyhxu.github.io/projects/grm/)
- [Instant3D](https://arxiv.org/search/?query=Instant3D+diffusion&searchtype=all)
- [TripoSR](https://github.com/VAST-AI-Research/TripoSR)
- [CRM](https://arxiv.org/search/?query=CRM+3D+reconstruction+diffusion&searchtype=all)
- [LRM](https://arxiv.org/search/?query=Large+Reconstruction+Model+3D&searchtype=all)
- [VideoLDM](https://research.nvidia.com/labs/toronto-ai/VideoLDM/)
- [Text2Video-Zero](https://github.com/Picsart-AI-Research/Text2Video-Zero)
- [Tune-A-Video](https://github.com/showlab/Tune-A-Video)
- [AnimateDiff](https://github.com/guoyww/AnimateDiff)
- [FateZero](https://github.com/ChenyangQiQi/FateZero)
- [Video-P2P](https://github.com/ShaoTengLiu/Video-P2P)
- [TokenFlow](https://diffusion-tokenflow.github.io/)
- [CoDeF](https://qiuyu96.github.io/CoDeF/)
- [Rerender A Video](https://www.mmlab-ntu.com/project/rerender/)
- [COVE](https://github.com/wangjiangshan0725/COVE)
- [VideoCrafter](https://github.com/AILab-CVC/VideoCrafter)
- [VideoCrafter2](https://github.com/AILab-CVC/VideoCrafter)
- [ModelScopeT2V](https://github.com/modelscope/modelscope)
- [Make-A-Video](https://arxiv.org/search/?query=Make-A-Video&searchtype=all)
- [Imagen Video](https://arxiv.org/search/?query=Imagen+Video&searchtype=all)
- [Phenaki](https://arxiv.org/search/?query=Phenaki+video&searchtype=all)
- [VideoFusion](https://arxiv.org/search/?query=VideoFusion+diffusion&searchtype=all)
- [Latte](https://arxiv.org/search/?query=Latte+video+diffusion&searchtype=all)
- [VideoPoet](https://arxiv.org/search/?query=VideoPoet&searchtype=all)
- [Lumiere](https://arxiv.org/search/?query=Lumiere+video+diffusion&searchtype=all)
- [Sora technical report](https://openai.com/research/video-generation-models-as-world-simulators)
- [MovieDreamer](https://arxiv.org/search/?query=MovieDreamer&searchtype=all)
- [TaleCrafter](https://arxiv.org/search/?query=TaleCrafter&searchtype=all)
- [One-Prompt-One-Story](https://arxiv.org/search/?query=One-Prompt-One-Story&searchtype=all)
- [Animate-A-Story](https://github.com/AILab-CVC/Animate-A-Story)
- [MotionStream](https://openreview.net/forum?id=v1DKz5Vxr7)
- [VideoDirectorGPT](https://arxiv.org/search/?query=VideoDirectorGPT&searchtype=all)
- [ShotAdapter](https://arxiv.org/search/?query=ShotAdapter+text+to+multi-shot+video&searchtype=all)
- [VideoBooth](https://arxiv.org/search/?query=VideoBooth&searchtype=all)
- [DreamVideo](https://arxiv.org/search/?query=DreamVideo&searchtype=all)
- [Vlogger](https://arxiv.org/search/?query=Vlogger+video+generation&searchtype=all)
- [MagicAnimate](https://github.com/magic-research/magic-animate)
- [AnimateAnyone](https://arxiv.org/search/?query=AnimateAnyone&searchtype=all)
- [Champ](https://arxiv.org/search/?query=Champ+controllable+human+image+animation&searchtype=all)

### Benchmarks & Evaluators

- [MVG-Bench](https://github.com/xiexh20/MVGBench)
- [MET3R](https://github.com/mohammadasim98/met3r)
- [VBench](https://github.com/Vchitect/VBench)
- [Video-Bench](https://github.com/Video-Bench/Video-Bench)
- [EvalCrafter](https://github.com/evalcrafter/EvalCrafter)
- [FETV](https://github.com/llyx97/FETV)
- [ViStoryBench](https://github.com/ViStoryBench/ViStoryBench)
- [T2V-CompBench](https://arxiv.org/search/?query=T2V-CompBench&searchtype=all)
- [VideoScore](https://arxiv.org/search/?query=VideoScore+video+generation+evaluation&searchtype=all)
- [VideoPhy temporal subset](https://github.com/Hritikbansal/videophy)
- [Long-video consistency evaluation](https://arxiv.org/search/?query=long+video+consistency+benchmark&searchtype=all)
- [Character consistency benchmark](https://arxiv.org/search/?query=character+consistency+benchmark+text+to+image&searchtype=all)
- [Multi-view consistency metrics](https://arxiv.org/search/?query=multi-view+consistency+metric+generated+images&searchtype=all)
- [Story visualization benchmark](https://arxiv.org/search/?query=story+visualization+benchmark+consistency&searchtype=all)
- [Video editing consistency metrics](https://arxiv.org/search/?query=video+editing+consistency+metric+diffusion&searchtype=all)
- [CLIP frame consistency](https://arxiv.org/search/?query=CLIP+frame+consistency+video+generation&searchtype=all)
- [DINO tracking consistency](https://arxiv.org/search/?query=DINO+tracking+consistency+video+generation&searchtype=all)
- [Identity similarity metrics](https://arxiv.org/search/?query=identity+similarity+metric+personalized+generation&searchtype=all)
- [Face recognition metrics](https://arxiv.org/search/?query=face+identity+metric+diffusion+generation&searchtype=all)
- [LPIPS temporal smoothness](https://arxiv.org/search/?query=LPIPS+temporal+smoothness+video+generation&searchtype=all)

### Datasets & Data Resources

- [MeViS](https://github.com/henghuiding/MeViS)
- [MOSE](https://github.com/henghuiding/MOSE-api)
- [TAO](https://github.com/TAO-Dataset/tao)
- [VSPW](https://github.com/VSPW-dataset/VSPW_code)
- [nuScenes](https://github.com/nutonomy/nuscenes-devkit)
- [KITTI](https://www.cvlibs.net/datasets/kitti/)
- [Waymo Open Dataset](https://waymo.com/open/)
- [DAVIS](https://davischallenge.org/)
- [YouTube-VOS](https://youtube-vos.org/)
- [LaSOT](https://cis.temple.edu/lasot/)
- [TrackingNet](https://tracking-net.org/)
- [Objaverse](https://objaverse.allenai.org/)
- [Objaverse-XL](https://objaverse.allenai.org/objaverse-xl/)
- [CO3D](https://github.com/facebookresearch/co3d)
- [RealEstate10K](https://google.github.io/realestate10k/)
- [ScanNet](http://www.scan-net.org/)
- [ShapeNet](https://shapenet.org/)
- [Google Scanned Objects](https://research.google/tools/datasets/google-scanned-objects/)
- [MVImgNet](https://github.com/GAP-LAB-CUHK-SZ/MVImgNet)
- [Kubric](https://github.com/google-research/kubric)

## Normative consistency

Normative consistency asks whether generated content satisfies evaluative principles such as preference, aesthetics, safety, fairness, concept restrictions, physical plausibility, commonsense, action consequence, and world-state validity.

**Current coverage: 107 entries.**

### Methods

- [Pick-a-Pic / PickScore](https://github.com/yuvalkirstain/PickScore)
- [ImageReward](https://github.com/zai-org/ImageReward)
- [HPS](https://arxiv.org/search/?query=Human+Preference+Score+text+to+image&searchtype=all)
- [HPSv2](https://github.com/tgxs002/HPSv2)
- [HPSv3](https://github.com/MizzenAI/HPSv3)
- [MPS](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Learning_Multi-Dimensional_Human_Preference_for_Text-to-Image_Generation_CVPR_2024_paper.html)
- [VisionReward](https://github.com/zai-org/VisionReward)
- [Diffusion-DPO](https://github.com/SalesforceAIResearch/DiffusionDPO)
- [DDPO](https://github.com/jannerm/ddpo)
- [AlignProp](https://arxiv.org/abs/2310.03739)
- [DPOK](https://arxiv.org/abs/2305.16381)
- [D3PO](https://arxiv.org/abs/2402.08385)
- [SPO](https://openaccess.thecvf.com/content/CVPR2025/html/Liang_Aesthetic_Post-Training_Diffusion_Models_from_Generic_Preferences_with_Step-by-step_Preference_CVPR_2025_paper.html)
- [DSPO](https://openreview.net/forum?id=7f70331dbe58ad59d83941dfa7d975aa)
- [RankDPO](https://openaccess.thecvf.com/content/ICCV2025/papers/Karthik_Scalable_Ranked_Preference_Optimization_for_Text-to-Image_Generation_ICCV_2025_paper.pdf)
- [CMPO / CaPO](https://openaccess.thecvf.com/content/CVPR2025/html/Lee_Calibrated_Multi-Preference_Optimization_for_Aligning_Diffusion_Models_CVPR_2025_paper.html)
- [Diffusion-NPO](https://openreview.net/forum?id=BADtQ9p1T2)
- [BranchGRPO](https://openreview.net/forum?id=93N8hU2q5V)
- [Flow-GRPO](https://arxiv.org/search/?query=Flow-GRPO+diffusion&searchtype=all)
- [RLAIF for Diffusion](https://arxiv.org/search/?query=RLAIF+diffusion+text+to+image&searchtype=all)
- [Safe Latent Diffusion](https://github.com/ml-research/safe-latent-diffusion)
- [Erasing Concepts from Diffusion Models](https://github.com/rohitgandikota/erasing)
- [Ablating Concepts](https://www.cs.cmu.edu/~concept-ablation/)
- [Unified Concept Editing](https://github.com/rohitgandikota/unified-concept-editing)
- [MACE](https://arxiv.org/abs/2403.06135)
- [Forget-Me-Not](https://arxiv.org/abs/2303.17591)
- [Ring-A-Bell](https://github.com/chiayi-hsu/Ring-A-Bell)
- [ACE](https://arxiv.org/search/?query=anti+editing+concept+erasure+diffusion&searchtype=all)
- [Editing Massive Concepts](https://arxiv.org/search/?query=editing+massive+concepts+text+to+image+diffusion&searchtype=all)
- [SalUn](https://arxiv.org/search/?query=SalUn+machine+unlearning+diffusion&searchtype=all)
- [ESD](https://arxiv.org/search/?query=ESD+erasing+stable+diffusion&searchtype=all)
- [ConceptPrune](https://arxiv.org/search/?query=ConceptPrune+diffusion&searchtype=all)
- [Responsible Text-to-Image Diffusion](https://arxiv.org/search/?query=Responsible+Text-to-Image+Diffusion&searchtype=all)
- [T2VSafetyBench methods](https://arxiv.org/abs/2409.08615)
- [SafeGen](https://arxiv.org/search/?query=SafeGen+diffusion&searchtype=all)
- [Safety Checker / post-hoc filters](https://arxiv.org/search/?query=diffusion+safety+checker+post-hoc+filter&searchtype=all)
- [NSFW prompt filtering](https://arxiv.org/search/?query=NSFW+prompt+filtering+text+to+image&searchtype=all)
- [Adversarial prompt defense](https://arxiv.org/search/?query=adversarial+prompt+defense+text-to-image+diffusion&searchtype=all)
- [Jailbreak-resistant diffusion](https://arxiv.org/search/?query=jailbreak+text-to-image+diffusion+safety&searchtype=all)
- [Concept restoration after erasure](https://arxiv.org/search/?query=concept+erasure+benign+retention+diffusion&searchtype=all)
- [UniSim](https://openreview.net/forum?id=sFyTZEqmUY)
- [Genie](https://proceedings.mlr.press/v235/bruce24a.html)
- [GAIA-1](https://wayve.ai/thinking/gaia-1/)
- [WorldDreamer](https://arxiv.org/abs/2401.09985)
- [DriveDreamer](https://arxiv.org/search/?query=DriveDreamer&searchtype=all)
- [DriveDreamer-2](https://arxiv.org/search/?query=DriveDreamer-2&searchtype=all)
- [Vista](https://arxiv.org/search/?query=Vista+world+model+video+generation&searchtype=all)
- [Pandora](https://arxiv.org/search/?query=Pandora+world+model+video+generation&searchtype=all)
- [Cosmos World Foundation Models](https://arxiv.org/search/?query=Cosmos+world+foundation+models&searchtype=all)
- [HunyuanWorld / Hunyuan World](https://arxiv.org/search/?query=Hunyuan+World+world+model&searchtype=all)
- [World-consistent Video Diffusion](https://arxiv.org/search/?query=world+consistent+video+diffusion&searchtype=all)
- [Physics-guided Diffusion](https://arxiv.org/search/?query=physics-guided+diffusion+generation&searchtype=all)
- [Simulator-guided Diffusion](https://arxiv.org/search/?query=simulator-guided+diffusion+generation&searchtype=all)
- [Verifier-guided Generation](https://arxiv.org/search/?query=verifier-guided+diffusion+generation&searchtype=all)
- [Causal Video Generation](https://arxiv.org/search/?query=causal+video+generation+diffusion&searchtype=all)
- [Object-state-change Generation](https://arxiv.org/search/?query=object+state+change+text-to-video+generation&searchtype=all)
- [Embodied Diffusion World Models](https://arxiv.org/search/?query=embodied+world+model+diffusion&searchtype=all)

### Benchmarks & Evaluators

- [Pick-a-Pic / PickScore](https://github.com/yuvalkirstain/PickScore)
- [ImageReward](https://github.com/zai-org/ImageReward)
- [HPSv2](https://github.com/tgxs002/HPSv2)
- [HPSv3](https://github.com/MizzenAI/HPSv3)
- [VisionReward](https://github.com/zai-org/VisionReward)
- [MPS evaluation](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Learning_Multi-Dimensional_Human_Preference_for_Text-to-Image_Generation_CVPR_2024_paper.html)
- [Aesthetic score models](https://arxiv.org/search/?query=aesthetic+score+text-to-image+diffusion&searchtype=all)
- [LAION aesthetic predictor](https://laion.ai/blog/laion-aesthetics/)
- [Six-CD](https://github.com/Artanisax/Six-CD)
- [I2P](https://arxiv.org/search/?query=I2P+inappropriate+image+prompts&searchtype=all)
- [Unsafe Diffusion benchmark](https://arxiv.org/search/?query=unsafe+diffusion+benchmark&searchtype=all)
- [T2VSafetyBench](https://arxiv.org/abs/2409.08615)
- [Concept removal benchmarks](https://arxiv.org/search/?query=concept+removal+benchmark+diffusion&searchtype=all)
- [Benign retention benchmarks](https://arxiv.org/search/?query=benign+retention+concept+erasure+diffusion&searchtype=all)
- [Red-teaming prompts](https://arxiv.org/search/?query=red+teaming+text-to-image+diffusion+prompts&searchtype=all)
- [PhyBench](https://github.com/OpenGVLab/PhyBench)
- [VideoPhy](https://github.com/Hritikbansal/videophy)
- [PhyCoBench](https://github.com/Jeckinchen/PhyCoBench)
- [PhyGenBench](https://github.com/OpenGVLab/PhyGenBench)
- [VideoPhy-2](https://videophy2.github.io/)
- [T2VPhysBench](https://arxiv.org/search/?query=T2VPhysBench&searchtype=all)
- [T2VWorldBench](https://arxiv.org/search/?query=T2VWorldBench&searchtype=all)
- [Physics-IQ](https://github.com/google-deepmind/physics-IQ-benchmark)
- [PhyWorldBench](https://github.com/g-jing/phy-world-bench)
- [VideoVerse](https://github.com/Zeqing-Wang/VideoVerse)
- [PhyEduVideo](https://github.com/meghamariamkm/PhyEduVideo)
- [PhyWorld](https://proceedings.mlr.press/v267/kang25g.html)
- [OSCBench](https://arxiv.org/search/?query=OSCBench+Object+State+Change+Text-to-Video&searchtype=all)
- [Morpheus](https://arxiv.org/search/?query=Morpheus+physical+reasoning+video+generative+models&searchtype=all)
- [World-model Video Evaluation](https://arxiv.org/search/?query=world+model+evaluation+video+generation+benchmark&searchtype=all)

### Datasets & Data Resources

- [Pick-a-Pic dataset](https://github.com/yuvalkirstain/PickScore)
- [ImageRewardDB](https://github.com/zai-org/ImageReward)
- [HPD / HPSv2 data](https://github.com/tgxs002/HPSv2)
- [HPDv3 / HPSv3 data](https://github.com/MizzenAI/HPSv3)
- [MPS preference data](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Learning_Multi-Dimensional_Human_Preference_for_Text-to-Image_Generation_CVPR_2024_paper.html)
- [LAION-Aesthetics](https://laion.ai/blog/laion-aesthetics/)
- [AVA Aesthetics](https://arxiv.org/search/?query=AVA+dataset+aesthetics&searchtype=all)
- [I2P prompts](https://arxiv.org/search/?query=I2P+inappropriate+image+prompts&searchtype=all)
- [NSFW prompt resources](https://arxiv.org/search/?query=NSFW+prompt+dataset+text+to+image&searchtype=all)
- [Concept erasure prompt sets](https://arxiv.org/search/?query=concept+erasure+prompt+set+diffusion&searchtype=all)
- [Physical commonsense prompts](https://arxiv.org/search/?query=physical+commonsense+prompts+text+to+image&searchtype=all)
- [Video physical prompts](https://arxiv.org/search/?query=physical+commonsense+prompts+text+to+video&searchtype=all)
- [Driving world-model datasets](https://arxiv.org/search/?query=driving+world+model+dataset+video+generation&searchtype=all)
- [Ego4D](https://ego4d-data.org/)
- [Something-Something V2](https://developer.qualcomm.com/software/ai-datasets/something-something)
- [CLEVRER](https://clevrer.csail.mit.edu/)
- [PHYRE](https://phyre.ai/)
- [IntPhys](https://arxiv.org/search/?query=IntPhys+physical+reasoning+dataset&searchtype=all)
- [CLEVR](https://cs.stanford.edu/people/jcjohns/clevr/)
- [Kubric](https://github.com/google-research/kubric)

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
