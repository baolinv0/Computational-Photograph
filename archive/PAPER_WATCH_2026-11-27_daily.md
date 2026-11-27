# Paper Watch v3.2 — 2026-11-27
## 检索范围
前一轮本任务成功核验的官方公告 2026-11-25；本次 cs.CV/eess.IV/cs.AI/cs.LG /new 显示 11-26，分别402/16/398/419项；关键词定位（非全部逐篇全文）覆盖 RAW/HDR/ISP/TM、恢复/SR/增强、IQA/Reward、参考编辑、PGT、Agent及效率；开放搜索与日公告分开。今日另有周报（已核 README/Recent_Papers_2026-11-27 和 registry），其6篇已归档新作不重复推荐。本次 LayoutRecall 位于11-26公告且未在此前日更/今日周报条目或registry出现；属于本任务新公告补充，而不是旧月份回填。
核心作者 alphaXiv 重叠 11-18 起：Michael S. Brown、Shuhang Gu、Chao Dong、Jinjin Gu、Junjun Jiang、Weisi Lin、Radu Timofte、Kai Zhang、Yulun Zhang、Qingsen Yan、Ying Fu 均实际请求；仅Kai Zhang匹配索引返回 VADE（非目标成像任务）。索引未返回已知 FAIR/RegionAgent，故该作者源 partial，不推进个人主页或全作者水位。OpenReview、全部替换版本与原始个人主页未穷尽。
## 新证据
[LayoutRecall](../papers/arxiv-2611.33885.md) — 11-25首传 v1、11-26公告；T06主，T02/T03/T05/X01，GO-E Bridge/Boundary refinement。对象局部3D表面作为历史appearance索引、适配执行器。LayoutLoop 十轮 full/last2/no mem Back=23.75/19.18/15.71dB；真实10条序列且无真实目标GT；同历史token预算的无几何检索尚欠。主[可执行空间控制](../surveys/multi-reference-executable-scene-control.md)，交叉[多轮保真](../surveys/multi-turn-editing-preservation.md)，总图T06更新。证据仅作者报告。
## 历史回填与未完成项
[AutoRef](../papers/arxiv-2609.35530.md) 9-28旧v1，之前已覆盖，新增canonical而非新论文。Table4等生成预算的complaint revision消融已存在（7.37→6.99），仍欠具体错误纠正率；Appendix I Qwen五参考负例。BoxCtrl与Thinking in Boxes 原始摘要/项目回溯进入路线表，未重建全文。SIA 2611.33894 有SIGGRAPH Asia会议先例需核最早公开及同等选择控制基线；RelPRM 2611.33903 为相邻视觉推理奖励，非图像恢复实证；DocDUR-Net、TORE、X-Matte 为候选未完成原文审查。Multidimensional Observer Model 2609.38487 replacement 条目可见，但abs/html原文访问失败，实质更新未判定，待补查，不以失败视为无新增。
## 回执
LayoutRecall及AutoRef canonical、主survey、交叉survey、总图、survey索引逐份写入并精确读回。alphaXiv两篇此前无membership，新增至既有Agent并核验，未更改阅读状态；AutoRef为历史漏归档补齐。Registry及本日记录分别写入读回；无私人项目数据。未做独立实验/复现。
