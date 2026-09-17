# Additional literature batch 01 · papers 1–20

> Part of the 200-paper literature expansion for the survey repository.

## External consistency

- **[CPAM: Context-Preserving Adaptive Manipulation for Zero-Shot Real Image Editing](https://arxiv.org/abs/2506.18438)** — arXiv 2025 · Method + Benchmark. Adapts self-attention and localized cross-attention to preserve object identity and background during non-rigid editing; introduces IMBA.
## Internal consistency

- **[A$^2$RD: Agentic Autoregressive Diffusion for Long Video Consistency](https://arxiv.org/abs/2605.06924)** — arXiv 2026 · Method + Benchmark. Uses multimodal memory and segment-level refinement to limit long-video semantic drift; introduces LVBench-C.
- **[Stream4D: 4D-Consistency for Streaming Autoregressive Diffusion Video Models](https://arxiv.org/abs/2608.19556)** — arXiv 2026 · Method. Combines a dynamic 4D reconstruction reward with motion priors to discourage drift without rewarding frozen videos.
## External consistency

- **[HiCoGen: Hierarchical Compositional Text-to-Image Generation in Diffusion Models via Reinforcement Learning](https://arxiv.org/abs/2511.19965)** — arXiv 2025 · Method + Benchmark. Decomposes complex prompts into iterative synthesis units and optimizes subject, relation and global alignment with hierarchical rewards.
- **[MCCD: Multi-Agent Collaboration-based Compositional Diffusion for Complex Text-to-Image Generation](https://arxiv.org/abs/2505.02648)** — arXiv 2025 · Method. Combines multi-agent scene parsing with hierarchical regional diffusion to reduce errors in complex object compositions.
- **[Edge-Aware Image Manipulation via Diffusion Models with a Novel Structure-Preservation Loss](https://arxiv.org/abs/2601.16645)** — arXiv 2026 · Method. Introduces a local-linear structure-preservation loss and localization strategies for edge-faithful diffusion editing.
- **[Synthetic Curriculum Reinforces Compositional Text-to-Image Generation](https://arxiv.org/abs/2511.18378)** — arXiv 2025 · Method. Builds scene-graph curricula for reinforcement learning of object, attribute and relation composition.
## Internal consistency

- **[Dual-Expert Consistency Model for Efficient and High-Quality Video Generation](https://openaccess.thecvf.com/content/ICCV2025/html/Lv_Dual-Expert_Consistency_Model_for_Efficient_and_High-Quality_Video_Generation_ICCV_2025_paper.html)** — ICCV 2025 · Method. Separates semantic and detail experts during distillation and uses temporal-coherence losses to retain motion consistency in few-step video generation.
## External consistency

- **[Stable Flow: Vital Layers for Training-Free Image Editing](https://openaccess.thecvf.com/content/CVPR2025/html/Avrahami_Stable_Flow_Vital_Layers_for_Training-Free_Image_Editing_CVPR_2025_paper.html)** — CVPR 2025 · Method. Identifies vital DiT layers for selective feature injection and controlled real-image edits with improved inversion.
## Internal consistency

- **[ConsistentCity: Semantic Flow-guided Occupancy DiT for Temporally Consistent Driving Scene Synthesis](https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_ConsistentCity_Semantic_Flow-guided_Occupancy_DiT_for_Temporally_Consistent_Driving_Scene_ICCV_2025_paper.html)** — ICCV 2025 · Method. Uses semantic-flow-guided occupancy diffusion to provide temporally coherent structure for driving video synthesis.
- **[Free4D: Tuning-free 4D Scene Generation with Spatial-Temporal Consistency](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_Free4D_Tuning-free_4D_Scene_Generation_with_Spatial-Temporal_Consistency_ICCV_2025_paper.html)** — ICCV 2025 · Method. Combines point-guided denoising and latent replacement to construct spatially and temporally consistent 4D scenes from one image.
## External consistency

- **[SwiftEdit: Lightning Fast Text-Guided Image Editing via One-Step Diffusion](https://openaccess.thecvf.com/content/CVPR2025/html/Nguyen_SwiftEdit_Lightning_Fast_Text-Guided_Image_Editing_via_One-Step_Diffusion_CVPR_2025_paper.html)** — CVPR 2025 · Method. Pairs one-step inversion with mask-guided attention rescaling to localize text-guided edits.
- **[LiON-LoRA: Rethinking LoRA Fusion to Unify Controllable Spatial and Temporal Generation for Video Diffusion](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_LiON-LoRA_Rethinking_LoRA_Fusion_to_Unify_Controllable_Spatial_and_Temporal_ICCV_2025_paper.html)** — ICCV 2025 · Method. Uses orthogonality and norm-consistent LoRA fusion to decouple camera and object motion controls.
- **[AnyPortal: Zero-Shot Consistent Video Background Replacement](https://openaccess.thecvf.com/content/ICCV2025/html/Gao_AnyPortal_Zero-Shot_Consistent_Video_Background_Replacement_ICCV_2025_paper.html)** — ICCV 2025 · Method. Combines video priors and relighting with refinement projection to retain foreground details during background replacement.
## Internal consistency

- **[Multi-focal Conditioned Latent Diffusion for Person Image Synthesis](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_Multi-focal_Conditioned_Latent_Diffusion_for_Person_Image_Synthesis_CVPR_2025_paper.html)** — CVPR 2025 · Method. Aggregates pose-invariant facial and texture conditions to preserve identity and clothing in person synthesis.
## External consistency

- **[h-Edit: Effective and Flexible Diffusion-Based Editing via Doob's h-Transform](https://openaccess.thecvf.com/content/CVPR2025/html/Nguyen_h-Edit_Effective_and_Flexible_Diffusion-Based_Editing_via_Doobs_h-Transform_CVPR_2025_paper.html)** — CVPR 2025 · Method. Separates reconstruction and editing updates through Doob's h-transform, enabling joint textual and reward-guided edits.
## Normative consistency

- **[PhyS-EdiT: Physics-aware Semantic Image Editing with Text Description](https://openaccess.thecvf.com/content/CVPR2025/html/Cai_PhyS-EdiT_Physics-aware_Semantic_Image_Editing_with_Text_Description_CVPR_2025_paper.html)** — CVPR 2025 · Method + Dataset. Jointly controls material, illumination and semantics with a synthetic disentanglement dataset for physically grounded editing.
- **[Erasing More Than Intended? How Concept Erasure Degrades the Generation of Non-Target Concepts](https://openaccess.thecvf.com/content/ICCV2025/html/Amara_Erasing_More_Than_Intended_How_Concept_Erasure_Degrades_the_Generation_ICCV_2025_paper.html)** — ICCV 2025 · Benchmark + Evaluation study. Evaluates spillover degradation after concept removal across visually, semantically and compositionally related non-target concepts.
- **[SuMa: A Subspace Mapping Approach for Robust and Effective Concept Erasure in Text-to-Image Diffusion Models](https://openaccess.thecvf.com/content/ICCV2025/html/Nguyen_SuMa_A_Subspace_Mapping_Approach_for_Robust_and_Effective_Concept_ICCV_2025_paper.html)** — ICCV 2025 · Method. Maps target concept subspaces to reference subspaces to balance fine-grained erasure and neighboring-concept retention.
## External consistency

- **[Through-The-Mask: Mask-based Motion Trajectories for Image-to-Video Generation](https://openaccess.thecvf.com/content/CVPR2025/html/Yariv_Through-The-Mask_Mask-based_Motion_Trajectories_for_Image-to-Video_Generation_CVPR_2025_paper.html)** — CVPR 2025 · Method + Benchmark. Uses mask-based motion trajectories and object-level attention to align multi-object motion and appearance; introduces SA-V-128.

[Back to additional-paper index](../additional-papers-200.md)
