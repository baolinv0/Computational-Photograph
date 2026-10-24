# 贡献与检查说明

目录：[放在哪里](#放在哪里) · [更新顺序](#更新顺序) · [本地检查](#本地检查) · [检查边界](#检查边界)

## 放在哪里

| 内容 | 入口 |
|---|---|
| 单篇论文的技术正文 | `papers/<canonical-id>.md`，一篇只保留一份 |
| 论文身份、事件和同步回执 | [archive/registry.json](archive/registry.json) |
| 跨论文路线、比较与待查问题 | [surveys/README.md](surveys/README.md) 与 [文献地图](LITERATURE_MAP.md) |
| 当期变化和历史快照 | `Recent_Papers_YYYY-MM-DD.md` |
| 厂商归属、产品与专利证据 | [CameraPaper](https://github.com/baolinv0/CameraPaper) |

归档与核验规则以 [ARCHIVE_PROTOCOL.md](ARCHIVE_PROTOCOL.md) 为准，持续调研规则以 [PAPER_WATCH_V3.md](archive/PAPER_WATCH_V3.md) 为准。

## 更新顺序

1. 查 registry、别名和已有卡片，确认稳定身份；正文模板见归档协议。
2. 更新唯一正文，分别说明作者报告、已核验证据、推断和待查项。仅做结构维护时，不更新论文的 `checked_on` 或核验范围。
3. 登记真实发生的事件；按需要更新对应 survey、地图与快照。跨仓库同步只记录实际回执。
4. 从 registry 重新生成论文速查表，执行下列检查，将源文件和生成结果一起提交。

不要手工编辑 [papers/README.md](papers/README.md)：它只呈现 registry 的已有字段，不产生新的科学结论或阅读状态。新增日期不是推荐排名，最近核验也不等于全文已读。

## 本地检查

使用 Python 3.10 及以上版本，无需安装第三方依赖。在仓库根目录执行：

```bash
python scripts/knowledge_base.py index
python scripts/knowledge_base.py check
python -m unittest discover -s tests -v
python skills/critical-paper-research/scripts/validate_skill.py
git diff --check
```

`index` 更新派生速查表；`check` 只读取文件，发现问题时返回非零退出码。GitHub Actions 在 push 和 pull request 时执行结构检查、工具测试与既有 Skill 校验，不自动改写正文或提交文件。

## 检查边界

检查覆盖 registry 结构、重复身份、本仓库论文路径与文件登记、可解析的本地 Markdown 内联文件链接、正文中误写的字面量换行，以及派生索引是否过期。代码围栏中的示例和 `skills/` 内部链接由各自工具处理；普通链接的锚点不在通用离线检查范围。

它不会联网核验外部链接、论文事实、引用关系、作者归属、版本差异或远程收藏与同步。`verification_scope` 与 `source_version` 保留现有自由文本和未知值；CameraPaper 的外部 canonical URL 也不按本地文件处理。所有成功结果仅代表对应结构检查通过。
