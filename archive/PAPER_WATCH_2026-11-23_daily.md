# 2026-11-23｜Paper Watch v3.2 静默核验 + T06 历史路线补齐

**裁决：研究通知静默。** 当前成功覆盖的 arXiv 最新新公告仍为 **2026-11-20（星期五）**；相对上一次成功覆盖范围，尚未核实晚于该日期、满足高价值研究门槛的全新论文或影响结论的实质版本。本次仅补先前 backlog 的已公开旧论文；不是新论文、更不是新结果。

## 知识库与实际成功范围

- 首先实际读取本仓库 ARCHIVE_PROTOCOL.md、archive/PAPER_WATCH_V3.md (v3.2)、LITERATURE_MAP.md、archive/LEGACY.md、registry.json、surveys/README.md、11-21/22 daily 及相关 T06 survey；并检索 CameraPaper README 和 AgenticIR survey。
- 官方 [cs.CV /new](https://arxiv.org/list/cs.CV/new)、[eess.IV /new](https://arxiv.org/list/eess.IV/new)、[cs.AI /new](https://arxiv.org/list/cs.AI/new)、[cs.LG /new](https://arxiv.org/list/cs.LG/new) 在本轮访问时均仍显示 **Friday, 20 November 2026**；未把系统日期 11-23 伪装成新的成功公告水位。周末和北京时间星期一上午的新内容可能存在发布/索引延迟。
- 另做 RAW/HDR/ISP/TM、图像恢复/SR/IQA、伪 GT、偏好优化、Agent、多参考图像生成与少步训练的开放关键词检索；相当一部分命中属于历史已归档工作，未达到新证据通知条件。查 AUTOREF 种子 [2609.35530](https://arxiv.org/abs/2609.35530)：本轮没有新的可核验结论改变证据。
- alphaXiv 对 Michael S. Brown、Shuhang Gu、Chao Dong、Jinjin Gu、Junjun Jiang、Weisi Lin、Radu Timofte、Wangmeng Zuo、Lei Zhang、Marcos V. Conde、Andrey Ignatov 十一名核心研究者查询 2026-11-14 之后论文。**索引滞后**已被上轮证实：已收录的 Chao Dong/Jinjin Gu 参与 FA(I)R、Junjun Jiang 参与 ApexFuse 可能不出现在作者页，故十一位作者均标 **partial / metadata lag**，不得说作者无新作；Lei Zhang 同名匹配不可靠。
- 官方分类 /new 成功读取，但没有穷尽 OpenReview 近期更新、作者网页提前公开、GitHub 所有实质 commit 或 arXiv 替换通道；它们仍为 partial/not_checked，不推进成功水位。

## T06 / T02 历史补充：活跃属性与图像载体不能混为一谈

[TRACE: Attribute Execution for Sequential Image Editing](../papers/arxiv-2611.25648.md)（Xiyang Zhang 等）arXiv **2026-11-19 v1**，已在上一成功覆盖的 11-20 公告窗口中列为 candidate backlog，于 11-23 补全文选段入库。**类型 backfill；非 New / Update；first_covered=2026-11-23**。主 T06、次 T02/T03/T04；角色：持续目标、候选执行、检查；**PROBE / Bridge + Boundary refinement**。

抽象：在连续编辑中保留属性（如“蓝色”）而不是复制承载该属性的旧表面（如“玻璃”），当前已变金属时，应在金属图上局部回写历史色彩，材质缺失才考虑额外采样生成当前 carrier。原文 §3–4 和 Table 1/2/4、Supplement S1/S2 证据：窄 color–material both 96/108 vs all-history 83/108；固定 proposal 8B 目标盲读 21/112 历史像素→26/112 历史 chroma→41/112 TRACE；但**完整 EdiVal 的 Core→TRACE 第三轮 IF 30.77%→31.12%，source-disjoint Klein 60/125 低于 Core 63/125**。说明局部操作是适应某类属性冲突的机制，不代表通用多轮恢复已突破。没有真实 IR 物理保真/跨手机或完整 E2E 对等预算证明。

旧路线对比：MT Forcing/TailSteer 是训练期抑制累计漂移；ReSpec/SEAM 是历史目标/证据取用；ROI compositing 是像素保护。TRACE 新增的是 *goal-state → carrier-qualified local operation* 接口，不能说它直接继承前两篇的训练机制。在线冻结编辑器 + ROI Oklab/新 carrier 生成 + complete-request check；离线无需再训练编辑器。最小等预算实验与反例在 [T06 living survey](../surveys/multi-turn-editing-preservation.md)。**既有真实恢复与 ISP 执行决策不变**。

## 归档状态与 backlog

- GitHub 更新/创建的 canonical [TRACE card](../papers/arxiv-2611.25648.md)、既有[多轮编辑 survey](../surveys/multi-turn-editing-preservation.md)、[LITERATURE_MAP](../LITERATURE_MAP.md)、[surveys 索引](../surveys/README.md)；没有复制 CameraPaper 已有 AgenticIR 大综述，也没有公开私人项目细节。
- alphaXiv 检查 2611.25648 无已有 membership 后，已保存至 **Agent** 主主题并再次查询确认；不更改 Want to read / Reading / Completed。
- 保留 backlog：Life-IQA+ v1/v2 的真正新增实验归因、TRACE 对真实用户完整对话的人评、OpenReview 原始提前公开验证，及 AUTOREF 多参考模型级 harness 上的独立实际复现。
- 本轮不新增另一套报告任务、不修改已有定时任务/通知设置。

## 一手来源

- [arXiv cs.CV /new](https://arxiv.org/list/cs.CV/new)
- [arXiv eess.IV /new](https://arxiv.org/list/eess.IV/new)
- [TRACE v1 原文](https://arxiv.org/html/2611.25648v1)
- [TRACE identity/date](https://arxiv.org/abs/2611.25648)
