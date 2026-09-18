# Recent Imaging Papers — 2026-09-18

本页记录 2026-09-16 首次公开、且对计算摄影 / ISP / 生成式恢复具有较高研究价值的三篇论文。重点不是复述摘要，而是判断其真正技术增量、证据边界，以及对当前 ISP / HDR / IQA / Pseudo-GT / 数据闭环研究的迁移价值。

---

## 1. Visual Autoregressive Priors for RAW-to-sRGB Image Signal Processing

**Authors:** Tailai Chen, Xiaotong Luo, Yuan Gao, Xin Jin, Wenjun Zeng  
**Venue:** ECCV 2026 Workshop on Low-Level Vision Frontiers (LoViF)  
**First public:** 2026-09-16  
**Paper:** https://arxiv.org/abs/2609.18302  
**Verdict:** **GO**

### Core problem

RAW-to-sRGB ISP 不只需要恢复结构和细节，还需要稳定完成 exposure、white balance、tone、color rendering。生成式大模型虽然有很强的空间先验，但离散 token / generative latent 是否适合同时承载这些连续 photometric states，并不明确。

### Real technical increment

论文首次将 Visual Autoregressive Model (VAR) 用于 RAW-to-sRGB ISP。核心不是“换成 VAR”，而是通过一组诊断实验暴露出 Neural ISP 的瓶颈：

- 冻结 1.10B VAR backbone，只训练约 32.93M 参数（2.99%）。
- 使用 RAW-conditioned cross attention。
- 用 frequency-decomposed color loss 分离低频 tone/color 与高频 chromatic edge。
- VAR 可以较好恢复结构，但 **continuous color transfer 成为主要误差来源**。

最关键的实验是：对输出做不可部署的 per-image oracle affine color correction，PSNR-Y 可提高约 **3.8 dB**；而 learned color head 的收益很小。这说明当前生成 prior 的主要问题已不再是“不会生成结构”，而是：

> **如何显式表示并控制 exposure / WB / tone / camera style 等连续 rendering state。**

### Evidence

Zurich RAW-to-sRGB benchmark 上：

- PSNR-Y: **21.31 → 21.89 dB**
- LPIPS: **0.276 → 0.218**

但它并非 SOTA ISP：

- 只验证单一数据集和 256×256 crop。
- 1.1B backbone 不适合移动端。
- RAW→sRGB 中连续颜色状态仍未真正解决。

另一个重要反证是：随着 fidelity supervision 增强，PSNR / SSIM / LPIPS 改善，但 CLIPIQA / MUSIQ 反而下降。这再次说明：

> **NR-IQA higher ≠ ISP fidelity higher.**

### Relation to recent work

与 FourierISP、ISPDiffuser 等工作的共同方向是：

```
structure / detail prior
        +
explicit photometric / color state
```

区别在于这篇通过强生成 prior 的失败案例，进一步证明“颜色、曝光、tone 不能完全隐式塞进生成 latent”。

### Implication for our work

对 Cross-Camera TM / AWB / Neural ISP，更合适的结构可能是：

```
Strong spatial / structural prior
              +
Explicit continuous rendering state

z_render = [exposure, WB, CCM, tone, camera style]
```

让大模型负责 structure / texture，让低维 continuous state 负责 rendering。

**Research takeaway:** 下一阶段 Neural ISP 的关键问题可能不是更大的 image prior，而是 **如何建模和控制连续 camera rendering state**。

---

## 2. Constrained Color Carrier: Characterization-Preserving Conditional Color Rendering in Multi-Illuminant Camera Profiles

**Author:** Xilai Liang  
**First public:** 2026-09-16  
**Paper:** https://arxiv.org/abs/2609.18361  
**Verdict:** **PROBE**

### Core problem

在 DNG multi-illuminant profile 中：

- ColorMatrix / ForwardMatrix：负责 camera characterization
- HueSatMap：负责 nonlinear rendering

但这些模块共享 condition-dependent interpolation slots。

因此，如果为了增强 WB-dependent rendering capacity 而增加 illuminant state，会同时改变 camera characterization。

这会把两个本应独立的问题耦合：

```
What is this camera?
vs.
How should this image be rendered?
```

### Real technical increment

论文提出 Constrained Color Carrier (CCC)，将问题写成 constrained optimization：

```
min rendering error

s.t.
camera characterization error <= ε
```

即：

> **允许 rendering 随 WB / condition 改变，但保护 camera characterization 不被破坏。**

CCC 使用原 dual-illuminant matrix segment 构造受保护的 characterization，同时利用三个共享 slot 承载更多 HueSatMap rendering basis。

### Evidence

测试设置：

- Sony A7R V Adobe Standard profile
- Hasselblad X2D / Phocus rendering target
- 2400–10000 K
- ±3 EV
- 53,207 temperature/exposure states

结果：

- Dual representation worst target error: **0.08208**
- CCC: **0.03508**（约 -57.3%）
- characterization preservation error: **0.003857**
- 低于设定 tolerance 0.004
- Ordinary Triple preservation error: **0.014802**，明显破坏原 characterization

### Evidence boundary

