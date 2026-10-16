# 2026-10-16 周报快照

> 窗口：2026-10-09 09:08—2026-10-16 09:08（Asia/Shanghai）。这里只记录当周决策变化；技术正文维护在 canonical cards。

## Executive Decision

本周最值得行动的是三个系统边界：空间曝光控制要求传感器读出配合；双摄融合必须显式建模跨镜头不可靠区域；恢复/编辑 agent 开始把“执行前预测”和“提交/回滚”作为一等接口。证据仍主要是作者实验，手机端时延、功耗、热和跨传感器泛化普遍缺失。

## 选择与评分

| 项目 | 类型 | E/T/S/A | 加权分 | 本周决策变化 |
|---|---|---:|---:|---|
| [PreActIR](papers/arxiv-2610.20384.md) | Restoration agent | 4.4/4.7/4.7/4.4 | 4.57 | 新：执行前世界模型 + 独立 commit/rollback；公开实现，但 matched replay 不是无参考部署 |
| [BluePixel](papers/arxiv-2610.19882.md) | Editing / industry paper | 4.5/4.6/4.6/4.1 | 4.50 | 新：公开 native-4K 训练、4-step 蒸馏与 agent harness；服务器 XPU 非手机证据 |
| [Neural Block-wise AE](papers/arxiv-2610.18733.md) | Camera / AE / HDR | 4.2/4.6/4.6/3.7 | 4.35 | 新：16×16 空间曝光预测；硬件可分区曝光是前置条件 |
| [Physics-Shaped, Not Physical](papers/arxiv-2610.19763.md) | Negative / restoration audit | 4.5/4.3/4.3/4.2 | 4.35 | 新：最终恢复收益与物理中间量有效性必须分开证明 |
| [DuSRFlow](papers/arxiv-2610.14630.md) | Multi-camera / SR | 4.1/4.4/4.5/4.0 | 4.28 | 新：专用双摄流 + 可靠性互补 warping；Huawei 论文时署名 |
| [OLiVES](papers/arxiv-2610.20501.md) | Low-light video benchmark | 4.4/4.3/4.2/3.9 | 4.24 | 新：同步成对动态视频 + segmentation；ND 白天模拟不等于真实夜景 |
| [ScenePercept](papers/arxiv-2610.17661.md) | IQA / preference | 4.1/4.2/4.4/3.8 | 4.17 | 新：场景—属性—总分结构；需防语义偏好吞没物理失真 |

## 产业支持证据

- [OPPO Find X10 全球版样张](https://www.gsmarena.com/oppo_find_x10_pro_max_and_find_x10_camera_samples-news-75035.php) 将证据从官方规格推进到媒体实机样张，但完整评测仍未发布。
- [iPhone 18 Pro 摄影评测](https://amateurphotographer.com/review/iphone-18-pro-review/) 提供可变光圈、手动控制和焦点跟踪的操作观察；光学与计算景深贡献仍未分离。
- OPPO 10 月 13–14 日 LUMO / DeepPix / O-Log2 官方披露已由 daily intake 先通知，本周只作支持证据，不重复标新。

## Watchlist

- [Recovery-Oriented Optical System Design](https://arxiv.org/abs/2610.17950)：Fisher-information 可恢复性目标有方法价值，但当前仅模拟镜头、两张测试图和固定 AWGN；出现实物手机模组或跨噪声/场景验证再升级。
- [WorldMemBench](https://arxiv.org/abs/2610.19063)：适合观察身份/场景记忆，但与低层成像的直接决策距离较远；数据与脚本可用性、跨模型复现后再升级。
- [PhyMetric](https://arxiv.org/abs/2610.19823)：场景级物理 QA 有潜力；代码/数据链接完整可用且 judge 偏差审计后再升级。

## 审计

- 新增 canonical cards：7；carry-over headline：0。
- 论文均核对 arXiv v1 与当前版本；未把 QK-Edit 的 2026 arXiv 上传误标为新研究（同题同作者已见 ICCV 2025）。
- 公司归属仅记录论文首页明确署名；设备/数据集使用不算公司作者。
- 覆盖包含直接成像、恢复、编辑、IQA、agent 与产业；未检出足够强的新 AF/AWB/demosaic/burst 条目，不以弱项补齐数量。
