# 2026-11-22｜Paper Watch v3.2 静默复核与历史补发现

状态：**没有通过「相对上次成功检查产生新研究/实质更新」门槛的证据**。此页为真实执行覆盖台账，不是当日研究通知；不推进未实际覆盖的来源水位。

## 先恢复
- 已读取 [协议](../ARCHIVE_PROTOCOL.md)、[v3.2 执行规则](PAPER_WATCH_V3.md)、[文献总图](../LITERATURE_MAP.md)、[历史纠错边界](LEGACY.md)、[registry](registry.json)、[surveys 索引](../surveys/README.md)，并核对 2026-11-21 日更归档。
- 上次成功公告已覆盖 **2026-11-20**（arXiv 2026-11-19 首传文献、5篇选定）；不能以当前定时任务的执行时间伪造搜索覆盖。
- 今日实际检查 [arXiv cs.CV /new](https://arxiv.org/list/cs.CV/new)、[cs.CV pastweek](https://arxiv.org/list/cs.CV/pastweek?show=2000)、[eess.IV /new](https://arxiv.org/list/eess.IV/new)、[cs.AI /new](https://arxiv.org/list/cs.AI/new)：均显示最新公告为 **Friday, 2026-11-20**，暂无随后周末独立的新公告。日公告、7天重叠窗口的同ID/版本去重以官方来源为准。
- 开放检索涵盖 RAW/HDR/TM/ISP、去噪/SR/Agent/IQA/数据监督、AUTOREF 多参考、扩散训练与少步蒸馏；独立按 Michael S. Brown、Shuhang Gu、Chao Dong、Jinjin Gu、Radu Timofte、Weisi Lin 等作者检索。搜索引擎不能保证作者主页及 OpenReview 全覆盖，作者级状态为 **partial**，不推进为“已穷尽”。
- 已核验上一轮五篇（FAIR、RegionAgent、AesDistill、ApexFuse、LG-FiLM）仍为 2026-11-19 arXiv v1，无可核实的结论性版本增量；原有注册条目保持不动。
- AUTOREF arXiv 2609.35530 v1 是 2026-09-28 旧种子。 [官方代码库](https://github.com/KuOnoda/AutoRef) 最近可访问提交为 2026-09-29 的 README 文档修订；没有证据表明 11-21/22 发布了改变结论的版本。不因本次新发现旧页面触发通知。

## 历史补发现与持续专题（非 New）
- [PMD / Posterior Matching Distillation](../papers/arxiv-2611.26629.md)，arXiv v1 于 **2026-11-19** 首次提交，属于**上次成功公告窗口内的旧文新发现**。主 X01、次 T03/T05，系统角色：离线训练；裁决 WATCH、No material map change / Boundary refinement。原文 §1–5、Table 1–2、Appendix E 已读取。它更好保持一般文生图后验多模态，但 PMD-only 质量严重退化、需要 GAN；既没有图像恢复 LQ 条件，也没有真实端侧 ISP 证据。
- 在[高效生成式恢复 living survey](../surveys/efficient-generative-restoration.md) 更新蒸馏路线比较（轨迹/端点 vs 生成边缘分布 vs 条件后验），并在[总图 X01](../LITERATURE_MAP.md)补充适用边界。**非实质研究新发布**，没有改变产品或研究执行决策，也不应同步 alphaXiv（WATCH）。
- 候选 eDMD、Life-IQA+、TRACE 等维持历史/前轮 backlog，不能仅凭今日再检索当作新作。论文页首传和版本不变不足以触发更新通知。

## 仍未覆盖
- 尚未逐篇穷尽 OpenReview 所有投稿、全部核心学者个人主页和 GitHub 所有代码，搜索结果可能滞后；这些来源标 **partial/unverified**，不能声称没有任何研究。
- 今日官方 arXiv 分类无晚于 11-20 的新公告，故不创建虚假的 11-21/22「新」论文，不升级作者论文指标为独立复现。

## 原始来源
- [arXiv cs.CV 最新公告](https://arxiv.org/list/cs.CV/new)
- [PMD 原文 v1](https://arxiv.org/html/2611.26629v1)
- [DMD2 NeurIPS 2024 官方论文](https://proceedings.neurips.cc/paper_files/paper/2024/hash/54dcf25318f9de5a7a01f0a4125c541e-Abstract-Conference.html)
