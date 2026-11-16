# 真实场景文字恢复：从像素证据到上下文推断的真实性边界

版本 v0.1｜2026-11-16｜主 T03，连接 T04 / T06 / X01
目录：[问题与记忆](#问题与记忆) · [竞争路线](#竞争路线) · [证据和判断](#证据和判断) · [完整方案](#完整方案) · [后续覆盖](#后续覆盖) · [References](#references)

> 本页是长期的**文本事实保真问题**，不按单篇论文或本次日期组织。基于 2026-11-16 对 ReasonText arXiv v1 选定章节的核验；前序名称源于该论文 Related Work，独立全文尚待逐篇查验。

## 问题与记忆

问题：在低清晰度自然照片中，字符的纹理是否有可恢复的物理证据？当局部不可辨而场景/语言上下文可推断，系统该追求可读的猜测、忠于观察的保真，还是显示“不确定”？

非目标：不把生成的字样当作原始字符的法律/史料证据；不把 OCR 打分当图像全部质量。

记忆锚点：**知道应该写什么 ≠ 模型真的画得出来；画得像真的 ≠ 原场景确有这些字。**

## 竞争路线

| 路线与历史锚点 | 输入/输出 | 控制/监督 | 成立条件 | 主要失败方式 |
|---|---|---|---|---|
| 纯视觉/传统 SR（SwinIR 2021、DiT4SR 2025） | LR → HR | pixel/perceptual/生成先验 | 原始笔画仍可辨或局部纹理足够 | 字母笔画造假，漂亮却读错 |
| 显式 text-aware SR（Scene Text Telescope 2021、TeReDiff、UniT） | LR + text ROI/预测文字 → HR | OCR/检测/文本感知特征 | OCR/先验文字可信；精确空间定位 | OCR 错/区域错传播，字符 renderer 不听条件 |
| 上下文推断 → caption → 文本条件 SR（ReasonText/RTC 2026，**历史 backfill**） | LR+全局上下文 → 推断词串 → HR | 外部 MLLM + caption，不调 SR 权重 | 场景上下文带有真实线索且 SR 接口可执行文字 | 数据泄漏、合理但错误推断、额外模型成本 |
| 证据分级/拒绝生成（研究设计，**非论文验证**） | LR + ROI + provenance → copy/repair/abstain | OCR、相邻区域证据、可信度与保护边界 | 用户允许拒绝/含真值或可靠审计 | 保守过度、可达性下降、Judge 同源偏置 |

这些是**比较路线**，不能凭发表年份画直接继承；ReasonText 的作者引用了一些前序，但它与现有 Agent Judge 约束的连接是本次综合推断。

## 证据和判断

- **2026-11-16 历史 chronology 修复**：ReasonText arXiv:2611.15449 v1 首传 2026-11-11，进入 11-13 已覆盖 arXiv 公告；本任务曾于 11-14 标候选。其作者 HF 输出数据集在 2026-10-28 的第三方快照中已公开（快照声称 2026-08-04 创建），因此不能把 11-16 的补读算新增研究。最早完整论文公开日期仍未穷尽核验。
- 作者构建 513 LR-HR pairs / 2,463 个主测文本实例；Level 2 在 12 种 SR 基线普遍失效。GT text crop OCR 使 detection error 不进入 GTTCA，但仅为带 GT benchmark。
- Gemma 4 reasoning caption 给 DiT4SR 的 Level 2 GTTCA 24.54% → 45.84%；GT text oracle 也仅达 47.70%，HR OCR oracle 90.69%，说明除了推断正确，还存在**条件渲染执行器能力上限**。
- **旧判断：** SR 应兼顾真实保真，IQA 应看结构、文字。**更新为：** 字符应拆成（a）证据是否存在；（b）文本推断是否准确；（c）SR 是否画对；（d）系统是否有资格声称事实性。前两个不同于编辑后选图，不能仅更换 Judge。
- 不变：无源证据的“可读”文本不自动等于原文字；没有部署设备证据不得推荐作为实时手机相机链路。
- 当前共识级别仅为**特定数据与作者实验的局部证据**，需跨独立任务、不同脚本和真实对齐数据验证。

## 完整方案

**离线数据/评测链：** 高质量原图及真实字符转录 → 合成/实采退化与对齐 → 局部像素可读性/上下文可读性/不可判定分层 → 文本检测/字符准确/结构泄漏/偏好和成本各自计分 → 对错误重建保留反例。

**在线图像执行链：** LR 输入 → text ROI / OCR 和邻域证据 → 根据规则区分“原图确证”“上下文假设”“未知” → copy/传统 SR/文本条件生成候选 → 非目标保持和字符核验 → 返回结果及无法保证时的保守原样。

**Agent 控制层（仅设计）：** 只路由是否进行推断及调用何模型；要分别记录 candidate oracle 上限、搜索覆盖、Judge winner 命中率。不可将 hallucination 分数改进当作 Executor 可达性提升。

**成本合同：** 预处理/OCR/VLM 推断/SR/合成/复核的完整端到端时间、模型显存和设备，不能由单一 SR NFE 推算；SR 输出可读与文字真实性同时验收。

**最小判别实验：** 有 GT 招牌/印刷体文本 50–100 张，分 locally readable、context-only、truly ambiguous，固定 SR，对比 default/OCR/reasoning/GT-caption oracle，统计 L1/L2 accuracy、错误新字率、non-target leakage 与总推理时延。

## 后续覆盖

- 核验 ReasonText 作者项目/HF 最初公开日期和 NeurIPS OpenReview 原文可见日期；**目前只有第三方历史 artifact 证据**。
- 独立重读 Scene Text Telescope、TextSR、TeReDiff、UniT 原文和明确物体/文本的生成式保真审计工作；不要把论文作者的 Related Work 直接升级为正式历史综述的已核验方法。
- 需要更多非英文/字符随机串、串号、OCR-grounded 与无 GT 用户摄影场景；高风险的印刷文字应允许 abstain，而不把推断当真值。

## References

- [ReasonText/RTC，arXiv:2611.15449v1](https://arxiv.org/html/2611.15449v1) · [canonical card](../papers/arxiv-2611.15449.md)
- [作者代码](https://github.com/jasonleex1995/TAISR_needs_Reasoning) · [数据集](https://huggingface.co/datasets/Jasonleex1995/ReasonTextDataset)
- [作者模型输出历史证据](https://huggingface.co/datasets/Jasonleex1995/ReasonText-SR-outputs) · [第三方早期存档](https://silytics.si/datasets/Jasonleex1995/ReasonText-SR-outputs)
- [既有多轮编辑保真](multi-turn-editing-preservation.md) · [评价证据审计](artifact-grounded-reward-and-verification.md) · [可信恢复](efficient-generative-restoration.md)
