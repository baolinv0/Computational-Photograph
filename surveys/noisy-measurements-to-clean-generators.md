# 无干净 GT 的生成式恢复：从有噪声观测学习清晰分布

版本 v0.1｜2026-11-05｜T05/T03

## 问题

有真实噪声成像数据但无法采集干净 GT 时，能否学习的不只是某一噪声水平的去噪器，而是可生成干净图像的完整分布？

## 竞争路线

| 路线 | 核心证据 | 主要限制 |
|---|---|---|
| 配对 GT | 有干净参照 | 成本高、动态对齐困难 |
| Noise2Noise / 自监督去噪 | 同潜在样本两条件独立噪声观测 | 后验均值不等于生成干净样本分布 |
| Gaussian noisy diffusion + consistency | Daras 等历史工作 | 噪声 law 未必匹配真实 photon count/speckle |
| **按测量 law 构造生成过程 + consistency** | [Kruse/Baldassari/Dokmanić 2026](../papers/arxiv-2610.42036.md) | 必须满足独立观测、posterior targets、可识别性 |

## 新论文增量

[Learning Clean Generative Processes from Noisy Measurements](https://arxiv.org/abs/2610.42036v1)（2026-10-30）把独立 noisy views 的 N2N 回归推广到 Poisson、Binomial、Gamma、Negative-Binomial 的 measurement-specific generative processes，并研究 measured noise 级以下的 consistency 约束能否唯一确定干净极限。

论文 CIFAR-10 Poisson 的一组作者 FID：无 consistency 的直接外推 30.66±0.03，有 consistency 3.98±0.13；验证同时包含计数显微成像和 SAR。相关数学创新不是第一次提出无 GT 去噪或一致性，而是非高斯测量过程统一建模与成立条件。

## 系统方案

离线：真实或可生成的同源独立噪声观测 + 校准 measurement law → posterior-target regression at observable information levels → consistency below observed noise → generator → 独立 clean reference/物理统计/任务效用验收。

在线：噪声观测 → 噪声机制选择 → 条件 posterior sampling → 多候选/不确定性或点估计 → 结构保真与观测一致性验收。

## 判断变化与边界

以前倾向把 N2N 和生成式先验训练分成两个不相接的方案。本篇说明可在**条件独立/噪声 law 可识别**前提下联通；这不是手机 RAW 可无条件套用。复杂相关 read noise、坏点、裁剪、ISP 非线性及 color-dependent pattern 需分别检查。样本看着像干净图 ≠ 原观测像素事实准确。

## 待检验

在校准的 Poisson-Gaussian RAW 小规模真实独立观测上，比 N2N 点估计、监督 GT、简单 Gaussian noisy diffusion；比较噪声统计、真实动态范围、文本与肤色区域以及 GPU-hours。

## References

- [原论文](https://arxiv.org/abs/2610.42036v1)
- [历史 RAW/ISP data synthesis survey](imaging-training-data-synthesis.md)
