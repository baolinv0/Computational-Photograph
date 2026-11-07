# 基于可观察伪影的 Reward 与候选验证：解释能否帮助选对？

版本 v0.1｜2026-11-07｜主主题 T04，连接 T06/T05

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

## References
- [ArtiVidRM v1](https://arxiv.org/html/2611.07301v1)
- [VideoScore (2024)](https://arxiv.org/abs/2406.15252)
- [NightIQA + CIE/GT 既有综合](low-light-iqa-and-gt-validity.md)
- [CameraPaper AgenticIR已有survey](https://github.com/baolinv0/CameraPaper/blob/main/knowledge/imaging-agent/agentic-image-restoration-survey.md)
