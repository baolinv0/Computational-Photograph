# Posterior Matching Distillation（PMD）
更新：2026-11-22｜canonical arxiv-2611.26629｜最早已核验公开：2026-11-19 arXiv v1｜首次覆盖：2026-11-22（历史补发现；**不是新论文提醒**）
主主题：X01 高效训练/少步生成；次主题：T03 生成式恢复迁移假设 / T05 训练目标。系统角色：离线蒸馏训练、生成执行；地图变化：**Boundary refinement / No material map change**。裁决：**WATCH（仅 text-to-image 证据，非恢复直接验证）**。
目录：[快速回忆](#快速回忆) · [机制与竞争路线](#机制与竞争路线) · [定量证据与反例](#定量证据与反例) · [系统方案和缺口](#系统方案和缺口) · [References](#references)

## 快速回忆
- **一句话命题**：少步学生不仅匹配教师最终输出分布，还通过改变后验的指数倾斜、约束相同噪声状态下的多个可能干净结果，从而更好保留生成多样性。
- **最强前序**：DMD/DMD2 对边缘生成分布做 score-based matching，Moment Matching 用条件均值，LCM/consistency 按轨迹/端点监督；PMD 与它们是竞争/共同抽象，不因被引用等于直接继承。
- **关键信息**：PMD-only 在 FLUX.2 [klein] 4B 的四步设置具有更高多样性但 FID 56.13、ImageReward -1.232；联合 GAN 后达到更合理的画质/对齐（全文 Table 1、Appendix E），所以“后验匹配 = 高质量生成”并不成立。
- **对 T03 现状的影响**：尚未在有真实观测 y 的恢复任务中检验测量一致性、内容保真、结构损坏、训练开销；不改变现有恢复执行、评价或手机部署决策。

## 机制与竞争路线
- **离线**：冻结生成教师 D_t，针对固定噪声状态 z_t 取指数倾斜方向 λ；Gaussian 下可将倾斜后验均值表示为在移位输入处的一次教师去噪评估；学生通过同一 z_t 的多次随机样本估计倾斜均值，匹配教师目标，并用 GAN 辅助项保持真实感。
- **理论边界**：所谓“恢复完整后验”是零总体损失、精确教师后验均值、所有近零邻域 tilt 等理想条件下的唯一性结论，不是有限样本实验中实证的准确条件后验。
- **在线**：文本+采样噪声 → 已训练学生，在既有噪声网格内做 1–N 步重加噪采样 → 合成图像。无原始传感器观测、无物理 forward model、无 ROI 忠实度约束、无 Agent。
- **机制先例与区别**：DMD2（NeurIPS 2024）目标是少步生成分布对齐且依赖 fake score/对抗；PMD 用同一 z_t 的一组 tilted moment 目标约束条件后验，并不用辅助 student-score 网络；但仍依赖 GAN 及多次学生采样，不能称为零额外训练成本。

## 定量证据与反例
- 原文 Table 1（1024²，MS-COCO 2014 10K prompts，均四步）：SDXL PMD FID 19.14 对 DMD2 19.20；FLUX.2 [klein] 4B PMD FID 24.12 对基准原模型四步 24.58；不能由如此小的差距推断所有指标/统计条件稳健领先。
- Table 2（PartiPrompts，1,632 prompts × 8 seeds，均四步）：FLUX PMD Vendi 3.3708，对 Moment Matching 2.3891；SDXL PMD Vendi 4.4621，对 DMD2 2.5178。多样性上升本身不说明对源图正确。
- Appendix E 对照：PMD-only Vendi 5.112 但 FID 56.13、ImageReward -1.232；GAN-only FID 34.19 但 Vendi 2.219。负面消融说明“保留多模态”与“成像质量/提示词对齐”是两个不同优化问题。
- §5 实验训练为 8×NVIDIA L40、2000 student updates、每状态 4 次 student draw、判别器/生成器更新比 5:1。4 NFE 是**推理**预算，不是整体训练算力或真实端侧时延。
- 来源核验：arXiv v1 原文 §1/§2/§4/§5、Table 1–2、Appendix E；非独立复现；项目页可见，但未核对可运行代码与权重。

## 系统方案和缺口
- **非目标**：本文没有恢复有噪 RAW/HDR/IR 图像，不证明具体观测 y 给定时可恢复真实人物、文字或纹理。
- **强简单基线**：同骨干同训练预算 DMD2/Moment Matching、GAN-only、PMD-only；迁移到 image restoration 前还需加测量条件与无 hallucination 约束。
- **待核验**：有损观测条件后验如何构造 tilt、同实际退化分布的保真与感知 Pareto、计算花费、真实高分辨率推理，以及相同随机输入下的多样性—真实性权衡。
- **行动**：WATCH，不替换原恢复算法。仅在下一轮出现直接 restoration/inverse problem 的公平实验或强反证时考虑升 PROBE/GO-E。

## References
- [原始论文 arXiv:2611.26629v1](https://arxiv.org/html/2611.26629v1)
- [DMD2（NeurIPS 2024）](https://proceedings.neurips.cc/paper_files/paper/2024/hash/54dcf25318f9de5a7a01f0a4125c541e-Abstract-Conference.html)
- [Moment Matching / IMM（不同的近似后验/均值机制）](https://arxiv.org/abs/2503.07565)
- [主主题：高效生成式恢复 living survey](../surveys/efficient-generative-restoration.md)
