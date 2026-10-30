# Of Chains and Gains: What Reinforcement Learning Changes on Reasoning-based Image Quality Assessment

## 快速回忆

- **首次公开**：2026-10-23（arXiv v1；当前可核验版本日期另行检查）
- **主题**：IQA / RLVR audit
- **核验范围**：selected_sections_checked；independent replication = not performed
- **一句话**：RLVR 能提高 IQA 打分，却不证明分数真正依赖显式 CoT；增益的映射部分主要集中在分布内，且奖励会学到与画质无关的 MOS 线索。

## 精读记录

### 机制与证据

作者在 Qwen2.5-VL 7B/32B 上，用 KADID-10k 与 KonIQ-10k 训练，另测 SPAQ、AGIQA-3K、CSIQ。每图采样 512 次，用 max_g@k 区分采样覆盖与能力；再做链交换、空链/乱序、链移植、隐藏状态方向干预和人为文本捷径实验。RL 模型在 k=512 仍高于 base，但平均采样可在 OOD 缩小甚至消除单次增益；链可用性提高，实际打分对链的依赖反而不一定增强。

### 限制与竞争解释

这是受控机制审计，不是新 SOTA IQA 模型。512 次/图与 4,096 token 上限成本极高；结论限于所测 Qwen2.5-VL、两种 RLVR 配方和数据集。人为文本线索证明“可被利用”，不等于所有现有 IQA 训练都已泄漏。未找到可核验的官方代码。

### 下一实验

对任何 CoT-IQA/RL-IQA 先跑三件套：去链/换链、MOS/数据源线索置乱、跨传感器 OOD；报告平均多采样基线，不把更像解释的文本当作因果解释。

## References

- https://arxiv.org/abs/2610.33203v1
