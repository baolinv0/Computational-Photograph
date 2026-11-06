# Paper Watch v3.2｜2026-11-06｜四项新证据与三条长期路线

目录：[覆盖与裁决](#覆盖与裁决) · [T01](#t01新增观测vs推理的区别) · [T03](#t03通用恢复扩容与已知算子的生成式反演) · [T06](#t06训练期抑制多轮编辑漂移) · [边界与回执](#边界与回执)

## 覆盖与裁决

本轮恢复并查询 GitHub 2026-11-05 归档快照/66项 registry，搜索 Computational-Photograph 与 CameraPaper 入口，使用公开 arXiv cs.CV/eess.IV 当日列表、跨主题 alphaXiv 搜索与开放网页检索（2026-11-06），并针对本轮四篇 arXiv 2026-11-04 v1 阅读方法、选定结果与相关前序。不是全站无遗漏审计；核心作者逐人 7–14 日覆盖尚不完整，不能推进其成功水位。之前已覆盖的 CHROMA-MILL、Beyond CCT、NightIQA、Mobile AI ISP 报告等不重复推荐。

| 身份 / 公开日期 / v1 | 主主题与地图变化 | 决策 | 主要反例或价值 |
|---|---|---|---|
| [UGD-FM](papers/arxiv-2611.06422.md), 2026-11-04 | T01↔T03, Bridge / Engineering maturity | GO-E | 真 NIR 新观测 + 迭代稀疏匹配；强视差、采集成本未解决 |
| [UniRestorer++](papers/arxiv-2611.06042.md), 2026-11-04 | T03/T05/X01, Engineering maturity / Boundary refinement | GO-E | 接续 ICLR UniRestorer，引入局部多层路由、CDD-50 与规模曲线；SIDD 仍有专项恢复器优势 |
| [Dual Flow](papers/arxiv-2611.05843.md), 2026-11-04 | T03↔T01, New route / Bridge | PROBE | image–measurement 联合 flow，可满足已知 A 的末端前向一致；仅线性已知 A 和 Gaussian 主要证据 |
| [TailSteer](papers/arxiv-2611.06741.md), 2026-11-04 | T06/T02, New route / Boundary refinement | GO | 编辑器尾段参数训练降低十轮累积漂移，单轮能力仍有下降反例 |

## T01：新增观测 vs 推理的区别

**旧地图**：单 RGB 低光恢复、跨光谱对齐后导引、双模态融合各有适用条件；背景锚点 NAFNet/Restormer、NAID/SANet（未在本轮逐篇重审）。**新证据** UGD-FM 在 noisy RGB+unaligned NIR 上让 correspondence 随 flow denoising 变得更可信：FANVID Table6 2-step 30.34 dB standard FM，stage+state design 到 30.58 dB；window guide 30.03 vs sparse guide 30.58。部分增益来自**新增 NIR 信息与匹配机制**，非“一步 flow 神奇恢复没有拍到的纹理”。**不变**：遮挡、NIR/可见光差异、额外传感器成本和图像真实 GT 要单独处理。详见 [新 canonical survey](surveys/unaligned-guided-restoration.md)。

**方案**：在线 RGB+NIR/同步/外参 → confidence sparse alignment + 1–2 step conditional flow → RGB；离线多谱配对、Poisson-Gaussian 噪声、ROI/视差和真实采集对照。无真实 NIR 的单路手机 pipeline 暂不采用。**锚点**：同景第二份有效测量可减少不确定性，合成 NIR 不能复制真实观测价值。

## T03：通用恢复扩容与已知算子的生成式反演

**旧地图**：专项/restorer vs 共享 backbone/prompt/MoE，以及 BAM/PnP 这条 known-operator guided posterior route。本轮两篇新作不是同一种方法。

**UniRestorer++**：ICLR 2026 UniRestorer 已有粗细粒度路由。新作重点是 **局部稠密路由+可扩层级 LoRA 与 CDD-50**；同论文七任务均值 31.81→32.24 dB、CDD-50 OOD 23.09→23.46；512方块 A6000 171M/0.484s vs 176M/0.515s，2.9B 权重不能称移动端已部署。SIDD 与专项 NAFNet 仍存在差距。**判断更新**：专家数量的有效扩容需要误分类时的粗粒度回退；原本“specialist 可能更优”的判断不变。见 [统一恢复 survey](surveys/universal-restoration-degradation-routing.md)。

**Dual Flow**：已知 y=Ax+n 的物理 inverse problem，联合 image 和 noise-free measurement flow；以 operator-dependent correlated Gaussian denoising sufficient statistic 训练，最终 y_hat=A x_hat。作者 Table I CelebA 100 图报告 0.18s/image，仍不是 RAW/ISP 手机实测。与 BAM 是并行物理条件后验的**共同抽象机制**；不能把它误读成未知退化自动识别。**判断更新**：对已知线性算子加入可检验观测一致性是值得 PROBE 的执行路径，不替代 RAW nonlinear pipeline。见 [已增补的高效生成式恢复 survey](surveys/efficient-generative-restoration.md)。

**系统**：离线是复合退化训练 expert routing **或**已知 operator flow 的专项训练；在线是 LQ→专家识别→修复 **或** y+A→joint inverse flow→x_hat。这两种是并行解法，不是已证明可串联的产品链。**锚点**：已知算子约束和退化识别置信度是不同种类的控制变量。

## T06：训练期抑制多轮编辑漂移

**旧地图**：多轮 rollout training（[MT Forcing](papers/arxiv-2610.25404.md)）、保留原图重试、mask compositing 和执行后 judge；与任务式 Agent planner 分层。**新证据** TailSteer 用 editor 自有局部轨迹，保护区复制原图形成 endpoint，训练时前段模仿 base velocity、尾段在 student rollout 上逐渐转向 preservation；推理保持原编辑流程。

原文 100 张十轮实验 SenseNova onset42 第十轮保护区 PSNR 11.23→18.22 dB，指令完成比例 94.93%→94.78%；但单轮 Qwen RISE score 20.56→18.06，不能称零代价。所需 8×H100 微调不等于免费。**判断更新**：多轮漂移可通过编辑器内部尾段纠偏降低；不变的是文本 ROI 能否正确理解、候选能否生成和 Judge 能否选择依然是不同瓶颈。详见 [新多轮保真 survey](surveys/multi-turn-editing-preservation.md)。

**方案**：离线 self-generated local/identity instructions→preservation endpoints→on-policy tail steering→十轮/单轮双验收；在线不强制新控制器，仍用通用编辑器，必要时外部 ROI validator。对没有多轮瓶颈的编辑实验维持既有设计。**锚点**：抑制连续编辑漂移与让一次编辑正确命中指定区域不是同一问题。

## 边界与回执

以上为论文作者实验/所读原文选定章节，未做独立复现或跨模型等预算重跑。未触发新作的旧候选 UGD 外部前序、BiCG-Net（缺 target-level 人工 MOS）、ILLRAW（11-02）保留后续 triage，不占新论文推荐数；不能将历史日期冒充今日首发。

**归档**：四份 canonical cards；三个稳定问题名新 survey；高效生成式恢复原 survey 的 Dual Flow 分支；LITERATURE_MAP / registry / surveys索引 / README / 本期快照。alphaXiv 仅收藏核验 ID 的论文；实际 GitHub 与 alphaXiv 状态以写入与读回回执为准。未完：作者级逐一 overlap 审计、真实手机链验证、强历史前序逐篇重审。
