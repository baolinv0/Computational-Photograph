# Benchmarking color judgment in multimodal LLMs with CIE-computable ground truth

目录：[快速回忆](#快速回忆) · [机制与前序](#机制与前序) · [证据与争议](#证据与争议) · [系统与迁移](#系统与迁移) · [References](#references)

- **ID**: arxiv-2610.40212; **首次公开**: 2026-10-29（arXiv v1）；**当前审查版本**: v1（后续实质版本需另行比较）。
- **作者/团队**: Shuwei Yue, Kaida Xiao, Zhihua Wang, Qiao Chen (Shenzhen Polytechnic University / University of Leeds / Sun Yat-sen University)
- **核验**: 2026-11-05，原文相关方法、实验与局限章节（selected_sections_checked）；无独立复现。
- **主主题**: T04；**关联主题**: T02；**系统角色**: physical color judgment evaluation。
- **地图变化**: Counter-evidence + New benchmark；**裁决**: GO — color evaluator validity。
- **历史事件**: 2026-10-25—11-05 停用窗口补查，2026-11-05 回填；不是 11-05 新发表，首次覆盖以归档日期而非首次公开记录。

## 快速回忆

**核心瓶颈**：VLM 会说颜色词，不等于可以可靠估计色温和细微色差。

**一句话技术命题**：将 MLLM 的 AWB 成对判断、肤色偏向方向、CCT 估计、ΔE2000 排序与照明变化下颜色命名拆成五项可用 CIE 计算真值的测试，检查粗语义判断与精细计量误差。

## 机制与前序

将 MLLM 的 AWB 成对判断、肤色偏向方向、CCT 估计、ΔE2000 排序与照明变化下颜色命名拆成五项可用 CIE 计算真值的测试，检查粗语义判断与精细计量误差。

**近两年与必要前序 / prior-art attack**：传统相机色度/白平衡物理校准、色彩一致性基准、MLLM IQA/编辑 Judge 偏差审计；新意在用颜色科学物理真值而非主观偏好打分。

## 证据与争议

**作者报告（非独立复现）**：8 个视觉语言模型，ColorChecker-24 刺激；闭源模型 CCT MAE 约 715–1056 K，测试开源模型约 1358–2133 K；在非 ColorChecker 模板上部分优势大幅下降，说明模板/预训练先验影响判断。

**主要限制与反证**：合成色卡，不是复杂自然场景；每任务单一 prompt，未覆盖 prompt 不确定性；CCT 回归部分测量数值输出能力；不能由此否认 MLLM 的粗类别语义辨认。

**主张层级**：作者主张有条件局部实验支持；跨独立团队的方向与普遍共识不可仅据本篇推断。对于已存在成熟前序的机制，本篇主要按数据、评价、系统或限定方法增量裁决。

## 系统与迁移

**系统接口与方案回忆**：可控色彩刺激 → CIE/测量真值 → MLLM judge → 细分类误差 + prompt/模板稳定性 → 用传统颜色算子与人评独立交叉验证。

**最小可执行判断**：对 Retouch/TM 的 Qwen/Gemini 评价器加 ΔE、肤色方向、背景去黄等独立数值标定；不以 VLM 文本理由取代颜色 GT。

不将论文中报告的作者实验外推为用户项目实测或手机端已部署。

## References

- [arXiv v1](https://arxiv.org/abs/2610.40212v1)
- [alphaXiv](https://www.alphaxiv.org/abs/2610.40212)
- [长期文献地图](../LITERATURE_MAP.md)
