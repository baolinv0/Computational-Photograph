# Learning Clean Generative Processes from Noisy Measurements

目录：[快速回忆](#快速回忆) · [机制与前序](#机制与前序) · [证据与争议](#证据与争议) · [系统与迁移](#系统与迁移) · [References](#references)

- **ID**: arxiv-2610.42036; **首次公开**: 2026-10-30（arXiv v1）；**当前审查版本**: v1（后续实质版本需另行比较）。
- **作者/团队**: Fabian Kruse, Lorenzo Baldassari, Ivan Dokmanić (University of Basel)
- **核验**: 2026-11-05，原文相关方法、实验与局限章节（selected_sections_checked）；无独立复现。
- **主主题**: T05；**关联主题**: T03；**系统角色**: no-GT generative training theory。
- **地图变化**: New route + Boundary refinement；**裁决**: GO — theory / supervision。
- **历史事件**: 2026-10-25—11-05 停用窗口补查，2026-11-05 回填；不是 11-05 新发表，首次覆盖以归档日期而非首次公开记录。

## 快速回忆

**核心瓶颈**：N2N 能学会当前噪声水平的后验预测，不会自动教会生成过程走到真实干净分布。

**一句话技术命题**：从同一潜在干净样本的条件独立噪声观测学习 posterior predictions；Noise2Noise 仅能监督训练数据噪声水平以上的过程，使用跨采样轨迹 consistency 约束把预测扩展至干净极限；推广高斯、泊松、二项、Gamma、负二项测量。

## 机制与前序

从同一潜在干净样本的条件独立噪声观测学习 posterior predictions；Noise2Noise 仅能监督训练数据噪声水平以上的过程，使用跨采样轨迹 consistency 约束把预测扩展至干净极限；推广高斯、泊松、二项、Gamma、负二项测量。

**近两年与必要前序 / prior-art attack**：Noise2Noise、Daras 等在 Gaussian noisy diffusion + consistency 中的思路；新增是统一非高斯测量驱动过程及其可识别性条件，而非首次提出无干净 GT 或 consistency。

## 证据与争议

**作者报告（非独立复现）**：作者在 CIFAR-10、计数显微成像与 SAR 验证；Poisson CIFAR-10 的示例 FID：继续生成而不加 consistency 30.66±0.03，加 consistency 3.98±0.13（对应指定 count 613.1）。两 seed 结果不能视为所有真实手机场景统计保证。

**主要限制与反证**：必须满足可建模的噪声 law、条件独立性、unbiased posterior-target 与可识别性条件；复杂手机 RAW 的空间相关噪声/ISP clipping 与模型失配没有被证明。

**主张层级**：作者主张有条件局部实验支持；跨独立团队的方向与普遍共识不可仅据本篇推断。对于已存在成熟前序的机制，本篇主要按数据、评价、系统或限定方法增量裁决。

## 系统与迁移

**系统接口与方案回忆**：同源独立有噪观测 → 噪声律定义的信息层级 → Noise2Noise posterior regression → consistency below measured-noise level → clean-sample generator → 独立真实检验。

**最小可执行判断**：先检验真实 RAW 的 shot/read-noise 与独立配对条件；不能在未校准测量分布上直接训练或把生成样本认作真实 GT。

不将论文中报告的作者实验外推为用户项目实测或手机端已部署。

## References

- [arXiv v1](https://arxiv.org/abs/2610.42036v1)
- [alphaXiv](https://www.alphaxiv.org/abs/2610.42036)
- [长期文献地图](../LITERATURE_MAP.md)
