# Paper Watch v3.2 — 2026-11-12 Topic Update

## 本轮结论

本轮覆盖到 **2026-11-11（Wednesday）arXiv daily new listing**，相对上次成功覆盖的 2026-11-10 listing 出现 5 项达到通知门槛的研究事件：

- **New：2 篇** — RetinexGS、Dark Matters。
- **Update：3 项** — LucidNFT v4、DVFace v2、UWNature v2。
- 首次覆盖日期统一为 **2026-11-12**。每篇分别记录 arXiv v1 首传、当前版本提交时间、11-11 public listing 和本库首次覆盖日期；版本更新不重复算作新论文。
- 本轮没有发现足以改变结论的 DORIS v2 更新；其 v2 扩展了实验，但核心 MixPolar 数据/方法和主结论在 v1 已存在，因此不推送 Update。

---

## Topic 1｜T01/T02/T03：输入表示决定可恢复信息的边界

### 1. 旧地图

这里有两个相关但不同的问题：

- **低照 RAW 多视图重建：** RawNeRF（2021）在线性 RAW 上利用多视图噪声平均；LE3D（2024）将问题迁移到 3DGS；From Chaos to Clarity（2024）通过 noise extractor / noise prior 防止 Gaussian 拟合 RAW 噪声；HDRSplat（2024）强调 14-bit RAW 与 HDR loss。
- **HDR 视频生成：** LumiVid（2026）使用 LogC3 对齐预训练生成 latent；DiffHDR（2026）使用 Log-Gamma 与 latent radiance inpainting。

以上均为历史锚点，不是本轮新推荐。

### 2. 本次变化

