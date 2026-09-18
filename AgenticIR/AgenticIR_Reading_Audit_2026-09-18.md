# Agentic 图像恢复与增强：五篇阅读路径核查

核查日期：2026-09-18。目标：最少阅读量覆盖问题、决策范式、演进与边界。以下选读判断针对已熟悉恢复网络、生成先验和 IQA 基础的读者，不是性能排名。未运行复现实验。

## 结论

原组合 AgenticIR / MAIR / 4KAgent / Restore-R1 / SEAR 部分符合标准，但对现成工具调度的覆盖偏多，对目标定义、工具协同失效的覆盖不足。

建议五篇：**AgenticIR → 4KAgent → Restore-R1 → OPERA → RetouchIQ**。MAIR 和 SEAR 移至问题驱动选读。4KAgent 只精读决策与消融部分，不需要重读超分模型。两篇新增工作是机制与边界读物，不称为公认经典。

## 一、对原五篇逐项核查

“强/中”评价的是对于本次阅读目标的贡献，不代表论文整体质量；“证据中”表示能支持限定条件下的主张，但不足以推出通用优势。

| 论文 | 范式代表性 | 问题解释力 | 演进关键性 | 证据可靠性 | 边界揭示能力 | 组合互补性与决定 |
|---|---|---|---|---|---|---|
| AgenticIR | 强：语言规划、视觉观察与执行反馈分工 | 强：复杂退化需要选工具、顺序和纠错 | 强：现代恢复 Agent 的清晰系统代表；不是最早序列决策 | 中：经验、回滚等消融支持机制；不等于所有真实退化可靠 | 强：感知错误、工具覆盖和搜索代价 | 高，保留作为框架入口 |
| MAIR | 中：同一工具编排路线加入结构先验与分工 | 强：用退化形成顺序缩小搜索空间 | 中：结构化优化，非全面替换原范式 | 中：同工具箱对照与消融有价值；逆序先验有条件 | 中：说明先验如何节约试错，也可能限制动作空间 | 相对低，移至“如何约束规划”选读 |
| 4KAgent | 中至强：先产生多个候选，再评价选择 | 强：诊断并不总能预知哪个工具最好 | 中：将测试时多候选选择系统化 | 中：收益应拆分为工具覆盖、选择器、规划与算力 | 强：感知/保真权衡、评估指标耦合及高成本 | 保留，但只读 Q-MoE 和对应消融 |
| Restore-R1 | 强：大模型评价训练轻量动作策略 | 强：在线推理和搜索成本能否转入训练 | 中至强：相对在线 LLM 编排的取舍；并非首次用 RL | 中：奖励与效率实验有支持；部分 NR 增益伴随 FR 下降 | 强：奖励代理与真实恢复目标可能分离 | 高，保留作为轻量策略对照 |
| SEAR | 中至强：长程搜索与持久轨迹记忆结合 | 强：搜索经验如何减少重复计算 | 中：AgenticIR 已有经验；新增在轨迹复用及搜索机制 | 中：同工具集、记忆/搜索消融；仍依赖诊断及裁判 | 强：冷启动、记忆失效和检索状态是否充分 | 有价值，但对当前五篇组合的增量低于目标/工具边界，转选读 |

