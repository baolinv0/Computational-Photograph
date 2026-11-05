# What Does LOL Measure? Hidden Label Shifts in Low-Light Enhancement Benchmarks

目录：[快速回忆](#快速回忆) · [机制与前序](#机制与前序) · [证据与争议](#证据与争议) · [系统与迁移](#系统与迁移) · [References](#references)

- **ID**: arxiv-2610.38121; **首次公开**: 2026-10-28（arXiv v1）；**当前审查版本**: v1（后续实质版本需另行比较）。
- **作者/团队**: Adityan Thirumani Srinivasan (University of Wisconsin–Madison)
- **核验**: 2026-11-05，原文相关方法、实验与局限章节（selected_sections_checked）；无独立复现。
- **主主题**: T04；**关联主题**: T05；**系统角色**: evaluation / benchmark counter-evidence。
- **地图变化**: Counter-evidence + Boundary refinement；**裁决**: GO — evaluation counter-evidence。
- **历史事件**: 2026-10-25—11-05 停用窗口补查，2026-11-05 回填；不是 11-05 新发表，首次覆盖以归档日期而非首次公开记录。

## 快速回忆

**核心瓶颈**：模型分数可以因为测试标签的目标风格和后处理而变，而不是模型恢复能力提升。

**一句话技术命题**：通过官方 LOL 数据标签逐像素审计、统一重放公开 checkpoints、比较仅训练集与测试集调参，区分 GT 标注分布漂移、跨 benchmark 重叠与 test-time tuning 的影响。

## 机制与前序

通过官方 LOL 数据标签逐像素审计、统一重放公开 checkpoints、比较仅训练集与测试集调参，区分 GT 标注分布漂移、跨 benchmark 重叠与 test-time tuning 的影响。

**近两年与必要前序 / prior-art attack**：LOL-v1/LOLv2 官方数据、Retinexformer/HVI-CIDNet/IAT 的测试脚本和同期 Pan 的训练测试重复审计。标签漂移与 adaptive test-set tuning 是独立机制；不能以本文单篇否定增强网络架构。

## 证据与争议

**作者报告（非独立复现）**：8 种方法、18 checkpoints，公布分数复现误差≤0.09 dB；同 15 张 LOL-v1 测试采集在 LOLv2 出现时，v1 GT 饱和度中位高 1.48×；LOLv2-Real 测试 GT 较训练 GT 暗约 14%；测试专属校准相对训练集校准残余在 LOLv2-Real 中位 0.92 dB；特定设置移除后领先方法变化。作者明确称与 Pan 同期工作对 LOL 重叠的发现部分重合。

**主要限制与反证**：作者检查过的 benchmark、checkpoint 与脚本范围内成立；不能凭观测到的设置推断作者有意使用测试标签；不同 PSNR 计算协议与目标美学本身也需报告。

**主张层级**：作者主张有条件局部实验支持；跨独立团队的方向与普遍共识不可仅据本篇推断。对于已存在成熟前序的机制，本篇主要按数据、评价、系统或限定方法增量裁决。

## 系统与迁移

**系统接口与方案回忆**：采集/生成 GT → 分割与标签一致性审计 → 冻结 checkpoint 和无 oracle 测试协议 → 原指标/替代指标同时报告。

**最小可执行判断**：所有 LOL 排名报告原始脚本、去除 test-specific adjustments、train-only calibration、checkpoint 选取规则；检查数据交叉重叠。

不将论文中报告的作者实验外推为用户项目实测或手机端已部署。

## References

- [arXiv v1](https://arxiv.org/abs/2610.38121v1)
- [alphaXiv](https://www.alphaxiv.org/abs/2610.38121)
- [长期文献地图](../LITERATURE_MAP.md)
