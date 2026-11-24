# 持续专题综述索引

更新：2026-11-24（任务导向 RAW ISP、Agent 元修订与指令依赖）

目录：[专题](#专题) · [维护原则](#维护原则)

### 2026-11-24｜3 New：任务相关重建、元修订、依赖顺序
| 问题 | Canonical survey | 本次变化 |
|---|---|---|
| T01 任务性能是否应从RAW重建阶段优化 | [任务导向 RAW ISP](task-oriented-raw-isp.md) | Dem2TA：表征对齐增量，非照片审美结论 |
| T06 怎样修改恢复技能的修订规则 | [AgenticIR 主综述](https://github.com/baolinv0/CameraPaper/blob/main/knowledge/imaging-agent/agentic-image-restoration-survey.md) | SIR-Agent：每次修订成本和旧任务回放约束 |
| T06/T02 单次请求内撤销与对象依赖 | [多轮编辑与保真](multi-turn-editing-preservation.md) | CRIE：内部依赖与跨轮状态、外部多图参考分开 |

### 2026-11-21｜5 New：场景自适应、生成目标与局部失败可控恢复
| 稳定问题 / 系统位置 | Canonical living survey | 本次判断变化 |
|---|---|---|
| T01 / ISP 执行：是场景global条件还是local多专家真正有效？ | [场景条件化 Neural ISP（新稳定问题页）](scene-conditioned-neural-isp.md) | [LG-FiLM](../papers/arxiv-2611.25639.md)：真实Fujifilm约+0.62 dB vs RMFA-Net，但global-only距full仅0.141；PROBE / Bridge+Boundary refinement |
| T02/T05 / 目标训练：生成器的审美选择能否转成结构保留的低成本调色？ | [摄影属性目标和编辑器控制](photo-attribute-targets-and-editor-control.md) | [AesDistill](../papers/arxiv-2611.25635.md)：64,644教师编辑→1.13M学生；自动评分不等于人类偏好，GO-E / New route |
| T05/T01/T03 / 无融合GT的目标如何定义？ | [成像数据与PGT监督](imaging-training-data-synthesis.md) | [ApexFuse](../papers/arxiv-2611.25453.md)：VIS/IR→经人筛选的生成目标→FLUX LoRA；需事实真实性审计，PROBE / New route |
| T03/T06 / 局部失败怎么修且保住别处？ | [选择性恢复与控制](selective-task-aware-restoration.md) | [FAIR](../papers/arxiv-2611.26456.md)：参考/ROI约束单步执行，GT-assisted reference vs LQ-only强区别，GO-E |
| T06/T03 / 即时动作收益与后续轨迹收益不同时怎样学习？ | [CameraPaper 唯一AgenticIR主survey](https://github.com/baolinv0/CameraPaper/blob/main/knowledge/imaging-agent/agentic-image-restoration-survey.md) | [RegionAgent](../papers/arxiv-2611.26179.md)：单步+轨迹DPO，固定工具消融+0.43dB，PROBE；18.6s/图，需无GT迁移 |

首次arXiv v1 2026-11-19、2026-11-20新公告；原论文选段核验，非独立复现，不把自动分数称人工判断；本轮[完整快照](../archive/PAPER_WATCH_2026-11-21_daily.md)。

### 2026-11-20｜状态交互与物理光度保真（新日更，独立于既有周报）

| 稳定问题/主题 | Canonical living survey | 本次改变 |
|---|---|---|
| T03/T05/T06：多退化当前状态是否改变另一退化的恢复响应？ | [统一恢复退化路由（已有页）](universal-restoration-degradation-routing.md) | [PROBE](../papers/arxiv-2611.23889.md)：语义轴+强度坐标+交叉有限差分；同骨干组合增量受静态坐标强基线限制，PROBE / New route |
| T03/T01/T05：科学SR如何兼顾真实测量与跨滤镜域泛化？ | [物理光度保持与跨滤镜超分（新稳定问题页）](photometric-fidelity-and-cross-filter-super-resolution.md) | [STAR++](../papers/arxiv-2611.24023.md)：2025 STAR 的重大扩展，36 HST滤镜、7个未见测试、FAA/SADL；GO-E / substantive Update；不将已有Flux Error当新 |

其中11月18日 v1的新研究在11月19日官方新公告；与当日周度任务已登记的五项不同ID，旧STAR不计当日新增。无跨手机实测、独立复现与OpenReview全覆盖证明。

### 2026-11-19｜3 New：采集可信度、局部执行与VLM读出

| 稳定问题/主主题 | 复用现有 Canonical living survey | 新证据与判断 |
|---|---|---|
| T01/T03/T05：不对齐的真实双相机引导怎样利用额外观测？ | [RGB–HSI / RGB–NIR 非配准恢复](unaligned-guided-restoration.md) | [TANGO/DUET](../papers/arxiv-2611.22699.md) 真实双相机 HR HSI+RGB，但 LR HSI 合成；全局/局部对齐+occlusion gate，GO-E / New route |
| T03/T06：恢复动作能否在网络内部区域化？ | [选择性恢复与控制位置](selective-task-aware-restoration.md) | [ExplicitIR](../papers/arxiv-2611.22222.md) 逐像素 Budget/Style field，区别于整图路由、latent gate、后处理 Judge；PROBE / Bridge |
| T04/T06：VLM 分数失准来自看不见还是读不出？ | [伪影证据、IQA 和评价接口](artifact-grounded-reward-and-verification.md) | [Lost in Read-out](../papers/arxiv-2611.22564.md) 层间 quality probe 与 closed-form readout，可能救回单图 MOS，但非通用编辑 Judge；GO-E / Boundary refinement |

新论文首传 2026-11-17、官方 cs.CV 新公告 11-18、首次覆盖 11-19。跨主题复用 canonical card，不另建重复 survey。

### 2026-11-18｜4 New + 1 Material Update（跨主题路由）

| 主题 | Canonical living survey | 本轮对长期地图的变化 |
|---|---|---|
| T01/T05 | [成像训练数据与真实同机采集监督](imaging-training-data-synthesis.md) | LC-ISP：live/capture 双流形成单帧 Neural ISP 的中间/终端监督；同机目标也不等于辐射 GT；GO-E |
| T03/T06 | [生成参考与真实测量不同](generated-reference-guided-low-light-restoration.md) | MrLIE：MLLM 造正常曝光参考→置信配准→源结构锚定 diffusion；生成参考不提供独立实测细节；PROBE |
| T03/X01 | [高效生成恢复的训练目标路线](efficient-generative-restoration.md) | FDIR：Fréchet feature distribution 损失训练一步恢复，对比 distillation / GAN；MUSIQ↑与PSNR↓须同时看；GO-E |
| X01/T03 | [移动 ISP 与 DiT 真实硬件成本](mobile-isp-and-event-hdr-efficiency.md) | dit.xpu：异构 NPU/GPU 静态 sparse+anchors；denoising E2E 与全产品 pipeline 不同；GO-E |
| T04/T02 | [HDR 显示与观看条件评价](display-viewing-conditioned-visual-quality.md) | HDR-VDC **2024 QoMEX→2026 arXiv 实质扩展**：新的是 35 VQA 指标/PU21+PPS 的比较和失败边界，原数据非新作；GO-E Update |

## 专题

| 主问题/主题 | Canonical survey | 范围与状态 |
|---|---|---|
| T03/T04/T06：自然场景文字模糊时，什么时候可以借助语义推断恢复字符？ | [文字恢复的像素证据、语境推断和真实性边界](scene-text-faithfulness-and-reasoning.md) | 2026-11-16 backfill：ReasonText-SR 11-11 arXiv v1，11-14 已列候选；区分文本可推断性、render 执行能力、GT polygon OCR 指标与真实字符保真；不触发新论文通知 |
| T02/T05/T06：无专家编辑对时如何学习可执行的全局摄影目标？ | [摄影属性目标与确定性编辑器控制](photo-attribute-targets-and-editor-control.md) | 2026-11-14：ATune 10M优质图自退化→13属性目标→RawTherapee/darktable优化；与PREEN参考预设、群体/个体MOS区分，全局控制与42s搜索边界 |
| T02/T01/T03：未知TMO下如何约束SDR-to-HDR亮度偏差？ | [盲逆影调与可辨识性](blind-video-inverse-tone-mapping.md) | 2026-11-14：新SDR→HDR视频论文采用5个TMO边缘化+clip-gated expectile；与LogC3/EquivFlow前VAE表示分开；族外失效是明确边界 |
| T02/T05/T01：人物动态重照明怎样让光方向和相对强度可检验？ | [动态 OLAT 光照响应基与视频重照明](lighting-conditioned-portrait-video-relighting.md) | 2026-11-11：DynOLAT 实采 24M 帧+224衣着身份组合；对比 Lux Post Facto/HumanOLAT/直接视频 relighting；基视频生成成本和绝对光强不确定性明确 |
| T03/T01：已知测量算子下怎样在保持先验分布内优化？ | [已知算子的生成式反演与测量一致性](measurement-consistent-generative-inverse-problems.md) | 2026-11-10：FANO 对 DAPS/SITCOM 的优化变量与 radial drift；BAM/Dual Flow 为不同训练预算路线，真实 RAW 待验证 |
| T02/T05：固定物体布局，怎样协调前景照明与背景投影？ | [物体—环境光影协调与一步合成](object-scene-composition-and-relighting.md) | 2026-11-14：扩展与PACSRNet(2025)关联的FreeDeshadow物体指定cast-shadow移除；其是Paste2Place物体插入光影的互补逆任务，2026仅material Update；保留11-10物理bridge证据 |
| T04/T02：众人美学 MOS 怎样校准为个人偏好，与同场景修图偏好有何区别？ | [个人审美与摄影渲染评价](personalized-aesthetic-preference-and-rendering.md) | 2026-11-09：Undertone-P v2（11-05 公开）历史实质修订补录，PARA / LAPIS / DEAR 路线比较；不作新研究通知 |
| T02/T03：编辑器如何联合理解、生成并保留几何先验？ | [执行器理解、几何与训练](editor-understanding-and-geometry-training.md) | 2026-11-07：WeLM-Image工程系统与StitchEdit逐层兼容迁移；独立于多轮漂移/Agent Judge |
| T04/T06：编辑事实正确性、视频伪影与人类偏好如何分开检验Reward？ | [伪影、反事实正确性与Reward](artifact-grounded-reward-and-verification.md) | 2026-11-17 交叉更新：EditJudge-Bench 测指令事实正确性，TrustUIQA 测人类偏好/指标可刷分；ArtiVidRM/CheckDistill 保留原方法边界 |
| T01/T03：真实跨模态观测在不对齐时如何帮助恢复？ | [非配准跨模态导引恢复](unaligned-guided-restoration.md) | 2026-11-06：UGD-FM，含 NIR 数据边界、sparse alignment 与单图基线 |
| T03/T05/X01：统一恢复怎样随退化层次扩容？ | [统一恢复的退化建模与专家扩容](universal-restoration-degradation-routing.md) | 2026-11-07：增加OptIMerge后验融合权重（与UniRestorer++层级MoE竞争而非继承）；完整预算/硬件边界 |
| T06/T02：连续编辑怎样同时防止漂移，并保留未被撤销的属性？ | [多轮编辑保真/有效属性与当前载体](multi-turn-editing-preservation.md) | 2026-11-23 历史 backfill：在MT Forcing/TailSteer的训练期抑漂移路线外，加入TRACE（2026-11-19旧文），把“活跃颜色属性”与“旧表面像素”区分；窄颜色+材质任务有效，一般多轮仅小幅增益且有负例；不作新研究通知 |
| T01/T02/T05：低光、光源、色彩怎样联合定义 GT？ | [低光 RAW、AWB 与照明光谱](low-light-raw-awb-illumination.md) | 2026-11-05 补查：CHROMA-MILL、3L-D、Beyond CCT；含关键成立条件及跨手机缺口 |
| T04/T05：无 GT 增强评价和训练奖励在跨域/多轮优化时是否仍可靠？ | [低光、颜色与水下 IQA/Reward 审计](low-light-iqa-and-gt-validity.md) | 2026-11-17：TrustUIQA 73 个指标、五个人类参照、场景内偏好/简单调色与多轮漂移压力测试（与 LOL/CIE/NightIQA 目标区分）；GO-E，跨数据集最差 κ/同源训练收益边界 |
| T05/T03：只有噪声测量能否学习干净生成分布？ | [无干净 GT 的生成式恢复](noisy-measurements-to-clean-generators.md) | 2026-11-05 补查：Noise2Noise→非高斯测量过程+Consistency，理论条件与手机 RAW 缺口 |
| X01/T01：真手机 ISP、edge NPU 部署合同与 Event-HDR 如何分开评价？ | [移动 ISP GPU、edge NPU 与 Event-HDR](mobile-isp-and-event-hdr-efficiency.md) | 2026-11-13 backfill：三层 Baseline/VG-NPU/VG-E2E；原 Mobile AI 2026、CoGenRec/HIVE-Diff 保留不同硬件和观测边界 |
| T05：训练数据从哪里来，哪些部分可信？ | [成像训练数据合成：逆 ISP、RAW 生成与曝光退化](imaging-training-data-synthesis.md) | MESS、RawGen、UNICE 等 13 项代表工作；v0.1，有明确全文/摘要核验边界及待补历史分支 |
| T01/T05：HDR 来源、输入与目标是什么关系？ | [既有 HDR 数据分类](../HDR/HDR_Data_Taxonomy.md) | 复用既有文档，不迁移；本次不重新核验其中全部条目 |
| T02/T05：SDR video → HDR 的训练目标怎么定义？ | [既有 HDR 数据与 PGT](../HDR/HDR_Dataset_References_and_PGT.md) | 保留原适用范围，通用合成路线转至本目录新分支 |
| X01/T03：多步 DiT 推理怎样在不训练时减少网络调用？ | [Diffusion 缓存、预测与分频调度](diffusion-inference-caching-forecasting.md) | 2026-10-24 v0.1；SpecKCast 历史补录（10-21 已推荐），比较 TeaCache/TaylorSeer/Spectrum，前序待逐篇复核 |
| T03/X01：生成式恢复能否用一次网络前向完成？ | [高效生成式恢复：潜空间与采样目标](efficient-generative-restoration.md) | 2026-11-11：加入 DeLang-SR 暗光 SR 的退化语言方向和区域步长分离（20,390.77 GFLOPs；与判别式基线分开看）；2026-11-06 加 Dual Flow 已知线性算子分支；原 GLOW-FM/TVM 结论未改 |
| T02/T06：一步编辑要几个噪声时刻？ | [一步免反演编辑与端点校准](one-step-inversion-free-editing.md) | 2026-11-11 v0.3：V2C-Edit 多步 velocity 逐时刻 VLM 选择/成本；2026-11-10 v0.2：AR-Edit 的自回归视频 source-V 注入；ECT 对 ChordEdit，ER-Chord 作为不同空间控制轴；前序 backlog |
| T06/T03/T04：什么时候不应该恢复？ | [选择性恢复与任务效用](selective-task-aware-restoration.md) | 2026-11-15 backfill：SGVD（11-12 v1，11-13 已覆盖）区域级不确定性门控、双探测成本与时序 anchor，和整图 KEEP/RESTORE 门控明确分开；原 2026-11-10 v0.3：新增水下 UAV MLLM 诊断≠恢复的负例；原 Gate3DGen 与低光道路检测 WATCH/backfill 的不同任务负例：减少统一增强伤害不等于击败 always-KEEP；后者非新论文通知 |
| T06：恢复执行器如何组织、验证、学习并修订策略？ | [CameraPaper 的 AgenticIR survey](https://github.com/baolinv0/CameraPaper/blob/main/knowledge/imaging-agent/agentic-image-restoration-survey.md) | 2026-11-17 RecurIR：条件收益→主动反例→工具/顺序/区域修订→transfer/retention；与 SkillIR/EvoIR/SEAR 前序比较；复用跨库唯一主 survey，不复制正文 |

这是跨仓库导航，不代表所有主题都已完成 survey；未建设的分支继续保存在 [总图](../LITERATURE_MAP.md) 中。

## 2026-11-12 新建与更新

- [Low-Light RAW Neural Rendering](low-light-raw-neural-rendering.md) — T03/T01：RawNeRF、LE3D、From Chaos to Clarity、HDRSplat 与 RetinexGS 的 RAW 3DGS 竞争路线。
- [VAE-Aware HDR Representation](vae-aware-hdr-representation.md) — T02/T03：LumiVid LogC3、DiffHDR Log-Gamma、Dark Matters EquivFlow 的冻结 VAE 前表示路线。
- [LR-Anchored Real-ISR Preference Optimization](lr-anchored-real-isr-preference-optimization.md) — T04/T03：DSPO、DiffusionNFT 与 LucidNFT 的 reward / preference / LR-faithfulness 路线。
- 更新 [高效生成式恢复](efficient-generative-restoration.md)：补入 DVFace v2 的 one-step 视频人脸实测成本。
- 更新 [低光与颜色 IQA](low-light-iqa-and-gt-validity.md)：补入 LucidNFT v4 的 reward-independent human study。
- 更新 [成像训练数据合成](imaging-training-data-synthesis.md)：补入 UWNature v2 supervision reliability 反证。

## 2026-11-13 已有论文的知识地图接入（不作新增通知）

- [EditJudge-Bench](../papers/arxiv-2611.12524.md) 在 11-13 周报已归档：将 T04 主 survey 从原“执行器训练”交叉入口修正为 [Judge 反事实审计](artifact-grounded-reward-and-verification.md)，避免把生成能力与验证能力混淆。
- [Edge NPU Benchmark](../papers/arxiv-2611.13563.md) 在 11-13 周报已归档：补入 [端侧部署合同](mobile-isp-and-event-hdr-efficiency.md) 中的 common-I/O NPU 与 vendor-native E2E 三层比较。
- 两项均为 `missing_map_integration` 的历史整理；未改变首次公开、首次覆盖日期或已完成的 alphaXiv 收藏，不构成新论文或新通知。

## 维护原则

1. **已有则插入，缺少独立分支才创建。** 查同问题和同义词，不仅查文件名。
2. 新论文连同必要历史工作，进入对应路线、比较表、证据和当前判断；不只在文末追加名单。
3. 论文卡片只有一个 canonical path；多主题复用链接。survey 管综合关系，卡片管单篇证据。
4. 前序无年龄限制；旧论文用 backfill，不冒充新增提醒。发表先后不等于继承。
5. 主视图保留少量记忆锚点，完整索引可扩展；写明已核验范围、反证和未覆盖部分。

执行规则：[Paper Watch v3.2](../archive/PAPER_WATCH_V3.md#持续专题综述)。
