# CHROMA-MILL: Joint Low-Light Enhancement and White Balance under Colored Illumination

目录：[快速回忆](#快速回忆) · [机制与前序](#机制与前序) · [证据与争议](#证据与争议) · [系统与迁移](#系统与迁移) · [References](#references)

- **ID**: arxiv-2611.04092; **首次公开**: 2026-11-03（arXiv v1）；**当前审查版本**: v1（后续实质版本需另行比较）。
- **作者/团队**: Pol Riubrogent-Comas, David Serrano-Lozano, Maria Pilligua, Michael S. Brown, Ramon Baldrich, Javier Vazquez-Corral (CVC/UAB/York University)
- **核验**: 2026-11-05，原文相关方法、实验与局限章节（selected_sections_checked）；无独立复现。
- **主主题**: T01；**关联主题**: T02/T05；**系统角色**: RAW dataset + joint AWB/LLIE benchmark。
- **地图变化**: New route + Bridge；**裁决**: GO — data / evaluation。
- **历史事件**: 2026-10-25—11-05 停用窗口补查，2026-11-05 回填；不是 11-05 新发表，首次覆盖以归档日期而非首次公开记录。

## 快速回忆

**核心瓶颈**：在暗光环境，亮度恢复和光源估计共用同一受噪声污染的观测，任务串联顺序不能假定无害。

**一句话技术命题**：固定场景、标定四个光源与 11 档强度，在 DSLR 和手机 RAW 域获取可配对观测；线性混合不同照明测量构建已知 chromaticity 的照明条件，并给出 LLIE-only/AWB-only 与最终联合目标，检验级联与联合网络。

## 机制与前序

固定场景、标定四个光源与 11 档强度，在 DSLR 和手机 RAW 域获取可配对观测；线性混合不同照明测量构建已知 chromaticity 的照明条件，并给出 LLIE-only/AWB-only 与最终联合目标，检验级联与联合网络。

**近两年与必要前序 / prior-art attack**：传统 Retinex/LLIE、DWB/FC4/FFCC/RL-AWB、MILL 原始采集协议；明确区别低光增强后的颜色评分与真实照明 chromaticity GT。

## 证据与争议

**作者报告（非独立复现）**：50 场景，4 标定光源，11 强度档；作者 CTI-Retinexformer 对最佳级联方案报告约 +0.7 dB PSNR_L 与 -1.1 ΔE00。手机表中 CTI-Retinexformer PSNR_L 24.352，最佳列出的 Retinexformer+DWB 24.421，说明跨机型未在每项指标全部领先；手机 ΔE00 8.881 vs 9.327。

**主要限制与反证**：线性 RAW 混光要求对齐、响应线性、光源固定且有效光谱组合在已采集 convex hull；不等于所有真实非均匀多光源场景的每像素 ground truth。DSLR/手机主要验证范围有限，不是手机硬件 AE 优化。

**主张层级**：作者主张有条件局部实验支持；跨独立团队的方向与普遍共识不可仅据本篇推断。对于已存在成熟前序的机制，本篇主要按数据、评价、系统或限定方法增量裁决。

## 系统与迁移

**系统接口与方案回忆**：标定单光源 RAW × 多亮度采集 → RAW 混合与来源记录 → 任务拆分中间 GT → 增强和 AWB 分开/级联/联合训练 → 亮度与色度独立测试。

**最小可执行判断**：复用数据协议，固定训练和采集输入，直接比较 LLIE→AWB、AWB→LLIE、联合模型在暗光/彩光条件下的增益及误差传播。

不将论文中报告的作者实验外推为用户项目实测或手机端已部署。

## References

- [arXiv v1](https://arxiv.org/abs/2611.04092v1)
- [alphaXiv](https://www.alphaxiv.org/abs/2611.04092)
- [长期文献地图](../LITERATURE_MAP.md)
