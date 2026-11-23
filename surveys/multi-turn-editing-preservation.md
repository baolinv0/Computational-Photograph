# 多轮编辑的未编辑区保真：避免误差随交互累积

版本 v0.2｜2026-11-23（历史路线补齐）｜主主题 T06，连接 T02/T05/T04

目录：[问题边界](#问题边界) · [竞争路线](#竞争路线) · [证据与裁决](#证据与裁决) · [在线与离线方案](#在线与离线方案) · [回溯与缺口](#回溯与缺口)

## 问题边界

同一照片连续多次文本编辑时，输出被反复作为下一轮输入。需要同时测：当轮意图是否满足、保护区域是否变动、文字/人脸/几何是否失真、每轮累计误差和完整成本。本专题关心**模型执行过程的多轮稳定性**，不是 Agent 自动选动作的正确率；与 [CameraPaper AgenticIR 综述](https://github.com/baolinv0/CameraPaper/blob/main/knowledge/imaging-agent/agentic-image-restoration-survey.md) 的 control/judge/rollback 属互补，保留该 canonical survey 不复制正文。

记忆锚点：**同一个模型单轮优秀，不意味着连续 10 次仍保持原有背景；单轮未编辑区少量泄漏可以在后续轮次累积。**

## 竞争路线

| 路线 | 在线输入/动作 | 离线监督及主要机制 | 能解决 / 不能解决 |
|---|---|---|---|
| 原样串行模型 | 每轮输入上一轮 RGB/指令 | 常规单步编辑训练 | 低集成成本，误差逐步叠加 |
| 每轮回原图/状态回滚 | 原图+累计意图 | LLM/Agent 保留原始观测、重写意图 | 降低累积污染；完整累计意图可能难以表达 |
| ROI mask/硬 compositing | 原图/保护区域 mask | 推理期分割/ROI 保护 | 可显式锁像素，边界融合/阴影不连续 |
| **跨轮有效属性与当前载体分离** | 当前proposal + 活跃目标 + 历史颜色证据 + 当前/旧ROI mask → 定点Oklab编辑；缺材质时生成新载体 | [TRACE](../papers/arxiv-2611.25648.md)：冻结编辑器，active goal retirement、carrier acquisition、tonal calibration、complete-request check | 同一目标区域内保留颜色但更换材质；有窄任务增益，通用多轮几乎与Core持平，额外VLM/生成成本未消除 |
| 跨回合 rollout / distill | 连续编辑历史和 teacher | [MT Forcing](../papers/arxiv-2610.25404.md)：对 student 自己历史和一次完成累计意图 teacher 对齐 | 训练较重；不能自动保证任意操作/区域条件 |
| **生成轨迹尾端保真训练** | 常规编辑器+已有指令 | [TailSteer](../papers/arxiv-2611.06741.md)：自生成局部训练数据/保护区 endpoint，前段模仿 base，末段纠偏 | 同步降低长期泄漏但可能轻伤单轮能力；不解决指令理解 |
| 执行前后选择/验证 | 动作、候选与 ROI 检查 | Judge/Router 可拒绝或原图重试 | 提升可发现/可选性，不扩大生成器能做到的候选集合 |

**关系说明**：MT Forcing 与 TailSteer 同目标而训练机制不同；不能由发布时间判定继承。TailSteer 对原图硬 compositing 是训练期替代/互补；对 Judge 是不同系统层。若无同条件对照，不称路线 A 全面胜过路线 B。

## 证据与裁决

[MT Forcing](../papers/arxiv-2610.25404.md) 在 100 个八轮 session 报告多轮 IF/CC 提升；其既有卡片是历史追索入口，今天没有重新核验全文，旧数值不升级为独立证据。

**2026-11-04 新证据 TailSteer**：四个大编辑器家族、同论文 100 图十轮保护区客观指标；SenseNova onset 42，第十轮 PSNR 11.23→18.22 dB，completion 94.93→94.78%；20轮是可视化案例不是 20 轮数据集的量化论证。Qwen-Image-2.1 的单轮 RISE acc 从 20.56 降至 18.06（onset 30）；明确**保真—编辑能力 trade-off**。八 H100/2,000 updates 是额外训练成本；推理无额外外部模型并非训练廉价。

**最强替代解释**：训练图源、监督 mask 的可靠性、回合 prompt 类型和生成模型选择影响指标；在不改变底座下做 ROI-protected compositor/从原图重试或等预算 best-of-K，可能得到部分保真收益。需独立对比受用户意图保护的 ROI 与真实编辑区过渡。

### 2026-11-23 历史补齐：活跃属性 ≠ 旧表面（TRACE；非新论文通知）

**新增的稳定子问题**：先前“保护未编辑区/控制误差累积”的视角，仍缺少“同一个区域持续收到不同属性指令时，如何保留未被新指令否决的属性？”例如蓝色玻璃→蓝色金属：不能复制历史蓝色玻璃像素；应在当前金属载体上执行历史蓝色色彩目标。这与退化恢复或单纯 mask 保护是不同的 T06↔T02 桥接问题。

**作者原文证据**：TRACE arXiv:2611.25648 v1 于 2026-11-19 首传（11-20 已成功覆盖的公告范围内），故 11-23 记 backfill。Section 4 Table 1 的 56 条两轮颜色/材质任务×2 seeds：完整请求 Native Both TRACE 96/108、All history 83/108；无目标提示的外观双属性 8B 41/112 vs 28/112。Table 4 固定同一 proposal 的受控比较：historical pixels 双属性 21/112 vs historical chroma 26/112 vs TRACE 41/112 (8B)，显示“属性执行”确实与“历史像素复制”不同。然而 Table 2 完整 EdiVal Klein 第三轮 IF 仅 30.77% (Core)→31.12% (TRACE)，O 66.87→66.93；Supplement S2 source-disjoint Klein 完整请求 60/125 (TRACE) 反而低于 Core 63/125、ReSpec 64/125。**窄场景成功不等于通用多轮压倒性改善**；MagicBrush 历史保真 All-history 也有反例。

**与已有路线的机制关系**：MT Forcing/TailSteer 在训练时改变编辑器以减少 drift；ReSpec/SEAM 的历史引用/状态服务于目标持续；TRACE 在冻结编辑器之外用规则化 active-goal、Oklab 局部算子、必要时生成新 carrier 和 complete-request admission 执行冲突属性。相关引用为前序/并行，不能由时间推断直接继承。其强简单对照必须是**同一初始生成 proposal、mask、全部有效目标、相同额外图像生成预算与 Judge**，否则无法识别是 chroma 参数化还是更多修正机会导致改善。

**完整方案与决策**：在线原图/当前图+新指令/历史有效属性→冻结编辑器候选→检测当前区域是否有正确材质→Oklab 在当前 carrier 上匹配历史目标颜色，或仅缺载体时生成局部修正→验证当前及历史 complete requests → 接受或停止。离线只做参数与规则评测，不声明该方法微调了执行器或拥有物理 GT。新增接口是“**目标属性—可用载体—可执行区域**”的显式绑定，不替代恢复真实性评估。**PROBE/Bridge + Boundary refinement**，现有单轮低层图像恢复执行方案不因本项改变。

**剩余缺口**：独立人工观察者/真实摄影图、颜色卡与肤色/白衣及保真约束、跨模型成本和各 VLM 判断可靠性；作者选定局部实验不能替代无 GT 真实恢复验收。

## 在线与离线方案

**离线训练**：原图与局部/identity prompt → base editor 自生成候选和轨迹 → 通过 mask/局部性检查 → 保留区复制原像素、编辑区保留 base 结果作为 endpoint → early prior matching + on-policy tail steering → 多轮/单轮平衡验证。

**在线推理**：真实用户原图与当前指令 → 单编辑器采样 → 检查目标 edit ROI 与保护区 → 接受/原图重试/拒绝 → 后续指令。Judge/Agent 并非 TailSteer 原论文的必需部件；此处外部检查是**系统设计假设**，未被多论文联合验证。

**决策**：对多轮模型训练 GO；对当前单轮 semantic region editing，维持原执行器基线不变，除非明确测出连续回合 drift 是主要瓶颈。若需最小判别实验，固定候选数、编辑类型和相同的保护区 mask，比较 base、base+原图 compositing 和 TailSteer，报告 turn-wise leakage 与 instruction completion 两条曲线。

## 回溯与缺口

待补：ConsLoRA/FreqEdit 原文与单轮副作用、MT Forcing v1/v2 的同数据条件比较；更长真实用户操作/不同指令是否使 mask 失效；保护区和阴影连续性/人像色彩失真；训练预算和推理端时延独立基准。

- [TailSteer arXiv v1](https://arxiv.org/html/2611.06741v1)
- [MT Forcing arXiv v2](https://arxiv.org/abs/2610.25404)
- [TailSteer card](../papers/arxiv-2611.06741.md)
- [TRACE arXiv v1，历史 backfill](https://arxiv.org/html/2611.25648v1)
- [TRACE canonical](../papers/arxiv-2611.25648.md)
- [跨仓库已有 AgenticIR survey](https://github.com/baolinv0/CameraPaper/blob/main/knowledge/imaging-agent/agentic-image-restoration-survey.md)
