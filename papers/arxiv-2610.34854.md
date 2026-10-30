# Learning Dual-Camera Smooth Zoom via Decoupled Geometric-Photometric Data Synthesis

## 快速回忆

- **首次公开**：2026-10-26（arXiv v1）
- **主题**：ISP / Dual-camera zoom
- **核验范围**：selected_sections_and_author_project_checked；independent replication = not performed
- **一句话**：ZoomGS v2 把双摄切换中的几何与光度差异从 3D 场景表示中拆开，用单摄多视图场景扩展合成训练，再由双向 warping 的 ZoomFI 生成中间变焦帧。

## 精读记录

### 机制与证据

作者以 Redmi K50 Ultra 和 Huawei Mate 40E 估计 UW/W 相机几何与颜色差异，在 DL3DV-10K 的 4,000 个场景上生成每设备 16,000 条序列，清洗后保留 8,704/7,686 条。真实测试仅含两机型的 100/50 个 UW-W 端点对，没有物理中间视角 GT；因此用 MUSIQ、MANIQA、TOPIQ、DOVER、FasterVQA 与 Smooth-ΔE 评价。ZoomGS v2 微调多种 VFI 均改善，ZoomFI-Lite/ZoomFI 在表内形成更好的质量—色彩连续性组合。数据、代码和权重项目页已公开。

### 限制与竞争解释

核心训练监督仍是 3DGS 合成；COLMAP 标定、3DGS 重建与颜色插值误差可能共同决定结果。真实测试没有中间帧 GT，NR-IQA 和平滑 ΔE 会奖励模糊，论文也明确提示未微调模型可因过模糊而得到更好颜色连续性。没有手机端端到端延迟、功耗、内存或预览稳定性数据，手机仅提供端点图像，不能当作设备部署。

### 下一实验

在硬件同步双摄视频上测镜头切换前后光流残差、肤色/文字保真、运动遮挡和 AE/AWB 突变；把 ZoomFI-Lite 部署到目标 NPU/GPU，报告含传感器读取、缩放、融合、显示的整链路 P50/P95 延迟与热稳态。

## References

- https://arxiv.org/abs/2610.34854v1
- https://hitjunjief.github.io/DCSZ-v2
