# HDR 常用数据集与 Benchmark：项目决策表

> Last checked: 2026-09-09  
> Scope: SDR→HDR / inverse tone mapping (ITM), same-EV HDR video, alternating-exposure HDR video, multi-exposure HDR imaging, HDR-IQA/VQA, HDR reference/master content.

## 目录

- [1. 如何读这个表](#how-to-read)
- [2. SDR→HDR / ITM：直接相关数据](#itm)
- [3. HDR Video / Temporal：视频源与多曝光数据](#video)
- [4. HDR Source / Reference：可用于合成和物理校验的数据](#source)
- [5. HDR IQA / VQA：主观质量与显示评价数据](#iqa)
- [6. 对当前项目的推荐组合](#recommended)
- [7. 使用任何 HDR 数据集前必须确认的信息](#checklist)

---

<a id="how-to-read"></a>
## 1. 如何读这个表

### 适用等级

- **S**：对当前 same-EV、8-bit、压缩 SDR video → HDR 项目某个关键环节具有直接价值，应优先获取。
- **A**：强相关，适合预训练、benchmark、受控实验或数据引擎。
- **B**：有明显参考价值，但任务/域存在较大差异。
- **C**：主要用于架构参考、辅助 sanity-check 或特定子问题。
- **D**：不适合作为当前项目主训练/主 benchmark，只能作为外围参考。

### 影响力标记

- **★★★★★**：经典/长期复用，或已经形成事实 benchmark。
- **★★★★☆**：高水平 venue + 明显复用/规模优势；新数据可能引用尚未充分积累。
- **★★★☆☆**：有价值但较新、较小或用途较窄。

> 注意：2025–2026 新数据不能仅以当前引用次数判断影响力，因此“影响力”综合考虑 venue、数据规模、是否形成挑战赛/后续工作、是否被多篇方法复用。

---

<a id="itm"></a>
## 2. SDR→HDR / Inverse Tone Mapping：直接相关数据

| 数据集 | 基本情况 | 原始数据 / 怎么得到 | SDR/HDR 配对真实性 | 影响力 / 使用情况 | 对当前项目适用度 | 最适合我们的用途 | 主要局限 |
|---|---|---|---|---|---|---|---|
| **HDRTV1K** | 1,235 train pairs + 117 test pairs；来源为 4K HDR10/SDR 视频帧；HDR 为 10-bit Rec.2020 PQ | 从 YouTube 收集具有 HDR10 版本及对应 SDR counterpart 的视频，抽帧形成 paired image dataset | **内容级 SDR/HDR counterpart，非 camera sensor 同源物理 GT** | **★★★★★**；ICCV 2021 HDRTVNet 建立后，被 FMNet、HDRTVNet++ 等 SDRTV→HDRTV 工作持续复用，是当前最常见的公开 ITM baseline 之一 | **A** | 单帧 baseline、Gain Map/ITM 对比、预训练、与公开论文横向比较 | 主要是逐帧 benchmark；不能验证长时 video stability；内容/后期制作域与眼镜 camera ISP 不同 |
| **AIM 2025 ITM Challenge** | 约 19,000 train pairs，100 val，100 test；256²/512²；PU21-PSNR/SSIM 评价 | 从真实 HDR 内容出发，经 exposure sampling → noise → clipping → sampled CRF/nonlinearity → 8-bit JPEG LDR | **HDR GT 真实，LDR 输入为合成 camera pipeline** | **★★★★☆**；ICCV AIM Challenge，67 名参与者、319 次有效提交；protocol 和隐藏 GT 使其 benchmark 可信度较高 | **A** | 做标准化单图 ITM 算法排名、验证 missing-highlight reconstruction 能力 | synthetic LDR domain；仍不能证明真实眼镜 ISP 泛化 |
| **xDR Dataset** | 10 段约 40 s、1920×1080、30 fps cinematic video；每段均有 SDR/HDR 版本 | 同一短片由专业制作流程分别 **native graded in SDR and HDR**，由专业调色人员保持同一艺术意图 | **真实独立 grading pair，不是 HDR→TMO→SDR 合成** | **★★★★☆（新但重要）**；2026 SPIC；当前规模小但数据构造非常稀缺，专门用于 ITM 评价 | **S（评价）/ B（训练）** | 最适合验证“算法输出是否接近真正专业 HDR rendering”，检查 synthetic-to-real grading gap | 只有 10 段；cinematic domain 与眼镜 UGC/camera domain 不同；更适合 eval 而非大规模训练 |
| **HDRMovie7K** | 大规模 lossless cinematic SDR-HDR frame pairs；AAAI 2026 | 来自专业 **Digital Cinema Distribution Master (DCDM)** workflow 的 SDR/HDR frame pairs | **真实专业后期配对，不是简单 synthetic TMO** | **★★★★☆（新）**；AAAI 2026，首次大规模 cinematic SDR/HDR lossless benchmark；引用尚未充分积累 | **A（研究）** | 学习专业亮度/色彩映射、验证 synthetic TMO 与真实 grading 差异 | 电影域与 camera UGC 不同；数据公开可获得性需按作者发布状态确认 |
| **HDRMovie1K** | 从公开 HDR film clips 构造的 streaming-oriented evaluation set | 从公开电影 HDR 内容 curated，面向在线/流媒体场景评估 | 不是 sensor-level paired capture；主要用于评测 | **★★★☆☆（新）**；与 HDRMovieformer 同期提出 | **B** | 检查模型在影视/streaming 内容上的跨域泛化 | 不是 mobile camera domain；不适合作为主要训练 GT |
| **LIVE-TMHDR** | 40 pristine HDR source videos → **15,000 tone-mapped sequences**；>750k subjective opinions；>1,600 observers | 40 个真实 HDR source，经 **10 个开源 TMO × 4 spatial settings × 3 temporal modes**，另有 2 proprietary TMO 和 **human expert colorist** 手工 tone map；同时包含 compression | **HDR source 真实；大部分 SDR 为 TMO 派生，少部分为专家人工 SDR** | **★★★★★**；目前最系统的 HDR→SDR tone-mapping diversity 数据之一，也是 LumaFlux 训练源之一 | **S** | **最适合构建 unknown-front-end-TM robustness 实验**；同一 HDR 经多种 TMO 产生多种 SDR，可测试逆映射是否依赖某一 tone style；专家 SDR 可做高质量 eval | 仍不是完整 camera ISP：不包含真实 sensor→AE/AWB→DNR→sharpen→local TM 的全部链路 |
| **LumaFlux mixed corpus** | 314,396 SDR-HDR pairs，来自 2,092 HDR videos；不是独立传统 benchmark | 将 HIDROVQA/CHUG/LIVE-TMHDR 等 HDR source 统一到 PQ/BT.2020/1000 nit；再生成 **8 TMOs × x264 CRF {23,31,39}** 的 SDR variants；LIVE-TMHDR 专家 SDR 可直接 passthrough | **HDR source 多为真实；绝大多数 SDR 仍为 synthetic degradation** | **★★★★☆（方法级）**；2026 LumaFlux 数据引擎；不是社区独立 benchmark，但构造方式很值得复用 | **A（数据引擎）** | 直接参考其“多 TMO + gamut conversion + codec round-trip + UGC/PGC balance”的造数方法 | 不应把 314K pair 规模误解为 314K 个真实 SDR/HDR camera pair；domain gap 仍存在 |

### 这一组怎么选

**如果要做公开论文 baseline：HDRTV1K + AIM 2025。**  
**如果要验证真实/专业 SDR↔HDR 映射：xDR + HDRMovie7K。**  
**如果要研究未知前端 Tone Mapping 鲁棒性：LIVE-TMHDR 最关键。**

---

<a id="video"></a>
## 3. HDR Video / Temporal：视频源与多曝光数据

| 数据集 | 基本情况 | 原始数据 / 怎么得到 | 输入曝光关系 | 影响力 / 使用情况 | 对当前项目适用度 | 最适合我们的用途 | 主要局限 |
|---|---|---|---|---|---|---|---|
| **HdM-HDR-2014 / Stuttgart** | 专业 cinematic HDR video；动态范围最高约 18 stops；OpenEXR scene-radiance、Rec.2020 graded versions | 两台 ARRI Alexa 通过 mirror-rig 同时采集不同曝光，约 4-stop 差，再重建 HDR；场景专门包含高光进出、亮度变化、肤色、specular、饱和彩色等 HDR 难例 | 原始数据是 **真实 HDR video**；后续 ITM 论文通常再从它合成 SDR/LDR | **★★★★★**；经典 HDR video source；长期被 HDRCNN、DeepHDRVideo、VITM-TC、AIM 等代际工作复用 | **A** | 作为高质量 HDR 母片，构造 **Fixed-EV / AE-varying / codec-degraded** 的受控实验；验证 temporal clue 到底来自哪里 | 它本身不是 SDR/HDR paired camera dataset；如果自己合成 SDR，结论仍只代表 synthetic domain |
| **LiU HDRv** | 多个真实 HDR sequences；公开 720p OpenEXR；原系统 2336×1752@30fps，>24 f-stops | LiU/SpheronVR 多传感器 HDRv camera 实拍；部分场景用 PR-650 做 radiometric calibration；很多序列未做绝对亮度标定 | 原始数据为 **真实 HDR video**，不是 LDR/HDR pair | **★★★★★**；经典 HDR video source；被 HDRCNN、STPN、DeepHDRVideo 等长期复用 | **A** | 与 HdM 类似，用作真实 HDR mother content；构造 fixed-EV synthetic SDR，做 temporal ablation | 多数序列不代表绝对 scene luminance；720p 公开版较低分辨率；非现代 mobile camera distribution |
| **MPI HDRv** | 经典小规模 HDR video source；常见工作使用约 2 个 sequence | 早期 MPI HDR video repository 的真实 HDR scene data | 原始 HDR；后续常被用来合成 LDR/作为 source | **★★★☆☆**；被早期 HDRCNN/STPN/VITM-TC 等使用，但规模非常小 | **B** | sanity-check、补充场景 | 规模太小，不应作为主要 benchmark；旧数据获取/维护稳定性较弱 |
| **DeepHDRVideo / ICCV 2021 benchmark** | 真实 + synthetic HDR video benchmark；真实捕获分 static GT、dynamic GT、dynamic no-GT；4K 级 Basler capture | 使用 Basler acA4096-30uc 拍摄 **2/3 档 alternating exposures**；另以 HdM/LiU HDR source 合成 alternating-exposure train/test data | **真实包围曝光**，输入帧之间具物理曝光互补信息 | **★★★★★**；ICCV 2021 后成为 alternating-exposure HDR video 主流 benchmark/代码基线之一 | **C（直接）/ A（架构）** | 学 alignment/fusion、motion robustness、real-world benchmark 设计 | 与我们 **same-EV SDR** 输入不公平；不能直接比较 PSNR 证明我们模型弱/强 |
| **Real-HDRV / CVPR 2024** | 500 LDRs-HDRs video pairs；约 28k LDR frames + 4k HDR labels；450 train/50 test；昼夜/室内外/多运动模式 | **RAW domain 实拍**；官方提供原始 RAW；预生成版本采用 2 档 alternating exposures、相差 3 stops；HDR label 为真实采集构造 | **真实 alternating-exposure** | **★★★★☆**；CVPR 2024；当前最重要的大规模 real-world HDR video reconstruction benchmark 之一；论文直接证明 real-data training 比 synthetic 更强 | **C（直接）/ A（capture-side）** | 如果未来眼镜允许 exposure-bracket/staggered capture，非常重要；当前可用于研究真实运动/对齐难点 | 和当前 fixed-EV 输入机制不同，不能作为主 benchmark |
| **Kalantari13 HDR Video / TOG13** | 9 个 dynamic video sequences；2/3 exposures；无可靠 HDR GT | 真实动态场景使用不同曝光拍摄；公开 exposure information、CRF 等 | **真实 alternating exposures** | **★★★★☆（经典）**；在 DeepHDRVideo 之前是常用真实动态 HDR video qualitative set | **D（主任务）/ B（参考）** | qualitative deghosting / alignment sanity check | 只有 9 段，且无 HDR GT，无法做严格定量 |
| **VITM-TC synthetic protocol over HdM/LiU/MPI** | 不是独立母数据集；CVPR 2024 用真实 HDR video source 生成普通 LDR video | 对 HDR \(H\) 施加 exposure \(T\) → clipping → gamma/CRF（论文采用约 1/2.2）得到 LDR；HDR 保留为 GT | **HDR GT 真实，LDR synthetic**；曝光可随时间改变 | **★★★★☆**；VITM-TC 用于 same-video temporal clue ITM | **A（机制验证）** | 很适合复现并进一步改造成 **strict Fixed-EV** 版本，直接测“same-EV 多帧到底有没有额外信息” | 原论文更依赖 temporal exposure diversity，不等价于我们严格固定 EV 视频 |

### 对我们最关键的结论

- **HdM / LiU / MPI = 真实 HDR 母片，不是现成真实 SDR/HDR pair。**
- **DeepHDRVideo / Real-HDRV = 真正的多曝光 HDR video reconstruction 数据，但输入条件与我们不一致。**
- 对当前项目，最有价值的实验是：基于 HdM/LiU 的同一 HDR GT，人工构造 **Fixed-EV / smooth-AE / alternating-exposure** 三种输入，定量拆解 temporal gain。

---

<a id="source"></a>
## 4. HDR Source / Reference：可用于合成和物理校验的数据

| 数据集 / 内容 | 基本情况 | 怎么得到 | 影响力 | 对当前项目适用度 | 推荐用途 | 局限 |
|---|---|---|---|---|---|---|
| **LIVE UGC-HDR** | **2,153** 个 10-bit HDR source videos；1080p/4K；30/60 fps；HLG + Rec.2100 | 由 amateur iPhone users 真实拍摄的 HDR UGC | **★★★★☆**；目前最重要的 consumer/mobile HDR source collection 之一；CHUG/Beyond8Bits/LumaFlux 研究链均依赖这一类 UGC HDR | **S（HDR source）** | **最贴近消费级 camera 内容分布**；可作为 HDR mother data 生成多种 SDR，特别适合补充手持运动、人像、日常场景 | 只有 HDR source，没有真实对应 SDR；若生成 SDR 仍属于 synthetic pair |
| **Fairchild HDR Photographic Survey** | 106 HDR images；28 张有 colorimetric/appearance data，其余至少有 absolute luminance calibration；可下载原始 exposure stacks | 静态场景多档曝光（通常 1 stop 间隔）融合；同时现场做 luminance/color measurement | **★★★★★**；HDR imaging/color science 经典 reference | **B** | 检查 absolute luminance、色彩、tone mapping 物理合理性；作为静态 HDR source | 图像不是视频；场景较老；不适合 temporal training |
| **Netflix Sol Levante** | 4K HDR anime open content；HDR10 Rec.2020 ST2084 1000 nit、Dolby Vision、16-bit HDR assets 等 | 从制作阶段即以 4K HDR 为目标完成专业 master；Netflix 开放 production/master assets | **★★★★☆**；行业级 open mastering reference，常用于 codec/display/HDR pipeline 验证 | **B** | 测 PQ/BT.2020/HDR10 pipeline、high-quality master sanity-check、codec robustness | 动画域单一；不是 camera UGC；不能代表 real sensor degradation |
| **Netflix Sparks / Nocturne 等 open content** | 4K/HFR/Dolby Vision/HDR mastering assets；Sparks 具有 16-bit RAW/PQ 等高质量版本 | Netflix 为 codec/HDR production 研究专门拍摄并开放 | **★★★★☆** | **B** | 专业 HDR master、极端亮度/编码测试 | 场景数量有限；仍非真实 SDR/HDR paired camera data |
| **SICE** | 589 高分辨率 multi-exposure sequences、4,413 images | 每个场景多曝光实拍；用 13 个 MEF/HDR 算法产生候选增强结果，再主观筛选参考图 | **★★★★★（曝光/增强领域）** | **C** | 学 exposure/contrast augmentation、局部明暗处理；辅助数据引擎 | 目标是 single-image contrast enhancement / MEF，不是 SDR→HDR video；reference 不是 radiometric HDR GT |
| **Kalantari17 HDR image dataset** | 74 train + 15 test scenes；每场 3 个不同曝光 LDR + HDR GT | 动态场景多曝光实拍；曝光常为 {-2,0,+2} 或 {-3,0,+3}；通过专门流程获得 HDR GT | **★★★★★（HDR deghosting）**；至 2026 仍是最常用 multi-exposure HDR image benchmark 之一 | **D（主任务）/ B（fusion参考）** | 研究对齐、deghosting、曝光互补；若未来做 bracket capture 很重要 | 单图、多曝光；与 same-EV SDR→HDR 核心任务不一致 |

---

<a id="iqa"></a>
## 5. HDR IQA / VQA：主观质量与显示评价数据

| 数据集 | 基本情况 | 怎么得到 | 影响力 / 认可度 | 对当前项目适用度 | 最适合我们的用途 | 主要局限 |
|---|---|---|---|---|---|---|
| **LIVE HDR** | 310 HDR10 videos，31 source contents × 10 bitrate/resolution variants；>20k opinions；66 participants（其中质量任务约 40 subjects）；50/60 fps | 专业 HDR10 content 经 resolution/bitrate ladder 转码；在不同 ambient 条件下实验室主观评分 | **★★★★☆**；早期大型 HDR video subjective benchmark | **A（IQA）** | HDR compression/quality model 校准，验证 HDR 输出在不同码率下的质量 | 主要是 PGC + compression；不评价 SDR→HDR reconstruction truthfulness |
| **LIVE HDR vs SDR** | 356 videos；212 公开；每视频有 3 个 TV 对应 MOS；>23k ratings，67 subjects，OLED/QLED/LCD | 同内容 HDR/SDR，在不同 scaling/bitrate + 三种显示设备上主观观看评分 | **★★★★☆**；IEEE TIP 2024；明确证明 HDR 不一定总优于 SDR | **S（产品评价）** | 非常适合回答“我们生成 HDR 后用户是否真的觉得更好”；建立 display-aware acceptance criterion | 不是 SDR→HDR GT；更适合 preference/quality 而非训练重建网络 |
| **LIVE-TMHDR** | 15,000 tone-mapped videos；>750k opinions；>1,600 observers | 40 HDR source 经大量 TMO/时序模式/压缩 + expert colorist SDR | **★★★★★** | **S（IQA + 数据）** | 同时用于数据引擎和 tone-mapping quality judge；分析 halo、flicker、过度压缩等 TMO artifact | 主要评价 HDR→SDR tone mapping，不是原生 SDR→HDR |
| **CHUG** | 856 UGC-HDR source → 5,992 videos；211,848 ratings | 真实 UGC HDR source，经多 resolution/bitrate transcoding 模拟社交平台 streaming；AMT 主观打分 | **★★★★☆**；ICIP 2025；第一批大规模 UGC-HDR subjective dataset | **S（IQA）** | 训练/验证 NR HDR-UGC VQA；学习真实消费视频压缩失真 | 不是 SDR/HDR pair；不能直接当 SDR→HDR supervision |
| **BrightVQ** | 300 HDR UGC source → 2,100 transcoded clips；73,794 ratings | HDR UGC 经 bitrate ladder 编码，再 crowdsourcing 收集 MOS | **★★★★☆**；WACV 2026；BrightRate 在其上达到 0.889 SROCC | **S（IQA）** | 评估 HDR-specific + UGC-specific artifact；做 NR VQA baseline | 规模比 Beyond8Bits 小；主要关注转码质量 |
| **HDRSDR-VQA / LIVE Paired Comparison HDR vs SDR** | 960 videos，54 sources；HDR+SDR、9 distortion levels；145 participants；6 台 consumer HDR TV；>22k pairwise comparisons，转换为 JOD | 同内容 HDR 与 SDR 经过 distortion ladder，在多台真实电视上做成对比较 | **★★★★☆**；2025 起的重要 display-aware HDR-vs-SDR benchmark | **S（产品 preference）** | 很适合定义“同内容 HDR 是否真正比 SDR 好”、屏幕依赖与用户收益 | 更偏评价，不给 scene-radiance GT；部分内容版权限制 |
| **Beyond8Bits** | paper-reported ~44k videos / ~6.5k sources / >1.5M ratings；公开版 5,917 source → 41,419 clips，约 1.46M ratings | Crowd iPhone HDR + Vimeo HDR source，经 resolution/bitrate ladder transcoding；AMT 连续评分并用 SUREAL 聚合 MOS | **★★★★★（新但规模领先）**；CVPR 2026；当前最大公开 HDR-UGC subjective 数据之一，整合/扩展 CHUG、BrightVQ | **S（IQA/困难样本）** | 训练 HDR-native VQA/MLLM；构建 hard-case retrieval、版本比较、HDR artifact taxonomy | 不提供 SDR→HDR paired GT；训练 HDR reconstruction 本身价值有限 |
| **ESPL-LIVE HDR Image Quality** | 1,811 processed images；>300k scores；>5,000 observers | 从多曝光 HDR/MEF 图像经 TMO/MEF/post-processing 获得多种结果，再大规模 crowdsourcing | **★★★★☆（经典 HDR-IQA image dataset）** | **B** | HDR/TMO image quality metric sanity-check | 静态图像；不是 video temporal quality |

---

<a id="recommended"></a>
## 6. 对当前 Mobile Same-EV Compressed SDR Video → HDR 的推荐组合

### 6.1 如果目标是“训练一个能跑的 SDR→HDR baseline”

| 优先级 | 数据 | 为什么 |
|---|---|---|
| **1** | HDRTV1K | 有公开 paired baseline，最方便和论文比较 |
| **2** | LIVE-TMHDR | 同一 HDR 有大量不同 TMO 的 SDR，可训练 unknown tone-style robustness |
| **3** | LIVE UGC-HDR → 自建 synthetic SDR | 让 HDR mother content 更接近 consumer/mobile UGC |
| **4** | AIM 2025 | 补单帧 clipping/noise/CRF inverse 能力 |
| **5** | 自采真实眼镜 SDR + teacher/reference HDR | 最终解决 target-domain gap；这是公开数据无法替代的核心 |

### 6.2 如果目标是“验证多帧到底有没有用”

推荐用 **HdM + LiU HDRv** 作为真实 HDR mother video，然后自己生成三组完全可控输入：

```text
A. Fixed-EV
EV0  EV0  EV0  EV0  EV0

B. Smooth AE
0  0  -0.3  -0.5  -0.3 EV

C. Alternating exposure
0  -2  0  -2  0 EV
```

再对比：

```text
Single-frame SDR→HDR
vs
Multi-frame SDR→HDR
```

这比直接拿 DeepHDRVideo/Real-HDRV 更能回答我们当前问题，因为后者天然拥有曝光互补信息。

### 6.3 如果目标是“证明输出 HDR 用户真的更喜欢”

优先：

1. **HDRSDR-VQA / LIVE HDR vs SDR** — 直接研究 HDR-vs-SDR preference 和 display dependency。
2. **xDR** — 用专业 native SDR/HDR grading pair 做 reference comparison。
3. **Beyond8Bits / BrightVQ / CHUG** — 做 HDR-specific artifact / UGC quality judge。
4. **ColorVideoVDP / HDR-VDP-3** — 有可信 HDR reference 时做 FR perceptual evaluation。

### 6.4 我们最建议的数据体系

```text
                         Public HDR source
                ┌──────────────┼──────────────┐
                │              │              │
          LIVE UGC-HDR       HdM/LiU       Professional
             (UGC)          (HDR video)   xDR/HDRMovie
                │              │              │
                └───────┬──────┴───────┬──────┘
                        ▼              ▼
             Multi-TMO / ISP-like     Native pair eval
             degradation engine
                        │
                        ▼
               Synthetic SDR/HDR pairs
                        +
               Real glasses SDR domain
                        │
                        ▼
               SDR Video → HDR Model
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
          FR / paired          NR / preference
      xDR, HDRTV1K, AIM     Beyond8Bits, HDRSDR-VQA
```

### 当前项目建议优先下载/申请的 8 个资源

| 顺序 | 数据 | 角色 |
|---|---|---|
| **1** | **LIVE-TMHDR** | Tone Mapping diversity + expert SDR + subjective quality |
| **2** | **LIVE UGC-HDR** | Consumer HDR mother video，最接近 UGC/mobile 内容 |
| **3** | **HDRTV1K** | 标准 SDR→HDR paired baseline |
| **4** | **HdM-HDR-2014** | 高质量 HDR video mother；做 fixed-EV temporal controlled test |
| **5** | **LiU HDRv** | 补充真实 HDR video scene diversity |
| **6** | **AIM 2025 ITM** | 标准化 single-image reconstruction benchmark |
| **7** | **xDR** | native SDR/HDR grading pair，检查 synthetic→real grading gap |
| **8** | **Beyond8Bits / HDRSDR-VQA** | HDR quality、版本比较、用户 preference 与困难样本挖掘 |

---

<a id="checklist"></a>
## 7. 使用任何 HDR 数据集前必须确认的信息

对每个数据集至少记录：

1. **原始母数据是什么**：真实 scene radiance、HDR master、UGC HDR、专业 grading、还是 synthetic HDR。
2. **SDR 怎么来的**：真实 camera SDR、独立专业 grading、TMO、camera simulation、codec degradation、还是 diffusion/generative synthesis。
3. **HDR GT 怎么来的**：sensor/multi-exposure reconstruction、professional master、teacher output、还是生成模型。
4. **输入是否包含曝光互补信息**：same-EV、AE-varying、alternating exposure、multi-sensor/staggered exposure。
5. **颜色/亮度表示**：linear HDR / OpenEXR / PQ / HLG / Rec.2020 / P3 / BT.709；是否绝对亮度 calibrated。
6. **视频时序是否真实**：逐帧抽样 dataset 不能证明 temporal consistency。
7. **测试 split 是否按 source/video 隔离**：禁止相邻帧/同一母视频跨 train-test 泄漏。
8. **评价任务是什么**：radiometric fidelity、content fidelity、HDR perceptual quality、HDR-vs-SDR preference、还是 compression quality。
9. **公开可获得性与 license**：研究可用不代表商用可用。
10. **与目标眼镜 pipeline 的 domain gap**：camera ISP、AE/AWB、local TM、DNR、sharpen、codec、bit-depth 等是否被覆盖。

---

## Primary sources / project links

- HDRTV1K / HDRTVNet: https://github.com/chxy95/HDRTVNet
- AIM 2025 ITM: https://openaccess.thecvf.com/content/ICCV2025W/AIM/html/Wang_AIM_2025_challenge_on_Inverse_Tone_Mapping_Report_Methods_and_ICCVW_2025_paper.html
- xDR: https://www.sciencedirect.com/science/article/pii/S0923596526000536
- HDRMovieformer: https://ojs.aaai.org/index.php/AAAI/article/view/37578
- LIVE-TMHDR: https://live.ece.utexas.edu/research/LIVE_TMHDR/index.html
- LIVE UGC-HDR: https://live.ece.utexas.edu/research/LIVE_UGC_HDR/index.html
- LumaFlux data pipeline: https://github.com/shreshthsaini/LumaFlux
- HdM-HDR-2014: https://hdm-stuttgart.de/vmlab/hdm-hdr-2014
- LiU HDRv: https://computergraphics.on.liu.se/hdrv_itn_liu/Resources.php
- DeepHDRVideo: https://github.com/guanyingc/DeepHDRVideo-Dataset
- Real-HDRV: https://github.com/yungsyu99/Real-HDRV
- Fairchild HDRPS: https://markfairchild.org/HDR.html
- Sol Levante / Netflix Open Content: https://opencontent.netflix.com/
- LIVE HDR: https://live.ece.utexas.edu/research/LIVEHDR/LIVEHDR_index.html
- LIVE HDR vs SDR: https://live.ece.utexas.edu/research/LIVE_HDRvsSDR/index.html
- CHUG: https://github.com/shreshthsaini/CHUG
- BrightVQ: https://github.com/shreshthsaini/BrightVQ
- HDRSDR-VQA: https://arxiv.org/abs/2505.21831
- Beyond8Bits: https://github.com/shreshthsaini/Beyond8Bits
- ESPL-LIVE HDR: https://www.colorado.edu/lab/live/espl-live-hdr-subjective-image-quality-database
