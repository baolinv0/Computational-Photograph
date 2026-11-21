# AesDistill: Distilling Generative Aesthetics for Image Color Enhancement
更新：2026-11-21｜canonical arxiv-2611.25635｜arXiv v1 首传2026-11-19｜首次覆盖2026-11-21｜Chuanzhi Xu; Chengkun Yue; Huiqi Liang; Haoyang Li; Zihan Deng; Qingwen Zeng; Pengfei Ye; Weidong Cai｜主 T02，次 T05/T04/X01；数据目标/训练/执行/评价；GO-E；New route + Boundary refinement。

目录：[快速回忆](#快速回忆) · [问题与路线](#问题与路线) · [作者证据](#作者证据) · [系统、限制与行动](#系统限制与行动) · [References](#references)
## 快速回忆
一句命题：给定单张原图，让多个大型生成器先提出不同“有吸引力的色调”目标，然后只蒸馏其**颜色/影调选择**到小而结构保留的确定性学生网络。改变的是训练目标来源，不是把生成式修改直接上线。
旧前序/竞争：FiveK/PPR10K固定专家编辑、HDRNet与3D LUT/DeepLPF/BPAM 参数化修图、PREEN风格到参数、ATune目标属性优化。AesDistill 与 ATune 是目标来源/执行器路线竞争关系，并非直接继承。
## 问题与路线
- 16,161张基础源图（FiveK 5000+PPR10K 11161），4教师各1次共64,644张编辑，约3360 H100 GPU-hours产生教师监督；FLUX.2-dev、FireRed-Image-Edit、HunyuanImage、Step1X-Edit。
- 教师可能改写场景结构；学生仅学从原图到教师目标的空间颜色调整和曲线/局部仿射变换，利用 correspondence 和置信加权降低错位监督，约1.13M参数，并保留teacher-condition多样性。
- 离线：原图→四教师生成→参考可信对齐/权重→多教师颜色教师训练→16个IQA/美学自动指标评估；在线：RGB+教师风格条件→学生局部颜色映射→输出，未运行四个巨型教师。无Agent/外部Judge或个人用户偏好学习。
## 作者证据
- FiveK 500、PPR10K 2286测试；“Joint Score”是12种自动美学指标+4 NR-IQA在参考池中百分位秩的平均，不是人类MOS。
- Table1/Figure2跨两数据集：学生 JS 74.75、最好非教师 baseline DeepLPF 67.50、HDRNet64.12，四个生成教师 76.62–96.62；专家 PPR10K 均值63.25、FiveK60.25。作者报告自定义JS最优不等于真人总体共识。
- NIMA 提升占比 FiveK 74.2%、PPR10K75.6%是**模型评分**，不是人工选择百分比；学生相对教师平均PSNR23.93/SSIM0.8118/LPIPS0.1662，证明拟合外观但并非真实保真。
- 先验泄漏：多个美学模型可能共享AVA等训练标注，16票不等于16独立的人评；教师/评价器可能偏向生成式过饱和或肤色不自然。教师成本 3360 H100小时不能包装成小模型只需廉价数据。未提供手机端完整 pipeline 实测。
## 系统、限制与行动
训练目标是生成器构造的“审美候选”，不是物理GT；输出变化约束只针对允许的颜色/影调，不能声称复制4个教师的结构改写。“教师高分→学生高分”与“用户偏好→按需可控”不同。
**GO-E（可复用生成目标数据工程）**。最小实验固定同一学生/数据预算，比较 FiveK专家配对、多教师未过滤目标、颜色/位置置信过滤后目标；用独立真人AB、人脸中性色/白衣和结构泄漏判胜负，不只用16指标。当前不替换ISP/TM已有目标策略。
记忆锚点：生成器可以教轻量编辑器“怎么调色”，却不能把它改写的场景事实当作GT。
## References
- [arXiv v1，§3–5，Table1/Fig2，Appendix](https://arxiv.org/abs/2611.25635v1)
- [摄影目标与可替换编辑器](../surveys/photo-attribute-targets-and-editor-control.md)
- [个人审美和泛化](../surveys/personalized-aesthetic-preference-and-rendering.md)
