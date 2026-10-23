# Interpretable Face Contrast Modeling for Smartphone Portrait Rendering

## 快速回忆

- **首次公开**：2026-10-19（arXiv v1；按本轮可核验来源）
- **主题**：Color / IQA
- **核验范围**：selected_sections_checked；independent replication = not performed
- **一句话**：把“人脸对比度”拆成整体明暗分离、眼区对比、皮肤微对比三个可解释维度，并用成对人评验证；这是比单一美学分数更可行动的手机人像 evaluator。

## 精读记录

### 机制与证据

在受控几何/照明下，用两种肤色的高保真人台与 29 款手机采集 508 张全分辨率图像，建立区域 mask 和分维度 pairwise judgments；三个指标组合用于建模 balanced facial contrast preference，并在较小真人集上做初步外推。

**证据范围**：论文选定章节；WACV 2027 接收见 arXiv comments。无厂商作者归属，数据来自多厂商手机。未独立复现。

### 限制与竞争解释

人台使主体、姿态与表情受控，也限制真实肤色、妆容、运动和社会偏好外推；真人验证规模较小。对比度相关性不是整体 portrait IQ，更不是跨文化偏好共识。

### 下一实验

先复现 device-wise 排序，再加入真实多肤色/年龄/妆容、HDR 显示和不同观看环境；分离 tone curve、local contrast 与锐化/降噪混淆。

## References

- https://arxiv.org/abs/2610.26517
