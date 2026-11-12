# LR-Anchored Reward and Preference Optimization for Real-World Super-Resolution

- Last updated: 2026-11-12
- Main themes: T04
- Secondary themes: T03, T05, X01
- Status: new living survey; integrates DSPO and LucidNFT v4
- Scope: preference/reward optimization for generative Real-ISR when paired HR ground truth is unavailable or unreliable.

## 1. Stable problem definition

Generative Real-ISR can create perceptually convincing high-frequency detail, but the LR input does not uniquely determine all generated details. The central optimization problem is therefore multi-objective:

- improve perceptual quality;
- preserve semantic, geometric and photometric evidence supported by the LR input;
- avoid hallucinated structures that are visually plausible but unsupported.

The key distinction is between **perceptual quality** and **LR-faithfulness**. A single scalar NR-IQA score is not guaranteed to represent both.

## 2. Competing routes

| Route | Representative work | Preference/reward signal | Optimization | Main contribution | Boundary |
|---|---|---|---|---|---|
| Human preference + semantic alignment | DSPO (2025) | Human preference plus instance-level semantic guidance and user-description feedback | Direct Preference Optimization | Adapts image-level preferences to local semantic consistency | Preference data and semantic feedback are costly; local anomalies can dominate |
| Multi-reward policy optimization | DiffusionNFT (base optimizer used by LucidNFT) | Scalar reward after combining candidate scores | Negative-aware fine-tuning | Policy update for generative restoration | Early scalarization can erase per-objective contrast |
| LR-anchored multi-reward optimization | LucidNFT v4 (2026) | UniPercept perceptual reward + LucidConsistency LR-faithfulness | Per-LR rollout-group reward normalization, then DiffusionNFT update | Separates reward axes before fusion and adds a learned LR-referenced evaluator | Reward/metric self-reference, small human study, no standard LR-faithfulness benchmark |

## 3. Historical anchors and relationships

- **DSPO (2025):** explicitly introduces human preference alignment into Real-ISR and uses semantic instance alignment plus textual feedback to mitigate hallucinations.
- **DiffusionNFT:** LucidNFT explicitly retains its policy update and redesigns the reward normalization/fusion stage.
- **LucidNFT v4 (2026):** adds LR-referenced faithfulness evaluation and a reward-independent human study.

The relation to DiffusionNFT is explicit inheritance of the update rule. The relation to DSPO is competitive/complimentary: both address alignment, but DSPO is DPO over human preference with semantic feedback, while LucidNFT uses learned LR-faithfulness and multi-reward RL.

## 4. LucidNFT v4: evidence and critical boundary

LucidNFT introduces:

- **LucidConsistency:** a degradation-invariant LR-referenced evaluator, trained with content-consistent degradation pools and inpainting hard negatives to detect localized hallucination;
- **LucidLR:** about 20K real-world degraded images for RL fine-tuning;
- **decoupled reward normalization:** normalize each reward within each LR-conditioned rollout group before fusion;
- **DiffusionNFT update:** reused rather than replaced.

The v4 human study uses 40 RealSR LR inputs and 5 expert annotators, producing 200 binary comparisons. LucidNFT outputs are judged more LR-faithful in 72.5% of 200 binary judgments, versus 27.5% for LucidFlux; ties were not allowed and Fleiss’ κ is 0.415.

The study is useful because it is independent of LucidConsistency's own score, but it is still small. The paper also evaluates 8 Real-ISR methods across RealLQ250, DRealSR and RealSR.

## 5. Full system reconstruction

### Online inference

LR image → trained flow-based Real-ISR generator → SR output.

The reward evaluator is not required at inference. The paper does not implement an online agent that generates many candidates and selects one with a judge.

### Offline data and training

1. Build LucidConsistency from content-consistent degradation pools and inpainting hard negatives.
2. Build LucidLR to expand real degradation coverage.
3. For each LR input, sample multiple SR rollouts.
4. Compute perceptual and LR-faithfulness rewards separately.
5. Normalize each reward within the LR-conditioned group.
6. Fuse normalized rewards and update the flow model using DiffusionNFT.

Reported RL setup: 8 A100 GPUs, 600 RL steps, 24 LR groups × 12 rollouts per step, 768 resolution. Full wall-clock training cost is not reported.

### Agent/control layer

No online agent. This is an offline reward-model and policy-optimization pipeline. It does not decide KEEP/RESTORE/REJECT and does not solve executor candidate accessibility.

## 6. Evidence and failure boundaries

- **Author claim:** perceptual quality improves while LR-referenced consistency is generally maintained; human raters prefer the output for LR-faithfulness in 72.5% of comparisons.
- **Local evidence:** 8 methods, 3 real-world benchmarks, one 40-input/5-expert human study, ablations of reward components and normalization.
- **Strong alternative explanation:** gains may be due to the evaluator, LucidLR data and RL budget jointly; they cannot be attributed only to decoupled normalization.
- **Metric risk:** LucidConsistency is used for training and some evaluation, so the reward and metric are not fully independent. The human study reduces but does not remove this concern.
- **Data risk:** LucidLR and degradation pools may not cover all sensor pipelines and extreme degradations.
- **Cost:** 8 A100 RL training and an 8B evaluator; not a lightweight deployment method.
- **Not established:** robust behavior under severe information loss, large-scale consumer preference alignment, or a universal LR-faithfulness metric.

## 7. Practical design implications

- Keep perceptual quality and LR-faithfulness as separate objectives until after per-objective normalization.
- Evaluate hallucination at semantic and local-structure levels; do not infer LR faithfulness from NR-IQA.
- Treat reward models as training signals, not automatically as trustworthy online judges.
- Measure executor accessibility, candidate discoverability and judge selectivity separately. LucidNFT mainly changes the offline training reward; it does not address online candidate search.

## 8. Current judgment

LR-anchored reward is a useful research direction for generative Real-ISR. LucidNFT v4 strengthens the evidence with a small reward-independent human study, but it does not establish a universal reward or an online restoration agent.

## References

- [DSPO, arXiv:2504.15176](https://arxiv.org/abs/2504.15176)
- [LucidNFT v4, arXiv:2603.05947](https://arxiv.org/abs/2603.05947)
