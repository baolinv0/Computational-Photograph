# Paper Watch v3.2｜2026-11-17：条件策略证伪与人类偏好下的 NR-IQA 失效

目录：[本轮覆盖与通知裁决](#本轮覆盖与通知裁决) · [T06 条件策略与自我修订](#t06-条件策略与自我修订) · [T04 IQA 人类偏好与刷分](#t04-iqa-人类偏好与刷分) · [跨主题与其余候选](#跨主题与其余候选) · [完整系统位置](#完整系统位置) · [证据与归档](#证据与归档)

## 本轮覆盖与通知裁决

- **成功检查的官方源**：arXiv cs.CV/new、cs.LG/new、cs.AI/new、cs.MM/new、eess.IV/new、eess.SP/new，2026-11-16 新公告；相较此前成功覆盖的 11-13 公告有新增窗口。并行对 T01–T06/X01 作题名/机制开放发现。
- **作者级**：alphaXiv 10 位领域关注者（Michael S. Brown、Lei Zhang、Radu Timofte、Tianfan Xue、Mahmoud Afifi、Wangmeng Zuo、Zhilu Zhang、Kai Zhang、Sida Peng、Xiaowei Zhou）核对 11-09 以来 recent 索引；Timofte 的 RipBench 非本范围，其他无本次达到门槛的候选。另 5 位已关注但非领域名单未逐个查询。
- **真实增量**：RecurIR 2611.18006（11-13 10:33 UTC v1）、TrustUIQA 2611.18429（11-13 17:10 UTC v1），均于 11-16 官方新公告列出，首次覆盖 11-17。未证实比 arXiv 更早的完整论文公开，因此 earliest_public_verified 用当前核验到的 arXiv v1，不称全网最早。
- **事件**：2 x new（均 GO-E）；无 duplicate old/update counted as new。只在此报告关键争议；完整证据和作者结果归各自 canonical card。

## T06 条件策略与自我修订

**旧地图 / 历史锚点（非新推荐）**：AgenticIR/MAIR 负责诊断、调度与反馈；EvoIR-Agent（2026）和 SEAR（2026）复用经验/轨迹；SkillIR/Causal-AgentIR 发展有条件技能与结构化经验；HarnessIR 在 MFM 执行器外组织 evidence/prompt/validation。它们不是确认的单向继承链。

**本次新增**：[RecurIR](papers/arxiv-2611.18006.md)（Hu Gao、Haoran Zhang、Yulong Chen、Lizhuang Ma，2026-11-13 v1；系统角色策略、训练）。技术命题：用 GT 配对工具执行学习**条件化动作偏好**，再主动生成破坏旧规则的退化例，学会因严重度、区域和混合形式变化而修改工具选择、顺序、强度和 ROI，通过独立 transfer/retention 验收。**主 T06，次 T03/T05；地图 New route + Boundary refinement；GO-E**。

**作者证据**：同套工具库下的自身逐项消融平均 PSNR 34.88 → PDM 35.11 → + RTEM 35.39 → + CPRM 35.58 dB；主表与强 Agent 基线 35.24 dB 对比。合成退化的 GT 和额外训练任务执行是真正成本，不得称在线自主免 GT 或相同离线预算。可替代解释是仅 hard-example mining + oracle + 更多工具前向数；真实跨相机泛化、冻结 MFM 和手机端执行未证。

**旧判断→新判断**：成功经验需要可检索；新增要求每个策略带清楚的有效条件，并主动找使它失效的证据；保留“经验不能替代实际执行器能力或 Judge 正确性”不变。**完整系统位置**：离线 GT+合成变化→同图多工具计划比较→条件效用→生成反例→更新策略→迁移/保持；在线低质图/估计退化→规则控制固定专用工具→验证后返回/拒绝。Agent 侧控制与训练端成本分开。

**行动**：保留已有方案，仅将 rule validity / counterexample 视为可研究变量。唯一最小判别实验：固定训练样本数、工具池、训练总调用、GT、模型容量和评测集合，比较 rule-falsification vs random hard-example mining 的未见条件改善和既有条件退化。

**记忆锚点**：以前那次做对，不代表换一种严重度/空间分布仍然做对。

主 living survey：[AgenticIR（CameraPaper 唯一正文）](https://github.com/baolinv0/CameraPaper/blob/main/knowledge/imaging-agent/agentic-image-restoration-survey.md)。[AUTOREF](https://arxiv.org/abs/2609.35530) 是 2026-09-28 旧文，作为相邻多参考生成的 harness 策略优化历史锚点；任务不同且无已证实直接继承，不触发额外新通知。

## T04 IQA 人类偏好与刷分

**旧地图 / 历史锚点（非新推荐）**：UIQM/UCIQE 的 hand-crafted 颜色/清晰度 proxy、URanker/Q-Align 等 learned/VLM IQA、gMAD/BAPPS 的主动分歧/配对人评，以及多轮生成 Banana100；本库 LOL GT 偏移和 [EditJudge-Bench](papers/arxiv-2611.12524.md) 事实操作审计属于互补任务，不能混当同一指标。

**本次新增**：[TrustUIQA](papers/arxiv-2611.18429.md)（Rishii Kumar Singh、Abhinav Rajput、Dinesh Kumar Vishwakarma，2026-11-13 v1；系统角色评价/Benchmark），系统比较 73 指标配置、4 份已有 MOS 数据及 20 人/32 源场景/1920 双选，另用简单过饱和/锐化、5 个可微 IQA 的 ε=2/255 PGD 和多步生成复制做压力测试。**主 T04，次 T03/T05；地图 Counter-evidence + Boundary refinement；GO-E**。

**作者证据**：五套人评参照下最佳跨数据源 worst-case κ=0.23；其自建两位评委 median κ=0.41；训练同源表现强的水下 metric 跨实验室 κ 至多 0.31；Pro exact-copy 条件下噪声约增加 2.5×，只有 22/73 metric 在每次检查点持续下降。SAUD 与 SAUD2.0 来自同实验室且有 33 场景重叠；73 配置也非 73 个独立模型。人类偏好和真实辐射不等价；作者并非首次提出 metric hacking。

**旧判断→新判断**：评委需验证是否看见正确操作；进一步要求其**在同一源图的候选中选对人类偏好赢家**，并对“增分不增质”的简单调色/生成链进行主动攻击。既有可达性/可发现性/可选择性区分不变；人类偏好、内容真实性和使用场景仍非一个统一评价轴。

**方案**：离线原始/候选/人评→跨域分层→pairwise κ/人-人基线→简单编辑/对抗/多轮漂移攻击→评委适用边界；在线（设计假设，不是论文部署系统）原图+固定候选池→经审计指标+独立结构/颜色证据→选优/拒绝；Agent 仅决定动作和是否接受，不能由指标创造正确候选。

**行动**：暂不简单替换 Judge；先固定候选池/人评和调用数，测 NR-IQA/VLM scorer 对过锐化/过饱和反例的胜者反转频率。**记忆锚点**：奖励优化成功可以只意味着刷分成功。

主 living survey：[低光、颜色、水下 IQA 可靠性](surveys/low-light-iqa-and-gt-validity.md)；[可控编辑与 artifact judge](surveys/artifact-grounded-reward-and-verification.md) 仅互补交叉链接。

## 跨主题与其余候选

- T01/T02/T03/T05/X01 全域检索并未产生除这两篇之外可据此高价值推送的充分证据；这不是认定全部相关平台不曾更新。
- 同公告候选 DiffusionSSD（2611.17908）涉及近存储/加速的方案，但硬件/E2E 真实性与移动 ISP 迁移未查足，暂 Watch/backlog，不作为通知；Real-Time Diffusion Relighting as Neural Sensor（2611.17438）需核对 IROS 2026 正式论文更早公开，暂不当新文；旧 DeLang-SR 11-16 新版本若仅排版修正不属于 material update。
- AUTOREF 作为新增监控分支继续检查多参考身份/风格冲突、Harness 自优化、模型能力适配、候选与评价；不挤占其余主题。
- OpenReview 全量和所有作者提前公开材料尚未完整核验，源级成功覆盖并非全网覆盖。

## 完整系统位置

```text
离线数据和训练：
  真实 GT/监督偏好 [T05/T04]
  ├─ 可控退化 + plan pair → 条件假说 → 反例 → 策略更新 [RecurIR/T06]
  └─ 同场景候选 + 人类选择 → κ/Metric-Hacking测试 [TrustUIQA/T04]

在线恢复：
  真实退化输入 → 诊断 → 可执行动作/候选 → Executor → 结构/事实/质量验收

Agent 控制层：
  挑动作、搜索、决定接受/回滚/停止；训练时 GT 和人工标签不能被假定线上可用。
```

组合以上两篇属于本 Survey 的设计推断，不是原论文共同验证过的系统；没有读取私人项目当前运行实验，不能声称任何现有代码已经实现。

## 证据与归档

- [RecurIR arXiv v1](https://arxiv.org/abs/2611.18006v1) · [TrustUIQA arXiv v1](https://arxiv.org/abs/2611.18429v1) · [TrustUIQA 作者代码](https://github.com/TrustUIQA/TrustUIQA)
- [归档协议](ARCHIVE_PROTOCOL.md) · [v3.2 规则](archive/PAPER_WATCH_V3.md) · [文献总图](LITERATURE_MAP.md) · [Identity registry](archive/registry.json)
- 原论文作者报告，独立复现：未做；详细核验范围与失败条件请看各自 canonical cards。GitHub/alphaXiv receipts 以操作实际读回为准。
