# 4K Image Super-Resolution on Mobile NPUs

## 快速回忆

- **类型 / 问题**：3× 4K 超分移动 NPU 赛题；比较 Snapdragon INT8 与 Dimensity 浮点部署。
- **本周变化**：arXiv v1 于 2026-10-31 公开；给出 720p→4K 的真实 NPU 运行结果与量化退化。
- **决策含义**：摘要的“低于 5 ms”只成立于 Snapdragon 量化赛道，不能外推到另一平台或完整相机链路。
- **证据边界**：核验赛题设置和结果表；未独立复现。

## 精读记录

### 机制与证据

数据来自 DIV2K 的 bicubic 3× 下采样。Snapdragon 赛道冠军 AntYSP 约 54.9 KB，PSNR 29.96、SSIM 0.8729、NPU 4.33 ms；相对 FP32 的 PSNR 降幅约 0.08 dB。Dimensity 浮点赛道 ZTE-cv 方案 PSNR 30.91、SSIM 0.8921，但 NPU 时延约 110 ms；若算子不兼容，多项方案回退 GPU 并显著变慢。

### 限制与竞争解释

DIV2K+bicubic 不是相机真实退化，未覆盖去马赛克、噪声、锐化、压缩或镜头畸变；未给功耗、温升、内存峰值、P95 或 I/O。平台赛道的精度/数值格式不同，不应直接比较“赢家”。

### 下一实验

用真实手机 zoom/SR 数据和相同质量门槛，逐算子记录 NPU 覆盖、fallback、能耗、峰值内存与持续 4K 帧率。

## References

- [arXiv:2611.00963 v1](https://arxiv.org/abs/2611.00963v1)
