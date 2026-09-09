# HDR Data Taxonomy for SDR→HDR / Video HDR

> Last checked: 2026-09-09  
> Scope: data construction for **SDR→HDR / inverse tone mapping / Video HDR**, with emphasis on the current project: **same-EV, 8-bit compressed SDR video from smart glasses → HDR on phone**.

## 目录

- [1. 总览：HDR 数据一般分哪几类](#overview)
- [2. A类：真实 HDR → 合成 SDR](#class-a)
  - [2.1 真实 HDR 母数据的来源](#hdr-source-types)
  - [2.2 从 HDR 合成 SDR 的五个层级](#sdr-synthesis)
- [3. B类：真实 SDR + 真实 HDR Pair](#class-b)
  - [3.1 Existing delivery pair](#delivery-pair)
  - [3.2 Professional independent grading pair](#grading-pair)
  - [3.3 Physical camera SDR/HDR pair](#physical-pair)
- [4. C类：真实多曝光输入 + HDR GT](#class-c)
- [5. D类：真实 SDR + Pseudo HDR](#class-d)
- [6. 四类数据的真实性与适用性对比](#comparison)
- [7. 当前项目建议的数据组合](#project-recommendation)
- [8. 关键数据集示例](#examples)
- [9. 使用数据时必须明确的标签](#metadata)
- [10. 论文 / 官方资源链接](#references)

---

<a id="overview"></a>
## 1. 总览：HDR 数据一般分哪几类

从 **“SDR 和 HDR 分别是怎么来的”** 出发，训练 / 测试数据最清楚可以分为四类：

```text
                         SDR→HDR Data
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
          ▼                   ▼                   ▼
 A. Real HDR             B. Real SDR/HDR     C. Real Multi-
 + Synthetic SDR             Pair              Exposure HDR
          │                   │                   │
          │           ┌───────┼────────┐          │
          │           ▼       ▼        ▼          │
          │       Delivery  Pro-grade  Physical   │
          │        Pair      Pair      Pair        │
          │
          └────────────────────────────────────────────┐
                                                       ▼
                                           D. Real SDR + Pseudo HDR
```

### 一句话判断

- **A 类**：最容易规模化，适合做大规模训练；风险是 synthetic→real domain gap。
- **B 类**：最有价值，但“真实 pair”内部差异很大，必须说明 pair 是怎样建立的。
- **C 类**：物理信息最充分，但输入假设通常是多曝光，不等同于 same-EV SDR→HDR。
- **D 类**：目标域最真实，工程上很实用；但 HDR target 不是严格物理 GT。

---

<a id="class-a"></a>
## 2. A类：真实 HDR → 合成 SDR

这是当前 SDR→HDR / ITM 最常见的数据构造方式。

```text
Real HDR source H
        ↓
Synthetic SDR formation D(·)
        ↓
Synthetic SDR S
        ↓
(S, H) paired training data
```

数学上可写成：

\[
S = D(H; \theta)
\]

其中 \(H\) 是真实 HDR 内容，\(D\) 是人为定义的 SDR formation / degradation pipeline，\(\theta\) 是曝光、Tone Mapping、CRF、量化、压缩等参数。

<a id="hdr-source-types"></a>
### 2.1 真实 HDR 母数据的来源

| HDR 来源 | 原始 HDR 怎么得到 | 代表数据 | 优点 | 局限 | 对当前项目价值 |
|---|---|---|---|---|---|
| **Professional HDR Master / Graded HDR** | 影视制作 / DI / mastering 流程直接生成 PQ / HLG HDR master | Netflix **Sol Levante**、部分影视 HDR content | HDR rendering、色彩、峰值亮度较规范 | 内容偏 PGC / cinematic，不等于 camera scene GT | **高：作为 HDR rendering / color target** |
| **Consumer HDR UGC** | 手机等消费设备直接拍摄 HLG / PQ HDR video | **LIVE UGC-HDR**, CHUG source | 内容分布接近日常拍摄、运动、曝光变化、真实 UGC | SDR counterpart 通常没有现成 GT | **很高：最接近眼镜/手机消费场景** |
| **Professional / Multi-sensor HDR Capture** | 双机、多传感器或专用 HDR camera 直接捕获高动态范围视频 | **HdM-HDR-2014**, **LiU HDRv**, MPI-HDRv | HDR 动态范围可信，可作为高质量 HDR mother data | 设备、场景分布偏实验 / cinematic | **很高：尤其适合 controlled temporal synthesis** |
| **Multi-exposure HDR Reconstruction** | 同一场景拍摄不同曝光，再做对齐/融合得到 HDR | Fairchild HDRPS、Kalantari17 等 | HDR GT 与曝光物理关系清楚 | 动态场景可能有 motion / merge artifact；常见于 image | **中：适合单图/物理验证** |
| **CG / Rendered HDR** | 渲染器直接输出 scene-linear HDR / EXR | Synthetic / CG datasets | GT 完全可控，容易覆盖极端场景 | 与真实 optics / ISP / sensor 分布差异大 | **中低：用于补 coverage，不宜单独证明泛化** |

### 代表性的真实 HDR mother data

#### HdM-HDR-2014

- 来源：Hochschule der Medien Stuttgart。
- 类型：真实 cinematic HDR video。
- 采集：专业电影摄影机 + 双曝光 / mirror rig HDR capture。
- 动态范围：最高约 18 stops。
- 特点：专门包含高光进出画面、brightness change、skin、specular、饱和颜色等 HDR 难例。
- 适合：从同一真实 HDR video 人为生成 **Fixed-EV / AE-varying / bracketed** SDR，用于受控 temporal ablation。
- Dataset: https://www.hdm-stuttgart.de/vmlab/hdm-hdr-2014/

#### LiU HDRv

- 来源：Linköping University HDR Video Repository。
- 类型：真实 HDR video，OpenEXR。
- 采集：多传感器 HDR camera；原系统约 2336×1752、最高 30 fps、>24 f-stops，公开版本常为 1280×720 OpenEXR。
- 特点：经典 HDR-video source，长期被 HDR reconstruction / tone mapping 工作复用。
- 适合：扩充真实 HDR scene diversity，与 HdM 共同作为 synthetic SDR 的 HDR GT。
- Repository: https://computergraphics.on.liu.se/hdrv_itn_liu/Resources.php

#### LIVE UGC-HDR

- 类型：真实消费级 HDR UGC 视频。
- 基本规模：2,153 个 HDR source videos。
- 来源：iPhone amateur-user HDR capture，包含 HLG / Rec.2100 consumer content。
- 适合：生成更接近真实 UGC 的 SDR training distribution。
- Dataset: https://live.ece.utexas.edu/research/LIVE_UGC_HDR/index.html

---

<a id="sdr-synthesis"></a>
### 2.2 从 HDR 合成 SDR 的五个层级

#### Level A — Simple Tone Mapping

最简单形式：

\[
S = T(H)
\]

典型操作：

- Reinhard / Hable / Drago 等 global TMO；
- simple shoulder / toe；
- gamma；
- saturation / exposure variation。

```text
HDR
 ↓
Global TMO
 ↓
SDR
```

**优点**：简单、便宜、容易规模化。  
**问题**：很容易学成某个固定 \(T^{-1}\)，与真实 camera ISP 差距大。

---

#### Level B — Multi-TMO / Multi-style SDR

```text
                  ┌─ TMO 1
HDR ──────────────┼─ TMO 2
                  ├─ TMO 3
                  ├─ ...
                  └─ TMO N
```

进一步变化：

- global / local TMO；
- shoulder / toe strength；
- saturation；
- spatial strength；
- temporal mode。

**代表思路**：LIVE-TMHDR、LumaFlux data pipeline。  
**价值**：避免模型只拟合一个 Tone Mapping inverse，提升未知前端 TM 的鲁棒性。

---

#### Level C — Camera Imaging Model

比简单 TMO 更物理：

\[
S = Q\left[f\left(\operatorname{clip}(E\cdot H + n)\right)\right]
\]

其中：

- \(E\)：Exposure；
- \(n\)：Noise；
- `clip`：sensor / signal clipping；
- \(f\)：CRF / Gamma；
- \(Q\)：8-bit quantization。

```text
HDR radiance
   ↓
Exposure
   ↓
Noise
   ↓
Clipping
   ↓
CRF / Gamma
   ↓
Quantization
   ↓
8-bit SDR/LDR
```

**代表场景**：AIM 2025 ITM、VITM-TC 等 synthetic LDR protocol。  
**适合研究**：clipped highlight、exposure ambiguity、CRF inversion。

---

#### Level D — ISP-like Synthetic SDR

对当前眼镜项目更理想：

```text
HDR
 ↓
Exposure / AE
 ↓
Tone Mapping / Local TM
 ↓
Color / CCM / WB
 ↓
Denoise
 ↓
Sharpen
 ↓
Gamut Compression
 ↓
8-bit Quantization
 ↓
H.264 / H.265 Compression
 ↓
Synthetic glasses SDR
```

可抽象为：

\[
S = D_{ISP+Codec}(H; \theta)
\]

其中：

\[
\theta = \{EV, TM, CCM, AWB, DNR, Sharpen, Gamut, Quant, Codec, ...\}
\]

**这是当前项目最值得建设的数据引擎方向。**  
目标不是“模拟所有 ISP”，而是让 synthetic SDR 的信息损失与真实眼镜 SDR 尽可能接近。

---

#### Level E — Video-aware Synthetic SDR

除了空间退化，还要显式控制时间参数 \(\theta_t\)。

##### Fixed-EV

```text
Frame:  t-2   t-1   t   t+1   t+2
EV:      0     0    0    0     0
TM:     TM0   TM0  TM0  TM0   TM0
```

用于回答：

> **严格 same-EV 多帧究竟能增加多少真实信息？**

##### Smooth AE variation

```text
EV:  0 → -0.2 → -0.5 → -0.3 → 0
```

用于模拟普通相机 AE history。

##### Exposure-diverse / bracket-like

```text
EV:  0 → -1 → 0 → -1 → 0
```

用于研究 temporal exposure complementarity，但**不应与 Fixed-EV 结果混为一谈**。

##### TM / ISP temporal variation

可以单独改变：

- TM strength；
- local contrast；
- saturation / WB；
- denoise / sharpening；
- codec state。

用于研究 flicker、history stability、reference switching。

---

<a id="class-b"></a>
## 3. B类：真实 SDR + 真实 HDR Pair

“真实 pair”必须继续细分，不能简单写成 `Real SDR/HDR GT`。

<a id="delivery-pair"></a>
### 3.1 Existing Delivery Pair

```text
Original content
   ├─ Existing real SDR delivery
   └─ Existing real HDR delivery
```

特点：

- SDR 和 HDR 都是真实存在的成品版本；
- 中间 mastering / grading / transcoding pipeline 往往不完全可知；
- 两个版本可能并非严格 pixel-perfect 同源处理。

代表：

- **HDRTV1K**（公开 SDRTV→HDRTV baseline 常用数据）。

适合：

- public benchmark；
- output-to-output SDR→HDR mapping；
- 预训练 / 横向论文比较。

不适合宣称：

> HDR = 原始场景 radiance GT。

---

<a id="grading-pair"></a>
### 3.2 Professional Independent Grading Pair

```text
Same source / master
        │
        ├─ Professional SDR grading → SDR
        │
        └─ Professional HDR grading → HDR
```

特点：

- SDR / HDR 都是人为真实制作的；
- 不是“先有 HDR，再用算法 TMO 生成 SDR”；
- 更接近专业制作中“好的 SDR / HDR 应该怎样表达”。

代表：

- **xDR Dataset**：同一内容 native SDR / HDR grading；
- **HDRMovie7K**：cinematic / DCDM-related SDR-HDR mapping。

适合：

- 检查 synthetic TMO inverse 是否偏离真实 grading；
- 研究 brightness / chroma / gamut mapping；
- 作为 perceptual / rendering target。

局限：

> HDR target 是 **creative / mastered target**，不是 physical scene GT。

---

<a id="physical-pair"></a>
### 3.3 Physical Camera SDR/HDR Pair

这是当前项目最理想、但公开数据最少的一类：

```text
                         ┌─ Target glasses / SDR pipeline
Scene / optics / time ───┤        ↓
                         │     Real 8-bit SDR
                         │
                         └─ HDR reference capture
                                  ↓
                             HDR reference
```

理想条件：

- 同一时刻 / 高时间同步；
- 同视角或可高精度几何对齐；
- reference HDR 有足够动态范围；
- 亮度 / 色彩 reference 明确；
- 能记录 target camera 的真实 ISP + codec output。

得到：

\[
(S_{real\ glasses}, H_{reference})
\]

这类数据最能验证：

> 从真实眼镜 SDR 到可信 HDR reference 的实际恢复能力。

**对当前项目价值：S++，建议通过自采平台建立。**

---

<a id="class-c"></a>
## 4. C类：真实多曝光输入 + HDR GT

```text
Short exposure
Long exposure
Short exposure
       ↓
Alignment / fusion / HDR GT
```

或者 RAW：

```text
RAW EV-3
RAW EV0
   ↓
HDR reference
```

代表：

- **DeepHDRVideo**；
- **Real-HDRV**；
- Kalantari dynamic HDR datasets。

特点：

- LDR/RAW 输入是真实采集；
- HDR reference 也有较强物理依据；
- exposure diversity 真实存在。

价值：

- multi-exposure alignment；
- motion / ghosting；
- exposure fusion；
- future capture-side HDR design。

但对当前项目必须明确：

> **Alternating / bracketed exposure ≠ Same-EV compressed SDR video。**

因此不能直接拿这类 benchmark 的 PSNR 与当前算法做公平比较。

---

<a id="class-d"></a>
## 5. D类：真实 SDR + Pseudo HDR

这是产品工程中非常现实的一类：

```text
Real glasses SDR
       ↓
High-quality teacher / existing HDR pipeline /
professional grading / generator / PGT selector
       ↓
Pseudo HDR target
```

例如：

- 当前已有厂商 HDR pipeline output；
- offline high-quality HDR model；
- professional colorist output；
- LumaFlux / diffusion HDR candidate；
- 多候选 + HDR-IQA / human selection 得到的 PGT。

形成：

\[
(S_{real}, H_{pseudo})
\]

优点：

- **输入 domain 100% 是目标眼镜真实 SDR**；
- 能直接用于 target-domain adaptation；
- 很适合产品型“目标 HDR rendering”任务。

局限：

- HDR target 不是严格 physical ground truth；
- teacher bias / generator hallucination 会进入训练；
- 必须标注为 `Pseudo / Teacher / Target Rendering`，不能写成 Scene GT。

---

<a id="comparison"></a>
## 6. 四类数据的真实性与适用性对比

| 类型 | SDR 是否真实 | HDR 是否真实 | Pair 是否物理严格 | 是否易规模化 | 主要价值 | 当前项目适用度 |
|---|---:|---:|---:|---:|---|---:|
| **A. Real HDR + Synthetic SDR** | 否 | 是 | 是（synthetic mapping 已知） | **高** | 大规模训练、controlled ablation | **S** |
| **B1. Existing SDR/HDR delivery pair** | 是 | 是 | 通常否 | 中高 | 公共 benchmark / output mapping | **A** |
| **B2. Professional SDR/HDR grading pair** | 是 | 是 | 不追求 scene-physical GT | 低 | 真实 HDR rendering target | **A/S-评价** |
| **B3. Physical camera SDR/HDR pair** | 是 | 是 | **最高** | **低** | target-device 真正恢复 / 验收 | **S++** |
| **C. Real multi-exposure + HDR GT** | 是 | 是 | 高 | 中低 | 多曝光 reconstruction / future capture | **C（当前）/ A（未来）** |
| **D. Real SDR + Pseudo HDR** | **是** | Pseudo | 否 | 中高 | target-domain adaptation / PGT | **S-工程** |

### 重要原则

1. `Real HDR` 不代表 `Real SDR/HDR pair`。
2. `Real SDR/HDR pair` 不代表 `physical scene GT`。
3. Professional grading HDR 是可信的 **rendering target**，不是场景辐射真值。
4. Multi-exposure HDR 数据虽然物理信息强，但输入条件与 same-EV SDR 不同。
5. Pseudo HDR 可以非常有工程价值，但必须与真实 GT 分开命名。

---

<a id="project-recommendation"></a>
## 7. 当前项目建议的数据组合

当前项目不建议等待一个“完美的大规模真实 SDR/HDR 数据集”，而应组合不同数据类型。

### 7.1 大规模训练主体

> **Real HDR → diverse ISP-aware synthetic SDR**

建议 HDR source pool：

```text
Consumer HDR UGC
LIVE UGC-HDR / CHUG source
       +
Professional / cinematic HDR
Sol Levante / other HDR masters
       +
Real HDR capture
HdM / LiU / MPI
```

再通过：

```text
Multi-TMO
+ Exposure / clipping / CRF
+ Local TM / color / gamut
+ Denoise / sharpen
+ 8-bit quantization
+ H.264/H.265 compression
+ Video temporal variation
```

生成 synthetic glasses SDR。

---

### 7.2 Target-domain adaptation

> **Real glasses SDR + high-quality pseudo / teacher HDR**

用于：

- 缩小 synthetic→real gap；
- 针对真实眼镜 hard cases；
- 产品风格对齐。

---

### 7.3 高价值自采 GT

> **Real glasses SDR + synchronized HDR reference**

规模可以小，但应重点覆盖：

- strong backlight；
- night lights / specular；
- indoor→outdoor；
- skin + bright background；
- head motion；
- highlight entering/leaving frame；
- codec difficult scenes。

这部分应该作为最终模型选择和验收的核心证据。

---

### 7.4 Controlled temporal experiment

利用 HdM / LiU 等真实 HDR mother video，针对同一 HDR sequence 人工生成三组输入：

```text
A. Fixed-EV
EV0 EV0 EV0 EV0 EV0

B. Smooth AE-varying
0 -0.2 -0.5 -0.3 0

C. Exposure-diverse
0 -1 0 -1 0
```

然后比较：

```text
Single-frame
vs
Multi-frame
```

回答真正的问题：

> **Same-EV temporal information 到底贡献了 texture / denoise / visibility recovery，还是只有稳定作用？**

---

<a id="examples"></a>
## 8. 关键数据集示例

| 数据 | 分类 | 原始数据怎么得到 | SDR/HDR 关系 | 适合当前项目做什么 |
|---|---|---|---|---|
| **LIVE UGC-HDR** | A-HDR source | iPhone 等 consumer HDR UGC capture | 只有真实 HDR source；SDR 需自行合成 | **最适合构造消费场景 synthetic SDR** |
| **HdM-HDR-2014** | A-HDR source | 双机 / 不同曝光专业 cinematic HDR capture | HDR 真实；SDR 常由后续论文合成 | **Controlled temporal synthesis** |
| **LiU HDRv** | A-HDR source | 多传感器 HDR video camera | HDR 真实；SDR 需合成 | 扩充 HDR video scene diversity |
| **Netflix Sol Levante** | A-HDR source | 专业原生 4K HDR production / mastering | 真实 HDR master | HDR rendering / mastering sanity check |
| **LIVE-TMHDR** | A/B-like | 真实 HDR source 经多 TMO、空间/时间设置及专业 colorist 生成 SDR variants | HDR 真实；多数 SDR 为 TMO / expert rendered | **未知 Tone Mapping 鲁棒性** |
| **HDRTV1K** | B1 | 公开 SDRTV / HDRTV paired content | SDR/HDR 都是真实 delivery，非 scene-physical pair | 公共 baseline / 预训练 |
| **xDR** | B2 | 同内容分别做 native SDR / HDR professional grading | **真实独立 grading pair** | **真实 rendering target / evaluation** |
| **HDRMovie7K** | B2 | cinematic / professional SDR-HDR workflow | professional paired rendering | 检查 synthetic mapping 偏差 |
| **Real-HDRV** | C | RAW multi-exposure real capture + HDR labels | 真实多曝光输入 + HDR GT | future capture / alignment，不直接做 same-EV benchmark |
| **DeepHDRVideo** | C | real + synthetic alternating-exposure HDR video | 多曝光条件 | architecture reference |
| **Real glasses SDR + teacher HDR** | D | 真实产品 SDR + offline/teacher HDR | SDR 真实，HDR pseudo | **Target-domain adaptation** |
| **Real glasses SDR + synchronized HDR reference** | B3 | 自采同步 SDR / HDR reference | 最接近 physical pair | **最终验收 / 高价值 fine-tuning** |

---

<a id="metadata"></a>
## 9. 使用数据时必须明确的标签

任何新数据进入项目时，至少记录以下字段：

```text
Dataset / Source name
Task
HDR origin
SDR origin
Capture device / rendering pipeline
Real vs synthetic SDR
Real vs pseudo HDR
Exposure relationship
Same-EV / AE-varying / bracketed
Color space / transfer function
Bit depth
Compression
Temporal continuity
Pair alignment quality
GT type
Train / val / test role
Can be used for FR metric?
Can prove real-camera generalization?
```

推荐统一使用以下 GT 标签，避免概念混淆：

- `Scene / Physical HDR Reference`
- `Captured HDR Reference`
- `Professional HDR Grading Target`
- `Existing HDR Delivery`
- `Synthetic HDR Target`
- `Teacher / Pseudo HDR`

### 最终项目数据策略

```text
Large-scale:
Real HDR → ISP-aware synthetic SDR

+

Target-domain:
Real glasses SDR → Pseudo / teacher HDR

+

High-value validation:
Real glasses SDR ↔ synchronized HDR reference
```

这三层组合，比单独依赖某一种公开数据，更适合当前 **same-EV compressed SDR video → mobile HDR** 项目。

---

<a id="references"></a>
## 10. 论文 / 官方资源链接

> 原则：优先给正式论文页；没有独立 canonical dataset paper 的数据集给官方 repository / project page。

### A. Real HDR mother data / SDR synthesis

- **HdM-HDR-2014**  
  Paper: *Creating cinematic wide gamut HDR-video for the evaluation of tone mapping operators and HDR-displays* — Fröhlich et al., SPIE 2014.  
  Dataset / project: https://www.hdm-stuttgart.de/vmlab/hdm-hdr-2014/

- **LiU HDRv**  
  Official HDR Video Repository: https://computergraphics.on.liu.se/hdrv_itn_liu/HDRv.php  
  Resources: https://computergraphics.on.liu.se/hdrv_itn_liu/Resources.php  
  Note: LiU HDRv is generally cited via the official repository rather than one single canonical dataset paper.

- **MPI HDRv**  
  Historical HDR video source used by HDRCNN / STPN / VITM-TC and related work.  
  For current research comparison, see VITM-TC: https://openaccess.thecvf.com/content/CVPR2024/html/Ye_Deep_Video_Inverse_Tone_Mapping_Based_on_Temporal_Clues_CVPR_2024_paper.html

- **LIVE UGC-HDR**  
  Official dataset: https://live.ece.utexas.edu/research/LIVE_UGC_HDR/index.html

- **CHUG**  
  Paper: *CHUG: Crowdsourced User-Generated HDR Video Quality Dataset* — Saini et al., ICIP 2025.  
  Paper: https://arxiv.org/abs/2510.09879  
  Project: https://shreshthsaini.github.io/CHUG/

- **Netflix Sol Levante**  
  Official Netflix Open Content: https://opencontent.netflix.com/

- **Fairchild HDR Photographic Survey**  
  Paper: *The HDR Photographic Survey* — Mark D. Fairchild, CIC 2007.  
  Paper: https://library.imaging.org/cic/articles/15/1/art00044  
  Dataset / HDR resources: https://markfairchild.org/HDR.html

- **Kalantari17**  
  Paper: *Deep High Dynamic Range Imaging of Dynamic Scenes* — Kalantari & Ramamoorthi, SIGGRAPH 2017.  
  Project / paper / dataset: https://cseweb.ucsd.edu/~viscomp/projects/SIG17HDR/

### B. Multi-TMO / camera-model synthetic SDR

- **LIVE-TMHDR**  
  Paper: *Subjective Quality Assessment of Compressed Tone-Mapped High Dynamic Range Videos* — Venkataramanan & Bovik, IEEE TIP 2024.  
  Paper: https://arxiv.org/abs/2403.15061  
  Dataset: https://live.ece.utexas.edu/research/LIVE_TMHDR/index.html

- **LumaFlux**  
  Paper: *LumaFlux: Lifting 8-Bit Worlds to HDR Reality with Physically-Guided Diffusion Transformers* — Saini et al., 2026.  
  Paper: https://arxiv.org/abs/2604.02787  
  Code: https://github.com/shreshthsaini/LumaFlux

- **AIM 2025 ITM Challenge**  
  Paper: *AIM 2025 challenge on Inverse Tone Mapping: Report, Methods and Results* — ICCV Workshops 2025.  
  Paper: https://openaccess.thecvf.com/content/ICCV2025W/AIM/html/Wang_AIM_2025_challenge_on_Inverse_Tone_Mapping_Report_Methods_and_ICCVW_2025_paper.html

- **VITM-TC synthetic protocol**  
  Paper: *Deep Video Inverse Tone Mapping Based on Temporal Clues* — Ye et al., CVPR 2024.  
  Paper: https://openaccess.thecvf.com/content/CVPR2024/html/Ye_Deep_Video_Inverse_Tone_Mapping_Based_on_Temporal_Clues_CVPR_2024_paper.html  
  Code: https://github.com/ye3why/VITM-TC/

### C. Real SDR / HDR paired or professionally graded data

- **HDRTV1K**  
  Paper: *A New Journey From SDRTV to HDRTV* — Chen et al., ICCV 2021.  
  Paper: https://openaccess.thecvf.com/content/ICCV2021/html/Chen_A_New_Journey_From_SDRTV_to_HDRTV_ICCV_2021_paper.html  
  Code / dataset: https://github.com/chxy95/HDRTVNet

- **xDR Dataset**  
  Paper: *The xDR dataset: A cinematic natively graded HDR & SDR dataset for evaluation of inverse tone mapping methods* — Luzardo et al., Signal Processing: Image Communication 2026.  
  Paper: https://www.sciencedirect.com/science/article/pii/S0923596526000536

- **HDRMovie7K / HDRMovie1K**  
  Paper: *HDRMovieformer: A Transformer Framework and Benchmark for Cinematic SDR-to-HDR Conversion* — Li et al., AAAI 2026.  
  Paper: https://ojs.aaai.org/index.php/AAAI/article/view/37578

### D. Real multi-exposure HDR video

- **DeepHDRVideo**  
  Paper: *HDR Video Reconstruction: A Coarse-To-Fine Network and a Real-World Benchmark Dataset* — Chen et al., ICCV 2021.  
  Paper: https://openaccess.thecvf.com/content/ICCV2021/html/Chen_HDR_Video_Reconstruction_A_Coarse-To-Fine_Network_and_a_Real-World_Benchmark_ICCV_2021_paper.html  
  Dataset/code: https://github.com/guanyingc/DeepHDRVideo-Dataset/

- **Real-HDRV**  
  Paper: *Towards Real-World HDR Video Reconstruction: A Large-Scale Benchmark Dataset and A Two-Stage Alignment Network* — Shu et al., CVPR 2024.  
  Paper: https://openaccess.thecvf.com/content/CVPR2024/html/Shu_Towards_Real-World_HDR_Video_Reconstruction_A_Large-Scale_Benchmark_Dataset_and_CVPR_2024_paper.html

- **Kalantari13 HDR Video**  
  Paper: *Patch-Based High Dynamic Range Video* — Kalantari et al., SIGGRAPH Asia / ACM TOG 2013.  
  Project / paper / dataset: https://web.ece.ucsb.edu/~psen/PaperPages/HDRVideo/

### E. 与当前 same-EV Video HDR 最值得优先阅读的 6 篇

1. **A New Journey From SDRTV to HDRTV** — HDRTV1K / SDR→HDR baseline  
   https://openaccess.thecvf.com/content/ICCV2021/html/Chen_A_New_Journey_From_SDRTV_to_HDRTV_ICCV_2021_paper.html
2. **Subjective Quality Assessment of Compressed Tone-Mapped HDR Videos** — LIVE-TMHDR / 多 TMO  
   https://arxiv.org/abs/2403.15061
3. **Deep Video Inverse Tone Mapping Based on Temporal Clues** — Video temporal clue  
   https://openaccess.thecvf.com/content/CVPR2024/html/Ye_Deep_Video_Inverse_Tone_Mapping_Based_on_Temporal_Clues_CVPR_2024_paper.html
4. **HDRMovieformer** — professional SDR/HDR grading / cinematic pair  
   https://ojs.aaai.org/index.php/AAAI/article/view/37578
5. **Real-HDRV** — real-data vs synthetic-data gap / capture-side HDR  
   https://openaccess.thecvf.com/content/CVPR2024/html/Shu_Towards_Real-World_HDR_Video_Reconstruction_A_Large-Scale_Benchmark_Dataset_and_CVPR_2024_paper.html
6. **LumaFlux** — large-scale HDR-source → diverse synthetic SDR data engine  
   https://arxiv.org/abs/2604.02787
