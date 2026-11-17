# RecurIR: Learning When and How to Revise Restoration Policies via Recursive Self-Improvement

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [前序与竞争路线](#前序与竞争路线) · [证据边界与判断](#证据边界与判断) · [系统回忆与最小实验](#系统回忆与最小实验) · [References](#references)

**身份**：arXiv:2611.18006；Hu Gao、Haoran Zhang、Yulong Chen、Lizhuang Ma（上海交通大学/哈尔滨工业大学）。2026-11-13 10:33:36 UTC 首传 v1，2026-11-16 官方 cs.CV 新论文公告；首次覆盖 2026-11-17。已读 v1 原文方法、实验、主要消融和前序，非独立复现；其他作者提前公开材料未穷尽。

**主题/角色**：主 T06；次 T03/T05/T04/X01；离线数据生成、策略学习、在线工具选择和验证。**裁决：GO-E（条件策略和工程机制）**；地图 New route + Boundary refinement。

## 快速回忆

**一句技术命题（去作者术语）**：不要仅储存“某个恢复操作曾经成功”；用同一图像上的配对工具对照形成有条件的动作规则，主动合成足以使规则失效的退化，学习该改哪种工具、顺序、强度或区域，并仅保留通过迁移/保持测试的修订。

**旧→新**：工具调度与成功轨迹记忆 → 条件性策略假说、针对性反例生成、规则修订与外部验收。**记住**：失败例来自按假说主动构造的离线测量，并不是在线真实图像具有 GT 或自动知道正确恢复动作。

## 精读记录

- **输入/目标**：训练期 clean GT `x`、可控退化 `y=D(x;z)`、用户恢复意图、固定工具库；退化条件 `z=(type,severity,spatial distribution,interaction)`；目标是降低混合退化下工具调度错误，而非直接训练更大像素恢复器。
- **PDM / 条件规则**：在相同观测上对两条计划 `p_a,p_b` 执行相同工具库，以 `ΔQ=Q(R(y;p_a),x)-Q(R(y;p_b),x)` 构造带 GT 的相对偏好，拟合退化条件与计划收益的关系。
- **RTEM / 有目的的反例**：主动变化退化强度、覆盖范围、叠加关系，针对旧规则搜索失效边界。与一般随机数据增强的区别应由固定额外样本/计算预算的消融证明。
- **CPRM / 策略修订**：预测条件变化所要求的工具选择、执行顺序、操作幅度及 spatial mask 的变化，经独立 transfer 和 retention 测试后接受；否则保留旧策略。
- **训练和推理分离**：训练与规则验证使用 clean GT 和更多配对工具执行；在线只估计退化状态、按已学策略控制冻结工具库并输出图像。不能称“全流程在线无监督 RSI”。
- **作者证据**：论文主表上平均 PSNR 35.58 dB（其列举的强 Agent 基线 35.24）；自身逐步消融 34.88→35.11（PDM）→35.39（加 RTEM）→35.58（加 CPRM）dB，合计 +0.70 dB。另一真实雨数据集的 PSNR 差距较小（27.83 vs 27.65 dB）；无 GT 真实图的 FADE/BRISQUE/NIMA 不能证明实际保真。这些均为作者测试，须保留任务、预算及指标条件，不等同独立复现。

## 前序与竞争路线

| 路线 | 核心区别 | 关系 |
|---|---|---|
| AgenticIR（2024）、MAIR（2025） | 退化诊断、工具规划、反思/顺序先验 | 作者引用前序；RecurIR 重点转向规则随条件失效的学习 |
| EvoIR-Agent（2026）、SEAR（2026） | 经验/轨迹复用与验证后搜索 | 直接关联的先行 experience 路线；条件性规则证伪更显式，但并非第一次提出“学习经验” |
| Causal-AgentIR、SkillIR、PreActIR（2026） | 因果式经验表述、条件化技能、事前动作效果预测 | 部分机制竞争或互补；SkillIR 已处理技能适用条件，不能写成 RecurIR 首次考虑条件 |
| HarnessIR（2026） | 冻结生成式 MFM 上组织证据、指令和原图重试 | **分析者的接口比较**，未据文献证实 RecurIR 直接继承 HarnessIR；两者执行器不同 |
| 等预算随机困难例/固定 rule/单轮 memory 更新 | 同离线样本和工具前向数，比较是否真的需要主动“证伪” | 尚缺完全隔离的关键反解释 |

## 证据边界与判断

**主要贡献类型：**条件化经验学习与可证伪训练任务机制，非模型架构层的新像素生成先验。

**负面和未知**：受控退化上能测相对 Q，不代表无 GT 真实手机 RAW 能定义正确规则；策略更新的收益可能来自更多 hard cases、oracle GT 与离线工具执行预算；同工具库对照不等于总训练预算一致。真实域退化状态估计误差、反例有效性、跨相机/跨退化迁移、在线时延和完整训练成本尚不足以据此称已部署。避免把作者统计称独立复现或跨团队共识。

**判断变化**：从“记录成功轨迹/失败轨迹”进一步到“明确策略条件、主动找反例、审查修订”。保留的结论是：执行器可达性、计划搜索可发现性、结果选择可靠性仍须分别测量。

## 系统回忆与最小实验

- **目标/非目标**：目标是稳健工具策略；不是凭空恢复丢失的图像信息，也不是自动更新基础生成模型权重。
- **离线**：GT + 合成退化 → 控制变量 z → 同输入不同计划执行 → 条件收益拟合 → 受控反例 → 训练规则修订 → 迁移/保留验收。
- **在线**：退化图 + 用户要求 → 估计 z → 策略选工具/顺序/强度/区域 → 工具执行 → 原图与候选质量检查；GT 不可用。
- **Agent 控制**：学习策略选择不同于 per-step VLM velocity（V2C-Edit），也不同于候选后 Judge。
- **简单强基线**：固定工具/固定 budget + 随机 hard-example mining 或 equally-sized uniform task evolution。
- **最小判别**：保持 clean GT、工具库、离线生成/执行预算、控制器容量与独立测试集完全一致，只把 uniform difficulty mining 替换成 hypothesis-falsification task evolution；报告新条件 gain、旧条件 retention、有害动作率、完整 offline/online cost。

## References

- [RecurIR 官方 arXiv v1](https://arxiv.org/abs/2611.18006v1)
- [AgenticIR 历史 survey（CameraPaper）](https://github.com/baolinv0/CameraPaper/blob/main/knowledge/imaging-agent/agentic-image-restoration-survey.md)
- [EvoIR-Agent](https://arxiv.org/abs/2605.22208)
- [SEAR](https://arxiv.org/abs/2606.28971)
- [HarnessIR](https://arxiv.org/abs/2610.10133)
