# 影像研究文献地图：从单篇论文到系统认识

版本：v0.7｜结构建立/最近实质修订：2026-11-14

目录：[使用方法](#使用方法) · [系统总图](#系统总图) · [长期主题](#长期主题) · [三个连接示例](#三个连接示例) · [主题更新卡](#主题更新卡) · [回忆与维护](#回忆与维护) · [变更记录](#变更记录) · [来源与覆盖](#来源与覆盖)

> 本页是持续修订的问题地图，不是按时间堆叠的论文列表，也不是一套已经验证有效的完整算法。论文正文继续保留在各自 canonical card；本页只保存问题、路线关系、系统位置、判断及未决问题。
>
> 本版建立六个长期主题和一个横向约束层，演示三个已归档案例的连接。它不代表所有历史推荐已重新核验或全部接入。公开地图不记录私人项目实验、个人阅读状态和未公开研发信息。

## 使用方法

遇到新论文，先问：它回答哪个长期问题、改变哪项假设、在系统中改了哪一个接口？再阅读标题和模块名称。

同一篇论文可以支持多个主题，但只有一个稳定身份和一份技术正文。主题中的路线是并列备选，不按“年份越新越先进”排列。没有改变原判断的论文可作为支持证据，不必新增路线或重写整体方案。

记忆单位：**问题 → 路线选择 → 代表机制 → 证据边界 → 当前判断**。不要以记住论文简称的数量衡量理解。

## 系统总图

### 在线成像与编辑

```text
场景 / 用户意图 / 设备与显示条件
                 ↓
采集控制：曝光时间、模拟增益、帧数、传感器模式              [T01]
                 ↓
RAW / 多帧观测 / 元数据 → 对齐、可靠性与可恢复信息分析
                 ↓
恢复与融合：确定性恢复 / 生成辅助 / 保守保留                [T03]
                 ↓
影调色彩：目标定义 → 参数化或直接图像渲染                  [T02]
                 ↓
输出 → 质量、事实保持、任务目标与成本的独立评价             [T04]

决策层 [T06]：选择动作、安排证据、决定重试/回滚/停止；
             控制上面的处理环节，不要求它们全部由 Agent 执行。
```

RAW 成像与已有照片编辑的入口不同。只有 RGB 的编辑系统不能假设仍有 RAW、真实曝光元数据或丢失的高光观测。

### 离线训练与数据闭环

```text
真实配对 / 物理合成 / 生成退化 / 生成目标 / 偏好反馈        [T05]
                           ↓
来源可信度、配对关系、分布覆盖与标签校准                   [T04/T05]
                           ↓
训练 / 蒸馏 / 偏好优化                                    [X01]
                           ↓
独立真实测试与失败分析 → 决定补哪些数据、修改哪些机制
```

离线数据生成器、在线执行器、评价器和训练期教师可以是不同模型。把几篇论文放在不同模块里，不等于已经证明它们能直接拼成有效系统；未验证接口必须标明。

## 长期主题

| ID | 长期问题，而不是方法名称 | 要持续区分的竞争路线 | 快速回忆句 |
|---|---|---|---|
| T01 采集与成像物理 | 什么信息应在采集时保住，哪些损失无法靠渲染补回？ | 固定/自适应采集；单帧/多帧；人眼渲染与机器任务；独立与后端条件化控制 | 先问测到了什么，再问能把图调成什么 |
| T02 影调、颜色、意图与参考 | 这张照片应该怎样呈现，目标如何变成可执行控制？ | 显式曲线/LUT/局部算子；神经映射；生成式编辑；全局/语义局部；群体/个人偏好 | 目标定义、表达能力和执行正确性是三件事 |
| T03 可信恢复、生成式 SR 与高分辨率 | 哪些细节由观测支持，哪些只是合理补全？ | 确定性恢复；后验生成；外部参考；局部选择与拒绝；原生高分辨率/分块/参考传播 | 清晰、自然、真实不是同一个轴 |
| T04 IQA、Reward 与偏好决策 | 分数测量了什么，能否选对当前候选，并承受被优化？ | 全参考/无参考；全局/局部；标量/多维；rubric/工具证据；静态/在线评价 | 会打分，不等于会选优，更不等于适合当训练奖励 |
| T05 数据与 Pseudo-GT | 监督从哪里来，哪部分可信，如何覆盖真实退化和目标？ | 真实配对；物理正向合成；生成退化输入；生成增强目标；区域可信监督 | 目标真实性、退化真实性、配对一致性分别审查 |
| T06 Agent、动作与闭环控制 | 在既定执行器下，如何找到有效动作并控制失败与成本？ | 固定链；单步直接模型；等预算候选选择；自适应工具；原图重试/就地编辑；学习动作后果 | 执行器能做到、搜索找得到、评价选得对须分开 |
| X01 效率与训练部署（横向层） | 哪些能力在训练期获取，哪些计算必须在部署期保留？ | 蒸馏/量化；低分辨率控制+高分辨率执行；少步/多阶段；缓存；端云分工 | 训练成本、模型时延、完整产品成本分别算 |

### 2026-11-05 缺口补查：三个受影响的系统决策

**T01/T02/T05：低光亮度与颜色不应默认串行独立**。补入 [CHROMA-MILL](papers/arxiv-2611.04092.md)、[3L-D](papers/arxiv-2611.02695.md)、[Beyond CCT](papers/arxiv-2610.40175.md)；照度、illumination SPD/chromaticity、AWB gain、CCM 和 Tone Mapping 是不同变量。新增的受控 RAW 与多通道环境光证据支持联合评价，但真实非均匀多光源和手机部署仍待证。详见 [联合恢复专题](surveys/low-light-raw-awb-illumination.md)。

**T04：先验证 GT 和评价器是否测对目标**。补入 [LOL benchmark 审计](papers/arxiv-2610.38121.md)、[CIE color judgment](papers/arxiv-2610.40212.md)、[NightIQA](papers/arxiv-2611.04811.md)。旧认识是 PSNR 与 VLM 可作为有效信号；本轮修正为必须分别检验 GT 风格漂移、评价器物理色差误差，以及夜景失真识别能否转化为候选偏好选择。见 [评价可信度专题](surveys/low-light-iqa-and-gt-validity.md)。

**T05/T03/X01：无 clean GT 与真实代价不能只靠主观样图判断**。[Learning Clean Generative Processes](papers/arxiv-2610.42036.md) 将 noisy-only generative learning 扩展到非高斯测量过程（满足 noise law/独立性条件）；[Mobile AI 2026 Learned ISP](papers/arxiv-2611.05008.md) 提供移动 GPU 真实运行对照；[HIVE-Diff](papers/arxiv-2611.03465.md) 用单张 LDR+events 扩展 N 帧 HDR，但非实时和饱和静态区域观测仍受限。见 [无 GT 理论](surveys/noisy-measurements-to-clean-generators.md) 与 [真机/Event-HDR](surveys/mobile-isp-and-event-hdr-efficiency.md)。

上述均为停用窗口历史补查，不把 2026-10-30 已归档的八篇重复计为新发现。此次不宣称所有 arXiv 日列表已穷尽。

### 2026-11-07｜T01/T03：传感补充测量和生成先验，贡献不得混算

**旧路线**：单RAW/多曝光帧融合、event+一帧锚点HDR（HIVE-Diff）、同步RGB/NIR辅助恢复（UGD-FM）。**新证据**：[CoGenRec](papers/arxiv-2611.07665.md) 把CVS长曝光RGB+短曝光高速稀疏差分融合为去模糊/插帧/HDR序列，采用多尺度测量约束+video diffusion+细节VAE；作者有真实CVS样例和同测量基线，但约1M训练clips、曝光增强和额外硬件都是强替代解释。**变化 Bridge / Engineering maturity**，这并非先验凭空创造HDR事实。**判断**：观测信息的增益与生成重建改进单独分摊，不变的是单手机RGB/TM无CVS不能继承此结果。在线CVS观测→传感约束→diffusion→RGB；离线仿真+真实配对→分阶段训练；Agent不是必需。详见[多模态sensor与Event-HDR survey](surveys/mobile-isp-and-event-hdr-efficiency.md)。

### 2026-11-10｜三个长期问题的增量：测量先验、控制型编辑、评价执行分离

**T03 / T01，已知物理观测与生成先验**。此前 BAM/Dual Flow 是已知算子的生成式路线，DAPS/SITCOM 等分层反演还存在优化目标与先验分布的张力。新 [FANO](papers/arxiv-2611.08923.md)（PROBE，Boundary refinement）解释 SITCOM 的 late-layer radial drift：residual 持续降低而 PSNR 变坏，锚定前向噪声 e 而不是任意 x_t；FFHQ 模拟 HDR PSNR 28.13→29.88 dB，e-search 是主要贡献、radius 在 HDR 上有净效益。**未变**：已知 A/高斯模拟、约1500次需反传 denoiser 不等于已解决真实手机 HDR 或部署。新增[完整反演路线图](surveys/measurement-consistent-generative-inverse-problems.md)，离线需物理算子/噪声/GT，在线已知 y、A→分层约束搜索→x，Agent 非必需。

**T02 / T05 / X01，执行器内部的源图锁定有两条并行途径**。[Paste2Place](papers/arxiv-2611.09387.md)（GO-E，Bridge / Engineering maturity）以固定位置的拼接物体+mask 为输入，离线对齐 Blender 物理成像三态训练前景光照和背景影响，在线 1-step source-anchored bridge；作者消融 bridge-only PSNR 29.68→加物理引导30.83，不能把全收益算成物理分解。[AR-Edit](papers/arxiv-2611.09795.md)（GO-E，New route）在已蒸馏 causal video 模型用 t=0 V-cache 实施免反演串流编辑；Reward Forcing 同 4步对照6 NFE/10.5FPS，运行于 H100。它们分别控制**空间物理目标**和**attention/时间流的源保持**，不是一条直接继承路径，均无手机 RAW 色彩证明。见[合成专题](surveys/object-scene-composition-and-relighting.md)和[免反演编辑](surveys/one-step-inversion-free-editing.md)。

**T04 / T03 / T06，先识别失真≠具备恢复动作**。[水下 UAV 五模型 zero-shot benchmark](papers/arxiv-2611.09740.md)（GO-E，Counter-evidence）报告诊断性能与直接 restoration 之间明显落差：最佳 balanced acc 约0.654，但100图直接恢复 PSNR 最高只增0.255dB、pool LPIPS 没有改善，还会幻觉内容。它与[选择性恢复](surveys/selective-task-aware-restoration.md)的 KEEP/RESTORE 失败证据互补但不是直接方法继承。**未变**：评估、执行器候选可达性和 selector 需要三项独立证据；特殊水下域不代表全部真实照片恢复失败。

**行动**：上述结果暂无需扩张当前 Tone Mapping / AWB / RAW 恢复执行链；优先复用强简单对照，只有出现对应真实失败条件再安排最小判别实验。所有技术指标均为作者报告，并非独立复现。

### T01｜采集与成像物理

系统位置：进入恢复之前的观测生成与控制。保留曝光时间、模拟增益、数字增益、帧数与渲染亮度的区别。

已有入口：[RIECR](papers/arxiv-2610.28191.md)、[RawVLA](papers/arxiv-2609.37530.md)、[Neural Block-wise AE](papers/arxiv-2610.18733.md)、[HDR 专题](HDR/)。这些是已有卡片导航，不表示本次重审了各篇方法。

需要维护的争议：联合采集–渲染的收益来自更好采集、目标外观变化、额外预算，还是耦合机制本身？何时一条共享渲染流足够，何时需要任务专用表示？

方案回忆：输入观测/元数据 → 候选采集配置 → 固定或条件化后端 → 同目标外观评价。没有同预算、同目标的对照，不能归因为联合控制。

**2026-11-12 T01/T03 backfill：** [RetinexGS](papers/arxiv-2611.13280.md) 将 DNG noise metadata、Retinex appearance factorization 和 depth-guided initialization 接入低照 RAW 3DGS。它属于多视图 scene reconstruction，不是单帧 ISP；与 RawNeRF/LE3D 竞争，证据目前只有 5 个场景。详见 [Low-Light RAW Neural Rendering survey](surveys/low-light-raw-neural-rendering.md)。

### 2026-11-07｜T02：理解—生成训练与深度先验迁移是两条不同能力路径

**旧路线**：Qwen-Image类通用编辑器+专门空间mask与外部动作系统；多轮编辑保真另有TailSteer/MT Forcing。**新证据**：[WeLM-Image](papers/arxiv-2611.07392.md)（GO-E，Engineering maturity）通过大型MoT–MoE分离理解/生成路径、不同生成/编辑奖励与蒸馏扩展一体执行器；[StitchEdit](papers/arxiv-2611.07922.md)（PROBE，New route/Boundary refinement）用逐层depth/edit梯度兼容性微调深度LoRA，解决特定几何编辑中的遗忘。StitchEdit同depth-init baseline DCS 0.80→0.92，但固定cosine已0.90、目标depth是真实感知模型proxy。

**判断**：模型表示、已有知识迁移和按指令命中区域是不同能力，不能把榜单或3D深度基准迁移成光度区域编辑的证据。**不变**：保持目标区域成功与未编辑区泄漏双独立指标。**系统**：离线大规模多任务数据/奖励训练或深度先验+逐层探针训练；在线源图+指令/参考→编辑器→独立空间保护检验；外部Agent仅负责动作/候选，不被上述研究证明已集成。详见[编辑执行器训练与几何专题](surveys/editor-understanding-and-geometry-training.md)。

### T02｜影调、颜色、意图与参考

系统位置：目标定义与可控渲染。区分摄影修图、恢复和改变内容的创作编辑。

已有入口：[FlowTool](papers/arxiv-2609.35673.md)、[UniSlider](papers/arxiv-2610.06831.md)、[Face Contrast](papers/arxiv-2610.26517.md)、[BluePixel](papers/arxiv-2610.19882.md)。

路线不是线性替代：参数化算子的可控性、神经映射的表达能力、生成式编辑的开放性可以互补，也有不能兼得的边界。参考图可以提供风格目标，但不自动成为当前源图的结构 GT。

需要维护的争议：目标定义不足、算子容量不足、参数预测失误和评价器偏好错误，哪一个限制最终结果？增加分割或 VLM，不自动补足其余缺口。

方案回忆：源图+意图/参考 → 目标描述 → 全局/区域控制量 → renderer → 未编辑区域与期望改变的分别验收。

**2026-10-24 增量（T02）**：[ECT](papers/arxiv-2610.30827.md) 用单时刻 angular transport + endpoint calibration 把 ChordEdit 的多时刻估计改成一次 temporal support；范围仅 ε-prediction VP 一步编辑，非任意 Qwen/FLUX。与 ER-Chord 的空间能量重新分配是**不同优化轴**，没有互相取代的实测证据。详见 [一步免反演编辑 survey](surveys/one-step-inversion-free-editing.md)。**保留判断**：指令完成度与未编辑区保真需要独立衡量。

**2026-11-11 光照可控性分支**：[DynOLAT](papers/arxiv-2611.11210.md) 不直接由单个目标环境图生成整段人像视频，而是在 LightStage 动态 OLAT paired data 上训练同一视频多入射方向的响应基，再按目标 HDR 环境图在线**线性光域重组**；与 [Lux Post Facto](https://openaccess.thecvf.com/) / HumanOLAT / UniRelight 属于相邻/竞争的动态重照明路线，与 [Paste2Place](papers/arxiv-2611.09387.md) 只有 source-anchored bridge 的共同抽象，**非经证实直接继承**。**旧→新**：只比较新光照外观是否合理→增加控制方向/相对强度的可测接口。**不变**：准确光谱、局部曝光量、实时手机部署尚未验证；101 基、57帧1088p在 8×A100 下生成约26.89分钟，不能等同实时编辑。路线、采集和对照：[动态人像 OLAT relighting 专题](surveys/lighting-conditioned-portrait-video-relighting.md)。

**2026-11-12 T02 增量：** [Dark Matters](papers/arxiv-2611.13504.md) 把 HDR 视频生成的表示接口前移到 frozen VAE 之前，使用 exposure-equivariant EquivFlow 保留 deep-dark chroma。与 LumiVid 的 LogC3、DiffHDR 的 Log-Gamma 是竞争表示路线；尚不能据此改写确定性 TM。详见 [VAE-Aware HDR Representation survey](surveys/vae-aware-hdr-representation.md)。


**2026-11-14｜T02/T03 三个不同控制对象（2 New + 1 substantive Update）：**
- **目标控制**：[ATune](papers/arxiv-2611.16236.md)（11-12 v1，GO-E）由10M优质图的自退化监督学习13维全局摄影目标，并通过RawTherapee/darktable数值搜索实现。与 [PREEN](papers/arxiv-2610.36896.md) 的「参考B→预设」是互补目标，不是已确认直接继承。旧“参数化可控但需专家配对”→新“可无专家配对训练目标且可更换编辑器”，但无法区域独立，median42s且没有手机E2E。见 [摄影属性目标survey](surveys/photo-attribute-targets-and-editor-control.md)。
- **观测不确定性控制**：[Blind Video ITM](papers/arxiv-2611.15146.md)（11-11 v1，GO）通过五种TMO训练边缘化和clip-gated非对称潜空间亮度监督，缓解未知TMO造成的有符号亮度偏差；不替代 [Dark Matters](papers/arxiv-2611.13504.md) 的VAE前色度编码。旧“编解码/生成prior主要约束”→新“未知TMO和clip位置本身必须作为可辨识性问题”；仍无法恢复丢失的唯一辐射，族外Severe可能失效。见 [盲逆影调survey](surveys/blind-video-inverse-tone-mapping.md)。
- **空间修改控制**：[FreeDeshadow](papers/arxiv-2611.14608.md)（2026-11-10 v1，2025 [PACSRNet](https://arxiv.org/abs/2501.15043)的**实质扩展**，GO-E/Update），新增文本object指定与1024² PCSRD+，分离投影定位与非目标保留。此任务**2025已有**、不是2026首创；它与 [Paste2Place](papers/arxiv-2611.09387.md) 的增加投影是互补逆任务。见 [物体场景光影survey](surveys/object-scene-composition-and-relighting.md)。

**系统边界（推断组合，非论文已验证系统）**：离线优质图自退化、HDR/TMO合成、object-shadow prompt数据为三类不同监督；在线依次区分目标属性预测/未知算子下HDR估计/对象阴影局部移除；T06可选择动作与验收，但三篇均未证明端到端Agent路由或手机部署。**不变**：可达性、可发现性、可选择性分测，物理真值/人评/空间保持独立。

### 2026-11-06｜T01/T03：在输入侧补充真实观测，而非让恢复器猜得更好

**旧路线**：单 RGB 去噪、对齐 NIR/RGB 引导和光源/RAW 条件化恢复。**新证据** [UGD-FM](papers/arxiv-2611.06422.md) 在 noisy RGB+unaligned NIR 上融合跨谱 sparse matching 与 1–2 step flow；在 FANVID 作者消融中 sparse window→adaptive propagation，2-step 30.03→30.58 dB；但 3D 遮挡与额外 sensor 是未解约束。**地图变化 Bridge / Engineering maturity**：新增可用**物理第二观测**的跨谱引导路线，与 [CHROMA-MILL](papers/arxiv-2611.04092.md) 的曝光/颜色训练监督是互补而非继承。**不变**：恢复方法不能创造未测到的真实光线信息，也不能跳过相机双路同步/端到端成本。详见 [非配准导引恢复 survey](surveys/unaligned-guided-restoration.md)。

### 2026-11-07｜T03/X01：恢复专家并不一定要用MoE路由才能统一

**旧路线**：独立任务专家、统一多任务backbone、UniRestorer++的退化层级MoE。**新证据**：[OptIMerge](papers/arxiv-2611.07543.md)（Google，GO-E，New route/Boundary refinement）把相同基础U-Net上独立微调的恢复专家，经小规模校准优化attention+convolution空间对齐合并成一份多任务checkpoint；不是免训练的均值，也不是在线按输入选择专家。作者OID+DPDD任务上优于简单均值/部分joint对照，但DPDD LPIPS较独立专家更差，DPDD+SR上SR PSNR未赢joint。

**判断**：把“训练期共享”“在线专家路由”“后验权重合并”列为三种竞争路线；同样需要共享底座及跨相机迁移检验。**不变**：不能把低秩融合训练费用或32 DDIM steps当作手机端低成本。**系统**：离线各任务专家→冻结→联合校准权重→单合并checkpoint；在线LQ→合并扩散恢复器→RGB；无额外Agent，仍需外部GT fidelity与成本。见[统一恢复survey](surveys/universal-restoration-degradation-routing.md)。

### T03｜可信恢复、生成式 SR 与高分辨率

系统位置：保留/重建观测信息，并界定可接受的生成自由度。

已有入口：[BAM](papers/arxiv-2609.39660.md)、[WorldSR](papers/arxiv-2610.28423.md)、[RelayVSR](papers/arxiv-2609.37850.md)、[VHA](papers/arxiv-2610.25770.md)。

新结果需定位到具体轴：输入是否有 GT/RAW/多帧/外部参考；生成先验在训练还是推理；高分辨率是原生处理、分块还是低分辨率生成后上采样；保持结构、文字、身份与颜色用了什么独立证据。

需要维护的争议：输出看似真实是否属于当前输入？外部参考减少内部幻觉时，是否引入参考迁移错误？方法复杂度下降是否兑现为端到端成本下降？

方案回忆：可靠观测 → 恢复/融合 → 仅在授权范围引入先验 → 独立事实保持与感知评价。该分解是分析坐标，不是假设必须实施每个模块。

**2026-10-24 增量（T03/X01）**：[GLOW-FM](papers/arxiv-2610.31222.md) 把已有 Terminal Velocity Matching 迁移到 Tiny-VAE 潜空间低光增强，1 NFE 的结果在部分真实配对数据有竞争力；但 UHD-LOL4K 和 LOL-v1 PSNR 并非最佳，跨域 NR-IQA 也不证明文字/身份/原生高分辨率保真。详见 [高效生成式恢复 survey](surveys/efficient-generative-restoration.md)。**不变**：需要同时报告可观察结构、生成自由度与端到端设备代价。

**2026-11-06 增量（T03/T05/X01）**：并列两类**不同问题**。其一，[UniRestorer++](papers/arxiv-2611.06042.md) 明确接续 ICLR 2026 UniRestorer 的粗细层次路由，本次主要新增可扩 LoRA 层级、区域 dense routing 和 CDD-50 五重组合退化；作者报告七任务均值 31.81→32.24 dB，但 2.9B 不等于移动部署，SIDD 仍有专项模型优势。地图变化 Engineering maturity/Boundary refinement，综述见 [退化专家扩容](surveys/universal-restoration-degradation-routing.md)。其二，[Dual Flow](papers/arxiv-2611.05843.md) 在**已知线性 A/高斯**条件下让 image/measurement joint flow 末态满足 y_hat=A x_hat；这是与 [BAM](papers/arxiv-2609.39660.md) 的物理条件生成路线不同的求解机制，New route/Bridge，详见 [高效生成式恢复 survey 的并行 inverse 分支](surveys/efficient-generative-restoration.md)。**判断更新**：恢复能力的规模收益、退化识别置信度、已知测量约束是三个分离控制轴。**不变**：真实 GT fidelity、端到端设备成本、专项简单 baseline 必须独立对照。

**2026-11-11 暗光 SR 可控恢复分支**：[DeLang-SR](papers/arxiv-2611.10485.md) 将 LQ 推导的退化意图/视觉 token 对应生成 velocity **direction**，将区域可靠性对应 step-size **magnitude**，在 SD3 先验上实现一网络 update。它承接 DaLPSR/S3Diff 的任务抽象，新增的是方向与局部剂量的显式分工而非首次使用语言。作者 RELLISUR x2 PSNR23.865dB；同 5K steps base→full 21.358→22.986dB，但没有纯数值描述对语言的足额反证，完整模型 20,390.77 GFLOPs、0.448s/图。**旧→新**：从只压 NFE，加入局部修复风险与语义方向的独立条件；**不变**：可信明区保护、GT 真实性和全链真实成本缺一不可。详见 [高效生成恢复 survey](surveys/efficient-generative-restoration.md)。

**2026-11-12 T03 增量：** [DVFace v2](papers/arxiv-2604.14560.md) 增加 one-step 视频人脸恢复的单卡效率实测；81 帧 512×512 在 A6000 上 15.13 s，约 5.4 FPS，属于工程成熟度而非实时部署。RetinexGS 属 RAW 多视图重建邻接分支；Dark Matters 属 HDR VAE 表示邻接分支。三者不应合并成一个通用恢复器。

### 2026-11-07｜T04：可解释的故障列表是否真的提高候选选优？

**旧路线**：VideoScore/VideoAlign等标量排序、VisionReward等自然语言推理、NightIQA/CheckDistill结构化视觉证据。**新证据**：[ArtiVidRM](papers/arxiv-2611.07301.md)（PROBE，Boundary refinement / Supporting evidence）在视频生成中先列artifact，再用semantic recall/列表长度/偏好同时优化Qwen3-VL。GenAI-Bench的无ties作者准确率0.753，较VisionReward 0.744略高；MonetBench 0.697低于VisionReward 0.721；T2VQA-DB的Hit@1不是最优。

**判断**：结构化缺陷可成为训练奖励的可检查中间表示，但不能从“写得出故障”推断Judge会在真实RAW恢复候选中选得准。**不变**：可达性/发现性/可选性三者分离。**系统**：离线人类偏好+独立伪影标注→SFT+多Reward→独立排名与下游验证；在线视频→故障列表→得分/决策；Agent若用该分数进行重试，属于未验证接口。详见[artifact-rubric survey](surveys/artifact-grounded-reward-and-verification.md)。

### 2026-11-09｜T04/T02 历史回填：个体审美与同场景渲染选择不是同一个评价目标

**旧路线**：统一 MOS/NR-IQA、场景条件化 IQA（ScenePercept）、结构化缺陷评价；个人化美学已有 [PARA (CVPR 2022)](https://arxiv.org/abs/2203.16754) 的用户属性/评分监督与其他个体探针方法。**历史补录**：[Undertone-P](papers/arxiv-2609.27110.md) 最早 v1 2026-09-22 研究 rubric judge panel；2026-11-05 的 v2 实质重写为 frozen VLM 特征 + 非测试用户权重协方差先验 + 新用户少量评分的贝叶斯线性回归。这是一次实质的**同 ID 版本转向**，但 v2 在上轮成功覆盖的 11-06 日列表内，本轮只记 `backfill`，不触发新作通知。

**证据/替代解释**：Ryu–Yanaka PARA 同一 200 人协议，作者报告群体先验 ρ=.640，10 条个人评分 .648，100 条 .676；首 10 条评分增量只有 +.008，不能把跨论文击败弱冷启动基线完全解释为「只用十个评分学会个人口味」，人群其他评分者标签和多 VLM 特征是重要优势。与 [DEAR](https://arxiv.org/abs/2512.05209) 的同一 RAW 五种修图渲染两两偏好是**并行任务**，不是同一 GT；两者不可直接比较准确率。

**判断变化（New route / Boundary refinement）**：从「更好群体美学分数」细分为 crowd MOS / 单图个人美学 / 同场景编辑候选偏好。**不变**：物理色差、结构事实、编辑任务完成必须单独验收；Judge 的准确分数不自动意味着用户候选池可选择性提高。**离线**：冻结特征 + 非测试用户群监督 → 人群先验 → 独立同场景渲染偏好采集；**在线**：个人 K 条评分 → 后验权重 → 候选排序/保留原图；Agent 只调用评价接口，非已经验证的联合修图框架。详见[个人偏好与渲染评价 living survey](surveys/personalized-aesthetic-preference-and-rendering.md)。

### T04｜IQA、Reward 与偏好决策

系统位置：候选测量、选择、验收和训练反馈。必须分别说明这些角色，不能因同用 IQA 名称就合并。

已有入口：[VHA](papers/arxiv-2610.25770.md)、[EditJudgeBias](papers/arxiv-2610.01670.md)、[CheckDistill](papers/arxiv-2610.26740.md)、[Multidimensional Observer Model](papers/arxiv-2609.38487.md)。

需要维护的轴：感知质量、事实保持、指令执行、个人偏好、任务效用、排序稳定性。最终决策可以是选优、接受、拒绝或保持当前结果，不要求所有轴可相互补偿。

当前连接示例：VHA 既有卡片把它定位为 GT 支持的事实差异评价，而不是无参考部署检测器。它扩展评价轴，不替代所有感知评分器。[S3]

方案回忆：先定义该评什么 → 取得可用证据 → 校准评分/排序 → 检查稳定性 → 根据场景约束做决定 → 独立审核被优化后的结果。

**2026-11-12 T04 增量：** [LucidNFT v4](papers/arxiv-2603.05947.md) 增加 40 个 LR 输入、5 位专家、200 次 binary judgments 的 reward-independent human study（72.5% vs 27.5%，不允许 tie，Fleiss’ κ=0.415）。它是离线 RL reward 证据，不是在线 Agent judge；详细路线见 [LR-Anchored Real-ISR Preference Optimization](surveys/lr-anchored-real-isr-preference-optimization.md)。

**2026-11-13 T04 历史地图接入补齐（backfill，非新通知）：** [EditJudge-Bench](papers/arxiv-2611.12524.md)（2026-11-09 首次 arXiv 公开，11-13 周报已覆盖）以 1,382 组已知 Blender 操作真值审计 25 个 judge 配置；作者报告 VIEScore+GPT-4o 的 correctness AUROC 69.0%，图文顺序可令 AUROC 变化最多 14.1 个百分点。与 [EditJudgeBias](papers/arxiv-2610.01670.md)（顺序/线索偏差）、[CheckDistill](papers/arxiv-2610.26740.md)（checklist 蒸馏）和 ArtiVidRM（视频伪影 reward）属于相互补充的评价问题，**不是已核实的直接继承链**。**旧判断→新判断：** 先检验评委是否看到了可证伪的编辑操作，再问它能否按人类偏好选图；binary correctness 不等于真实风格保真，评价器改善不提高 executor 可达性。[T04 canonical survey](surveys/artifact-grounded-reward-and-verification.md) 已接入，原 T02 编辑器训练 survey 仅保留交叉索引。

### T05｜数据与 Pseudo-GT

系统位置：离线监督构造。至少分成四条并列路线：

```text
真实采集：                 measured LQ  ↔ measured/validated HQ
物理正向合成：             known HQ → physical degradation → synthetic LQ
学习型退化合成：           curated HQ → learned degradation → synthetic LQ
增强目标生成：             real LQ → editor/restorer → pseudo HQ
```

已有入口：[MESS](papers/arxiv-2610.24680.md)、[Dense Illuminant](papers/arxiv-2610.06508.md)、[OLiVES](papers/arxiv-2610.20501.md)。

当前连接示例：MESS 属于“生成退化输入、保留原始 RGB 目标”的路线。它与“保留真实 LQ、生成目标”的路线互补，而不是后者的天然升级。v0.1 依据已归档机制定位；v0.2 已重新核对原文方法与选定实验，详见专题核验记录。[S1]

需要维护的争议：同规模下收益来自退化建模、目标质量还是场景覆盖？合成输出更像照片，不等于成像信息损失更准确。生成目标更漂亮，不等于结构真实。

方案回忆：确定 target 来源 → 选择退化/目标生产方式 → 检查配对与区域可靠性 → 训练同一 student → 在独立真实数据上验收。

**2026-11-12 T05 更新：** [UWNature v2](papers/arxiv-2511.14521.md) 在 v1 已有的两个 10K-pair 数据集、6 个架构和 3 个测试集基础上，增加更深入的 appearance/structure/depth reliability、人类感知、degradation–restoration reciprocity 与 real-world validation，并明确指出更高 spatial plausibility 不必然改善 restoration performance。该版本是 2025-11-18 首发论文的实质更新，不作为新论文计数；source-preserving pseudo-pair 仍是有效路线，但需同时测 intrinsic realism 与 downstream utility。

专题深化：[成像训练数据合成 survey](surveys/imaging-training-data-synthesis.md)。覆盖逆 ISP、RAW/XYZ 生成和曝光监督的历史路线；MESS 与 RawGen 是综合建立的并行关联，不是已核实的直接继承。阅读时同时区分 UNICE 的融合目标与 MESS 保留原始 RGB 目标。

### T06｜Agent、动作与闭环控制

系统位置：控制器，组织已有能力；不是默认替代恢复网络本身。

已有入口：[HarnessIR](papers/arxiv-2610.10133.md)、[PreActIR](papers/arxiv-2610.20384.md)、[FlowTool](papers/arxiv-2609.35673.md)、[AgenticIR 专题](AgenticIR/)。

当前连接示例：HarnessIR 的既有卡片记录了证据工具与 MFM 执行器的角色分离，以及验证失败后从原图重新尝试；这影响执行器接口和状态更新方式，不能直接证明换成任意弱执行器也有效。[S2]

需要维护的三种瓶颈：候选可达性（执行器有没有好结果）、可发现性（搜索能否找到）、可选择性（评价能否识别）。三者中的哪一个受限，需要实验区分，不能看到新 verifier 就认定评价器是瓶颈。

方案回忆：原始输入+目标 → 状态诊断 → 有界动作/候选 → 执行 → 独立验收 → 接受/回滚/从原图重试/停止。必须保留强单步与等预算 best-of-K 对照。

**2026-10-24 增量（T06 / T03 / T04）**：[Gate3DGen](papers/arxiv-2610.31649.md) 在图像到 3D 任务中引入整图 KEEP/PURIFY 路由与下游几何目标；合成 benchmark 净化显著有效，但真实照片 proxy 路由 accuracy 与 Always-PURIFY 同为 58.33%。应将**净化器收益**、**路由收益**和**任务指标真实性**独立验证。关联 [选择性恢复与任务效用 survey](surveys/selective-task-aware-restoration.md)。**不变**：非 GT 可观察输入不能被 VLM 评价变成真实 GT。

**2026-11-08 历史 backfill（T06/T04/X01，不触发新作通知）**：[Adaptive Low-Light Enhancement for Road Anomaly Detection](papers/arxiv-2611.08393.md) 首发为 **2026-11-05 v1**，属于 11-07 已成功检查过的 arXiv 日列表窗口。它在合成低光道路检测中展示 uniform SCI 可损害 mAP，而亮度三分支有时部分恢复 dusk；但 YOLOv8n 严重低光 mAP always-KEEP 0.268 > router 0.218，且 router 切换 SCI 强度的贡献未单独隔离。**地图变化 Supporting evidence / Boundary refinement**：对前述 [Gate3DGen](papers/arxiv-2610.31649.md) 真实域路由未胜过 trivial baseline 的判断，新增不同任务负例。两个论文属于分析者归纳的共同机制而非经核验的直接继承。**不变**：必须同时比较 always-KEEP/always-EXECUTE/route，真实域收益、完整设备成本和模型兼容性未被证明；单路手机 ISP/TM 不改。系统位置：在线图像→亮度或其他任务证据→KEEP/选择增强强度→下游 detector；离线数据/检测监督与路由校准独立核验，本文无 Agent。详见 [选择性恢复与任务效用专题](surveys/selective-task-aware-restoration.md)。

**2026-11-06 增量（T06/T02）**：[TailSteer](papers/arxiv-2611.06741.md) 在多轮编辑器训练期，以原图保护区构造自监督 endpoint，并让 early trajectory 学 base、late trajectory 学 preservation。与 [MT Forcing](papers/arxiv-2610.25404.md) 的跨回合 rollout distillation 属竞争/互补机制（分析者综合，非断言直接继承），与推理时原图回退/ROI compositor 也是不同选项。作者的十轮保真优势伴随某些 Qwen/FLUX 单轮编辑准确率下降，不能称无损。**地图变化 New route/Boundary refinement**：将“多轮执行器本身的保真能力”从 Agent 的可发现性、可选择性明确分开；单轮目标区域操作失败不能由此文直接解决。综述见 [多轮编辑保真](surveys/multi-turn-editing-preservation.md)。

**2026-11-11 同执行器轨迹内闭环选择**：[V2C-Edit](papers/arxiv-2611.10066.md) 基于 FlowEdit 的 coupled/decoupled 等多 velocity 备选，逐时刻使用 VLM Instruction-Level Similarity 选择和可选 mask；改变的是**可发现性**，不是训练新 executor 或完全解决 Judge **可选择性**。同骨干消融 IA 5.69→6.07、保护区 PSNR 17.78→17.44；高预算 brute-force IA6.22但更破坏背景；H100 26.44s/图远慢于固定 FlowEdit 4.00s。**地图变化 Bridge/Boundary refinement**：Agent 思路能下沉到模型生成轨迹，且闭环成本/偏差必须评价。**不变**：可达/可发现/可选及 ROI 真实保持独立，现有确定性局部 photofinishing 不是直接被替代。详见 [免反演编辑竞争路线](surveys/one-step-inversion-free-editing.md)。

### X01｜效率与训练部署

它是贯穿六个主题的比较维度，不再把每个高效模块当成新的孤立研究方向。

已有入口：[RelayVSR](papers/arxiv-2609.37850.md)、[LoopMoEVR](papers/arxiv-2610.05109.md)、[BluePixel](papers/arxiv-2610.19882.md)。

**2026-11-12 X01 增量：** RetinexGS 报告 RTX 4090 91–145 FPS novel-view rendering，但训练迭代与 baseline 不同；DVFace v2 报告约 5.4 FPS 的 81-frame batch，不是实时视频。训练成本、模型推理时延和完整端到端吞吐继续分开记录。

**2026-11-13 X01 历史地图接入补齐（backfill，非新通知）：** [Edge NPU Benchmark](papers/arxiv-2611.13563.md)（2026-11-10 arXiv 首发、11-13 周报已覆盖）将共同 host I/O 下的 VG-NPU 模型转换与 vendor-native VG-E2E 整链部署分成不同的实验合同。作者在四款边缘 NPU×三任务中报告 VG-E2E 较 VG-NPU 再降低 10.4%–70.7% system latency，只有 4/12 组相对 baseline 提高精度。与 [Mobile AI 2026 Learned Smartphone ISP](papers/arxiv-2611.05008.md) 是**不同任务/平台下的工程测量互补**，不能拿来证明手机 RAW→RGB 性能。**旧→新：**“MAC/NFE/模型调用≠产品完整成本”不变，新增 common-I/O model conversion 与 native E2E 的分层归因要求；功耗、P95、热与相机质量仍待核验。[X01 canonical survey](surveys/mobile-isp-and-event-hdr-efficiency.md) 已接入。

统一记录：训练 GPU-hours/teacher 调用、推理 NFE、总时延、显存/内存带宽、设备与分辨率、质量约束、是否含预处理/数据搬运/重试。没有设备实测就不标手机部署成功。

### X01｜多步推理：缓存还是预测？（2026-10-24 历史补录）\n\n[SpecKCast](papers/arxiv-2610.26837.md) 于 2026-10-19 首次公开、2026-10-21 已推荐；本次仅修复未接入知识地图的问题。**旧地图**只把少步蒸馏、缓存等概括为加速路线；**新地图**明确分出 training-free reuse（TeaCache 等）、uniform forecasting（TaylorSeer/Spectrum）与 band-specific schedule-aligned forecasting（SpecKCast）。作者报告最高 6× 但非手机端恢复实测；生成轨迹一致性不等于 GT fidelity。当前项目方案不因该文自动改变。详见 [Diffusion 推理缓存与预测 survey](surveys/diffusion-inference-caching-forecasting.md)。\n\n## 三个连接示例

以下是已有论文的地图组织示例，不是新发现。v0.2 重核了 MESS 的方法与选定证据；VHA、HarnessIR 沿用既有卡片的核验范围。

| 论文 | 应放的位置 | 与已有路线的关系 | 改变哪项认识 | 不改变什么 |
|---|---|---|---|---|
| MESS [S1] | T05 数据生产；桥接 T01 曝光与 ISP | 与生成增强目标互补；将生成模型用于退化输入构造 | PGT 设计要分别选择输入来源和目标来源 | 生成曝光 RGB 不自动成为真实 RAW/CRF 测量 |
| VHA [S3] | T04 事实保持评价；桥接 T03 生成式 SR | 与感知质量分数互补 | 应单列内容遗漏与无依据新增的评价需求 | 有 GT 评价能力不等于真实无 GT 场景可部署 |
| HarnessIR [S2] | T06 执行器接口与状态更新 | 与串联专用工具竞争；与独立验证互补 | Agent 的改进可能在执行单元/重试策略，而非更长规划 | 好候选能否产生仍受执行器能力限制 |

三个模块可以形成一个**待验证**的系统草图：离线数据生产 → 训练执行器 → 在线候选与重试 → 独立评价。它们的输入域、目标和证据条件不同，不能直接声称已经形成可运行组合；尤其 VHA 的 GT 要求限制了其在线使用。

## 主题更新卡

每次以主题而非论文标题开头：

```text
Topic ID / 稳定问题：
之前的路线与判断：
本次新证据：paper ID、版本、章节/表、适用条件
地图变化：新增路线 / 支持已有 / 修正边界 / 反证 / 跨主题连接 / 工程成熟 / 无变化
与 2–3 个锚点的关系：继承、竞争、互补或限制；未证实关系标推断
更新后的判断：
仍未改变的判断：
系统位置：输入 → 控制变量 → 机制 → 输出；训练与推理分开
当前方案：保留 / 替换 / 新增 / 暂不采用；是否有已运行证据
下一决定性实验或待获取证据：
快速回忆：一个机制句、一个关键反例
```

### 2026-11-12｜三个受影响主题的 Topic Update

#### 1. T01/T02/T03：输入表示决定可恢复信息的边界

**旧地图：** RAW 多视图重建已有 RawNeRF、LE3D、From Chaos to Clarity、HDRSplat；HDR 视频生成已有 LumiVid（LogC3）和 DiffHDR（Log-Gamma）。这些是历史锚点，不是本轮新推荐。

**本次变化：**
- [RetinexGS](papers/arxiv-2611.13280.md)：在已有 RAW 3DGS 路线上增加 DNG 噪声元数据加权与 Retinex 外观分解，地图变化为 Engineering maturity / Boundary refinement。
- [Dark Matters](papers/arxiv-2611.13504.md)：提出 exposure-equivariant、scale-independent chroma 的 VAE 前编码，地图变化为 New route。

两篇只共享“输入表示决定可恢复信息”这一抽象机制；不是直接继承，也不是同一系统。

**判断更新：** 过去把 RAW/HDR 表示主要看作输入预处理；现在应把它视为模型内部可恢复信息的关键接口。保持不变的是：RetinexGS 只证明小规模多视图 RAW 场景，Dark Matters 只证明特定冻结 VAE/视频扩散设置，均不等于移动 ISP 已可部署。

**系统方案：**
- RAW 3DGS：多视图 RAW + DNG metadata → 几何/深度初始化 → Retinex 颜色分解与噪声加权优化 → novel-view rendering。
- HDR video diffusion：SDR → scene-linear proxy → LogC3/Log-Gamma/EquivFlow → frozen VAE → video diffusion → HDR video。
- 两条路线均无 Agent 控制层。

**行动：** 保留两条研究分支，不改动现有确定性 ISP/TM 方案。若验证 HDR 表示，先做同输入合同、同 backbone 的三编码 matched comparison；若验证 RAW 噪声先验，固定 3DGS appearance capacity 后只切换噪声权重。

**记忆锚点：** 线性 RAW 的多视图噪声平均，与 VAE 前的 HDR 色度传输，是两个不同层级的表示问题。

#### 2. T03/T04/X01：生成恢复的保真奖励与真实推理成本

**旧地图：** DSPO（2025）将人类偏好引入 Real-ISR；DiffusionNFT 提供 policy update；DicFace（2025）使用时序 codebook 处理视频人脸；多步 diffusion 视频恢复强调时序先验但推理成本高。

**本次变化：**
- [LucidNFT v4](papers/arxiv-2603.05947.md) 增加独立 human study，支持 LR-faithfulness reward；地图变化 Supporting evidence / Boundary refinement。
- [DVFace v2](papers/arxiv-2604.14560.md) 增加单卡效率测量与更多对比；地图变化 Engineering maturity。

**判断更新：** LR-faithfulness 已有比 NR-IQA 更直接的训练/人评接口，但 LucidNFT 仍是离线 reward optimization，不是在线 judge；DVFace 的 one-step 有实际速度收益，但约 5.4 FPS 不能称为实时。保持不变的是：候选可达性、可发现性、可选择性仍须分开验证。

**系统方案：**
- LucidNFT 在线：LR → flow-based SR generator → SR；离线：LucidConsistency + LucidLR → 多候选 rollout → per-reward group normalization → DiffusionNFT update。Agent 层为空。
- DVFace 在线：LQ video → spatial/temporal codebooks → asymmetric fusion → one-step Wan2.1 diffusion；离线：codebook、LQ refinement、diffusion adaptation。长视频 chunk boundary 是未验证接口。

**行动：** 将 perceptual quality 与 LR-faithfulness 保持为两个独立目标；视频恢复报告真实吞吐、显存和 chunk 边界质量。不要把两篇工作合并成通用图像 Agent。

**记忆锚点：** Reward model 训练期可用，不代表它已成为可靠的在线候选选择器；one-step 也不等于 real-time。

#### 3. T05：Pseudo-GT 的内在真实性不等于训练效用

**旧地图：** WaterGAN（2017）用 in-air RGB + depth 生成 underwater pseudo-pairs；Sea-Thru（CVPR 2019）用 RGBD/range 与分离的 attenuation/backscatter 模型做物理恢复；UIEB（2019）提供 950 张真实水下图，其中 890 张有 pairwise-consensus reference、60 张没有满意参考；UWNature 则保留 clean source 作为 target 做 unpaired synthesis。

**本次变化：** [UWNature v2](papers/arxiv-2511.14521.md) 对 6 个 restoration architectures、3 个 test sets 增加外观、结构、深度和人类感知分析，指出空间上更合理的合成退化不一定提升下游恢复。地图变化 Counter-evidence / Boundary refinement。

**判断更新：** 不能只根据合成图像是否“像真实水下”选择数据引擎；必须同时评价 source/target 一致性与 student 的 downstream learning utility。保持不变的是：该证据仍限于 underwater domain，不直接外推手机相机。

**系统方案：** clean source + unpaired underwater references → I2I degradation synthesis / depth modulation → source-preserving pseudo-pair → 多个 restoration students → 三个测试集与 human evaluation。Agent 层为空。

**行动：** 将 intrinsic realism 与 downstream utility 分开记录；当前其他数据管线不因这一水下更新自动改变。

**记忆锚点：** 更真实的退化图，不一定产生更好的恢复模型。


## 回忆与维护

专题层按 [survey 索引](surveys/README.md) 维护。先检索两仓库的同问题综述：有则插入，无且存在独立分支才新建；沿引用与机制关系补齐历史工作。总图保留少量锚点，完整 survey 不受锚点数量限制。

每个主题主视图只保留约 3–5 条核心路线和 3–5 篇记忆锚点；完整论文索引留在 registry 与卡片层。路线数量按实际问题复杂度调整，不为凑数创建分支。

每次新证据先用几句话重建旧地图，再高亮变化。每次只展开受影响最大的 1–3 个主题，不把整库重讲一遍。重大突破可以触发主题重写；一般支持证据只增加引用，不改变结论措辞。

完整方案另以一页回忆卡呈现：目标与非目标、输入输出、运行链、训练链、关键约束、已有证据和未验证接口。关联私人项目时应先读取实际计划/实验记录；不要把该信息写入本公共文献地图。

重访一个主题时，可用一个简短问题帮助主动回忆，例如“同样提高 IQA，哪些情况不意味着保真提高？”不因用户看过报告或收藏论文就记为已掌握。

### 2026-11-12 Paper Watch v3.2 source coverage

- arXiv latest available daily listing at scan time: Wednesday 2026-11-11. Checked cs.CV/new, cs.LG/new, cs.AI/new, cs.MM/new, eess.IV/new and eess.SP/new; the 2026-11-12 listing had not yet appeared at scan time.
- alphaXiv followed-researcher roster: 15 researchers queried for recent papers; no additional qualifying paper from the followed roster beyond already covered items.
- Open discovery: alphaXiv discovery plus title/keyword search across HDR/RAW, generative restoration, IQA/reward, preference optimization, benchmarks and efficiency.
- GitHub recovery: Computational-Photograph default branch, archive protocol, Paper Watch v3.2, literature map, legacy record, registry, relevant cards and surveys; CameraPaper README/knowledge indexes and matching title search. No CameraPaper record was changed.
- Current run first-coverage date: 2026-11-12. Version/listing dates and original arXiv v1 dates are stored separately in canonical cards and registry.
- Private project implementation/experiment status was not asserted; this run updated public literature only.

## 变更记录

| 日期 | 类型 | 变化 | 研究结论影响 |
|---|---|---|---|
| 2026-11-14 | 2篇新作 + 1项实质衍生扩展 / T02、T03、T05、T06 | ATune无专家pair全局摄影属性目标；视频Blind ITM联合TMO族与clip非对称监督；FreeDeshadow在2025 PACSRNet基础上扩展文本提示/多样数据并纠正首创归属 | 增目标/算子/空间三控制接口，分别标GO-E/GO/GO-E；传统全局/局部ISP及用户项目状态不自动改变，后者为material Update非新问题 |
| 2026-11-13 | 已归档论文 living survey 接入 / T04、X01 | EditJudge-Bench（Judge事实操作审计）与 Edge NPU Benchmark（统一 I/O→厂商原生 E2E）的既有卡片归位；校正前者的主 survey；不重算论文首发 | 区分指令正确性/偏好、模型调用/E2E。仅 backfill，无新论文通知 |
| 2026-11-11 | 新论文 / T02、T03、T06、X01、T05 | V2C-Edit（逐时刻编辑动作选择）、DeLang-SR（暗光 SR 方向/局部剂量）、DynOLAT（动态人像物理光照响应基） | T06 加强可发现性与评审成本边界；T03 增控制分工但不改变手机计算预算结论；T02 新增可测方向/光强控制路线；均不宣称多论文共识 |
| 2026-11-10 | 新论文 / T02、T03、T04、T05、X01 | FANO、Paste2Place、AR-Edit、水下 UAV 五模型基准（均11-06 arXiv v1、11-09 新公告）归位；新增两专题、修订两专题 | 分离真实测量一致性/优化先验、源图条件化编辑、失真诊断/真实恢复能力；原 ISP/TM 方案保持 |
| 2026-11-09 | 历史实质版本回填 / T04、T02 | Undertone v1（09-22）→ v2（11-05）技术命题改变；补审 PARA、DEAR 与同场景渲染偏好边界；11-06 已覆盖，不作为新通知 | crowd-only 强先验与 K 个用户标签净收益分开；新个人化 survey，但不直接改变 ISP/TM 或 Agent 实验 |
| 2026-11-08 | 历史回填 / T06、T04、X01 | 11-05 v1 的道路低光检测任务路由补归档，新增跨模型/亮度的 always-KEEP 负例与 Jetson 分支代价；非新论文通知 | 加强“能减少 always-on 损害 ≠ 比不增强更好”的边界；保留原有控制与 TM 方案 |
| 2026-11-06 | 新证据 / T01、T03、T06 | UGD-FM、UniRestorer++、Dual Flow、TailSteer 四项 arXiv 11-04 v1，3 个新 survey、1 个旧 survey 增补 | 明确真实新增跨谱观测与恢复先验分开；模型扩容须结合误识别与成本；已知算子联合流是并行解法；多轮保真训练不解决工具规划 |
| 2026-11-05 | 停用缺口补查 / 多主题 | 9 篇首次公开 10-28—11-03 的论文接入四个 living survey；10-30 已归档 8 篇不重复计数 | T04 加强 benchmark/色彩评价审计；T01/T02 补联合低光/AWB 和谱 CCM；T05 补 non-Gaussian noisy-only 生成，X01 补实机 ISP 与 Event-HDR 限制 |
| 2026-10-24 | 历史覆盖纠错 / X01 | SpecKCast 10-21 已推荐但未进入 canonical card/X01 survey；补卡片和路线，纠正误称全局漏检 | 不是新论文通知；X01 分清缓存与预测，恢复迁移仍待实测 |\n| 2026-10-24 | 新证据 / 三主题更新 | 单步生成式 LLIE（TVM）；ε-VP 一步编辑的单时刻控制；任务级净化与真实域路由反例 | T03 增加质量–成本实证；T02 修正“多时刻必要性”；T06 添加 router 必须胜过 Always-PURIFY 的边界，以上均不声称社区共识 |
| 2026-10-23 | 历史回填 / survey 建立 | 新建 T05 成像训练数据合成分支，接入 RawGen、UNICE 和逆 ISP 等前序 | 从单篇 MESS 定位扩展为输入来源、生成域、目标来源与真实验证的路线比较；不将并行工作画为继承 |
| 2026-10-23 | 结构基线 / historical organization | 建立 T01–T06 与 X01，关联已有 canonical cards，加入 MESS/VHA/HarnessIR 三个示例 | 改变组织与回忆方式；不宣称新增论文、独立复现或新共识 |

后续条目必须写旧判断、新证据、新判断及不变部分。误判使用 correction，不删除历史判断；新增支持不等于范式突破。

## 来源与覆盖

- [S1：MESS 卡片](papers/arxiv-2610.24680.md)。v0.2 重新核对方法、附录数据构造与选定实验；历史路线比较见 survey，未独立复现。
- [S2：HarnessIR 既有卡片](papers/arxiv-2610.10133.md)。本次复核档案内容；档案记载过去 selected sections/author repository 核验，v2 差异未完整核实。
- [S3：VHA 既有卡片](papers/arxiv-2610.25770.md)。本次复核档案内容；档案记载过去 full paper/repository 核验，未独立复现。
- [现有主题入口](README.md)、[身份与核验范围](archive/registry.json)、[历史接入边界](archive/LEGACY.md)。
- [归档协议](ARCHIVE_PROTOCOL.md)、[Paper Watch v3 执行规则](archive/PAPER_WATCH_V3.md)。

v0.1 建立时直接访问上述几篇 arXiv 页面未取得内容，当时没有把档案重读升级为新的原文核验。其他已列入口是导航，不代表本次已逐篇复审。未来任何新技术结论、数值、版本变化均需重新核对一手来源。


### v0.2 核验增量

2026-10-23 本轮通过原论文全文文本重新核对 MESS 与 RawGen 的方法及选定证据，并在专题中记录各前序的核验范围。上文 v0.1 的“本次未重审/访问失败”描述保留为当时状态，不代表 v0.2 未取得这些原文；VHA、HarnessIR 等未在本轮重审。完整范围与缺口见 survey 的核验记录。


### 2026-11-14｜Paper Watch 本轮真实覆盖与未核验边界

- 读取默认分支现有protocol/v3.2/registry/legacy/主题入口，核对11-13周报已报道6项不同ID；公开arXiv cs.CV、eess.IV、cs.LG、cs.MM 2026-11-13 new listing，另按标题/机制查同行历史及独立前序，重点复核ATune、Blind ITM、FreeDeshadow的arXiv v1 HTML原文方法、消融及限制；未做独立复现。
- 新的 arXiv v1 首发/首次本库覆盖分别为 ATune 2026-11-12/11-14、Blind ITM 2026-11-11/11-14；FreeDeshadow虽然2026-11-10首次上传expanded稿，但其核心任务在2025-01-25已由PACSRNet公开，本轮仅对文本+局部refiner+PCSRD+的实质变化标Update。
- 同轮以alphaXiv已关注研究者列表为入口核对15位稳定研究者slug近2026-11-04后的文章（Brown、PolyU Lei Zhang、Radu Timofte、Wangmeng Zuo、Tianfan Xue等）；该来源没有引出更高优先级且此前尚未覆盖的相关新作。跨主题alphaXiv发现另外标记ReasonText-SR与HIFC-IQA的最早公开日期待查，不以其arXiv上传自动触发。作者索引不等于独立成功覆盖全部主页/会议。
- 2026-11-13 public listing的当前检索成功范围不等于今天已完成全站OpenReview、所有团队和最新周末公告；11-14的其他新公告、完整作者逐人水位和独立重复训练仍待补；旧11-13覆盖陈述保留为当时情况，不再当当前水位。

### 2026-11-13｜Paper Watch v3.2 本轮检索与覆盖边界

- 官方 arXiv `cs.CV`、`cs.LG`、`cs.AI`、`cs.MM`、`eess.IV`、`eess.SP` 的 `/new` 本轮仍均显示 **2026-11-11（Wednesday）**，与此前已成功覆盖的 public listing 相同；**不将 11-12 listing 冒充已核验，也不以 last_run_time 代替源水位**。
- alphaXiv 15 位已关注研究者名单按研究者独立检索，姓名重合的 PolyU Lei Zhang、Kai Zhang、Xiaowei Zhou 与 Zhilu Zhang 用准确 slug 补查。另对 T01–T06/X01 做开放发现；当前实际覆盖内未核实晚于上次已覆盖 source window 的合格新公开。作者检索及开放检索不代表穷尽所有会议、团队或个人主页。
- 本轮读回 11-13 周报与 registry 100 个身份记录，原文复核 EditJudge-Bench、Edge NPU Benchmark 的选定方法、结果及失败边界，两篇的技术正文已经存在，只补 survey、总图与身份映射。原作者结果没有独立复现。
- **待核验：** 11-12 的新公告页尚未出现在所读官方源中；OpenReview/作者提前公开材料未穷尽；真实手机相机照片的 Judge 跨域审计与移动 ISP 原生 NPU 完整成本尚欠数据。下次应从最后成功 public listing 前至少 7 天重叠检索，未覆盖源不推进水位。

