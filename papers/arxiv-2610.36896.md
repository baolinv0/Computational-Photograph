# PREEN: Exemplar-Based Color Style Transfer with Smartphone Editor Presets

## 快速回忆

- **首次公开**：2026-10-27（arXiv v1）
- **主题**：Color / Parametric editing
- **核验范围**：selected_sections_checked；independent replication = not performed
- **一句话**：不直接生成像素，而是从内容图和参考图回归 29 个确定性编辑滑杆，让参考风格变成可解释、可保存、可继续修改的手机预设。

## 精读记录

### 机制与证据

Samsung Research 单作者工作。SA-LUT 教师生成伪目标，再把伪目标反演为 29 维伪预设；CLIP ViT-L/14 与颜色统计进入双支路 MLP，第二阶段用 LoRA 和 CIELAB 图像损失校准。PST50 的 50 个 256×256 配对上，PREEN 为 PSNR 24.63、SSIM 0.914、LPIPS 0.094、ΔE 9.07。模型共 315M 参数，其中 CLIP 304M；TFLite 动态范围量化后在 Snapdragon 8 Elite Gen 5 手机 CPU（8 线程、20 次 warm run 中位数）上预测一对预设为 283 ms，编辑器应用时间未计入。

### 限制与竞争解释

PST50 很小，训练目标和评测都受 SA-LUT/专家风格空间限制；教师天花板与伪预设反演可能把“能被 29 个滑杆表达”误当成通用风格匹配。论文的 CPU 时间只覆盖预设生成，不是照片解码—编辑—显示全链路。Vivid 强度主要缩放色度参数；人评显示“更像参考”和“单张更好看”目标冲突。未找到可核验的公开代码/数据仓库。

### 下一实验

先实现编辑器与 29 维头，在跨品牌 RAW/JPEG、肤色、混合光和局部色块上复现；单独报告参考匹配、独立美感和结构保真，并把编辑器应用、颜色空间转换和全分辨率导出纳入移动端时延。

## References

- https://arxiv.org/abs/2610.36896v1
