# 增量影像研究归档协议 v1

目录：[职责](#职责) · [阅读结构](#阅读结构) · [身份与增量](#身份与增量) · [写入流程](#写入流程) · [质量与通知](#质量与通知) · [模板](#模板) · [首批范围](#首批范围)

## 职责

归档不是把聊天全文复制三份。每个研究对象只有一份可修订的正文，周报是当时的增量视图。

| 位置 | 保存内容 | 不保存或不默认执行 |
|---|---|---|
| 本仓库 `papers/<canonical-id>.md` | 通用计算摄影、ISP/3A、RAW/HDR、色彩、恢复、IQA、编辑、Agent、相邻成像研究的技术卡片 | 不把个人项目现状混入外部研究事实 |
| 本仓库 `archive/registry.json` | 跨仓库身份、正文位置、出现记录、核验范围、增量事件与同步结果 | 不替代 CameraPaper 既有品牌论文数据库 |
| 本仓库 `Recent_Papers_YYYY-MM-DD.md` | 周报快照：当期变化、论文卡片链接、分歧、排除与遗漏 | 不反复复制并独立维护论文全文 |
| [CameraPaper](https://github.com/baolinv0/CameraPaper) | 公司署名研究的品牌元数据、产业/产品、专利、竞品与跨品牌影响 | 使用某品牌手机或数据集，不等于该公司论文 |
| Notion | 私有阅读入口、周报链接、个人批注与待读选择 | 不建立第二套独立维护的技术正文；不覆盖人工笔记 |
| alphaXiv | 原论文收藏和主题归类；已有阅读状态由用户维护 | 不是研究笔记同步目标；当前连接器没有私有笔记写入接口；不把产品新闻当论文收藏 |

公司署名论文如已有 CameraPaper 记录，沿用其 `data/papers.csv`、`DATA_SCHEMA.md`、`CONTRIBUTING.md`。品牌表引用技术正文，不复制长篇笔记。已有正文优先复用原路径；无需搬迁历史 HDR/AgenticIR 文档。

## 阅读结构

每条卡片有两层：

**回忆层：**问题一句话、旧方法→新增机制、证据边界、为什么值得读、下一步。目标是重新打开时快速想起要点。

**精读层：**输入/输出/控制变量、训练/推理机制、定量证据及条件、横向支持/竞争路线、失败边界、最小验证、原始链接。没读过正文就写“待精读”，不得用摘要生成看似完整的数学推导或实验结论。

目录按主题聚合；日期只承担事件与周报索引。每份 Markdown 有前置可点击目录，方法和数据集首次出现尽量给原始入口，末尾保留 References。

## 身份与增量

### 一篇论文，一个身份

优先使用 `arxiv-YYMM.NNNNN`，版本单独记录；无 arXiv 用 DOI，再否则使用已核验官方页面的稳定标识。标题缩写、改名、会议版和预印本是别名，不另建论文。产品使用 `product-厂商-型号`；专利按 family 归并、独立 claim 单独讨论。

### 区分四种时间

- `earliest_public_verified`：实际找到的最早公开证据；不是声明已经穷尽全网。
- `source_version`：此次读到的版本；不一定是全站最新版本。
- `first_covered`：首次进入简报的日期。
- `checked_on`：本次核验或修订时间。

日期未知用 null，不猜测。首次上传 arXiv、会议接收公告、首次被本系统发现，都不自动等于新的技术内容。

### 两层去重

1. **对象去重：**canonical ID / DOI / 官方 URL / 标题别名。
2. **结论去重：**比较 `decision_key`、适用条件和证据；不同论文若只支持同一行动结论，归入 supporting evidence，不重复推送。

`material_update` 必须记录旧状态、新变化、原始证据定位（版本/章节/表/commit/发布说明）和影响的决策。历史回填使用 `backfill`，不伪装成当周新论文。修正使用 `correction`，保留被修正结论与原因。

## 写入流程

1. **发现与核验：**先搜索两个仓库和 registry，再看原论文/官方材料。发现和排序独立于个人项目；选定后才写应用联系。历史助手回复只是待核验线索。
2. **更新正文：**新对象写卡片；已存在则最小修订。来源事实、作者报告、推断、建议分开。只有读摘要时标 `abstract_checked`；看过选定正文段落标 `selected_sections_checked`；复现另记。
3. **登记事件：**先写 canonical 正文，再更新 registry 与本期快照。使用 GitHub 当前 SHA 更新；有并发冲突先重新读取，不能用旧副本覆盖其他任务的新记录。
4. **派生同步：**alphaXiv 先查已有收藏，再加入一个主主题文件夹；Notion 更新本期短卡和正文链接。不得更改 Reading/Completed，不得移除已有其他分类。沿用 ISP，不再向重复的 `3-ISP` 新增。
5. **核验与回执：**读取 GitHub 文件，检查 ID/链接/JSON；读回 Notion 页面；查询 alphaXiv membership。成功才写 synced；失败写 pending/failed + 原因，下一轮只补失败目的地，不重建成功条目。

推荐主题映射：ISP←通用 ISP/恢复；Raw←传感器/RAW；HDR←HDR/TM 重建；Color←颜色控制；Display←显示/观察者；IQA←质量评价；Agent←编辑控制/视觉 Agent/相邻控制。若长期出现新主题，再建文件夹，而非每周新建一套。

不配置双向正文覆盖：GitHub 是技术正文主源；Notion 人工批注不反向覆盖；alphaXiv 只同步论文引用。公开 GitHub 不存 Notion 私有页面 ID、访问令牌或个人项目笔记。

## 质量与通知

- **收藏 ≠ 已读；作者报告 ≠ 独立复现；归档 ≠ 推荐；新来源 ≠ 新结论。**
- 数值必须带数据集/硬件/分辨率/比较基线和来源定位；没核验完整条件就不继承旧简报数字。
- 趋势必须横向比较近 1–2 年独立工作及反例；同源转载不算独立证据。单篇只能标作者主张/局部信号。
- 产业项区分 Official / Independently Verified / Reported / Rumored / Inferred；产品支持不代表 OEM 已实现全部能力；不能从功能命名猜测底层硬件。
- **入库和推送分开。**日常 Watch 在有实质变化时入库并通知；无变化不发“无更新”。周度任务用同一 ledger 汇总，不把日内已推送内容当全新发现。
- 失败重试是同步修复，不是研究新增。首次读到旧论文可入历史库，但不触发新论文通知。
- 自动执行依赖当次任务确实获得连接器权限；未发生远程写入时只报告失败和待写内容，不能声称已同步。通知开关由用户客户端设置，本协议不修改。
- 当前 v1 是连接器驱动的归档协议，不是已部署的 GitHub Actions、持续爬虫或双向同步服务。

## 模板

卡片最小字段：`id / title / authors / topic / source URL / earliest_public_verified / first_covered / checked_on / source_version / verification_scope / decision_key`。

正文模板：

```markdown
# 论文标题
目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)
## 快速回忆
问题：
旧→新：
记住：
下一步：
## 精读记录
输入/输出/机制：
作者证据与具体位置：
支持和竞争路线：未核验就写待核验。
## 证据边界
核验到哪里；不能推出什么；失败条件；最小对照。
## References
原论文、项目、代码、比较文献。
```

registry 每条对象包含独立的 `events`：`backfill / first_archive / material_update / correction / supporting_evidence / sync_retry`。同步只更新该对象的 receipts，不改变研究结论。

## 首批范围

2026-10-03 对 2026-10-01 简报做首次回填：8 篇论文 + 1 条产业线索。核验等级逐条记录；本次不宣称已审计此前所有周报。历史已覆盖记录与纠错要求见 [历史接入边界](archive/LEGACY.md)。

References：
- [CameraPaper 贡献规则](https://github.com/baolinv0/CameraPaper/blob/main/CONTRIBUTING.md)
- [CameraPaper 数据结构](https://github.com/baolinv0/CameraPaper/blob/main/DATA_SCHEMA.md)
- [已有 2026-09-19 论文笔记](Recent_Papers_2026-09-19.md)
