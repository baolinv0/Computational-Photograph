# Computational-Photograph｜计算摄影研究库

目录：[怎么使用](#怎么使用) · [长期文献地图](#长期文献地图) · [主题入口](#主题入口) · [周报快照](#周报快照) · [归档机制](#归档机制) · [既有资料](#既有资料) · [References](#references)

## 怎么使用

先看每篇卡片的“快速回忆”，再按需展开“精读记录”。**收藏不等于已读，摘要核验不等于全文验证，作者实验不等于独立复现。**论文正文只维护一份；周报记录当时的变化和链接。

本仓库存通用研究技术笔记；厂商归属、产品/专利和竞品证据进入 [CameraPaper](https://github.com/baolinv0/CameraPaper/blob/main/WEEKLY_ARCHIVE.md)。Notion 作为私有阅读入口，alphaXiv 收藏原论文。

### 按问题快速定位

| 想解决的问题 | 长期问题地图 | 相关专题入口 |
|---|---|---|
| 采集、曝光或 HDR 输入应保留什么信息？ | [T01：采集与成像物理](LITERATURE_MAP.md#t01) | [HDR 数据分类](HDR/HDR_Data_Taxonomy.md) |
| 如何控制照片呈现，或理解一步编辑？ | [T02：影调、颜色、意图与参考](LITERATURE_MAP.md#t02) | [一步免反演编辑与端点校准](surveys/one-step-inversion-free-editing.md) |
| 生成式恢复怎样权衡质量、真实性与成本？ | [T03：可信恢复与高分辨率](LITERATURE_MAP.md#t03) | [高效生成式恢复](surveys/efficient-generative-restoration.md) |
| 质量评价与任务效用应怎样区分？ | [T04：IQA、Reward 与偏好决策](LITERATURE_MAP.md#t04) | [选择性恢复与任务效用](surveys/selective-task-aware-restoration.md) |
| 训练监督来自哪里，哪些部分可信？ | [T05：数据与 Pseudo-GT](LITERATURE_MAP.md#t05) | [成像训练数据合成](surveys/imaging-training-data-synthesis.md) |
| 恢复执行器如何组织、验证与重试？ | [T06：Agent、动作与闭环控制](LITERATURE_MAP.md#t06) | [AgenticIR survey](https://github.com/baolinv0/CameraPaper/blob/main/knowledge/imaging-agent/agentic-image-restoration-survey.md) |
| 多步推理怎样减少计算，缓存与预测有何区别？ | [X01：效率与训练部署](LITERATURE_MAP.md#x01) | [Diffusion 缓存、预测与分频调度](surveys/diffusion-inference-caching-forecasting.md) |

查找单篇论文：[全部论文速查（由 registry 生成）](papers/README.md)。查看全部已有专题：[持续专题综述索引](surveys/README.md)；按日期回顾：[周报快照](#周报快照)。

## 长期文献地图

- [持续文献总图：问题、竞争路线与系统方案](LITERATURE_MAP.md)：六个稳定主题与横向效率层；先建立问题坐标，再定位新证据。初版为结构基线，不代表所有历史论文已重新核验。
- [Paper Watch v3：主题更新与方案回忆规则](archive/PAPER_WATCH_V3.md)：旧地图 → 新证据 → 判断变化与不变部分 → 系统位置 → 决策。保留原有新颖性审查、去重和无更新静默规则。

地图维护跨论文关系和当前认识；以下主题入口仍导航到唯一技术卡片。已有专门综述不被总图取代，私人项目方案和未公开实验不写入公共地图。

- [持续专题综述索引](surveys/README.md)：已有专题就增补，缺少独立研究分支时新建；同时回填前序工作。
- [成像训练数据合成 survey](surveys/imaging-training-data-synthesis.md)：MESS、RawGen、UNICE 与逆 ISP / RAW 生成 / 曝光数据路线的系统比较。
- [Diffusion 推理缓存与预测 survey](surveys/diffusion-inference-caching-forecasting.md)：训练免改的 reuse/forecast 与频带调度，SpecKCast 历史补录。
- [高效生成式恢复 survey](surveys/efficient-generative-restoration.md)：单步 latent transport、少步蒸馏、判别式基线与真实性/成本权衡。
- [一步免反演编辑 survey](surveys/one-step-inversion-free-editing.md)：时间状态估计、端点校准和空间强度的不同控制维度。
- [选择性恢复和任务效用 survey](surveys/selective-task-aware-restoration.md)：KEEP/PURIFY/VERIFY，真实路由与净化器独立评价。

## 主题入口

### ISP / 成像逆问题

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

- [ExpandDiff：双端裁剪分布与 HDR 重建](papers/arxiv-2609.39624.md)
- [FLASH：时序 HDR 跨曝光脉冲光攻击](papers/arxiv-2609.37742.md)
- [既有 HDR 专题资料](HDR/)

### 恢复 / 视频 / 参考传播

- [GLOW-FM：Tiny-VAE + TVM 单步低光增强](papers/arxiv-2610.31222.md)
- [Gate3DGen：任务导向净化与真实路由对照](papers/arxiv-2610.31649.md)

- [RelayVSR：稀疏生成参考与逐帧轻量恢复](papers/arxiv-2609.37850.md)
- [HarnessIR：MFM executor + verification 的真实恢复](papers/arxiv-2610.10133.md)
- [LoopMoEVR：循环 MoE 的统一 UHD 恢复](papers/arxiv-2610.05109.md)
- [OLiVES：同步低照视频增强与分割基准](papers/arxiv-2610.20501.md)
- [Physics-Shaped, Not Physical：物理引导恢复审计](papers/arxiv-2610.19763.md)
- [WorldSR：实体检索约束的多参考超分](papers/arxiv-2610.28423.md)

### 效率 / 推理缓存与预测

- [SpecKCast：按频带时间校准的 Kalman 输出预测](papers/arxiv-2610.26837.md)（2026-10-21 已推荐，10-24 补归档）

### 编辑 / Agent / 可控渲染

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

- [Multidimensional Observer Model：任务相关感知子空间](papers/arxiv-2609.38487.md)
- [EditJudgeBias：编辑评审器的顺序与线索偏置](papers/arxiv-2610.01670.md)
- [ScenePercept：场景条件化 UGC 感知评价](papers/arxiv-2610.17661.md)
- [Face Contrast：手机人像三维可解释对比度](papers/arxiv-2610.26517.md)
- [CheckDistill：结构化 checklist 的编辑 reward 蒸馏](papers/arxiv-2610.26740.md)
- [VHA：生成式超分 hallucination 的问答式审计](papers/arxiv-2610.25770.md)

### World Model / 时序状态

- [LOCI：几何条件化混合记忆](papers/arxiv-2609.40222.md)

## 周报快照

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
- [贡献与检查：更新顺序、索引生成与离线校验](CONTRIBUTING.md)

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

