# PreserveReward: Reliable Consistency Reward Modeling for Image Editing via Dual-Teacher On-Policy Self-Distillation

ID: arxiv-2611.34446 | Xueheng Li, Yong Liu, Wen Xue et al. (JD.com, USTC, SCUT, Nanjing University) | T04 / T02,T05 | evaluation, reward, editing | GO-E | New evaluator route.
First verified: arXiv v1 2026-11-25; first covered/checked 2026-11-27. Original methods, benchmark/RL sections and selected ablations checked; no independent reproduction.
Decision key: preservation reward must localize subtle change and judge instruction necessity, not collapse to full-image similarity.

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [下一实验](#下一实验) · [References](#references)

## 快速回忆
- 9B reward model采用双教师 on-policy self-distillation：局部匹配 crop 捕捉微小改动，联合教师用全局上下文判断改动是否符合指令。
- 教师分数先在参考误差约束下做最小 KL 校准，再按与评分目标的梯度一致性选择过程监督；推理仅需输入前后图与指令。
- 价值在“结构化保真评价”，不等于奖励模型能证明编辑事实正确，也没有端侧部署证据。

## 精读记录
作者在 EditReward-Bench、EditReward-Compass 与 EBench-18K 上比较通用 VLM、编辑 reward 与消融，并用所得 reward 做编辑模型 RL 后训练。局部教师解决小区域漂移易被全局相似度淹没，联合教师抑制“应当改变的内容也被判不一致”；KL 投影与梯度路由针对教师偏差和优化冲突。
论文前页明确 JD.com 为主要机构；这是论文时公司署名，不是产品采用证据。

## 证据边界
结果均为作者报告；模型和教师规模大，训练/推理成本、移动端延迟、独立 MOS 与跨编辑器泛化仍不足。reward 参与 RL 后存在对评估器过拟合风险；细微身份、文字和局部几何是否被同一模型可靠覆盖，不能由综合分数替代。代码/权重的实际可用性待核。

## 2026-11-28 证据补齐（非新作/新版本）
原文 v1 §4/Table1–3 重核：9B 在 EditReward-Bench 的保真偏好 pairwise accuracy 为 base 39.80%、Score-MSE 67.30%、local-only 72.40%、joint-only 73.50%、full 80.60%；移除校准/梯度路由分别74.20%/75.90%。直接标签监督贡献显著，双教师及其路由在同骨干上提供增量，不能把各差值视为独立可加贡献。27B 在三个保真子集平均为84.70/84.60/80.73%，不是全维编辑分数。§4.1–4.2 说明 tie 阈值为1e-5；RL后 Qwen-Image-2.1 的 KRIS consistency 3.67→4.07（27B reward），由 GPT-6.1-Sol 打分而非独立人评，不能从表2推断用户偏好或 instruction success 同时改善。
前序 [CheckDistill](https://arxiv.org/abs/2610.26740) 已做 privileged checklist+on-policy distillation；此处真正增量是局部/全局视觉视野互补和监督冲突处理，不是首次使用自蒸馏。 [EditReward-Compass](https://arxiv.org/abs/2605.13062) 的同任务偏好对为评估基准，不是独立复现。强替代：相同标签、骨干及训练预算下，单教师同时提供局部与全局、推理期 crop+rubric、无蒸馏直接监督。真实照片保真与闭环修复效果仍待审计。主 [T04 survey](../surveys/artifact-grounded-reward-and-verification.md)。

## 下一实验
用隐藏编辑器、真实用户指令和未见主体构造“应改/不应改”成对集；把 OCR、身份、局部几何、色调和背景分层报告；让 reward 与独立人评、专用判别器交叉验证，并审计 RL 后是否只提高 reward。

## References
- https://arxiv.org/abs/2611.34446v1
- https://arxiv.org/html/2611.34446v1
