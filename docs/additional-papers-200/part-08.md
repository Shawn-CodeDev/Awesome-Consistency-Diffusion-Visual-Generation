# Additional literature batch 08 · papers 141–160

> Part of the 200-paper literature expansion for the survey repository.

## Normative consistency

- **[FairHuman: Boosting Hand and Face Quality in Human Image Generation with Minimum Potential Delay Fairness in Diffusion Models](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_FairHuman_Boosting_Hand_and_Face_Quality_in_Human_Image_Generation_ICCV_2025_paper.html)** — ICCV 2025 · Method. Balances global, hand, and face objectives to improve local anatomical plausibility; fairness here concerns optimization objectives, not demographic parity.
- **[Enhancing Reward Models for High-quality Image Generation: Beyond Text-Image Alignment](https://openaccess.thecvf.com/content/ICCV2025/html/Ba_Enhancing_Reward_Models_for_High-quality_Image_Generation_Beyond_Text-Image_Alignment_ICCV_2025_paper.html)** — ICCV 2025 · Evaluator + Method. Separates text-content coverage from image-only high-preference scoring to study aesthetic detail beyond text-image similarity.
- **[V.I.P. : Iterative Online Preference Distillation for Efficient Video Diffusion Models](https://openaccess.thecvf.com/content/ICCV2025/html/Kim_V.I.P.__Iterative_Online_Preference_Distillation_for_Efficient_Video_Diffusion_ICCV_2025_paper.html)** — ICCV 2025 · Method. Uses online preference-pair curation and preference distillation to retain desired video properties under model compression.
- **[Taming Preference Mode Collapse via Directional Decoupling Alignment in Diffusion Reinforcement Learning](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Taming_Preference_Mode_Collapse_via_Directional_Decoupling_Alignment_in_Diffusion_CVPR_2026_paper.html)** — CVPR 2026 · Method. Corrects reward directions in embedding space to reduce preference mode collapse while maintaining generation diversity.
## Internal consistency

- **[Diffusion Self-Distillation for Zero-Shot Customized Image Generation](https://openaccess.thecvf.com/content/CVPR2025/html/Cai_Diffusion_Self-Distillation_for_Zero-Shot_Customized_Image_Generation_CVPR_2025_paper.html)** — CVPR 2025 · Method + Dataset. Curates paired image data from a model's in-context generations to learn reference-conditioned, identity-preserving customization.
- **[DiffSensei: Bridging Multi-Modal LLMs and Diffusion Models for Customized Manga Generation](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_DiffSensei_Bridging_Multi-Modal_LLMs_and_Diffusion_Models_for_Customized_Manga_CVPR_2025_paper.html)** — CVPR 2025 · Method + Dataset. Combines character-conditioned diffusion with multimodal identity adaptation to preserve characters across text-directed manga panels.
## Normative consistency

- **[Black Hole-Driven Identity Absorbing in Diffusion Models](https://openaccess.thecvf.com/content/CVPR2025/html/Shaheryar_Black_Hole-Driven_Identity_Absorbing_in_Diffusion_Models_CVPR_2025_paper.html)** — CVPR 2025 · Method. Studies identity erasure in diffusion bottleneck features while avoiding unrealistic outputs from arbitrary latent-space directions.
## Internal consistency

- **[HiFi-Portrait: Zero-shot Identity-preserved Portrait Generation with High-fidelity Multi-face Fusion](https://openaccess.thecvf.com/content/CVPR2025/html/Xu_HiFi-Portrait_Zero-shot_Identity-preserved_Portrait_Generation_with_High-fidelity_Multi-face_Fusion_CVPR_2025_paper.html)** — CVPR 2025 · Method. Fuses multiple reference-face features with identity-aware landmarks to balance portrait identity and attribute control.
## Normative consistency

- **[Physical Simulator In-the-Loop Video Generation](https://openaccess.thecvf.com/content/CVPR2026/html/Foo_Physical_Simulator_In-the-Loop_Video_Generation_CVPR_2026_paper.html)** — CVPR 2026 · Method. Reconstructs simulated object trajectories from an initial video and uses simulator correspondences to guide motion and texture consistency.
## Internal consistency

- **[GaussianIP: Identity-Preserving Realistic 3D Human Generation via Human-Centric Diffusion Prior](https://openaccess.thecvf.com/content/CVPR2025/html/Tang_GaussianIP_Identity-Preserving_Realistic_3D_Human_Generation_via_Human-Centric_Diffusion_Prior_CVPR_2025_paper.html)** — CVPR 2025 · Method. Uses human-centric diffusion distillation to generate 3D people consistent with image-based identity and text conditions.
- **[PSHuman: Photorealistic Single-image 3D Human Reconstruction using Cross-Scale Multiview Diffusion and Explicit Remeshing](https://openaccess.thecvf.com/content/CVPR2025/html/Li_PSHuman_Photorealistic_Single-image_3D_Human_Reconstruction_using_Cross-Scale_Multiview_Diffusion_CVPR_2025_paper.html)** — CVPR 2025 · Method. Couples global-body and local-face diffusion with body priors to generate identity-preserving, anatomically compatible multiple views.
- **[MagicMirror: ID-Preserved Video Generation in Video Diffusion Transformers](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_MagicMirror_ID-Preserved_Video_Generation_in_Video_Diffusion_Transformers_ICCV_2025_paper.html)** — ICCV 2025 · Method. Combines facial identity and structure features with conditioned normalization to preserve identity without suppressing natural video motion.
- **[Identity-Preserving Text-to-Video Generation by Frequency Decomposition](https://openaccess.thecvf.com/content/CVPR2025/html/Yuan_Identity-Preserving_Text-to-Video_Generation_by_Frequency_Decomposition_CVPR_2025_paper.html)** — CVPR 2025 · Method. Separates low-frequency facial structure and high-frequency identity features for identity-conditioned video diffusion.
- **[Multi-View Image Diffusion via Coordinate Noise and Fourier Attention](https://openaccess.thecvf.com/content/WACV2025/html/Theiss_Multi-View_Image_Diffusion_via_Coordinate_Noise_and_Fourier_Attention_WACV_2025_paper.html)** — WACV 2025 · Method. Combines coordinate-correlated noise, Fourier attention, and cross-attention alignment for coherent multi-view image synthesis.
- **[FaceLift: Learning Generalizable Single Image 3D Face Reconstruction from Synthetic Heads](https://openaccess.thecvf.com/content/ICCV2025/html/Lyu_FaceLift_Learning_Generalizable_Single_Image_3D_Face_Reconstruction_from_Synthetic_ICCV_2025_paper.html)** — ICCV 2025 · Method + Dataset. Uses synthetic head supervision and input reconstruction to generate consistent side and back views before Gaussian reconstruction.
- **[MOSAIC: Generating Consistent, Privacy-Preserving Scenes from Multiple Depth Views in Multi-Room Environments](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_MOSAIC_Generating_Consistent_Privacy-Preserving_Scenes_from_Multiple_Depth_Views_in_ICCV_2025_paper.html)** — ICCV 2025 · Method. Optimizes overlapping depth-conditioned views jointly to generate cross-view-compatible indoor scenes without using source RGB appearance.
## Normative consistency

- **[When Safety Collides: Resolving Multi-Category Harmful Conflicts in Text-to-Image Diffusion via Adaptive Safety Guidance](https://openaccess.thecvf.com/content/CVPR2026/html/Xiang_When_Safety_Collides_Resolving_Multi-Category_Harmful_Conflicts_in_Text-to-Image_Diffusion_CVPR_2026_paper.html)** — CVPR 2026 · Method. Adapts category-specific safety guidance to mitigate conflicts in which suppressing one harmful category amplifies another.
## Internal consistency

- **[MagicCity: Geometry-Aware 3D City Generation from Satellite Imagery with Multi-View Consistency](https://openaccess.thecvf.com/content/ICCV2025/html/Yao_MagicCity_Geometry-Aware_3D_City_Generation_from_Satellite_Imagery_with_Multi-View_ICCV_2025_paper.html)** — ICCV 2025 · Method. Combines satellite-derived geometry and texture with inter-frame cross-attention for consistent city-scale multi-view generation.
- **[HouseCrafter: Lifting Floorplans to 3D Scenes with 2D Diffusion Models](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_HouseCrafter_Lifting_Floorplans_to_3D_Scenes_with_2D_Diffusion_Models_ICCV_2025_paper.html)** — ICCV 2025 · Method. Conditions autoregressive RGB-D diffusion on a global floorplan and earlier views to maintain house-scale scene consistency.
## Normative consistency

- **[AutoPrompt: Automated Red-Teaming of Text-to-Image Models via LLM-Driven Adversarial Prompts](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_AutoPrompt_Automated_Red-Teaming_of_Text-to-Image_Models_via_LLM-Driven_Adversarial_Prompts_ICCV_2025_paper.html)** — ICCV 2025 · Method + Evaluation study. Studies black-box automated adversarial-prompt generation as a stress test of text-to-image safety mechanisms.

[Back to additional-paper index](../additional-papers-200.md)
