# HIVE-Diff: High Frame Rate HDR Video Reconstruction from a Single LDR Frame and Events

目录：[快速回忆](#快速回忆) · [机制与前序](#机制与前序) · [证据与争议](#证据与争议) · [系统与迁移](#系统与迁移) · [References](#references)

- **ID**: arxiv-2611.03465; **首次公开**: 2026-11-02（arXiv v1）；**当前审查版本**: v1（后续实质版本需另行比较）。
- **作者/团队**: Caixin Wang, Qingrui Wang, Jie Zhang, Ralph Etienne-Cummings (Johns Hopkins / Northwestern / MIT)
- **核验**: 2026-11-05，原文相关方法、实验与局限章节（selected_sections_checked）；无独立复现。
- **主主题**: T01；**关联主题**: T03/X01；**系统角色**: event-assisted HDR temporal expansion。
- **地图变化**: New route + Boundary refinement；**裁决**: PROBE↑ — new capture/output formulation。
- **历史事件**: 2026-10-25—11-05 停用窗口补查，2026-11-05 回填；不是 11-05 新发表，首次覆盖以归档日期而非首次公开记录。

## 快速回忆

**核心瓶颈**：events 提供变化而不是绝对颜色；单帧锚点也不能恢复完全不可见的静态高光纹理。

**一句话技术命题**：单张 LDR 参考为视频提供绝对亮度/颜色锚点，事件流提供高时间分辨变化；视频扩散补偿时域运动和 HDR 细节，从 1 张 LDR 与 events 扩展出 N 帧 HDR。

## 机制与前序

单张 LDR 参考为视频提供绝对亮度/颜色锚点，事件流提供高时间分辨变化；视频扩散补偿时域运动和 HDR 细节，从 1 张 LDR 与 events 扩展出 N 帧 HDR。

**近两年与必要前序 / prior-art attack**：Event-only HDR 不拥有绝对亮度锚点；NeurImg-HDR、HDRev 等传统 hybrid event-frame 需要 N 参考；本文改变的是 1:LDR→N:HDR 输入输出协议，不能只比较 PSNR 不计参考数。

## 证据与争议

**作者报告（非独立复现）**：Held-out EventHDR 五序列：作者在 single-reference 5× setting 报告 LPIPS 0.197、SSIM 0.825；20×性能进一步下降。512²、L40S、25 Euler steps/帧约 1.79s/帧，对 Feedforward 0.037s/帧级方法慢很多。

**主要限制与反证**：静态饱和区无事件时生成内容只能依赖先验，非真实观测；强依赖事件相机同步、仿真/少量真实 HDR GT；仍非可部署实时手机 HDR。

**主张层级**：作者主张有条件局部实验支持；跨独立团队的方向与普遍共识不可仅据本篇推断。对于已存在成熟前序的机制，本篇主要按数据、评价、系统或限定方法增量裁决。

## 系统与迁移

**系统接口与方案回忆**：事件流 + 单帧 LDR → 时间条件化视频生成/亮度色彩锚定 → HDR N 帧 → 真实性、Ewarp、时间成本评价。

**最小可执行判断**：在数据集层将 LDR 参考帧数与事件可观测性显式列为 benchmark 约束；不要简单映射现有手机视频多帧 HDR。

不将论文中报告的作者实验外推为用户项目实测或手机端已部署。

## References

- [arXiv v1](https://arxiv.org/abs/2611.03465v1)
- [alphaXiv](https://www.alphaxiv.org/abs/2611.03465)
- [长期文献地图](../LITERATURE_MAP.md)
