# 个体审美偏好与摄影渲染评价：众人 MOS 能否代表用户？

版本 v0.1｜2026-11-09 历史实质版本补录｜主 T04，连接 T02/T05/T06/X01

目录：[研究边界](#研究边界) · [竞争路线](#竞争路线) · [历史证据和横向对照](#历史证据和横向对照) · [完整系统方案](#完整系统方案) · [判断与缺口](#判断与缺口) · [References](#references)

## 研究边界

**稳定问题**：人群平均图像质量/美学分数（MOS）、个人对单图的美学评分、同一输入场景不同渲染候选的偏好，三个目标并不相同。更强的通用 IQA 可能提高 crowd MOS，却不必提高个体的候选选优。

**目标**：从 K 个个人标注估计对新照片或新渲染的个体评价/排序；**非目标**：借此替代物理色差、RAW 保真或解决执行器不具备的编辑能力。

## 竞争路线

| 路线 | 输入/目标 | 监督与可控变量 | 适用条件与风险 |
|---|---|---|---|
| 群体 MOS/NR-IQA | 单幅图→平均分 | 多人平均标签；内容/技术失真 | 冷启动基准；忽略人际差异 |
| 用户条件网络/元学习 | 图像+用户属性或少量评分→个人分 | [PARA](https://arxiv.org/abs/2203.16754) / Flickr-AES 多用户评分 | 需要用户数据、训练；跨艺术域差 |
| 冻结 VLM + 个体线性探针 | 视觉隐藏状态 + K 个用户分→排序 | 每用户少量评分；Ryu–Yanaka 风格 | K 太小易欠定；相同冻结 backbone 才公平 |
| **人群协方差先验 + 冻结 VLM 特征** | 非测试用户群 + K 条个人评分→用户权重/排序 | [Undertone-P v2](../papers/arxiv-2609.27110.md)，Gaussian prior + posterior | 冷启动稳定；高度依赖先验监督和昂贵的预特征计算 |
| 同场景多个渲染版本偏好 | 同一 RAW/源图的多个编辑结果→两两偏好 | [DEAR](https://arxiv.org/abs/2512.05209) 众包偏好；与个人口味不等价 | 最贴近 TM/修图选择，但它不自动提供真实个人定制模型 |

## 历史证据和横向对照

- **PARA (CVPR 2022)**：31,220 张照片、438 名受试者、每图约 25 人评分；可研究个人审美与图像及标注属性关系。作者提出用户属性条件模型，证明用户信息可影响预测；不等于仅 10 评分时个人识别充分。本轮复核论文 §§1–2。
- **LAPIS (CVPRW 2025)**：11,723 张艺术作品，提供偏好与个人属性；照片上高分模型未必泛化艺术品。原官方摘要与 Undertone v2 实验复核。
- **DEAR (初公开 2025-12)**：MIT-Adobe FiveK 5 个 Expert 的不同渲染、同场景 pairwise preferences；每比较对作者报告 25 名评定者，偏向**渲染版本好坏**问题，而非普通图像美学排序。本轮复核正文 §§1、3；数据可得性和个体复标可靠性需续核。
- **Undertone-P (v1 2026-09-22，v2 2026-11-05)**：v2 彻底改为人群先验个性化。作者在 R&Y PARA 200 人固定划分下 crowd-only ρ=.640，10 人评分 .648，100 人评分 .676；绝大部分 10 样本性能来自先验，而非学到大量个性。被 v2 取代的 v1 研究的是 rubric panel dimension fusion，与 v2 不是同一命题。回填，不是 11-09 新首发。

**关系属性**：PARA/LAPIS 是数据与基准；R&Y 个人探针和 Undertone-P 是竞争/扩展；DEAR 是相邻但不同的**渲染候选偏好**任务；这里只建立综合对照，不臆断所有作者间的直接方法继承。

## 完整系统方案

**离线**：冻结视觉特征器（预计算图像） + 独立群体评分 → 人群 MOS 基线和个人参数先验 → 检查标签划分、群体覆盖与画像偏差；另用同场景 RAW→不同 renderer 生成可比较候选并收集独立 pairwise preference。

**在线**：源图或已渲染候选 + 用户历史 K 条评分 → 选择 crowd-only / personal posterior → 输出候选排名或 abstain。对新的单图特征计算可能需要多个大 VLM；这一成本应与个体后验小矩阵求解分开。**Agent 控制**：如用于修图动作选择，只允许将评价器当成独立候选选择模块，执行器可达性和候选搜索应另测。

**评价与反馈**：在用户与场景 holdout 下同时报告 per-user Spearman、pairwise accuracy、与 crowd-only 的净提升、最差分组、打分一致性/预算与 OOD 失效；对编辑器结果还需结构保真、局部泄漏和客观色差。

**相邻但不同的执行目标专题（2026-11-14）**：[ATune：摄影属性目标→编辑器滑杆搜索](photo-attribute-targets-and-editor-control.md)属于群体图像质量改进和工具控制，**不**包含个人用户的K条偏好，也不要求参考B；与本页个体审美评价互补。不能将ATune的群体pairwise人评作为个人适配已验证证据。

## 判断与缺口

**旧判断**：IQA/美学评分可代理某种平均人群观感。**新判断**：若要个性化，首先检验 crowd prior 已覆盖多少信息，以及 K 条个人评分是否真正改变候选排序；不能只看相对某个弱个体模型的绝对分数。**不变**：单图 MOS、真实修图 preference 和像素事实是不同评价目标。

**最小判别实验**：固定同一场景 3–5 种可复现渲染，给每位新用户 K=0/10/100 条个人偏好，等冻结特征/数据预算比较 crowd、isotropic prior、population covariance prior 的候选 winner accuracy；特别关注 crowd 口味不一致用户。这里是研究建议，**不是已验证的系统**。

**待补历史和证据**：Ryu–Yanaka 原论文、Ren 残差个性化、PARA 官方协议差异、LAPIS 2026 cleaning、DEAR 完整公开配对可得性、真实 TM A/B vs 绝对单图美学差异、设备端成本、跨文化与显示条件。

**记忆锚点**：同一张图的高 MOS 不代表你的个人首选；对个人评分模型，先验强不代表其个人适应强。

## References

- [Ren 等个性化美学（ICCV 2017）](https://openaccess.thecvf.com/content_ICCV_2017/html/Ren_Personalized_Image_Aesthetics_ICCV_2017_paper.html)
- [Undertone v1 与 v2](https://arxiv.org/abs/2609.27110v2)
- [Undertone canonical](../papers/arxiv-2609.27110.md)
- [PARA / CVPR 2022](https://arxiv.org/abs/2203.16754)
- [LAPIS / CVPRW 2025](https://arxiv.org/abs/2504.07670)
- [DEAR / rendering aesthetics](https://arxiv.org/abs/2512.05209)
- [既有低光 IQA/GT audit](low-light-iqa-and-gt-validity.md)
- [T04 总图](../LITERATURE_MAP.md)
