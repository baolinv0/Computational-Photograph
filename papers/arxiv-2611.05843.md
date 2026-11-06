# Dual Flow: Joint Image–Measurement Flow for Inverse Problems

目录：[快速回忆](#快速回忆) · [机制与前序](#机制与前序) · [作者证据与边界](#作者证据与边界) · [系统位置](#系统位置) · [References](#references)

- **ID**: arxiv-2611.05843；**作者**: Sevket Ege Yesilyurt, Figen S. Oktem（METU SPACE Lab）。
- **首次公开**: arXiv v1, 2026-11-04；**source_version** v1；**首次覆盖/核验** 2026-11-06。
- **主主题**: T03；**次主题**: T01/X01；**系统角色**: 具有已知线性前向算子的后验重建执行器。
- **地图变化**: New route（image/measurement jointly evolved）+ Bridge（物理约束与 flow）；**裁决**: PROBE（机制与对照扎实，真实 ISP 物理先验跨域未知）。
- **核验范围**: 原始 PDF p.1–3、p.6、p.11 表1、实验定量片段 selected_sections_checked；independent_replication=not_performed。

## 快速回忆

**技术命题**：同时演化 clean image 与 noise-free measurement 两个状态，而非只用固定 noisy y 引导图像采样；末态保证满足作者定义的前向模型。

**成立条件**：线性且已知 y=Ax+n；高斯噪声（推导导出 operator-dependent correlated noise denoising sufficient statistic）。这不是已解决相机 RAW→ISP 的非线性、饱和、未知颜色变换。

## 机制与前序

在线：观测 y、已知 A 和噪声设定 → 初始化 measurement flow state + image flow state → 用 sufficient statistic 的预训练条件 velocity 网络重复联合更新 → 得到 x_hat 与 y_hat=A x_hat。满足前向模型指**估计的 noise-free measurement** 与重建输出互相一致，**不意味着 x_hat 与 noisy 实测 y 无残差或恢复的纹理是真值**。

离线：干净图像及可模拟 operator/noise → 训练 operator-dependent correlated Gaussian denoising 等价形式的 flow velocity → 已知五类线性 operator 检查（denoise/deblur/SR/random inpaint/box inpaint）。

**前序与竞争**：PnP-Flow（plug-and-play flow先验）、Flower、OT-ODE；BAM（此前仓库已有已知算子条件化生成）是共同抽象/并行，不是直接继承已核实。Dual Flow 新点不是“第一次把物理算子放进恢复”，而是联合 image–measurement 状态和消除额外 per-problem 参数调优的求解形式。

## 作者证据与边界

原文 Table I：CelebA 100 张，五种模拟线性逆问题的 PSNR/SSIM/LPIPS 与运行时间；在作者环境，Dual Flow-T 0.18 s/image，相比 PnP-Flow1 0.99 s/image；box inpainting PSNR 32.74（T）/33.71（W）vs Flower1 31.13，LPIPS trade-off。Dual Flow-W 平均多条轨迹改善失真指标，不能当单次样本保真全优。

**证据范围**：合成 Gaussian linear operator + 面部图像占主，作者报告且未由其他人实测手机设备；对 blind 算子、RAW noise, CFA demosaic, camera nonlinear CCM/TM, clipping 未确认。公平性需考虑 NFE、pretrained model/训练数据、不同实现 GPU 的对照。

## 系统位置

**PROBE**：在已知退化/前向算子问题，与 BAM/PnP-Flow 做固定 NFE、固定噪声失配的控制实验。对没有标定物理模型的真实照片，不替代默认恢复器；PSNR 与 LPIPS 分开报。

## References

- [原文 PDF v1](https://arxiv.org/pdf/2611.05843v1)
- [BAM card](arxiv-2609.39660.md)
- [高效生成式恢复 survey](../surveys/efficient-generative-restoration.md)
