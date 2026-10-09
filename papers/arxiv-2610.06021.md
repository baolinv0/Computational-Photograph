# ARRO：面向最小改动图像编辑的 agentic VLM reward

- **身份**：arXiv:2610.06021；作者标注 NeurIPS 2026 accepted
- **首次公开（已核）**：2026-10-05，v1；更早 OpenReview 公开时间未核实
- **本次核验**：2026-10-09；selected sections + author repository checked
- **独立复现**：未进行；代码尚未发布

## 快速回忆

**问题**：编辑模型常完成目标修改，却同时破坏背景、身份或未指定区域；单一视觉相似度不足以指导最小改动。

**机制**：VLM reward 先 Audit 未实现修改和非目标变化，再以组级 rubric 聚合，并验证候选问题；训练目标围绕可解释失败项构造。

**证据**：作者报告 FLUX.1 Kontext-dev 在四个 benchmark 上 EditScore 5.21→5.88、600 例 off-target pixel change 降低 8.4%，并给出盲测人评与 OmniGen2 transfer。

**决策边界**：一次组级 reward 在 N=16 设置需 2N+1 次推理，论文示例使用独立 A100 80GB 承载 VLM/LLM，约 16.06 s/group。作者仓库仅 README，明确 code coming soon；尚不可复现。

**下一步**：先复做 judge-order、prompt、reward hacking 和跨 judge 稳定性；再比较同预算区域掩码、CLIP/DINO、像素/特征约束与人类审核。

## 精读记录

- **战略含义**：结构化“应改/不应改”rubric 比总分更接近可行动 evaluator，但成本和 judge 偏差必须显式预算。
- **竞争解释**：提升可能来自更强视觉语言监督或更高推理预算，不一定来自 agentic aggregation 本身。
- **产品含义**：更适合离线训练与高价值审核，不适合直接推断为移动端在线评价器。

## References

- [arXiv abstract / v1](https://arxiv.org/abs/2610.06021)
- [作者仓库（当前仅 README）](https://github.com/Showwwwwwwww/ARRO)
