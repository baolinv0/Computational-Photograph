# Paper Watch Topic Update｜2026-10-24

目录：[本轮判断](#本轮判断) · [三篇新论文](#三篇新论文) · [主题地图变化](#主题地图变化) · [发现与核验范围](#发现与核验范围) · [归档回执](#归档回执)

## 本轮判断

2026-10-22 arXiv v1 初次提交的三篇新工作改变了三个相互关联但不能混用的判断：

1. **T03/X01**：生成式低光增强可以在特定条件下把采样变成 1 NFE，核心取舍从步数扩展到 latent、训练目标和真实质量/成本 Pareto；不意味着全面取代判别式低光增强。
2. **T02/T06**：一步编辑不一定需要两个时间噪声状态；一个共享状态可以同时得到局部语义切向和端点校准，但限制于 epsilon VP 一步模型。
3. **T06/T04**：使用下游 3D 任务定义净化监督可以改进几何，但新路由器在真实照片的 proxy label 协议中未优于 always-PURIFY，证明“净化器有效”和“路由有效”必须分开。

无论文被声称已经独立复现或手机端部署。

## 三篇新论文

| 论文与团队 | 首次可核验版本日期 | 所在路线/变化 | 最重要证据及反例 | 裁决/链接 |
|---|---|---|---|---|
| GLOW-FM — Ariel Lapid 等，Arm AI Research | 2026-10-22，arXiv v1 | T03 + X01：高效 latent TVM / Engineering maturity | GLOW-FM-S 1 NFE / 34 GFLOPs / 9.1M，LSD-DLL PSNR 19.7；XL 同任务 20.3 但 48 GFLOPs。UHD-LOL4K PSNR 弱于一些非生成基线；无手机实测 | GO-E；[card](papers/arxiv-2610.31222.md) |
| One Evaluation Is Enough (ECT) — Lifan Jiang 等，浙江大学/蚂蚁集团 | 2026-10-22，arXiv v1 | T02/T06：单时刻端点校准 / Boundary refinement | PIE-Bench SD-Turbo 背景 PSNR 22.63→23.74，核心时延 0.265→0.212s（H20）；CLIP 略退；只支持 epsilon VP 一步骨干 | PROBE；[card](papers/arxiv-2610.30827.md) |
| Gate3DGen — Xiaolin Li 等，清华大学/华为 | 2026-10-22，arXiv v1 | T06/T04：KEEP / PURIFY 与任务效用 / Bridge & Counter-evidence | 合成 3D Mesh Distance 1.984→0.764（×10⁻³）；真实路由 accuracy=58.33%，与 Always-PURIFY 的 proxy accuracy 一样，且下游任务非手机拍照 | PROBE；[card](papers/arxiv-2610.31649.md) |

## 主题地图变化

- [高效生成式恢复：采样步数、潜空间与质量成本](surveys/efficient-generative-restoration.md) — 新建并对照 GLOW-FM、ELIR、ReDDiT、WCDM、判别式基线，前序逐篇核验 backlog 已记录。
- [一步免反演图像编辑：时间控制与空间控制](surveys/one-step-inversion-free-editing.md) — 新建并区分 ECT、ChordEdit、ER-Chord 的具体优化变量。
- [选择性恢复与下游任务效用](surveys/selective-task-aware-restoration.md) — 新建并明确 KEEP baseline 和真实域路由失败证据。

未在本轮重新验证全文的旧锚点只是历史背景，不计为新论文，不新增 alphaXiv 收藏。GIGABENCH（arXiv:2610.31644）经过原文选段检查：10 个 gigapixel 场景比较神经表示、压缩和 SR，具有跨尺度背景研究价值，但与移动影像 4K 可部署恢复不直接同条件；暂列 WATCH，不触发本期新论文推荐或归档，不将新发现等同新技术突破。

## 发现与核验范围

- **时间边界**：论文首页 arXiv v1 均为 **2026-10-22**，本次检查 **2026-10-24**。此前 2026-10-23 新论文通知所列 2610.29xxx 等不当作新作。
- **实际成功来源**：alphaXiv topic discovery with `published_after=2026-10-22` + 原 PDF 全文提取（新作3篇；另 GIGABENCH 测试对象）。
- **失败/未知**：arXiv `/list/cs.CV/new` 和 `eess.IV/new` 通过网页工具命中**过期的 2026-08-10 快照**；对 2026-10-23 按日列表的直接网页请求失败。故**不能宣称整个 cs.CV/eess.IV 逐条检查完毕**，也不能把来源覆盖水位推进到完整 2026-10-23。其他核心作者未逐位重查；保留残余漏检风险。
- **核验层级**：三篇均检查提取的 arXiv v1 原文方法、主要实验与失败条件，但并非逐图完整审计/独立复现。GIGABENCH 只作为背景候选，证据范围不支持本轮强推荐。
- **争议边界**：NR-IQA vs 真实保真；一时刻 vs 多分支计算；任务净化器效果 vs 路由增益；不同 backbone/resolution/compute 无法直接排名。

## 归档回执

本期新增 3 篇 canonical 论文卡片、3 个持续主题综述；更新 [总图](LITERATURE_MAP.md) 和 [surveys/README](surveys/README.md) 等入口；alphaXiv 三篇各保存到一个主题文件夹且已回查会员关系（GLOW-FM: Restoration，ECT: Agent，Gate3DGen: Restoration）。

本期没有修改先前已发表旧卡片和研究结论。**Notion 和 CameraPaper 的下游同步需单独以写入读回为准；没有回执不得当成功**。

## 原始入口

- [GLOW-FM](https://arxiv.org/abs/2610.31222v1)
- [One Evaluation Is Enough](https://arxiv.org/abs/2610.30827v1)
- [Gate3DGen](https://arxiv.org/abs/2610.31649v1)
