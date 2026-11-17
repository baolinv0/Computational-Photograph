# 无 GT 图像增强的 IQA / Reward 可靠性：低光、颜色与水下的不同失效

版本 v0.2｜2026-11-17｜T04 主主题，连接 T02/T03/T05；11-17 扩展水下 NR-IQA 跨来源人评与压力测试，旧低光证据保持原核验范围

## 一分钟回忆

**三种错误应分开**：测试 GT 的渲染风格偏移、模型评价器不能计量物理色差、模型能识别局部降质却不能选择最佳影调。这不是一个可由更强 VLM 自动消除的问题。

## 路线地图

| 路线 | 核验对象 | 对照证据 | 独立风险 |
|---|---|---|---|
| FR-IQA 与配对 Benchmark | 预测对 GT 的距离 | [What Does LOL Measure?](../papers/arxiv-2610.38121.md) | GT 目标漂移/数据重叠/test-only tuning |
| CIE 真值颜色诊断 | AWB、肤色、CCT、ΔE 排序等可计算目标 | [CIE-computable color judge benchmark](../papers/arxiv-2610.40212.md) | VLM 粗分类会对，但细色差、数值估计未校准 |
| 夜景结构化质量问答 | 失真类别、严重度、位置及成因 | [NightIQA](../papers/arxiv-2611.04811.md) | MCQ accuracy 不等同 MOS / pairwise preference |
| **跨来源同场景主观排序及刷分审计** | 水下/真实增强版本 + 跨实验室 MOS/人类 pairwise → κ + 简单编辑/对抗/生成漂移压力测试 | [TrustUIQA](../papers/arxiv-2611.18429.md) | 73 配置包含同模型多 checkpoint；无单指标可保证所有来源的人类一致性，真实性与偏好也不同 |\n| 主观/多维 IQA | 自然、真实性、局部品质与任务效用 | 既有 [VHA](../papers/arxiv-2610.25770.md)、EditJudgeBias、Face Contrast | 单一分数难以涵盖互不补偿维度 |

## 三条新证据

**LOL 审计（2026-10-28）**：官方配对像素复核和 18 checkpoint 测试发现：同 15 个 LOL-v1 测试输入在 LOLv2 中存在不同的色彩目标，LOL-v1 测试 GT 饱和度中位高 1.48×；LOLv2-Real 测试 GT 较训练 GT 暗约 14%。test-only 与 train-only calibration 的效果不一样，某些评测脚本设置改变方法排名。同期 Pan 研究也报告数据重叠；不得将重叠发现全部归此篇独创。

**CIE-computable（2026-10-29）**：8 个 MLLM 测 5 项色彩计算真值；闭源模型 CCT MAE 715–1056K、开源 1358–2133K；ColorChecker 去模板后部分模型恶化。粗 AWB 识别不等于物理色度校准，且用合成色卡测试不能直接声称自然人像偏好可靠。

**NightIQA（2026-11-03）**：1769 张真实夜景，6 类受控降质，4 级 QA，80k 合成；Qwen3-VL-8B 的 MCQ 准确率从 63.82 提到 80.71（SFT+GRPO），对照是夜景问答而非主观 MOS 相关系数。标注为多模型初标+人工校验，仍可能包含共同偏差。

## 新旧判断

**旧判断**：IQA 模型精度、PSNR 或 VLM 解释可用于评价增强。**新判断**：先审计 GT、split 和 test-time 处理，再检验评价器对于目标条件的计量能力，并分离“能找出降质”与“能判断候选赢家”。**不变**：没有一种单指标普遍替代全部视觉与任务效用。

## 完整评价方案

数据来源/目标定义 → 数据泄漏与 GT 风格审计 → 固定无 oracle 评测 → 多维 FR/NR/Color/Localization/Preference 评价 → 针对执行器候选池测 pairwise winner accuracy、reversal 和稳定性 → 保留重要失败例。

校准与测试必须分离；有 GT 的 VHA/FR metrics 不能直接转为真实无 GT 部署评分器。

## 最小判别实验

对固定候选池和真实测试样本，分别比较公开 test-time 设置与训练集可确定设置的排名变化，并叠加数值 ΔE/ROI fidelity 与独立偏好；重点测“哪些模型改进其实是匹配 GT 风格而非更自然”。

## 2026-11-12：LR-faithfulness 不等于 NR-IQA

[LucidNFT v4](../papers/arxiv-2603.05947.md) 将 Real-ISR 的目标拆成 perceptual quality 与 LR-referenced faithfulness，并训练 LucidConsistency 作为 LR 证据评价器。v4 新增 40 个 RealSR LR inputs、5 位专家、200 次 binary comparisons 的 reward-independent human study；LucidNFT 在 72.5% 的 200 次 binary judgments 中被判定更忠实于 LR，LucidFlux baseline 27.5%；实验不允许 tie，Fleiss’ κ=0.415。

