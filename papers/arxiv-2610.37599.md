# MoI-Bench: A Benchmark for Image Generation and Editing on Mobile Devices

## 快速回忆

- **首次公开**：2026-10-27（arXiv v1）
- **主题**：IQA / Mobile generation and editing
- **核验范围**：selected_sections_and_author_project_checked；independent replication = not performed
- **一句话**：把移动图像生成/编辑拆成 Operation × Target × Criterion，并把质量与真实设备端到端时延、峰值内存、部署体积保留为二维，而不是揉成单一分数。

## 精读记录

### 机制与证据

基准有 64 个子任务、1,150 个样本、16 种操作和 8 类目标，评价 instruction following、visual quality 与 detail preservation。19 个模型用 GPT-4o 主裁判并由 Gemini 3.1 Pro 复评；设备侧在 iPhone 17 Pro（Core ML/MLX）和 Xiaomi 15 Pro（ONNX Runtime + Qualcomm QNN HTP）测端到端生成、峰值内存和部署体积。DreamLite/Ovis-U1 质量为 Q2，Mobile-O 与 DreamLite 达 D3，无模型达 D4；DreamLite 1024² T2I 为 iOS 3.22 s、Android 18.19 s。数据与评测/推理工具项目页已公开。

### 限制与竞争解释

只有 DreamLite 成功部署编辑，跨模型共同部署任务实际是 T2I；因此“移动编辑可部署性”仍缺同条件系统对比。每样本只生成一次，主评价依赖两个闭源 VLM judge；未测能耗、热稳态、P95 尾延迟和长期内存抖动。未支持任务按零分处理适合覆盖率决策，却不能当作模型已支持任务的纯质量排名。

### 下一实验

把 64 子任务压成可维护的回归套件，先复现身份保持、文字替换、多人参考编辑三类失败；在同一设备、同一分辨率、同一运行时下补 P50/P95、能量/帧和 10 分钟热降频。

## References

- https://arxiv.org/abs/2610.37599v1
- https://carlofkl.github.io/MoI-Bench-project/
