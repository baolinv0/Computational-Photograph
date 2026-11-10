# Paper Watch v3.2｜2026-11-10（Topic Update）

## 检索身份与覆盖边界
本次公告源 [arXiv cs.CV/new](https://arxiv.org/list/cs.CV/new) 于 2026-11-09 发布，包含前一工作日 **2026-11-06** 首次上传的研究；这批文献在前一次 11-09 早晨已成功检查之后才进入当日公告。与 `archive/registry.json`、11-06/11-07 通知及 LEGACY 对照后，本轮四篇属于全新 canonical ID（不是早期会议通知、旧文章补查或 v2 修改）。arXiv 已核验 v1、论文选定方法/表格/消融；不同来源最初公开证据仍以本次可见 v1 为限。
检索：arXiv cs.CV/eess.IV/cs.LG 新增公告及多主题开放检索；alphaXiv 15 位现有关注学者 11-01 后近期论文，少数同名作者索引匹配保留 partial。并非所有视频生成/3D/agent coding 都自动纳入本 watch。没有把上轮已经覆盖的 2611.08264 或 2611.08393 当新作。
所有数字都是原论文作者报告，非独立复现；所有系统合成联系为分析者推断，未做联合原型。

## Topic Update｜T03：测量一致性与生成先验分布并非同一个目标

**旧地图**：BAM/Dual Flow 与 DAPS/SITCOM 都在已知 A 的反问题中使用先验；前者注重给定测量条件的生成流，后者在预训练 diffusion 上迭代反演。强基线不只有模型大小，也包括是否训练 A、总优化步骤数和真实误差假设。

**新证据**：[FANO](papers/arxiv-2611.08923.md)｜Shilong Han、Hongxia Wang｜2026-11-06 v1｜**PROBE / Boundary refinement**｜T03 主，T01/X01 次；角色执行/评价。作者指出 SITCOM 的直接 x_t 优化即便残差下降也可能把扩散噪声分量推离 typical shell；锚定 x0、只优化 e 的方案在 FFHQ100 模拟 HDR 由 SITCOM 28.13→FANO 29.88dB。固定半径 variant 为 29.06dB，证据表明 e-search 是主要增量，极坐标半径控制也是 HDR 任务增量。强反例：已知 A、Gaussian 噪声和 256² 合成观测，不代表真实传感器；N=50 K=30，每层 backprop，不能视为端侧解法。FANO 直接讨论 DAPS/SITCOM；和 BAM/Dual Flow 并列由专题综合，不建立未经证实的继承。

**判断**：原先“观测约束与生成先验互补”不变，新增“约束优化变量自身的分布可能是恢复质量的独立瓶颈”。离线：已知 A/模拟测量和 GT→固定预训练 DDPM→等预算指标；在线 y+A→选择 x0/xt/e 或 joint-flow 路线→x_hat→measurement consistency + fidelity；Agent 非必要。行动：不改手机 TM，保留对照 `SITCOM+简单末层 radius clamp` vs FANO-Sphere 的最小判别。记忆：**观测越拟合，图像未必越真实。** [完整路线](surveys/measurement-consistent-generative-inverse-problems.md)。

## Topic Update｜T02：固定内容编辑，什么时候需要物理量或注意力源特征？

**旧地图**：确定性 ROI/LUT、generative edit、单时刻 ECT、时空 FlowEdit 等是控制/执行的不同途径；参考只是目标线索，不能保证 pixel identity。

**新证据1**：[Paste2Place](papers/arxiv-2611.09387.md)｜Hongzhen Li 等，Transsion｜2026-11-06 v1｜**GO-E / Bridge+Engineering maturity**｜T02 主/T05+X01 次；角色目标/数据/执行/训练/评价。给定已放置物体 RGB+mask，source-anchored latent bridge 与 I=A⊙S+R 物理重组联合建模前景重照明、背景投影/反射。77,218 Blender 实例+9,055 real-derived pair，paired bench 1250，Wild 250。作者消融，原 FLUX baseline 22.07→训练 bridge 29.68→物理引导 30.83 dB；物理净效益约 **1.15dB**，主要总增益不能误归因物理模块。强前序 LBM、Intrinsic Harmonization、IC-Light 与 SHINE，分别是桥接机制和相邻任务；真实肤色光谱/手机端未测。离线 G/B/O 对齐渲染及真实对→物理标签→联合训练；在线拼图+mask→单步光影校正→检查前景文字和背景区域。记忆：**对象内部和对象外部都属于同一次光照事件。** [完整路线](surveys/object-scene-composition-and-relighting.md)。

**新证据2**：[AR-Edit](papers/arxiv-2611.09795.md)｜Hovhannes Margaryan 等｜2026-11-06 v1｜**GO-E / New route**｜T02 主/T06+X01 次；角色执行/策略/部署。3–4 步 DMD-distilled causal 视频生成器：源帧一次前向 V-cache，目标 prompt 编辑时分层注入 V，流式视频免反演。单 H100、Reward Forcing 4步，source adherence 7.28，text 6.11，**6 NFE / 10.50 FPS**，同预算 DynaEdit 13 NFE/4.66 FPS；StreamEdit 15 步保留源更强，且 10.5FPS 未达消费端 30FPS。与 ECT 的关系是共同减少编辑开销，模型架构与输入约束不同，非直接继承。在线源视频→V-cache→因果逐 chunk target generation→源结构和 edit fidelity 验收；底座蒸馏在离线已完成，Agent 非强制。行动：保持静态 ISP/修图方案，流式编辑分支可单独追踪。记忆：**保留 source 的 V 不等于反演 entire noise chain。** [现有专题修订](surveys/one-step-inversion-free-editing.md)。

## Topic Update｜T04：能够判读失真，能否直接执行修复？

**旧地图**：视觉质量/缺陷诊断、给不给恢复器、恢复器自身 capacity 与 Judge 选择是四个变量，Gate3DGen 的真实域 router 和道路低光门控此前已提供 KEEP 基线反例。

**新证据**：[Zero-Shot Benchmarking of Unified Multimodal Models for Shallow-Water UAV Image Distortion Assessment and Restoration](papers/arxiv-2611.09740.md)｜Dario Scilla 等，KAUST 等｜2026-11-06 v1｜**GO-E（负结果/新 benchmark）/ Counter-evidence**｜T04 主/T03+T05+T06 次，角色评价/执行/数据。五个冻结 unified MLLM 在 1000 成对 shallow-water UAV 退化样本诊断，100 张零样本恢复。作者发现最佳失真检测 balanced accuracy 约0.654，PSNR 最大平均 +0.255 dB，pool LPIPS 皆未改善且出现 hallucination。前序/竞争：InstructIR、专项水下恢复与基于物理散射方法；不是同一测量任务的普适 MLLM 否定。在线 image→诊断（不强制 VLM）→specialist vs direct MLLM→独立 fidelity+假细节审计；离线配对与人标基准仍有浊度标注分歧。行动：保留可达性/可选择性分离，别把一个诊断性描述当编辑器控制成功。记忆：**找到病因，不等于具有修复动作空间。** [选择性恢复专题修订](surveys/selective-task-aware-restoration.md)。

## 维护与待查
新建 4 canonical cards、2 个稳定专题；按具体路线与反例更新现有一步编辑和选择性恢复专题、[总图](LITERATURE_MAP.md)、[专题索引](surveys/README.md)、[registry](archive/registry.json)。alphaXiv 仅向用户已有主主题收藏新 ID，保持 Reading/Completed。
未完成：核心作者的全局身份消歧、DAPS/SITCOM/SHINE/ObjectDrop 等前序逐篇原文重查、真实 RAW 反演、上手机端部署、真实水下成像域泛化、第三方复现；余项在对应 survey backlog，不能提升证据等级。
