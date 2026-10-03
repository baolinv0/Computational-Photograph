# 历史接入边界与纠错

目录：[接入范围](#接入范围) · [历史已出现清单](#历史已出现清单) · [纠错规则](#纠错规则) · [回填顺序](#回填顺序) · [References](#references)

## 接入范围

2026-10-03 首次建立稳定卡片与 registry。已回填 2026-10-01 主简报的 8 篇论文及 1 条产业线索；**不是此前所有聊天、周报和论文已经全文入库。**原有 `Recent_Papers_2026-09-18.md`、`Recent_Papers_2026-09-19.md`、`HDR/` 和 `AgenticIR/` 保持原样。

下面是当前对话中可见的历史覆盖线索，用于防止再次当成新发现；它们不是已经重新验证的出版记录或事实数据库。标题可能有简称，必须在正式回填时解析 canonical ID。搜索这些对象得到新链接，也不能自动触发新论文通知。

## 历史已出现清单

| 简报日期 | 可见覆盖线索（含部分 Watch） |
|---|---|
| 2026-07-30 | ScaleResfusion；RL-AWB；ID-V2V；FreeShadow；WhereEdit；Beyond Facial Consistency；Zoom-IQA；GigaWorld-1；StatePlay |
| 2026-08-06 | FDIR；DualTSR；Localize, Don't Beautify；ConfBench；FaithIR；MDTD-ArtIR；E2Pano；SelfWAM；Sony–Mitsubishi；S³-Diff；PixelSR |
| 2026-08-13 | ISOCELL HPC/DeepPix；Twilight Cowboy；SegDem；MeanFlow extreme low-light RAW；SPAD noise modeling；VC-Tooler；Open Evaluation Agent；WorldCycle；Sony–TSMC；MotionCraft |
| 2026-08-20 | BinRVR；JPEG AIC2026；High-Flux Count-Free Single-Photon 3D Cameras；TRAIL/Frozen DINO localizes edits；FIT；HarnessEval-W；ConceptEdit-12M；BiCRVC；agent failure detection/repair；Colorist |
| 2026-08-27 | MR-IQA-2；Boundary-Continuous Cross-Camera RGB Mapping；Restoring Without Forgetting；Ordinal Lens Alignment；Information-Optimized Color Metalenses；Depth-Guided Multi-view Exposure Bracketing；Bit Allocation Transfer；UHDformer++；Galaxy S26 FE；VIGIL；AIGIQA |
| 2026-09-03 | Benchmarking RAW and RGB Restoration in ISPs；UEAP-4K；Real-Time Scene-Adaptive Tone Mapping for HDR Object Detection；P-PatchDiff；Cross-Spectral Dense Correspondence；one-step generator reward fine-tuning；SolarWM；Osmo 360 II；Thread-Efficient Neural Texture Compression |
| 2026-09-11 | iPhone variable aperture；PIC；GS-IQA；WorldReward；WeAgent-MMGenEdit；SyncWorld；OracleZoom；MARR；Adreno Neural Fusion；G-NeRV；CF-GAP |
| 2026-09-18 | Visual Autoregressive Priors for RAW-to-sRGB ISP；PULSE；Restore What Matters/JR²；BVB；Dimensity 9600 Pro；HFVQA；GraLoD；VOR-Bench；PhysStream；Qualcomm CAMSS offline ISP；Illusion of Depth |
| 2026-09-25 | RawHDRV；Snapdragon Gen 6 imaging；ImIR；When Visual Quality Misleads；ZoomDiff；HaRP；PrismGPT；InternW0；Paint-Anything；RoomLight |
| 2026-10-01 | 已结构化回填：BAM、ExpandDiff、RelayVSR、FlowTool、The Camera Inside the Editor、Multidimensional Observer Model、Raw Imagery Impacting Your AI、LOCI、Z10。未回填 Watch：ViTeX-Bench、RefGAP、ReCaVSR |
| 跨期专题 | Color Pass-Through via Camera-Display Coupling；DiffRAW；ISPDiffuser；RAW 生成偏色；camera-display；可变光圈 Apple–Huawei 对照 |

这些名单只表示“聊过/出现过”，不表示技术内容、日期和型号都已验证。正式卡片覆盖后，在 registry 建立 canonical alias，不重复创建摘要。

## 纠错规则

1. **旧会论文晚上传 arXiv：**曾把 NeurIPS 2025 的 task-oriented HDR TM 工作当成周新增。正式回填必须先对比会议原文和当前版本，找不到实质差异就只作历史基线。此处记录用户提出的纠错，不冒充本轮重新完成版本比对。
2. **把厂商首次当行业首次：**“自动控制 + Pro UI + API”不能未经横向核验就当 Apple 独有。公司首用、跨生态采用与算法创新是不同事件。
3. **离散先验解释过强：**AR/VQ 中出现颜色问题，不足以证明离散量化是主因；连续 diffusion 也可能出现类似问题。需要 tokenizer 重建、条件不足、目标域和颜色损失等分离实验。
4. **MAC/step/FPS 外推：**理论复杂度不等于运行时；桌面 GPU 不等于手机；模型时间不等于完整端到端延迟。
5. **时间戳机械排除：**接收公告先于 arXiv，不代表新公开全文、代码或数据一定没有价值。必须比较当时实际可访问内容；元数据重现不是实质更新，首次可读全文/首次可执行资产则需要独立判断。
6. **单篇趋势化：**不同论文讨论同一大主题，不等于支持同一具体机制；支持证据和竞争路线要同时保留。

## 回填顺序

先回填需要继续阅读/引用的条目，再处理其所在周报；以原论文/官网重建来源，不把旧助手引用标记当可访问 URL。保留原输出是审计历史，不是自动认可其内容。

未知项入待核验；明确重复或旧论文入不提醒集合；真实新版本通过 material-delta gate 后才允许重新进入周报。未核验原文时不自动同步可能错误的 arXiv ID。

## References

- [归档协议](../ARCHIVE_PROTOCOL.md)
- [结构化登记](registry.json)
- [首批周报回填](../Recent_Papers_2026-10-01.md)
