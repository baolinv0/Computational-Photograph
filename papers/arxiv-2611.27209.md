# Dem2TA: Beyond Pixels, Towards Perception
更新：2026-11-24｜canonical arxiv-2611.27209｜2026-11-20 v1 首传；11-23 arXiv 新公告；首次覆盖 11-24。主 T01；次 T03/T04/X01；角色：重建、任务渲染、训练、评价；GO-E；Bridge + Boundary refinement。
目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)
## 快速回忆
- 一句话：使 Bayer demosaicing 同时受线性 RGB 重建和下游视觉任务监督，再冻结重建部分、学习局部渲染；目标是机器感知，而非人眼审美。
- 旧路线：SegDem (2608.07916) 将语义表征引入去马赛克；本文明确采用该方向预训练基础。TA-ISP (2509.13762) 任务导向渲染、AdaptiveISP、RAW-Adapter 是竞争/互补路线。
- 记忆锚点：任务性能不是线性 RGB PSNR 的单调函数；也不能由相关反例推出降低 PSNR 会提高任务性能。
## 精读记录
- 离线 Stage 1：联合适配 demosaicer 和下游网络，线性 RGB GT 重建、冻结 DINO 表征、任务 encoder embedding alignment、任务损失；WB/CCM/gamma 固定；辅助对齐分支推理移除。Stage 2 冻结 demosaicer，训练局部 tone/color/detail 控制和任务网络；颜色残差在 clipping 前加权亮度为零。
- 在线：Bayer → demosaic → 固定 WB/CCM/gamma → 局部 tone/color/detail → 检测或 box-prompted 分割。不是已经验证的手机实时 ISP。
- 作者 Table 4 COCO segmentation IoU：预训练 76.924、仅适配下游 77.262、联合无表征对齐 77.379、DINO+task 对齐 80.023、完整 81.152；同阶段联合训练 81.047。阶段顺序增量仅 0.105；对齐相对联合无对齐 +2.644。
- Table 1 同 Stage1 frontend，TA-ISP→本文 detection AP 32.282→32.746，IoU 80.096→81.152。Table 2 真实 RAW 100 张（63 Quad、37 single Bayer），1112 个人工复核 SAM3 masks，box-prompted IoU 82.890→83.519。
- Table 3 S 模型线性 PSNR 44.2218→42.7870、IoU 77.064→80.495；L 44.6938→44.7186、IoU 76.924→80.023。下游网络同时更新，不是因果证明。S/L 6.65/33.69M 参数。
## 证据边界
已读 v1 原文（alphaXiv 全文提取）及表 1–4，arXiv 身份核验；无独立复现。真实样本小且有 box prompt，不能当无提示检测、跨相机全面泛化、人眼画质或真实移动部署证据。最小实验：固定数据/下游网络/训练预算，比较冻结 demosaic 仅任务适配、联合训练、表征对齐、局部渲染；分别测真实留出 CFA 的任务指标与 RGB fidelity。代码链接作者声明，未核验运行。
## References
- https://arxiv.org/abs/2611.27209v1
- https://arxiv.org/abs/2608.07916 (SegDem)
- https://arxiv.org/abs/2509.13762 (TA-ISP)
- https://github.com/cipi666/Dem2TA
- [任务导向 RAW ISP](../surveys/task-oriented-raw-isp.md)
