# HDR Research Index

> Last checked: 2026-09-09

This folder collects research resources for **SDR→HDR / inverse tone mapping, HDR video reconstruction, gain-map HDR, HDR-IQA/VQA, perceptual evaluation, generative HDR, and commonly used HDR datasets/benchmarks**.

## 目录

- [Files](#files)
  - [HDR_Scholars.md](#hdr-scholars)
  - [HDR_Papers_and_IQA.md](#hdr-papers-iqa)
  - [HDR_OpenSource.md](#hdr-open-source)
  - [HDR_Datasets.md](#hdr-datasets)
- [Current Research Framing for Mobile Same-EV SDR Video → HDR](#current-research-framing)
- [Recommended core baseline stack](#recommended-core-baseline-stack)
- [Maintenance rule](#maintenance-rule)

---

<a id="files"></a>
## Files

<a id="hdr-scholars"></a>
### 1. [HDR_Scholars.md](./HDR_Scholars.md)
HDR-related researcher/team watchlist, including:
- Alan C. Bovik / Shreshth Saini / Bowen Chen
- Rafał K. Mantiuk
- Francesco Banterle
- Zhiwei Xiong / Yinuo Liao / Yuanshen Guan
- Ronggang Wang / Yuyao Ye
- Guanying Chen / HDRFlow team
- foundational single-image HDR researchers

Each entry records research focus, representative work, and why the line is relevant to mobile Video HDR.

<a id="hdr-papers-iqa"></a>
### 2. [HDR_Papers_and_IQA.md](./HDR_Papers_and_IQA.md)
Paper list organized by task:
- single-image SDR→HDR / inverse tone mapping;
- Gain Map / structured HDR representation;
- real-world/cinematic SDR→HDR;
- alternating-exposure HDR video reconstruction;
- same-video temporal-clue inverse tone mapping;
- generative HDR;
- HDR IQA/VQA and subjective datasets;
- ITU HDR standards and evaluation references.

The list explicitly distinguishes **peer-reviewed papers, preprints, datasets, metrics, and standards**.

<a id="hdr-open-source"></a>
### 3. [HDR_OpenSource.md](./HDR_OpenSource.md)
Verified open-source/project links, including:
- `jpneagle/sdr2hdr`
- `qtlark/GMNet`
- `ye3why/VITM-TC`
- `OpenImagingLab/HDRFlow`
- `guanyingc/DeepHDRVideo`
- `kepengxu/RealRep`
- `shreshthsaini/LumaFlux`
- `gfxdisp/ColorVideoVDP`
- `cpb68/HDRQA`
- `avinabsaha/HIDRO-VQA`
- `shreshthsaini/CHUG`
- `shreshthsaini/Beyond8Bits`

The table records **input assumptions, capture type, open assets, and direct relevance to same-EV compressed SDR video**.

<a id="hdr-datasets"></a>
### 4. [HDR_Datasets.md](./HDR_Datasets.md)
Task-oriented HDR dataset / benchmark index covering:
- SDR→HDR / inverse tone mapping pairs: HDRTV1K, AIM 2025 ITM, HDRMovie7K/1K, xDR;
- same-video HDR sources: HdM-HDRv, LiU-HDRv, MPI-HDRv and the VITM-TC synthesis protocol;
- alternating-exposure HDR video: DeepHDRVideo, Real-HDRV, TOG13/Kalantari13;
- multi-exposure HDR image: Kalantari17, SICE, NTIRE HDR;
- HDR-IQA/VQA: ESPL-LIVE HDR, LIVE HDR, LIVE HDR-vs-SDR, CHUG, BrightVQ, HDRSDR-VQA, Beyond8Bits, HDRC;
- calibrated/test content: Fairchild HDR Photographic Survey, EBU HDR sequences.

Each entry records **task/input assumption, scale, HDR target origin, GT/subjective labels, strengths, limitations, access link, and direct comparability to current Same-EV mobile Video HDR**.

---

<a id="current-research-framing"></a>
# Current Research Framing for Mobile Same-EV SDR Video → HDR

Keep the following distinctions explicit when comparing papers:

1. **Same-EV temporal information ≠ exposure-bracket information.**
2. **Temporal stabilization ≠ temporal information recovery.**
3. **PQ/BT.2020/HDR10 compliance ≠ successful HDR reconstruction.**
4. **Synthetic HDR→SDR pairs are useful training data but do not prove real-camera generalization.**
5. **Clipped SDR regions do not uniquely determine original HDR radiance; conservative rendering and generative completion are different research objectives.**
6. **Full-reference HDR metrics and no-reference HDR-VQA solve different evaluation problems.**

<a id="recommended-core-baseline-stack"></a>
## Recommended core baseline stack

```text
Same-EV compressed SDR video
        │
        ├─ Engineering control baseline: jpneagle/sdr2hdr
        ├─ Structured HDR representation: GMNet
        ├─ Temporal evidence recovery: VITM-TC
        ├─ Real-domain robustness: RealRep
        │
        ├─ Dataset baseline: HDRTV1K / AIM2025 / xDR + target-camera data
        ├─ FR evaluation: ColorVideoVDP / HDRQA
        ├─ NR / HDR reasoning: HIDRO-VQA / BrightRate / Beyond8Bits
        │
        └─ Generative upper-bound reference: LumaFlux / Generative HDR Video
```

<a id="maintenance-rule"></a>
## Maintenance rule

When adding a new paper/project/dataset, record at minimum:
- venue/year and publication status;
- exact input/capture assumption;
- HDR output/target representation;
- training data origin / target origin;
- temporal mechanism or video continuity;
- missing-information policy;
- evaluation dataset/metric / subjective label;
- dataset scale and split;
- open-source/data link and license if available;
- direct comparability to the current Same-EV compressed SDR video setting.
