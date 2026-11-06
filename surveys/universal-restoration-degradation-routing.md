# 统一恢复的退化建模与专家扩容：更大模型何时更稳健？

版本 v0.1｜2026-11-06｜主主题 T03，连接 T05/X01

目录：[问题](#问题) · [竞争路线](#竞争路线) · [前序与本轮增量](#前序与本轮增量) · [证据与反例](#证据与反例) · [完整方案](#完整方案) · [覆盖缺口](#覆盖缺口)

## 问题

一个 restoration network 在噪声、模糊、雨雪、压缩和多项叠加下，能否以有限可执行预算恢复原场景，而不因退化识别错误选错专家？这与“用 Agent 选择多少个工具调用”不同：这里训练期就将不同恢复子能力嵌入同一个执行器。

记忆锚点：**识别越细、专家越专，错误路由的损害也越大；通用性取决于识别不确定性下能否退回粗粒度。**

## 竞争路线

| 路线 | 输入与条件控制 | 训练监督/执行表达 | 主利益 | 失败边界 |
|---|---|---|---|---|
| 单任务专家 | 专门数据/明确退化类别 | 每退化训练独立模型 | 高专项 PSNR，基线可控 | 部署多模型、未知退化 |
| 单 backbone 混合恢复 | RGB LQ，隐式识别 | PromptIR/InstructIR/Restormer 类统一模型 | 参数共享、简洁 | 任务冲突、极端复合退化 |
| 固定粒度专家路由 | 图像退化表示 → expert | MoCE-IR 类 MoE | 用专家减少冲突 | 细粒度 OOD 误识别、像素非均匀 |
| **层级 + 退化置信/区域路由** | 图像/局部 degradation map → 路由层级和 expert | ICLR2026 UniRestorer → [UniRestorer++](../papers/arxiv-2611.06042.md) 扩至多层 LoRA 和局部 top-1 | 可扩容且按不确定性回退 | 标签/路由 OOD、权重存储和训练成本 |
| 外部 Agent 工具池 | 状态/目标 → 工具、顺序、重试 | [HarnessIR](../papers/arxiv-2610.10133.md) 或专用工具系统 | 动作动态组合、可验证 | 搜索/评估成本与不可观察真值；**不等于网络 MoE** |

数据路线分别是单项合成、组合合成 CDD-11/50、真实配对和无真值的 OOD 使用；不得用同一 GT 假设对所有路线归因。

## 前序与本轮增量

[UniRestorer (ICLR 2026)](https://proceedings.iclr.cc/paper_files/paper/2026/hash/04fb0ea2010694af12735724a601a3b4-Abstract-Conference.html) 已有 hierarchical clustering、granularity estimation、multi-granularity mixture experts；这是**直接前作**而非“2026-11 首次提出层级路由”。

2026-11-04 arXiv 首发 [UniRestorer++](../papers/arxiv-2611.06042.md) 的可证增量：hierarchy LoRA 大规模扩容、dense degradation representation、local/region-aware routing、CDD-50 从单项到五重组合退化 benchmark。与 MoCE-IR、PromptIR 等是部分可比较的**竞争路线**；与外部恢复 Agent 是分层互补（综合推断），不是直接继承。

## 证据与反例

作者在七单项测试报告：UniRestorer 31.81→UniRestorer++ 32.24 dB，CDD-50 OOD 23.09→23.46 dB；这是论文内部特定权重和数据条件，不是独立复现。

对于 512×512 输入，同量级模型 UniRestorer++ 为 176M / 1255 GFLOPs / 0.515s (A6000)，UniRestorer 为 171M / 1156G / 0.484s：局部路由增加实际成本。其 2.9B 总参数 scaling 改善 OOD PSNR，但**总权重/内存/训练预算极大**，不能从 active-expert FLOPs 近似固定推出手机可部署。单任务 SIDD NAFNet 40.30 vs 新模型 2.9B zero-shot 38.72 dB 是明确反例。

挑战可信性：CDD-50 在作者构造的合成复合退化条件下有优势；能否泛化真实 ISP 域、RAW/视频/新硬件噪声/几何运动仍未定。更大模型与更多合成数据是重要替代解释；作者做了 dense/vanilla MoE 对照但并非完整等总成本匹配。

## 完整方案

**离线**：真实退化/标注可信 GT + 合成单/复合退化及独立 held-out compositions → 学习 degradation representations 和 hierarchy → train shared trunk+experts → train granularity uncertainty/local routing → 外场 OOD 验证、成本曲线和 specialist 比较。

**在线**：RGB LQ → degradation identification and confidence → spatial hierarchy expert routing → one selected expert per location / shared trunk → restored RGB → fidelity/perceptual evaluation；可有独立的任务级 Agent，但 UniRestorer++ 本身不需要 Agent。

**旧→新**：之前仅有在多任务下粗/细专家能互补的机制论证；新加入同一扩容族、CDD-50 和真实集的性能/成本曲线，说明专家容量扩展必须与退化不确定性适配。**不变**：单任务轻量模型依旧是强基线，当前端侧 photofinishing/TM 方案不能用此论文直接替换。裁决 GO-E（研究与 benchmark / non-mobile executor）。

## 覆盖缺口

待核验 PromptIR / MoCE-IR 原文训练预算、复合退化数据与新增 2.9B 的同活跃参数匹配；公开 checkpoint 是否和论文 v1 一致；手机 GPU/DDR 和 4K 运行成本；真实几何和色彩 GT 可信性。只核验 UniRestorer++ 选定原文章节与 UniRestorer 官方 ICLR 摘要。

- [UniRestorer++ 2026 原文](https://arxiv.org/html/2611.06042v1)
- [ICLR 2026 原始前作](https://proceedings.iclr.cc/paper_files/paper/2026/hash/04fb0ea2010694af12735724a601a3b4-Abstract-Conference.html)
- [UniRestorer++ canonical card](../papers/arxiv-2611.06042.md)
