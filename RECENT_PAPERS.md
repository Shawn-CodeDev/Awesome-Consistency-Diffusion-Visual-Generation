# Recent papers · 2025–2026

<a id="recent-literature"></a>
## Recent literature · 2025–2026

**168 distinct papers · 113 first posted in 2026 · 55 first posted in 2025**<br>
Research snapshot: **2026-11-05**. Dates below are first arXiv submission dates, not conference publication dates.

[JSON](resources/recent_papers.json) · [CSV](resources/recent_papers.csv) · [BibTeX, abbreviated authors](resources/recent_papers.bib) · [Evidence register](docs/recent-papers.md#evidence-register) · [Scope and limitations](docs/research-notes.md)

> **Reading note.** Titles, dates and short summaries were checked against original arXiv records or their indexed abstracts. Conference status and empirical results were not comprehensively audited. The three-relation assignments are editorial annotations under this survey's taxonomy. A method and its associated benchmark are counted once when they share one paper.

| Primary relation | Papers in this update | Browse |
|:--|--:|:--|
| **External** | 50 | [External consistency](#recent-external) |
| **Internal** | 66 | [Internal consistency](#recent-internal) |
| **Normative** | 52 | [Normative consistency](#recent-normative) |

Within each topic, the most recently posted papers appear first. **Paper titles link to the original arXiv record**; optional code/project links are author-provided discovery links, not a deployment or availability guarantee.

<a id="recent-external"></a>
### 01 · External consistency

#### Image editing and in-context generation

| First posted | Paper and resources | Consistency focus |
|:--|:--|:--|
| 2026-10-18 | **[MT Forcing](https://arxiv.org/abs/2610.25404)**<br><sub>Method · Image · also Internal</sub> | Combines single-turn distribution-matching supervision of self-rollouts with teacher-forcing guidance to reduce quality drift and preserve content across editing turns. |
| 2026-10-17 | **[LayerEditor](https://arxiv.org/abs/2610.24738)**<br><sub>Method + Dataset + Benchmark · Image · also Internal</sub> | Couples instruction editing with ordered RGBA-layer generation and compositional distillation to preserve editing fidelity and enable localized reusable layers. |
| 2026-10-15 | **[ACEdit](https://arxiv.org/abs/2610.22328)**<br><sub>Method · Image · also Internal</sub><br>[Project](https://saradorfman1.github.io/ACEdit/) | Trains on self-generated edit trajectories while anchoring a distillation teacher to the clean source and cumulative instructions to reduce cross-turn drift. |
| 2026-10-08 | **[VibeEdit](https://arxiv.org/abs/2610.12229)**<br><sub>Method + Dataset + Benchmark · Image · also Normative</sub><br>[Project](https://zhaojingjing713.github.io/VibeEdit/) | Separately conditions on source images and spatial canvas instructions, with region-weighted training and rubric-guided rewards for target selection and unedited-region preservation. |
| 2026-10-05 | **[ARRO](https://arxiv.org/abs/2610.06021)**<br><sub>Method · Image · also Normative</sub><br>[Code](https://github.com/Showwwwwwwww/ARRO) | Uses an agentic vision-language reward audit of missed requests and unintended changes to optimize source preservation without per-instruction human labels. |
| 2026-09-09 | **[Overpainting](https://arxiv.org/abs/2609.10811)**<br><sub>Method · Image · also Internal</sub><br>[Project](https://overpainting.github.io/) | Uses trimaps and joint-attention adaptation to distinguish required, optional and forbidden edit regions while preserving source context. |
| 2026-08-30 | **[Discrete Diffusion Bridges](https://arxiv.org/abs/2608.29997)**<br><sub>Method · Image · also Internal</sub><br>[Code](https://github.com/HKU-HealthAI/DDB) | Uses source-anchored corruption and an information-guided schedule to balance semantic editing with structural preservation in discrete diffusion. |
| 2026-08-18 | **[EditBridge](https://arxiv.org/abs/2608.18063)**<br><sub>Method · Image · also Internal</sub><br>[Code](https://github.com/songyangyifei/editbridge) · [Project](https://editbridge.github.io/) | Refines low-resolution edits through a source-conditioned diffusion bridge and correspondence-guided sparse attention to preserve authentic high-resolution details. |
| 2026-06-10 | **[AnchorEdit](https://arxiv.org/abs/2606.11751)**<br><sub>Method + Benchmark · Image · also Internal</sub><br>[Code](https://github.com/xuhang07/AnchorEdit) | Uses autoregressive diffusion, self-rollout training and persistent source memory to reduce identity drift and accumulated errors across editing turns. |
| 2026-05-16 | **[Edit-GRPO](https://arxiv.org/abs/2605.16951)**<br><sub>Method · Image · also Normative</sub> | Decouples region-specific editing and preservation rewards to reduce unintended changes outside target regions during diffusion-editor post-training. |
| 2026-02-15 | **[UniRef-Image-Edit](https://arxiv.org/abs/2602.14186)**<br><sub>Method · Image · also Internal/Normative</sub> | Serializes reference latents under a shared pixel budget and applies multi-source policy optimization to reconcile cross-reference constraints during image editing. |
| 2026-01-09 | **[Generalized multi-image editing](https://arxiv.org/abs/2601.05572)**<br><sub>Method + Benchmark · Image · also Internal</sub> | Disambiguates multiple input images through latent separators and image-index encoding; evaluates cross-image editing integration. |
| 2025-11-25 | **[ImageCritic](https://arxiv.org/abs/2511.20614)**<br><sub>Method + Dataset · Image · also Internal</sub><br>[Code](https://github.com/HVision-NKU/ImageCritic) · [Project](https://ouyangziheng.github.io/ImageCritic-Page/) | Uses reference-guided post-editing, a detail encoder and attention-alignment supervision to correct fine-grained subject inconsistencies in generated images. |
| 2025-10-28 | **[GRAG](https://arxiv.org/abs/2510.24657)**<br><sub>Method · Image · also Internal</sub><br>[Code](https://github.com/little-misfit/GRAG-Image-Editing) · [Project](https://little-misfit.github.io/GRAG-Image-Editing/) | Reweights content-specific attention signals relative to layer-dependent biases to balance source-image fidelity and instruction strength without fine-tuning. |
| 2025-06-23 | **[OmniGen2](https://arxiv.org/abs/2506.18871)**<br><sub>Method + Benchmark · Image · also Internal</sub><br>[Code](https://github.com/VectorSpaceLab/OmniGen2) · [Project](https://vectorspacelab.github.io/OmniGen2) | Unifies generation, editing and in-context tasks; introduces OmniContext to evaluate reference-conditioned subject consistency. |
| 2025-06-17 | **[FLUX.1 Kontext](https://arxiv.org/abs/2506.15742)**<br><sub>Method + Benchmark · Image · also Internal</sub> | Uses joint text-image context for generation and iterative editing; KontextBench separates local edits, reference consistency and text editing. |
| 2025-06-03 | **[UniWorld](https://arxiv.org/abs/2506.03147)**<br><sub>Method · Image · also Internal</sub> | Uses high-resolution semantic representations for unified perception, generation and image manipulation. |
| 2025-05-20 | **[BAGEL](https://arxiv.org/abs/2505.14683)**<br><sub>Method · Image / Video · also Internal</sub><br>[Project](https://bagel-ai.org/) | Unified multimodal pretraining supports image manipulation and future-frame prediction; relevant as a backbone rather than a dedicated consistency guarantee. |
| 2025-04-29 | **[IC-Edit](https://arxiv.org/abs/2504.20690)**<br><sub>Method · Image · also Internal</sub><br>[Project](https://river-zhang.github.io/ICEdit-gh-pages/) | Uses in-context diffusion-transformer generation, lightweight adaptation and early candidate filtering for instruction-guided editing. |
| 2025-04-24 | **[Step1X-Edit](https://arxiv.org/abs/2504.17761)**<br><sub>Method + Benchmark · Image · also Internal</sub> | Combines multimodal instruction understanding with diffusion editing and introduces GEdit-Bench for real-user editing requests. |

[Back to recent-literature navigation](#recent-literature)

#### Compositionality and spatial grounding

| First posted | Paper and resources | Consistency focus |
|:--|:--|:--|
| 2026-10-31 | **[ODC](https://arxiv.org/abs/2611.00819)**<br><sub>Method · Image</sub> | Diagnoses prompt-image drift from an initial sample and refines text conditioning through orthogonal correction for a second generation pass. |
| 2026-05-27 | **[BiDPO / BiComp](https://arxiv.org/abs/2605.28615)**<br><sub>Method + Dataset · Image · also Normative</sub> | Combines image-text preference optimization, compositional preference data and region-level guidance for prompt fidelity. |
| 2026-03-23 | **[SpatialReward / SpatRelBench](https://arxiv.org/abs/2603.22228)**<br><sub>Evaluator + Benchmark · Image · also Normative</sub> | Grounds spatial reward judgments in decomposed prompts and detected objects; introduces SpatRelBench for fine-grained spatial evaluation. |
| 2026-03-06 | **[StruVis](https://arxiv.org/abs/2603.06032)**<br><sub>Method · Image</sub> | Uses structured visual representations as intermediate reasoning states to improve prompt interpretation before image generation. |
| 2026-01-21 | **[Iterative refinement](https://arxiv.org/abs/2601.15286)**<br><sub>Method · Image</sub><br>[Project](https://iterative-img-gen.github.io/) | Uses a vision-language critic to guide sequential corrections of objects, attributes and relations during test-time generation. |

[Back to recent-literature navigation](#recent-literature)

#### Typography and text rendering

| First posted | Paper and resources | Consistency focus |
|:--|:--|:--|
| 2026-05-19 | **[TextAlign](https://arxiv.org/abs/2605.19320)**<br><sub>Method · Image · also Normative</sub> | Decomposes rendering defects into global, word and glyph levels to supply hierarchical rewards for preference alignment. |
| 2026-03-07 | **[TIQA / ANTIQA](https://arxiv.org/abs/2603.07119)**<br><sub>Evaluator + Dataset · Image · also Normative</sub> | Evaluates perceptual quality of rendered text with human-labeled crops and images rather than relying only on OCR correctness. |
| 2026-02-24 | **[TextPecker](https://arxiv.org/abs/2602.20903)**<br><sub>Method + Dataset · Image · also Normative</sub> | Uses character-level structural anomaly supervision to make text-rendering rewards sensitive to malformed glyphs and distortions. |
| 2026-01-02 | **[FreeText](https://arxiv.org/abs/2601.00535)**<br><sub>Method · Image</sub> | Separates text-region localization from glyph injection to improve visual text rendering without retraining the generator. |
| 2025-08-04 | **[Qwen-Image](https://arxiv.org/abs/2508.02324)**<br><sub>Method · Image · also Internal</sub> | Combines multilingual text-rendering training with semantic and reconstructive image encodings for editing fidelity. |

[Back to recent-literature navigation](#recent-literature)

#### Structural and camera control

| First posted | Paper and resources | Consistency focus |
|:--|:--|:--|
| 2026-10-19 | **[Mise-en-Video](https://arxiv.org/abs/2610.26801)**<br><sub>Method + Dataset · Video · also Internal</sub> | Combines per-shot 3D layout guidance with hierarchical attention to jointly support controllable staging and cross-shot narrative consistency. |
| 2026-07-06 | **[From Open Loop to Closed Loop](https://arxiv.org/abs/2607.04691)**<br><sub>Method · Image · also Internal</sub><br>[Code](https://github.com/zzdrill/From-Open-Loop-to-Closed-Loop) | Uses test-time feedback and a modified PID controller to refine latent control signals for reference fidelity in identity-, pose- and depth-conditioned generation. |
| 2026-03-30 | **[MMFace-DiT](https://arxiv.org/abs/2603.29029)**<br><sub>Method · Image</sub><br>[Project](https://vcbsl.github.io/MMFace-DiT/) | Fuses semantic text and spatial mask or sketch conditions within a dual-stream diffusion transformer for controllable face synthesis. |
| 2025-12-15 | **[Beyond the Visible](https://arxiv.org/abs/2512.13392)**<br><sub>Method · Video · also Internal</sub><br>[Project](https://anranqi.github.io/beyondvisible.github.io/) | Separates articulated motion from appearance editing to control newly revealed regions in image-to-video generation. |
| 2025-03-13 | **[CameraCtrl II](https://arxiv.org/abs/2503.10592)**<br><sub>Method · Video · also Internal</sub> | Extends camera-controlled video generation toward wider scene exploration while preserving dynamic content and inter-clip continuity. |
| 2025-03-11 | **[OminiControl2](https://arxiv.org/abs/2503.08280)**<br><sub>Method · Image · also Internal</sub> | Compresses condition tokens and reuses conditional features across denoising steps for efficient multi-condition image generation. |
| 2025-01-07 | **[Diffusion as Shader](https://arxiv.org/abs/2501.03847)**<br><sub>Method · Video / 3D · also Internal</sub><br>[Code](https://github.com/IGL-HKUST/DiffusionAsShader) · [Project](https://igl-hkust.github.io/das/) | Uses 3D tracking videos as a common control interface for camera, motion and object manipulation with temporal correspondence. |

[Back to recent-literature navigation](#recent-literature)

#### Reference-conditioned video generation

| First posted | Paper and resources | Consistency focus |
|:--|:--|:--|
| 2026-10-01 | **[MemComposer](https://arxiv.org/abs/2610.01884)**<br><sub>Method · Video · also Internal</sub> | MemComposer builds entity-centric memory from user footage and retrieves shot-specific references to ground generated B-roll in collection identities, settings and style. |

[Back to recent-literature navigation](#recent-literature)

#### Temporally consistent video editing

| First posted | Paper and resources | Consistency focus |
|:--|:--|:--|
| 2026-11-02 | **[MoviEdit / MoviEdit-Bench](https://arxiv.org/abs/2611.02737)**<br><sub>Method + Dataset + Benchmark · Video · also Internal</sub><br>[Project](https://multi-shot-edit.github.io/) | Builds a globally coherent compressed editing draft before autoregressive refinement, with paired multi-shot editing data and a dedicated evaluation benchmark. |
| 2026-08-04 | **[JoyAI-Video-Edit](https://arxiv.org/abs/2608.03974)**<br><sub>Method · Video · also Internal</sub><br>[Code](https://github.com/jd-opensource/JoyAI-Video-Edit) | Combines source-anchored distillation and long-horizon autoregressive training to preserve source fidelity in streaming video editing. |
| 2026-06-07 | **[Temporal-structure-preserving editing](https://arxiv.org/abs/2606.08780)**<br><sub>Method · Video · also Internal</sub> | Preserves source-video temporal organization using semantic clip partitioning, anchor frames and clip-adaptive token merging. |
| 2026-02-02 | **[MLV-Edit](https://arxiv.org/abs/2602.02123)**<br><sub>Method · Video · also Internal</sub> | Uses flow blending at segment boundaries and attention anchors to reduce flicker and structural drift in minute-length editing. |
| 2026-01-22 | **[Memory-V2V](https://arxiv.org/abs/2601.16296)**<br><sub>Method · Video · also Internal</sub><br>[Project](https://dohunlee1.github.io/MemoryV2V) | Retrieves earlier edits from external memory and integrates them through relevance-aware tokenization and compression to preserve content across editing turns. |

[Back to recent-literature navigation](#recent-literature)

#### Editing and reasoning evaluation

| First posted | Paper and resources | Consistency focus |
|:--|:--|:--|
| 2026-10-29 | **[EditAgent](https://arxiv.org/abs/2610.39664)**<br><sub>Method + Benchmark + Evaluator · Image · also Internal</sub> | Routes edits across general and specialized tools and uses verification records to compare parallel candidates for complex instruction following and source preservation. |
| 2026-07-08 | **[ReSpec / OCCUR-Bench](https://arxiv.org/abs/2607.07051)**<br><sub>Method + Benchmark · Image · also Internal</sub><br>[Code](https://github.com/anonymous745961852-cloud/implicit-preservation-editing) | Tests restoration of temporarily occluded but unchanged content and uses historical references with restoration-aware instructions to preserve editing history. |
| 2025-08-24 | **[T2I-ReasonBench](https://arxiv.org/abs/2508.17472)**<br><sub>Benchmark · Image · also Normative</sub> | Separates reasoning accuracy from image quality across idioms, textual design, entity reasoning and scientific reasoning. |
| 2025-06-09 | **[OneIG-Bench](https://arxiv.org/abs/2506.07977)**<br><sub>Benchmark · Image · also Normative</sub> | Separates prompt alignment, rendered text, reasoning, style and diversity into selectable image-generation evaluation dimensions. |
| 2025-06-02 | **[TIIF-Bench](https://arxiv.org/abs/2506.02161)**<br><sub>Benchmark · Image</sub><br>[Project](https://a113n-w3i.github.io/TIIF_Bench/) | Tests fine-grained instruction following across prompt complexity and length, including text rendering and style control. |
| 2025-05-22 | **[KRIS-Bench](https://arxiv.org/abs/2505.16707)**<br><sub>Benchmark · Image · also Normative</sub> | Organizes knowledge-based editing around factual, conceptual and procedural knowledge, with a knowledge-plausibility evaluation protocol. |
| 2025-04-03 | **[RISEBench](https://arxiv.org/abs/2504.02826)**<br><sub>Benchmark · Image · also Internal/Normative</sub><br>[Code](https://github.com/PhoenixZ810/RISEBench) | Evaluates temporal, causal, spatial and logical editing instructions alongside appearance preservation and visual plausibility. |

[Back to recent-literature navigation](#recent-literature)

<a id="recent-internal"></a>
### 02 · Internal consistency

#### Subject and identity preservation

| First posted | Paper and resources | Consistency focus |
|:--|:--|:--|
| 2026-08-20 | **[WithEveryone](https://arxiv.org/abs/2608.20336)**<br><sub>Method + Benchmark · Image · also External</sub><br>[Project](https://doby-xu.github.io/WithEveryone/) | Uses addressed identity tokens, explicit identity-layout planning and region-grounded identity supervision to reduce identity mixing in group generation. |
| 2026-07-27 | **[Diff-ID](https://arxiv.org/abs/2607.25078)**<br><sub>Method + Dataset · Image · also External</sub> | Combines ArcFace and CLIP conditioning with timestep-weighted identity supervision, evaluating facial identity fidelity jointly with perceptual realism. |
| 2026-03-10 | **[ID-LoRA](https://arxiv.org/abs/2603.10256)**<br><sub>Method · Video / Audio · also External</sub> | Jointly personalizes visual appearance and voice using reference conditioning, separated temporal positions and identity guidance. |
| 2026-02-15 | **[SpatialID](https://arxiv.org/abs/2602.13994)**<br><sub>Method · Image · also External</sub> | Restricts identity injection spatially and schedules it over denoising to reduce interference with background and prompt-driven content. |
| 2025-08-05 | **[MoCA / CelebIPVid](https://arxiv.org/abs/2508.03034)**<br><sub>Method + Dataset · Video · also External</sub> | Uses temporally pooled identity features, cross-attention experts and video perceptual supervision to preserve facial identity across frames. |
| 2025-06-30 | **[Proteus-ID / Proteus-Bench](https://arxiv.org/abs/2506.23729)**<br><sub>Method + Dataset + Benchmark · Video · also External</sub><br>[Project](https://grenoble-zhang.github.io/Proteus-ID/) | Combines multimodal identity fusion, time-aware identity injection and motion-weighted learning to balance identity fidelity with natural motion. |
| 2025-06-11 | **[Asymmetry Zigzag Sampling](https://arxiv.org/abs/2506.09612)**<br><sub>Method · Image · also External</sub><br>[Code](https://github.com/Mingxiao-Li/Asymmetry-Zigzag-StoryDiffusion) | Alternates asymmetric prompts and shared visual cues during training-free sampling to preserve subjects across story panels. |
| 2025-04-23 | **[DreamO](https://arxiv.org/abs/2504.16915)**<br><sub>Method · Image · also External</sub> | Routes reference features and task conditions in a unified diffusion transformer for identity, subject, style and background customization. |
| 2025-04-02 | **[UNO](https://arxiv.org/abs/2504.02160)**<br><sub>Method · Image · also External</sub> | Builds consistent multi-subject training pairs and uses multi-image conditioning to preserve subjects under compositional control. |

[Back to recent-literature navigation](#recent-literature)

#### Subject and identity evaluation

| First posted | Paper and resources | Consistency focus |
|:--|:--|:--|
| 2026-10-01 | **[DynSC-Eval](https://arxiv.org/abs/2610.01052)**<br><sub>Evaluator + Method · Video · also Normative</sub> | DynSC-Eval tracks changing subject sets and diagnoses local continuity and global identity; its signals also guide DiffusionNFT post-training. |
| 2026-09-03 | **[Persistent identity benchmark](https://arxiv.org/abs/2609.04151)**<br><sub>Benchmark + Evaluator · Image · also External</sub> | Compares context-based, parameter-based and persistent identity representations across generation, iterative editing, restoration and multi-subject composition. |
| 2026-06-14 | **[CogCanvas](https://arxiv.org/abs/2606.15867)**<br><sub>Benchmark · Image · also External</sub> | Jointly tests multi-person identity, per-subject object and fashion binding, background fidelity and interaction plausibility. |
| 2026-05-30 | **[MBench](https://arxiv.org/abs/2606.00793)**<br><sub>Benchmark + Evaluator · Video · also Normative</sub><br>[Code](https://github.com/study-overflow/MBench) · [Project](https://peanutup.github.io/MBench-project/) | Measures long-term entity, environment and causal memory using real-video conditions, rule-based metrics and VLM evaluation across twelve dimensions. |

[Back to recent-literature navigation](#recent-literature)

#### Multi-view and geometric consistency

| First posted | Paper and resources | Consistency focus |
|:--|:--|:--|
| 2026-10-26 | **[OmniShowcase](https://arxiv.org/abs/2610.35684)**<br><sub>Method + Dataset + Benchmark · Video / 3D · also External</sub><br>[Code](https://github.com/justin4ai/OmniShowcase) · [Project](https://justin4ai.github.io/OmniShowcase/) | Conditions video diffusion on reconstructed surface-normal turntables and geometry-consistent training videos; ShowcaseBench evaluates identity and 3D consistency across camera paths. |
| 2026-10-23 | **[CompMVR](https://arxiv.org/abs/2610.32800)**<br><sub>Method + Dataset · Image / 3D · also External</sub> | Jointly restores compressed multiview observations with compression priors and cross-view correspondences to preserve geometry for reconstruction and novel-view synthesis. |
| 2026-10-08 | **[WorldAlign](https://arxiv.org/abs/2610.12382)**<br><sub>Method + Evaluator · Video · also Normative</sub><br>[Project](https://worldalign.github.io/) | Separates static-region geometric rewards from dynamic-subject checklist rewards to improve 4D coherence without favoring nearly motionless videos. |
| 2026-09-09 | **[StreetDiff / Street360](https://arxiv.org/abs/2609.09890)**<br><sub>Method + Dataset · Image / 3D · also External</sub> | Uses panorama-perspective alignment constraints during denoising to preserve urban-scene layout across rotated views. |
| 2026-07-19 | **[HarmoHOI](https://arxiv.org/abs/2607.17097)**<br><sub>Method · Video / 3D · also Normative</sub><br>[Project](https://droliven.github.io/HarmoHOI_project) | Jointly models synchronized interaction videos and globally aligned 3D point tracks to couple appearance, motion and multi-view geometry. |
| 2026-07-06 | **[MV-Forcing](https://arxiv.org/abs/2607.05376)**<br><sub>Method · Video / 3D</sub><br>[Project](https://galfiebelman.github.io/mv-forcing/) | Bridges view-wise and temporal autoregression with reconstructed 4D geometry and spatio-temporal self-forcing. |
| 2026-06-09 | **[HarmoView](https://arxiv.org/abs/2606.10839)**<br><sub>Method · Video / 3D · also External</sub> | Combines appearance anchors, proxy tokens and identity-separated positional encoding with a progressive multi-view training curriculum. |
| 2026-05-19 | **[SEGS](https://arxiv.org/abs/2605.19876)**<br><sub>Method · 3D</sub> | Injects structural-energy gradients derived from diffusion features to mitigate inconsistent geometry and Janus artifacts across views. |
| 2026-04-13 | **[SyncFix](https://arxiv.org/abs/2604.11797)**<br><sub>Method · Image / 3D · also External</sub><br>[Project](https://syncfix.github.io/) | Learns a joint latent bridge across reconstructed views to synchronize refinement and reduce semantic and geometric inconsistency, with optional sparse references. |
| 2026-03-17 | **[MosaicMem](https://arxiv.org/abs/2603.17117)**<br><sub>Method · Video / 3D · also External</sub><br>[Project](https://mosaicmem.github.io/) | Lifts image patches into 3D for targeted retrieval and composes aligned observations in queried views while permitting dynamic scene changes. |
| 2026-02-10 | **[ConsID-Gen / ConsIDVid](https://arxiv.org/abs/2602.10113)**<br><sub>Method + Benchmark + Dataset · Video / 3D · also External</sub><br>[Project](https://myangwu.github.io/ConsID-Gen) | Augments image-to-video conditioning with auxiliary views and evaluates identity and geometry using the ConsIDVid data and benchmark. |
| 2026-01-25 | **[MV-S2V](https://arxiv.org/abs/2601.17756)**<br><sub>Method · Video / 3D · also External</sub><br>[Project](https://szy-young.github.io/mv-s2v) | Uses multiple reference views and temporally shifted positional encoding to separate subject identity from reference viewpoint. |
| 2025-12-16 | **[ViewMask-1-to-3](https://arxiv.org/abs/2512.14099)**<br><sub>Method · Image / 3D · also External</sub> | Models multiple views as visual-token sequences and uses joint masked-token diffusion to encourage cross-view agreement without explicit geometric priors. |
| 2025-11-27 | **[3DC-MVE](https://arxiv.org/abs/2511.22228)**<br><sub>Method · Image / 3D · also External</sub><br>[Project](https://3d-consistent-editing.github.io/) | Guides diffusion or flow editing with a correspondence-based consistency loss to preserve geometric and photometric agreement across scene views. |
| 2025-10-16 | **[Coupled Diffusion Sampling](https://arxiv.org/abs/2510.14981)**<br><sub>Method · Image / 3D · also External</sub><br>[Project](https://coupled-diffusion.github.io/) | Couples trajectories from pretrained image-editing and multiview distributions to regularize cross-view edits without explicit 3D optimization. |
| 2025-10-15 | **[MVCustom](https://arxiv.org/abs/2510.13702)**<br><sub>Method · Image / 3D · also External</sub><br>[Project](https://minjung-s.github.io/mvcustom) | Combines subject-specific feature fields, depth-aware rendering and latent completion to jointly control camera pose, appearance customization and cross-view geometry. |
| 2025-08-22 | **[MV-RAG](https://arxiv.org/abs/2508.16577)**<br><sub>Method + Benchmark · Image / 3D · also External</sub><br>[Code](https://github.com/yosefdayani/MV-RAG) · [Project](https://yosefdayani.github.io/MV-RAG/) | Conditions multiview diffusion on retrieved images and trains held-out-view prediction to improve 3D consistency and prompt fidelity for rare concepts. |
| 2025-06-04 | **[Voyager](https://arxiv.org/abs/2506.04225)**<br><sub>Method · Video / 3D · also External</sub> | Jointly generates aligned RGB and depth while maintaining a culled world cache for camera-controlled, geometrically coherent scene exploration. |

[Back to recent-literature navigation](#recent-literature)

#### Multi-shot narratives and persistent memory

| First posted | Paper and resources | Consistency focus |
|:--|:--|:--|
| 2026-10-12 | **[REEL](https://arxiv.org/abs/2610.16632)**<br><sub>Method + Dataset + Benchmark · Video · also External</sub> | Trains a generator-agnostic visual-memory planner through supervised and multi-shot reinforcement learning; REEL-Bench tests identity persistence and intended state changes. |
| 2026-05-26 | **[ReCA / MSVE-Bench](https://arxiv.org/abs/2605.26525)**<br><sub>Method + Benchmark · Video · also External</sub><br>[Project](https://reca.vmv.re) | Allocates planning and generation context hierarchically to preserve observed state while extending a source clip into multiple shots. |
| 2026-05-19 | **[MSAVBench](https://arxiv.org/abs/2605.20183)**<br><sub>Benchmark · Video / Audio · also External</sub> | Evaluates video, audio, shots and references with adaptive segmentation and tool-grounded evidence for multi-shot audio-video generation. |
| 2026-05-14 | **[EntityBench / EntityMem](https://arxiv.org/abs/2605.15199)**<br><sub>Benchmark + Method · Video · also External</sub><br>[Code](https://github.com/Catherine-R-He/EntityBench/) | Tracks recurring characters, objects and locations across long shot sequences, with fidelity-gated scoring and a persistent entity-memory baseline. |
| 2026-05-12 | **[CausalCine](https://arxiv.org/abs/2605.12496)**<br><sub>Method · Video · also External</sub><br>[Project](https://yihao-meng.github.io/CausalCine/) | Uses content-aware memory routing and causal multi-shot training to support streaming narratives with changing prompts and shot boundaries. |
| 2026-02-14 | **[DCDM](https://arxiv.org/abs/2602.13637)**<br><sub>Method · Video · also External/Normative</sub> | Separates intra-clip semantics, inter-clip camera control and inter-shot element persistence into complementary video-generation components. |
| 2026-01-07 | **[VideoMemory](https://arxiv.org/abs/2601.03655)**<br><sub>Method + Benchmark · Video · also External</sub><br>[Project](https://hit-perfect.github.io/VideoMemory/) | Stores and updates visual-semantic entity states across planned shots to preserve characters, props and backgrounds; evaluates multi-shot persistence. |
| 2025-12-22 | **[StoryMem / ST-Bench](https://arxiv.org/abs/2512.19539)**<br><sub>Method + Benchmark · Video · also External</sub> | Conditions iterative shot synthesis on selected historical keyframes and introduces ST-Bench for long-form storytelling evaluation. |
| 2025-12-02 | **[MultiShotMaster](https://arxiv.org/abs/2512.03041)**<br><sub>Method · Video · also External</sub><br>[Project](https://qinghew.github.io/MultiShotMaster/) | Uses shot-aware and spatiotemporal RoPE variants to preserve narrative order and bind reference identities and scene controls across shots. |
| 2025-10-23 | **[HoloCine](https://arxiv.org/abs/2510.20822)**<br><sub>Method · Video · also External</sub><br>[Project](https://holo-cine.github.io/) | Combines shot-local text conditioning with sparse inter-shot attention for jointly generated, coherent cinematic scenes. |
| 2025-08-15 | **[CineTrans / Cine250K](https://arxiv.org/abs/2508.11484)**<br><sub>Method + Dataset + Evaluator · Video · also External</sub> | Uses shot-boundary-aware attention masks and annotated multi-shot training data to control cinematic transitions while retaining temporal coherence. |
| 2025-06-03 | **[Context as Memory](https://arxiv.org/abs/2506.03141)**<br><sub>Method · Video · also External</sub><br>[Project](https://context-as-memory.github.io/) | Retrieves historical frames by camera field-of-view overlap and directly concatenates them as context to preserve revisited scene content. |
| 2025-04-16 | **[WorldMem](https://arxiv.org/abs/2504.12369)**<br><sub>Method · Video / 3D · also Normative</sub> | Retrieves state-indexed visual memories to reconstruct previously visited scenes across viewpoint and temporal gaps. |
| 2025-03-19 | **[VideoGen-of-Thought](https://arxiv.org/abs/2503.15138)**<br><sub>Method · Video · also External</sub> | Combines storyline planning, identity-aware cross-shot propagation and latent transitions for coherent multi-shot video generation. |

[Back to recent-literature navigation](#recent-literature)

#### Long-horizon video generation

| First posted | Paper and resources | Consistency focus |
|:--|:--|:--|
| 2026-11-01 | **[Learning-to-Memorize](https://arxiv.org/abs/2611.01858)**<br><sub>Method · Video</sub> | Learns frame importance, memory replacement and degradation-aware context handling to retain useful history within a fixed KV-cache budget. |
| 2026-10-31 | **[Commit Forcing](https://arxiv.org/abs/2611.00937)**<br><sub>Method + Analysis · Video</sub> | Separates denoising context from KV-cache committing context and restricts committing to a preceding-block chain to reduce subject and scene drift. |
| 2026-10-13 | **[SMART](https://arxiv.org/abs/2610.19257)**<br><sub>Method · Video · also External</sub><br>[Project](https://eren-cetin.github.io/SMART/) | Uses camera-addressed constant-size slot memory and confidence-conditioned diffusion to recall previously observed scenes when the camera returns. |
| 2026-10-08 | **[Memory Forcing](https://arxiv.org/abs/2610.11756)**<br><sub>Method · Video</sub> | Partitions fixed-capacity memory into sink, archive and working banks, with bank-aware positional encoding to retain intermediate events and returning subjects. |
| 2026-10-05 | **[Keepsake](https://arxiv.org/abs/2610.06588)**<br><sub>Method · Video · also External</sub> | Uses a pose-appearance graph to reassess redundant observations and retain distinctive spatial memories under a fixed capacity without retraining the host generator. |
| 2026-10-01 | **[MosaiChunk](https://arxiv.org/abs/2610.02153)**<br><sub>Method + Benchmark · Video · also External</sub> | Learns a lightweight router over historical spatial-temporal KV entries for fixed-budget memory; RememBench evaluates scene revisits in text- and camera-controlled generation. |
| 2026-07-13 | **[Cycle-World](https://arxiv.org/abs/2607.11836)**<br><sub>Method · Video</sub> | Trains with reverse-prediction cycle consistency and applies a reverse-model latent corrector at inference to suppress accumulated rollout errors. |
| 2026-06-21 | **[Towards Error-Free Long Video Generation](https://arxiv.org/abs/2606.22370)**<br><sub>Method · Video</sub> | Combines intra-clip bidirectional and inter-clip causal attention with constant KV caching and truncation-rectified flow to reduce drift. |
| 2026-06-11 | **[TetherCache](https://arxiv.org/abs/2606.13035)**<br><sub>Method · Video</sub> | Balances relevant and diverse historical frames within a fixed cache, then aligns recalled token statistics to reduce contamination from drifted context. |
| 2026-06-01 | **[LongLive-RAG](https://arxiv.org/abs/2606.02553)**<br><sub>Method · Video</sub><br>[Code](https://github.com/qixinhu11/LongLive-RAG) | Retrieves non-local self-generated latent history with temporal-change-aware embeddings to reduce identity drift caused by sliding-window conditioning. |
| 2026-05-29 | **[SlotMemory](https://arxiv.org/abs/2605.31033)**<br><sub>Method · Video · also External</sub><br>[Project](https://tj12323.github.io/SlotMemory/) | Indexes original transformer KV tokens through reusable semantic slots to preserve recurring entities and support prompt-aware long-range retrieval. |
| 2025-12-16 | **[MemFlow](https://arxiv.org/abs/2512.14699)**<br><sub>Method · Video · also External</sub><br>[Code](https://github.com/KlingAIResearch/MemFlow) · [Project](https://sihuiji.github.io/MemFlow.github.io/) | Updates a bounded memory using prompt-conditioned retrieval and sparsely activates relevant historical tokens for coherent interactive long-video narratives. |
| 2025-12-15 | **[LongVie 2](https://arxiv.org/abs/2512.13604)**<br><sub>Method · Video · also External</sub><br>[Project](https://vchitect.github.io/LongVie2-project/) | Combines dense-sparse controls, degraded-input training and adjacent-clip historical context to retain visual quality and temporal coherence over long rollouts. |
| 2025-12-04 | **[VideoSSM](https://arxiv.org/abs/2512.04519)**<br><sub>Method · Video · also External</sub> | Combines an evolving state-space global memory with local context windows to preserve scene dynamics and reduce motion drift and repetition. |
| 2025-10-02 | **[Self-Forcing++](https://arxiv.org/abs/2510.02283)**<br><sub>Method · Video</sub><br>[Project](https://self-forcing-plus-plus.github.io/) | Supervises sampled segments of self-generated long videos to reduce error accumulation beyond short-teacher training horizons. |
| 2025-09-26 | **[LongLive](https://arxiv.org/abs/2509.22622)**<br><sub>Method · Video · also External</sub> | Combines long-rollout training, prompt-aware cache refresh and frame sinks to preserve consistency during interactive long-video generation. |
| 2025-08-28 | **[Mixture of Contexts](https://arxiv.org/abs/2508.21058)**<br><sub>Method · Video</sub><br>[Project](https://primecai.github.io/moc/) | Learns sparse routing to informative historical chunks while retaining caption and local anchors, supporting identity, action and scene persistence. |
| 2025-08-05 | **[LongVie / LongVGenBench](https://arxiv.org/abs/2508.03694)**<br><sub>Method + Benchmark · Video · also External</sub> | Aligns clip noise and control normalization, combining dense and sparse guidance with degradation-aware training for temporally coherent controlled video. |
| 2025-06-09 | **[Self Forcing](https://arxiv.org/abs/2506.08009)**<br><sub>Method · Video</sub><br>[Project](https://self-forcing.github.io/) | Trains on self-generated context to reduce exposure bias; long extrapolation still requires separate consistency evaluation. |
| 2025-04-17 | **[FramePack](https://arxiv.org/abs/2504.12626)**<br><sub>Method · Video</sub><br>[Code](https://github.com/lllyasviel/FramePack) | Packs frame context by importance and studies endpoint anchors, sampling order and discrete history representations for drift prevention. |
| 2025-02-18 | **[MALT Diffusion](https://arxiv.org/abs/2502.12632)**<br><sub>Method · Video</sub> | Encodes prior video segments in recurrent attention memory and trains segment-level autoregression to limit long-horizon quality degradation. |

[Back to recent-literature navigation](#recent-literature)

<a id="recent-normative"></a>
### 03 · Normative consistency

#### Preference alignment and reward learning

| First posted | Paper and resources | Consistency focus |
|:--|:--|:--|
| 2026-10-12 | **[IsoVRBench / IsoVRM](https://arxiv.org/abs/2610.17234)**<br><sub>Benchmark + Evaluator + Dataset + Method · Video · also External/Internal</sub> | Creates controlled video pairs that isolate one changed property, exposing reward-model blind spots and providing synthetic data for reward and generator training. |
| 2026-10-01 | **[iADD](https://arxiv.org/abs/2610.01789)**<br><sub>Method · Image · also External</sub> | Studies diversity effects of timestep-restricted policy updates and uses incremental Feynman-Kac training to balance reward alignment and diversity. |
| 2026-09-03 | **[DM-Align](https://arxiv.org/abs/2609.04283)**<br><sub>Method · Video · also External</sub> | Combines distribution-matching distillation gradients with preference-guided gradients derived from paired or group-sampled video generations. |
| 2026-07-30 | **[cIPO](https://arxiv.org/abs/2607.28058)**<br><sub>Method · Video · also Internal</sub><br>[Project](https://henglin-liu.github.io/cIPO_vis/) | Derives preferences from real-video reconstruction errors and concentrates updates on high-error temporal segments to reduce flicker and motion artifacts. |
| 2026-07-07 | **[D2PO](https://arxiv.org/abs/2607.06609)**<br><sub>Method · Image</sub> | Optimizes sampler timesteps and guidance weights through dynamic preferences rather than fixed teacher-regression targets. |
| 2026-07-04 | **[Reward Lightning](https://arxiv.org/abs/2607.03960)**<br><sub>Method + Evaluator · Video · also External/Internal</sub><br>[Project](https://reward-lightning.github.io/) | Shares latent representations between reward modeling and adversarial distillation to jointly optimize few-step generation and video preference alignment. |
| 2026-06-25 | **[Qwen-Image-2.0-RL](https://arxiv.org/abs/2606.27608)**<br><sub>Method · Image · also External/Internal</sub> | Uses task-specific rewards, GRPO and on-policy distillation to align image generation and editing while preserving identity. |
| 2026-06-10 | **[SG-PVR](https://arxiv.org/abs/2606.11838)**<br><sub>Evaluator + Method · Video · also External/Internal</sub> | Decomposes prompts into claims and grounds reward reasoning in persistent spatio-temporal scene graphs to evaluate and rerank compositional video alignment. |
| 2026-05-08 | **[Diffusion-APO](https://arxiv.org/abs/2605.07503)**<br><sub>Method · Video · also External</sub> | Aligns preference-training noise with inference trajectories and supports several online and offline video-alignment stages. |
| 2026-03-12 | **[DIAE](https://arxiv.org/abs/2603.11556)**<br><sub>Method + Dataset · Image · also External/Internal</sub> | Uses multimodal aesthetic guidance and weakly paired supervision to improve aesthetics while retaining image content. |
| 2026-02-05 | **[DeDPO](https://arxiv.org/abs/2602.06195)**<br><sub>Method · Image</sub> | Corrects systematic bias in synthetic preference labels to combine limited human feedback with inexpensive AI annotations. |
| 2025-10-19 | **[UniWorld-V2 / Edit-R1](https://arxiv.org/abs/2510.16888)**<br><sub>Method · Image · also External/Internal</sub><br>[Code](https://github.com/PKU-YuanGroup/UniWorld-V2) | Combines DiffusionNFT and multimodal-model feedback for post-training instruction editing, with filtering to reduce scoring noise. |
| 2025-10-14 | **[SRUM](https://arxiv.org/abs/2510.12784)**<br><sub>Method · Image · also External</sub> | Uses a unified model's understanding branch to provide global and object-local feedback for its image-generation branch. |
| 2025-09-19 | **[DiffusionNFT](https://arxiv.org/abs/2509.16117)**<br><sub>Method · Image · also External</sub> | Contrasts positively and negatively rewarded generations in a forward-process objective without requiring reverse-trajectory likelihoods. |
| 2025-05-12 | **[DanceGRPO](https://arxiv.org/abs/2505.07818)**<br><sub>Method · Image / Video · also External/Internal</sub> | Adapts group-relative policy optimization across diffusion and rectified-flow image and video generation tasks. |
| 2025-01-23 | **[VideoReward / VideoAlign](https://arxiv.org/abs/2501.13918)**<br><sub>Method + Evaluator + Dataset · Video · also External/Internal</sub><br>[Project](https://gongyeliu.github.io/videoalign) | Introduces multi-dimensional video preferences and reward modeling, with flow-based preference optimization and inference-time reward guidance. |

[Back to recent-literature navigation](#recent-literature)

#### Safety, erasure and capability retention

| First posted | Paper and resources | Consistency focus |
|:--|:--|:--|
| 2026-10-05 | **[Harmful-content moderation audit](https://arxiv.org/abs/2610.06503)**<br><sub>Evaluation study · Image</sub> | Audits harmful generation and moderation gaps across open image models, with human ratings and comparisons of standard versus community-tuned variants. |
| 2026-10-05 | **[In-generation safety RL](https://arxiv.org/abs/2610.05908)**<br><sub>Method · Image · also External</sub> | Detects emerging unsafe signals during denoising and uses reinforcement learning to steer generation while retaining perceptual quality and prompt fidelity. |
| 2026-10-01 | **[CALM](https://arxiv.org/abs/2610.02300)**<br><sub>Method + Evaluation study · Image · also External</sub> | Analyzes safety coverage versus benign selectivity and applies prompt-local counterfactual corrections instead of removing one global unsafe subspace. |
| 2026-10-01 | **[CEASE](https://arxiv.org/abs/2610.01989)**<br><sub>Method · Image</sub> | CEASE constrains closed-form edits using replacement-token invariance and past-update subspaces to limit interference and preserve unrelated generations during continual concept erasure. |
| 2026-09-30 | **[ShieldCLIP / ViSUv2](https://arxiv.org/abs/2609.39688)**<br><sub>Method + Dataset · Image · also External</sub><br>[Project](https://aimagelab.github.io/ShieldCLIP/) | Uses modality-specific safety labels to redirect unsafe embeddings while anchoring benign representations, including downstream diffusion-image evaluation. |
| 2026-09-23 | **[InGuard / RevGen](https://arxiv.org/abs/2609.27620)**<br><sub>Method + Benchmark · Image · also External</sub> | Combines embedding-level risk grading and steering with intermediate-latent detection; RevGen tests safety and disturbance to benign generations. |
| 2026-09-21 | **[IMPLICIT-Bench](https://arxiv.org/abs/2609.24228)**<br><sub>Benchmark · Image · also External</sub> | Contrasts neutral, stereotypical and counter-stereotypical prompt triplets to separate demographic defaults from explicit instruction following. |
| 2026-09-11 | **[GRACE](https://arxiv.org/abs/2609.12731)**<br><sub>Method · Image</sub> | Combines sensitive-subspace adapters, safe anchors and dynamic gating to reduce undesired concepts while limiting semantic drift. |
| 2026-08-22 | **[GuardPaint](https://arxiv.org/abs/2608.21869)**<br><sub>Method · Image · also External</sub> | Audits intermediate diffusion outputs and selectively inpaints unsafe regions, accepting repairs that improve safety while preserving fidelity and quality. |
| 2026-06-15 | **[REINS](https://arxiv.org/abs/2606.17257)**<br><sub>Method · Video · also External</sub> | Steers intermediate video-transformer hidden states along a learned safety direction to redirect harmful generations without changing model weights. |
| 2026-05-31 | **[SafeGen-Bench](https://arxiv.org/abs/2606.01481)**<br><sub>Benchmark · Video · also External/Internal</sub> | Tests unsafe behaviors that can emerge from jointly benign-looking image and text inputs in conditional video generation. |
| 2026-05-27 | **[OCE](https://arxiv.org/abs/2605.28902)**<br><sub>Method · Image</sub><br>[Code](https://github.com/HansSunY/OCE) | Uses multiplicative orthogonal parameter transformations to separate concept removal from broader generative-capability preservation. |
| 2026-05-03 | **[TrajShield](https://arxiv.org/abs/2605.01761)**<br><sub>Method · Video · also External/Internal</sub> | Uses trajectory-level risk analysis and targeted prompt rewriting to address unsafe intent and temporally emerging video risks. |
| 2026-04-22 | **[Target-based fairness prompting](https://arxiv.org/abs/2604.21036)**<br><sub>Method · Image · also External</sub> | Audits generated demographic representation against explicitly declared target distributions rather than assuming one universal fairness target. |
| 2026-04-06 | **[Erasure or Erosion?](https://arxiv.org/abs/2604.04575)**<br><sub>Evaluation study · Image · also External</sub> | Audits how concept unlearning affects attribute binding, spatial relations and counting rather than checking erasure success alone. |
| 2025-10-31 | **[S-GRACE](https://arxiv.org/abs/2510.27285)**<br><sub>Method · Image</sub><br>[Code](https://github.com/Qhong-522/S-GRACE) | Uses semantic guidance during adversarial erasure training to improve concept coverage while limiting collateral changes. |
| 2025-09-25 | **[DyME / ErasureBench-H](https://arxiv.org/abs/2509.21433)**<br><sub>Method + Benchmark · Image</sub> | Composes concept-specific erasure adapters with orthogonality constraints and evaluates interference on a hierarchical erasure benchmark. |

[Back to recent-literature navigation](#recent-literature)

#### Physics-aware generation

| First posted | Paper and resources | Consistency focus |
|:--|:--|:--|
| 2026-10-07 | **[RobotAPO / AgiBot-PhysPref](https://arxiv.org/abs/2610.09454)**<br><sub>Method + Dataset · Video · also External/Internal</sub> | Uses condition-matched physics preferences and adversarial denoising-space counterfactuals to penalize localized interaction failures in manipulation videos. |
| 2026-10-01 | **[HiPhy / MultiPhyBench](https://arxiv.org/abs/2610.02197)**<br><sub>Method + Dataset + Benchmark · Video · also External/Internal</sub><br>[Project](https://hiphy-video.github.io/) | Combines principle-level temporal rewards with scene-level physical and semantic alignment; introduces multi-principle prompts and MultiPhyBench. |
| 2026-09-01 | **[Chain-of-events physical conditioning](https://arxiv.org/abs/2609.00656)**<br><sub>Method · Video · also External/Internal</sub> | Represents physical evolution as event chains and uses routed keyframe conditioning with physics-informed semantic guidance. |
| 2026-04-03 | **[MMPhysVideo](https://arxiv.org/abs/2604.02817)**<br><sub>Method · Video · also Internal</sub> | Jointly models appearance, geometry and trajectory cues, then distills learned physical priors into an efficient video generator. |
| 2026-03-19 | **[PhysVideo / PhysMV](https://arxiv.org/abs/2603.18639)**<br><sub>Method + Dataset · Video / 3D · also Internal</sub> | Uses physics-aware multi-view foreground generation and background synthesis to couple motion plausibility with cross-view geometry. |

[Back to recent-literature navigation](#recent-literature)

#### Physical and causal evaluation

| First posted | Paper and resources | Consistency focus |
|:--|:--|:--|
| 2026-10-30 | **[GeoFlip](https://arxiv.org/abs/2610.42002)**<br><sub>Benchmark + Dataset · Video · also External/Internal</sub> | Uses paired geometric interventions with verified reference events to test whether image-conditioned videos predict correct physical outcomes. |
| 2026-10-22 | **[PhysTrace / IntPhys2-Timing](https://arxiv.org/abs/2610.31429)**<br><sub>Evaluator + Dataset · Video · also Internal</sub><br>[Code](https://github.com/PhysTrace/PhysTrace) | Matches history-conditioned physical expectations to video windows to localize violations; adds timed annotations and probes diffusion or flow reconstruction trajectories. |
| 2026-10-19 | **[PVBench](https://arxiv.org/abs/2610.26711)**<br><sub>Benchmark + Evaluator · Video · also External/Internal</sub> | Measures generated-video physical plausibility using object-level geometry, kinematics and conservation-law diagnostics alongside semantic and temporal criteria. |
| 2026-10-06 | **[World Models’ Last Exam in Physics](https://arxiv.org/abs/2610.08791)**<br><sub>Benchmark + Evaluator · Video · also Internal</sub> | Pairs controlled image-conditioned video tasks with observability screening and task-specific physical measurements across six physical domains, without reference videos. |
| 2026-10-01 | **[PhysicsLENS](https://arxiv.org/abs/2610.01162)**<br><sub>Benchmark + Dataset · Video · also External/Internal</sub> | Holds the conditioning frame and task fixed while varying stated physical properties to separate plausible-looking motion from sensitivity to hidden physics. |
| 2026-09-29 | **[PhyProbe](https://arxiv.org/abs/2609.38377)**<br><sub>Evaluator · Video · also Internal</sub> | Calibrates a lightweight scorer over frozen spatio-temporal features using ranking, noisy scalar supervision and anchors for physical-violation evaluation. |
| 2026-06-25 | **[PhyEditBench](https://arxiv.org/abs/2606.26551)**<br><sub>Benchmark + Method · Image / Video · also External</sub><br>[Code](https://github.com/Previsior/PhyEditBench) | Uses real physical transitions and anti-physics cases to diagnose physical understanding in instruction-based image editing. |
| 2026-06-21 | **[Reference-free physical assessment](https://arxiv.org/abs/2606.22363)**<br><sub>Evaluator · Video · also Internal</sub> | Combines SLAM- and optical-flow-based measures to rank generated robotic videos and localize physical artifacts without reference videos. |
| 2026-05-11 | **[PhyGround / PhyJudge-9B](https://arxiv.org/abs/2605.10806)**<br><sub>Benchmark + Evaluator · Video · also Internal</sub><br>[Project](https://phyground.github.io/) | Grounds physical evaluation in observable law-specific questions, controlled human annotations and a specialized visual-language judge. |
| 2026-05-11 | **[WorldReasonBench / WorldRewardBench](https://arxiv.org/abs/2605.10434)**<br><sub>Benchmark + Evaluator · Video · also Internal/External</sub><br>[Code](https://github.com/UniX-AI-Lab/WorldReasonBench/) · [Project](https://unix-ai-lab.github.io/WorldReasonBench/) | Tests future-state evolution from initial conditions and actions with process-aware reasoning checks, plus expert preference pairs for world-reasoning rewards. |
| 2026-05-08 | **[AV-Phys Bench / AV-Phys Agent](https://arxiv.org/abs/2605.07061)**<br><sub>Benchmark + Evaluator · Video / Audio · also External/Internal</sub><br>[Code](https://github.com/ZijunCui02/AV-Phys) · [Project](https://zijuncui.com/AV-Phys/) | Tests visual, audio and cross-modal physical commonsense across steady scenes and transitions, combining rubric judgments with acoustic measurements. |
| 2026-03-20 | **[Physion-Eval](https://arxiv.org/abs/2603.19607)**<br><sub>Benchmark + Dataset · Video · also Internal</sub><br>[Project](https://huggingface.co/datasets/PhysionLabs/Physion-Eval) | Provides expert reasoning traces and temporally localized physical-glitch annotations for diagnosing generated-video realism failures. |
| 2025-09-26 | **[VideoScore2 / VideoFeedback2](https://arxiv.org/abs/2509.22799)**<br><sub>Evaluator + Dataset · Video · also External/Internal</sub><br>[Project](https://tiger-ai-lab.github.io/VideoScore2/) | Produces interpretable assessments of visual quality, text alignment and physical or commonsense consistency using human-annotated video feedback. |
| 2025-03-27 | **[VBench-2.0](https://arxiv.org/abs/2503.21755)**<br><sub>Benchmark · Video · also External/Internal</sub> | Extends video evaluation toward human fidelity, controllability, creativity, physics and commonsense rather than appearance alone. |

[Back to recent-literature navigation](#recent-literature)
