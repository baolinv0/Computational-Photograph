# Adaptive Low-Light Enhancement for Road Anomaly Detection: A Multi-Architecture Benchmark and Edge Deployment Study

目录：[快速回忆](#快速回忆) · [方法与对照](#方法与对照) · [原文证据](#原文证据) · [归因与边界](#归因与边界) · [研究位置](#研究位置) · [References](#references)

- **Canonical ID**：arxiv-2611.08393；**版本**：v1，2026-11-05 18:06:59 UTC 提交；最早本次可核验公开材料：2026-11-05 arXiv v1；**first_covered / checked_on**：2026-11-08；**事件**：backfill（2026-11-07 已成功扫描 11-06 日列表，这不是本轮新研究通知）。
- **作者**：Obed Honour Eje、Oluwatosin Kolade、Glory Bagai、Taliha Abiodun Folorunso；Federal University of Technology Minna、Obafemi Awolowo University。
- **定位**：T06（主）/T01、T03、T04、X01（次）；**角色**：策略/执行/评价/部署；**地图变化**：Supporting evidence + Boundary refinement（未达到新的独立系统路线）。
- **裁决：WATCH**。作者给出有用的负面结果与 Jetson Nano 计算代价，但工作限定小规模道路检测、合成低光和简单亮度路由；没有验证真实夜间/复杂混合退化的泛化，也未解决路由收益的因果归因。
- **证据等级**：原文 HTML v1 的方法、表 I/II、讨论与 References 已核，selected_sections_checked；未运行代码、未复现实验。原论文和官方 arXiv 元数据是一手依据。

## 快速回忆

**无作者术语的一句话命题**：把低光增强无条件放在目标检测前面，会在部分光线条件下损害检测；一个低成本条件分支可能减少损害，但不能保证每个检测器上都有增益。

**记忆锚点**：`router 减少 uniform enhancement 的伤害 ≠ router 优于 always-KEEP`，尤其当检测器本身已对某个光照条件相对鲁棒时。

**不把它当本轮新作**：arXiv v1 于 2026-11-05 提交，与 2026-11-07 Watch 入选论文属于同一已查公开窗口；本轮仅补齐此前漏选的 T06 支持/反例。

## 方法与对照

- 数据：两套公开坑洞和减速带数据合并为 4,444 张，640×640、70/15/15 划分；验证 667 张、测试 666 张。
- 固定四种检测器，训练均仅在 clean training images 上；合成 gamma、近似 Poisson-like noise、严重光照追加水平 motion blur。合成雨和 Harmattan 也评测，但**SCI 并未应用到天气退化图像**；光照和天气未复合。
- 固定已有 SCI 权重（medium/difficult），路由仅计算 Rec.601 平均亮度：`L>=0.40` KEEP；`0.20<=L<0.40` moderate SCI；`L<0.20` denoise + strong SCI。不是 learnable router；且并非每张 dusk 图都会 KEEP。
- 基线：always-KEEP，统一执行 Plain SCI，Rule-based Adaptive；并报告四检测器和 Jetson Nano 各分支计时。没有进行一个固定预算、等处理强度的“仅更换 SCI variant / 门限”的完整对照。

## 原文证据

作者 Table I 的合成验证数据（mAP@50，越高越好）：

| Detector / lighting | Always-KEEP | Plain SCI | Adaptive |
|---|---:|---:|---:|
| RT-DETR dusk | 0.861 | 0.722 | 0.847 |
| RT-DETR night | 0.612 | 0.679 | 0.657 |
| YOLOv12n severe | 0.305 | 0.368 | 0.294 |
| YOLOv8n severe | 0.268 | 0.282 | 0.218 |
| Faster R-CNN night | 0.548 | 0.442 | 0.407 |

**更强的反例**：在夜间和严重低光，Adaptive 不仅可能比 Plain SCI 差，也可能**比从不增强更差**。例如 YOLOv8n severe，0.218 < always-KEEP 0.268；说明作者报告的“挽回 dusk 损失”不能外推为跨光照、跨架构最优分支决策。

**实测成本**（Table II，Jetson Nano 640×640，作者报告，含亮度/增强/检测）：YOLOv8n A(clean) 25.83 FPS、B(dusk) 18.18 FPS、C(severe) 13.52 FPS；RT-DETR A/B/C 8.23/7.65/6.69 FPS。计时 10 次预热后 50 次；它是该硬件上列明处理阶段的 pipeline FPS，不是手机 SoC 的产品端到端 FPS。

## 归因与边界

1. **问题已被前序提出**。论文自己引用 IA-YOLO、GDIP-YOLO、DENet/DE-YOLO 等 always-on 增强，并引用 YOLO-DER、ClassLIE 等 enhance/bypass 策略。因此“条件增强”不是新抽象；实际增量是特定任务的无需训练三分支规则、损害示例与 Jetson 代价。
2. **没有隔离路由机制优势**。Adaptive 的分支决定同时改变 SCI 权重版本、denoise、是否增强；缺少 always-medium-SCI、always-strong-SCI 及同计算预算相应对照，不能把收益全部归给亮度门控。
3. **合成成像不等于实机采集**。输入由已拍 RGB 经 gamma 与噪声合成；不是传感器曝光、RAW 噪声、真实空间混合光、运动的完整前向 ISP。论文明确将真实恶劣天气和混合退化留作未来工作。
4. **部署条件有别**。Jetson Nano 速度展示运行可行性/瓶颈，不证明车载全链路安全性或手机 NPU/GPU 成本；部分分支远低于 15 FPS。
5. **不同检测器收益方向相反**。这支持任务/下游模型条件化思想，但并未证明单独依靠图像平均亮度就能知道是否应该恢复。

## 研究位置

与 [Gate3DGen](arxiv-2610.31649.md) 属于“KEEP 与执行动作分开评估”的**共同抽象机制**；无已核实直接继承。Gate3DGen 是几何下游与学习 router，真实 proxy 路由同 always-PURIFY；本文是合成道路检测、手写亮度 router，几个架构仍低于 always-KEEP。后续检索方向是原文所列 YOLO-DER、ClassLIE、IA-YOLO 等真实检测场景竞争方案；完整独立复核欠缺。

- **暂不采用**为通用 ISP/照片增强模块。对真正需要面向检测任务的输出，固定同源图像、检测 backbone、增强网络及预算，优先做 always-KEEP / always-Enhance / per-backbone 规则 router 以及真实低光测试。报告 mAP、漏检和各分支完整延迟，不用 NR-IQA 代替任务指标。
- 这只是跨领域的反例补充，不改变当前照片 TM 或区域修图系统的已定方案。

## References

1. [原论文 arXiv v1](https://arxiv.org/abs/2611.08393v1)；[HTML 方法、Table I/II](https://arxiv.org/html/2611.08393v1)。
2. [Gate3DGen v1](https://arxiv.org/abs/2610.31649)；[已归档的竞争路线及失败证据](../surveys/selective-task-aware-restoration.md)。
3. Ma et al., **Toward Fast, Flexible, and Robust Low-Light Image Enhancement (SCI)**, CVPR 2022（论文 Reference [9]，本轮未重新核原文）。
4. IA-YOLO / GDIP-YOLO / YOLO-DER / ClassLIE（原论文 References [23–27]，本轮仅完成该论文的引用链识别，未将其当独立核验证据）。
