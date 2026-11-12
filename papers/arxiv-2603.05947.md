# LucidNFT: LR-Anchored Multi-Reward Preference Optimization for Flow-Based Real-World Super-Resolution

- Paper ID: arXiv:2603.05947
- Authors: Song Fei, Tian Ye, Sixiang Chen, Zhaohu Xing, Jianyu Lai, Lei Zhu
- arXiv first upload: 2026-03-06 06:30 UTC, v1
- Current version: v4, submitted 2026-11-10 05:34 UTC
- First public listing of v4: 2026-11-11
- First covered in this archive: 2026-11-12
- Main theme: T04 — IQA/Reward/偏好决策
- Secondary themes: T03, T05, X01
- System roles: target, data, execution, evaluation, policy, training
- Map change: Supporting evidence; Boundary refinement
- Verdict: GO
- Canonical survey: [LR-Anchored Real-ISR Preference Optimization](../surveys/lr-anchored-real-isr-preference-optimization.md)
- Verification: v4 full text, reward design, ablations, benchmark results and human study checked; no independent reproduction performed.

## 30-second recall

LucidNFT在 flow-based Real-ISR 中同时优化感知质量与 LR-faithfulness：它训练一个 degradation-invariant 的 LR-referenced evaluator，并在每个 LR 条件下先分别归一化各 reward，再融合为 DiffusionNFT 更新所需的标量信号。

**记忆锚点：** 它的核心不是“再加一个 reward”，而是保留每个 reward 在同一 LR rollout group 内的相对差异，避免先混合再归一化抹掉目标冲突。

## 旧路线与关系

- DSPO（2025）把 human preference 引入 Real-ISR，使用 semantic instance alignment 和 user-description feedback 处理图像级偏好与局部异常之间的冲突。
- DiffusionNFT 是 LucidNFT 明确沿用的 policy update；LucidNFT 改造的是多 reward 到 scalar reward 的映射/归一化环节。
- 因此，LucidNFT 不是第一个把偏好优化用于 Real-ISR 的工作；它的增量是 LR-referenced faithfulness reward、decoupled reward normalization 和更大规模真实退化数据。

## 技术机制

1. LucidConsistency：以冻结的 Qwen3-VL-Embedding-8B 为基础训练 LoRA；85K LSDIR images 构建三等级 content-consistent degradation pools，37.7K original–inpainted pairs（来自 33.3K originals）作为局部 hallucination hard negatives。
2. LucidLR：20K unpaired real-world degraded images，覆盖 13 个 semantic categories、15 种 primary degradations，median resolution 1080×960，附逐图 license metadata，用于 RL fine-tuning。
3. Decoupled reward normalization：对每个 LR-conditioned rollout group 内的不同 reward 分别归一化，再融合，保留 objective-specific candidate contrast。
4. 使用 DiffusionNFT update 对 flow-based Real-ISR backbone 做 RL fine-tuning；不是新的在线 agent。

## 完整系统回忆卡

- **目标：** 在无可靠 HR ground truth 的 Real-ISR 中提高感知质量，同时不偏离 LR 输入证据。
- **非目标：** 通用 IQA、在线图像编辑 agent、自动决定 KEEP/RESTORE 的路由器。
- **输入：** LR 图像；训练时对每个 LR 采样多个 SR rollout。
- **输出：** 经 RL 优化的 flow-based SR 模型。
- **目标定义：** LR 输入提供可恢复内容边界；perceptual reward 定义视觉质量；human study 检查 LR-faithfulness。
- **执行表示：** flow-based Real-ISR generator；训练期多候选 rollout，不要求推理期保留候选集。
- **训练数据/监督：** LucidLR 约 20K 图像；LucidConsistency 使用 LSDIR 内容一致退化池和 inpainting hard negatives；RL 通过多 reward 反馈更新 generator。
- **评价：** RealLQ250、DRealSR、RealSR；多项 NR-IQA/一致性指标；v4 增加 reward-independent human study。
- **反馈：** UniPercept perceptual reward + LucidConsistency LR-faithfulness reward；每个目标先独立归一化再融合。
- **成本：** 论文报告 8 A100、600 RL steps、24 LR groups × 12 rollouts、768 resolution；另有 8B 级 evaluator。没有完整墙钟成本。
- **强基线：** 同 backbone 的 DiffusionNFT scalar-first reward、DPO/DSPO 类偏好路线和已有 flow-based Real-ISR。
- **Agent 控制层：** 无。reward 主要用于离线 RL 训练，论文没有在线 judge 选择候选的闭环。

## v4 更新与关键证据

**纠错记录 2026-11-12：** 依据 v4 arXiv HTML 的 Table 9，200 次 binary judgments 中为 72.5% 对 27.5%，且不允许 tie；此前草稿中的 17.5% / 10% tie 是不准确转录，已更正。

v4 新增 reward-independent human study：40 个 RealSR LR inputs、5 位 expert annotators、共 200 个 binary judgments；LucidNFT 输出在 72.5% 的 binary judgments 中被判定更忠实于 LR，baseline 为 27.5%；实验不允许 tie，Fleiss’ κ=0.415（moderate agreement）。这比仅用 LucidConsistency 自身分数评价更有价值，但样本量仍小。

作者还报告在 8 个 Real-ISR 方法、3 个真实退化测试集上取得感知质量提升，并通常保持 LR-referenced consistency。

## 批判性评审

- **主要收益来源：** evaluator、LucidLR 数据和 decoupled normalization 同时改变；不能把全部增益归因于 reward normalization。
- **指标风险：** LucidConsistency 同时参与训练和部分评价，存在 reward/metric self-reference；v4 的 human study 缓解但没有消除该问题。
- **公平性：** 需要确认各方法的 backbone、rollout 数、RL budget 和 reward access 一致；作者结果不是独立复现。
- **边界：** human study 只有 40 inputs/5 experts；没有大规模消费者偏好；极端退化时 LR 本身可能不包含足够证据；learned reward 仍可能被 generator exploit。
- **共识：** Real-ISR 正在从单一 perceptual reward 转向多目标 faithfulness/perceptual alignment，但尚不能称为共识。

## 判断与行动

GO。v4 的关键更新是独立 human preference 证据，不是新 RL 算法。保留“感知质量”和“LR-faithfulness”两个目标，避免先混合再归一化。不要把该工作误当作在线候选选择器或 Agent；它是离线 reward model + RL training pipeline。

## References

- [LucidNFT v4, arXiv:2603.05947](https://arxiv.org/abs/2603.05947)
- [DSPO, arXiv:2504.15176](https://arxiv.org/abs/2504.15176)
