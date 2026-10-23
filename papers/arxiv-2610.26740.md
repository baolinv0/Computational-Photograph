# CheckDistill: Adaptive Checklist Distillation for Efficient Distributional Reward Modeling in Image Editing

## 快速回忆

- **首次公开**：2026-10-19（arXiv v1；按本轮可核验来源）
- **主题**：IQA / Reward model
- **核验范围**：selected_sections_checked；independent replication = not performed
- **一句话**：训练时让 teacher 用任务自适应 checklist、逐项 judgment 和 rationale 审查编辑，再把这种多维证据压进 student 的直接分布式评分；部署时不需要长推理。

## 精读记录

### 机制与证据

CR-OPSD 用 teacher-label agreement 作可靠性权重进行 on-policy self-distillation。9B 配置在 MMRB2/MER-Bench/EditReward-Bench 报告 72.30%/56.67%/82.90%；约 10 输出 token，高于约 700-token reasoning 配置。其 reward-guided RL 在三个编辑基准上相对 base 有小幅提升。

**证据范围**：全文选定章节；当前仅 v1。代码/权重未找到已核实公开入口，未独立复现。

### 限制与竞争解释

三组准确率不可合并为通用正确率；teacher agreement 只是可靠性 proxy，不能排除共同偏差和 reward hacking。自动 judge 提升不等于身份、文字与未编辑区事实保真。

### 下一实验

先做 candidate swap、prompt cue、肤色/人脸吸引力、文字和最小改动审计；比较 checklist student 与同 token 预算强 baseline。

## References

- https://arxiv.org/abs/2610.26740
