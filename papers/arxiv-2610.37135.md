# Physics Guided Diffusion Model Based Exposure Interpolation for High Dynamic Range Imaging

## 快速回忆

- **首次公开**：2026-10-27（arXiv v1）
- **主题**：HDR / Exposure interpolation
- **核验范围**：selected_sections_checked；independent replication = not performed
- **一句话**：先用物理曝光映射得到中间曝光，再让条件扩散只补残差高频，目标是缓解双大曝光比单次采集直接融合的亮度次序反转。

## 精读记录

### 机制与证据

输入为对齐的最大/最小曝光 Z1/Z7，目标是中间曝光 Z4；物理项固定，Swin-UNet 扩散学习 Z4 与物理插值间的残差，并以相关性变化和拟合误差放大因子设计预测目标。训练/验证/测试为 420/40/60 条对齐序列，显著运动和错位样本被排除；另有外部测试集。训练在 NVIDIA A6000 完成，表内优于三类物理/CNN exposure interpolation 基线。

### 限制与竞争解释

论文论证的“单次双曝光”依赖专用同时采集器件，但实验使用受控对齐七曝光序列构造端点和 GT；这不等于真实动态场景的单次双曝光验证。剔除错位样本规避了运动、rolling shutter 与跨曝光配准难点。没有代码、手机端速度/功耗或传感器噪声分层，生成高频也可能产生不可观测细节。

### 下一实验

用真实同帧双增益/交错曝光 RAW 建立 BOR 边界集，测运动、饱和、暗噪与肤色；与纯物理、多帧 HDR、CNN residual 在相同 ISP 和端到端时延下对照，并做高频真实性审计。

## References

- https://arxiv.org/abs/2610.37135v1
