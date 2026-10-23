# Unified RAW Image Exposure Correction and Restoration via Linear Illumination and Frequency-Adaptive Enhancement

## 快速回忆

- **首次公开**：2026-10-20（arXiv v1；按本轮可核验来源）
- **主题**：RAW / Exposure
- **核验范围**：selected_sections_checked；independent replication = not performed
- **一句话**：把欠曝与过曝统一放回线性 RAW 域：先估计曝光方向与线性增益，再按曝光状态恢复噪声或剪切纹理。真正新增的不只是网络，而是 223 场景、1,784 对的真实多曝光 RAW 基准 CMER。

## 精读记录

### 机制与证据

LICN 使用 Bayer 通道互补性估计增益：Green 为欠曝亮化提供较高 SNR，Red/Blue 为高光压暗提供较少饱和的线索；FEN 以局部卷积、全局注意力和频率动态卷积处理欠曝放大噪声与过曝纹理缺失。论文在 CMER 上比较 16 种方法；CMER-only 平均 32.63 dB/0.950，合成预训练后 33.85 dB/0.951。

**证据范围**：全文选定段落；CMER 由 Canon EOS 5D Mark IV 三脚架静态拍摄，213 场景训练、10 场景测试；另给 Sony IMX586 跨相机可视化。未独立复现，数据/权重公开性未完成验证。

### 限制与竞争解释

这是采集后的 exposure correction，不是硬件 AE 闭环。完全饱和区无法从观测中恢复真实纹理；跨相机主要是可视化，动态场景、手机时延/功耗/热均未验证。

### 下一实验

用两种手机 Bayer RAW 建立固定曝光比和真实手持动态子集；分别测线性增益、FEN、跨传感器微调，以及饱和区 hallucination rate。

## References

- https://arxiv.org/abs/2610.28191
