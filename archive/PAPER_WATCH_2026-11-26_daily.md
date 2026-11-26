# Paper Watch v3.2 — 2026-11-26
## 检索水位与结果
上轮已验证官方新公告 2026-11-24（见 11-25 daily）。本轮 cs.CV、eess.IV、cs.AI、cs.LG /new 均显示 2026-11-25，分别列 459、20、447、391 项，采用关键词定位 RAW/HDR/AWB/TM、restoration/SR/enhancement、IQA/reward、PGT、editing/multi-reference/Agent 与效率，加主题开放搜索；未逐一全文筛查全部条目/替换版本。核心作者 alphaXiv 批检覆盖 11-17 之后的 Michael S. Brown、Shuhang Gu、Chao Dong、Jinjin Gu、Junjun Jiang、Weisi Lin、Radu Timofte、Kai Zhang、Yulun Zhang、Qingsen Yan、Ying Fu；索引可能延迟且同名消歧不充分，不能据此推进作者个人页面水位。开放搜索与分类公告水位分别记录。
## New：两篇 v1（2026-11-24 提交；11-25 新公告；11-26 首次覆盖）
- [MAGPIE](../papers/arxiv-2611.32462.md)，T06/T02/T04/T05/X01，GO-E，New route + Boundary refinement。[多参考可执行空间控制](../surveys/multi-reference-executable-scene-control.md) 是新独立专题；Scone、AutoRef、Code-as-Room 为历史锚点（机制关系/竞争而非自动继承）。DreamOmni2 Qwen base42.01→proxy-only29.47→full64.26，表明几何中间表示有价值但不能替代执行器适配。FLUX 标准SFT48.90/full67.08；固定adapted executor 0/3/6轮53.61/61.13/67.08。候选代理验收不等于像素事实正确；几何控制不外推纯外观恢复。
- [HazeFlux](../papers/arxiv-2611.32632.md)，T03/X01/T05，GO-E，Engineering maturity + Boundary refinement。[高效生成式恢复](../surveys/efficient-generative-restoration.md) 追加任务适配与源图旁路路线；Merge-HAZE 11.94→20.61→20.98 dB，I-HAZE adapter后退化，主要收益来自任务LoRA而非decoder；须做同参数普通decoder/简单频域融合对照。
两者均为作者实验；首次公开下限为arXiv v1，精确题名搜索未见更早公开全文，作者主页与OpenReview不穷尽。无独立复现。
## 分开记录：历史回填、纠错、待核验
本轮 Scone/AutoRef/Code-as-Room/HNDiff/DehazeXL 为旧锚点，按原始摘要及可访问章节核查后接入专题，不重复算新增或收藏；本轮无独立历史卡片或纠错写入。GRUN（2611.31690）需核验逐任务权重与通用模型含义；Nemotron-Labs-VisualCreation（2611.31358）需查更早发布与本次技术增量；Every Edit Its Own Budget（2611.32407）需全文核验等预算基线与保真。未推进这些候选为正式推荐。全量替换版本、个人主页/OpenReview仍未穷尽；不依据运行时间补写成功水位。
## 实际归档回执
两份 canonical card、新建多参考专题、修订高效生成恢复专题、总地图、专题索引、README、CameraPaper 既有 AgenticIR 主综述交叉链接均写入并逐份精确读回；alphaXiv 先查 membership，再新增 MAGPIE→Agent、HazeFlux→Restoration 并重新查证，未更改阅读状态。Registry 与本记录作为本轮最后的提交，需分别读回确认。无私人项目数据入库。
