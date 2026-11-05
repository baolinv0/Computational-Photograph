# 低光与颜色 IQA：分数、目标、Judge 与 Benchmark 到底在测量什么？

版本 v0.1｜2026-11-05｜T04 主主题，连接 T02/T05

## 一分钟回忆

**三种错误应分开**：测试 GT 的渲染风格偏移、模型评价器不能计量物理色差、模型能识别局部降质却不能选择最佳影调。这不是一个可由更强 VLM 自动消除的问题。

## 路线地图

| 路线 | 核验对象 | 对照证据 | 独立风险 |
|---|---|---|---|
| FR-IQA 与配对 Benchmark | 预测对 GT 的距离 | [What Does LOL Measure?](../papers/arxiv-2610.38121.md) | GT 目标漂移/数据重叠/test-only tuning |
| CIE 真值颜色诊断 | AWB、肤色、CCT、ΔE 排序等可计算目标 | [CIE-computable color judge benchmark](../papers/arxiv-2610.40212.md) | VLM 粗分类会对，但细色差、数值估计未校准 |
| 夜景结构化质量问答 | 失真类别、严重度、位置及成因 | [NightIQA](../papers/arxiv-2611.04811.md) | MCQ accuracy 不等同 MOS / pairwise preference |
| 主观/多维 IQA | 自然、真实性、局部品质与任务效用 | 既有 [VHA](../papers/arxiv-2610.25770.md)、EditJudgeBias、Face Contrast | 单一分数难以涵盖互不补偿维度 |

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

## References

- [LOL Benchmark audit](https://arxiv.org/abs/2610.38121v1)
- [CIE color judgment](https://arxiv.org/abs/2610.40212v1)
- [NightIQA](https://arxiv.org/abs/2611.04811v1)
- [VHA 卡片](../papers/arxiv-2610.25770.md)
