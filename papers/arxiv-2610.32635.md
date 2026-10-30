# EditJev: System One Routing for Image Editing Models

## 快速回忆

- **首次公开**：2026-10-23（arXiv v1）
- **主题**：Agent / Editing routing
- **核验范围**：selected_sections_checked；independent replication = not performed
- **一句话**：在编辑前用单次 VLM 前向直接预测候选编辑器偏好，再与模型级速度先验组合；这是样本级工具路由，不是执行后验证。

## 精读记录

### 机制与证据

路由器在 VLM backbone 上接固定维度偏好头，离线执行全部候选编辑器并由 MLLM judge 构造 gap-filtered pairwise preferences。路由前向约 94 ms。ImgEdit/GEdit-En 上，作者报告相对最强固定编辑器质量 4.540→4.592、8.194→8.255，同时按候选模型平均端到端时间估算时延下降 60.8%/31.7%。

### 限制与竞争解释

速度是模型级平均值与路由开销的估算组合，不是设备上的请求级实际排队、加载、峰值内存、功耗或热测量。监督和评价都依赖 MLLM judge，可能继承选择、身份与顺序偏差；候选池改变后偏好头需要更新，且小幅质量增益未证明对新编辑器/新域稳健。未找到可核验代码。

### 下一实验

用人工 pairwise 子集和结构化 evaluator 双审；按请求测冷/热启动、内存与 P95，并做候选池 leave-one-model-out 和新版本漂移；与 always-best、成本阈值、执行后 verifier 路由比较。

## References

- https://arxiv.org/abs/2610.32635v1
