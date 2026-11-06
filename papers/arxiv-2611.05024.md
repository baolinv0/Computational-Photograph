# RGB Photo Enhancement with Deep Learning on Smartphone GPUs

## 快速回忆

- **类型 / 问题**：Mobile AI 2026 RGB 照片增强赛题；在真实手机 GPU/NPU 上比较全高清增强质量与时延。
- **本周变化**：arXiv v1 于 2026-11-03 公开；首次给出 Snapdragon 8 Elite Gen 5（Adreno 840/QNN）与 Dimensity 9500（Mali/MTK NPU）的同赛道结果。
- **决策含义**：部署评估必须拆开 GPU、NPU、算子兼容与设备差异；不能用单一 MAC 或桌面 GPU 推断手机成本。
- **证据边界**：已核验论文方法、数据与结果表；未独立复现。

## 精读记录

### 机制与证据

赛题沿用 DPED 的旧 iPhone 3GS→Canon 70D 风格映射，输入为 1920×1088。DaHua-IIG 方案约 3.24 MB，作者表中 PSNR 22.20、SSIM 0.7881、MOS 4.1；Adreno GPU 23.8 ms、Mali GPU 60.4 ms，Qualcomm NPU 21.8 ms，而 Dimensity NPU 转换失败。结果说明同一网络在不同 GPU 上相差显著，NPU 可用性也受算子/转换链限制。

### 限制与竞争解释

DPED 的手机与 DSLR 均较老，目标更接近固定相机风格迁移，而非现代传感器/ISP 的跨域增强。作者未给功耗、温升、P95、相机管线 I/O 或持续运行数据。MOS 不能替代色彩、肤色、纹理和失真分项。

### 下一实验

在现代多机 RAW→sRGB 管线上复跑同一模型，统一预处理与色域；记录 GPU/NPU fallback、端到端 P50/P95、能耗、温升和跨设备色彩漂移。

## References

- [arXiv:2611.05024 v1](https://arxiv.org/abs/2611.05024v1)
- [Mobile AI Workshop / Challenge](https://ai-benchmark.com/workshops/mai/2026/)
