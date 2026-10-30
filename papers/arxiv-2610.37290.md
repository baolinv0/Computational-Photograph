# Taming Noise Initialization for Zero-shot Video Restoration with Image Diffusion Priors

## 快速回忆

- **首次公开**：2026-10-27（arXiv v1）
- **主题**：Restoration / Zero-shot video
- **核验范围**：selected_sections_checked；independent replication = not performed
- **一句话**：TINDER 用退化帧的 DDIM inversion 初始化时序相关噪声，再自适应混入高斯噪声并用测量引导轨迹注意力，使图像扩散先验可零样本用于视频恢复。

## 精读记录

### 机制与证据

与逐帧独立噪声或所有帧相同噪声不同，方法从输入视频反演得到含运动相关性的初始噪声；频率自适应混合抑制随反演带入的退化，再按输入估计的轨迹在采样注意力中对齐。作者在 DAVIS、REDS4、Set8 的多类逆问题上报告优于所测 zero-shot 基线，不需要重新训练视频扩散模型。

### 限制与竞争解释

DDIM inversion 既保留时序，也会编码退化与压缩；滤波无法保证只移除退化。评价主要依赖设定的退化算子和经典数据集，不证明真实手机夜景、rolling shutter、AE/AWB 跳变或未知 ISP 的泛化。零训练不等于低成本：反演 + 多步采样 + 轨迹估计没有移动端延迟/内存/功耗证据，且未找到已公开代码。

### 下一实验

先在真实手机 burst/video degradation 上测 flicker、warp error、OCR/身份保真与端到端时延；对 inversion、noise blending、trajectory attention 分别做跨传感器/跨压缩 OOD 消融。

## References

- https://arxiv.org/abs/2610.37290v1
