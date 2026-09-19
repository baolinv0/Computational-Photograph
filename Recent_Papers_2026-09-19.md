# Recent Imaging Papers — 2026-09-19

本页记录自上次检查后新公开、且对 IQA / RAW / ISP / 计算摄影具有较高研究价值的两篇工作。重点不做摘要堆叠，而是分析其问题定义、真正技术增量、证据边界、横向关系，以及对当前 ISP / IQA / Pseudo-GT / Camera-Agent 研究的迁移价值。

---

## 1. MOSAIQ-500K and MOSAIQ-Bench

**Authors:** Wenbo Yang, Zhongling Wang, Jialu Xu, Jinghan Zhou, Zhou Wang  
**Affiliation:** University of Waterloo / Samsung AI Center-Toronto  
**First public:** 2026-09-17  
**Verdict:** **GO**

### Core problem

现有 IQA 数据集往往来自：

- 不同受试者群体
- 不同显示环境
- 不同打分范围
- 不同 MOS / DMOS 协议
- 不同 distortion / content distribution

因此：

```
Dataset A: MOS = 80
Dataset B: MOS = 80
```

并不意味着两张图在人眼上具有相同质量。

传统 multi-dataset IQA 往往采用：

- 每数据集独立 normalization
- pairwise ranking
- dataset-specific head
- coarse label alignment

但这些方案没有真正解决：

> **不同数据集的 ground-truth quality scale 本身不一致。**

---

### Real technical increment

MOSAIQ 的核心贡献不是一个新 backbone，而是重新定义 **cross-dataset IQA evaluation**。

作者从 26 个 IQA 数据集中重新采样图像，并进行统一主观实验：

- 1,039 张初始图像
- 最终保留 919 张
- 40 名受试者
- 36,760 个 subjective ratings

利用这些共同评分作为 **cross-dataset anchors**，学习严格单调 score mapping，并将 23 个 IQA dataset 映射到统一质量尺度。

最终构建：

```
MOSAIQ-500K
> 500K images
> common perceptual quality scale
```

同时提出 **MOSAIQ-Bench**，在统一质量轴上直接比较不同 IQA 模型。

真正改变的是：

```
Before:
evaluate SRCC inside each dataset

Now:
evaluate whether a model preserves
a common quality ordering across datasets
```

---

### Key evidence

统一尺度训练后：

- **MonotonicIQA**
  - unseen-set inter-dataset SRCC:
  - 0.7836 → **0.8591**

- **LIQE**
  - 0.7262 → **0.7912**

甚至普通 HyperIQA 在没有专门 multi-dataset architecture 的情况下，也能从统一 score calibration 获益。

论文还得到一个非常重要的反例：

> **intra-dataset SRCC 高，并不意味着模型拥有正确的 cross-domain quality scale。**

有些模型在每个独立数据集里表现很好，但把所有图像 pooled 到统一质量轴后排序明显恶化。

---

### Evidence strength

**High**

原因：

1. 它不是依赖某个特定 backbone 的性能增益；
2. 问题来自 IQA 数据监督本身；
3. 覆盖 23 个数据集和 31 个 IQA 方法；
4. 对训练、测试协议和 cross-domain evaluation 都有直接影响。

但需要注意：

MOSAIQ 主要解决 **technical perceptual quality scale alignment**，并不意味着 HDR、Retouch、生成式增强、人像审美都可以压缩成同一个 scalar quality axis。

---

### Relation to recent IQA work

近期 IQA 有两条同时发展的主线。

#### Line A — Unified quality scale

```
MOSAIQ
→ align labels across datasets
→ make cross-dataset quality comparable
```

#### Line B — Task-specific quality decomposition

```
Grounding-IQA
→ Zoom-IQA
→ GS-IQA
→ HDR-VLM
→ MCIQA-2K
```

这些工作强调：

```
quality depends on:
region
task
semantic correctness
rendering intent
failure type
```

因此两条路线不是冲突，而是解决不同问题：

```
MOSAIQ:
"Are labels calibrated?"

Task-specific IQA:
"What should be judged?"
```

---

### Implication for our IQA / Pseudo-GT work

当前 Tone Mapping / Retouch / PGT 数据往往来自：

- 不同实验 batch
- 不同 camera / phone
- 人评
- VLM judge
- reference / non-reference 模式
- 不同评分尺度

如果直接拼接：

```
Dataset A score
+
Dataset B score
+
VLM score
```

很容易制造假的 global ranking。

更合理的做法是增加：

```
Cross-dataset Anchor Set
        ↓
Score Calibration
        ↓
Common Quality Axis
        ↓
Pairwise / PGT Ranking
```

对于 HDR 则建议单独建立 **HDR-native anchor scale**，不要直接和 SDR MOS 混用。

### Research takeaway

在继续优化 IQA architecture 之前，应先确认：

```
Are the labels themselves aligned?
```

很多 cross-dataset failure 可能不是模型不够强，而是监督标尺本身没有统一。

---

## 2. RawSLAM: Online HDR Gaussian SLAM from Linear Radiance

**Authors:** Marina Orozco González, Luis Merino  
**Affiliation:** Universidad Pablo de Olavide  
**First public:** 2026-09-17  
**Verdict:** **PROBE↑**

### Core problem

传统视觉系统通常使用：

```
RAW
 ↓
ISP
 ↓
Tone Mapping / Gamma
 ↓
8-bit sRGB
 ↓
SLAM / Detection / Tracking
```

但经过 ISP 后：

- highlight radiance 可能被压缩或 clipping
- shadow precision 被量化
- gamma / tone mapping 改变 photometric relation
- scene-linear information 不可逆丢失

