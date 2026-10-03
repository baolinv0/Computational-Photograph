# 2026-10-01 影像研究简报｜回填快照

目录：[范围](#范围) · [快速回忆](#快速回忆) · [产业线索](#产业线索) · [核验与纠错](#核验与纠错) · [同步状态](#同步状态) · [References](#references)

## 范围

本文件于 **2026-10-03** 回填 2026-10-01 简报的 8 篇主论文与 1 条产业线索。它是整理和核验后的索引，不是原聊天逐字副本，也不是又一轮新论文推荐。未对这些条目重新排名。

论文详细正文只存一份，下表直接引用。来源：3 篇读取了选定原文段落；5 篇目前只核验原摘要索引与元数据；产业线索仅官方索引部分核验。均未独立复现。

## 快速回忆

| 主题 | 论文卡片 | 旧→新 / 最值得记住 | 首先检查 |
|---|---|---|---|
| ISP / 逆问题 | [BAM](papers/arxiv-2609.39660.md) | operator-conditioned 点估计扩展到后验采样；接口中显式保留成像物理 | 算子/噪声失配 |
| 视频恢复 | [RelayVSR](papers/arxiv-2609.37850.md) | 大模型稀疏供参考，小模型每帧跑；优化整段视频而不只参考图 | 错误传播、lookahead 与完整延迟 |
| 编辑控制 | [FlowTool](papers/arxiv-2609.35673.md) | 连续参数生成；仍有 tool-presence 和固定 renderer 顺序假设 | 工具集/renderer 改变后的泛化 |
| HDR | [ExpandDiff](papers/arxiv-2609.39624.md) | 训练时动态改变暗部和高光裁剪范围 | 可观测区与不可观测区分开评价 |
| 编辑评价 | [The Camera Inside the Editor](papers/arxiv-2609.37732.md) | 用画出的校准图案读取编辑器隐含相机偏差 | 焦距、姿态和透视保真 |
| IQA | [Multidimensional Observer Model](papers/arxiv-2609.38487.md) | 质量判断的感知子空间随任务改变 | 维度选择与行为协议 |
| Sensor→AI | [Raw Imagery Impacting Your AI](papers/arxiv-2609.38265.md) | SNR/MTF/分辨率与检测效用需联合评估 | 遥感结果不能直推手机 RAW |
| World Model | [LOCI](papers/arxiv-2609.40222.md) | 显式 KV 历史与几何递归记忆混合 | 同预算重访一致性及吞吐 |

## 产业线索

[华为 Z10 来源核对卡（CameraPaper）](https://github.com/baolinv0/CameraPaper/blob/main/raw/huawei/2026-10-03-z10-source-check.md)：保留官网可检索的模块化相机规格线索，但直接抓取正文不完整。本次不继承全部产品细节、不猜测手机与模块的 ISP 分工、不升级行业趋势。

## 核验与纠错

- **BAM：**主要已知算子设定不等于没有 blind-kernel pipeline 或非线性探索，卡片保留该区别。
- **RelayVSR：**首帧模型时间不含未来帧等待，不能等同用户端 end-to-end 延迟。
- **FlowTool：**原文说明代码、权重和数据访问受内部批准限制；不能当作已开源。
- **其他五篇：**不继承未逐项核表的全部数字，不用空白精读部分伪造完整评审。

本期 Watch 中的 ViTeX-Bench、RefGAP、ReCaVSR 未在此次回填中完成核验或收藏。更早周报仍在 [历史接入清单](archive/LEGACY.md)，不是已全量迁移。

## 同步状态

2026-10-03：GitHub 八篇技术卡片及一篇 CameraPaper 来源卡已写入；alphaXiv 八篇已加入既有主题文件夹并读回 membership；Notion 已建立私有阅读入口。Notion 不复制技术全文，alphaXiv 不写自定义长笔记，未修改用户已读状态。

索引与事件以 [registry.json](archive/registry.json) 为准。未来真实新证据追加事件；原周报快照不反复改成“最新榜单”。修正时注明发生日期和原因。

## References

- 八篇原论文、项目入口见对应卡片的 References。
- [归档机制](ARCHIVE_PROTOCOL.md)
- [品牌/产业入口](https://github.com/baolinv0/CameraPaper/blob/main/WEEKLY_ARCHIVE.md)
- [历史覆盖与纠错](archive/LEGACY.md)
