# HDR 论文与 IQA/VQA Reading List

> Last checked: 2026-09-09  
> Focus: SDR→HDR / inverse tone mapping, HDR video reconstruction, gain-map HDR, generative HDR, HDR IQA/VQA, subjective datasets and evaluation protocols.

Legend: **[P]** peer-reviewed paper · **[Preprint]** arXiv/preprint · **[D]** dataset/benchmark · **[M]** metric · **[S]** standard.

---

# 1. SDR → HDR / Single-Image Inverse Tone Mapping

## Foundational

### 1. HDR Image Reconstruction from a Single Exposure Using Deep CNNs — Eilertsen et al., ACM TOG / SIGGRAPH Asia 2017 **[P]**
- Authors: Gabriel Eilertsen, Joel Kronander, Gyorgy Denes, Rafał K. Mantiuk, Jonas Unger
- Key idea: learn to reconstruct saturated regions from a single exposure.
- Importance: foundational deep single-image HDR reconstruction / highlight hallucination work.
- Paper/code: https://github.com/gabrieleilertsen/hdrcnn

### 2. Single-Image HDR Reconstruction by Learning to Reverse the Camera Pipeline — Liu et al., CVPR 2020 **[P]**
- Authors: Yu-Lun Liu, Wei-Sheng Lai, Yu-Sheng Chen, Yi-Lung Kao, Ming-Hsuan Yang, Yung-Yu Chuang, Jia-Bin Huang
- Key idea: explicitly reverse clipping, camera response nonlinearity, and quantization with dedicated subnetworks.
- Why important: canonical physics-informed SDR/LDR→HDR formulation.
- Paper: https://openaccess.thecvf.com/content_CVPR_2020/html/Liu_Single-Image_HDR_Reconstruction_by_Learning_to_Reverse_the_Camera_Pipeline_CVPR_2020_paper.html
- Code: https://github.com/alex04072000/SingleHDR

## Recent structured / gain-map routes

### 3. Learning Gain Map for Inverse Tone Mapping — Liao et al., ICLR 2025 **[P]**
- Authors: Yinuo Liao, Yuanshen Guan, Ruikang Xu, Jiacheng Li, Shida Sun, Zhiwei Xiong
- Model: **GMNet**.
- Key idea: predict a Gain Map rather than directly predict HDR RGB; combines local contrast restoration and global luminance estimation.
- Data: synthetic SDR-GM pairs + real-world mobile-captured SDR-GM pairs.
- Relevance: strong evidence that structured HDR control representations remain competitive.
- Paper: https://proceedings.iclr.cc/paper_files/paper/2025/hash/43d2b7fbee8431f7cef0d0afed51c691-Abstract-Conference.html
- Code: https://github.com/qtlark/GMNet

### 4. HDR Image Generation via Gain Map Decomposed Diffusion — Guan et al., ICCV 2025 **[P]**
- Authors: Yuanshen Guan, Ruikang Xu, Yinuo Liao, Mingde Yao, Lizhi Wang, Zhiwei Xiong
- Key idea: represent HDR as SDR base + Gain Map and adapt diffusion around that decomposition.
- Relevance: useful middle path between deterministic gain-map mapping and unconstrained pixel-space HDR generation.
- Paper: https://openaccess.thecvf.com/content/ICCV2025/html/Guan_HDR_Image_Generation_via_Gain_Map_Decomposed_Diffusion_ICCV_2025_paper.html
- Code: https://github.com/Guanys-dar/GM-Diffusion

### 5. Gain-MLP: Improving HDR Gain Map Encoding via a Lightweight MLP — Canham et al., ICCV 2025 **[P]**
- Authors: Trevor D. Canham, SaiKiran Tedla, Michael J. Murdoch, Michael S. Brown
- Key idea: lightweight MLP encoding of HDR gain maps; fixed ~10 KB representation reported in the paper.
- Relevance: product-side HDR representation/encoding rather than SDR→HDR reconstruction itself.
- Paper: https://openaccess.thecvf.com/content/ICCV2025/html/Canham_Gain-MLP_Improving_HDR_Gain_Map_Encoding_via_a_Lightweight_MLP_ICCV_2025_paper.html

