# HDR Dataset References & Pseudo-GT (PGT) Strategy

> Last checked: 2026-09-09  
> Scope: dataset papers/project links and pseudo-ground-truth construction for **same-EV, 8-bit compressed SDR video from smart glasses → HDR on phone**.

## 目录

- [1. 数据集论文 / 官方链接](#dataset-references)
- [2. PGT 是什么，为什么当前项目需要](#pgt-definition)
- [3. 推荐的 PGT 生成模型](#pgt-models)
- [4. 推荐的 PGT 生成流程](#pgt-pipeline)
- [5. 直接采用 PGT / Teacher-Pseudo-HDR 的参考论文](#pgt-papers)
- [6. 当前项目建议](#project-recommendation)
- [7. PGT 使用边界](#pgt-limitations)

---

<a id="dataset-references"></a>
## 1. 数据集论文 / 官方链接

> 原则：优先给正式论文；若数据集没有独立论文，则给官方 dataset/project page。

### 1.1 SDR→HDR / ITM 直接相关

| 数据集 / Benchmark | 论文 / 官方资源 | 说明 |
|---|---|---|
| **HDRTV1K** | **A New Journey From SDRTV to HDRTV**, Chen et al., ICCV 2021 — https://openaccess.thecvf.com/content/ICCV2021/html/Chen_A_New_Journey_From_SDRTV_to_HDRTV_ICCV_2021_paper.html | 建立 HDRTV1K；常用 SDRTV→HDRTV baseline 数据。 |
| **AIM 2025 ITM** | **AIM 2025 challenge on Inverse Tone Mapping Report: Methods and Results**, Wang et al., ICCV Workshops 2025 — https://openaccess.thecvf.com/content/ICCV2025W/AIM/html/Wang_AIM_2025_challenge_on_Inverse_Tone_Mapping_Report_Methods_and_ICCVW_2025_paper.html | 单幅 LDR→HDR benchmark；HDR GT 真实，LDR 为模拟 camera/degradation pipeline。 |
| **xDR** | **The xDR dataset: A cinematic natively graded HDR & SDR dataset for evaluation of inverse tone mapping methods**, Luzardo et al., Signal Processing: Image Communication 2026 — https://www.sciencedirect.com/science/article/pii/S0923596526000536 | 专业人员分别 native grade SDR/HDR；非常适合真实 grading 评价。 |
| **HDRMovie7K / HDRMovie1K** | **HDRMovieformer: A Transformer Framework and Benchmark for Cinematic SDR-to-HDR Conversion**, Li et al., AAAI 2026 — https://ojs.aaai.org/index.php/AAAI/article/view/37578 | HDRMovie7K 来自专业 DCDM SDR/HDR workflow；HDRMovie1K 面向 streaming 评价。 |
| **LIVE-TMHDR** | **Subjective Quality Assessment of Compressed Tone-Mapped High Dynamic Range Videos**, Venkataramanan & Bovik, 2024 — https://arxiv.org/abs/2403.15061 ; Dataset: https://live.ece.utexas.edu/research/LIVE_TMHDR/index.html | 40 HDR source → 15,000 tone-mapped videos；10 open-source TMOs、2 proprietary TMOs、人工 colorist。 |
| **HDRTV4K** | **Learning a Practical SDR-to-HDRTV Up-Conversion Using New Dataset and Degradation Models**, Guo et al., CVPR 2023 — https://openaccess.thecvf.com/content/CVPR2023/html/Guo_Learning_a_Practical_SDR-to-HDRTV_Up-Conversion_Using_New_Dataset_and_Degradation_CVPR_2023_paper.html | 强调真实 SDR domain 与简单 HDR→SDR 合成之间的 gap；对我们数据退化设计很有参考价值。 |
| **GMNet real/synthetic datasets** | **Learning Gain Map for Inverse Tone Mapping**, Liao et al., ICLR 2025 — https://proceedings.iclr.cc/paper_files/paper/2025/hash/43d2b7fbee8431f7cef0d0afed51c691-Abstract-Conference.html ; Code/Data: https://github.com/qtlark/GMNet | 同时提供 synthetic SDR-GM 与 real-world mobile SDR-GM 数据。 |
| **LumaFlux mixed corpus / Luma-Eval** | **LumaFlux: Lifting 8-Bit Worlds to HDR Reality with Physically-Guided Diffusion Transformers**, Saini et al., 2026 — https://arxiv.org/abs/2604.02787 | 大规模多来源 HDR + 多 TMO + codec round-trip；适合作为数据引擎参考，不应视为真实 camera pair。 |

### 1.2 真实 HDR video mother data / Temporal source

| 数据 | 论文 / 官方资源 | 说明 |
|---|---|---|
| **HdM-HDR-2014** | **Creating cinematic wide gamut HDR-video for the evaluation of tone mapping operators and HDR-displays**, Fröhlich et al., SPIE 2014 — 官方入口：https://www.hdm-stuttgart.de/~froehlichj/ ; Dataset: https://www.hdm-stuttgart.de/vmlab/hdm-hdr-2014/ | 双 ARRI Alexa / mirror rig 不同曝光采集并重建 HDR；适合做 controlled Fixed-EV / AE-varying synthesis。 |
| **LiU HDRv** | Official HDRv Repository — https://computergraphics.on.liu.se/hdrv_itn_liu/HDRv.php ; Resources: https://computergraphics.on.liu.se/hdrv_itn_liu/Resources.php | 多传感器 HDR video camera；真实 OpenEXR HDR source。没有单一“数据集论文”被统一作为引用入口，官方 repository 最可靠。 |
| **MPI HDRv** | MPI HDR video repository / historical HDR source；在 VITM-TC、HDRCNN 等工作中被使用。 | 规模小，主要作为经典 HDR source / sanity check。 |
| **DeepHDRVideo** | **HDR Video Reconstruction: A Coarse-To-Fine Network and a Real-World Benchmark Dataset**, Chen et al., ICCV 2021 — https://openaccess.thecvf.com/content/ICCV2021/html/Chen_HDR_Video_Reconstruction_A_Coarse-To-Fine_Network_and_a_Real-World_Benchmark_ICCV_2021_paper.html | alternating-exposure HDR video benchmark；不应和 same-EV 输入直接比较。 |
| **Real-HDRV** | **Towards Real-World HDR Video Reconstruction: A Large-Scale Benchmark Dataset and A Two-Stage Alignment Network**, Shu et al., CVPR 2024 — https://openaccess.thecvf.com/content/CVPR2024/html/Shu_Towards_Real-World_HDR_Video_Reconstruction_A_Large-Scale_Benchmark_Dataset_and_CVPR_2024_paper.html | 500 real alternating-exposure LDR/HDR video pairs；真实 RAW domain。 |
| **Kalantari13 HDR Video** | **Patch-Based High Dynamic Range Video**, Kalantari et al., SIGGRAPH Asia / TOG 2013 — https://web.ece.ucsb.edu/~psen/PaperPages/HDRVideo/ | 经典 alternating-exposure HDR video；主要用于 motion/deghosting。 |

### 1.3 Consumer HDR / HDR-IQA / VQA

| 数据 | 论文 / 官方资源 | 说明 |
|---|---|---|
| **LIVE UGC-HDR** | Official dataset page — https://live.ece.utexas.edu/research/LIVE_UGC_HDR/index.html | 2,153 个 iPhone amateur HLG/Rec.2100 HDR source videos；非常适合做 consumer HDR mother content。 |
| **CHUG** | **CHUG: Crowdsourced User-Generated HDR Video Quality Dataset**, Saini et al., ICIP 2025 — https://arxiv.org/abs/2510.09879 ; Dataset: https://shreshthsaini.github.io/CHUG/ | 856 source → 5,992 clips；211,848 ratings；UGC-HDR distortion / compression。 |
| **BrightVQ** | **BrightRate: Quality Assessment for User-Generated HDR Videos**, Saini et al., WACV 2026 — https://openaccess.thecvf.com/content/WACV2026/html/Saini_BrightRate_Quality_Assessment_for_User-Generated_HDR_Videos_WACV_2026_paper.html | 2,100 HDR UGC clips / 73,794 ratings；可用于 HDR-specific NR-VQA。 |
| **HDRSDR-VQA** | **HDRSDR-VQA: A Subjective Video Quality Dataset for HDR and SDR Comparative Evaluation**, Chen et al., 2025 — https://arxiv.org/abs/2505.21831 | 960 videos / 54 sources / 145 participants / 6 HDR TVs；直接比较 HDR vs SDR 用户偏好。 |
| **Beyond8Bits** | **Seeing Beyond 8bits: Subjective and Objective Quality Assessment of HDR-UGC Videos**, Saini et al., CVPR 2026 — https://github.com/shreshthsaini/Beyond8Bits | 大规模 HDR-UGC + HDR-Q；适合 NR-HDR VQA、reasoning、hard-case mining。 |
| **Fairchild HDR Photographic Survey** | **The HDR Photographic Survey**, Mark D. Fairchild, CIC 2007 — https://dblp.org/rec/conf/imaging/Fairchild07 | 经典 HDR photographic reference；适合亮度 / color science sanity check。 |

---

<a id="pgt-definition"></a>
## 2. PGT 是什么，为什么当前项目需要

当前项目最终会遇到大量：

```text
Real glasses SDR
       ↓
没有严格同步 / 同视角 / 物理可信的 HDR GT
```

因此可以引入：

```text
Real glasses SDR
       ↓
High-quality teacher / existing HDR pipeline / multiple HDR candidates
       ↓
Reliability & quality filtering
       ↓
Pseudo HDR Target (PGT)
       ↓
Target-domain fine-tuning / student training
```

PGT 的核心价值不是“把生成结果变成真 GT”，而是：

> **让训练输入来自真实眼镜 domain，同时用可信度受控的 HDR target 提供弱监督。**

PGT 必须明确标记为 **pseudo target / teacher target**，不能写成 physical ground truth。

---

<a id="pgt-models"></a>
## 3. 推荐的 PGT 生成模型

### 3.1 推荐排序

| 模型 / 来源 | 类型 | 作为 PGT Teacher 的推荐度 | 为什么 | 主要风险 | 参考 |
|---|---|---:|---|---|---|
| **现有厂商 / 专业 HDR pipeline** | Product / professional teacher | **S** | 如果目标是复现产品 HDR rendering，它最接近最终目标域；不存在“生成模型风格偏离产品”的问题 | 可能自身存在 artifact；不是 physical scene GT | 内部/合作方 pipeline；需记录版本与参数 |
| **RealRep / DDACMNet** | degradation-aware SDR→HDR mapping | **S/A** | 专门解决不同真实 SDR style/degradation 的泛化；比固定 TMO teacher 更适合真实眼镜 SDR | 仍是单图/映射模型；与眼镜视频 temporal domain 有差异 | **RealRep: Generalized SDR-to-HDR Conversion via Attribute-Disentangled Representation Learning**, AAAI 2026 — https://ojs.aaai.org/index.php/AAAI/article/view/38111 |
| **GMNet** | Gain-Map structured ITM | **A** | 输出结构化 Gain Map，内容保真、可解释，适合作为“保守 teacher”或 PGT baseline | 对真正缺失/clipped 信息补全能力有限 | **Learning Gain Map for Inverse Tone Mapping**, ICLR 2025 — https://proceedings.iclr.cc/paper_files/paper/2025/hash/43d2b7fbee8431f7cef0d0afed51c691-Abstract-Conference.html |
| **HDRTVDM / LSN** | practical SDR→HDRTV | **A** | 明确针对真实 SDR degradation/domain gap；亮/暗区分支适合产生较稳定的 HDR mapping target | 主要是媒体内容/单图映射；不是 video teacher | **Learning a Practical SDR-to-HDRTV Up-Conversion Using New Dataset and Degradation Models**, CVPR 2023 — https://openaccess.thecvf.com/content/CVPR2023/html/Guo_Learning_a_Practical_SDR-to-HDRTV_Up-Conversion_Using_New_Dataset_and_Degradation_CVPR_2023_paper.html |
| **HDRTVNet** | lightweight SDRTV→HDRTV baseline | **B/A** | 成熟、可复现、输出稳定，可作为廉价 teacher / ensemble member | HDRTV1K 域偏电视/影视；真实 camera 泛化有限 | **A New Journey From SDRTV to HDRTV**, ICCV 2021 — https://openaccess.thecvf.com/content/ICCV2021/html/Chen_A_New_Journey_From_SDRTV_to_HDRTV_ICCV_2021_paper.html |
| **LumaFlux** | generative DiT SDR→HDR | **A（候选生成）/ C（单一 GT）** | 对 clipping、复杂真实退化和 HDR perceptual prior 更强；适合产生“高质量上界候选” | 生成式 hallucination、计算重、逐帧 video consistency 不能保证；不应直接作为唯一 PGT | **LumaFlux: Lifting 8-Bit Worlds to HDR Reality with Physically-Guided Diffusion Transformers**, 2026 — https://arxiv.org/abs/2604.02787 |
| **HDRMovieformer** | cinematic Transformer | **B** | 专业 SDR/HDR grading mapping 强，可作为 cinematic/reference-style teacher | domain 偏电影，不接近 glasses UGC | **HDRMovieformer**, AAAI 2026 — https://ojs.aaai.org/index.php/AAAI/article/view/37578 |

### 3.2 对当前项目的建议：不要只用一个 Teacher

推荐采用：

```text
Real glasses SDR clip
       │
       ├─ Conservative teacher: RealRep / GMNet
       ├─ Practical mapper: HDRTVDM / HDRTVNet
       └─ Generative candidate: LumaFlux
                    ↓
             Candidate HDR pool
```

理由：

- **RealRep / GMNet**：提供内容保真、稳定的低风险 target；
- **LumaFlux**：提供缺失高光 / perceptual HDR 的高质量候选，但只作为候选；
- **多 teacher 分歧** 本身可以作为 uncertainty / reliability signal。

---

<a id="pgt-pipeline"></a>
## 4. 推荐的 PGT 生成流程

### Step 1 — Real target-domain SDR

输入必须来自真实眼镜最终链路：

```text
Glass capture → ISP → TM → 8-bit SDR → codec → Real SDR clip
```

### Step 2 — Multi-teacher candidate generation

对每个 SDR clip / key frame 产生多个 HDR candidates：

```text
S_t
 ├─ RealRep → H_realrep
 ├─ GMNet → H_gainmap
 ├─ HDRTVDM → H_practical
 └─ LumaFlux (optional) → H_gen
```

### Step 3 — Reliability / source-consistency filtering

不要直接“选最漂亮”的 HDR。至少检查：

1. **Content fidelity**：边缘/纹理/identity 不应无依据改变；
2. **Highlight plausibility**：已 clipped 区域必须降低置信度；
3. **Shadow noise / texture**：不能把压缩噪声放大成 HDR detail；
4. **Tone / color naturalness**：避免过饱和、过亮、skin shift；
5. **Temporal consistency**：连续帧 tone / chroma / local contrast 不能闪烁；
6. **Teacher disagreement**：多个 teacher 差异大的区域标为 low-confidence。

### Step 4 — Confidence Mask，而不是整幅 PGT 全信

构造：

\[
M(x,t) \in [0,1]
\]

训练时：

\[
L_{PGT}=M\cdot L(\hat H,H_{PGT})
\]

对于：

- clipped highlight；
- heavy compression；
- motion/occlusion；
- teacher disagreement；
- generative hallucination region；

降低 \(M\)。

这比“选出一张 PGT 后整张图监督”更可靠。

### Step 5 — IQA / Verifier 用于排序，但不单独定义 GT

推荐组合：

- **Beyond8Bits / HDR-Q**：HDR-aware reasoning / NR quality；
- **BrightRate**：HDR-UGC NR quality；
- **source consistency**：SDR source 与 tone-mapped-back PGT 的结构/颜色一致性；
- **temporal metric**：连续窗口 flicker / local tone variation；
- 有真实参考的小规模 calibration set 上再使用 **HDR-VDP-3 / ColorVideoVDP / ΔE_ITP** 校准筛选规则。

> IQA 应作为 **candidate ranking / rejection / confidence estimation**，而不是把“模型喜欢”直接等同于真实 HDR GT。

### Step 6 — Student / target model fine-tuning

```text
Large synthetic paired data
          +
Real-glasses SDR + confidence-masked PGT
          +
Small true/reference HDR calibration set
          ↓
     Target Video HDR model
```

---

<a id="pgt-papers"></a>
## 5. 直接采用 PGT / Teacher-Pseudo-HDR 的参考论文

### 5.1 最直接：AAAI 2026 Semi-Supervised HDR

**Wei Jiang, Jiahao Cui, Yizheng Wu, Zhan Peng, Zhiyu Pan, Zhiguo Cao**  
**Semi-Supervised High Dynamic Range Image Reconstructing via Bi-Level Uncertain Area Masking**  
AAAI 2026  
Paper: https://ojs.aaai.org/index.php/AAAI/article/view/37461  
arXiv: https://arxiv.org/abs/2511.12939

核心机制：

```text
Limited LDR-HDR GT
       ↓
Teacher
       ↓
Pseudo HDR GT for unlabeled LDR
       ↓
Pixel-level uncertainty mask
+ Patch-level uncertainty mask
       ↓
Student learns only trusted pseudo-HDR regions
```

论文明确指出 pseudo HDR GT 会产生 confirmation bias，因此必须丢弃不可靠区域。作者报告只使用 **6.7% HDR GT** 时仍可达到与近期 fully-supervised 方法相近的性能。

**对我们的直接启发**：

> 真实眼镜 SDR 可以使用 PGT，但必须配套 **uncertainty / confidence mask**，尤其不能全信高光 clipping 区和生成式补全部分。

---

### 5.2 直接 HDR PGT：IJCV 2025 HIDD

**Qiang Wen, Zhefan Rao, Chenyang Lei, Wenxiu Sun, Qiong Yan, Jing Li, Fei Lei, Qifeng Chen**  
**Enhancing HDR Imaging with Joint Denoising and Deblurring**  
International Journal of Computer Vision, 2025  
Paper: https://link.springer.com/article/10.1007/s11263-025-02537-w  
Project: https://csqiangwen.github.io/projects/hdr-hidd/

核心机制：

```text
Static scenes with clean HDR GT
       ↓
Train HDR network
       ↓
Freeze a copy as Teacher
       ↓
Teacher generates clean/sharp pseudo HDR GT
for dynamic scenes
       ↓
Learnable network trains on dynamic PGT
```

这里 PGT 不是简单由 heuristic 生成，而是由**在可信 clean-GT domain 上训练过的 fixed network**产生。

**对我们的直接启发**：

> 先在 synthetic / true paired HDR 数据上训练一个高质量 teacher，再用它给真实眼镜 SDR 生成 PGT，比从零用 generative model 直接造 GT 更稳。

---

### 5.3 Synthetic→Real 的补充依据：ICLR 2026 S2R-HDR

**S2R-HDR: A Large-Scale Rendered Dataset for HDR Fusion**, Wang et al., ICLR 2026  
Paper: https://proceedings.iclr.cc/paper_files/paper/2026/hash/aeb0168e73ed5605b1b3695fed12be97-Abstract-Conference.html  
Project: https://openimaginglab.github.io/S2R-HDR/

它不是 PGT 论文，但明确证明：

> 大规模 synthetic HDR 数据仍存在 synthetic→real gap，需要专门的 S2R-Adapter 做真实域适配。

**对我们的作用**：支持“synthetic paired pretrain + real-glasses PGT/domain adaptation”这条双阶段数据路线。

---

### 5.4 PGT 风险参考：ICCV 2021

**On the Limits of Pseudo Ground Truth in Visual Camera Re-Localisation**, Brachmann et al., ICCV 2021  
Paper: https://openaccess.thecvf.com/content/ICCV2021/html/Brachmann_On_the_Limits_of_Pseudo_Ground_Truth_in_Visual_Camera_ICCV_2021_paper.html

虽然不是 HDR 任务，但它提供一个重要原则：

> PGT 会把 teacher/reference algorithm 的 bias 带入最终 benchmark / student；越接近 teacher 的方法越可能被偏爱。

因此我们的 PGT 不能用“同一个 teacher 生成 GT，再用同风格 metric 验证”形成自闭环。

---

<a id="project-recommendation"></a>
## 6. 当前项目建议

### 推荐方案 A — 最稳妥（首选）

```text
Synthetic paired HDR data
        ↓
Train RealRep/GMNet-like teacher
        ↓
Real glasses SDR
        ↓
Teacher generates PGT
        ↓
Confidence mask + temporal consistency filtering
        ↓
Fine-tune target Video HDR model
```

**优点**：保真、低 hallucination、工程可解释。  
**对应参考**：AAAI 2026 uncertainty-masked pseudo HDR + IJCV 2025 fixed-teacher PGT。

### 推荐方案 B — 多候选 PGT（质量优先）

```text
Real SDR
  ↓
RealRep / GMNet / HDRTVDM / LumaFlux
  ↓
Multiple HDR candidates
  ↓
HDR-Q / BrightRate
+ source consistency
+ temporal consistency
+ teacher disagreement
  ↓
Select / fuse only high-confidence regions
  ↓
PGT
```

适合研发阶段构造困难样本，但**LumaFlux 只作为 candidate generator，不作为唯一 teacher**。

### 推荐方案 C — 产品 Teacher

如果合作方已有高质量离线 HDR pipeline：

```text
Real glasses SDR → Existing high-quality offline HDR pipeline → PGT
```

这往往比通用公开模型更适合产品 target，因为它直接定义了“我们最终想复现的 HDR rendering”。

同时保留少量公开模型候选做 cross-check，防止 PGT 继承现有 pipeline 的系统性 artifact。

---

<a id="pgt-limitations"></a>
## 7. PGT 使用边界

1. **PGT ≠ Physical HDR GT**：尤其在 SDR 已 clipping 的区域，teacher 只能估计/生成 plausible HDR。
2. **必须保留 PGT provenance**：teacher 名称、版本、参数、HDR 表示、IQA 分数、confidence mask。
3. **视频 PGT 不能逐帧独立生成后直接训练**：必须加入 temporal consistency / clip-level screening。
4. **生成式模型输出不能整图全信**：只允许高置信区域参与监督，或者只用作 candidate / upper-bound reference。
5. **IQA ≠ GT generator**：IQA 负责筛选和定权，不能单独证明 HDR target 是真实的。
6. **必须保留 small true/reference set**：用于校准 teacher bias、IQA threshold 和 PGT reliability。

### 最终推荐的数据闭环

```text
A. Real HDR → ISP/Codec-aware synthetic SDR
                 │
                 └──── large-scale paired pretrain

B. Real glasses SDR → Multi-teacher → confidence-masked PGT
                 │
                 └──── target-domain adaptation

C. Small synchronized/reference HDR set
                 │
                 └──── calibration + final evaluation
```

对当前项目，**PGT 最合理的定位是“真实眼镜 domain 的弱监督”，不是替代真实 HDR GT。**
