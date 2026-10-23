# S3D-Mosaic: Subgradient-Guided Cross-Band Structure Transfer for Spectral Demosaicing

## 快速回忆

- **首次公开**：2026-10-17（arXiv v1；按本轮可核验来源）
- **主题**：RAW / Multispectral sensing
- **核验范围**：selected_sections_and_repository_checked；independent replication = not performed
- **一句话**：将跨波段共同结构以方向 subgradient 形式注入 MSFA demosaicing，并保持幅值不变；这是光谱传感器/算法协同线索，不是普通手机 Bayer 去马赛克结论。

## 精读记录

### 机制与证据

DSE-DConv 通过自监督学习跨波段方向结构，结合 dual-scan ADMM 迭代重建；覆盖 CAVE、NTIRE 2022、pan-mosaic fusion 与 UAV-mounted Specvision 3×3 MSFA 实拍。

**证据范围**：论文选定章节与作者仓库；当前仅 v1。真实数据为 6 个代表场景、无 ground truth，使用指定 false-color composite 的 NIQE 辅助评价。未独立复现。

### 限制与竞争解释

MSFA 与手机 RGB Bayer/Quad-Bayer 的采样、光谱响应和噪声不同；100 次 ADMM 等迭代未证明移动实时。无 GT 的少量真实场景不能证明逐波段光谱保真。

### 下一实验

在公开 MSFA raw 上增加 spectral angle/每波段 MTF 与噪声敏感性；再移植为少迭代 unrolled 版本测端到端延迟。

## References

- https://arxiv.org/abs/2610.24414
- https://github.com/bestwishes43/S3D-Mosaic
