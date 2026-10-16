# Look Before You Restore：执行前预测的恢复 Agent

- **身份**：arXiv:2610.20384
- **别名**：PreActIR
- **首次公开（已核）**：2026-10-14，v1
- **本次核验**：2026-10-16；full paper + author repository checked
- **独立复现**：未进行

## 快速回忆

**问题**：混合退化恢复 agent 通常执行工具后才知道效果，失败调用浪费算力，伤害输出发现过晚。

**机制**：tool-conditioned world model 在执行前预测残余退化、质量、保真、伤害与不确定度；执行后由独立 verifier 决定 commit/rollback。离线 reference-based candidate-frontier audit 区分 selector 与工具池上限。

**证据**：固定工具池、verifier 与预算的 matched replay 中，作者报告调用减少 42.5%、被拒调用减少 63.4%、PSNR +0.92 dB。仓库含实现、transition-data builder、训练/推理/评测脚本与 tests。

**决策边界**：这些数字依赖 reference-annotated states 与固定候选池，不是无参考真实部署保证。仓库 debug pipeline 明确只是合成 smoke test；未核验训练权重已发布。

**下一步**：在隐藏真值的真实混合退化集上固定总预算，对比 execute-first、oracle selector 与 no-rollback；单独记录 verifier 漏检、文字/身份变化、每工具端到端成本。

## 精读记录

- 真正可迁移的不是具体工具，而是“预测—执行—提交/回滚”的风险控制接口。
- 世界模型若与 verifier 共享偏差，会同时高估收益与低估伤害。
- **可能关联**：可直接转化为恢复流水线的离线 counterfactual audit 与运行时拒绝策略。

## References

- [arXiv abstract](https://arxiv.org/abs/2610.20384)
- [arXiv HTML v1](https://arxiv.org/html/2610.20384v1)
- [Author repository](https://github.com/House-yuyu/PreActIR)
