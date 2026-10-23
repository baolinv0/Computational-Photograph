# 2026-10-23 周报快照

> 窗口：2026-10-16 09:08—2026-10-23 09:25（Asia/Shanghai）。10 月 13–16 日仅作三日重叠去重；技术正文维护在 canonical cards。

## Executive Decision

本周应优先投入“可测边界”而不是更大模型：RAW 曝光恢复需要把可逆增益与不可逆饱和分开；生成式 SR/编辑需要事实型 hallucination 与长程漂移评价；CameraX 把低光补光、物理镜头选择和资源生命周期变成可回归的系统接口。论文证据仍以作者实验为主，手机端功耗、热、跨传感器与真实运动覆盖普遍不足。

## 选择与评分

| 项目 | 类型 | E/T/S/A | 加权分 | 本周决策变化 |
|---|---|---:|---:|---|
| MESS | ISP / enhancement data | 4.6/4.6/4.7/4.3 | 4.59 | RAW→MES→500K RGB 训练对；真实跨手机物理一致性仍待验证 |
| CameraX 1.7.0-rc01 | Camera API / industry | 4.8/4.0/4.7/4.8 | 4.57 | 低光补光 last-setting-wins、物理镜头绑定与 Surface 修复 |
| RIECR | RAW exposure | 4.5/4.7/4.7/4.1 | 4.55 | 统一欠曝/过曝 RAW，但完全饱和仍不可逆 |
| Face Contrast | Color / IQA | 4.4/4.4/4.7/4.1 | 4.45 | 29 手机、508 图的人脸三维对比度；真人/跨文化外推有限 |
| WorldSR | Restoration / agent | 4.2/4.7/4.6/3.8 | 4.39 | 显式实体检索约束 SR；NR-IQA 不证明事实细节 |
| CheckDistill | IQA / reward | 4.3/4.5/4.5/4.0 | 4.37 | checklist 蒸馏到短输出 reward；共同 judge 偏差未排除 |
| MT Forcing | Editing / agent | 4.4/4.5/4.4/4.0 | 4.37 | 自 rollout + 单轮 teacher；八轮小基准不等于长程保证 |
| OPPO Find X10 global | Product / review | 4.6/3.8/4.5/4.5 | 4.36 | 正式发布与 Blackmagic 11 月边界；完整评测暴露高分辨率/防抖取舍 |
| VHA | IQA / negative | 4.3/4.3/4.4/3.9 | 4.25 | 问答式 SR hallucination 审计；依赖 GT |
| S3D-Mosaic | Sensor / demosaic | 4.0/4.4/3.9/3.6 | 4.01 | MSFA 结构迁移；不能外推手机 Bayer |

## Canonical cards

- [RIECR](papers/arxiv-2610.28191.md)
- [MESS](papers/arxiv-2610.24680.md)
- [S3D-Mosaic](papers/arxiv-2610.24414.md)
- [Face Contrast](papers/arxiv-2610.26517.md)
- [WorldSR](papers/arxiv-2610.28423.md)
- [CheckDistill](papers/arxiv-2610.26740.md)
- [MT Forcing](papers/arxiv-2610.25404.md)
- [VHA](papers/arxiv-2610.25770.md)

## 产业支持证据

- [CameraX 1.7.0-rc01](https://developer.android.com/jetpack/androidx/releases/camera)：Google 2026-10-21 发布 RC；这是开发库变化，不是 Pixel 固件或新 ISP。
- [OPPO Find X10 全球发布](https://www.oppo.com/en/newsroom/press/oppo-find-x10-series-global-launch/)：Blackmagic 合作版本官方写明 11 月可用，不能称本周已部署。
- [GSMArena 完整评测](https://www.gsmarena.com/oppo_find_x10_pro_max-review-3008p5.php)：补出 26MP/12.6MP/2×细节与平移稳定边界；不能反推唯一 ISP 原因。

## Watchlist

- [RoboPhoto-VLA](https://arxiv.org/abs/2610.26287)：600 demonstrations/42 instructions 的机器人摄影问题新颖，但评价依赖预训练 aesthetic/quality scorers；出现真实用户盲评、代码与跨场景复现后升级。
- [FlashReFocus](https://arxiv.org/abs/2610.23297)：交互重聚焦工作流有价值，但仓库仍写自家核心权重待发布；完整资产和真实遮挡失败率可验后升级。
- [OverSeer](https://arxiv.org/abs/2610.28554)：多 agent 辅助视角 world model 有方向性；真实多机只定性，远离辅助相机仍不一致。

## 审计

- 新 headline：10（8 篇新论文 + 2 个产业项）；carry-over：0。OPPO 10 月 14 日机制与 10 月 21–23 日每日评测已对账，不重标技术首发。
- 论文均核对 arXiv v1/current version；MT Forcing 记录 v2，未把普通版本更新另算新研究。
- 覆盖直接成像/传感器 3，恢复 2，tone/color 1，IQA/evaluator 3，agent 2，产业 2；同一项可跨类，未检出足够强的新 AF/AWB 专项。
- 所有论文未独立复现；MAC、服务器 GPU/权重尺寸不作为端到端手机证据。
