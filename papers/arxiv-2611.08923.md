# FANO: Anchored Forward-Noise Optimization for Diffusion Inverse Problems

元数据：Shilong Han, Hongxia Wang；National University of Defense Technology；arXiv 2611.08923v1，首次公开 **2026-11-06**（11-09 arXiv 公告），首次覆盖 2026-11-10；selected original sections checked；作者结果、非独立复现。裁决 **PROBE**；T03 主主题 / T01、X01 连接；角色 **执行/评价**；地图变化 **Boundary refinement**。
目录：[快速回忆](#快速回忆) · [机制与证据](#机制与证据) · [竞争路线](#竞争路线) · [边界与方案](#边界与方案) · [References](#references)

## 快速回忆
技术命题：在已知观测算子的零样本扩散逆问题中，直接优化扩散状态可能把噪声分量推离训练时分布；改为锚定 clean estimate，只优化前向噪声及其半径，可减少末层恢复退化。
记忆：**测量残差下降≠图像恢复质量上升；优化变量也有分布约束。**

## 机制与证据
在线：已知测量 y、正向算子 A、观测噪声假设 → 预训练 DDPM 的 annealing layers → 前一层去噪图作为固定 anchor，优化 forward-noise e 的方向和半径，半径靠近 Gaussian typical shell → 估计 x，核查 measurement fidelity、PSNR/LPIPS。无需针对退化重新训练，但每个内层梯度都要求 denoiser forward+backward。
作者 Table 1：FFHQ100 256²，σ_y=0.05，已知 clipping-factor-2 HDR：FANO PSNR **29.88**、LPIPS **0.157**，SITCOM **28.13/0.217**，DAPS **27.48/0.210**；非线性去模糊 30.83 vs SITCOM 29.31 dB；ImageNet HDR 27.32 vs DAPS 26.07 dB。基线在同预训练权重、测试图、算子与噪声设置下通过公开实现重跑（作者实验）。
作者 Figure 2：SITCOM 末层噪声范数径向漂移，残差继续下降但 PSNR 回落；无测量噪声对照仍能出现。作者 Table 2 消融，HDR：固定半径 Sphere 29.06，直接欧氏噪声优化 Euc 29.18，完整 29.88；非线性去模糊三者 30.72/30.80/30.83。**主要改进来自把搜索变量改为前向噪声，不是仅来自 polar penalty。**

## 竞争路线
DAPS (2025) 搜索 clean-image/后验、SITCOM (2025) 直接搜索 denoiser input、DiffRGD (2026) 球面几何约束、INO (2026) 初噪优化；BAM、Dual Flow 的已知测量约束属于相关而不等价的（训练/推理接口不同）竞争路线。论文直接引用 DAPS/SITCOM；BAM/Dual Flow 联系为本图综合推断。

## 边界与方案
仅 FFHQ/ImageNet 256² 模拟算子、已知 A/高斯噪声，未测试未知相机管线、真实 RAW/Poisson-Gaussian、相机跨域或手机。HDR 配置 N=50、K=30，上界约 **1500 次需反传的 denoiser 计算**，绝非轻量实时。最小判别实验：固定 SITCOM 预算，加入仅末层 radius renormalization 与 FANO-Sphere 两个简单对照；记录残差/图像 PSNR 的非单调区间，确认收益不只是额外优化预算。**不改现有端侧 ISP 或 Tone Mapping。**

## References
- [arXiv v1](https://arxiv.org/abs/2611.08923v1)，原文 §2–4、Figure 2、Tables 1–2，Appendix B.4–B.5
- [已归档 BAM](arxiv-2609.39660.md) · [Dual Flow](arxiv-2611.05843.md)
- [专题](../surveys/measurement-consistent-generative-inverse-problems.md)
