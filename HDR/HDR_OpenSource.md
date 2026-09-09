# HDR GitHub / Open-Source Work List

> Last checked: 2026-09-09  
> This list prioritizes projects relevant to SDR→HDR, HDR video reconstruction, Gain Map, HDR-IQA/VQA and HDR evaluation.

## 目录

- [1. SDR → HDR / Inverse Tone Mapping](#sdr-to-hdr)
- [2. HDR Video Reconstruction / Temporal Modeling](#hdr-video)
- [3. HDR IQA / VQA / Perceptual Evaluation](#hdr-iqa-vqa)
- [4. Gain Map / HDR Representation Resources](#gain-map-resources)
- [5. Suggested Baseline Stack for Current Same-EV Compressed SDR Video → HDR](#baseline-stack)
  - [A. Minimal engineering baseline](#baseline-a)
  - [B. Structured HDR representation baseline](#baseline-b)
  - [C. Temporal-evidence baseline](#baseline-c)
  - [D. Real-domain robustness baseline](#baseline-d)
  - [E. Evaluation stack](#baseline-e)
  - [F. Generative upper-bound / research reference](#baseline-f)
- [6. What Not to Compare Directly](#comparison-boundaries)
  - [Same-EV SDR video vs alternating-exposure HDR video](#same-ev-vs-alternating)
  - [Full-reference vs no-reference IQA](#fr-vs-nr)
- [7. Practical Evaluation Checklist](#evaluation-checklist)
- [8. Direct Links Summary](#direct-links)

---

<a id="sdr-to-hdr"></a>
## 1. SDR → HDR / Inverse Tone Mapping

| Project | Task / Input assumption | Main idea | Open assets | Relevance to same-EV mobile Video HDR | Link |
|---|---|---|---|---|---|
| **jpneagle/sdr2hdr** | 8-bit SDR video → HDR10 | heuristic priors + U-Net residual control maps + protection gate + temporal gain smoothing | code, training pipeline, TorchScript model workflow | **High as engineering baseline**; lightweight/control-oriented, but temporal module mainly stabilizes rather than recovers neighbor-frame evidence | https://github.com/jpneagle/sdr2hdr |
| **qtlark/GMNet** | SDR image → Gain Map → HDR | predict Gain Map instead of HDR RGB; local + global branches | code, datasets, scripts | **High** for structured output representation and controllable mapping | https://github.com/qtlark/GMNet |
| **alex04072000/SingleHDR** | single LDR image → HDR | learn to reverse clipping, CRF and quantization | code, pretrained model/data links | **High foundational value**; useful for defining what is physically lost vs learned/hallucinated | https://github.com/alex04072000/SingleHDR |
| **gabrieleilertsen/hdrcnn** | single exposure → HDR | CNN reconstructs saturated highlight regions | code, inference/training | **Medium**; classic single-frame missing-highlight baseline | https://github.com/gabrieleilertsen/hdrcnn |
| **kepengxu/RealRep** | SDR from varied degradation domains → HDR | luminance/chrominance degradation-disentangled representation + degradation-adaptive mapping | code, model implementation, benchmark numbers | **Very high** for real camera/domain generalization | https://github.com/kepengxu/RealRep |
| **Guanys-dar/GM-Diffusion** | text/SDR + Gain Map → HDR generation / SDR→HDR | SDR+Gain Map decomposition + diffusion | code, training/inference scripts | **Medium/Exploratory**; useful for combining structured Gain Map with generative prior | https://github.com/Guanys-dar/GM-Diffusion |
| **shreshthsaini/LumaFlux** | 8-bit BT.709 image/video → 10-bit PQ BT.2020 | frozen FLUX + physical/perceptual adapters + monotone tone-field decoder | code, training/eval/demo, weights/project page | **High research reference, low mobile practicality**; strong generative prior and modern HDR evaluation suite | https://github.com/shreshthsaini/LumaFlux |

<a id="hdr-video"></a>
## 2. HDR Video Reconstruction / Temporal Modeling

| Project | Capture/input | Core method | Open assets | Direct comparability to same-EV SDR? | Link |
|---|---|---|---|---|---|
| **ye3why/VITM-TC** | ordinary LDR/SDR video | global temporal clue sampling + local propagation for video inverse tone mapping | code | **High**; closest open reference for using neighbor-frame evidence in non-bracketed video | https://github.com/ye3why/VITM-TC |
| **OpenImagingLab/HDRFlow** | alternating-exposure video | HDR-oriented optical flow + real-time fusion | code, pretrained models, datasets/scripts | **Low for direct metric comparison; high architectural reference** because input has physically complementary exposures | https://github.com/OpenImagingLab/HDRFlow |
| **guanyingc/DeepHDRVideo** | 2/3 alternating exposures | coarse image-space alignment/merge + feature-space refinement | code, pretrained models | **Low direct comparability**, but major HDR-video benchmark/baseline | https://github.com/guanyingc/DeepHDRVideo |
| **guanyingc/DeepHDRVideo-Dataset** | alternating-exposure HDR benchmark | real/synthetic static/dynamic HDR video data | dataset tools/data access info | useful for understanding multi-exposure benchmark design; not same-EV | https://github.com/guanyingc/DeepHDRVideo-Dataset |
| **gfxdisp/HDRutils** | exposure/gain-modulated RAW/image stacks | HDR merge, RAW Bayer handling, alignment, exposure estimation, noise simulation | Python package/code | useful capture/physics toolbox; not an SDR→HDR model | https://github.com/gfxdisp/HDRutils |

<a id="hdr-iqa-vqa"></a>
## 3. HDR IQA / VQA / Perceptual Evaluation

| Project | Type | Input/reference requirement | What it provides | Recommended use | Link |
|---|---|---|---|---|---|
| **gfxdisp/ColorVideoVDP** | full-reference perceptual image/video metric | test + reference + display specification | JOD quality, distortion heatmaps, temporal/color modeling; supports SDR, PQ HDR and HLG | **Primary FR metric** when trustworthy HDR reference exists | https://github.com/gfxdisp/ColorVideoVDP |
| **cpb68/HDRQA** | HDR IQA / perceptual optimization | reference/testing depending metric setup | exposure-stack decomposition + adapted modern LDR metrics | HDR image quality and luminance-range-aware analysis | https://github.com/cpb68/HDRQA |
| **avinabsaha/HIDRO-VQA** | no-reference HDR VQA representation | HDR video; no pristine reference for NR setup | HDR-domain self-supervised quality representation + SVR pipeline | baseline for HDR-native NR VQA | https://github.com/avinabsaha/HIDRO-VQA |
| **shreshthsaini/CHUG** | HDR-UGC subjective dataset | dataset + MOS | 5,992 videos, 211,848 subjective ratings | HDR-UGC compression/quality research and model calibration | https://github.com/shreshthsaini/CHUG |
| **shreshthsaini/Beyond8Bits** | HDR-UGC dataset + HDR-Q | HDR video; HDR-aware VQA/reasoning | large-scale HDR-UGC data, subjective ratings, HDR-Q project resources | **High priority** for HDR-specific artifacts and MLLM quality reasoning | https://github.com/shreshthsaini/Beyond8Bits |
| **NYU-ICL/TM-metric-adaptation** | tone-mapping quality metric adaptation | HDR reference + tone-mapped content + display model | display-photometry normalization; ColorVideoVDP-tm workflow | strong reference for evaluating SDR/HDR tone-mapping pairs correctly | https://github.com/NYU-ICL/TM-metric-adaptation |
| **shreshthsaini/Awesome-Perceptual-Quality** | curated catalog | n/a | tagged IQA/VQA/HDR methods and subjective datasets | literature/dataset discovery | https://github.com/shreshthsaini/Awesome-Perceptual-Quality |

<a id="gain-map-resources"></a>
## 4. Gain Map / HDR Representation Resources

| Project | Purpose | Notes | Link |
|---|---|---|---|
| **NMoroney/Awesome-Gain-Maps** | Gain Map HDR resource collection | papers, examples, tools, standards-related resources | https://github.com/NMoroney/Awesome-Gain-Maps |
| **qtlark/GMNet** | learn Gain Map from SDR | ICLR 2025 official implementation | https://github.com/qtlark/GMNet |
| **Guanys-dar/GM-Diffusion** | generative SDR+Gain Map HDR | ICCV 2025 official implementation | https://github.com/Guanys-dar/GM-Diffusion |

<a id="baseline-stack"></a>
## 5. Suggested Baseline Stack for Current Same-EV Compressed SDR Video → HDR

<a id="baseline-a"></a>
### A. Minimal engineering baseline

1. `jpneagle/sdr2hdr`
   - establish deterministic/control-map SDR→HDR baseline;
   - inspect highlight expansion, protection gates, temporal EMA and PQ output pipeline.

<a id="baseline-b"></a>
### B. Structured HDR representation baseline

2. `qtlark/GMNet`
   - test Gain Map prediction as an alternative to direct HDR RGB;
   - retain controllability and display adaptation.

<a id="baseline-c"></a>
### C. Temporal-evidence baseline

3. `ye3why/VITM-TC`
   - determine whether same-EV neighbor frames contain recoverable evidence;
   - separate **temporal clue recovery** from simple **flicker suppression**.

<a id="baseline-d"></a>
### D. Real-domain robustness baseline

4. `kepengxu/RealRep`
   - compare degradation-conditioned mapping against fixed synthetic-TMO training.

<a id="baseline-e"></a>
### E. Evaluation stack

5. `gfxdisp/ColorVideoVDP` — reference HDR video evaluation.
6. `cpb68/HDRQA` — HDR luminance-range-aware image evaluation.
7. `shreshthsaini/Beyond8Bits` / `BrightRate` line — HDR no-reference / reasoning-oriented evaluation.

<a id="baseline-f"></a>
### F. Generative upper-bound / research reference

8. `shreshthsaini/LumaFlux`
9. `Guanys-dar/GM-Diffusion`
10. *Generating HDR Video from SDR Video* project page: https://sdr2hdrvideo.github.io/ (no verified official GitHub repository listed here as of the last check).

<a id="comparison-boundaries"></a>
## 6. What Not to Compare Directly

<a id="same-ev-vs-alternating"></a>
### Same-EV SDR video vs alternating-exposure HDR video

`HDRFlow` and `DeepHDRVideo` receive exposure-bracket information that same-EV SDR does not contain. They should be used to study:
- alignment/fusion architecture;
- motion robustness;
- benchmark design;
- latency/runtime engineering.

They should **not** be used as a direct quality baseline unless the capture/input condition is matched.

<a id="fr-vs-nr"></a>
### Full-reference vs no-reference IQA

- `ColorVideoVDP`, HDR-VDP-style metrics: require a meaningful reference and display assumptions.
- `HIDRO-VQA`, BrightRate/HDR-Q line: target no-reference or learned perceptual quality prediction.
- The two classes answer different questions and should not be merged into one score table without explanation.

<a id="evaluation-checklist"></a>
## 7. Practical Evaluation Checklist

For every open-source SDR→HDR model, record:

1. **Input signal** — 8-bit/10-bit, BT.709/P3/BT.2020, gamma/sRGB/BT.1886, image/video.
2. **Capture assumption** — same EV, alternating exposure, RAW/ISP output, synthetic SDR.
3. **HDR target representation** — linear HDR, PQ, HLG, Gain Map, HDR10 container.
4. **Training pair origin** — synthetic TMO, real paired grading, sensor capture, teacher output.
5. **Temporal mechanism** — none, EMA, optical flow, feature propagation, video diffusion.
6. **Missing-information policy** — conservative mapping, neighbor recovery, hallucination/generation.
7. **Metrics** — PU21, ΔE_ITP, HDR-VDP/ColorVideoVDP, subjective study, temporal flicker.
8. **Deployment cost** — resolution, fps, latency, VRAM/RAM, parameters/MACs, codec I/O.

<a id="direct-links"></a>
## 8. Direct Links Summary

```text
Engineering SDR2HDR
https://github.com/jpneagle/sdr2hdr

Gain Map
https://github.com/qtlark/GMNet
https://github.com/Guanys-dar/GM-Diffusion
https://github.com/NMoroney/Awesome-Gain-Maps

Video HDR
https://github.com/ye3why/VITM-TC
https://github.com/OpenImagingLab/HDRFlow
https://github.com/guanyingc/DeepHDRVideo
https://github.com/guanyingc/DeepHDRVideo-Dataset

Single-image HDR foundations
https://github.com/alex04072000/SingleHDR
https://github.com/gabrieleilertsen/hdrcnn

Generalized / generative SDR→HDR
https://github.com/kepengxu/RealRep
https://github.com/shreshthsaini/LumaFlux

HDR IQA/VQA
https://github.com/gfxdisp/ColorVideoVDP
https://github.com/cpb68/HDRQA
https://github.com/avinabsaha/HIDRO-VQA
https://github.com/shreshthsaini/CHUG
https://github.com/shreshthsaini/Beyond8Bits
https://github.com/NYU-ICL/TM-metric-adaptation
```
