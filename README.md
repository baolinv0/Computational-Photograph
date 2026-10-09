# Computational-Photograph｜计算摄影研究库

目录：[怎么使用](#怎么使用) · [主题入口](#主题入口) · [周报快照](#周报快照) · [归档机制](#归档机制) · [既有资料](#既有资料) · [References](#references)

## 怎么使用

先看每篇卡片的“快速回忆”，再按需展开“精读记录”。**收藏不等于已读，摘要核验不等于全文验证，作者实验不等于独立复现。**论文正文只维护一份；周报记录当时的变化和链接。

本仓库存通用研究技术笔记；厂商归属、产品/专利和竞品证据进入 [CameraPaper](https://github.com/baolinv0/CameraPaper/blob/main/WEEKLY_ARCHIVE.md)。Notion 作为私有阅读入口，alphaXiv 收藏原论文。

## 主题入口

### ISP / 成像逆问题

- [BAM：显式成像算子 + 少步后验采样](papers/arxiv-2609.39660.md)
- [RawVLA：任务目标反向约束显式 ISP](papers/arxiv-2609.37530.md)

### RAW / 传感器 / 任务成像

- [Raw Imagery Impacting Your AI：SNR/MTF/分辨率到检测效用](papers/arxiv-2609.38265.md)
- [Dense Illuminant：物理合成的密集多光源监督](papers/arxiv-2610.06508.md)

### HDR / Tone Mapping

- [ExpandDiff：双端裁剪分布与 HDR 重建](papers/arxiv-2609.39624.md)
- [FLASH：时序 HDR 跨曝光脉冲光攻击](papers/arxiv-2609.37742.md)
- [既有 HDR 专题资料](HDR/)

### 恢复 / 视频 / 参考传播

- [RelayVSR：稀疏生成参考与逐帧轻量恢复](papers/arxiv-2609.37850.md)
- [HarnessIR：MFM executor + verification 的真实恢复](papers/arxiv-2610.10133.md)
- [LoopMoEVR：循环 MoE 的统一 UHD 恢复](papers/arxiv-2610.05109.md)

### 编辑 / Agent / 可控渲染

- [FlowTool：连续参数与离散工具选择的边界](papers/arxiv-2609.35673.md)
- [The Camera Inside the Editor：几何保真评价](papers/arxiv-2609.37732.md)
- [ARRO：结构化最小改动 reward](papers/arxiv-2610.06021.md)
- [UniSlider：感知均匀的连续编辑校准](papers/arxiv-2610.06831.md)
- [既有 AgenticIR 资料](AgenticIR/)

### IQA / 观察者

- [Multidimensional Observer Model：任务相关感知子空间](papers/arxiv-2609.38487.md)
- [EditJudgeBias：编辑评审器的顺序与线索偏置](papers/arxiv-2610.01670.md)

### World Model / 时序状态

- [LOCI：几何条件化混合记忆](papers/arxiv-2609.40222.md)

## 周报快照

- [2026-10-09：任务导向 ISP、恢复 agent 与 evaluator 风险](Recent_Papers_2026-10-09.md)
- [2026-10-01：首批回填，2026-10-03 核验](Recent_Papers_2026-10-01.md)
- [2026-09-19：既有笔记，未在本次重新核验](Recent_Papers_2026-09-19.md)
- [2026-09-18：既有笔记，未在本次重新核验](Recent_Papers_2026-09-18.md)

## 归档机制

- [ARCHIVE_PROTOCOL：源头核验、职责、去重、同步与通知](ARCHIVE_PROTOCOL.md)
- [registry.json：稳定身份、证据范围、结论 key 与增量事件](archive/registry.json)
- [LEGACY：历史已出现对象与纠错边界](archive/LEGACY.md)

同一论文新版本只更新原卡片；真正改变决策才再次通知。若只是旧论文晚上传 arXiv、相同结论的新转述或同步重试，不当成研究新增。标题改名、会议版本与预印本用别名归并。

## 既有资料

- [Snapdragon 笔记](Snapdragon.md)
- [既有 prompt](prompt.md)

本次未移动或重写既有内容。新机制从首批回填开始运转，不代表历史资料已经全面规范化。

## References

一手论文、项目和实验依据请进入各卡片 References。跨厂商论文归属规则以 [CameraPaper CONTRIBUTING](https://github.com/baolinv0/CameraPaper/blob/main/CONTRIBUTING.md) 为准。
