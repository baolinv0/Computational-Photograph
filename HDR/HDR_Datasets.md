# HDR 常用数据集与 Benchmark

> Last checked: 2026-09-09  
> Scope: SDR→HDR / inverse tone mapping (ITM), single-image HDR reconstruction, same-EV HDR video, alternating-exposure HDR video, multi-exposure HDR imaging, HDR-IQA/VQA, HDR display/evaluation resources.

## 目录

- [1. 任务分类与快速选择](#task-map)
- [2. SDR→HDR / Inverse Tone Mapping 配对数据](#itm-paired)
- [3. Same-EV / 单视频 HDR 与 HDR Video Source 数据](#same-ev-video)
- [4. Alternating-Exposure HDR Video Reconstruction](#alternating-video)
- [5. Multi-Exposure HDR Image / Deghosting](#multi-exposure-image)
- [6. HDR IQA / VQA 主观质量数据集](#hdr-iqa-vqa)
- [7. HDR Reference / Display / Standards Test Content](#reference-content)
- [8. 当前 Mobile Same-EV SDR Video→HDR 推荐组合](#recommended-stack)
- [9. 使用数据集时必须记录的信息](#dataset-checklist)

---

<a id="task-map"></a>
## 1. 任务分类与快速选择

不同 HDR 数据集的输入假设差异非常大，不能只因为都叫 HDR 就直接横向比较。

| 任务 | 最常见输入 | 代表数据集 | 对当前 Same-EV SDR Video→HDR 的直接相关性 |
|---|---|---|---|
| **SDR→HDR / ITM** | 单张/逐帧 SDR → HDR | HDRTV1K, AIM 2025 ITM, HDRMovie7K/1K, xDR | **最高** |
| **Same-video Video ITM** | 普通 LDR/SDR 视频，多帧同类曝光 | HDM-HDRv, LiU-HDRv, MPI-HDRv；VITM-TC 用这些作为测试源 | **高** |
| **Alternating-exposure HDR video** | Short/Long 或 2/3 档交替曝光 | DeepHDRVideo, Real-HDRV, TOG13/Kalantari13 | **低直接可比，高架构参考** |
| **Multi-exposure HDR image** | 3 张或多张不同曝光静态/动态图 | Kalantari17, SICE, NTIRE HDR | **低直接可比** |
| **HDR-IQA/VQA** | HDR image/video + MOS/JOD/主观评分 | ESPL-LIVE HDR, LIVE HDR, CHUG, BrightVQ, HDRSDR-VQA, Beyond8Bits | **评价系统高相关** |
| **HDR reference source** | 原生 HDR EXR / HDR10 / HLG | Fairchild HDRPS, HdM-HDR-2014, LiU HDRv, MPI HDRv, EBU test sequences | 适合造数据、显示验证、FR evaluation |

> **重要边界**：Same-EV temporal information ≠ exposure-bracket information。DeepHDRVideo / Real-HDRV 输入中存在真实曝光互补信息，不能直接作为普通压缩 SDR 视频的公平基线。

---

<a id="itm-paired"></a>
## 2. SDR→HDR / Inverse Tone Mapping 配对数据

### 2.1 HDRTV1K — ICCV 2021 / HDRTVNet

- **任务**：SDRTV → HDRTV / inverse tone mapping。
- **数据**：1,235 training pairs + 117 test pairs。
- **来源**：4K HDR10 视频及其 SDR counterpart，抽取成配对图像。
- **HDR 表示**：10-bit, Rec.2020, PQ / HDR10 source。
- **优点**：SDR→HDR 领域最常见的公开 paired benchmark 之一；很多后续工作沿用。
- **局限**：以帧为主，不验证长时间视频稳定性；pair 的形成过程仍需与目标 camera/ISP domain 区分。
- **适合**：baseline、单帧映射能力、Gain Map / ITM 对比。
- Project: https://github.com/chxy95/HDRTVNet
- Dataset mirror: https://huggingface.co/datasets/chxy95/HDRTV1K

### 2.2 AIM 2025 Challenge on Inverse Tone Mapping

- **任务**：single LDR → HDR reconstruction。
- **Training**：约 19,000 LDR-HDR pairs，256×256。
- **Validation / Test**：各 100 张，512×512；test HDR GT 隐藏用于 challenge evaluation。
- **LDR 生成**：HDR source → exposure sampling → noise → clipping → sampled camera response function/nonlinearity → 8-bit LDR。
- **评价**：PU21-PSNR、PU21-SSIM。
- **优点**：2025 年较规范的公开 ITM challenge，protocol 清楚，适合算法横向比较。
- **局限**：依然属于由 HDR 合成 LDR 的训练/测试分布，不能单独证明真实 camera SDR 泛化。
- Paper: https://openaccess.thecvf.com/content/ICCV2025W/AIM/html/Wang_AIM_2025_challenge_on_Inverse_Tone_Mapping_Report_Methods_and_ICCVW_2025_paper.html

### 2.3 HDRMovie7K — AAAI 2026 / HDRMovieformer

- **任务**：cinematic SDR→HDR conversion。
- **来源**：professional Digital Cinema Distribution Master (DCDM) workflow 中的 lossless SDR-HDR frame pairs。
- **价值**：与 HDR→synthetic-TMO→SDR 不同，目标是专业 SDR/HDR grading pair；更适合研究真实 creative grading / wide-color-gamut mapping。
- **适合**：专业内容、电影 SDR→HDR、色彩和亮度映射。
- **局限**：cinematic grading domain 与 mobile camera SDR domain 不同；不能直接代表眼镜/手机 ISP。
- Paper: https://ojs.aaai.org/index.php/AAAI/article/view/37578

### 2.4 HDRMovie1K — AAAI 2026

- **任务**：online/streaming-oriented cinematic SDR→HDR evaluation。
- **来源**：公开 HDR film clips curated 成 benchmark。
- **作用**：与 HDRMovie7K 一起用于 HDRMovieformer 的跨内容/streaming evaluation。
- **局限**：仍偏影视内容，不是 camera-native paired capture。
- Paper: https://ojs.aaai.org/index.php/AAAI/article/view/37578

### 2.5 xDR Dataset — SPIC 2026

- **任务**：inverse tone mapping evaluation。
- **规模**：10 个约 40 s 的 FHD cinematic sequences。
- **关键特点**：同一 creative intent 下，由专业人员分别完成 **native SDR grading** 与 **native HDR grading**，而不是简单 HDR→TMO→SDR。
- **价值**：非常适合检验“synthetic SDR pair 是否导致 benchmark 偏差”。
- **局限**：规模小；适合 evaluation，不适合独立承担大模型训练。
- Paper: https://www.sciencedirect.com/science/article/pii/S0923596526000536

### 2.6 Fairchild HDR Photographic Survey — HDR reference source

- **任务**：HDR rendering / tone mapping / IQA reference，而不是直接 paired SDR→HDR benchmark。
- **规模**：106 HDR images；28 张具有更完整 colorimetric/appearance data，其余至少具备 absolute luminance calibration。
- **优点**：经典、带绝对亮度/色度信息，适合 tone mapping 和 HDR quality 研究。
- **局限**：静态图、年代较早，不代表 contemporary mobile video/UGC。
- Access: https://markfairchild.org/HDR.html

---

<a id="same-ev-video"></a>
## 3. Same-EV / 单视频 HDR 与 HDR Video Source 数据

这些数据通常是**原生 HDR 视频源**，研究者再根据 camera model/TMO 合成 LDR/SDR 输入。它们不等价于真实 paired camera SDR/HDR，但非常常用于 Video ITM。

### 3.1 HdM-HDR-2014 / Stuttgart HDR Dataset

- **内容**：cinematic wide-gamut HDR video sequences，室内/室外、焊接、火焰、汽车、人物等高动态范围场景。
- **格式**：常见研究版本为 floating-point / HDR source；很多论文从中合成 LDR 或 alternating-exposure input。
- **典型用途**：video tone mapping、video ITM、HDR display evaluation、DeepHDRVideo synthetic training/test source。
- **VITM-TC**：CVPR 2024 将其作为 real HDR video source 之一进行测试输入合成。
- **局限**：场景数量有限；历史影视/研究相机分布与 mobile UGC 不同。
- Project/resource: https://www.hdm-stuttgart.de/~froehlichj/

### 3.2 LiU HDRv Repository

- **内容**：多组 HDR video sequences 和 HDR light probes；OpenEXR frame sequences。
- **典型下载分辨率**：很多公开序列提供 1280×720 EXR 版本。
- **部分序列**：Students、Bridge、River、Exhibition Area 等；部分有 radiometric calibration。
- **用途**：video ITM、HDR video reconstruction synthetic source、tone mapping、lighting。
- **License**：网站声明数据/代码可按 CC BY-SA 4.0 使用。
- Resource: https://computergraphics.on.liu.se/hdrv_itn_liu/Resources.php

### 3.3 MPI HDR Video Dataset

- **任务**：早期 HDR video / perceptual HDR encoding reference。
- **规模**：常见 benchmark summary 中为 2 个 HDR videos。
- **用途**：video ITM / HDR compression / temporal HDR evaluation。
- **VITM-TC**：作为 CVPR 2024 的 public HDR video testing source 之一。
- Resource: https://resources.mpi-inf.mpg.de/hdr/video/

### 3.4 VITM-TC 数据合成设置 — CVPR 2024

VITM-TC 本身没有建立一个大规模 native paired SDR/HDR video dataset，而是组合不同数据源：

- **HDR image source**：SICE，589 multi-exposure scenes。
- **LDR video source**：REDS sharp training dataset。
- **Synthetic video generation**：对 HDR image 做 random perspective transform 模拟 camera motion；再模拟 exposure / clipping / camera response。
- **Real HDR video test source**：HdM-HDRv、LiU-HDRv、MPI-HDRv，并从 HDR source 模拟对应 LDR。

这套 protocol 对当前项目很重要，因为它说明：

> same-video temporal clue research 仍然严重受限于“缺少真实 paired SDR/HDR video”，很多结果仍依赖 synthetic camera pipeline。

- Paper: https://openaccess.thecvf.com/content/CVPR2024/html/Ye_Deep_Video_Inverse_Tone_Mapping_Based_on_Temporal_Clues_CVPR_2024_paper.html
- Code: https://github.com/ye3why/VITM-TC

---

<a id="alternating-video"></a>
## 4. Alternating-Exposure HDR Video Reconstruction

### 4.1 DeepHDRVideo Dataset — ICCV 2021

- **任务**：2/3 alternating-exposure LDR video → HDR video。
- **公开内容**：
  - synthetic training dataset；
  - synthetic test dataset；
  - real static scenes with GT HDR；
  - real dynamic scenes with GT HDR；
  - real dynamic scenes without GT HDR。
- **Synthetic training source**：13 个 HdM-HDR-2014 videos + 8 个 LiU HDRv videos，共 21 HDR videos。
- **Synthetic test**：`POKER FULLSHOT` 与 `CAROUSEL FIREWORKS`，各 60 frames，1920×1080。
- **真实采集**：Basler camera，2/3 exposure alternating capture，并保留 RAW/metadata 处理流程。
- **优点**：HDR video reconstruction 经典 benchmark，代码/数据/采集脚本完整。
- **局限**：输入有真实 exposure complementarity，和普通 same-EV SDR video 任务不同。
- Dataset: https://github.com/guanyingc/DeepHDRVideo-Dataset
- Code: https://github.com/guanyingc/DeepHDRVideo

### 4.2 Real-HDRV — CVPR 2024

- **任务**：real-world alternating-exposure HDR video reconstruction / deghosting。
- **规模**：500 LDRs-HDRs video pairs，约 28,000 LDR frames + 4,000 HDR labels。
- **覆盖**：daytime / nighttime / indoor / outdoor，多种 motion pattern。
- **数据形态**：
  - original RAW dataset；
  - Real-HDRV-v1: sRGB HDR video reconstruction；
  - Real-HDRV-v2: HDR deghosting。
- **典型 exposure setup**：公开 repo 提供 2 alternating exposures，3 EV stops 的预处理版本。
- **优势**：针对“synthetic HDR video data → real scene generalization gap”而设计。
- **局限**：仍然是 alternating exposure capture，不是 post-ISP same-EV SDR。
- Paper: https://openaccess.thecvf.com/content/CVPR2024/html/Shu_Towards_Real-World_HDR_Video_Reconstruction_A_Large-Scale_Benchmark_Dataset_and_CVPR_2024_paper.html
- Dataset: https://github.com/yungsyu99/Real-HDRV

### 4.3 TOG13 / Kalantari13 Dynamic HDR Video Dataset

- **任务**：dynamic HDR video from alternating exposures。
- **规模**：9 dynamic videos；包含 2-exposure / 3-exposure sequences。
- **典型 scenes**：Cleaning、Dog、Fire、Ninja、ThrowingTowel、WavingHands 等。
- **用途**：DeepHDRVideo/HDRFlow 等常作 qualitative or legacy benchmark。
- **局限**：规模很小，很多序列缺乏现代严格 GT；更适合 qualitative motion/deghosting comparison。
- Access mirror/info: https://github.com/guanyingc/DeepHDRVideo-Dataset

### 4.4 HDRFlow 2024 的训练/测试数据组合

HDRFlow 没有单独创造一个新的主 benchmark，而是使用：

- **Training**：Vimeo-90K + Sintel（加强 large motion / flow supervision）。
- **Testing**：DeepHDRVideo、HDR Synthetic Test Dataset、TOG13 Dynamic Dataset。
- **意义**：说明 HDR video 模型常需要“真实 HDR benchmark + 通用 motion/flow dataset”联合训练。
- Repo: https://github.com/OpenImagingLab/HDRFlow

---

<a id="multi-exposure-image"></a>
## 5. Multi-Exposure HDR Image / Deghosting

### 5.1 Kalantari HDR Dataset — SIGGRAPH / TOG 2017

- **任务**：dynamic multi-exposure HDR image reconstruction。
- **规模**：89 scenes = 74 train + 15 test。
- **输入**：每个 scene 三张不同 exposure LDR，典型为 {-2,0,+2} 或 {-3,0,+3} EV。
- **GT**：提供 aligned HDR ground truth。
- **分辨率**：常用 release 约 1500×1000。
- **地位**：multi-exposure HDR image deghosting 最经典的监督 benchmark 之一。
- **局限**：输入条件与 same-EV video 完全不同。
- Project: https://cseweb.ucsd.edu/~viscomp/projects/SIG17HDR/

### 5.2 SICE — TIP 2018

- **任务**：single-image contrast enhancement / multi-exposure fusion source；后续也常被拿来生成 HDR/ITM synthetic data。
- **规模**：589 multi-exposure sequences，4,413 images。
- **来源**：真实 multi-exposure image sequences。
- **Reference**：使用 13 个 MEF/HDR methods 生成候选，再通过 subjective screening 选择 reference。
- **重要限制**：这个 reference 是“主观筛选的 enhanced target”，**不是严格 radiometric HDR ground truth**。
- **VITM-TC**：将 SICE 作为 HDR image source 之一合成视频训练数据。
- Repo: https://github.com/csjcai/SICE

### 5.3 NTIRE 2021 HDR Dataset

- **任务**：multi-exposure HDR reconstruction challenge。
- **常见 split**：约 1,494 train + 60 val + 201 test（文献汇总口径）。
- **性质**：以 synthetic/controlled HDR reconstruction benchmark 为主。
- **适合**：多曝光 HDR image reconstruction；不适合直接作为 same-EV SDR→HDR 结论依据。

---

<a id="hdr-iqa-vqa"></a>
## 6. HDR IQA / VQA 主观质量数据集

### 6.1 ESPL-LIVE HDR Subjective Image Quality Database — 2016

- **任务**：HDR/tone-mapped image subjective IQA / NR-IQA。
- **规模**：1,811 images。
- **主观数据**：>300,000 opinion scores，>5,000 observers。
- **内容**：TMO / MEF algorithms 及 post-processing 输出。
- **价值**：经典 large-scale HDR-related subjective image quality dataset。
- **局限**：主要是 tone-mapped/displayed image quality，不代表原生 HDR10 video UGC。
- Access: https://live.ece.utexas.edu/research/HDRDB/hdr_index.html

### 6.2 LIVE HDR Video Quality Assessment Database — ICIP 2022

- **任务**：HDR10 video quality / compression / scaling / ambient-condition assessment。
- **规模**：310 videos，31 source contents，10 bitrate/resolution combinations。
- **格式**：HDR10，50/60 fps；clip 通常 7–10 s。
- **主观数据**：>20,000 human opinions。
- **用途**：HDR compression/VQA、display-condition-aware evaluation。
- Access: https://live.ece.utexas.edu/research/LIVEHDR/LIVEHDR_index.html

### 6.3 LIVE HDR vs SDR Database — TIP 2024

- **任务**：同内容 HDR vs SDR preference under scaling/compression/display differences。
- **规模**：356 videos；公开授权部分 212 videos。
- **主观实验**：67 observers，>23,000 ratings。
- **显示设备**：OLED / QLED / LCD TVs。
- **价值**：直接回答“HDR 是否一定比 SDR 更好”；非常适合产品 display-aware evaluation。
- Access: https://live.ece.utexas.edu/research/LIVE_HDRvsSDR/index.html

### 6.4 CHUG — ICIP 2025

- **任务**：UGC-HDR VQA / streaming distortions。
- **规模**：856 HDR-UGC sources → 5,992 videos。
- **主观数据**：211,848 ratings。
- **退化**：多 resolution / bitrate ladder transcoding，模拟真实平台 delivery conditions。
- **价值**：较早的大规模 HDR-UGC subjective dataset；适合 NR-VQA 和 compression quality。
- Dataset: https://github.com/shreshthsaini/CHUG
- LIVE page: https://www.colorado.edu/lab/live/chug-crowdsourced-user-generated-hdr-video-quality-dataset

### 6.5 BrightVQ — WACV 2026

- **任务**：No-Reference HDR-UGC VQA。
- **规模**：300 HDR source videos → 2,100 total clips。
- **主观数据**：73,794 ratings。
- **格式**：Rec.2020, 10-bit, PQ；portrait + landscape；360p/720p/1080p + source。
- **价值**：同时覆盖 UGC-specific + HDR-specific artifacts。
- **参考结果**：BrightRate 在作者公开版本中报告 BrightVQ SROCC 0.889；HIDRO-VQA 0.853。
- Dataset: https://github.com/shreshthsaini/BrightVQ
- Hugging Face: https://huggingface.co/datasets/shreshthsaini/BrightVQ

### 6.6 HDRSDR-VQA — 2025

- **任务**：HDR 与 SDR 的 pairwise preference / JOD modelling。
- **规模**：960 videos from 54 source sequences；HDR + SDR，9 distortion levels。
- **主观实验**：145 participants，6 consumer HDR-capable TVs，>22,000 pairwise comparisons。
- **标签**：JOD (Just-Objectionable-Difference) scores。
- **价值**：非常适合“HDR 增强是否真的比 SDR 好”与 display-dependent preference 研究。
- Paper: https://arxiv.org/abs/2505.21831

### 6.7 Beyond8Bits — CVPR 2026

- **任务**：large-scale HDR-UGC VQA / HDR reasoning。
- **论文完整规模**：约 44,276 videos，6,861 HDR sources，>1.5M crowd ratings。
- **公开 publish-ready release**：41,419 clips，5,917 sources，约 1.46M ratings。
- **resolution**：360p / 720p / 1080p + source；多 bitrate ladder。
- **价值**：截至 2026 年最重要的 HDR-UGC subjective data resources 之一；HDR-Q/HAPO 的训练与 benchmark 基础。
- **适合**：HDR-specific artifacts、NR VQA、MLLM reasoning、困难样本筛选。
- Dataset: https://github.com/shreshthsaini/Beyond8Bits
- Hugging Face: https://huggingface.co/datasets/shreshthsaini/Beyond8Bits

### 6.8 HDRC — 2024

- **任务**：compressed HDR image subjective quality assessment。
- **规模**：80 reference HDR images，400 distorted images，20 observers（论文/综述统计口径）。
- **压缩**：JPEG-XT、VVC。
- **用途**：HDR compression IQA、不同 HDR perceptual encoding / quality metric comparison。
- Repo: https://github.com/Yliu724/HDRC
- Paper: https://link.springer.com/article/10.1007/s13042-024-02151-1

### 6.9 Legacy HDR-IQA Databases

2024/2026 HDR-IQA surveys 仍经常比较：

- Narwaria2013: 10 refs / 140 distorted。
- Narwaria2014: 6 refs / 210 distorted。
- Korshunov2015: 20 refs / 240 distorted。
- UPIQ HDR subset: 30 refs / 380 distorted。
- HDR-Eye: 46 high-quality HDR images，常作 reference/source pool。

这些数据规模较小，但对验证 HDR-specific objective metrics 仍有历史价值。

---

<a id="reference-content"></a>
## 7. HDR Reference / Display / Standards Test Content

### 7.1 Fairchild HDR Photographic Survey

- 106 calibrated HDR photographs。
- 静态 HDR、绝对亮度/色度资料丰富。
- https://markfairchild.org/HDR.html

### 7.2 EBU HDR Test Sequences

- HLG / BT.2100-oriented broadcast test content。
- 典型研究汇总中包含约 10 个 4K-level sequences，50 fps。
- 适合：HLG pipeline、codec/display compatibility、标准验证；不是 SDR→HDR paired training data。
- https://tech.ebu.ch/testsequences

### 7.3 LiU HDRv

- 原生 OpenEXR HDR video sequences + light probes。
- 适合：synthetic degradation、tone mapping、FR evaluation。
- https://computergraphics.on.liu.se/hdrv_itn_liu/Resources.php

### 7.4 HdM-HDR-2014

- cinematic WCG/HDR test sequences，长期用于 HDR display/TMO/HDR reconstruction 研究。
- https://www.hdm-stuttgart.de/~froehlichj/

---

<a id="recommended-stack"></a>
## 8. 当前 Mobile Same-EV SDR Video→HDR 推荐组合

当前任务是：**眼镜输出压缩 Same-EV SDR video → 手机端 HDR video**。建议不要寻找一个“万能 HDR dataset”，而是组合不同数据完成不同验证。

### A. 第一阶段：快速建立可比较 baseline

1. **HDRTV1K**
   - 训练/验证单帧 SDR→HDR mapping；
   - 与 GMNet / HDRTVNet / RealRep 类方法建立横向基准。
2. **AIM 2025 ITM**
   - 用标准化 PU21 benchmark 检查 highlight / tone reconstruction；
   - 避免只看普通 PSNR/SSIM。

### B. 第二阶段：Video temporal capability

3. **HdM-HDRv + LiU-HDRv + MPI-HDRv**
   - 生成受控 same-EV synthetic SDR video；
   - 验证 temporal stability 与 temporal clue recovery。
4. **VITM-TC protocol**
   - 作为 same-video temporal clue baseline；
   - 重点研究“当前帧缺失、邻帧是否真的存在 evidence”。

### C. 第三阶段：Real-domain gap

5. **xDR / HDRMovie7K/1K**
   - 用 real/professional SDR-HDR grading pair 检查 synthetic-TMO bias。
6. **自采眼镜数据**
   - 这是最终不可替代的数据；需要覆盖真实 ISP、codec、AE/TM history、head motion、occlusion、compression artifact。
   - 若已有对应 HDR teacher/output，应明确它是 **target rendering / teacher result**，不自动等于 radiometric GT。

### D. 第四阶段：HDR quality evaluation

7. **ColorVideoVDP / HDRQA**
   - 有可信 HDR reference 时做 FR evaluation。
8. **LIVE HDR / HDRSDR-VQA**
   - 验证 display-aware HDR benefit。
9. **CHUG / BrightVQ / Beyond8Bits**
   - 训练/校准 NR HDR-VQA；
   - 做 HDR-specific artifact 分类、困难样本筛选和模型版本比较。

### E. 不应作为直接 baseline 的数据

- **DeepHDRVideo / Real-HDRV / TOG13**：因为输入含真实 alternating exposure information。
- **Kalantari17 / SICE**：属于 multi-exposure image setting。

它们可以参考 alignment、fusion、deghosting 和数据采集方式，但不能与 same-EV SDR→HDR 做不加说明的 PSNR 排名。

---

<a id="dataset-checklist"></a>
## 9. 使用数据集时必须记录的信息

每新增一个 HDR dataset，至少记录：

1. **Task**：ITM / HDR reconstruction / multi-exposure fusion / IQA / VQA / display test。
2. **Input representation**：8-bit SDR、10-bit SDR/HDR、RAW、linear RGB、PQ、HLG、EXR。
3. **Capture assumption**：same EV、alternating exposure、multi-exposure stack、synthetic SDR。
4. **HDR target origin**：native capture、professional grading、TMO inverse target、teacher output、synthetic GT。
5. **Pair validity**：是否 pixel-aligned / temporally aligned / same content / same creative intent。
6. **Scale**：source count、clip/image count、resolution、fps、duration。
7. **Temporal property**：single image、independent frames、continuous video、是否含 fast motion / scene cut / flicker。
8. **Distortion/domain**：camera ISP、codec、noise、clipping、local TM、streaming ladder、UGC artifact。
9. **Evaluation labels**：GT HDR、MOS、JOD、pairwise preference、attribute labels。
10. **Display condition**：reference monitor、peak luminance、ambient condition、PQ/HLG interpretation。
11. **License/access**：public / form request / academic-only / commercial restriction。
12. **Direct comparability**：是否能与当前 Same-EV compressed SDR Video→HDR 公平比较。

---

## 核心结论

对于当前项目，最值得优先获取/跑通的不是多曝光 HDR benchmark，而是：

```text
HDRTV1K / AIM2025
        ↓
单帧 SDR→HDR 基线

HdM-HDRv / LiU-HDRv / MPI-HDRv
        ↓
Same-EV video synthetic + temporal test

xDR / HDRMovie
        ↓
检查 synthetic-to-real grading gap

自采眼镜 SDR(+对应 HDR target)
        ↓
真实目标域

LIVE HDR / HDRSDR-VQA / CHUG / BrightVQ / Beyond8Bits
        ↓
HDR quality / preference / NR-VQA
```

**真正缺的仍然是“大规模、真实 camera/ISP、same-EV compressed SDR video 与可信 HDR target 成对”的公开数据。**这也是当前项目自采数据和真实退化建模最有研究价值的地方。
