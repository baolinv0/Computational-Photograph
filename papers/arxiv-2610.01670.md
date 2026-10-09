# EditJudgeBias：图像编辑评审器的线索偏置与顺序敏感性

- **身份**：arXiv:2610.01670
- **首次公开（已核）**：2026-10-01，v1
- **本次核验**：2026-10-09；selected sections checked
- **独立复现**：未进行

## 快速回忆

**问题**：多模态 judge 常被当作编辑 reward 或自动验收器，但可能依赖脆弱视觉线索和候选顺序。

**机制**：1,196 个真实编辑样本、13 类诊断线索、5 个 judge；以校准验证器和人工核查测试 cue reliance 与 position bias。

**证据**：作者报告交换候选顺序可使偏好反转最高达 60.9%。这直接影响 reward model、agent verifier 和自动回归测试的可信度。

**决策边界**：结论限于所测 judge、提示和编辑样本；验证器本身也可能遗漏错误。不能推出所有 LMM evaluator 都不可用。

**下一步**：所有编辑/恢复评测先做顺序随机化、盲化、多轮一致性与人审审计；把诊断维度输出保留为结构化 evidence，不只保留总分。

## 精读记录

- **决策含义**：自动 evaluator 进入训练闭环前，应通过 swap、cue ablation、adversarial negatives 和跨模型交叉检查。
- **竞争解释**：部分反转可能来自提示格式、长度或答案解析，而非视觉偏差；需要控制序列化和解码设置。
- **产品含义**：适合作为内部评价基础设施的“评委体检”，不是新的 IQA 单分数。

## References

- [arXiv abstract / v1](https://arxiv.org/abs/2610.01670)