**New — RetinexGS**  
[arXiv:2611.13280](https://arxiv.org/abs/2611.13280) · Yulang Fei、Huaiyuan Weng、Chul Min Yeum

- arXiv v1 首传：2026-11-09 21:44 UTC；当前 v1；首次进入本轮 public new listing：2026-11-11；本库首次覆盖：2026-11-12。
- 核心命题：用 Retinex-style base-color/modulation factorization、DNG noise metadata weighting 和 depth-guided initialization，改善低照 RAW 3DGS 的外观/噪声/几何优化。
- 关键证据：3 个公开 RawNeRF 场景 + 2 个自采 RAW 场景；作者报告 mean sRGB PSNR 比 LE3D 高 2.18 dB、比 RawNeRF 高 2.71 dB；RTX 4090 novel-view rendering 91–145 FPS。
- 主要争议：只有 5 个定量场景；RetinexGS 15k iterations，对照设置 30k；总增益不能全部归因于 DNG noise weighting，appearance factorization 是重要贡献；sRGB 指标还包含 per-channel affine alignment。
- 近年前序：RawNeRF、LE3D、From Chaos to Clarity、HDRSplat。与 RawNeRF/LE3D 是直接竞争；与另两篇是共同抽象机制下的互补/竞争，未确认直接方法继承。
- 作者主张：低照 RAW 场景重建质量和渲染效率提升。
- 局部证据：5 场景定量、6 场景定性、模块消融和 4090 渲染速度。
- 共同方向：RAW noise-aware 3DGS 正在形成多条竞争路线；尚无跨相机共识。
- 裁决：**GO-E**。价值类型是系统工程与表示/损失成熟度，不是新问题定义。
- 地图变化：**Engineering maturity + Boundary refinement**。

**New — Dark Matters**  
[arXiv:2611.13504](https://arxiv.org/abs/2611.13504) · Donghoon Cha、Bomseok Park、Hansl von Kwon、Ku DoHyung、Hanwool Sul

- arXiv v1 首传：2026-11-10 03:16 UTC；当前 v1；首次 public new listing：2026-11-11；首次覆盖：2026-11-12。
- 核心命题：预训练 VAE 在 HDR 深暗区域可能丢失 chroma；在 VAE 前加入 13-parameter invertible exposure-equivariant EquivFlow，让曝光变化成为 additive shift、chroma 对曝光尺度保持不变。
- 关键证据：多个冻结图像/视频 VAE 的编码测试；LTX-2.3 22B + IC-LoRA 端到端系统；5,780 crops、1,015 parent sequences；102 个 ARRI/HDRTV4K/UPIQ 视频片段。EquivFlow 拟合 15k steps，LoRA 训练 6.5k steps、4×H100 80GB；推理 30 diffusion steps，未报告墙钟/移动端成本。VAE round-trip 中 LogC3/Log-Gamma 的 reconstruction R² 可持平或略高，但在 −8/−10 EV 深暗区丢失更多 linearly recoverable chroma；EquivFlow 的六组 chromatic ΔEITP 更优，unseen ACES-like curve aggregate PSNR 则仍由 LogC3 占优。
- 主要争议：EquivFlow 与 LogC3 对比的输入合同不一致（scene-linear proxy vs raw SDR）；编码选择面板与 ARRI 测试集有少量重叠；unseen ACES-like curve 的 aggregate PSNR 上 LogC3 仍占优；无移动端成本。
- 近年前序：LumiVid（LogC3）、DiffHDR（Log-Gamma）。属于竞争表示路线，不能把发表先后当作继承。
- 作者主张：提升 VAE 传输深暗色度的能力。
- 局部证据：多 VAE 测试、102 clips 和 chroma loss ablation。
- 共同方向：VAE 前 HDR representation 是新近共同关注的问题；尚无最优编码共识。
- 裁决：**GO**。值得精读的是 exposure-equivariant / scale-independent chroma 表示，不是可直接替换手机 TM 的算法。
- 地图变化：**New route**。

### 3. 判断更新

此前主要把 RAW/HDR 表示看作输入预处理；现在应把它视为决定模型可恢复信息的关键接口。但两条路线必须分开：

- RetinexGS：多视图 RAW → 3D 场景重建。
- Dark Matters：SDR → scene-linear proxy → HDR encoding → frozen VAE → video diffusion。

不能把两者合并成一个通用增强器，也不能把它们的结果外推为移动 ISP 部署证据。

### 4. 系统方案

- **RAW 3DGS 在线：** trained Gaussian scene → view/exposure controls → rasterization → novel-view output。离线：multi-view RAW + DNG metadata → pose/depth initialization → Retinex factorization + noise-weighted loss → scene optimization。
- **HDR diffusion 在线：** SDR video → scene-linear proxy → LogC3/Log-Gamma/EquivFlow → frozen VAE → video diffusion → HDR video。离线：paired SDR/HDR clips → VAE round-trip / chroma tests → encoding fit → LoRA fine-tuning。
- 两条路线均无 Agent 控制层。

### 5. 行动

保留两条研究分支，不改变现有确定性 ISP/TM 方案。若验证 HDR 表示，先在相同输入合同、冻结 VAE、backbone、训练预算和 held-out tone curve 下比较 LogC3 / Log-Gamma / EquivFlow；若验证 RAW 噪声先验，固定 3DGS appearance capacity 后只切换 DNG-weighted loss。

### 6. 记忆锚点

线性 RAW 的多视图噪声平均，与 VAE 前的 HDR 色度传输，是两个不同层级的表示问题。

详细正文：
- [Low-Light RAW Neural Rendering survey](surveys/low-light-raw-neural-rendering.md)
- [VAE-Aware HDR Representation survey](surveys/vae-aware-hdr-representation.md)

---

## Topic 2｜T03/T04/X01：生成恢复的保真奖励与真实推理成本

### 1. 旧地图

- DSPO（2025）将 human preference 引入 Real-ISR，结合 semantic instance alignment 与用户描述反馈。
- DiffusionNFT 提供 policy update；多 reward 如何合并为训练信号仍是关键设计点。
- DicFace（2025）通过时序 codebook 建模视频人脸特征变化；多步 diffusion 视频恢复则以推理成本换取生成能力。

### 2. 本次变化

**Update — LucidNFT v4**  
[arXiv:2603.05947](https://arxiv.org/abs/2603.05947) · Song Fei、Tian Ye、Sixiang Chen、Zhaohu Xing、Jianyu Lai、Lei Zhu

- v1 首发：2026-03-06；当前 v4 提交：2026-11-10 05:34 UTC；v4 首次 public replacement listing：2026-11-11；本库首次覆盖：2026-11-12。
- 核心命题：把 perceptual quality 与 LR-faithfulness 分成不同 reward，在每个 LR-conditioned rollout group 内先分别归一化，再融合为 DiffusionNFT update 信号。
- 真正增量：v4 新增 reward-independent human study：40 个 RealSR LR inputs、5 位专家、200 次 binary comparisons；LucidNFT 在 72.5% 的 binary judgments 中被判定更忠实于 LR，LucidFlux baseline 27.5%；实验不允许 tie，Fleiss’ κ=0.415。
- 近年前序：DSPO 是人类偏好 + 语义实例反馈路线；LucidNFT 明确沿用 DiffusionNFT update，主要改造 reward evaluator / scalarization，而不是提出全新 RL 算法。
- 争议：LucidConsistency 同时参与训练和部分评价，仍有 reward/metric self-reference；人评样本小；收益同时受 evaluator、LucidLR 数据和 RL budget 影响。RL 使用 8×A100、600 steps、24 LR groups × 12 rollouts、768 resolution，完整墙钟成本未给出。
- 作者主张：感知质量提升且 LR 证据保持更好。
- 局部证据：8 个 Real-ISR 方法、3 个真实退化测试集和 40-input human study。
- 共同方向：Real-ISR 正在从单一 perceptual reward 转向多目标 faithfulness/perceptual alignment；尚无通用 reward 共识。
- 裁决：**GO**。v4 的重要性是增加了独立人评证据，而不是新 RL objective。
- 地图变化：**Supporting evidence + Boundary refinement**。

**Update — DVFace v2**  
[arXiv:2604.14560](https://arxiv.org/abs/2604.14560) · Zheng Chen、Bowen Chai、Rongjun Gao、Mingtao Nie、Xi Li、Bingnan Duan、Jianping Fang、Xiaohong Liu、Linghe Kong、Yulun Zhang

- v1 首发：2026-04-16；当前 v2 提交：2026-11-10 08:19 UTC；v2 首次 public replacement listing：2026-11-11；本库首次覆盖：2026-11-12。
- 核心机制仍是 spatial/temporal dual-codebook + asymmetric fusion + one-step Wan2.1 diffusion。
- 真正增量：v2 增加效率测量与近期 diffusion restoration 对比。81 帧、512×512、单张 A6000、one-step 15.13 s，约 5.4 FPS；作者报告相对 SVFR 约 15.2×、相对 Upscale-A-Video 约 23.1×。训练约 16K VFHQ 视频并合成退化，codebook/LQ refinement/diffusion adaptation 分别 250K/50K/15K iterations，4×A6000。
- 争议：one-step 不等于 real-time；真实视频缺少 HR GT；长视频 chunk-wise inference 可能引入边界不一致。
- 近年前序：DicFace 的时序 codebook、SVFR 等多步视频人脸恢复路线。
- 作者主张：质量、身份保持和时序一致性优于近期方法。
- 局部证据：合成 GT benchmark、真实视频无 GT 指标和单卡效率表。
- 共同方向：视频人脸恢复正在结合时序先验与少步生成；尚无跨任务共识。
- 裁决：**GO-E**。价值类型是工程成熟度和真实成本证据。
- 地图变化：**Engineering maturity**。

### 3. 判断更新

LR-faithfulness 已有比 NR-IQA 更直接的训练和人评接口，但 LucidNFT 是离线 reward optimization，不是在线 judge。DVFace 的 one-step 有实测速度收益，但约 5.4 FPS 仍不是实时视频。候选可达性、可发现性、可选择性依然需要分开验证。

### 4. 系统方案

- **LucidNFT 在线：** LR → trained flow-based SR generator → SR。离线：LucidConsistency + LucidLR → 多候选 rollout → per-reward group normalization → DiffusionNFT update。Reward 不需要进入推理链。
- **DVFace 在线：** LQ video → spatial/temporal codebooks → asymmetric fusion → one-step Wan2.1 diffusion。离线：codebook learning → LQ refinement → diffusion adaptation。
- 两者都没有在线 Agent 控制层。

### 5. 行动

将 perceptual quality 与 LR-faithfulness 保持为两个独立目标；不要把 LucidNFT 当作在线候选选择器。视频恢复后续评价必须报告端到端吞吐、显存峰值和 chunk boundary consistency，而不是只报告 NFE。

### 6. 记忆锚点

Reward model 训练期可用，不代表它已成为可靠的在线候选选择器；one-step 也不等于 real-time。

详细正文：
- [LR-Anchored Real-ISR Preference Optimization survey](surveys/lr-anchored-real-isr-preference-optimization.md)
- [Efficient Generative Restoration survey](surveys/efficient-generative-restoration.md)

---

## Topic 3｜T05：Pseudo-GT 的内在真实性不等于训练效用

### 1. 旧地图

水下增强的历史锚点是三条不同路线：WaterGAN（2017）用 in-air RGB + depth 生成 paired underwater input；Sea-Thru（CVPR 2019）用 RGBD/range 与修正物理模型恢复颜色；UIEB（2019）提供 950 张真实水下图，其中 890 张有 pairwise-consensus reference、60 张没有满意参考。UWNature 则是 source-preserving unpaired synthesis。它们解决的不是同一个 GT 可信度问题。

### 2. 本次变化

**Update — UWNature v2**  
[arXiv:2511.14521](https://arxiv.org/abs/2511.14521) · Yufeng Tian、Yifan Chen、Zhe Sun、Libang Chen、Mingyu Dou、Jijun Lu、Ye Zheng、Xuelong Li

- v1 首发：2025-11-18；当前 v2 提交：2026-11-10 13:37 UTC；v2 首次 public replacement listing：2026-11-11；本库首次覆盖：2026-11-12。
- 核心路线：保留清晰自然照片作为 target，通过 unpaired image-to-image translation 生成 underwater input，避免把传统增强算法输出直接当作 clean GT。
- v1 已构建 UWNature 与 UWImgNetSD 两个各 10,000 pairs 的数据集，并报告 6 个架构/3 个测试集；v2 的真正增量是更深入的 appearance/structure/depth reliability 分析、depth-aware modulation、人类感知评价、degradation–restoration reciprocity 和 real-world validation。
- 关键证据：v1 已有 6 个 restoration architectures、3 个 test sets；v2 的新增分析表明，更高 spatial plausibility 不必然提升下游 restoration performance。
- 近年前序：UIEB/EUVP 等真实水下增强测试集；WaterGAN/算法增强参考等合成监督路线。UWNature 与真实水下 paired GT 不等价。
- 作者主张：source-preserving supervision 可提供具有竞争力的 underwater restoration data。
- 局部证据：跨架构/测试集结果与 human perceptual analysis。
- 共同方向：数据质量必须同时考虑 intrinsic plausibility 和 downstream utility；目前仍是 underwater 局部证据。
- 裁决：**PROBE**。价值类型是监督可靠性边界和反证。
- 地图变化：**Counter-evidence + Boundary refinement**。

### 3. 判断更新

此前可以把更真实的合成退化视作数据质量改善的代理指标；v2 明确提示这一推断不成立。数据评价至少要拆成 intrinsic realism、source/target consistency、downstream learning utility 三层。保持不变的是：clean in-air source 并不是真实 underwater radiance reference，结论不能直接迁移到移动相机。

### 4. 系统方案

clean source + unpaired underwater references → I2I degradation synthesis / depth modulation → source-preserving pseudo-pair → 多个 restoration students → 多测试集和 human evaluation。Agent 层为空。

### 5. 行动

保留 source-preserving pseudo-pair 路线，但把“生成图看起来更真实”与“训练后模型更好”分开测量。当前其他数据管线不因这一水下更新自动改变。

### 6. 记忆锚点

更真实的退化图，不一定产生更好的恢复模型。

详细正文：[Imaging Training Data Synthesis survey](surveys/imaging-training-data-synthesis.md)。

---

**纠错记录（LucidNFT v4，2026-11-12）：** 依据 arXiv v4 Table 9，human study 为 200 次 binary judgments、无 tie，72.5% vs 27.5%，Fleiss’ κ=0.415。此前草稿的 17.5% / 10% tie 是不准确转录，已更正。

## 其他候选与未升级项

以下已在本轮检索，但未进入 5 项主更新：

- **RB-LDC, arXiv:2611.13955 — WATCH。** 新的 latent coding / diffusion robustness 理论路线，实验显示 whitening 对总收益贡献很大；尚无 restoration downstream task，暂放 X01/T03 backlog。
- **SpatialSR, arXiv:2611.13046 — WATCH。** SRe-conditioned one-step remote-sensing SR，包含 UAV/Google Earth 数据；真实场景没有 paired HR GT，当前证据主要依赖 NR-IQA 和下游任务，域迁移到手机图像未验证。
- **PickGlass-TPI, arXiv:2611.13200 — WATCH。** 任务级图像质量与纺织密度测量案例，提醒 NR-IQA 与任务成功率可能脱钩；样本和场景范围窄，数据公开性/独立复现待确认。
- **LipsFlower, arXiv:2611.13995 — WATCH。** Lipschitz-constrained flow matching 的鲁棒人脸恢复；当前证据集中于单一 blind-face restoration task。
- **AncBench, arXiv:2611.13010 — WATCH。** 古文档恢复 synthetic benchmark，领域较窄，真实 paired GT 与跨场景效用待验证。
- **DORIS v2, arXiv:2610.17991 — no material map change。** v2 扩展比较，但 MixPolar 核心数据/方法和主要结论在 v1 已存在；不作为实质 Update。
- **DTO v2 / Diff-Instruct replacement — not promoted。** 前者偏通用 T2I reward optimization，后者本次更新主要是稿件/作者信息，未改变恢复领域判断。
- 核心作者组：alphaXiv 15 位 followed researchers 均已查询；没有新增的直接相关论文，已覆盖 DynOLAT 不重复推荐。

---

## 检索范围与时间边界

- 上次成功覆盖：2026-11-10 arXiv daily listing。
- 本轮成功覆盖：2026-11-11（Wednesday）listing；2026-11-12 listing 在扫描时尚未发布。
- arXiv categories：cs.CV、cs.LG、cs.AI、cs.MM、eess.IV、eess.SP 的 new/replacement listings；同时对 HDR/RAW、low-light、video restoration、SR、IQA/reward、preference、benchmark、training efficiency 做关键词检索。
- 页面总条目数（含 cross-list，不等于 unique new papers）：cs.CV 239、cs.LG 383、cs.AI 381、cs.MM 16、eess.IV 17、eess.SP 44。
- alphaXiv：15 位 followed researchers + discovery search；GitHub：Computational-Photograph 默认分支的 archive protocol、Paper Watch v3.2、LITERATURE_MAP、LEGACY、registry、相关 cards/surveys；CameraPaper README/knowledge index 与同名搜索。
- 访问失败不等于无新增；本轮已覆盖的日期边界与未发布的 11-12 listing 已明确记录。

## 实际归档回执

**GitHub：** 已创建 5 张 canonical cards；新建 3 个 living surveys；更新 efficient-generative-restoration、low-light-iqa-and-gt-validity、imaging-training-data-synthesis、HDR/HDR_Papers_and_IQA、HDR/README、surveys/README、LITERATURE_MAP、README 和 registry。后续读回验证路径与关键内容。

**alphaXiv：** 已按现有主主题收藏并读回 membership：
- HDR：Dark Matters
- Raw：RetinexGS
- Restoration：LucidNFT v4、DVFace v2、UWNature v2

未改变 Reading/Completed 状态；未写入 Notion；未修改 CameraPaper；未修改 schedule、时区、condition_watch、启用状态或客户端通知设置。

**未完成项：** 本轮没有读取私人项目的完整实验记录，因此不对当前项目实现/实测状态作判断；RetinexGS 的跨相机复现、Dark Matters 的 matched-input 三编码比较、LucidNFT 的更大规模人评、DVFace 的长视频 chunk consistency、UWNature 的跨域数据效用均留在对应 survey backlog。
