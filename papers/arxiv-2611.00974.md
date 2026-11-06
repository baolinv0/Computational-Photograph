# Efficient Image Denoising on Smartphone GPUs

## 快速回忆

- **类型 / 问题**：Mobile AI 2026 手机 RGB 去噪；重点是两款旗舰 SoC 的真实 GPU/NPU 时延。
- **本周变化**：arXiv v1 于 2026-10-31 公开；新增近代 Sony 手机传感器、真实 Camera2 采集和 20 帧平均 clean target。
- **决策含义**：比旧合成噪声赛题更接近产品数据，但仍需跨传感器、RAW 域与持续功耗验证。
- **证据边界**：核验数据构造、官方表格与设备说明；未独立复现。

## 精读记录

### 机制与证据

数据含 1000+ 场景、4000×3000 RAW，经关闭去噪的经典 ISP 转成 RGB；20 帧 burst 平均作为 clean，且人工剔除 OIS/错配样本。1920×1088 评测中，TLG 模型约 194 KB，PSNR 37.31、SSIM 0.9129；Adreno GPU 28 ms、Mali GPU 50.7 ms，QNN NPU 46 ms、MTK NPU 18.7 ms。TeamPAK PSNR 37.58，但 GPU 时延约 127–138 ms。

### 限制与竞争解释

平均 burst 会残留错配与场景运动偏差；RGB classical ISP 后训练不等于 RAW 噪声建模。只覆盖单一传感器/采集链，未报告跨设备、端到端相机管线、功耗、温升和持续帧率。

### 下一实验

按传感器/SNR/运动分层，加入 RAW 域基线、跨设备零样本测试和 burst-GT 对齐审计；同时记录 P95、能耗与 GPU/NPU fallback。

## References

- [arXiv:2611.00974 v1](https://arxiv.org/abs/2611.00974v1)