证据比较工程化，但外推范围有限：

- 只验证一组 Sony → Hasselblad profile。
- tint 固定为 0。
- 0.004 tolerance 是作者定义的工程约束，不等于 perceptual JND。
- 尚未证明对通用 mobile ISP / learned ISP 同样成立。

### Relation to recent work

它与近期 neural ISP / cross-camera work 从另一侧支持同一个原则：

```
Stable device characterization
        ≠
Conditional / creative rendering
```

即 camera identity / sensor characterization 与 WB / style / tone rendering 应尽量分离。

### Implication for our work

对 Camera→Phone color alignment / Cross-Camera TM，可以采用：

```
Device characterization
        ↓
Canonical color state
        ↓
WB / scene / intent-conditioned rendering
```

而不是让一个网络同时学习：

1. 这台 sensor / camera 是什么；
2. 这一次应该如何渲染。

**Research takeaway:** Cross-camera color/TM 的可迁移性很可能取决于是否把 **device characterization 与 rendering intent 解耦**。

---

## 3. Copy What Is Seen, Generate What Is Not: Training-Free Anomaly-Aware Video Restoration

**Authors:** Zhida Qu, Shengchao Chen  
**First public:** 2026-09-16  
**Paper:** https://arxiv.org/abs/2609.18836  
**Verdict:** **PROBE↑**

### Core problem

生成式 video restoration 最大风险是：模型会在已有真实证据的位置也自由生成，从而产生 hallucination 和 temporal inconsistency。

论文提出一个很清晰的问题边界：

```
Observed somewhere in history?
    → restore / copy

Never observed?
    → generation may be necessary
```

### Real technical increment

作者把待恢复区域拆成：

- **U_obs**：至少在某个历史帧中被真实观测过
- **U_gen**：整段视频中从未被观测

并定义：

```
U_obs → evidence-based restoration
U_gen → generative completion
```

pipeline：

1. motion-gated anomaly detection
2. 利用历史帧构建 background prior
3. 能从历史恢复的像素直接 copy / restore
4. 只有从未观测区域交给 diffusion
5. frozen verifier 在多个 restoration candidate 中选择

真正重要的不是 surveillance 任务，而是它明确提出：

> **Generation should begin where evidence ends.**

### Evidence

三个 surveillance benchmark 上：

- motion gating 可带来 **5.2–15.3 dB** PSNR 增益
- 真实 anomaly case 中，AVR 显著降低 flicker 和 warp error
- failure case 与理论边界一致：当遮挡物一直静止、背景从未被看到时，方法退化为 unconstrained generation

这使论文的假设和 failure mode 是一致的。

### Limitations

- task 很特定：surveillance anomaly removal
- observed / unseen 是二值定义，真实 ISP 中 evidence reliability 更可能是连续变量
- diffusion 部分非常慢，约 **3.91 s/frame**
- 不可直接作为移动端 video restoration 方法

### Relation to recent work

它与 OracleZoom、Recurrent Dynamic Range Extension、reference-constrained restoration 等方向共同指向：

```
Generative Restoration
        ↓
Evidence-Constrained Generative Restoration
```

即生成自由度必须由真实 evidence coverage 决定。

### Implication for our work

对 Smart Glasses Video HDR / multi-frame restoration，可以把二值 mask 扩展成连续的：

```
Evidence Coverage / Recoverability Map
```

例如：

```
Reliable historical evidence
    → temporal fusion / denoise / detail recovery

Weak evidence
    → conservative restoration

No evidence / irreversible clipping
    → optional generative prior
```

同时在 Pseudo-GT 训练中，不同区域也应按 evidence coverage 设置不同监督权重。

**Research takeaway:** 多帧恢复下一步不只要估计“历史帧是否可靠”，还要显式估计 **最终每个输出区域到底有多少真实观测支持**。

---

# Cross-paper synthesis

三篇论文虽然分别来自 RAW ISP、color profile 和 video restoration，但共同指向一个更一般的设计原则：

> **先确定哪些变量属于可靠事实，再决定哪些变量允许模型自由优化或生成。**

对应到三个任务：

| Task | Stable / Evidence-backed | Flexible / Conditional |
|---|---|---|
| RAW ISP | structure / RAW evidence | exposure / WB / tone / style |
| Camera color | device characterization | WB / scene-dependent rendering |
| Video restoration | historically observed content | never-observed completion |

因此一个更一般的 imaging pipeline 可以写成：

```
Evidence State
      ↓
Recoverable Processing
      ↓
Conditional Rendering
      ↓
Generative Completion (only when needed)
      ↓
Independent Fidelity / Quality Audit
```

## Overall research implication

比起继续追求一个“全能增强模型”，更值得研究的是三个显式状态：

1. **Evidence state**：当前信息中什么是真的、什么可恢复；
2. **Rendering state**：哪些曝光 / WB / tone / style 是可控连续变量；
3. **Generative boundary**：只有在 evidence 不足的位置允许 prior 补全。

这三层可能成为 ISP、HDR、跨相机 TM、Pseudo-GT 和生成式恢复之间更统一的系统框架。
