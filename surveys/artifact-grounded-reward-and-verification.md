# 基于可观察伪影的 Reward 与候选验证：解释能否帮助选对？

版本 v0.2｜2026-11-13｜主主题 T04，连接 T06/T05

目录：[稳定问题](#稳定问题) · [路线地图](#路线地图) · [新旧证据](#新旧证据) · [完整方案](#完整方案) · [决策与缺口](#决策与缺口) · [References](#references)

## 稳定问题
当图像/视频候选同时存在运动伪影、结构扭曲、时序闪烁、主观美感和指令完成度差异时，是直接输出一个scalar，还是把**可见事实错误**先写成可校验列表，再判断候选谁更好？伪影发现的准确性、偏好排序的可靠性、作为训练奖励后的优化安全性应分开评价。

记忆锚点：**会列出缺陷不等于能选对；能选对现有候选不等于能提升执行器可达性。**

## 路线地图
| 路线 | 输入、表示、监督 | 可以回答与典型失效 |
|---|---|---|
| 单分数视频IQA/Reward | 视频或视频+prompt→scalar；MOS/偏好/训练 | 快速排序，但质量轴混合、不可定位；VideoScore / VideoAlign |
| 自由语言推理的评分器 | 影片→自然语言理由→分数 | 可能解释但理由不一定与误差有因果关系；VisionReward / VideoScore2 |
| **结构化artifact-as-rubric + reward联合优化** | 视频对→伪影列表→分数/偏好；SFT + artifact recall/length + preference GRPO | [ArtiVidRM](../papers/arxiv-2611.07301.md)，可输出纠错描述；漏检/误检、同源LLM标注和reward hacking |
| **可控反事实编辑真值审计** | 源图+已知操作参数/负例→instruction-correctness；[EditJudge-Bench](../papers/arxiv-2611.12524.md) | 操作是否真正完成；合成二元 GT 非真人偏好 | 
| 物理/ROI/事实保持的外部验证 | 源图和候选+颜色/边界/时序/结构观测→多维证据 | 对真实成像保真必要，不可无条件压缩为一个偏好分数 |
| 原图重试+独立Judge | 原始任务+候选池→接受、回滚、停 | 能提高选择性，无法在候选池完全失败时创造成功 |

## 新旧证据
VideoScore (2024)、VideoAlign/VideoScore2 (2025) 与 VisionReward (2026) 是该任务对照基线；[ArtiVidRM](../papers/arxiv-2611.07301.md)（2026-11-05 v1，PROBE，Boundary refinement / Supporting evidence）增加“从多个inspector收集伪影，经视频证据核查，训练时对缺陷召回和分数偏好共同监督”的具体可实施链。结构化checklist思想已在图像编辑/评测工作出现，本次不能称其第一次提出“解释后评分”。

作者 Table 1 out-of-domain：GenAI-Bench 去除ties后0.753 vs VisionReward 0.744；MonetBench 0.697 < VisionReward 0.721。T2VQA-DB 的10候选排序最优部分指标，但VideoAlign Hit@1/Spearman更优，且基线比较有从其他论文直接引数、tie阈值不同。Table 2 移除SFT不总比未训模型好，这意味着结构学习是关键，而不能把所有贡献归因到GRPO。

NightIQA 的夜景失真定位、[CIE颜色评价](low-light-iqa-and-gt-validity.md)、CheckDistill 的结构清单是**不同任务的共同抽象机制**。它们对视频偏好和对真实修图的结论条件不同，不是假定已能无缝迁移的成熟系统。

## 完整方案
**离线数据/训练**：真实视频候选+人类偏好/MOS+多来源伪影标注 → 筛选/验证证据 → SFT artifact list → reward GRPO → held-out split上的伪影recall、pairwise winner、排序和鲁棒性。
**在线**：视频/原始prompt → artifact list→score→候选选择或提示修正；可训练生成器，但论文图像/视频推理与训练费用需分别统计。
**Agent层（假设）**：原始用户目标→固定K候选→artifact judgement与物理检查→拒绝/选择/回原图重做，不是原论文在手机影像中已验证的闭环。

## 决策与缺口
目前作为奖励证据表示的**PROBE**，不直接更换照片IQA或手机真实RAW评价方案。若最小测试：**固定同一候选池、标注预算、模型和调用预算**，比较“直接scalar”“free-form reasoning”“artifact rubric”的人类winner准确率及互相矛盾的故障检测，并核验是否提升实际任务/真实性而不仅是模型自身打分。
缺口：公开伪影标注的第三方一致性、不同tie阈值统一重估、生成视频→真实camera video跨域、真实物理GT下的内容保持、优化后的reward hacking；与其他归档结论同源的证据不视为独立共识。


## 2026-11-13｜EditJudge-Bench：已归档论文的事实正确性审计接入（backfill）

**主主题 T04，连接 T02/T06；系统角色 evaluation；GO-E；地图类型 Boundary refinement + Supporting evidence。** [EditJudge-Bench](../papers/arxiv-2611.12524.md)（Jens Parslov 等，arXiv v1 2026-11-09）已在 11-13 周报与 alphaXiv 收录，本次只补充专题路线，不作为新论文通知。

**去术语的技术命题：** 用已知三维编辑参数构造事实/反事实图像对，让模型判断编辑是否真的按照指令发生；不要把喜好哪个候选当作是否完成操作的真值。

| 竞争/互补路线与历史锚点 | 输入→控制/监督→输出 | 适用判断 | 失败边界 |
|---|---|---|---|
| [EditJudgeBias](../papers/arxiv-2610.01670.md)（10-01） | 真实编辑候选+交换顺序/线索→偏好稳定性 | 评委会不会因排序或 cue 反转 | 不直接知道编辑操作真值 |
| [CheckDistill](../papers/arxiv-2610.26740.md)（10-19） | teacher checklist+agreement→低 token reward | 结构证据是否可被高效蒸馏 | teacher 共享偏差 |
| [VGIQA](../papers/arxiv-2610.37186.md)（10-27） | SR 图像+缺陷 bbox→伪影定位 | 哪个局部出了问题 | bbox F1 不是指令完成或偏好排序 |
| **EditJudge-Bench**（11-09） | Blender 场景+真实/反事实指令→binary AUROC | 方向、对象、细微动作是否被看到 | 合成室内与二元验证不等于真实照片偏好 |
| [ArtiVidRM](../papers/arxiv-2611.07301.md)（11-05） | 视频伪影列表/偏好→reward | 描述缺陷能否帮助选择 | 视频偏好不验证物理真值 |

各路线关系为本 survey 的综合判断，不暗示作者直接方法继承。作者在 **1,382 组可控 Blender 前后图、九类编辑、25 种 judge 配置** 上报告：VIEScore+GPT-4o 仅 69.0% AUROC，部分微调评委为 51.7%–66.3%；图像/文本输入顺序让 AUROC 最多变化 14.1 个百分点。作者称 judge 在两个真实编辑人工偏好 benchmark 的**模型排名**相关为 0.95/0.71，不能当作真实照片上的同等绝对正确率或保真证明。均未独立复现。

**判断更新：** 此前问“artifact rubric 能不能让评委更会选图”；现在增加必要前置测试“评委能否看到已知操作是否发生”。二元编辑正确性、候选偏好、真实结构保持是不同目标。既有结论不变：好的 judge 不能创造 executor 生成不了的候选。

**系统方案回忆：**
- 离线：已知操作/ROI/magnitude→事实与反事实编辑→按动作类别、轻微变化、no-edit 和 prompt 顺序评估 judge→真实手机样本人工复核。
- 在线（建议组合，未在论文验证）：A/目标/B参考+固定候选→Code 核实显式 ROI/颜色/结构→审计过的 VLM 判断参考匹配与自然度→PASS/拒绝/保留原图。
- Agent 控制层可选：依据失败类型选重试或停止；可达性、可发现性、可选择性独立计算。
- 最小实验：固定 3–5 张候选与同调用预算，测试已知肤色 ΔL、色相方向、非目标区无改动，比较直接 Listwise 与 Code-evidence Listwise 的人工 winner 一致率。
- 待核验：真实人像肤色/阴影、文字、mask 边界、跨执行器、reward hacking。

**记忆锚点：**看出改了什么 ≠ 能判断哪张最好 ≠ 执行器能够达到目标。

原始依据：[EditJudge-Bench v1，方法/实验/附录](https://arxiv.org/html/2611.12524v1)。

## References
- [ArtiVidRM v1](https://arxiv.org/html/2611.07301v1)
- [VideoScore (2024)](https://arxiv.org/abs/2406.15252)
- [NightIQA + CIE/GT 既有综合](low-light-iqa-and-gt-validity.md)
- [CameraPaper AgenticIR已有survey](https://github.com/baolinv0/CameraPaper/blob/main/knowledge/imaging-agent/agentic-image-restoration-survey.md)
