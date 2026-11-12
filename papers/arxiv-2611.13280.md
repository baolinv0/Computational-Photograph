# RetinexGS: Retinex-Inspired Gaussian Splatting for Low-Light RAW Reconstruction

- Paper ID: arXiv:2611.13280
- Authors: Yulang Fei, Huaiyuan Weng, Chul Min Yeum
- arXiv first upload: 2026-11-09 21:44 UTC, v1
- First public new-listing coverage: 2026-11-11
- First covered in this archive: 2026-11-12
- Current version: v1
- Main theme: T03 — 可信恢复、生成式 SR 与高分辨率
- Secondary themes: T01, X01
- System roles: data, execution, training, deployment
- Map change: Engineering maturity; Boundary refinement
- Verdict: GO-E
- Canonical survey: [Low-Light RAW Neural Rendering](../surveys/low-light-raw-neural-rendering.md)
- Verification: full arXiv text, method, main tables and ablations checked; no independent reproduction performed.

## 30-second recall

RetinexGS把低照 RAW 多视图重建中的三个问题——噪声、外观变化和暗区稀疏几何——分别交给 DNG 噪声元数据加权、Retinex 外观分解和深度引导初始化处理，再用 3DGS 实时合成新视角。

**记忆锚点：** 它不是单图 RAW 去噪器，而是用多视图冗余把 RAW 噪声平均掉，并把传感器噪声信息带进 3D 场景优化。

## 问题边界与路线关系

- RawNeRF（2021）直接在线性 RAW 上训练 NeRF，利用 25–200 张 noisy RAW 的多视图冗余恢复暗场 HDR 场景；代价是 NeRF 训练和渲染较慢。
- LE3D（2024）将问题迁移到 3DGS，使用 Cone Scatter Initialization、Color MLP、depth distortion 和 near-far regularization，重点解决低 SNR 下 SfM 与线性 RAW 颜色表达问题。
- From Chaos to Clarity（2024）指出 3DGS 会把 RAW 噪声过拟合成细长 Gaussian，使用 noise extractor 与 noise-distribution prior。
- HDRSplat（2024）使用 14-bit linear RAW、HDR loss 和 rasterization tuning，强调低照重建效率。

RetinexGS 与 RawNeRF、LE3D 是同问题上的直接竞争路线；与 From Chaos to Clarity、HDRSplat 属于共同抽象机制下的互补/竞争方案。没有证据表明它直接继承上述某一方法。

## 技术机制

1. 每个 Gaussian 的颜色分解为 view-independent base color 与共享的 position/view-dependent modulation field，并分别正则化，降低噪声驱动的外观自由度。
2. 从 DNG 读取 signal-dependent noise metadata，对 RAW reconstruction loss 加权。
3. 使用 distortion-aware rendering，避免 RAW target 被空间重采样。
4. 使用 depth-guided initialization 缓解暗区稀疏几何和 SfM 不稳定。

## 完整系统回忆卡

- **目标：** 从低照多视图 RAW 重建稳定的 3D 场景，并支持 novel-view synthesis。
- **非目标：** 单张图像增强、手机 ISP 端到端部署、动态视频恢复。
- **输入：** 多视角线性 RAW、相机 DNG 噪声元数据、相机位姿/几何信息及深度初始化。
- **输出：** 3D Gaussian 场景表示，以及新视角 RAW/显示域渲染结果。
- **目标定义：** 参考视角 RAW 测量定义重建目标；不是审美风格或人工偏好目标。
- **执行表示：** 3DGS；base color 与 appearance modulation 分解。
- **训练数据/监督：** 3 个公开 RawNeRF 场景和 2 个自采低照 RAW 场景；另有 6 个户外场景用于定性展示。自采数据来自 iPhone 14 Pro Max。
- **评价：** sRGB PSNR/SSIM/LPIPS 与 linear RAW 域指标；sRGB 指标包含 per-channel affine alignment。
- **反馈：** RAW 重建损失、DNG 噪声权重、外观分解正则和几何/深度约束。
- **成本：** 作者报告 RetinexGS 使用 15k iterations，对照方法使用 30k iterations；RTX 4090 上 novel-view rendering 为 91–145 FPS。渲染 FPS 不等于完整采集、训练和部署成本。
- **强基线：** RawNeRF、LE3D；From Chaos to Clarity 与 HDRSplat 是重要替代路线。
- **Agent 控制层：** 无；这是显式优化的 3D 场景重建系统。

## 关键证据与批判性评审

**作者主张：** 在 5 个场景、相同 RAW 输入条件下，RetinexGS 的 mean sRGB PSNR 比 LE3D 高 2.18 dB、比 RawNeRF 高 2.71 dB，并支持实时新视角渲染。

**局部证据：** 结果覆盖 3 个公开 RawNeRF 场景和 2 个自采场景；消融显示外观分解是主要增益来源，DNG noise weighting 与 depth initialization 提供额外收益。

**最强替代解释：** 总增益不能全部归因于 DNG 噪声模型。appearance factorization 增加了表达能力，且作者对比的迭代预算并不相同（15k 对 30k）；应拆开看每个模块的贡献。

**边界：** 场景数只有 5；自采部分仅 2 个场景，其中有参考视角的场景更少；没有跨传感器、跨厂商或动态场景验证。没有独立复现。

**共同方向/共识：** RAW 观测、噪声建模与 3DGS 表示结合是持续发展的路线；当前证据不足以称为统一共识。

## 判断与行动

GO-E 的价值主要是系统工程与表示/损失设计的成熟度，而不是提出全新的 RAW 重建问题。保留为 T01/T03 的邻接研究分支，不据此改动单帧移动 ISP。若要判别 DNG metadata 是否真是主因，最小实验是固定 3DGS appearance capacity，只切换 metadata-weighted loss 与固定噪声模型。

## References

- [RetinexGS, arXiv:2611.13280](https://arxiv.org/abs/2611.13280)
- [RawNeRF, arXiv:2111.13679](https://arxiv.org/abs/2111.13679)
- [LE3D, arXiv:2406.06216](https://arxiv.org/abs/2406.06216)
- [From Chaos to Clarity, arXiv:2406.08300](https://arxiv.org/abs/2406.08300)
- [HDRSplat, arXiv:2407.16503](https://arxiv.org/abs/2407.16503)
