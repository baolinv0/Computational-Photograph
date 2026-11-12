# Computational-Photograph｜计算摄影研究库

目录：[怎么使用](#怎么使用) · [长期文献地图](#长期文献地图) · [主题入口](#主题入口) · [周报快照](#周报快照) · [归档机制](#归档机制) · [既有资料](#既有资料) · [References](#references)

## 怎么使用

先看每篇卡片的“快速回忆”，再按需展开“精读记录”。**收藏不等于已读，摘要核验不等于全文验证，作者实验不等于独立复现。**论文正文只维护一份；周报记录当时的变化和链接。

本仓库存通用研究技术笔记；厂商归属、产品/专利和竞品证据进入 [CameraPaper](https://github.com/baolinv0/CameraPaper/blob/main/WEEKLY_ARCHIVE.md)。Notion 作为私有阅读入口，alphaXiv 收藏原论文。

## 2026-11-12 Paper Watch：HDR 表示、RAW 重建、Real-ISR Reward 与监督可靠性

- [本轮 Topic Update](Recent_Papers_2026-11-12.md)：2 篇新作 + 3 项实质版本更新。
- [RetinexGS](papers/arxiv-2611.13280.md) · [Dark Matters](papers/arxiv-2611.13504.md)
- [LucidNFT v4](papers/arxiv-2603.05947.md) · [DVFace v2](papers/arxiv-2604.14560.md) · [UWNature v2](papers/arxiv-2511.14521.md)
- 新建：[Low-Light RAW Neural Rendering](surveys/low-light-raw-neural-rendering.md) · [VAE-Aware HDR Representation](surveys/vae-aware-hdr-representation.md) · [LR-Anchored Real-ISR Preference Optimization](surveys/lr-anchored-real-isr-preference-optimization.md)
- 更新：[高效生成式恢复](surveys/efficient-generative-restoration.md) · [IQA/GT 可信度](surveys/low-light-iqa-and-gt-validity.md) · [训练数据合成](surveys/imaging-training-data-synthesis.md)

## 2026-11-11 Paper Watch：生成轨迹的闭环编辑、局部暗光 SR 强度、真实 OLAT 人像重照明

- [三个 Topic Update、三项 2026-11-06—08 新作](Recent_Papers_2026-11-11.md)：2026-11-10 arXiv cs.CV 新公告，早于本轮的 11-10 成功检查尚未覆盖；核心作者 + 全领域开放检索。
- [V2C-Edit：VLM 按时刻决定 flow editing velocity](papers/arxiv-2611.10066.md) · [免反演编辑路线](surveys/one-step-inversion-free-editing.md)；区分编辑可发现性与最终可选择性。
- [DeLang-SR：暗光 SR 的方向与局部步长分离](papers/arxiv-2611.10485.md) · [高效生成恢复路线](surveys/efficient-generative-restoration.md)；强提醒 1 NFE 仍需 20,390.77 GFLOPs。
- [DynOLAT：动态 OLAT 光响应基](papers/arxiv-2611.11210.md) · [新建人像视频重照明专题](surveys/lighting-conditioned-portrait-video-relighting.md)；物理光照方向可控但基视频生成缓慢。

## 2026-11-10 Paper Watch：测量约束、源内容编辑与评价能力边界

- [三个 Topic Update，四项 2026-11-06 v1 新作](Recent_Papers_2026-11-10.md)：进入 11-09 arXiv 新公告；和此前已覆盖论文做身份/结论去重。
- [FANO：已知算子扩散逆问题的前向噪声变量与 radial drift](papers/arxiv-2611.08923.md) · [物理测量一致性专题](surveys/measurement-consistent-generative-inverse-problems.md)。
- [Paste2Place：区域光影与源图桥接](papers/arxiv-2611.09387.md) · [物体—环境合成专题](surveys/object-scene-composition-and-relighting.md)。
- [AR-Edit：因果视频免反演源 V 缓存](papers/arxiv-2611.09795.md) · [一步免反演编辑专题](surveys/one-step-inversion-free-editing.md)。
- [水下 UAV：统一 MLLM 诊断不等于恢复能力](papers/arxiv-2611.09740.md) · [选择性恢复专题](surveys/selective-task-aware-restoration.md)。

## 2026-11-07 Paper Watch 增量

- [本轮三主题增量报告](Recent_Papers_2026-11-07.md)：五篇11-05首发v1，11-06新公告；区分采集观测、恢复模型合并和编辑/评价训练，不重复11-06已推荐研究。
- [CoGenRec：互补视觉传感器与HDR/运动重建](papers/arxiv-2611.07665.md)
- [OptIMerge：扩散恢复专家的后验参数合并](papers/arxiv-2611.07543.md)
- [WeLM-Image：多模态理解与生成训练系统](papers/arxiv-2611.07392.md)
- [StitchEdit：深度先验的逐层兼容迁移](papers/arxiv-2611.07922.md)
- [ArtiVidRM：基于视频伪影证据的Reward](papers/arxiv-2611.07301.md)
- [编辑器理解、几何训练survey](surveys/editor-understanding-and-geometry-training.md) · [伪影Reward survey](surveys/artifact-grounded-reward-and-verification.md)。

## 长期文献地图

- [持续文献总图：问题、竞争路线与系统方案](LITERATURE_MAP.md)：六个稳定主题与横向效率层；先建立问题坐标，再定位新证据。初版为结构基线，不代表所有历史论文已重新核验。
- [Paper Watch v3：主题更新与方案回忆规则](archive/PAPER_WATCH_V3.md)：旧地图 → 新证据 → 判断变化与不变部分 → 系统位置 → 决策。保留原有新颖性审查、去重和无更新静默规则。

地图维护跨论文关系和当前认识；以下主题入口仍导航到唯一技术卡片。已有专门综述不被总图取代，私人项目方案和未公开实验不写入公共地图。

- [2026-11-06 Paper Watch：跨模态真实观测、统一恢复扩容、联合 inverse flow 与多轮保真](Recent_Papers_2026-11-06.md)：4 篇 v1 原文核验，分别标新作/前作/证据边界。
- [非配准跨模态导引恢复专题](surveys/unaligned-guided-restoration.md)：RGB+NIR 真实新增观测、联合去噪与错配负例。
- [统一恢复退化路由专题](surveys/universal-restoration-degradation-routing.md)：ICLR UniRestorer→UniRestorer++ 的扩容与 CDD-50。
- [多轮编辑保真专题](surveys/multi-turn-editing-preservation.md)：MT Forcing、TailSteer、ROI 硬锁与原图重试的竞争关系。
- [2026-10-25—11-05 停用缺口补查快照](Recent_Papers_2026-11-05.md)：9 篇精选论文、截至检查时的去重与完整性边界。
- [低光 RAW、光谱与 AWB 联合恢复](surveys/low-light-raw-awb-illumination.md)：配对照明、RAW 混合、色温与多谱 CCM。
- [低光与颜色评价可信度](surveys/low-light-iqa-and-gt-validity.md)：LOL 数据/脚本审计、CIE 色差、NightIQA。
- [无干净 GT 的生成式恢复](surveys/noisy-measurements-to-clean-generators.md)：非高斯噪声过程与 Consistency。
- [移动 ISP GPU 与 Event-HDR](surveys/mobile-isp-and-event-hdr-efficiency.md)：实机成本和事件帧采集边界。
- [持续专题综述索引](surveys/README.md)：已有专题就增补，缺少独立研究分支时新建；同时回填前序工作。
- [成像训练数据合成 survey](surveys/imaging-training-data-synthesis.md)：MESS、RawGen、UNICE 与逆 ISP / RAW 生成 / 曝光数据路线的系统比较。
- [Diffusion 推理缓存与预测 survey](surveys/diffusion-inference-caching-forecasting.md)：训练免改的 reuse/forecast 与频带调度，SpecKCast 历史补录。\n- [高效生成式恢复 survey](surveys/efficient-generative-restoration.md)：单步 latent transport、少步蒸馏、判别式基线与真实性/成本权衡。
- [一步免反演编辑 survey](surveys/one-step-inversion-free-editing.md)：时间状态估计、端点校准和空间强度的不同控制维度。
- [选择性恢复和任务效用 survey](surveys/selective-task-aware-restoration.md)：KEEP/PURIFY/VERIFY，真实路由与净化器独立评价。

## 主题入口

### 2026-11-06 本轮新作

- [UGD-FM：无配准 NIR 引导、稀疏匹配与少步去噪](papers/arxiv-2611.06422.md)
- [UniRestorer++：退化层次扩容/区域专家与 CDD-50](papers/arxiv-2611.06042.md)
- [Dual Flow：image–measurement 联合 flow 反问题](papers/arxiv-2611.05843.md)
- [TailSteer：训练期修正多轮编辑漂移](papers/arxiv-2611.06741.md)

### 2026-11-06 周报追加

- [RGB 照片增强：跨 Snapdragon/Dimensity GPU/NPU](papers/arxiv-2611.05024.md)
- [真实手机 RGB 去噪：跨 SoC 部署](papers/arxiv-2611.00974.md)
- [4K 超分：移动 NPU 量化与 fallback](papers/arxiv-2611.00963.md)
- [ILLRAW：照度感知的 RAW 直接检测](papers/arxiv-2611.02995.md)
- [Goal-Driven Optical Experimentation：仪器确认闭环](papers/arxiv-2611.04481.md)
- [FLASH：冻结低分辨率锚点的 4K 编辑](papers/arxiv-2611.04416.md)
- [BiCG-Net：轻量目标级 IQA 与弱标签边界](papers/arxiv-2611.06203.md)

### 2026-11-05 缺口补查重点

- [CHROMA-MILL：低光增强与 AWB 联合标定](papers/arxiv-2611.04092.md)
- [LOL Benchmark label shift：训练/测试 GT 与排名审计](papers/arxiv-2610.38121.md)
- [CIE-grounded MLLM 色彩评价](papers/arxiv-2610.40212.md)
- [NightIQA：夜景局部失真与问答评价](papers/arxiv-2611.04811.md)
- [无 clean GT：非高斯噪声生成过程](papers/arxiv-2610.42036.md)
- [3L-D：标定真实光照台的夜级数据](papers/arxiv-2611.02695.md)
- [Beyond CCT：多通道 SPD 估计与 CCM](papers/arxiv-2610.40175.md)
- [Mobile AI 2026 Learned ISP 真机 GPU 报告](papers/arxiv-2611.05008.md)
- [HIVE-Diff：一帧 LDR + Event 的 HDR 视频](papers/arxiv-2611.03465.md)

### ISP / 成像逆问题

- [Dual-Camera Smooth Zoom：几何—光度解耦的双摄连续切换](papers/arxiv-2610.34854.md)


- [BAM：显式成像算子 + 少步后验采样](papers/arxiv-2609.39660.md)
- [RawVLA：任务目标反向约束显式 ISP](papers/arxiv-2609.37530.md)
- [Neural Block-wise AE：分块曝光与单次 HDR](papers/arxiv-2610.18733.md)
- [DuSRFlow：双摄大视差专用流与可靠性融合](papers/arxiv-2610.14630.md)
- [RIECR：统一 RAW 欠曝/过曝校正与恢复](papers/arxiv-2610.28191.md)
- [MESS：RAW 引导的多曝光训练数据合成](papers/arxiv-2610.24680.md)

### RAW / 传感器 / 任务成像

- [Raw Imagery Impacting Your AI：SNR/MTF/分辨率到检测效用](papers/arxiv-2609.38265.md)
- [Dense Illuminant：物理合成的密集多光源监督](papers/arxiv-2610.06508.md)
- [S3D-Mosaic：跨波段结构迁移的光谱去马赛克](papers/arxiv-2610.24414.md)

### HDR / Tone Mapping

- [Physics-Guided Exposure Interpolation：物理中间曝光 + diffusion 高频残差](papers/arxiv-2610.37135.md)


- [ExpandDiff：双端裁剪分布与 HDR 重建](papers/arxiv-2609.39624.md)
- [FLASH：时序 HDR 跨曝光脉冲光攻击](papers/arxiv-2609.37742.md)
- [既有 HDR 专题资料](HDR/)

### 恢复 / 视频 / 参考传播

- [TINDER：用输入反演噪声维持零样本视频恢复时序](papers/arxiv-2610.37290.md)


- [GLOW-FM：Tiny-VAE + TVM 单步低光增强](papers/arxiv-2610.31222.md)
- [Gate3DGen：任务导向净化与真实路由对照](papers/arxiv-2610.31649.md)

- [RelayVSR：稀疏生成参考与逐帧轻量恢复](papers/arxiv-2609.37850.md)
- [HarnessIR：MFM executor + verification 的真实恢复](papers/arxiv-2610.10133.md)
- [LoopMoEVR：循环 MoE 的统一 UHD 恢复](papers/arxiv-2610.05109.md)
- [OLiVES：同步低照视频增强与分割基准](papers/arxiv-2610.20501.md)
- [Physics-Shaped, Not Physical：物理引导恢复审计](papers/arxiv-2610.19763.md)
- [WorldSR：实体检索约束的多参考超分](papers/arxiv-2610.28423.md)

### 效率 / 推理缓存与预测\n\n- [SpecKCast：按频带时间校准的 Kalman 输出预测](papers/arxiv-2610.26837.md)（2026-10-21 已推荐，10-24 补归档）\n\n### 编辑 / Agent / 可控渲染

- [PREEN：参考风格回归 29 维手机编辑预设](papers/arxiv-2610.36896.md)
- [EditJev：编辑模型的样本级速度—质量路由](papers/arxiv-2610.32635.md)


- [ECT：单时刻免反演编辑与端点校准](papers/arxiv-2610.30827.md)

- [FlowTool：连续参数与离散工具选择的边界](papers/arxiv-2609.35673.md)
- [The Camera Inside the Editor：几何保真评价](papers/arxiv-2609.37732.md)
- [ARRO：结构化最小改动 reward](papers/arxiv-2610.06021.md)
- [UniSlider：感知均匀的连续编辑校准](papers/arxiv-2610.06831.md)
- [PreActIR：执行前预测与 commit/rollback](papers/arxiv-2610.20384.md)
- [BluePixel：native 4K 模型与编辑 Agent](papers/arxiv-2610.19882.md)
- [MT Forcing：自 rollout 与单轮 teacher 的多轮编辑稳定化](papers/arxiv-2610.25404.md)
- [既有 AgenticIR 资料](AgenticIR/)

### IQA / 观察者

- [MoI-Bench：移动生成/编辑的质量—部署二维基准](papers/arxiv-2610.37599.md)
- [VGIQA：局部缺陷 grounding reward](papers/arxiv-2610.37186.md)
- [Chains and Gains：RL-IQA 的 CoT 因果与捷径审计](papers/arxiv-2610.33203.md)


- [Multidimensional Observer Model：任务相关感知子空间](papers/arxiv-2609.38487.md)
- [EditJudgeBias：编辑评审器的顺序与线索偏置](papers/arxiv-2610.01670.md)
- [ScenePercept：场景条件化 UGC 感知评价](papers/arxiv-2610.17661.md)
- [Face Contrast：手机人像三维可解释对比度](papers/arxiv-2610.26517.md)
- [CheckDistill：结构化 checklist 的编辑 reward 蒸馏](papers/arxiv-2610.26740.md)
- [VHA：生成式超分 hallucination 的问答式审计](papers/arxiv-2610.25770.md)

### World Model / 时序状态

- [LOCI：几何条件化混合记忆](papers/arxiv-2609.40222.md)

## 周报快照

- [2026-11-06：三个 Topic Update，四项新作](Recent_Papers_2026-11-06.md)
- [2026-11-05：停用缺口恢复与 Topic Update](Recent_Papers_2026-11-05.md)

- [2026-10-30：双摄连续切换、移动部署基准与 IQA 因果审计](Recent_Papers_2026-10-30.md)

- [2026-10-24：一步低光、一步编辑与选择性恢复的三个判断变化](Recent_Papers_2026-10-24.md)

- [2026-10-23：RAW 曝光恢复、显式检索式 SR 与 CameraX 控制边界](Recent_Papers_2026-10-23.md)
- [2026-10-16：分块曝光、双摄可靠性与预测式恢复 Agent](Recent_Papers_2026-10-16.md)
- [2026-10-09：任务导向 ISP、恢复 agent 与 evaluator 风险](Recent_Papers_2026-10-09.md)
- [2026-10-01：首批回填，2026-10-03 核验](Recent_Papers_2026-10-01.md)
- [2026-09-19：既有笔记，未在本次重新核验](Recent_Papers_2026-09-19.md)
- [2026-09-18：既有笔记，未在本次重新核验](Recent_Papers_2026-09-18.md)

## 归档机制

- [ARCHIVE_PROTOCOL：源头核验、职责、去重、同步与通知](ARCHIVE_PROTOCOL.md)
- [registry.json：稳定身份、证据范围、结论 key 与增量事件](archive/registry.json)
- [LEGACY：历史已出现对象与纠错边界](archive/LEGACY.md)

同一论文新版本只更新原卡片；真正改变决策才再次通知。若只是旧论文晚上传 arXiv、相同结论的新转述或同步重试，不当成研究新增。标题改名、会议版本与预印本用别名归并。

## 既有资料

- [Snapdragon 笔记](Snapdragon.md)
- [既有 prompt](prompt.md)

本次未移动或重写既有内容。新机制从首批回填开始运转，不代表历史资料已经全面规范化。

## References

一手论文、项目和实验依据请进入各卡片 References。跨厂商论文归属规则以 [CameraPaper CONTRIBUTING](https://github.com/baolinv0/CameraPaper/blob/main/CONTRIBUTING.md) 为准。

## 批判性论文研究 Skill

- [critical-paper-research](skills/critical-paper-research/)：L1 论文快速筛选、L2 批判性深度审查、L3 可证伪研究计划；支持最近前作反查、实验归因、ISP/计算摄影部署专项与证据分级。
- [CameraPaper 研究方法库](https://github.com/baolinv0/CameraPaper/blob/main/knowledge/research-methodology/paper-review-framework.md)：跨论文的审查框架与经验 R01–R06。
- 运行时安装与仓库归档是两个不同动作；参见 [Skill 安装说明](skills/critical-paper-research/README.md)。