### 6. AIM 2025 Challenge on Inverse Tone Mapping: Report, Methods and Results — Wang et al., ICCV Workshops 2025 **[P][D]**
- Organizers/authors include Chao Wang, Francesco Banterle, Radu Timofte et al.
- Importance: one of the clearest recent public ITM benchmark snapshots.
- Evaluation uses HDR-aware/perceptually-uniform metrics such as PU21-domain measures.
- Paper: https://openaccess.thecvf.com/content/ICCV2025W/AIM/html/Wang_AIM_2025_challenge_on_Inverse_Tone_Mapping_Report_Methods_and_ICCVW_2025_paper.html

### 7. Boosting Inverse Tone Mapping via Diffusion Regularization — Lu et al., ICCV Workshops 2025 **[P]**
- Key idea: add diffusion regularization to ITM for saturated/missing regions.
- Paper: https://openaccess.thecvf.com/content/ICCV2025W/AIM/html/Lu_Boosting_Inverse_Tone_Mapping_via_Diffusion_Regularization_ICCVW_2025_paper.html

---

# 2. SDR → HDR, Real-World Generalization and Cinematic Grading

### 8. HDRMovieformer: A Transformer Framework and Benchmark for Cinematic SDR-to-HDR Conversion — Li et al., AAAI 2026 **[P][D]**
- Authors: Xianwei Li, Huiyuan Fu, Chuanming Wang, Huadong Ma
- Datasets: **HDRMovie7K** (professional DCDM SDR/HDR pairs) and HDRMovie1K.
- Key idea: luminance-guided attention + chroma refinement + wide-color-gamut loss.
- Importance: attacks a major weakness of synthetic HDR→TMO→SDR training by using professional SDR/HDR grading pairs.
- Paper: https://ojs.aaai.org/index.php/AAAI/article/view/37578

### 9. RealRep: Generalized SDR-to-HDR Conversion via Attribute-Disentangled Representation Learning — Xu et al., AAAI 2026 Oral **[P]**
- Authors: Li Xu, Siqi Wang, Kepeng Xu, Lin Zhang, Gang He, Weiran Wang, Yu-Wing Tai
- Key idea: disentangle luminance/chrominance degradation attributes and condition HDR mapping on degradation representation.
- Relevance: directly addresses the failure of assuming one fixed SDR generation/tone-mapping operator.
- Paper: https://ojs.aaai.org/index.php/AAAI/article/view/38111
- Code: https://github.com/kepengxu/RealRep

### 10. The xDR Dataset: A Cinematic Natively Graded HDR & SDR Dataset for Evaluation of Inverse Tone Mapping Methods — Luzardo et al., SPIC 2026 **[P][D]**
- Authors: Gonzalo Luzardo, Jan Aelterman, Hiep Luong, Wilfried Philips, Daniel Ochoa
- Data: 10 ~40 s FHD cinematic sequences, professionally graded independently in SDR and HDR while preserving artistic intent.
- Importance: strong warning against evaluating ITM only on synthetic TMO pairs.
- Paper: https://www.sciencedirect.com/science/article/pii/S0923596526000536

---

# 3. HDR Video Reconstruction / Temporal Information

## Alternating / multi-exposure capture

### 11. HDR Video Reconstruction: A Coarse-to-Fine Network and a Real-World Benchmark Dataset — Chen et al., ICCV 2021 **[P][D]**
- Authors: Guanying Chen, Chaofeng Chen, Shi Guo, Zhetong Liang, Kwan-Yee K. Wong, Lei Zhang
- Input: alternating-exposure LDR sequences.
- Key idea: coarse image-space alignment/merge followed by feature-space temporal fusion.
- Benchmark: real-world static/dynamic sequences + synthetic data.
- Paper: https://openaccess.thecvf.com/content/ICCV2021/html/Chen_HDR_Video_Reconstruction_A_Coarse-To-Fine_Network_and_a_Real-World_Benchmark_ICCV_2021_paper.html
- Code: https://github.com/guanyingc/DeepHDRVideo
- Dataset: https://github.com/guanyingc/DeepHDRVideo-Dataset

