# 持续专题综述索引

更新：2026-10-24

目录：[专题](#专题) · [维护原则](#维护原则)

## 专题

| 主问题/主题 | Canonical survey | 范围与状态 |
|---|---|---|
| T05：训练数据从哪里来，哪些部分可信？ | [成像训练数据合成：逆 ISP、RAW 生成与曝光退化](imaging-training-data-synthesis.md) | MESS、RawGen、UNICE 等 13 项代表工作；v0.1，有明确全文/摘要核验边界及待补历史分支 |
| T01/T05：HDR 来源、输入与目标是什么关系？ | [既有 HDR 数据分类](../HDR/HDR_Data_Taxonomy.md) | 复用既有文档，不迁移；本次不重新核验其中全部条目 |
| T02/T05：SDR video → HDR 的训练目标怎么定义？ | [既有 HDR 数据与 PGT](../HDR/HDR_Dataset_References_and_PGT.md) | 保留原适用范围，通用合成路线转至本目录新分支 |
| T03/X01：生成式恢复能否用一次网络前向完成？ | [高效生成式恢复：潜空间与采样目标](efficient-generative-restoration.md) | 2026-10-24 v0.1；GLOW-FM、ELIR、WCDM、ReDDiT 等路线；仅 GLOW 本轮原文核验 |
| T02/T06：一步编辑要几个噪声时刻？ | [一步免反演编辑与端点校准](one-step-inversion-free-editing.md) | 2026-10-24 v0.1；ECT 对 ChordEdit，ER-Chord 作为不同空间控制轴；前序 backlog |
| T06/T03/T04：什么时候不应该恢复？ | [选择性恢复与任务效用](selective-task-aware-restoration.md) | 2026-10-24 v0.1；Gate3DGen 的净化器效果和真实路由负例分开记录 |
| T06：恢复执行器如何组织、验证与学习策略？ | [CameraPaper 的 AgenticIR survey](https://github.com/baolinv0/CameraPaper/blob/main/knowledge/imaging-agent/agentic-image-restoration-survey.md) | 复用另一仓库已有 canonical survey；不复制第二份全文 |

这是跨仓库导航，不代表所有主题都已完成 survey；未建设的分支继续保存在 [总图](../LITERATURE_MAP.md) 中。

## 维护原则

1. **已有则插入，缺少独立分支才创建。** 查同问题和同义词，不仅查文件名。
2. 新论文连同必要历史工作，进入对应路线、比较表、证据和当前判断；不只在文末追加名单。
3. 论文卡片只有一个 canonical path；多主题复用链接。survey 管综合关系，卡片管单篇证据。
4. 前序无年龄限制；旧论文用 backfill，不冒充新增提醒。发表先后不等于继承。
5. 主视图保留少量记忆锚点，完整索引可扩展；写明已核验范围、反证和未覆盖部分。

执行规则：[Paper Watch v3.2](../archive/PAPER_WATCH_V3.md#持续专题综述)。