RawSLAM 提出的问题是：

> **如果机器任务真正需要 radiometric information，为什么必须等 ISP 把这些信息丢掉之后再处理？**

---

### Real technical increment

论文提出在线 Gaussian SLAM，直接工作在：

```
16-bit linear HDR radiance
```

而不是 tone-mapped 8-bit RGB。

核心机制包括：

### 1. Log-domain Gaussian color representation

HDR radiance 跨多个数量级，直接在线性值上优化容易让高亮区域主导梯度。

因此将 Gaussian color 写入 log domain，使不同亮度区间拥有更均衡的 relative update。

---

### 2. Differentiable range compression inside the loss

作者在 photometric loss 内使用可微 Reinhard compression：

```
linear HDR
→ differentiable compression
→ loss
```

目的是让 optimizer 保留 HDR 信息，同时避免高亮像素完全控制 loss。

---

### 3. HDR gradient weighting for tracking

只在 tracking 阶段利用 linear-HDR gradient：

```
strong radiometric edge
→ higher geometric importance
```

从而改善极端亮暗场景中的 camera pose estimation。

---

### 4. HDR-aware rasterization threshold

原 Gaussian rasterizer 的 alpha floor 基于 8-bit assumptions。

作者将阈值调到适配 16-bit HDR，使暗部微弱 Gaussian contribution 不会被过早丢弃。

---

## RawSLAM Dataset

论文同时发布新的 RAW/HDR SLAM dataset：

- 10 个真实室内序列
- >18,600 frames
- 16-bit DNG
- ISP-processed 8-bit LDR
- Depth
- IMU
- OptiTrack 6-DoF ground truth

这是本工作的另一个重要价值：它第一次提供较完整的 **RAW / HDR + geometry + pose** 联合 benchmark。

---

### Key evidence

同一 MonoGS backbone 下：

```
Direct HDR adaptation:
ATE = 49.43 cm

RawSLAM:
ATE = 24.15 cm
```

HDR rendering fidelity：

```
PSNR-μ:
20.96 → 22.96 dB
```

把 HDR modules 插入：

- MonoGS
- SplaTAM
- Gaussian SLAM

平均 tracking ATE 可下降约 **32–39%**。

在极端 illumination sequence 中，还能消除部分 tracking failure。

---

### Important counter-evidence

论文也说明：

> **HDR input 并不是对所有视觉 backbone 都自动有效。**

例如 DROID-W：

```
LDR ATE = 16.30 cm
HDR ATE = 16.46 cm
```

几乎没有收益。

这说明 learned representation 本身可能已经吸收部分 photometric invariance。

因此不能推出：

```
RAW/HDR always > RGB
```

更准确的结论是：

> **RAW/HDR 对依赖 photometric consistency 的 downstream task 更可能有价值。**

---

### Relation to recent work

此前已经有：

```
RawNeRF
HDR-NeRF
HDR-GS
HDRSplat
LE3D
```

证明 scene-linear / HDR 对 **offline radiance reconstruction** 有价值。

RawSLAM 的新变化是：

```
Offline HDR reconstruction
        ↓
Online perception directly in radiance domain
```

它也与以下方向一致：

- RAWild
- Task-aware Tone Mapping
- TaskGuard
- Restore What Matters

共同说明：

> **最终给人看的 rendering domain，不一定是机器任务最优的 representation domain。**

---

### Implication for ISP / Camera-Agent

这篇对 ISP 最大的启示是：

```
RAW / Linear HDR
      ├── Machine branch
      │     AF
      │     tracking
      │     scene understanding
      │     capture planning
      │
      └── Human branch
            AWB
            Tone Mapping
            style
            display rendering
```

即：

```
Human Rendering Stream
!=
Machine Perception Stream
```

这比传统：

```
preview sRGB
→ NPU semantics
→ ISP feedback
```

更加彻底。

对于 unified ISP / Camera Agent，可以进一步研究：

1. 哪些任务必须使用 RAW / linear feature；
2. 哪些任务 sRGB preview 已经足够；
3. 是否需要共享一个 lightweight radiance feature stream；
4. 如何避免维护双 pipeline 带来的内存与带宽成本。

---

### Evidence boundary

当前还不能直接作为手机方案：

- 仅室内数据
- 部分长序列降到 360×640
- 系统约 **1.22 FPS**
- 仍远离移动端实时部署

因此它目前更多是一条 **system architecture signal**，而不是直接可部署的 ISP module。

### Research takeaway

下一代 ISP 的问题可能不只是：

```
How to make better RGB?
```

而应该同时问：

```
What representation should each downstream task see?
```

---

# Cross-paper synthesis

两篇论文表面完全不同：

- MOSAIQ：IQA
- RawSLAM：RAW/HDR perception

但都指向同一个系统性问题：

> **Representation / scale alignment may be more important than adding a stronger model.**

MOSAIQ 解决：

```
Quality labels
→ common perceptual scale
```

RawSLAM 解决：

```
Sensor information
→ task-appropriate representation domain
```

因此对当前 ISP / IQA / Pseudo-GT 系统，更值得先检查三个 alignment：

```
1. Input-domain alignment
   RAW / linear / RGB 是否适合当前任务？

2. Supervision-scale alignment
   不同数据集和 judge 的 score 是否真的可比较？

3. Objective alignment
   Human perceptual quality 与 machine utility 是否需要分开？
```

## Overall research implication

很多当前瓶颈未必来自：

```
model capacity insufficient
```

而可能来自：

```
wrong input representation
+
misaligned supervision scale
+
wrong optimization target
```

这三点值得作为之后 ISP / IQA / Camera-Agent 方案设计中的前置检查项。