### 12. HDRFlow: Real-Time HDR Video Reconstruction with Large Motions — Xu et al., CVPR 2024 **[P]**
- Authors: Gangwei Xu, Yujin Wang, Jinwei Gu, Tianfan Xue, Xin Yang
- Input: alternating exposures.
- Key idea: HDR-oriented flow, HDR alignment loss, efficient large-motion flow estimation.
- Reported runtime: 720p at ~25 ms.
- Paper: https://openaccess.thecvf.com/content/CVPR2024/html/Xu_HDRFlow_Real-Time_HDR_Video_Reconstruction_with_Large_Motions_CVPR_2024_paper.html
- Code: https://github.com/OpenImagingLab/HDRFlow

> Note: these two papers receive **physically complementary exposures** and should not be directly compared with same-EV compressed SDR→HDR video.

## Same-video / inverse-tone-mapping temporal clues

### 13. Deep Video Inverse Tone Mapping Based on Temporal Clues — Ye et al., CVPR 2024 **[P]**
- Authors: Yuyao Ye, Ning Zhang, Yang Zhao, Hongbin Cao, Ronggang Wang
- Key idea: Global Sample + Local Propagate; search and propagate useful temporal clues for over-exposed areas.
- Relevance to same-EV video: much closer than alternating-exposure HDR, because temporal information is mined from ordinary video rather than an exposure bracket sequence.
- Paper: https://openaccess.thecvf.com/content/CVPR2024/html/Ye_Deep_Video_Inverse_Tone_Mapping_Based_on_Temporal_Clues_CVPR_2024_paper.html
- Code: https://github.com/ye3why/VITM-TC

---

# 4. Generative HDR / Foundation-Model Direction

### 14. LumaFlux: Lifting 8-Bit Worlds to HDR Reality with Physically-Guided Diffusion Transformers — Saini et al., 2026 **[Preprint]**
- Authors: Shreshth Saini, Hakan Gedik, Neil Birkbeck, Yilin Wang, Balu Adsumilli, Alan C. Bovik
- Input/output: 8-bit BT.709 SDR → 10-bit PQ/BT.2020 HDR.
- Key idea: frozen FLUX backbone + physical cues + perceptual features + monotone tone-field decoder.
- Video: uses inference-time stabilization rather than a dedicated temporal network; project reports reduced excess flicker.
- Important engineering note: training pipeline itself still uses a large synthetic SDR degradation corpus (multiple TMOs + codec round trips), so it does not eliminate synthetic-domain concerns.
- Paper/project/code: https://shreshthsaini.github.io/LumaFlux/ · https://github.com/shreshthsaini/LumaFlux

### 15. Generating HDR Video from SDR Video — Tedla et al., 2026 **[Preprint]**
- Authors: SaiKiran Tedla, Francesco Banterle, Trevor Canham, Karanpreet Raja, David B. Lindell, Kiriakos N. Kutulakos, Jiacheng Li, Feiran Li, Daisuke Iso
- Key idea: **MEVM** predicts exposure-bracketed linear SDR video from one nonlinear SDR video; **VMM** merges generated brackets into HDR.
- Interpretation: generated ±EV brackets are priors/inference, not physically captured exposure measurements.
- Relevance: represents the strongest “missing information should be plausibly generated” position.
- Paper: https://arxiv.org/abs/2605.14703
- Project: https://sdr2hdrvideo.github.io/

### 16. LumaGuide: Distribution Shaping for Training-Free HDR Generation in Diffusion Models — Chen et al., 2026 **[Preprint]**
- Authors: Bowen Chen, Shreshth Saini, Balu Adsumilli, Alan C. Bovik
- Key idea: training-free sampling guidance that matches target luminance distributions in perceptually uniform PQ space.
- Relevance: HDR generation as controllable distribution shaping rather than a fixed trained mapping.
- Paper: https://arxiv.org/abs/2607.26237

---

# 5. HDR IQA / VQA / Perceptual Metrics

## Full-reference perceptual metrics

### 17. HDR-VDP-3: A Multi-Metric for Predicting Image Differences, Quality and Contrast Distortions in HDR and Regular Content — Mantiuk et al., 2023 **[Preprint][M]**
- Authors: Rafał K. Mantiuk, Dounia Hammou, Param Hanji
- Type: full-reference perceptual metric.
- Outputs: visual differences, quality and contrast distortion prediction across SDR/HDR luminance ranges.
- Paper: https://arxiv.org/abs/2304.13625

