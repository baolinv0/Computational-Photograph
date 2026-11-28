# Paper Watch v3.2 — 2026-11-28
## 检索水位与新发现
- 2026-11-28 检查四个官方 /new 页面：cs.CV 402、eess.IV 16、cs.AI 398、cs.LG 419，均仍为 2026-11-26 公告（上一轮已覆盖），没有将重复列表算新批次。来源：https://arxiv.org/list/cs.CV/new ; https://arxiv.org/list/eess.IV/new ; https://arxiv.org/list/cs.AI/new ; https://arxiv.org/list/cs.LG/new 。感恩节延后邮件的二手线索与页面日期一致；未核到2026官方假期公告原文，不保证下一批具体时间。
- 开放检索：11-26/27 arXiv 与一般网页主题搜索，覆盖 RAW/ISP/HDR/TM、SR/恢复/增强、IQA/reward/偏好、多参考与Agent；效率及PGT为组合关键词有限覆盖，未单独穷尽。命中 PreserveReward 等既有工作；未核实符合通知阈值且在上一轮后首次公开的论文。本轮不推进官方公告成功水位，也不将开放搜索视为全网覆盖。OpenReview及独立实验室发布未穷尽。
- alphaXiv 作者索引以11-18起重叠查询11位作者。Chao Dong→FAIR；Junjun Jiang→ApexFuse、PrismRestore（均既有），Kai Zhang→VADE（非目标）；Michael S. Brown、Shuhang Gu、Jinjin Gu、Weisi Lin、Radu Timofte、Yulun Zhang、Qingsen Yan、Ying Fu 未返回窗口内论文。相较前日索引已补回部分已知条目，但尚非完整作者覆盖；逐名均标 partial，不推进个人主页/独立作者源水位。
## 历史整合（非新增）
T04 [PreserveReward](../papers/arxiv-2611.34446.md) 11-25 v1、11-27已覆盖。重核 Tables1–3：同9B base/score-only/full 39.80/67.30/80.60%（EditReward-Bench 保真子集），直接分数监督贡献显著；双教师和路由有增量。RL后KRIS consistency由GPT-6.1-Sol打分，不是独立人评。原摘要复查 CheckDistill / EditReward-Compass，未升为全文。主[伪影与Reward survey](../surveys/artifact-grounded-reward-and-verification.md) 补路线、系统方案与对照；总图、索引同步。无新版本或改变方案的证据，不重复推荐、不重复alphaXiv收藏。
## Backlog / 未完成
- SIA 2611.33894 v1（11-25）已见于上轮，作者项目页 https://selective-image-analogy.github.io/ 搜索索引早于arXiv（精确首发待核），故不是本轮新作。原文 https://arxiv.org/html/2611.33894v1 Table2：固定AnaLoRA时无抑制/CSV/ExLoRA/full的Supp分别1.93/4.93/7.81/7.85；ExLoRA主贡献、CSV边际收益小，保留目标准确率存在代价。下一步对照同信息预算文本选择、参考差分分解及RelationAdapter等前序后确定T02主survey及历史卡；本轮未创建/收藏，非定论。
- Multidimensional Observer Model 2609.38487 的 abs/html 再请求失败（DisabledError），仍 pending，保留旧核验等级，不能裁决replacement实质性。DocDUR-Net、TORE、X-Matte、RelPRM 及其余历史候选仍待查。
## 实际回执
PreserveReward canonical、T04 survey、LITERATURE_MAP、survey索引、registry 均已更新并精确读回。未改变首次覆盖/首传、既有alphaXiv阅读和收藏状态。未做独立复现，未写入私人项目。
