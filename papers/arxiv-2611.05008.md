# Learned Smartphone ISP on Mobile GPUs: Mobile AI 2026 Challenge Report

目录：[快速回忆](#快速回忆) · [机制与前序](#机制与前序) · [证据与争议](#证据与争议) · [系统与迁移](#系统与迁移) · [References](#references)

- **ID**: arxiv-2611.05008; **首次公开**: 2026-11-03（arXiv v1）；**当前审查版本**: v1（后续实质版本需另行比较）。
- **作者/团队**: Andrey Ignatov, Georgy Perevozchikov, Radu Timofte et al. (ETH Zürich / University of Würzburg / challenge teams)
- **核验**: 2026-11-05，原文相关方法、实验与局限章节（selected_sections_checked）；无独立复现。
- **主主题**: X01；**关联主题**: T01/T02；**系统角色**: mobile deployment / challenge benchmark。
- **地图变化**: Engineering maturity + Bridge；**裁决**: GO-E — deployment benchmark。
- **历史事件**: 2026-10-25—11-05 停用窗口补查，2026-11-05 回填；不是 11-05 新发表，首次覆盖以归档日期而非首次公开记录。

## 快速回忆

**核心瓶颈**：GFLOPs 与参数量都不是端侧真实时延；应按同一设备、分辨率和输出质量比较。

**一句话技术命题**：统一 RAW Bayer→RGB 的学习型 ISP 任务，在两个真实旗舰 SoC GPU 上实测提交网络，评价恢复质量与设备推理时间而非单纯 FLOPs。

## 机制与前序

统一 RAW Bayer→RGB 的学习型 ISP 任务，在两个真实旗舰 SoC GPU 上实测提交网络，评价恢复质量与设备推理时间而非单纯 FLOPs。

**近两年与必要前序 / prior-art attack**：Mobile AI Challenge 历年 Learned ISP on Mobile NPUs/GPUs、传统 ISP 与端侧轻量 CNN；新意主要在新硬件/数据/真实推理和公开参赛方案，不是一个统一新网络。

## 证据与争议

**作者报告（非独立复现）**：数据来自 Sony IMX586 Quad Bayer 与 Fujifilm GFX100 相机对应的 UltraISP paired set；论文表1采用 1920×2560 图像，在 Snapdragon 8 Elite Gen 5/Dimensity 9500 的 Adreno/Mali GPU 实测，参与模型质量/时延差异显著。

**主要限制与反证**：目标是 Fuji 中画幅渲染风格，未必代表手机厂商默认审美；受固定设备/运行时实现影响；不能把其 GPU 表格视为完整 Camera Pipeline 端到端延迟、功耗或热稳定。

**主张层级**：作者主张有条件局部实验支持；跨独立团队的方向与普遍共识不可仅据本篇推断。对于已存在成熟前序的机制，本篇主要按数据、评价、系统或限定方法增量裁决。

## 系统与迁移

**系统接口与方案回忆**：IMX586 RAW→专业相机 RGB reference → LiteRT 移动 GPU 执行 → PSNR/SSIM/主观评价/真实设备耗时 → Pareto 选择。

**最小可执行判断**：针对端侧 TM/ISP 增加设备实测与算子可用性对照，特别比较低分辨率控制器与轻量显式渲染。

不将论文中报告的作者实验外推为用户项目实测或手机端已部署。

## References

- [arXiv v1](https://arxiv.org/abs/2611.05008v1)
- [alphaXiv](https://www.alphaxiv.org/abs/2611.05008)
- [长期文献地图](../LITERATURE_MAP.md)