### 18. ColorVideoVDP: A Visual Difference Predictor for Image, Video and Display Distortions — Mantiuk et al., SIGGRAPH 2024 **[P][M]**
- Authors: Rafał K. Mantiuk, Param Hanji, Maliha Ashraf, Yuta Asano, Alexandre Chapiro
- Type: full-reference image/video metric.
- Key features: luminance + chroma, spatial + temporal vision, explicit display model, SDR/PQ/HLG support.
- Strong recommendation for HDR-video evaluation when a trustworthy HDR reference exists.
- Paper: https://arxiv.org/abs/2401.11485
- Code: https://github.com/gfxdisp/ColorVideoVDP

### 19. Perceptual Assessment and Optimization of HDR Image Rendering — Cao et al., CVPR 2024 **[P][M]**
- Authors: Peibei Cao, Rafał K. Mantiuk, Kede Ma
- Key idea: inverse-display decomposition of HDR into multiple LDR exposure slices, then reuse modern LDR quality metrics.
- Reported to outperform existing metrics across four HDR IQA datasets.
- Paper: https://openaccess.thecvf.com/content/CVPR2024/html/Cao_Perceptual_Assessment_and_Optimization_of_HDR_Image_Rendering_CVPR_2024_paper.html
- Code: https://github.com/cpb68/HDRQA

### 20. Adapting Quality Metrics to Tone Mapping — Chen et al., SIGGRAPH 2026 **[P][M][D]**
- Authors: Kenneth Chen, Dongyeon Kim, Yuta Asano, Alexandre Chapiro, Qi Sun, Rafał K. Mantiuk
- Key idea: properly model HDR/SDR display photometry and map both into a perceptually uniform representation before applying general-purpose metrics.
- Introduces/adapts **ColorVideoVDP-tm** for tone-mapping evaluation.
- Important conclusion: well-adapted general metrics can outperform older tone-mapping-specific metrics.
- DOI/project/code: https://doi.org/10.1145/3799902.3811107 · https://github.com/NYU-ICL/TM-metric-adaptation

## No-reference / learned HDR VQA

### 21. HIDRO-VQA: High Dynamic Range Oracle for Video Quality Assessment — Saini et al., WACV Workshops 2024 **[P][M]**
- Authors: Shreshth Saini, Avinab Saha, Alan C. Bovik
- Type: no-reference HDR VQA representation.
- Key idea: self-supervised contrastive fine-tuning transfers SDR quality-aware representations into HDR.
- Paper: https://openaccess.thecvf.com/content/WACV2024W/VAQ/html/Saini_HIDRO-VQA_High_Dynamic_Range_Oracle_for_Video_Quality_Assessment_WACVW_2024_paper.html
- Code: https://github.com/avinabsaha/HIDRO-VQA

### 22. HDR or SDR? A Subjective and Objective Study of Scaled and Compressed Videos — Ebenezer et al., IEEE TIP 2024 **[P][D][M]**
- Key result: HDR is not automatically preferred; preference depends on display, bitrate and scaling.
- Data: 356 videos, >23k ratings, 67 viewers, multiple TV technologies.
- Introduces HDRPatchMAX NR model.
- Dataset/info: https://www.colorado.edu/lab/live/live-hdr-vs-sdr-video-quality-assessment-database

### 23. CHUG: Crowdsourced User-Generated HDR Video Quality Dataset — Saini et al., ICIP 2025 **[P][D]**
- 856 UGC-HDR sources → 5,992 videos.
- 211,848 subjective ratings.
- Focus: realistic UGC compression/resolution distortions.
- Data/code: https://github.com/shreshthsaini/CHUG

### 24. HDRSDR-VQA: A Subjective Video Quality Dataset for HDR and SDR Comparative Evaluation — Chen et al., 2025 **[Preprint/Dataset; later PCS 2025 version]**
- Authors: Bowen Chen, Cheng-han Lee, Yixu Chen, Zaixi Shang, Hai Wei, Alan C. Bovik
- 960 videos from 54 sources, HDR and SDR, nine distortion levels.
- 145 participants, six consumer HDR-capable TVs, >22,000 pairwise comparisons, JOD scaling.
- Important for **display-aware HDR-vs-SDR preference**, not only absolute HDR MOS.
- Paper: https://arxiv.org/abs/2505.21831
- Dataset: https://www.colorado.edu/lab/live/live-paired-comparison-hdr-vs-sdr-database

