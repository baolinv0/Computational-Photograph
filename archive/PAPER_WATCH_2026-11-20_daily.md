# 2026-11-20｜Paper Watch v3.2 日常增量（与现有周度快照区分）

本次复核官方arXiv 2026-11-19新公告（2026-11-18首次上传）与现有registry；周度研究任务已经归档同日五篇（Joint RAW、PrismRestore、DetailScale-SR、ALIVE、GRAM），本快照**不重复登记/推荐**。本次独立追加1篇新机制与1篇旧路线重大扩展。未独立复现。

| 类型 / 首次可核验公开 | 主/次主题与角色 | 裁决与实际地图变化 | Canonical |
|---|---|---|---|
| **New** 2611.23889 / arXiv 2026-11-18 v1 | T03 / T05/T06；退化测量/执行/训练 | PROBE；New route+Boundary refinement；静态状态τ与interventional probing增益必须拆分 | [PROBE复合退化](../papers/arxiv-2611.23889.md) |
| **Material Update / major extension** 2611.24023 / arXiv 2026-11-18 v1；直接前作STAR 2025-07-22 | T03 / T01/T05/T04；数据/物理目标/评价 | GO-E；Engineering maturity + Boundary refinement；STAR单滤镜→36滤镜+FAA/SADL，未见滤镜泛化 | [STAR++](../papers/arxiv-2611.24023.md) |

## 主题判断
T03复合恢复：从因子识别/静态组合→状态条件交叉响应，作者CD11 30.77dB/0.898，CART29.95/0.894；关键同骨干τ+ΔD 30.63，full30.77。**当前不替换通用ISP/Agent模块**。主survey：[统一退化路由](../surveys/universal-restoration-degradation-routing.md)。

T03物理SR：从2025STAR单滤镜flux约束→2026 STAR++跨滤镜数据规模与条件建模；七未见滤镜×2 PSNR 35.42/FE0.4341 vs 同扩展数据 FISR34.32/FE0.5304。**合成LR≠真实跨仪器实测**。主survey：[光度保真](../surveys/photometric-fidelity-and-cross-filter-super-resolution.md)。两条路线不是可验证的同一技术栈。

## 排除、历史和覆盖
- HHW-Ego arXiv 2611.24010 2026-11-18提交，但同题ICLR2026 OpenReview更早公开版本已可检索；本轮不当新作。新v1声称5000组 vs 早期hundreds，但真实多源配对质量及公式需继续核验后方可考虑重大更新；额外物理争议：仅对XYZ乘同一标量不能直接修正色度/CCT。**WATCH / chronology pending**，不计新增通知、不收藏。
- CoScan 2611.23717有先期会议材料，未找到新实质差异；不通知。
- 已检查官方cs.CV/cs.LG/cs.AI/cs.MM/eess.IV/eess.SP 2026-11-19列表及7日重叠、αXiv核心作者Michael S. Brown/Shuhang Gu/Radu Timofte/Chao Dong/Weisi Lin/Junjun Jiang/Lei Zhang/Jinjin Gu/Yan Lu自11-12索引，独立按问题检索并抽查方法、消融、同机制前序。作者索引可能姓名歧义和时滞，OpenReview全量与个人主页仍不完整，不能把访问失败写成无新增。
- 先前 STAR 2025仅历史锚点（非新作）；两篇本轮新卡选段核验与原作者报告，尚未独立复现。
- 源入口：[官方cs.CV 11月19日新公告](https://arxiv.org/list/cs.CV/new)、[arxiv PROBE v1](https://arxiv.org/html/2611.23889v1)、[STAR++ v1](https://arxiv.org/html/2611.24023v1)、[旧STAR 2025](https://arxiv.org/abs/2507.16385)、[OpenReview HHW-Ego先期稿](https://openreview.net/pdf/6ff61aab43af0ce28bba8946b737118c5c433c7b.pdf)。

## 归档
已更新唯一卡片、主survey、LITERATURE_MAP和索引；registry及alphaXiv保存状态以实际后续读回为准。不得把此日更快照误认为原有 [2026-11-20周度研究快照](../Recent_Papers_2026-11-20.md) 已被修改。
