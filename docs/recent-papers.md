# Recent papers and evidence register

[Return to the survey](../README.md)

<a id="recent-literature"></a>
## Recent literature · 2025–2026

**81 distinct papers · 46 first posted in 2026 · 35 first posted in 2025**  
Research snapshot: **2026-09-16**. Dates below are first arXiv submission dates, not conference publication dates.

[JSON](../resources/recent_papers.json) · [CSV](../resources/recent_papers.csv) · [BibTeX, abbreviated authors](../resources/recent_papers.bib) · [Evidence register](../docs/recent-papers.md#evidence-register) · [Scope and limitations](../docs/research-notes.md)

> **Reading note.** Titles, dates and short summaries were checked against original arXiv records or their indexed abstracts. Conference status and empirical results were not comprehensively audited. The three-relation assignments are editorial annotations under this survey's taxonomy. A method and its associated benchmark are counted once when they share one paper.

| Primary relation | Papers in this update | Browse |
|:--|--:|:--|
| **External** | 30 | [External consistency](#recent-external) |
| **Internal** | 25 | [Internal consistency](#recent-internal) |
| **Normative** | 26 | [Normative consistency](#recent-normative) |

Within each topic, the most recently posted papers appear first. **Paper titles link to the original arXiv record**; optional code/project links are author-provided discovery links, not a deployment or availability guarantee.

<a id="recent-external"></a>
### 01 · External consistency

#### Image editing and in-context generation

| First posted | Paper and resources | Consistency focus |
|:--|:--|:--|
| 2026-08-30 | **[Discrete Diffusion Bridges](https://arxiv.org/abs/2608.29997)**<br><sub>Method · Image · also Internal</sub><br>[Code](https://github.com/HKU-HealthAI/DDB) | Uses source-anchored corruption and an information-guided schedule to balance semantic editing with structural preservation in discrete diffusion. |
| 2026-01-09 | **[Generalized multi-image editing](https://arxiv.org/abs/2601.05572)**<br><sub>Method + Benchmark · Image · also Internal</sub> | Disambiguates multiple input images through latent separators and image-index encoding; evaluates cross-image editing integration. |
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
| 2026-03-30 | **[MMFace-DiT](https://arxiv.org/abs/2603.29029)**<br><sub>Method · Image</sub><br>[Project](https://vcbsl.github.io/MMFace-DiT/) | Fuses semantic text and spatial mask or sketch conditions within a dual-stream diffusion transformer for controllable face synthesis. |
| 2025-12-15 | **[Beyond the Visible](https://arxiv.org/abs/2512.13392)**<br><sub>Method · Video · also Internal</sub><br>[Project](https://anranqi.github.io/beyondvisible.github.io/) | Separates articulated motion from appearance editing to control newly revealed regions in image-to-video generation. |
| 2025-03-13 | **[CameraCtrl II](https://arxiv.org/abs/2503.10592)**<br><sub>Method · Video · also Internal</sub> | Extends camera-controlled video generation toward wider scene exploration while preserving dynamic content and inter-clip continuity. |
| 2025-03-11 | **[OminiControl2](https://arxiv.org/abs/2503.08280)**<br><sub>Method · Image · also Internal</sub> | Compresses condition tokens and reuses conditional features across denoising steps for efficient multi-condition image generation. |
| 2025-01-07 | **[Diffusion as Shader](https://arxiv.org/abs/2501.03847)**<br><sub>Method · Video / 3D · also Internal</sub><br>[Code](https://github.com/IGL-HKUST/DiffusionAsShader) · [Project](https://igl-hkust.github.io/das/) | Uses 3D tracking videos as a common control interface for camera, motion and object manipulation with temporal correspondence. |

[Back to recent-literature navigation](#recent-literature)

#### Temporally consistent video editing

| First posted | Paper and resources | Consistency focus |
|:--|:--|:--|
| 2026-08-04 | **[JoyAI-Video-Edit](https://arxiv.org/abs/2608.03974)**<br><sub>Method · Video · also Internal</sub><br>[Code](https://github.com/jd-opensource/JoyAI-Video-Edit) | Combines source-anchored distillation and long-horizon autoregressive training to preserve source fidelity in streaming video editing. |
| 2026-06-07 | **[Temporal-structure-preserving editing](https://arxiv.org/abs/2606.08780)**<br><sub>Method · Video · also Internal</sub> | Preserves source-video temporal organization using semantic clip partitioning, anchor frames and clip-adaptive token merging. |
| 2026-02-02 | **[MLV-Edit](https://arxiv.org/abs/2602.02123)**<br><sub>Method · Video · also Internal</sub> | Uses flow blending at segment boundaries and attention anchors to reduce flicker and structural drift in minute-length editing. |

[Back to recent-literature navigation](#recent-literature)

#### Editing and reasoning evaluation

| First posted | Paper and resources | Consistency focus |
|:--|:--|:--|
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
| 2026-03-10 | **[ID-LoRA](https://arxiv.org/abs/2603.10256)**<br><sub>Method · Video / Audio · also External</sub> | Jointly personalizes visual appearance and voice using reference conditioning, separated temporal positions and identity guidance. |
| 2026-02-15 | **[SpatialID](https://arxiv.org/abs/2602.13994)**<br><sub>Method · Image · also External</sub> | Restricts identity injection spatially and schedules it over denoising to reduce interference with background and prompt-driven content. |
| 2025-06-11 | **[Asymmetry Zigzag Sampling](https://arxiv.org/abs/2506.09612)**<br><sub>Method · Image · also External</sub><br>[Code](https://github.com/Mingxiao-Li/Asymmetry-Zigzag-StoryDiffusion) | Alternates asymmetric prompts and shared visual cues during training-free sampling to preserve subjects across story panels. |
| 2025-04-23 | **[DreamO](https://arxiv.org/abs/2504.16915)**<br><sub>Method · Image · also External</sub> | Routes reference features and task conditions in a unified diffusion transformer for identity, subject, style and background customization. |
| 2025-04-02 | **[UNO](https://arxiv.org/abs/2504.02160)**<br><sub>Method · Image · also External</sub> | Builds consistent multi-subject training pairs and uses multi-image conditioning to preserve subjects under compositional control. |

[Back to recent-literature navigation](#recent-literature)

#### Subject and identity evaluation

| First posted | Paper and resources | Consistency focus |
|:--|:--|:--|
| 2026-06-14 | **[CogCanvas](https://arxiv.org/abs/2606.15867)**<br><sub>Benchmark · Image · also External</sub> | Jointly tests multi-person identity, per-subject object and fashion binding, background fidelity and interaction plausibility. |

[Back to recent-literature navigation](#recent-literature)

#### Multi-view and geometric consistency

| First posted | Paper and resources | Consistency focus |
|:--|:--|:--|
| 2026-09-09 | **[StreetDiff / Street360](https://arxiv.org/abs/2609.09890)**<br><sub>Method + Dataset · Image / 3D · also External</sub> | Uses panorama-perspective alignment constraints during denoising to preserve urban-scene layout across rotated views. |
| 2026-07-19 | **[HarmoHOI](https://arxiv.org/abs/2607.17097)**<br><sub>Method · Video / 3D · also Normative</sub><br>[Project](https://droliven.github.io/HarmoHOI_project) | Jointly models synchronized interaction videos and globally aligned 3D point tracks to couple appearance, motion and multi-view geometry. |
| 2026-07-06 | **[MV-Forcing](https://arxiv.org/abs/2607.05376)**<br><sub>Method · Video / 3D</sub><br>[Project](https://galfiebelman.github.io/mv-forcing/) | Bridges view-wise and temporal autoregression with reconstructed 4D geometry and spatio-temporal self-forcing. |
| 2026-06-09 | **[HarmoView](https://arxiv.org/abs/2606.10839)**<br><sub>Method · Video / 3D · also External</sub> | Combines appearance anchors, proxy tokens and identity-separated positional encoding with a progressive multi-view training curriculum. |
| 2026-05-19 | **[SEGS](https://arxiv.org/abs/2605.19876)**<br><sub>Method · 3D</sub> | Injects structural-energy gradients derived from diffusion features to mitigate inconsistent geometry and Janus artifacts across views. |
| 2026-02-10 | **[ConsID-Gen / ConsIDVid](https://arxiv.org/abs/2602.10113)**<br><sub>Method + Benchmark + Dataset · Video / 3D · also External</sub><br>[Project](https://myangwu.github.io/ConsID-Gen) | Augments image-to-video conditioning with auxiliary views and evaluates identity and geometry using the ConsIDVid data and benchmark. |
| 2026-01-25 | **[MV-S2V](https://arxiv.org/abs/2601.17756)**<br><sub>Method · Video / 3D · also External</sub><br>[Project](https://szy-young.github.io/mv-s2v) | Uses multiple reference views and temporally shifted positional encoding to separate subject identity from reference viewpoint. |

[Back to recent-literature navigation](#recent-literature)

#### Multi-shot narratives and persistent memory

| First posted | Paper and resources | Consistency focus |
|:--|:--|:--|
| 2026-05-26 | **[ReCA / MSVE-Bench](https://arxiv.org/abs/2605.26525)**<br><sub>Method + Benchmark · Video · also External</sub><br>[Project](https://reca.vmv.re) | Allocates planning and generation context hierarchically to preserve observed state while extending a source clip into multiple shots. |
| 2026-05-19 | **[MSAVBench](https://arxiv.org/abs/2605.20183)**<br><sub>Benchmark · Video / Audio · also External</sub> | Evaluates video, audio, shots and references with adaptive segmentation and tool-grounded evidence for multi-shot audio-video generation. |
| 2026-05-14 | **[EntityBench / EntityMem](https://arxiv.org/abs/2605.15199)**<br><sub>Benchmark + Method · Video · also External</sub><br>[Code](https://github.com/Catherine-R-He/EntityBench/) | Tracks recurring characters, objects and locations across long shot sequences, with fidelity-gated scoring and a persistent entity-memory baseline. |
| 2026-05-12 | **[CausalCine](https://arxiv.org/abs/2605.12496)**<br><sub>Method · Video · also External</sub><br>[Project](https://yihao-meng.github.io/CausalCine/) | Uses content-aware memory routing and causal multi-shot training to support streaming narratives with changing prompts and shot boundaries. |
| 2026-02-14 | **[DCDM](https://arxiv.org/abs/2602.13637)**<br><sub>Method · Video · also External/Normative</sub> | Separates intra-clip semantics, inter-clip camera control and inter-shot element persistence into complementary video-generation components. |
| 2025-12-22 | **[StoryMem / ST-Bench](https://arxiv.org/abs/2512.19539)**<br><sub>Method + Benchmark · Video · also External</sub> | Conditions iterative shot synthesis on selected historical keyframes and introduces ST-Bench for long-form storytelling evaluation. |
| 2025-10-23 | **[HoloCine](https://arxiv.org/abs/2510.20822)**<br><sub>Method · Video · also External</sub><br>[Project](https://holo-cine.github.io/) | Combines shot-local text conditioning with sparse inter-shot attention for jointly generated, coherent cinematic scenes. |
| 2025-04-16 | **[WorldMem](https://arxiv.org/abs/2504.12369)**<br><sub>Method · Video / 3D · also Normative</sub> | Retrieves state-indexed visual memories to reconstruct previously visited scenes across viewpoint and temporal gaps. |
| 2025-03-19 | **[VideoGen-of-Thought](https://arxiv.org/abs/2503.15138)**<br><sub>Method · Video · also External</sub> | Combines storyline planning, identity-aware cross-shot propagation and latent transitions for coherent multi-shot video generation. |

[Back to recent-literature navigation](#recent-literature)

#### Long-horizon video generation

| First posted | Paper and resources | Consistency focus |
|:--|:--|:--|
| 2025-10-02 | **[Self-Forcing++](https://arxiv.org/abs/2510.02283)**<br><sub>Method · Video</sub><br>[Project](https://self-forcing-plus-plus.github.io/) | Supervises sampled segments of self-generated long videos to reduce error accumulation beyond short-teacher training horizons. |
| 2025-09-26 | **[LongLive](https://arxiv.org/abs/2509.22622)**<br><sub>Method · Video · also External</sub> | Combines long-rollout training, prompt-aware cache refresh and frame sinks to preserve consistency during interactive long-video generation. |
| 2025-06-09 | **[Self Forcing](https://arxiv.org/abs/2506.08009)**<br><sub>Method · Video</sub><br>[Project](https://self-forcing.github.io/) | Trains on self-generated context to reduce exposure bias; long extrapolation still requires separate consistency evaluation. |

[Back to recent-literature navigation](#recent-literature)

<a id="recent-normative"></a>
### 03 · Normative consistency

#### Preference alignment and reward learning

| First posted | Paper and resources | Consistency focus |
|:--|:--|:--|
| 2026-07-07 | **[D2PO](https://arxiv.org/abs/2607.06609)**<br><sub>Method · Image</sub> | Optimizes sampler timesteps and guidance weights through dynamic preferences rather than fixed teacher-regression targets. |
| 2026-06-25 | **[Qwen-Image-2.0-RL](https://arxiv.org/abs/2606.27608)**<br><sub>Method · Image · also External/Internal</sub> | Uses task-specific rewards, GRPO and on-policy distillation to align image generation and editing while preserving identity. |
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
| 2026-09-11 | **[GRACE](https://arxiv.org/abs/2609.12731)**<br><sub>Method · Image</sub> | Combines sensitive-subspace adapters, safe anchors and dynamic gating to reduce undesired concepts while limiting semantic drift. |
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
| 2026-09-01 | **[Chain-of-events physical conditioning](https://arxiv.org/abs/2609.00656)**<br><sub>Method · Video · also External/Internal</sub> | Represents physical evolution as event chains and uses routed keyframe conditioning with physics-informed semantic guidance. |
| 2026-04-03 | **[MMPhysVideo](https://arxiv.org/abs/2604.02817)**<br><sub>Method · Video · also Internal</sub> | Jointly models appearance, geometry and trajectory cues, then distills learned physical priors into an efficient video generator. |
| 2026-03-19 | **[PhysVideo / PhysMV](https://arxiv.org/abs/2603.18639)**<br><sub>Method + Dataset · Video / 3D · also Internal</sub> | Uses physics-aware multi-view foreground generation and background synthesis to couple motion plausibility with cross-view geometry. |

[Back to recent-literature navigation](#recent-literature)

#### Physical and causal evaluation

| First posted | Paper and resources | Consistency focus |
|:--|:--|:--|
| 2026-06-25 | **[PhyEditBench](https://arxiv.org/abs/2606.26551)**<br><sub>Benchmark + Method · Image / Video · also External</sub><br>[Code](https://github.com/Previsior/PhyEditBench) | Uses real physical transitions and anti-physics cases to diagnose physical understanding in instruction-based image editing. |
| 2026-05-11 | **[PhyGround / PhyJudge-9B](https://arxiv.org/abs/2605.10806)**<br><sub>Benchmark + Evaluator · Video · also Internal</sub><br>[Project](https://phyground.github.io/) | Grounds physical evaluation in observable law-specific questions, controlled human annotations and a specialized visual-language judge. |
| 2026-03-20 | **[Physion-Eval](https://arxiv.org/abs/2603.19607)**<br><sub>Benchmark + Dataset · Video · also Internal</sub><br>[Project](https://huggingface.co/datasets/PhysionLabs/Physion-Eval) | Provides expert reasoning traces and temporally localized physical-glitch annotations for diagnosing generated-video realism failures. |
| 2025-09-26 | **[VideoScore2 / VideoFeedback2](https://arxiv.org/abs/2509.22799)**<br><sub>Evaluator + Dataset · Video · also External/Internal</sub><br>[Project](https://tiger-ai-lab.github.io/VideoScore2/) | Produces interpretable assessments of visual quality, text alignment and physical or commonsense consistency using human-annotated video feedback. |
| 2025-03-27 | **[VBench-2.0](https://arxiv.org/abs/2503.21755)**<br><sub>Benchmark · Video · also External/Internal</sub> | Extends video evaluation toward human fidelity, controllability, creativity, physics and commonsense rather than appearance alone. |

[Back to recent-literature navigation](#recent-literature)

---

<a id="evidence-register"></a>
## Evidence register

This register preserves full titles and the exact primary-source identifiers used in this update. The recorded author is the first author only. Short names in the tables are navigation labels, not replacement bibliographic titles.

### 2609.12731 · GRACE

**GRACE: Adaptive Concept Erasure with Geometry-Guided Retention in Diffusion Models**

First author: Gong, Qinghui. First submitted: 2026-09-11. Source: [arXiv:2609.12731](https://arxiv.org/abs/2609.12731). Checked: 2026-09-16.

Relation: **Normative**; topic: Safety, erasure and capability retention. Secondary relations: none recorded.

Combines sensitive-subspace adapters, safe anchors and dynamic gating to reduce undesired concepts while limiting semantic drift.

### 2609.09890 · StreetDiff / Street360

**StreetDiff: Multi-view Street Scenes Generation via Cross-view Consistent Multi-view Stable Diffusion with Structure Prompts**

First author: Zhang, Qi. First submitted: 2026-09-09. Source: [arXiv:2609.09890](https://arxiv.org/abs/2609.09890). Checked: 2026-09-16.

Relation: **Internal**; topic: Multi-view and geometric consistency. Secondary relations: External.

Uses panorama-perspective alignment constraints during denoising to preserve urban-scene layout across rotated views.

### 2609.00656 · Chain-of-events physical conditioning

**Physically Plausible Video Generation via Visual-Semantic Chain-of-Events Conditioning**

First author: Wang, Zixuan. First submitted: 2026-09-01. Source: [arXiv:2609.00656](https://arxiv.org/abs/2609.00656). Checked: 2026-09-16.

Relation: **Normative**; topic: Physics-aware generation. Secondary relations: External, Internal.

Represents physical evolution as event chains and uses routed keyframe conditioning with physics-informed semantic guidance.

### 2608.29997 · Discrete Diffusion Bridges

**Discrete Diffusion Bridges for Spatiotemporally Aligned Image Translation and Generation**

First author: Xie, Xing. First submitted: 2026-08-30. Source: [arXiv:2608.29997](https://arxiv.org/abs/2608.29997). Checked: 2026-09-16.

Relation: **External**; topic: Image editing and in-context generation. Secondary relations: Internal.

Uses source-anchored corruption and an information-guided schedule to balance semantic editing with structural preservation in discrete diffusion.

### 2608.03974 · JoyAI-Video-Edit

**JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion**

First author: Xiao, Yicheng. First submitted: 2026-08-04. Source: [arXiv:2608.03974](https://arxiv.org/abs/2608.03974). Checked: 2026-09-16.

Relation: **External**; topic: Temporally consistent video editing. Secondary relations: Internal.

Combines source-anchored distillation and long-horizon autoregressive training to preserve source fidelity in streaming video editing.

### 2607.17097 · HarmoHOI

**HarmoHOI: Harmonizing Appearance and 3D Motion for Multi-view Hand-Object Interaction Synthesis**

First author: Dang, Lingwei. First submitted: 2026-07-19. Source: [arXiv:2607.17097](https://arxiv.org/abs/2607.17097). Checked: 2026-09-16.

Relation: **Internal**; topic: Multi-view and geometric consistency. Secondary relations: Normative.

Jointly models synchronized interaction videos and globally aligned 3D point tracks to couple appearance, motion and multi-view geometry.

### 2607.06609 · D2PO

**D2PO: Optimizing Diffusion Samplers via Dynamic Preference**

First author: Kim, Jinkyu. First submitted: 2026-07-07. Source: [arXiv:2607.06609](https://arxiv.org/abs/2607.06609). Checked: 2026-09-16.

Relation: **Normative**; topic: Preference alignment and reward learning. Secondary relations: none recorded.

Optimizes sampler timesteps and guidance weights through dynamic preferences rather than fixed teacher-regression targets.

### 2607.05376 · MV-Forcing

**MV-Forcing: Long Multi-View Video Generation via 4D-Grounded Spatio-Temporal Self-Forcing**

First author: Fiebelman, Gal. First submitted: 2026-07-06. Source: [arXiv:2607.05376](https://arxiv.org/abs/2607.05376). Checked: 2026-09-16.

Relation: **Internal**; topic: Multi-view and geometric consistency. Secondary relations: none recorded.

Bridges view-wise and temporal autoregression with reconstructed 4D geometry and spatio-temporal self-forcing.

### 2606.27608 · Qwen-Image-2.0-RL

**Qwen-Image-2.0-RL Technical Report**

First author: Xu, Yixian. First submitted: 2026-06-25. Source: [arXiv:2606.27608](https://arxiv.org/abs/2606.27608). Checked: 2026-09-16.

Relation: **Normative**; topic: Preference alignment and reward learning. Secondary relations: External, Internal.

Uses task-specific rewards, GRPO and on-policy distillation to align image generation and editing while preserving identity.

### 2606.26551 · PhyEditBench

**PhyEditBench: A Real-World Multi-Stage Benchmark for Physics-Aware Image Editing**

First author: Guo, Shengbin. First submitted: 2026-06-25. Source: [arXiv:2606.26551](https://arxiv.org/abs/2606.26551). Checked: 2026-09-16.

Relation: **Normative**; topic: Physical and causal evaluation. Secondary relations: External.

Uses real physical transitions and anti-physics cases to diagnose physical understanding in instruction-based image editing.

### 2606.15867 · CogCanvas

**CogCanvas: A Benchmark for Evaluating Multi-Subject Reference-Based Image Generation**

First author: Nguyen, Long-Bao. First submitted: 2026-06-14. Source: [arXiv:2606.15867](https://arxiv.org/abs/2606.15867). Checked: 2026-09-16.

Relation: **Internal**; topic: Subject and identity evaluation. Secondary relations: External.

Jointly tests multi-person identity, per-subject object and fashion binding, background fidelity and interaction plausibility.

### 2606.10839 · HarmoView

**HarmoView: Harmonizing Multi-View Constraints for Identity-Consistent Video Generation**

First author: Wang, Cong. First submitted: 2026-06-09. Source: [arXiv:2606.10839](https://arxiv.org/abs/2606.10839). Checked: 2026-09-16.

Relation: **Internal**; topic: Multi-view and geometric consistency. Secondary relations: External.

Combines appearance anchors, proxy tokens and identity-separated positional encoding with a progressive multi-view training curriculum.

### 2606.08780 · Temporal-structure-preserving editing

**Beyond Consistency: Preserving Temporal Structure in Zero-Shot Video Editing**

First author: Liu, Deyin. First submitted: 2026-06-07. Source: [arXiv:2606.08780](https://arxiv.org/abs/2606.08780). Checked: 2026-09-16.

Relation: **External**; topic: Temporally consistent video editing. Secondary relations: Internal.

Preserves source-video temporal organization using semantic clip partitioning, anchor frames and clip-adaptive token merging.

### 2606.01481 · SafeGen-Bench

**SafeGen-Bench: Benchmarking Safety in Image-Conditioned Text-to-Video Generation**

First author: Ma, Yingzi. First submitted: 2026-05-31. Source: [arXiv:2606.01481](https://arxiv.org/abs/2606.01481). Checked: 2026-09-16.

Relation: **Normative**; topic: Safety, erasure and capability retention. Secondary relations: External, Internal.

Tests unsafe behaviors that can emerge from jointly benign-looking image and text inputs in conditional video generation.

### 2605.28902 · OCE

**Orthogonal Concept Erasure for Diffusion Models**

First author: Sun, Yuhao. First submitted: 2026-05-27. Source: [arXiv:2605.28902](https://arxiv.org/abs/2605.28902). Checked: 2026-09-16.

Relation: **Normative**; topic: Safety, erasure and capability retention. Secondary relations: none recorded.

Uses multiplicative orthogonal parameter transformations to separate concept removal from broader generative-capability preservation.

### 2605.28615 · BiDPO / BiComp

**Compositional Text-to-Image Generation Via Region-aware Bimodal Direct Preference Optimization**

First author: Liu, Zhuohan. First submitted: 2026-05-27. Source: [arXiv:2605.28615](https://arxiv.org/abs/2605.28615). Checked: 2026-09-16.

Relation: **External**; topic: Compositionality and spatial grounding. Secondary relations: Normative.

Combines image-text preference optimization, compositional preference data and region-level guidance for prompt fidelity.

### 2605.26525 · ReCA / MSVE-Bench

**ReCA: Multi-Shot Long Video Extrapolation via Recursive Context Allocation**

First author: Liu, Akide. First submitted: 2026-05-26. Source: [arXiv:2605.26525](https://arxiv.org/abs/2605.26525). Checked: 2026-09-16.

Relation: **Internal**; topic: Multi-shot narratives and persistent memory. Secondary relations: External.

Allocates planning and generation context hierarchically to preserve observed state while extending a source clip into multiple shots.

### 2605.20183 · MSAVBench

**MSAVBench: Towards Comprehensive and Reliable Evaluation of Multi-Shot Audio-Video Generation**

First author: Wei, Yujie. First submitted: 2026-05-19. Source: [arXiv:2605.20183](https://arxiv.org/abs/2605.20183). Checked: 2026-09-16.

Relation: **Internal**; topic: Multi-shot narratives and persistent memory. Secondary relations: External.

Evaluates video, audio, shots and references with adaptive segmentation and tool-grounded evidence for multi-shot audio-video generation.

### 2605.19876 · SEGS

**Structural Energy Guidance for View-Consistent Text-to-3D Generation**

First author: Zhang, Qing. First submitted: 2026-05-19. Source: [arXiv:2605.19876](https://arxiv.org/abs/2605.19876). Checked: 2026-09-16.

Relation: **Internal**; topic: Multi-view and geometric consistency. Secondary relations: none recorded.

Injects structural-energy gradients derived from diffusion features to mitigate inconsistent geometry and Janus artifacts across views.

### 2605.19320 · TextAlign

**TextAlign: Preference Alignment for Text Rendering with Hierarchical Rewards**

First author: Cui, Mingxuan. First submitted: 2026-05-19. Source: [arXiv:2605.19320](https://arxiv.org/abs/2605.19320). Checked: 2026-09-16.

Relation: **External**; topic: Typography and text rendering. Secondary relations: Normative.

Decomposes rendering defects into global, word and glyph levels to supply hierarchical rewards for preference alignment.

### 2605.15199 · EntityBench / EntityMem

**EntityBench: Towards Entity-Consistent Long-Range Multi-Shot Video Generation**

First author: He, Ruozhen. First submitted: 2026-05-14. Source: [arXiv:2605.15199](https://arxiv.org/abs/2605.15199). Checked: 2026-09-16.

Relation: **Internal**; topic: Multi-shot narratives and persistent memory. Secondary relations: External.

Tracks recurring characters, objects and locations across long shot sequences, with fidelity-gated scoring and a persistent entity-memory baseline.

### 2605.12496 · CausalCine

**CausalCine: Real-Time Autoregressive Generation for Multi-Shot Video Narratives**

First author: Meng, Yihao. First submitted: 2026-05-12. Source: [arXiv:2605.12496](https://arxiv.org/abs/2605.12496). Checked: 2026-09-16.

Relation: **Internal**; topic: Multi-shot narratives and persistent memory. Secondary relations: External.

Uses content-aware memory routing and causal multi-shot training to support streaming narratives with changing prompts and shot boundaries.

### 2605.10806 · PhyGround / PhyJudge-9B

**PhyGround: Benchmarking Physical Reasoning in Generative World Models**

First author: Lin, Juyi. First submitted: 2026-05-11. Source: [arXiv:2605.10806](https://arxiv.org/abs/2605.10806). Checked: 2026-09-16.

Relation: **Normative**; topic: Physical and causal evaluation. Secondary relations: Internal.

Grounds physical evaluation in observable law-specific questions, controlled human annotations and a specialized visual-language judge.

### 2605.07503 · Diffusion-APO

**Diffusion-APO: Trajectory-Aware Direct Preference Alignment for Video Diffusion Transformers**

First author: Zhu, Jingyuan. First submitted: 2026-05-08. Source: [arXiv:2605.07503](https://arxiv.org/abs/2605.07503). Checked: 2026-09-16.

Relation: **Normative**; topic: Preference alignment and reward learning. Secondary relations: External.

Aligns preference-training noise with inference trajectories and supports several online and offline video-alignment stages.

### 2605.01761 · TrajShield

**TrajShield: Trajectory-Level Safety Mediation for Defending Text-to-Video Models Against Jailbreak Attacks**

First author: Zou, Quanchen. First submitted: 2026-05-03. Source: [arXiv:2605.01761](https://arxiv.org/abs/2605.01761). Checked: 2026-09-16.

Relation: **Normative**; topic: Safety, erasure and capability retention. Secondary relations: External, Internal.

Uses trajectory-level risk analysis and targeted prompt rewriting to address unsafe intent and temporally emerging video risks.

### 2604.21036 · Target-based fairness prompting

**Who Defines Fairness? Target-Based Prompting for Demographic Representation in Generative Models**

First author: Nizam, Marzia Binta. First submitted: 2026-04-22. Source: [arXiv:2604.21036](https://arxiv.org/abs/2604.21036). Checked: 2026-09-16.

Relation: **Normative**; topic: Safety, erasure and capability retention. Secondary relations: External.

Audits generated demographic representation against explicitly declared target distributions rather than assuming one universal fairness target.

### 2604.04575 · Erasure or Erosion?

**Erasure or Erosion? Evaluating Compositional Degradation in Unlearned Text-To-Image Diffusion Models**

First author: Koma, Arian Komaei. First submitted: 2026-04-06. Source: [arXiv:2604.04575](https://arxiv.org/abs/2604.04575). Checked: 2026-09-16.

Relation: **Normative**; topic: Safety, erasure and capability retention. Secondary relations: External.

Audits how concept unlearning affects attribute binding, spatial relations and counting rather than checking erasure success alone.

### 2604.02817 · MMPhysVideo

**MMPhysVideo: Scaling Physical Plausibility in Video Generation via Joint Multimodal Modeling**

First author: Lin, Shubo. First submitted: 2026-04-03. Source: [arXiv:2604.02817](https://arxiv.org/abs/2604.02817). Checked: 2026-09-16.

Relation: **Normative**; topic: Physics-aware generation. Secondary relations: Internal.

Jointly models appearance, geometry and trajectory cues, then distills learned physical priors into an efficient video generator.

### 2603.29029 · MMFace-DiT

**MMFace-DiT: A Dual-Stream Diffusion Transformer for High-Fidelity Multimodal Face Generation**

First author: Krishnamurthy, Bharath. First submitted: 2026-03-30. Source: [arXiv:2603.29029](https://arxiv.org/abs/2603.29029). Checked: 2026-09-16.

Relation: **External**; topic: Structural and camera control. Secondary relations: none recorded.

Fuses semantic text and spatial mask or sketch conditions within a dual-stream diffusion transformer for controllable face synthesis.

### 2603.22228 · SpatialReward / SpatRelBench

**SpatialReward: Verifiable Spatial Reward Modeling for Fine-Grained Spatial Consistency in Text-to-Image Generation**

First author: Zhou, Sashuai. First submitted: 2026-03-23. Source: [arXiv:2603.22228](https://arxiv.org/abs/2603.22228). Checked: 2026-09-16.

Relation: **External**; topic: Compositionality and spatial grounding. Secondary relations: Normative.

Grounds spatial reward judgments in decomposed prompts and detected objects; introduces SpatRelBench for fine-grained spatial evaluation.

### 2603.19607 · Physion-Eval

**Physion-Eval: Evaluating Physical Realism in Generated Video via Human Reasoning**

First author: Zhang, Qin. First submitted: 2026-03-20. Source: [arXiv:2603.19607](https://arxiv.org/abs/2603.19607). Checked: 2026-09-16.

Relation: **Normative**; topic: Physical and causal evaluation. Secondary relations: Internal.

Provides expert reasoning traces and temporally localized physical-glitch annotations for diagnosing generated-video realism failures.

### 2603.18639 · PhysVideo / PhysMV

**PhysVideo: Physically Plausible Video Generation with Cross-View Geometry Guidance**

First author: Wang, Cong. First submitted: 2026-03-19. Source: [arXiv:2603.18639](https://arxiv.org/abs/2603.18639). Checked: 2026-09-16.

Relation: **Normative**; topic: Physics-aware generation. Secondary relations: Internal.

Uses physics-aware multi-view foreground generation and background synthesis to couple motion plausibility with cross-view geometry.

### 2603.11556 · DIAE

**Enhancing Image Aesthetics with Dual-Conditioned Diffusion Models Guided by Multimodal Perception**

First author: Nan, Xinyu. First submitted: 2026-03-12. Source: [arXiv:2603.11556](https://arxiv.org/abs/2603.11556). Checked: 2026-09-16.

Relation: **Normative**; topic: Preference alignment and reward learning. Secondary relations: External, Internal.

Uses multimodal aesthetic guidance and weakly paired supervision to improve aesthetics while retaining image content.

### 2603.10256 · ID-LoRA

**ID-LoRA: Identity-Driven Audio-Video Personalization with In-Context LoRA**

First author: Dahan, Aviad. First submitted: 2026-03-10. Source: [arXiv:2603.10256](https://arxiv.org/abs/2603.10256). Checked: 2026-09-16.

Relation: **Internal**; topic: Subject and identity preservation. Secondary relations: External.

Jointly personalizes visual appearance and voice using reference conditioning, separated temporal positions and identity guidance.

### 2603.07119 · TIQA / ANTIQA

**TIQA: Human-Aligned Text Quality Assessment in Generated Images**

First author: Koltsov, Kirill. First submitted: 2026-03-07. Source: [arXiv:2603.07119](https://arxiv.org/abs/2603.07119). Checked: 2026-09-16.

Relation: **External**; topic: Typography and text rendering. Secondary relations: Normative.

Evaluates perceptual quality of rendered text with human-labeled crops and images rather than relying only on OCR correctness.

### 2603.06032 · StruVis

**StruVis: Enhancing Reasoning-based Text-to-Image Generation via Thinking with Structured Vision**

First author: Lyu, Yuanhuiyi. First submitted: 2026-03-06. Source: [arXiv:2603.06032](https://arxiv.org/abs/2603.06032). Checked: 2026-09-16.

Relation: **External**; topic: Compositionality and spatial grounding. Secondary relations: none recorded.

Uses structured visual representations as intermediate reasoning states to improve prompt interpretation before image generation.

### 2602.20903 · TextPecker

**TextPecker: Rewarding Structural Anomaly Quantification for Enhancing Visual Text Rendering**

First author: Zhu, Hanshen. First submitted: 2026-02-24. Source: [arXiv:2602.20903](https://arxiv.org/abs/2602.20903). Checked: 2026-09-16.

Relation: **External**; topic: Typography and text rendering. Secondary relations: Normative.

Uses character-level structural anomaly supervision to make text-rendering rewards sensitive to malformed glyphs and distortions.

### 2602.13994 · SpatialID

**Inject Where It Matters: Training-Free Spatially-Adaptive Identity Preservation for Text-to-Image Personalization**

First author: Li, Guandong. First submitted: 2026-02-15. Source: [arXiv:2602.13994](https://arxiv.org/abs/2602.13994). Checked: 2026-09-16.

Relation: **Internal**; topic: Subject and identity preservation. Secondary relations: External.

Restricts identity injection spatially and schedules it over denoising to reduce interference with background and prompt-driven content.

### 2602.13637 · DCDM

**DCDM: Divide-and-Conquer Diffusion Models for Consistency-Preserving Video Generation**

First author: Zhao, Haoyu. First submitted: 2026-02-14. Source: [arXiv:2602.13637](https://arxiv.org/abs/2602.13637). Checked: 2026-09-16.

Relation: **Internal**; topic: Multi-shot narratives and persistent memory. Secondary relations: External, Normative.

Separates intra-clip semantics, inter-clip camera control and inter-shot element persistence into complementary video-generation components.

### 2602.10113 · ConsID-Gen / ConsIDVid

**ConsID-Gen: View-Consistent and Identity-Preserving Image-to-Video Generation**

First author: Wu, Mingyang. First submitted: 2026-02-10. Source: [arXiv:2602.10113](https://arxiv.org/abs/2602.10113). Checked: 2026-09-16.

Relation: **Internal**; topic: Multi-view and geometric consistency. Secondary relations: External.

Augments image-to-video conditioning with auxiliary views and evaluates identity and geometry using the ConsIDVid data and benchmark.

### 2602.06195 · DeDPO

**DeDPO: Debiased Direct Preference Optimization for Diffusion Models**

First author: Pham, Khiem. First submitted: 2026-02-05. Source: [arXiv:2602.06195](https://arxiv.org/abs/2602.06195). Checked: 2026-09-16.

Relation: **Normative**; topic: Preference alignment and reward learning. Secondary relations: none recorded.

Corrects systematic bias in synthetic preference labels to combine limited human feedback with inexpensive AI annotations.

### 2602.02123 · MLV-Edit

**MLV-Edit: Towards Consistent and Highly Efficient Editing for Minute-Level Videos**

First author: Cao, Yangyi. First submitted: 2026-02-02. Source: [arXiv:2602.02123](https://arxiv.org/abs/2602.02123). Checked: 2026-09-16.

Relation: **External**; topic: Temporally consistent video editing. Secondary relations: Internal.

Uses flow blending at segment boundaries and attention anchors to reduce flicker and structural drift in minute-length editing.

### 2601.17756 · MV-S2V

**MV-S2V: Multi-View Subject-Consistent Video Generation**

First author: Song, Ziyang. First submitted: 2026-01-25. Source: [arXiv:2601.17756](https://arxiv.org/abs/2601.17756). Checked: 2026-09-16.

Relation: **Internal**; topic: Multi-view and geometric consistency. Secondary relations: External.

Uses multiple reference views and temporally shifted positional encoding to separate subject identity from reference viewpoint.

### 2601.15286 · Iterative refinement

**Iterative Refinement Improves Compositional Image Generation**

First author: Jaiswal, Shantanu. First submitted: 2026-01-21. Source: [arXiv:2601.15286](https://arxiv.org/abs/2601.15286). Checked: 2026-09-16.

Relation: **External**; topic: Compositionality and spatial grounding. Secondary relations: none recorded.

Uses a vision-language critic to guide sequential corrections of objects, attributes and relations during test-time generation.

### 2601.05572 · Generalized multi-image editing

**Towards Generalized Multi-Image Editing for Unified Multimodal Models**

First author: Xu, Pengcheng. First submitted: 2026-01-09. Source: [arXiv:2601.05572](https://arxiv.org/abs/2601.05572). Checked: 2026-09-16.

Relation: **External**; topic: Image editing and in-context generation. Secondary relations: Internal.

Disambiguates multiple input images through latent separators and image-index encoding; evaluates cross-image editing integration.

### 2601.00535 · FreeText

**FreeText: Training-Free Text Rendering in Diffusion Transformers via Attention Localization and Spectral Glyph Injection**

First author: Zhang, Ruiqiang. First submitted: 2026-01-02. Source: [arXiv:2601.00535](https://arxiv.org/abs/2601.00535). Checked: 2026-09-16.

Relation: **External**; topic: Typography and text rendering. Secondary relations: none recorded.

Separates text-region localization from glyph injection to improve visual text rendering without retraining the generator.

### 2512.19539 · StoryMem / ST-Bench

**StoryMem: Multi-shot Long Video Storytelling with Memory**

First author: Zhang, Kaiwen. First submitted: 2025-12-22. Source: [arXiv:2512.19539](https://arxiv.org/abs/2512.19539). Checked: 2026-09-16.

Relation: **Internal**; topic: Multi-shot narratives and persistent memory. Secondary relations: External.

Conditions iterative shot synthesis on selected historical keyframes and introduces ST-Bench for long-form storytelling evaluation.

### 2512.13392 · Beyond the Visible

**Beyond the Visible: Disocclusion-Aware Editing via Proxy Dynamic Graphs**

First author: Qi, Anran. First submitted: 2025-12-15. Source: [arXiv:2512.13392](https://arxiv.org/abs/2512.13392). Checked: 2026-09-16.

Relation: **External**; topic: Structural and camera control. Secondary relations: Internal.

Separates articulated motion from appearance editing to control newly revealed regions in image-to-video generation.

### 2510.27285 · S-GRACE

**Rethinking Robust Adversarial Concept Erasure in Diffusion Models**

First author: Yin, Qinghong. First submitted: 2025-10-31. Source: [arXiv:2510.27285](https://arxiv.org/abs/2510.27285). Checked: 2026-09-16.

Relation: **Normative**; topic: Safety, erasure and capability retention. Secondary relations: none recorded.

Uses semantic guidance during adversarial erasure training to improve concept coverage while limiting collateral changes.

### 2510.20822 · HoloCine

**HoloCine: Holistic Generation of Cinematic Multi-Shot Long Video Narratives**

First author: Meng, Yihao. First submitted: 2025-10-23. Source: [arXiv:2510.20822](https://arxiv.org/abs/2510.20822). Checked: 2026-09-16.

Relation: **Internal**; topic: Multi-shot narratives and persistent memory. Secondary relations: External.

Combines shot-local text conditioning with sparse inter-shot attention for jointly generated, coherent cinematic scenes.

### 2510.16888 · UniWorld-V2 / Edit-R1

**Uniworld-V2: Reinforce Image Editing with Diffusion Negative-aware Finetuning and MLLM Implicit Feedback**

First author: Li, Zongjian. First submitted: 2025-10-19. Source: [arXiv:2510.16888](https://arxiv.org/abs/2510.16888). Checked: 2026-09-16.

Relation: **Normative**; topic: Preference alignment and reward learning. Secondary relations: External, Internal.

Combines DiffusionNFT and multimodal-model feedback for post-training instruction editing, with filtering to reduce scoring noise.

### 2510.12784 · SRUM

**SRUM: Fine-Grained Self-Rewarding for Unified Multimodal Models**

First author: Jin, Weiyang. First submitted: 2025-10-14. Source: [arXiv:2510.12784](https://arxiv.org/abs/2510.12784). Checked: 2026-09-16.

Relation: **Normative**; topic: Preference alignment and reward learning. Secondary relations: External.

Uses a unified model's understanding branch to provide global and object-local feedback for its image-generation branch.

### 2510.02283 · Self-Forcing++

**Self-Forcing++: Towards Minute-Scale High-Quality Video Generation**

First author: Cui, Justin. First submitted: 2025-10-02. Source: [arXiv:2510.02283](https://arxiv.org/abs/2510.02283). Checked: 2026-09-16.

Relation: **Internal**; topic: Long-horizon video generation. Secondary relations: none recorded.

Supervises sampled segments of self-generated long videos to reduce error accumulation beyond short-teacher training horizons.

### 2509.22799 · VideoScore2 / VideoFeedback2

**VideoScore2: Think before You Score in Generative Video Evaluation**

First author: He, Xuan. First submitted: 2025-09-26. Source: [arXiv:2509.22799](https://arxiv.org/abs/2509.22799). Checked: 2026-09-16.

Relation: **Normative**; topic: Physical and causal evaluation. Secondary relations: External, Internal.

Produces interpretable assessments of visual quality, text alignment and physical or commonsense consistency using human-annotated video feedback.

### 2509.22622 · LongLive

**LongLive: Real-time Interactive Long Video Generation**

First author: Yang, Shuai. First submitted: 2025-09-26. Source: [arXiv:2509.22622](https://arxiv.org/abs/2509.22622). Checked: 2026-09-16.

Relation: **Internal**; topic: Long-horizon video generation. Secondary relations: External.

Combines long-rollout training, prompt-aware cache refresh and frame sinks to preserve consistency during interactive long-video generation.

### 2509.21433 · DyME / ErasureBench-H

**DyME: Dynamic Multi-Concept Erasure in Diffusion Models with Bi-Level Orthogonal LoRA Adaptation**

First author: Liu, Jiaqi. First submitted: 2025-09-25. Source: [arXiv:2509.21433](https://arxiv.org/abs/2509.21433). Checked: 2026-09-16.

Relation: **Normative**; topic: Safety, erasure and capability retention. Secondary relations: none recorded.

Composes concept-specific erasure adapters with orthogonality constraints and evaluates interference on a hierarchical erasure benchmark.

### 2509.16117 · DiffusionNFT

**DiffusionNFT: Online Diffusion Reinforcement with Forward Process**

First author: Zheng, Kaiwen. First submitted: 2025-09-19. Source: [arXiv:2509.16117](https://arxiv.org/abs/2509.16117). Checked: 2026-09-16.

Relation: **Normative**; topic: Preference alignment and reward learning. Secondary relations: External.

Contrasts positively and negatively rewarded generations in a forward-process objective without requiring reverse-trajectory likelihoods.

### 2508.17472 · T2I-ReasonBench

**T2I-ReasonBench: Benchmarking Reasoning-Informed Text-to-Image Generation**

First author: Sun, Kaiyue. First submitted: 2025-08-24. Source: [arXiv:2508.17472](https://arxiv.org/abs/2508.17472). Checked: 2026-09-16.

Relation: **External**; topic: Editing and reasoning evaluation. Secondary relations: Normative.

Separates reasoning accuracy from image quality across idioms, textual design, entity reasoning and scientific reasoning.

### 2508.02324 · Qwen-Image

**Qwen-Image Technical Report**

First author: Wu, Chenfei. First submitted: 2025-08-04. Source: [arXiv:2508.02324](https://arxiv.org/abs/2508.02324). Checked: 2026-09-16.

Relation: **External**; topic: Typography and text rendering. Secondary relations: Internal.

Combines multilingual text-rendering training with semantic and reconstructive image encodings for editing fidelity.

### 2506.18871 · OmniGen2

**OmniGen2: Towards Instruction-Aligned Multimodal Generation**

First author: Wu, Chenyuan. First submitted: 2025-06-23. Source: [arXiv:2506.18871](https://arxiv.org/abs/2506.18871). Checked: 2026-09-16.

Relation: **External**; topic: Image editing and in-context generation. Secondary relations: Internal.

Unifies generation, editing and in-context tasks; introduces OmniContext to evaluate reference-conditioned subject consistency.

### 2506.15742 · FLUX.1 Kontext

**FLUX.1 Kontext: Flow Matching for In-Context Image Generation and Editing in Latent Space**

First author: Black Forest Labs. First submitted: 2025-06-17. Source: [arXiv:2506.15742](https://arxiv.org/abs/2506.15742). Checked: 2026-09-16.

Relation: **External**; topic: Image editing and in-context generation. Secondary relations: Internal.

Uses joint text-image context for generation and iterative editing; KontextBench separates local edits, reference consistency and text editing.

### 2506.09612 · Asymmetry Zigzag Sampling

**Consistent Story Generation with Asymmetry Zigzag Sampling**

First author: Li, Mingxiao. First submitted: 2025-06-11. Source: [arXiv:2506.09612](https://arxiv.org/abs/2506.09612). Checked: 2026-09-16.

Relation: **Internal**; topic: Subject and identity preservation. Secondary relations: External.

Alternates asymmetric prompts and shared visual cues during training-free sampling to preserve subjects across story panels.

### 2506.08009 · Self Forcing

**Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion**

First author: Huang, Xun. First submitted: 2025-06-09. Source: [arXiv:2506.08009](https://arxiv.org/abs/2506.08009). Checked: 2026-09-16.

Relation: **Internal**; topic: Long-horizon video generation. Secondary relations: none recorded.

Trains on self-generated context to reduce exposure bias; long extrapolation still requires separate consistency evaluation.

### 2506.07977 · OneIG-Bench

**OneIG-Bench: Omni-dimensional Nuanced Evaluation for Image Generation**

First author: Chang, Jingjing. First submitted: 2025-06-09. Source: [arXiv:2506.07977](https://arxiv.org/abs/2506.07977). Checked: 2026-09-16.

Relation: **External**; topic: Editing and reasoning evaluation. Secondary relations: Normative.

Separates prompt alignment, rendered text, reasoning, style and diversity into selectable image-generation evaluation dimensions.

### 2506.03147 · UniWorld

**UniWorld: High-Resolution Semantic Encoders for Unified Visual Understanding and Generation**

First author: Lin, Bin. First submitted: 2025-06-03. Source: [arXiv:2506.03147](https://arxiv.org/abs/2506.03147). Checked: 2026-09-16.

Relation: **External**; topic: Image editing and in-context generation. Secondary relations: Internal.

Uses high-resolution semantic representations for unified perception, generation and image manipulation.

### 2506.02161 · TIIF-Bench

**TIIF-Bench: How Does Your T2I Model Follow Your Instructions?**

First author: Wei, Xinyu. First submitted: 2025-06-02. Source: [arXiv:2506.02161](https://arxiv.org/abs/2506.02161). Checked: 2026-09-16.

Relation: **External**; topic: Editing and reasoning evaluation. Secondary relations: none recorded.

Tests fine-grained instruction following across prompt complexity and length, including text rendering and style control.

### 2505.16707 · KRIS-Bench

**KRIS-Bench: Benchmarking Next-Level Intelligent Image Editing Models**

First author: Wu, Yongliang. First submitted: 2025-05-22. Source: [arXiv:2505.16707](https://arxiv.org/abs/2505.16707). Checked: 2026-09-16.

Relation: **External**; topic: Editing and reasoning evaluation. Secondary relations: Normative.

Organizes knowledge-based editing around factual, conceptual and procedural knowledge, with a knowledge-plausibility evaluation protocol.

### 2505.14683 · BAGEL

**Emerging Properties in Unified Multimodal Pretraining**

First author: Deng, Chaorui. First submitted: 2025-05-20. Source: [arXiv:2505.14683](https://arxiv.org/abs/2505.14683). Checked: 2026-09-16.

Relation: **External**; topic: Image editing and in-context generation. Secondary relations: Internal.

Unified multimodal pretraining supports image manipulation and future-frame prediction; relevant as a backbone rather than a dedicated consistency guarantee.

### 2505.07818 · DanceGRPO

**DanceGRPO: Unleashing GRPO on Visual Generation**

First author: Xue, Zeyue. First submitted: 2025-05-12. Source: [arXiv:2505.07818](https://arxiv.org/abs/2505.07818). Checked: 2026-09-16.

Relation: **Normative**; topic: Preference alignment and reward learning. Secondary relations: External, Internal.

Adapts group-relative policy optimization across diffusion and rectified-flow image and video generation tasks.

### 2504.20690 · IC-Edit

**In-Context Edit: Enabling Instructional Image Editing with In-Context Generation in Large Scale Diffusion Transformer**

First author: Zhang, Zechuan. First submitted: 2025-04-29. Source: [arXiv:2504.20690](https://arxiv.org/abs/2504.20690). Checked: 2026-09-16.

Relation: **External**; topic: Image editing and in-context generation. Secondary relations: Internal.

Uses in-context diffusion-transformer generation, lightweight adaptation and early candidate filtering for instruction-guided editing.

### 2504.17761 · Step1X-Edit

**Step1X-Edit: A Practical Framework for General Image Editing**

First author: Liu, Shiyu. First submitted: 2025-04-24. Source: [arXiv:2504.17761](https://arxiv.org/abs/2504.17761). Checked: 2026-09-16.

Relation: **External**; topic: Image editing and in-context generation. Secondary relations: Internal.

Combines multimodal instruction understanding with diffusion editing and introduces GEdit-Bench for real-user editing requests.

### 2504.16915 · DreamO

**DreamO: A Unified Framework for Image Customization**

First author: Mou, Chong. First submitted: 2025-04-23. Source: [arXiv:2504.16915](https://arxiv.org/abs/2504.16915). Checked: 2026-09-16.

Relation: **Internal**; topic: Subject and identity preservation. Secondary relations: External.

Routes reference features and task conditions in a unified diffusion transformer for identity, subject, style and background customization.

### 2504.12369 · WorldMem

**WORLDMEM: Long-term Consistent World Simulation with Memory**

First author: Xiao, Zeqi. First submitted: 2025-04-16. Source: [arXiv:2504.12369](https://arxiv.org/abs/2504.12369). Checked: 2026-09-16.

Relation: **Internal**; topic: Multi-shot narratives and persistent memory. Secondary relations: Normative.

Retrieves state-indexed visual memories to reconstruct previously visited scenes across viewpoint and temporal gaps.

### 2504.02826 · RISEBench

**Envisioning Beyond the Pixels: Benchmarking Reasoning-Informed Visual Editing**

First author: Zhao, Xiangyu. First submitted: 2025-04-03. Source: [arXiv:2504.02826](https://arxiv.org/abs/2504.02826). Checked: 2026-09-16.

Relation: **External**; topic: Editing and reasoning evaluation. Secondary relations: Internal, Normative.

Evaluates temporal, causal, spatial and logical editing instructions alongside appearance preservation and visual plausibility.

### 2504.02160 · UNO

**Less-to-More Generalization: Unlocking More Controllability by In-Context Generation**

First author: Wu, Shaojin. First submitted: 2025-04-02. Source: [arXiv:2504.02160](https://arxiv.org/abs/2504.02160). Checked: 2026-09-16.

Relation: **Internal**; topic: Subject and identity preservation. Secondary relations: External.

Builds consistent multi-subject training pairs and uses multi-image conditioning to preserve subjects under compositional control.

### 2503.21755 · VBench-2.0

**VBench-2.0: Advancing Video Generation Benchmark Suite for Intrinsic Faithfulness**

First author: Zheng, Dian. First submitted: 2025-03-27. Source: [arXiv:2503.21755](https://arxiv.org/abs/2503.21755). Checked: 2026-09-16.

Relation: **Normative**; topic: Physical and causal evaluation. Secondary relations: External, Internal.

Extends video evaluation toward human fidelity, controllability, creativity, physics and commonsense rather than appearance alone.

### 2503.15138 · VideoGen-of-Thought

**VideoGen-of-Thought: Step-by-step generating multi-shot video with minimal manual intervention**

First author: Zheng, Mingzhe. First submitted: 2025-03-19. Source: [arXiv:2503.15138](https://arxiv.org/abs/2503.15138). Checked: 2026-09-16.

Relation: **Internal**; topic: Multi-shot narratives and persistent memory. Secondary relations: External.

Combines storyline planning, identity-aware cross-shot propagation and latent transitions for coherent multi-shot video generation.

### 2503.10592 · CameraCtrl II

**CameraCtrl II: Dynamic Scene Exploration via Camera-controlled Video Diffusion Models**

First author: He, Hao. First submitted: 2025-03-13. Source: [arXiv:2503.10592](https://arxiv.org/abs/2503.10592). Checked: 2026-09-16.

Relation: **External**; topic: Structural and camera control. Secondary relations: Internal.

Extends camera-controlled video generation toward wider scene exploration while preserving dynamic content and inter-clip continuity.

### 2503.08280 · OminiControl2

**OminiControl2: Efficient Conditioning for Diffusion Transformers**

First author: Tan, Zhenxiong. First submitted: 2025-03-11. Source: [arXiv:2503.08280](https://arxiv.org/abs/2503.08280). Checked: 2026-09-16.

Relation: **External**; topic: Structural and camera control. Secondary relations: Internal.

Compresses condition tokens and reuses conditional features across denoising steps for efficient multi-condition image generation.

### 2501.13918 · VideoReward / VideoAlign

**Improving Video Generation with Human Feedback**

First author: Liu, Jie. First submitted: 2025-01-23. Source: [arXiv:2501.13918](https://arxiv.org/abs/2501.13918). Checked: 2026-09-16.

Relation: **Normative**; topic: Preference alignment and reward learning. Secondary relations: External, Internal.

Introduces multi-dimensional video preferences and reward modeling, with flow-based preference optimization and inference-time reward guidance.

### 2501.03847 · Diffusion as Shader

**Diffusion as Shader: 3D-aware Video Diffusion for Versatile Video Generation Control**

First author: Gu, Zekai. First submitted: 2025-01-07. Source: [arXiv:2501.03847](https://arxiv.org/abs/2501.03847). Checked: 2026-09-16.

Relation: **External**; topic: Structural and camera control. Secondary relations: Internal.

Uses 3D tracking videos as a common control interface for camera, motion and object manipulation with temporal correspondence.
