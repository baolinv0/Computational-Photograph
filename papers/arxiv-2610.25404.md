# MT Forcing: Towards Stable and Consistent Multi-Turn Image Editing with Autoregressive Diffusion

## 快速回忆

- **首次公开**：2026-10-18（arXiv v2；按本轮可核验来源）
- **主题**：Editing / Agent
- **核验范围**：selected_sections_and_repository_checked；independent replication = not performed
- **一句话**：让多轮 editor 在自己产生的历史上训练，同时由“把累计意图一次做完”的 teacher 提供无递归误差的质量目标；另用 reference trajectory 约束跨轮一致性。

## 精读记录

### 机制与证据

Single-Turn DMD 对 student self-rollout 做分布匹配；Teacher-Forcing Guidance 用参考轨迹 warmup 并在蒸馏期正则。MTEdit-Bench 100 个八轮 session 上，从第 4 轮起四指标均改善；SenseNova-U1.5 第 8 轮 IF/CC 分别提升 4.65/4.46。

**证据范围**：论文选定章节、项目页、源码仓库和 Hugging Face 文件页；v1 2026-10-18，v2 2026-10-21。HF 列出 70.1GB model.safetensors，未下载验证。

### 限制与竞争解释

100 个八轮 session 与 failure-triggered IF/CC 计分规则不等于任意长度稳定；共享 judge 可能偏向 teacher 风格。大权重、训练和推理成本未给手机可行性。

### 下一实验

在身份、文字、相机几何和局部未编辑区建立 turn-wise factual error；比较等算力 rollout、packed trajectory 与 MT Forcing。

## References

- https://arxiv.org/abs/2610.25404
- https://houyuanchen111.github.io/mt-forcing.github.io/
- https://github.com/houyuanchen111/MT-Forcing
- https://huggingface.co/houyuanchen/MT-Forcing/tree/main