### 25. BrightRate: Quality Assessment for User-Generated HDR Videos — Saini et al., WACV 2026 **[P][D][M]**
- Authors: Shreshth Saini, Bowen Chen, Yilin Wang, Neil Birkbeck, Balu Adsumilli, Alan C. Bovik
- Dataset: BrightVQ, 2,100 videos, 73,794 perceptual ratings.
- Model targets both UGC distortions and HDR-specific artifacts.
- Paper: https://openaccess.thecvf.com/content/WACV2026/html/Saini_BrightRate_Quality_Assessment_for_User-Generated_HDR_Videos_WACV_2026_paper.html

### 26. Seeing Beyond 8bits: Subjective and Objective Quality Assessment of HDR-UGC Videos — Saini et al., 2026 **[Preprint / CVPR 2026 project][D][M]**
- Authors: Shreshth Saini, Bowen Chen, Neil Birkbeck, Yilin Wang, Balu Adsumilli, Alan C. Bovik
- Dataset: ~44K HDR-UGC videos from ~6.5K sources, >1.5M crowd ratings reported in paper.
- Model: **HDR-Q**, an HDR-aware multimodal large language model for HDR-UGC VQA.
- HAPO: HDR-aware policy optimization intended to force reasoning to rely on HDR cues rather than SDR-only priors.
- Paper: https://arxiv.org/abs/2603.00938
- Data/project: https://github.com/shreshthsaini/Beyond8Bits

---

# 6. Standards and HDR Evaluation References

### 27. ITU-R BT.2100-3 — Image parameter values for HDR television **[S]**
- Defines HDR-TV system parameters including PQ and HLG.
- Official: https://www.itu.int/rec/R-REC-BT.2100

### 28. ITU-R BT.2408-9 — Operational practices in HDR television production **[S]**
- Useful for HDR/SDR conversion, reference white and operational workflows.
- Official: https://www.itu.int/pub/R-REP-BT.2408

### 29. ITU-R BT.2124 — Objective metric for HDR/WCG color difference (ΔE_ITP) **[S]**
- Important color-difference metric for HDR/WCG evaluation.
- Official: https://www.itu.int/rec/R-REC-BT.2124

---

# 7. Recommended Reading Order for Mobile Same-EV SDR Video → HDR

## First priority
1. **Single-Image HDR Reconstruction by Learning to Reverse the Camera Pipeline** — understand information loss / physical inverse formulation.
2. **Deep Video Inverse Tone Mapping Based on Temporal Clues** — understand what temporal evidence can contribute in ordinary video.
3. **GMNet** — structured Gain Map output instead of unconstrained HDR RGB.
4. **RealRep** — real-SDR degradation/domain generalization.
5. **HDRMovieformer + xDR dataset** — why real/professional SDR/HDR pairs matter.

## Evaluation priority
6. **ColorVideoVDP** — reference video HDR perceptual metric.
7. **HDRQA CVPR 2024** — HDR luminance-range-aware IQA.
8. **HDR or SDR? + HDRSDR-VQA** — display dependence and whether HDR is actually perceived as better.
9. **BrightRate / Beyond8Bits** — HDR-native no-reference VQA and HDR quality reasoning.

## Exploratory generative direction
10. **LumaFlux**.
11. **Generating HDR Video from SDR Video**.
12. **LumaGuide**.

---

# 8. Key Research Questions to Keep Separate

1. **True reconstruction vs plausible HDR rendering** — clipped 8-bit SDR does not uniquely determine original scene radiance.
2. **Same-EV temporal evidence vs exposure-bracket information** — ordinary adjacent frames are not equivalent to multi-exposure capture.
3. **Temporal stabilization vs temporal information recovery** — EMA of gain/tone maps solves flicker; it does not recover missing texture from neighbor frames.
4. **Synthetic SDR generation vs real camera domain** — synthetic TMO pairs are useful but do not prove target-device generalization.
5. **HDR signal compliance vs HDR quality** — PQ/BT.2020/HDR10 encoding correctness does not prove perceptual or reconstruction quality.
6. **Reference evaluation vs no-reference deployment evaluation** — HDR-VDP-3/ColorVideoVDP require an appropriate reference; HDR-Q/BrightRate/HIDRO-VQA address different use cases.
