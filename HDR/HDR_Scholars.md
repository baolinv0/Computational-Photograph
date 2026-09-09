# HDR 相关学者与团队 Watchlist

> Last checked: 2026-09-09  
> Scope: SDR→HDR / inverse tone mapping (ITM), HDR video reconstruction, gain-map HDR, HDR image/video quality assessment (IQA/VQA), perceptual display metrics, generative HDR.

## 目录

- [1. Core Watchlist](#core-watchlist)
- [2. Industry / Platform HDR Quality Line](#industry-platform-line)
- [3. Recommended Tracking Priority for Mobile Video HDR](#tracking-priority)
  - [Tier A — current SDR-video→HDR project](#tier-a)
  - [Tier B — capture-side / multi-exposure HDR](#tier-b)
  - [Tier C — foundational single-image HDR](#tier-c)
- [4. Primary Links](#primary-links)
- [5. Notes](#notes)

---

<a id="core-watchlist"></a>
## 1. Core Watchlist

| Scholar / Team | Main affiliation / research line | HDR focus | Representative work | Why follow |
|---|---|---|---|---|
| **Alan C. Bovik** | LIVE Lab; perceptual image/video quality | HDR-VQA, UGC-HDR, subjective quality, MLLM quality reasoning | *HDR or SDR?* (TIP 2024); *BrightRate* (WACV 2026); *Seeing Beyond 8bits* (2026); *LumaFlux* (2026) | One of the strongest long-term perception/IQA lines; recent work connects HDR quality models with foundation/generative models. |
| **Shreshth Saini** | LIVE / HDR quality + generative media | HDR-VQA, HDR datasets, SDR→HDR generative conversion | *HIDRO-VQA* (2024); *CHUG* (ICIP 2025); *BrightRate* (WACV 2026); *Beyond8Bits / HDR-Q* (2026); *LumaFlux* (2026) | Continuous HDR research line from quality representation → large-scale HDR-UGC → HDR reasoning → generation. |
| **Bowen Chen** | LIVE / HDR subjective quality | HDR-vs-SDR preference, HDR reasoning, controllable HDR generation | *HDRSDR-VQA* (2025); *Beyond8Bits / HDR-Q* (2026); *LumaGuide* (2026) | Important for display-aware HDR quality and evaluator→generator/control transition. |
| **Rafał K. Mantiuk** | University of Cambridge, Graphics & Display group | HDR perception, visual difference metrics, display modeling, tone-mapping evaluation | *HDR-VDP-3* (2023); *ColorVideoVDP* (SIGGRAPH 2024); *Perceptual Assessment and Optimization of HDR Image Rendering* (CVPR 2024); *Adapting Quality Metrics to Tone Mapping* (SIGGRAPH 2026) | Core authority for HDR perceptual metrics and display-condition-aware evaluation. |
| **Peibei Cao** | HDR perceptual quality | HDR IQA, exposure-stack based perceptual assessment | *Perceptual Assessment and Optimization of HDR Image Rendering* (CVPR 2024) | Directly relevant to HDR-native IQA and luminance-range-aware quality decomposition. |
| **Kede Ma** | perceptual IQA / image quality | HDR perceptual optimization | *Perceptual Assessment and Optimization of HDR Image Rendering* (CVPR 2024) | Strong general IQA background; useful bridge between modern IQA and HDR rendering. |
| **Francesco Banterle** | HDR imaging / tone mapping | inverse tone mapping, HDR datasets/evaluation, generative video HDR | *AIM 2025 Challenge on Inverse Tone Mapping*; *Generating HDR Video from SDR Video* (2026) | Long-term HDR researcher; useful for both classical ITM and latest generative HDR video direction. |
| **Zhiwei Xiong** | USTC | gain-map HDR, SDR→HDR, HDR generation | *Learning Gain Map for Inverse Tone Mapping* (ICLR 2025); *HDR Image Generation via Gain Map Decomposed Diffusion* (ICCV 2025) | One of the clearest recent lines showing structured Gain Map representation can coexist with deep/generative models. |
| **Yinuo Liao** | USTC | gain-map based ITM | *Learning Gain Map for Inverse Tone Mapping / GMNet* (ICLR 2025) | Key author for predicting Gain Map instead of directly predicting HDR RGB. |
| **Yuanshen Guan** | USTC | gain-map HDR + diffusion | *GMNet* (ICLR 2025); *Gain Map Decomposed Diffusion* (ICCV 2025) | Important bridge from deterministic Gain Map prediction to generative HDR. |
| **Guanying Chen** | computational imaging / vision | alternating-exposure HDR video reconstruction | *HDR Video Reconstruction: A Coarse-to-Fine Network and a Real-World Benchmark Dataset* (ICCV 2021) | DeepHDRVideo remains a major benchmark/code base for multi-exposure HDR video reconstruction. |
| **Gangwei Xu / Xin Yang** | HUST / OpenImagingLab line | real-time alternating-exposure HDR video | *HDRFlow: Real-Time HDR Video Reconstruction with Large Motions* (CVPR 2024) | Strong reference for deployment-oriented multi-exposure HDR video and motion alignment. |
| **Tianfan Xue / Jinwei Gu** | CUHK computational imaging | HDR video, mobile/computational imaging | *HDRFlow* (CVPR 2024) | Useful for linking HDR reconstruction to practical mobile/computational photography constraints. |
| **Ronggang Wang / Yuyao Ye** | video restoration / HDR video | single-video inverse tone mapping, temporal clue recovery | *Deep Video Inverse Tone Mapping Based on Temporal Clues* (CVPR 2024) | Highly relevant to same-EV SDR video: explicitly studies using temporal clues rather than alternating exposures. |
| **Gabriel Eilertsen / Jonas Unger** | HDR imaging | single-image HDR reconstruction, HDR datasets/benchmarks | *HDR Image Reconstruction from a Single Exposure Using Deep CNNs* (TOG/SIGGRAPH Asia 2017); AIM 2025 participation | Foundational work for hallucinating/reconstructing saturated regions from single LDR input. |
| **Yu-Lun Liu / Jia-Bin Huang / Yung-Yu Chuang** | computational photography | inverse camera pipeline, single-image HDR reconstruction | *Single-Image HDR Reconstruction by Learning to Reverse the Camera Pipeline* (CVPR 2020) | Canonical physics-informed baseline: clipping → CRF → quantization reversed as separate learned stages. |
| **SaiKiran Tedla / Trevor Canham** | HDR imaging / display / generative video | gain-map encoding, generative HDR video | *Gain-MLP* (ICCV 2025); *Generating HDR Video from SDR Video* (2026) | Useful for both compact HDR representations and the new “generate exposure brackets then merge” route. |
| **Michael S. Brown** | computational photography / color | HDR gain maps | *Gain-MLP* (ICCV 2025) | Important for practical HDR encoding/representation and color-imaging engineering. |
| **Xianwei Li / Huadong Ma** | BUPT | cinematic SDR→HDR | *HDRMovieformer* (AAAI 2026) | Important real paired professional-grading direction, distinct from synthetic HDR→SDR training. |

<a id="industry-platform-line"></a>
## 2. Industry / Platform HDR Quality Line

These authors are especially relevant when the project objective is **UGC HDR, compression, streaming, display-device dependence, or deployment-scale quality** rather than only reconstruction PSNR.

| Scholar | Organization line | Representative HDR work |
|---|---|---|
| **Neil Birkbeck** | Google / YouTube | CHUG, BrightRate, Beyond8Bits, LumaFlux |
| **Yilin Wang** | Google / YouTube | CHUG, BrightRate, Beyond8Bits, LumaFlux |
| **Balu Adsumilli** | Google / YouTube | CHUG, BrightRate, Beyond8Bits, LumaFlux, LumaGuide |
| **Hai Wei / Zaixi Shang / Yixu Chen** | Amazon video-quality line | *HDR or SDR?*; HDRSDR-VQA |

<a id="tracking-priority"></a>
## 3. Recommended Tracking Priority for Mobile Video HDR

<a id="tier-a"></a>
### Tier A — directly relevant to current SDR-video→HDR project

1. Shreshth Saini / Alan Bovik / Bowen Chen — HDR quality, HDR-Q, LumaFlux/LumaGuide.
2. Rafał Mantiuk — HDR-native quality metrics and display-aware evaluation.
3. Ronggang Wang / Yuyao Ye — same-video temporal clues for video ITM.
4. Zhiwei Xiong / Yinuo Liao / Yuanshen Guan — Gain Map / structured HDR representation.
5. Francesco Banterle / SaiKiran Tedla — ITM benchmark + generative HDR video.
6. Xianwei Li / Huadong Ma — real professional SDR/HDR grading pairs.

<a id="tier-b"></a>
### Tier B — capture-side / multi-exposure HDR reference

1. Guanying Chen — DeepHDRVideo benchmark.
2. Gangwei Xu / Xin Yang / Tianfan Xue / Jinwei Gu — HDRFlow, real-time alternating-exposure HDR video.

<a id="tier-c"></a>
### Tier C — foundational single-image HDR

1. Gabriel Eilertsen / Jonas Unger.
2. Yu-Lun Liu / Jia-Bin Huang / Yung-Yu Chuang.

<a id="primary-links"></a>
## 4. Primary Links

- Alan C. Bovik / LIVE HDR resources: https://live.ece.utexas.edu/
- Rafał K. Mantiuk publications: https://www.cl.cam.ac.uk/~rkm38/publications_area.html
- Shreshth Saini: https://shreshthsaini.github.io/
- GMNet: https://github.com/qtlark/GMNet
- HDRFlow: https://github.com/OpenImagingLab/HDRFlow
- DeepHDRVideo: https://github.com/guanyingc/DeepHDRVideo
- VITM-TC: https://github.com/ye3why/VITM-TC
- ColorVideoVDP: https://github.com/gfxdisp/ColorVideoVDP

<a id="notes"></a>
## 5. Notes

- “HDR reconstruction” can mean very different tasks: **single SDR→HDR inference**, **alternating/multi-exposure fusion**, **display-oriented inverse tone mapping**, or **generative HDR synthesis**. Do not compare methods across these settings without checking the input assumptions.
- For same-EV compressed SDR video, alternating-exposure HDR papers are useful architectural references but are **not directly comparable** because they receive physically complementary exposures.
- For mobile deployment, prioritize methods with explicit runtime/memory evidence and distinguish **temporal stabilization** from **temporal information recovery**.