这是一条 **training reward / preference** 证据，不是通用 NR-IQA，也不是在线 Agent judge。其指标仍需谨慎：LucidConsistency 同时参与训练和部分评价，存在 self-reference；小规模人评只能补强，不能替代跨数据集独立验证。完整机制与系统分层见 [LR-anchored Real-ISR preference optimization](lr-anchored-real-isr-preference-optimization.md)。

## 2026-11-17｜TrustUIQA：跨来源主观偏好与评价器的可刷分性（New）

**主 T04；次 T03/T05；角色评价、Benchmark；GO-E；地图 Counter-evidence + Boundary refinement。** [Do Underwater Image Quality Metrics Agree with Human Perception?](../papers/arxiv-2611.18429.md)（Rishii Kumar Singh、Abhinav Rajput、Dinesh Kumar Vishwakarma，2026-11-13 arXiv v1 / 11-16 新公告）没有发明“NR-IQA 与人类不一致”的问题，但提供了可重复的系统性审计：73 个评价器配置、4 套先前 MOS 数据和额外 20 人/32 场景/1920 次人工二选一；同一图的不同增强版本上检验 pairwise Cohen κ，另用简单色彩/锐化/CLAHE、梯度扰动和多轮生成自拷贝寻找反例。

| 路线与历史锚点（非新推荐） | 测量对象/监督/控制 | 核心界限 |
|---|---|---|
| UIQM、UCIQE，传统 UW NR-IQA | 颜色、清晰度、对比度 hand-crafted proxy → 分数 | 极端饱和与强锐化可刷分；非感知保真真值 |
| URanker、Q-Align、泛化 NR-IQA | MOS/模型预训练 → 排序 | 同训练来源或某一数据集高相关不能保证新实验室、同图候选选优 |
| BAPPS/gMAD/先前 NR-IQA attacks（历史） | 双选偏好或指标不一致/抗攻击测试 | 比较和刷分思想已有先例，不把本次概括为第一次提出 |
| Banana100（历史） | 多轮生成复制 → 检查分数与退化单调性 | 旧共性，本次测更具体的水下域和两执行器 |
| **TrustUIQA 新增证据** | 五个人类参照源 → 场景内同图候选比较；对 73 指标做简单编辑/攻击/漂移/实现审计 | best worst-source κ 0.23；本实验人-人 median κ 0.41；跨实验室学得水下 metric κ ≤0.31；不可推成所有真实照片任务通用数值 |
| [EditJudge-Bench](artifact-grounded-reward-and-verification.md) | 已知操作参数 → 编辑正确性二元判断 | 事实正确性不是美学偏好；与水下人评互补 |

**实验事实与审查边界**：四个既有 MOS 数据按库相加为 12,360 张/1,160 场景，但 SAUD/SAUD2.0 同实验室、共享 33 张场景，不能算完全独立；自建偏好 32 个场景人数仅 20。最佳跨来源 worst-case κ 为 0.23（Q-Align），不是总体 κ=0.23；学得水下 metric 同源 κ 可达 0.60–0.92，迁移至独立实验室不超过 0.31；Nano Banana Pro exact-copy 链噪声增约 2.5×时，只有 22/73 指标各 checkpoint 单调变差。PGD 是对**5 个可微模型**成功，并非全部 73 项，也非所有闭源 Judge。作者原文已承认早期水下感知偏差与 general metric hacking 前序。

**判断更新（旧 → 新 → 不变）**：此前的低光/颜色审计强调 GT 风格、CIE 计量和 VLM 是否能定位缺陷；现在增加一条独立必要性：即使没有 GT，也要在同场景多候选上比较人工 winner 和评分器，验证指标在容易优化的色彩/锐化方向是否鼓励错误结果。不变的是**人类偏好、真实内容、局部结构/设备颜色和下游效用不互相替代**；本结果只在水下增强域提供定量反例。

**离线方案**：多设备/不同失真域数据 + 同源候选 + 匿名人评 → 防泄漏分层 → 配对一致率/κ+人-人分歧 → 简单参数刷分与多步重复编辑压力测试 → 得到指标适用条件。**在线评价（设计假设，非 TrustUIQA 原系统）**：LQ + K 候选 → 颜色/结构/自然度分开检查 + 已审计 Judge → 接受/拒绝/保留输入。**Agent 层**仅使用该评价结果，不因此提高 executor 产出能力。最小实验固定 K 与调用预算，比较 NR-IQA、VLM Judge 与简单可解释规则在真实人工 pairwise 中的可选择性，再用过饱和/锐化反例审计。

**记忆锚点**：IQA 能给两张照片排序，不等于排序和人一致；奖励能被优化，不等于改进了照片。

## References

- [LOL Benchmark audit](https://arxiv.org/abs/2610.38121v1)
- [CIE color judgment](https://arxiv.org/abs/2610.40212v1)
- [NightIQA](https://arxiv.org/abs/2611.04811v1)
- [TrustUIQA 论文](https://arxiv.org/abs/2611.18429) · [代码](https://github.com/TrustUIQA/TrustUIQA)\n- [VHA 卡片](../papers/arxiv-2610.25770.md)
