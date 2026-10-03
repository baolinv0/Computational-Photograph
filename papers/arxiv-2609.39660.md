# BAM! Bayesian Anything Model

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)

- 完整标题：BAM! Bayesian Anything Model: a foundation model for generative computational imaging
- 作者：Alessio Spagnoletti、Charlesquin Kemajou Mbakam、Jonathan Spence、Andrés Almansa、Marcelo Pereyra
- ID：arxiv-2609.39660；主题：ISP / computational imaging / inverse problems
- 已核验公开版本：2026-09-30，v1；首次简报：2026-10-01；核验：2026-10-03。
- 核验范围：原论文摘要及选定正文（p.1–4、7、9），不是完整精读或独立复现。没有穷尽更早公开渠道。
- Decision key：operator-conditioned-posterior-sampling

## 快速回忆

**问题：**通用图像先验灵活但推断成本高，专用物理模型又容易绑定任务。

**旧→新：**[RAM](https://arxiv.org/abs/2503.08915) 的 operator-conditioned 点估计，扩展为少步条件 flow-map 后验采样。

**记住：**增量在“把成像算子带进模型接口”，不是已经解决真实手机 RAW 的全部非线性。

**下一步：**固定图像，比较正确算子、轻微失配算子、不同噪声假设下的重建与不确定性。

## 精读记录

输入为观测和前向算子等条件，输出是重建样本，而非单一回归图。论文 p.1–4 报告 36M 参数、少步采样，并以已知线性观测与高斯噪声作为主要问题设定。噪声的具体进入方式涉及观测重标定，不能把概念接口直接当成网络有一个独立的 sigma 输入分支。

作者在 [FFHQ、AFHQ、LSUN、DIV2K 与 Köhler 等设置](https://arxiv.org/abs/2609.39660) 报告结果。p.7 还讨论先估计模糊核再重建、以及非线性 JPEG 的探索；因此“完全不能处理 blind/nonlinear”同样是过强概括。

**横向定位：**RAM 是直接前序，PnP/外部 likelihood guidance 是竞争路线。尚未系统复核所有比较论文，不能写成此路线已成为行业共识。

## 证据边界

作者实验不等于独立复现；3 steps 不等于手机实时。真实 shot noise、clipping、标定失配与跨传感器表现需要单独验证。当前记录不继承旧简报中未逐项核验的全部数值。

**修订说明：**保留“主要是已知算子设定”，同时补充文中存在 blind deblurring pipeline 与非线性探索，避免二元化排除。

## References

- [原论文 / v1](https://arxiv.org/abs/2609.39660v1)
- [作者项目入口](https://bayesian-anything-model.github.io/)
- [RAM 原论文](https://arxiv.org/abs/2503.08915)
- [归档协议](../ARCHIVE_PROTOCOL.md)