原文入口：[AgenticIR](https://arxiv.org/html/2410.17809v2)、[MAIR](https://arxiv.org/html/2503.09403v2)、[4KAgent](https://arxiv.org/html/2507.07105v1)、[Restore-R1](https://arxiv.org/html/2512.18599v2)、[SEAR](https://arxiv.org/html/2606.28971v2)。

## 二、五篇应分别留下什么

| 顺序 | 论文与阅读重点 | 删除后失去的关键理解 | 读后产出 |
|---|---|---|---|
| 1 | AgenticIR：§3.2–3.3、经验和回滚消融 | 观察、决策、执行、验证怎样构成可纠错闭环 | 一张控制流程图，标明谁观察、谁决定、谁执行、谁验收 |
| 2 | 4KAgent：NeurIPS 终稿 §2.3、附录 C.1、G 的 Table 27–29 | “提前选对工具”和“执行多个后选对结果”是两种策略 | 对照固定候选池与动态规划，分开计算候选收益和规划收益 |
| 3 | Restore-R1：§3.2–3.3、Table 2–3、Fig.6 | 决策可以学进轻量网络；训练奖励决定策略偏向 | 定义状态、动作、停止条件和独立于训练奖励的验收指标 |
| 4 | OPERA：§3、§4.3、Table 1、附录 H/I/K | 工具不一定是严格逆算子；只改善规划可能碰到工具协作上限 | 将失败分为诊断错、计划错、工具能力不足、工具衔接失配 |
| 5 | RetouchIQ：§3–4、§5.4 | 增强存在多个合理答案；评价目标要随用户指令变化 | 写出任务条件下的成功标准，并区分目标表达、参数执行与奖励可靠性 |

[OPERA: An Agent for Image Restoration with End-to-End Joint Planning–Execution Optimization](https://arxiv.org/html/2605.22104v1)；[RetouchIQ: MLLM Agents for Instruction-Based Image Retouching with Generalist Reward](https://arxiv.org/html/2602.17558v1)。

## 三、关键证据与不能扩大解释的地方

### AgenticIR

将退化观察、经验文档、工具执行和回滚分开，适合建立系统认识。应重点区分“目标退化消除了”和“整张图没有被改坏”。其经验知识依赖具体工具，新增工具后经验不能自动视为有效；这也是本报告建议增加的工程验证项。它是现代闭环的代表，不意味着大模型最早提出恢复序列决策。[原文](https://arxiv.org/html/2410.17809v2)

### MAIR

在同工具箱设置下，论文 Table 5 报告平均耗时由 AgenticIR 的 63.04 秒降至 35.42 秒，调用次数由 5.15 降至 1.82。这支持结构约束在该设置中的效率收益，但不证明“多 Agent”本身是收益来源，也不能将按退化逆序恢复当成通用定律。适合需要减少搜索时定向阅读。[原文](https://arxiv.org/html/2503.09403v2)

### 4KAgent

正式论文附录 C.1 明确说明，部分超分设置直接执行各个 SR 工具并择优，因此这类结果不能全部归因于规划能力。选择和报告中使用部分相同 NR 指标，应视为评估耦合，不能直接指控数据泄漏。Table 27 的感知指标收益伴随 PSNR/SSIM 下降。正式论文可核查证据主要为自动指标和可视化；OpenReview 答辩索引提及的用户研究细节未核实，不据此断言从未做过人工评价。[NeurIPS 终稿](https://papers.nips.cc/paper_files/paper/2025/file/f0075fe4e59652cf43148dcfab8d3c93-Paper-Conference.pdf)、[OpenReview](https://openreview.net/forum?id=IKxKs3rF9V)

### Restore-R1

前身名为 SimpleCall。它使用冻结 CLIP 与 MLP 策略，以 DeQA 分数变化训练，推理仍是逐步决策，不是训练语言推理链。Table 2 的 Setting II 中，其 PSNR 为 17.958，AgenticIR 为 20.418；DeQA 则为 3.599 对 3.434。Fig.6 还展示更多动作使 NR 与 FR 指标分化。故选入是为了学习低成本控制及奖励边界，不是因为全面胜出。[原文](https://arxiv.org/html/2512.18599v2)

### SEAR

外部轨迹记忆加搜索不等于在线更新模型权重。Table 4 去掉记忆后，工具调用由 8.15 增至 16.75，PSNR 仅由 22.1332 变为 22.0222，主要体现计算复用价值。Table 2 中其平均耗时 1.98 分钟，仍高于 AgenticIR 的 1.09 分钟。检索主要依赖退化严重度，是否足以区分皮肤、文字和树叶是需要额外验证的问题。[原文](https://arxiv.org/html/2606.28971v2)

### OPERA

在 120 张合成输入上穷举每张 340 条处理链，发现高分链可以包含重复或不对应输入退化的工具；这能直接质疑“识别退化后各调用一次对应工具”的假设。另有仅优化规划与同时训练工具的对照。证据边界：穷举范围小，质量由代理指标定义，联合训练改变了执行器，不能把全部增益归给规划。不同指标也非一致上升。其历史创新性还必须对照 RL-Restore，而不能接受“此前工具全固定”的笼统叙述。[原文](https://arxiv.org/html/2605.22104v1)

### RetouchIQ

将指令转成 Lightroom 参数，并学习按案例形成评价标准的奖励模型。SFT、规则奖励、学习奖励及奖励训练方式有对照。但 GLM-4.5V 同时参与补写训练意图/推理和语义、感知评价；本次读到的主文没有建立独立人工偏好验证。PGRT 还把用户参考编辑置于策略结果之上：摆脱逐像素奖励并不意味着已经摆脱参考偏好假设。适合研究目标与奖励设计，不可据此宣称可靠读懂个体审美。[原文](https://arxiv.org/html/2602.17558v1)

## 四、演进如何读，避免把年份当进步

正式阅读前，用约 15–20 分钟看 [RL-Restore](https://arxiv.org/abs/1804.03312) 的问题建模和联合训练：2018 年已有工具选择、停止与策略/工具协同学习。这是历史校准，不要求额外通读一篇。

| 问题压力 | 产生的设计选择 | 判断 |
|---|---|---|
| 真实退化组合难以预设固定顺序 | 运行时观察、规划和反馈纠错 | AgenticIR 等提供机制证据；开放世界可靠性仍有限 |
| 事先很难准确预测工具收益 | 增加候选、执行后评价 | 与在线搜索是一类计算取舍；增益必须按预算核算 |
| 反复调用大模型成本高 | 训练轻量策略，或训练 VLM 更直接行动 | Restore-R1 与 TIR-Agent 是不同实现；不是都应被压成同一种模型 |
| 前一步改变后一步输入分布 | 工具链联合训练或可微执行 | 历史上已有思想；OPERA、VeraRetouch 是不同任务下的近期探索，尚非统一答案 |
| 同一图片存在多个合理增强结果 | 指令/偏好条件化目标与评价 | RetouchIQ、PerTouch、RetouchAgent 有横向线索；可靠个性化仍待更独立验证 |

趋势判读：可以说“决策的计算放在哪里、反馈如何学习、执行器如何适配”正在分化。不能据这些论文宣称 Agent 已普遍优于单模型，也不能宣称记忆、长推理或更多工具必然有效。

## 五、扩展候选池与去留

扩展检索用于防止只围绕原五篇自我验证。下表包含深入核查和路线扫描；未把所有候选视为同等完成了实验审计。

| 候选 | 本次检查层级 | 未进入核心五篇的原因或条件 |
|---|---|---|
| [RL-Restore](https://arxiv.org/abs/1804.03312) | 核心机制与历史主张 | 作为短导读，防止将旧思想误认新突破 |
| [Exposure](https://arxiv.org/abs/1709.09602) | 路线扫描 | 白盒滤镜与连续参数的重要前史；语言目标由 RetouchIQ 补充 |
| [AgenticIR](https://arxiv.org/abs/2410.17809) | 方法、消融和边界 | 入选 |
| [MAIR](https://arxiv.org/abs/2503.09403) | 方法、同工具比较、消融 | 约束规划选读 |
| [4KAgent](https://arxiv.org/abs/2507.07105) | 方法、消融、版本差异 | 入选，限定章节 |
| [Restore-R1](https://arxiv.org/abs/2512.18599) | 方法、奖励、表格与版本 | 入选 |
| [SEAR](https://arxiv.org/abs/2606.28971) | v2 方法、记忆消融、效率 | 复用历史经验选读 |
| [TIR-Agent](https://arxiv.org/abs/2603.27742) | v2 方法、奖励、比较协议 | 若目标变成训练 VLM 控制器，可替换 Restore-R1；当前五篇中重叠较多 |
| [OPERA](https://arxiv.org/abs/2605.22104) | 方法、穷举、联合训练、消融及局限 | 入选，作为默认假设的压力测试 |
| [RetouchIQ](https://arxiv.org/abs/2602.17558) | 主文、奖励机制、评价来源 | 入选 |
| [PerTouch](https://arxiv.org/abs/2511.12998) | 记忆与区域机制、消融、用户研究范围 | 若重点改为长期个性化，可替换 RetouchIQ；需补记忆长期收益证据 |
| [RetouchAgent](https://ojs.aaai.org/index.php/AAAI/article/view/40237) | 路线扫描 | 检索示例与交互有价值，当前与闭环/经验部分重叠 |
| [PhotoArtAgent](https://arxiv.org/abs/2505.23130) | 路线扫描 | 易懂应用入口，新增决策机制有限 |
| [PhotoAgent](https://arxiv.org/html/2602.22809v3) | 路线扫描 | 美学规划与 MCTS，适合更广的生成编辑，当前范围偏宽 |
| [VeraRetouch](https://arxiv.org/abs/2604.27375) | 路线及执行器机制 | 如关注可微参数执行而非控制策略，可替换 OPERA |
| [Restore, Assess, Repeat](https://arxiv.org/abs/2603.26385) | 方法主线扫描 | 重要对照：评价/恢复可内化为潜空间迭代，不必外接工具编排；因用户熟悉网络基础，暂不占名额 |
| [DiTTo](https://arxiv.org/abs/2605.30915) | 路线扫描 | 模拟器帮助构造轨迹训练；应避免直接等同在线世界模型规划 |
| [Causal-AgentIR](https://arxiv.org/abs/2607.21125) | 摘要级发现 | 因果记忆值得观察，未完成足以支持替换的证据核查 |
| [Dotting the Eye](https://arxiv.org/abs/2609.01148) | 摘要级发现 | 意图与视觉焦点方向值得观察；不能仅凭最新入选 |

## 六、读完后应能回答的五个问题

1. 问题到底是诊断不准、动作选择不好、工具做不到，还是验收目标不对？
2. 同工具、同预算下，复杂控制器比固定流程或固定候选池多贡献多少？
3. 训练优化的是哪个奖励？有没有独立指标和人工偏好证据确认收益？
4. 经验存在哪里：规则、语言文档、模型权重、搜索树，还是持久记忆？何时失效？
5. 对一张低光人像，系统何时接受、回退、停止，何时交给人判断？

建议将上述问题填入同一张对照表。比为每篇写独立摘要更能形成可迁移的研究框架。核心验收应含质量收益、改坏率、保真、稳定性和总成本；这属于本报告建议，不是现有论文已完成的统一标准。

## 附：检索与版本限制

检索结合论文检索脚本、网页搜索、alphaXiv 候选发现，以及原论文与作者仓库。六张附件已查看，内容为宏观会议趋势图，本次没有将它们当作具体 Agent 机制或效果证据。

脚本查询为 `agentic image restoration`，2018–2026，每源最多 10 条。五个 API 来源未成功运行；原始错误如下：

```text
[open_alex] unavailable (import failed: No module named 'requests'); skipping this source.
[dblp] unavailable (import failed: No module named 'requests'); skipping this source.
[crossref] unavailable (import failed: No module named 'requests'); skipping this source.
[openreview] Error: openreview not installed. pip install openreview-py
[semantic_scholar] unavailable (import failed: No module named 'requests'); skipping this source.
```

因此不声称完成六数据库全覆盖。替代检索已用于本次筛选。脚本 arXiv 命中偏宽，以下 10 项均未作为 Agent 决策范式入选依据；其 citation=0 是返回字段，不能当真实引用数。

| 脚本原始 arXiv 命中 | 年份 | 本次处理 |
|---|---|---|
| [Restore-RWKV: Efficient and Effective Medical Image Restoration with RWKV](https://arxiv.org/abs/2407.11087) | 2024 | 主题偏离，排除 |
| [Beware of Aliases — Signal Preservation is Crucial for Robust Image Restoration](https://arxiv.org/abs/2406.07435) | 2024 | 主题偏离，排除 |
| [NTIRE 2025 Challenge on RAW Image Restoration and Super-Resolution](https://arxiv.org/abs/2506.02197) | 2025 | 主题偏离，排除 |
| [Multi-level Encoder-Decoder Architectures for Image Restoration](https://arxiv.org/abs/1905.00322) | 2019 | 主题偏离，排除 |
| [On the unreasonable vulnerability of transformers for image restoration — and an easy fix](https://arxiv.org/abs/2307.13856) | 2023 | 主题偏离，排除 |
| [Unsupervised Lesion Detection via Image Restoration with a Normative Prior](https://arxiv.org/abs/2005.00031) | 2020 | 主题偏离，排除 |
| [DVANet: Degradation-aware Visual-prior Alignment Network for Image Restoration](https://arxiv.org/abs/2606.19097) | 2026 | 主题偏离，排除 |
| [Exploiting Deep Generative Prior for Versatile Image Restoration and Manipulation](https://arxiv.org/abs/2003.13659) | 2020 | 用户熟悉的生成先验基础，排除 |
| [RFormer: Transformer-based Generative Adversarial Network for Real Fundus Image Restoration on A New Clinical Benchmark](https://arxiv.org/abs/2201.00466) | 2022 | 主题偏离，排除 |
| [V-Bridge: Bridging Video Generative Priors to Versatile Few-shot Image Restoration](https://arxiv.org/abs/2603.13089) | 2026 | 当前决策层问题之外，排除 |

没有按引用量、关键词频次或会场排名筛选，因为来源不齐、查询命中偏宽，这些统计会误导本次目标。上述选择不构成穷尽式系统综述。

MAIR 的 [IJCV 出版记录](https://link.springer.com/article/10.1007/s11263-026-02792-5) 已核实，但付费终稿正文未完整取得；分析以公开稿为准。4KAgent 的会议终稿 PDF 已核查，终稿 Table 27–29 对应早期 arXiv v1 Table 23–25，不应混用表号。OPERA [作者仓库](https://github.com/xsyshuishui/Opera)已查看到训练说明；仓库存在不等于复现实验成功。没有核实到代码的论文，也不据此断言代码一定未公开。
