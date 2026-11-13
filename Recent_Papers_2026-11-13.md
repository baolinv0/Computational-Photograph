# 2026-11-13 周报增量：测量可靠性、端到端部署与评价审计

本快照只记录本轮新进入选择集的 6 篇论文及其决策变化；技术正文见唯一 canonical cards。核验到原论文选定方法、实验与限制，均未独立复现。

| Paper | 主题 | 本周决策变化 | E/T/S/A | Score |
|---|---|---|---|---|
| [EditJudge-Bench](papers/arxiv-2611.12524.md) | IQA/编辑评价 | 可控 3D 反事实证明 judge prompt/类别脆弱，先审计再当 reward | 4.8/4.6/4.8/4.9 | 4.76 |
| [Edge NPU Benchmark](papers/arxiv-2611.13563.md) | 端侧系统 | NPU-only 排名不能替代 vendor-native E2E 排名 | 4.7/4.2/4.7/4.8 | 4.58 |
| [LipsFlower](papers/arxiv-2611.13995.md) | 稳健恢复 | 稳健 gain 下降伴随可量化质量损失，要求画 Pareto | 4.5/4.4/4.4/4.4 | 4.43 |
| [Event Trigger](papers/arxiv-2611.13488.md) | Event/常开视觉 | 重建提升通用模型召回，但连续触发与功耗仍未闭环 | 4.4/4.2/4.6/4.4 | 4.42 |
| [Hyperspectral HDR](papers/arxiv-2611.13663.md) | 传感器/HDR | 测量域可靠性融合优于先反演再融合的思路 | 4.4/4.5/4.4/4.1 | 4.40 |
| [LIC Quantization](papers/arxiv-2611.13707.md) | Codec/部署 | 联合 RD 搜索显著降 PTQ BD-rate，但无真实硬件闭环 | 4.3/4.1/4.2/4.5 | 4.25 |

## 方向判断

- **端侧评价边界变硬：** 至少同时报告 model-call 与系统时延；缺 power/thermal/P95 时不能宣称 mobile-ready。
- **可靠性前移：** 光谱 HDR 在测量域做 channel/exposure reliability；event trigger 在表示层选择重建接口；两者都把“输入是否可信”放在下游模型之前。
- **评价器不再默认可信：** EditJudge-Bench 与既有 cue/order bias 证据共同要求可控 counterfactual audit。
- **负面证据：** LipsFlower 显示降低扰动放大可能明显牺牲感知质量；LIC PTQ 仍可能被算子 fallback 和熵编解码成本抹平。

## 已通知支撑，不重复标新

RetinexGS、Dark Matters、V2C-Edit、DeLang-SR、DynOLAT 等已在 2026-11-10—12 Paper Watch 入库，本周仅作为趋势支撑，不计入 6 篇新作。

## Coverage audit

本轮按日期与问题地图检索 arXiv/alphaXiv，并检查主要厂商与供应商官方入口。开放论文/官方页面覆盖强；OpenReview 全量、闭源社交平台、专利全量检索和独立复现未完成。Agent/world-model 没有新候选同时通过硬门槛，未强行补位。
