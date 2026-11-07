# 持续专题综述索引

更新：2026-11-07

目录：[专题](#专题) · [维护原则](#维护原则)

## 专题

| 主问题/主题 | Canonical survey | 范围与状态 |
|---|---|---|
| T02/T03：编辑器如何联合理解、生成并保留几何先验？ | [执行器理解、几何与训练](editor-understanding-and-geometry-training.md) | 2026-11-07：WeLM-Image工程系统与StitchEdit逐层兼容迁移；独立于多轮漂移/Agent Judge |
| T04/T06：视频伪影列表能否让Reward选择更可信？ | [伪影证据驱动Reward与验证](artifact-grounded-reward-and-verification.md) | 2026-11-07：ArtiVidRM vs VideoScore/VisionReward；保留MonetBench与Hit@1反例 |
| T01/T03：真实跨模态观测在不对齐时如何帮助恢复？ | [非配准跨模态导引恢复](unaligned-guided-restoration.md) | 2026-11-06：UGD-FM，含 NIR 数据边界、sparse alignment 与单图基线 |
| T03/T05/X01：统一恢复怎样随退化层次扩容？ | [统一恢复的退化建模与专家扩容](universal-restoration-degradation-routing.md) | 2026-11-07：增加OptIMerge后验融合权重（与UniRestorer++层级MoE竞争而非继承）；完整预算/硬件边界 |
| T06/T02：如何抑制多轮图片编辑中的累积漂移？ | [多轮编辑保真](multi-turn-editing-preservation.md) | 2026-11-06：MT Forcing 与 TailSteer 的训练/推理/控制分层；单轮副作用 |
| T01/T02/T05：低光、光源、色彩怎样联合定义 GT？ | [低光 RAW、AWB 与照明光谱](low-light-raw-awb-illumination.md) | 2026-11-05 补查：CHROMA-MILL、3L-D、Beyond CCT；含关键成立条件及跨手机缺口 |
| T04/T05：低光/颜色评价的 GT 和 Judge 是否可靠？ | [低光 IQA、Color Judge 与 LOL Benchmark 审计](low-light-iqa-and-gt-validity.md) | 2026-11-05 补查：LOL 标签偏移、CIE 颜色真值、NightIQA；区分排名、物理色差与 MCQ |
| T05/T03：只有噪声测量能否学习干净生成分布？ | [无干净 GT 的生成式恢复](noisy-measurements-to-clean-generators.md) | 2026-11-05 补查：Noise2Noise→非高斯测量过程+Consistency，理论条件与手机 RAW 缺口 |
| X01/T01：实机 Learned ISP 和 Event-HDR 怎样对比？ | [移动 ISP GPU 部署与 Event-HDR](mobile-isp-and-event-hdr-efficiency.md) | 2026-11-07：CoGenRec作为CVS新观测重建分支；2026-11-05补查Mobile AI 2026 实机 Benchmark + HIVE-Diff 的单参考事件采集 |
| T05：训练数据从哪里来，哪些部分可信？ | [成像训练数据合成：逆 ISP、RAW 生成与曝光退化](imaging-training-data-synthesis.md) | MESS、RawGen、UNICE 等 13 项代表工作；v0.1，有明确全文/摘要核验边界及待补历史分支 |
| T01/T05：HDR 来源、输入与目标是什么关系？ | [既有 HDR 数据分类](../HDR/HDR_Data_Taxonomy.md) | 复用既有文档，不迁移；本次不重新核验其中全部条目 |
| T02/T05：SDR video → HDR 的训练目标怎么定义？ | [既有 HDR 数据与 PGT](../HDR/HDR_Dataset_References_and_PGT.md) | 保留原适用范围，通用合成路线转至本目录新分支 |
| X01/T03：多步 DiT 推理怎样在不训练时减少网络调用？ | [Diffusion 缓存、预测与分频调度](diffusion-inference-caching-forecasting.md) | 2026-10-24 v0.1；SpecKCast 历史补录（10-21 已推荐），比较 TeaCache/TaylorSeer/Spectrum，前序待逐篇复核 |
| T03/X01：生成式恢复能否用一次网络前向完成？ | [高效生成式恢复：潜空间与采样目标](efficient-generative-restoration.md) | 2026-11-06 增加与 LLIE 不同任务的已知线性算子 Dual Flow 分支；原 GLOW-FM/TVM 结论未改 |
| T02/T06：一步编辑要几个噪声时刻？ | [一步免反演编辑与端点校准](one-step-inversion-free-editing.md) | 2026-10-24 v0.1；ECT 对 ChordEdit，ER-Chord 作为不同空间控制轴；前序 backlog |
| T06/T03/T04：什么时候不应该恢复？ | [选择性恢复与任务效用](selective-task-aware-restoration.md) | 2026-10-24 v0.1；Gate3DGen 的净化器效果和真实路由负例分开记录 |
| T06：恢复执行器如何组织、验证与学习策略？ | [CameraPaper 的 AgenticIR survey](https://github.com/baolinv0/CameraPaper/blob/main/knowledge/imaging-agent/agentic-image-restoration-survey.md) | 复用另一仓库已有 canonical survey；不复制第二份全文 |

这是跨仓库导航，不代表所有主题都已完成 survey；未建设的分支继续保存在 [总图](../LITERATURE_MAP.md) 中。

## 维护原则

1. **已有则插入，缺少独立分支才创建。** 查同问题和同义词，不仅查文件名。
2. 新论文连同必要历史工作，进入对应路线、比较表、证据和当前判断；不只在文末追加名单。
3. 论文卡片只有一个 canonical path；多主题复用链接。survey 管综合关系，卡片管单篇证据。
4. 前序无年龄限制；旧论文用 backfill，不冒充新增提醒。发表先后不等于继承。
5. 主视图保留少量记忆锚点，完整索引可扩展；写明已核验范围、反证和未覆盖部分。

执行规则：[Paper Watch v3.2](../archive/PAPER_WATCH_V3.md#持续专题综述)。
