# Undertone：少量评分个性化 VLM 美学评价器（v2 实质改题）

目录：[快速回忆](#快速回忆) · [方法与证据](#方法与证据) · [前序与判断](#前序与判断) · [证据边界](#证据边界) · [References](#references)

- **ID**：`arxiv-2609.27110`；作者：Amit Jadhav、Shaurya Beriwala、Beomjin Kim（Purdue University Fort Wayne）
- **首次可核验公开**：2026-09-22，arXiv v1；**当前读到版本**：v2，2026-11-05；**首次覆盖**：2026-11-09（历史补录，不作为新增通知）
- **前版题名**：*Feed the Panel Dimensions, Not Verdicts: Rubric-Decomposed Fusion of Vision-Language Aesthetic Judges*；v2 明确声明实质修订、改题并取代 v1。
- **主题**：T04（主），T02（个性化渲染目标）、T06（候选判别接口）、X01（推理成本）；
  **系统角色**：评价/用户偏好建模；**地图变化**：New route（针对个性化评价）/ Boundary refinement（结果解释）。
- **判读**：PROBE（历史实质版本修订；不是本轮新首发论文）；**核验级别**：`selected_sections_checked`（v1 §1–2、v2 §1–3 与表1、方法说明；作者报告，未独立复现）。
- **decision_key**：`population-prior-frozen-vlm-readout-personalized-aesthetics-cold-start`

## 快速回忆

**一句话命题**：新用户只给 10–100 张美学评分，能否用其他用户学到的「偏好变化方向」来更新冻结视觉评价器，而非每个用户训练一个网络？

**旧→新**：v1 的命题是多模型 rubric 分维评分能否改进 MOS 预测；v2 改为「冻结 VLM 的期望分数+评分 token 隐状态+冻结图像特征 → 人群权重先验 → 对新用户闭式贝叶斯回归」。**这不是简单的名称升级**，原版的 panel-rubric 结论不可当成 v2 的个性化实证。

**记忆锚点**：少量个人评分不是从零拟合偏好，而是在人群已观察到的偏好差异子空间里校准；很小的个人增益也可能被强人群先验掩盖。

## 方法与证据

**离线**：六个冻结的 7B–12B VLM（含 Qwen2.5-VL-7B、Qwen3-VL-8B）给每张图的 1–10 分 token 分布与中间隐藏态，外加 CLIP/SigLIP/DINOv2，经过 PCA 和标准化形成约 391 维含截距特征。对非测试评分者各自 ridge 拟合线性权重，取均值 μ、协方差 Σ 和噪声方差，形成 Gaussian population prior。这里的「无网络训练」不等于没有离线计算、拟合或来自其他评分者的监督。

**在线**：新用户给 K 张评分，Bayesian linear regression 后验均值闭式解出个人 w；新图片预先计算 frozen read-outs → φᵀw；不必逐用户微调 VLM。实现成本需要将六个 VLM 推断与个人小矩阵求解分开统计。

**作者证据**（v2 §3，Spearman ρ；非独立复现）：
- Ryu–Yanaka 固定的 PARA 200 名评分者/每人 50 张留出图：仅人群先验 **0.640**；10 条新用户评分 **0.648**；100 条 **0.676**。个人化增量分别只有 +0.008/+0.036（相对其自身零样本先验）。
- 最不符合众人意见的评分者、LAPIS 艺术品域个性化收益更大；论文报告 LAPIS 100 条评分增量 +0.206，但其评价者划分、数据清洗版本与早期论文并不完全相同。
- 不使用数据集评分标签的 6-VLM 期望分数面板，在 PARA 3,000 图 MOS 上 ρ=0.835；同作者运行的 Q-Align 为 0.694；但 RED-Aes 为 0.859，PARA 上端到端监督方法也有更高分；在 AADB 上还存在强于此面板的报告结果。
- 6 个 VLM 读取特征每张图约 **2.1 A100 GPU-seconds**（论文声称，可离线计算），**不是手机端实时成本**；论文也给出单一 7B judge 可用的消融方向。

## 前序与判断

**历史机制**（不是直接方法继承的统一流水线）：
1. [Ren 等：Flickr-AES / 个性化美学残差](https://arxiv.org/abs/1704.01841)（经典个性化与通用模型残差路线；原文链接与机制需后续单独核验）。
2. [PARA (CVPR 2022)](https://arxiv.org/abs/2203.16754)：31,220 张照片、438 名评分者、客观/主观属性与条件 PIAA；已复核原文 §1–2。
3. [LAPIS (CVPRW 2025)](https://arxiv.org/abs/2504.07670)：11,723 张艺术品与个体评分属性，测试跨图像域；本次核验官方摘要及论文在 v2 的使用条件。
4. [DEAR (2025-12 预印本)](https://arxiv.org/abs/2512.05209)：MIT-Adobe FiveK 多修图版本的**同场景渲染偏好配对**；是摄影调色选择不同于单幅照片美学评分的直接任务边界，已复核论文 §1、§3。
5. Undertone v1 是同一 arXiv 身份的**被取代版本**，其「rubric 分维合并」与 v2 的「人群先验个性化」应分别描述，不视为两篇独立论文。

**最强替代解释**：收益来自 (a) 非测试用户标签形成的人群先验；(b) 更强/更多冻结大模型及预计算隐藏状态；(c) 新用户本身 K 次评分的独立贡献，可能非常小。应固定 VLM 特征、非测试用户信息和预算，对比 crowd-only、isotropic ridge/先验、per-user ridge 与人群协方差先验。

## 证据边界

- R&Y 过去发表的个性化方法有的**不使用其他评分者标签**，而 Undertone-P 使用；跨论文最好数值不是完全等监督的对照。
- PARA 原始协议（非 R&Y 协议）中，作者承认以 PARA 监督训练的网络仍更强；因此不能宣称全面 SOTA。
- 美学单图排名不等于**同一场景多个 Tone Mapping 候选的 pairwise preference**；个人审美也不能覆盖色彩准确性、真实性、泄漏、内容保真。
- 需独立测试不同摄影风格、不同相机与显示器、相同场景渲染版本的真实 A/B 配对，以及评分一致性/冷启动成本。
- **本轮分类**：v2 2026-11-05 公开于此前 2026-11-06 列表，本轮 2026-11-09 首次补录；标 `backfill`，不按新论文通知，不改 v1 earliest_public 日期。

## References

- [Undertone arXiv v1（2026-09-22）](https://arxiv.org/abs/2609.27110v1)
- [Undertone arXiv v2（2026-11-05）](https://arxiv.org/abs/2609.27110v2)
- [PARA](https://openaccess.thecvf.com/content/CVPR2022/html/Yang_Personalized_Image_Aesthetics_Assessment_With_Rich_Attributes_CVPR_2022_paper.html)
- [LAPIS](https://openaccess.thecvf.com/content/CVPR2025W/CVEU/html/Maerten_LAPIS_A_novel_dataset_for_personalized_image_aesthetic_assessment_CVPRW_2025_paper.html)
- [DEAR](https://arxiv.org/abs/2512.05209)
- [个人审美偏好/渲染选择 living survey](../surveys/personalized-aesthetic-preference-and-rendering.md)
