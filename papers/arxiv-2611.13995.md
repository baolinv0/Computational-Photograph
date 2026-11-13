# Lipschitz-Controlled Flow Matching for Robust Image Restoration

- Paper ID: arXiv:2611.13995
- Authors: Sedjro Salomon Hotegni, Konstantin Sonntag, Paul-Christian Bürkner, Sebastian Peitz
- arXiv first upload: 2026-11-10 12:40 UTC, v1
- First covered: 2026-11-13
- Main theme: T03 — 可信生成式恢复
- Secondary themes: X01
- Verdict: PROBE
- Verification: full arXiv method, robustness/quality tables and limitations checked; no independent reproduction.

## 30-second recall

LipsFlower 用近似 spectral normalization、bounded modulation、convex residual mixing 与 finite-radius adversarial gain regularization，降低 flow-matching 恢复器对小输入扰动的放大；但稳健性和感知质量存在明显交换。

## 完整系统回忆卡

- **任务：** 512² blind face restoration，比较 Flow-from-Y 与 observation-conditioned BayesFlow。
- **稳健证据：** Flow-from-Y 在归一化 L2/L∞ 预算 0.01 的 SPSA 攻击下，CVaR95 gain 分别约从 .849/.830 降至 .747/.727，最大 gain 从 1.74/1.66 降至 1.16/1.12。
- **质量代价：** Flow-from-Y PSNR 25.784→25.475 dB、LPIPS .350→.388；BayesFlow 稳健最大 gain 改善更大，但 PSNR 25.731→23.409、LPIPS .330→.508。
- **关键消融：** 仅加 regularizer 在 vanilla backbone 上可能恶化均值/尾部；架构与正则组合才稳定改善作者报告的全部 gain 指标。
- **边界：** 仅合成退化人脸；攻击扰动不等同跨传感器/真实噪声；无全局 Lipschitz 证书、端侧成本和身份保持审计。

## 判断与下一实验

不能只凭平均 PSNR/LPIPS 宣称恢复可信。最小实验是在真实手机噪声、JPEG/ISP 扰动和跨传感器输入上同时画出质量—增益 Pareto，并单独做人脸身份/文字保真。

## References

- [arXiv:2611.13995](https://arxiv.org/abs/2611.13995)
