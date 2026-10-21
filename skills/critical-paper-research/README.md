# critical-paper-research · v1.0.0

用于“论文创新性、实验可信度、科研价值、端侧部署与趋势分析”的可移植 Agent Skill。

## Quick start

让支持 Agent Skills 的本地智能体读取 `SKILL.md` 并按目录加载参考文件。常见安装位置（取决于运行时）：`~/.agents/skills/critical-paper-research/`，或该运行时文档指定的 skills 目录。复制完整文件夹；仅上传到 GitHub 不等于自动安装到 ChatGPT。

调用示例：

- `按 critical-paper-research 的 L2 模式深度分析 BluePixel。给出前作反查、创新性评价、E0–E4 证据表、最低可信实验。`
- `按 L1 筛选这周的 8 篇 ISP 论文，选 2 篇进入 L2。`
- `比较博客对 BluePixel 的判断和原文，核算端侧时延并搜索反例。`
- `使用 L3 审查 HarnessIR：Agent 是否有独立于 Best-of-N 的收益？`

## Contents

- `SKILL.md` — 入口、级别、审查流程和停止规则
- `references/` — 文献反查、实验审查、影像专项、经验库策略、GitHub 归档说明、来源
- `assets/` — 论文报告与经验条目模板
- `evals/` — 可交给不同 Agent 的对抗性验收场景（尚未执行行为测试）
- `scripts/validate_skill.py` — 标准库本地结构校验

验证：`python scripts/validate_skill.py`（本地无网络需求）。

## Integration with existing libraries

- 单篇论文：`baolinv0/Computational-Photograph/papers/arxiv-<id>.md`。
- 跨论文方法与经验：`baolinv0/CameraPaper/knowledge/research-methodology/`。
- 公司/产品证据仍在 `CameraPaper`，遵守该库 `AGENTS.md`，不重复存放论文精读正文。

## Boundaries

本 Skill 不自带论文下载模型、不默认拥有 GitHub 写权限、不执行独立科研实验。审核时需显式提供证据位置；无法访问的实验不可声称已确认。公开使用前注意私密稿件授权和第三方检索策略。

## Acknowledgment

Methods inspired by Sci-Extract, Scientific Agent Skills (literature-review and peer-review), and the Agent Skills open specification. See `references/sources.md`.