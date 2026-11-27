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

## 下一实验
用隐藏编辑器、真实用户指令和未见主体构造“应改/不应改”成对集；把 OCR、身份、局部几何、色调和背景分层报告；让 reward 与独立人评、专用判别器交叉验证，并审计 RL 后是否只提高 reward。

## References
- https://arxiv.org/abs/2611.34446v1
- https://arxiv.org/html/2611.34446v1
