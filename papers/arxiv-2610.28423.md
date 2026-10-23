# WorldSR: Harnessing World Knowledge Search for Grounded Image Super-Resolution

## 快速回忆

- **首次公开**：2026-10-20（arXiv v1；按本轮可核验来源）
- **主题**：Restoration / Agent
- **核验范围**：selected_sections_and_project_checked；independent replication = not performed
- **一句话**：把外部世界知识从模型隐式参数移到显式检索：先拆实体，再找结构/语义对齐的参考图，经筛选和记忆后约束多参考 SR。

## 精读记录

### 机制与证据

Agentic ROI Planner、memory verifier、web/local retrieval、质量/语义过滤和 multi-reference SR 组成迭代流程。论文声称在真实 SR 基准提高结构保真与感知质量，且以实体级对齐减少无约束生成。

**证据范围**：论文选定章节、项目页和受门槛保护的 Hugging Face results 页；NeurIPS 2026 接收见 arXiv comments。作者页/论文显示 HONOR Device Co., Ltd. 署名。未接受数据门槛条款，未下载文件或复现。

### 限制与竞争解释

检索依赖实体分解、语料覆盖与参考歧义，成本与隐私边界未解决；NR-IQA 增益不证明细节真实。它是检索增强 SR，不是可预测动作后果的 world simulator。

### 下一实验

做有/无正确实体命中、错误近邻和无结果三组压力测试；以 OCR/人脸/重复纹理的事实错误率和总延迟/网络成本为主。

## References

- https://arxiv.org/abs/2610.28423
- https://gwanjyun.github.io/worldsr.github.io/
- https://huggingface.co/datasets/gwanjyun/worldsr_results
