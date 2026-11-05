# Beyond CCT: Multi-channel SPD recovery for per-shot camera color correction

目录：[快速回忆](#快速回忆) · [机制与前序](#机制与前序) · [证据与争议](#证据与争议) · [系统与迁移](#系统与迁移) · [References](#references)

- **ID**: arxiv-2610.40175; **首次公开**: 2026-10-29（arXiv v1）；**当前审查版本**: v1（后续实质版本需另行比较）。
- **作者/团队**: Shuwei Yue, Hongke Wei, Qiao Chen (Shenzhen Polytechnic University / Insta360)
- **核验**: 2026-11-05，原文相关方法、实验与局限章节（selected_sections_checked）；无独立复现。
- **主主题**: T02；**关联主题**: T01；**系统角色**: per-shot color correction and spectral measurement。
- **地图变化**: New sensing-conditioned branch；**裁决**: GO-E — physically grounded ISP color。
- **历史事件**: 2026-10-25—11-05 停用窗口补查，2026-11-05 回填；不是 11-05 新发表，首次覆盖以归档日期而非首次公开记录。

## 快速回忆

**核心瓶颈**：相同白点或 CCT 可以隐藏不同 SPD，因此同一个 CCM 不一定给出相同颜色误差。

**一句话技术命题**：用相机 white point 与多通道 ALS 读数，通过非负最小二乘从 SPD 字典恢复照明光谱；合成虚拟 color chart 后逐张拟合 3×3 CCM，避免仅用 CCT/xy 近似同色异谱光源。

## 机制与前序

用相机 white point 与多通道 ALS 读数，通过非负最小二乘从 SPD 字典恢复照明光谱；合成虚拟 color chart 后逐张拟合 3×3 CCM，避免仅用 CCT/xy 近似同色异谱光源。

**近两年与必要前序 / prior-art attack**：Adobe DNG 2-CCT CCM、Karaimer/Brown 3-CCT、xy-conditioned CCM 与谱恢复；主要超越是增加 8–14 维 ALS 观测而非 NNLS 优化本身。

## 证据与争议

**作者报告（非独立复现）**：作者在 300 光源×3100 反射率的仿真上，平均 angular error 从最强非光谱 1.89° 降为 1.20°；LED-like 组 n=45 的 worst-25% 从 4.79° 降到 2.80°；实测 1684 SPD 做补充验证。

**主要限制与反证**：使用特定 Nikon D40 SSF 和理想/近似 ALS 滤波，所需标定/观测硬件并非所有手机可读；对未见的荧光灯 SPD 类别原字典失效，补光谱字典才能恢复优势。

**主张层级**：作者主张有条件局部实验支持；跨独立团队的方向与普遍共识不可仅据本篇推断。对于已存在成熟前序的机制，本篇主要按数据、评价、系统或限定方法增量裁决。

## 系统与迁移

**系统接口与方案回忆**：相机 SSF+ALS 滤波标定 → per-shot ALS/WP 读数 → SPD NNLS → virtual ColorChecker → 3×3 CCM → ΔE/角误差和端侧成本评价。

**最小可执行判断**：若具备可访问多通道 ALS，可测 off-Planckian 真实光谱；与 CCT/xy 级联保留强对照，不将白点正确等同最佳 CCM。

不将论文中报告的作者实验外推为用户项目实测或手机端已部署。

## References

- [arXiv v1](https://arxiv.org/abs/2610.40175v1)
- [alphaXiv](https://www.alphaxiv.org/abs/2610.40175)
- [长期文献地图](../LITERATURE_MAP.md)
