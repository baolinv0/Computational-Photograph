# Paper Watch v3.2｜2026-11-11：三个 Topic Update

## 检索契约和来源边界
- 本轮**真实成功检查**：[arXiv cs.CV / new](https://arxiv.org/list/cs.CV/new) 显示 **Tuesday, 2026-11-10** 的 250 条 new submissions，另核对 eess.IV / cs.LG 新公告，按 T01–T06/X01 搜索 HDR/RAW/AWB/低光/恢复/超分/编辑/Reward/效率及跨主题负例。并通过 alphaXiv 已关注 **15 名研究者**的 stable slug 索引回查 2026-11-02 后论文；部分索引时延/同名消歧仍为 partial。无需声称全网穷尽。
- 上一次成功档案 **2026-11-10** 的 [报告](Recent_Papers_2026-11-10.md) 仅覆盖 2026-11-09 official new submissions（首传 11-06 的另一批），本次 11-10 bulletin 中确认三篇新 ID、原文 v1 的 Selected Methods + Tables/Ablations 与 registry/旧历史去重。**arXiv v1 是本轮最早核验的可阅读全文证据，不宣称排除了早于 arXiv 的 OpenReview/ACM 源。**
- **仅 NeurIPS/SIGGRAPH Asia 录用并不是新论文事件**；例如 GenRM-Flow arXiv:2611.11421 已能找到 NeurIPS OpenReview ID dPSEe9I3nw 的先前条目，但无法核验首次公开全文日期，不按本轮新文提示，留 T04 公开日期与版本内容比较 backlog。旧 paper 换新公告分区/简单 crosslist 不触发。

## Topic 1｜T06/T02：在执行器内控制可发现性，而不只终态挑选

**旧地图**：FlowEdit（2025）用固定 source coupling 防编辑泄漏，但可能 zero-edit；DNAEdit/FlowAlign 调整 source-target 联合轨迹；ECT 的单时刻端点和 AR-Edit 的视频 source-V 缓存属**不同骨干/控制轴**。这些并行路线均要比较编辑成功和未编辑区保持。

**本轮新作**：[VLM as an Editing Pilot / V2C-Edit](papers/arxiv-2611.10066.md)｜Kuan-Shen Chiu 等｜最早可核验 v1 **2026-11-06**｜**GO-E / Bridge + Boundary refinement**｜主 T06；次 T02/T04/X01；角色 strategy / execution / evaluation。

- **机制一句话**：同一 flow model 的 velocity 有 source-anchored 到 decoupled/extrapolated 等不同候选，逐时刻用 VLM 指令完成度隐藏状态选择 velocity，适当 mask 保护背景。
- **可归因与反例**：作者 MagicBrush 535 / PIE-Bench 700、FLUX/SD3。Four directions vs coupling-only：**IA_GPT 5.69→6.07**，但未编辑区 PSNR **17.78→17.44**。强替代：在相同作者协议 brute-force 切换点搜索 **IA 6.22** 高于 V2C **6.07**，但背景 PSNR **16.18** 和 H100 **79.99s**，相较 V2C **17.44/26.44s**；原 FlowEdit 4.00s。Qwen3-VL-8B 逐步代理指标，未建立真实编辑幅度/肤色校准。
- **判断更新**：原先依靠终点候选选择的 Agent，可把动作决策下沉到一条生成轨迹的每步。**不变**：executor 可达、搜索可发现、judge 可选择仍独立；论文支持可发现性但不能说 VLM 解决所有目标匹配。
- **系统**：在线 RGB+instruction→多 velocity 与 terminal preview→ILS 评分→动态 mask→下一 flow step→RGB→独立 ROI fidelity 审查。离线保留原有 FLUX/SD3 和 VLM，不训练本控制器但需评估其 hidden-state signal。Agent 是策略层，不自动增加可用工具或数字精度。
- **决策/实验**：保留 GO-E 的 trajectory controller，当前局部确定性修图不变；必要时等 GPU 时间比较 FlowEdit fixed、brute t_cs、V2C 的 edit success 与 leakage。**记忆：更强编辑不是一味放松 source coupling，而是在合适时刻改变动作。**

[更新的编辑控制 Survey](surveys/one-step-inversion-free-editing.md)。

## Topic 2｜T03：暗光 SR 应分开估计方向和局部修复剂量

**旧地图**：RELLISUR（2021）真实低光 SR 任务、Restormer/CATANet 判别式恢复、DaLPSR (2024) 语言降质条件、S3Diff (2024) 单步生成 SR 与 GLOW-FM 的低光增强设计点。旧主张「语言 prompt 很新」不成立，须识别新增的控制变量。

**新作**：[DeLang-SR](papers/arxiv-2611.10485.md)｜Jiaxin Gao 等｜v1 **2026-11-07**｜**PROBE / Bridge + Boundary refinement**｜主 T03；次 T02/T05/X01；角色 goal/execution/training/evaluation。

- **机制一句话**：把由 LQ 统计确定的退化 intent/视觉 token 用于 SD3 flow 的 velocity direction，区域 strength map 决定一次 Euler  update 的本地 step size。推理不使用 oracle GT。
- **证据/反证**：RELLISUR ×2，作者 PSNR **23.865 dB/LPIPS 0.2186** vs DOD **20.806/0.2557**；同 S3Diff 基线同 5K update：base **21.358** vs full **22.986**，无 degradation language **22.433**，无 tokens **22.398**。真正可区分的是语言+视觉+局部剂量组合，**没有同容量纯数值描述完全取代文本的严格实验**。
- **成本重要负例**：4.48M trainable **不含** frozen SD3；**20,390.77 GFLOPs/0.448s** vs CATANet **21.266 GFLOPs/0.042s**（作者协议），1 NFE≠端侧可用。真实 DarkFace NR-IQA 不是恢复物理真实的证据。
- **判断更新**：少步生成恢复从「快不快」升级为「可靠输入区域应承担多大的生成修改」的空间强度控制；**不变**：信息缺失区域不可用 PSNR 或 VLM 一句话证明 hallucination 为真。在线 y→退化统计/intent→velocity+local strength→one-step RGB；离线 paired dark-SR/GT 训练 LoRA 和强度预测器。非 Agent 组件。
- **行动/实验**：PROBE，暂不替换手机 LLIE/TM。等训练预算比较 numeric descriptor vs language/numeric；单独打开 spatial step map 检查暗/明区域 PSNR 与人为纹理。**记忆：方向是什么，修改多少，是两个不同的控制变量。**

[更新的高效生成恢复 Survey](surveys/efficient-generative-restoration.md)。

## Topic 3｜T02/T05：可检查的动态光照响应基，而非只凭生成外观

**旧地图**：Lux Post Facto (2025) 使用视频 diffusion 直接重照明，HumanOLAT (2025) 提供 full-body OLAT 光照数据；UniRelight / RelightVid / DiffusionRenderer (2025) 是动态 relighting 的竞争执行器。参考或 prompt 能要求「换光」，却不自动保证方向/相对强度正确。

**新作**：[DynOLAT](papers/arxiv-2611.11210.md)｜Taoming Liu、Xiaowei Zhou 等（浙江大学/Cornell/4DV.ai/Ant Group）｜v1 **2026-11-08**｜**GO-E / New route + Engineering maturity + Boundary refinement**｜主 T02；次 T05/T01/X01；角色 acquisition/data/goal/execution/training/deployment。

- **机制一句话**：flat-lit 动态人像→生成不同单光源方向的 OLAT basis videos→按 HDR 环境图权重在线线性光域组合。额外信息来自实采 LightStage **24M+ frames、224 identity-outfit combinations**；不等于仅更强 backbone 的贡献。
- **证据与归因**：作者测试 OLAT paired GT，PSNR **26.23/LPIPS 0.0567** vs DiffusionRenderer **23.11/0.0900**，temporal LPIPS **0.02532 vs 0.02629**。Table 4：full bridge PSNR **27.61** 略低于 frame concat **27.67**，不可给 bridge 单项 SOTA 归因。为消除尺度歧义使用 channel-aligned metric，不能作为绝对光强精度验证。
- **核心失败边界**：8×A100 为 57 帧 1920×1088 生成 **101 basis 约 26.89 分钟**（201 基 52.01 分钟），且真实视频 delight 残余有色强阴影、不同方向基间一致性未得到保证。缓存后换环境图可快，但**首轮生成不是在线实时或手机 ISP**。
- **判断更新**：由直接条件生成新增可拆验的方向/强度物理控制接口；**不变**：正确光照方向不等于正确 RGB 相机光谱/色温，更不是无需硬件的端侧部署。在线 video→delight→OLAT bases→linear combination→验证时间/几何；离线同步多相机 LightStage→paired OLAT→bridge + direction training。Agent 非必需。
- **行动/实验**：GO-E 作为真实光照采集和物理响应数据路线；不改变单照片 Tone Mapping。仅需一个已知 OLAT 的同人物对照：direct conditional relight vs basis prediction 组合，分别检查 light direction、relative intensity、源图保持。**记忆：可控灯光不是换一种颜色风格，而是能够验证每一束光的响应。**

[新增 canonical 视频重照明 Survey](surveys/lighting-conditioned-portrait-video-relighting.md)。

## 完成/未完成
- 已创建并读回三篇 canonical card、新建一份 stable problem survey、在既有两份 survey 的竞争路线/数据/成本/判断章节实质插入，修订 [LITERATURE_MAP](LITERATURE_MAP.md)、[专题目录](surveys/README.md)、[总 README](README.md)、[registry](archive/registry.json)。Registry **86→89**；alphaXiv 新增三个经过 ID/membership 双检查的收藏：V2C-Edit→Agent，DeLang-SR→Restoration，DynOLAT→Color；未动 Reading/Completed。
- 未完成源覆盖：NeurIPS/OpenReview 和 ACM 最早全文上线时间的独立验证（不能用 arXiv 日期宣称绝对首次）、部分 alphaXiv 作者实体同名消歧、前序 DaLPSR/S3Diff/Lux Post Facto/HumanOLAT 的逐项同预算全文核验、DeLang-SR 跨传感器 RAW、V2C-Edit 真实肤色数值修图、DynOLAT 手机设备算力。
- 历史待查不是本轮新作名额，不因研究备案单独重通知。
