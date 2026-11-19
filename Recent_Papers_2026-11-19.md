# Paper Watch v3.2｜2026-11-19：真实双摄引导、空间恢复控制与 VLM 质量读出

**本轮：3 篇 New（2026-11-17 arXiv v1，2026-11-18 cs.CV 官方新公告，首次本系统覆盖 2026-11-19）**。先恢复既有 ARCHIVE_PROTOCOL/PAPER_WATCH_V3/LITERATURE_MAP/LEGACY/registry、两仓 survey 与 11-18 快照，再进行六分类新公告及核心作者/开放机制检索。不是会议录用重推，也不是旧论文补录。原文选定节/表/附录由作者提供，本轮未独立复现。

目录：[本次条目](#本次条目) · [T01跨模态观测](#t01跨模态观测) · [T03区域恢复](#t03区域恢复) · [T04质量读出](#t04质量读出) · [源覆盖与后续](#源覆盖与后续)

## 本次条目

| 身份/最早可核验公开 | 作者与研究 | 主/次/系统角色 | 地图变化 / 裁决 |
|---|---|---|---|
| 2611.22699，2026-11-17 arXiv v1 | [TANGO / DUET](papers/arxiv-2611.22699.md)：Matteo Kolyszko、Marco Buzzelli、Simone Bianco、Raimondo Schettini | T01 / T03、T05；采集、配准、执行、数据、评价 | **New route + Engineering maturity + Boundary refinement / GO-E** |
| 2611.22222，2026-11-17 arXiv v1 | [ExplicitIR](papers/arxiv-2611.22222.md)：Dezhi Zhang、Shangrong Yang、Yudong Liang、Wenjian Wang | T03 / T06、T04；区域执行、控制表示、训练 | **Bridge + Boundary refinement / PROBE** |
| 2611.22564，2026-11-17 arXiv v1 | [Lost in Read-out](papers/arxiv-2611.22564.md)：Zhuangzi Li、Shilv Cai、Jian Jin、Zhiyi Pan、Haihong Xiao、Weisi Lin | T04 / T06、T02、X01；评价读出、校准训练 | **New route + Boundary refinement + Counter-evidence / GO-E** |

## T01跨模态观测

**旧图**：真实 NIR 引导 UGD-FM、双传感器额外观测、静态/动态错配引导，及同一设备 live/capture 教师 LC-ISP。传统模拟成对的 RGB-guided HSI 常忽视实际视差。**新**：[DUET](papers/arxiv-2611.22699.md) 提供两台独立相机摄取的 403 个 RGB/HSI 场景。RGB 包含额外真实空间测量；高分辨率 HSI 真实采集并以其下采样生成合成 LR HSI，故并非 LR/HR 完整实测配对。TANGO 以 global alignment + local alignment + occlusion gate 来利用 RGB。作者 DUET x8 PSNR 38.116 对最强对照 36.403 dB，不能将收益全部归因 gate 或宣称手机部署，真实 dataset/code link 尚未可访问确认。

**判断**：双传感器能补实际信息但必须付出标定/错配代价，成立条件比单传感器更明确；其他旧结论不变。**方案** 离线双机标定、HR-HSI/真实RGB、synthetic LR-HSI 监督；在线 LR-HSI+RGB→匹配与信心 gating→HR-HSI。行动：保留 GO-E 基准；现有手机单RAW方案不动。最小证伪：固定模型/数据分别去掉 global/local/gate，分层测 parallax/occlusion。**记忆句**：真实第二传感器不是生成参考，却也不是自动对齐的 GT。详见 [非配准跨模态 living survey](surveys/unaligned-guided-restoration.md)。

## T03区域恢复

**旧图**：Whole image KEEP/RESTORE、generative latent confidence blend（SGVD）、外部 Judge，还有 Restormer/PromptIR 等条件化模型。**新**：[ExplicitIR](papers/arxiv-2611.22222.md) 将恢复网络的 update Budget 和 narrow/wide context Style 设为可见 per-pixel fields，直接控制 decoder，和在外部 Agent 中选择操作不同。作者三任务平均 PSNR 32.78，Restormer 31.98，外部退化标签的 DFPIR 32.88，性能与机制归因不能过度宣称。

**判断**：新增**内部 feature 更新**控制位置，属于路线 Bridge；仍不能保证像素保真或解决不可恢复信息。**方案** 离线 clean/LQ+训练 Budget/Style；在线 input→fields→decoder→RGB；Agent 可选但未验证。行动 PROBE、项目策略不改；最小实验等 FLOPs 对比普通空间注意力/单强度场/双策略场，测恢复与非目标泄漏。**记忆句**：决定哪里更新，不等于决定候选是否可信。详见 [选择性恢复 living survey](surveys/selective-task-aware-restoration.md)。

## T04质量读出

**旧图**：Q-Align 监督微调视觉质量、CLIP/NR-IQA 独立指标、EditJudge-Bench 指令真实性、TrustUIQA 的偏好/metric hacking。**新**：[Lost in Read-out](papers/arxiv-2611.22564.md) 以 layerwise quality probe 证明部分冻结 VLM 的 hidden states 有人类 MOS 质量信息但最终 good-vs-poor 回答利用不足，可用单神经元 closed-form readout edit 在部分测试改善读出。作者 Qwen3.5-0.8B KonIQ Spearman 0.642→0.800；其他模型/格式和下游迁移不普遍，有文字语义副作用。机制前序中线性探针和校准不是新概念，贡献是直接定位/干预 VLM 特定 readout 的诊断证据。

**判断**：以前诊断“模型看不清”的情况，新证据表明也可能是“看到了但表达/读出有偏”。但**单图 MOS ≠ 同场景修图人类 winner ≠ 内容真实**，更不能自动解决执行器可达性。**方案** 离线 MOS 标注→冻结 VLM 表征探针→readout 拟合→cross domain/prompt 副作用审计；在线输入图→quality readout→独立内容/指令检查，Agent 非必需。行动不立即更换 Judge，仅设计固定候选/同标注预算的直接答案 vs linear probe vs readout。**记忆句**：看见质量信号，不代表最终回答能正确读出。详见 [评价与证据 living survey](surveys/artifact-grounded-reward-and-verification.md)。

## 源覆盖与后续

- 本轮实际读取官方 arXiv 2026-11-18 的 cs.CV、cs.LG、cs.AI、cs.MM、eess.IV、eess.SP 分类 `/new`，上次已覆盖 11-17，使用重叠 7 日身份/结论去重。对用户已关注的 10 位作者作 alphaXiv 11-10 以来检索，包括 Radu Timofte 11-16 论文《Layerwise Learning-Rate Scaling》但不属于高相关性主线。
- OpenReview 全量、各作者个人站/更早材料没有宣称完成覆盖；这些可能早于 arXiv 的证据尚有核验缺口。代码/数据链接 TANGO 截至本轮不可访问，不能称其已经实际放出。
- **非通知候选**：Fast Training-Free Low-Light Video Enhancement（2611.22551）端到端收益在作者设置下受较强 framewise 对照限制，先 WATCH；2026 NeurIPS 标注的 Harnessing Image Diffusion Prior for Photo-Realistic Video Restoration（2611.22874）会议/先前原文公开时间有待核实，pending chronology；AUTOREF 相关旧论文不能当本轮 new。
- 本轮**三份 canonical paper**、**三份已有 canonical living survey**、LITERATURE_MAP、surveys/README、仓库 README 和本快照做路径级更新与读取核验；registry 事件/alphaXiv 收藏见具体实际写入记录。更新仅添加证据路线，未替代既有 specialized review；私人项目数据未公开。
