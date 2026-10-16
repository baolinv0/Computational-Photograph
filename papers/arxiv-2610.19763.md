# Physics-Shaped, Not Physical：物理引导水下恢复的审计

- **身份**：arXiv:2610.19763
- **首次公开（已核）**：2026-10-14，v1
- **本次核验**：2026-10-16；full paper review
- **独立复现**：未进行

## 快速回忆

**问题**：预测 transmission/backscatter 的网络可能提升恢复分数，却未学到物理上有效的中间量。

**机制**：对 PhysGuide-Net 做五 seed、数据效率与容量匹配对照，并在 LSUI/AUIED3K zero-shot 与 Sea-thru measured-range 上分开审计恢复收益和物理参数有效性。

**证据**：作者发现某些低数据收益存在，但多数在多重比较校正后不显著；物理中间量的有效性不能由最终图像分数代替。

**决策边界**：只审计一种架构、800 张训练图、256×256；Sea-thru 有迁移/域差。不能由此否定全部 physics-guided restoration，也未评价 downstream/perceptual outcomes。

**下一步**：将同样审计扩展到多种架构、真实传感器数据与下游任务；强制报告多 seed、容量匹配、物理量校准和跨域区间。

## 精读记录

- 负面价值在于把“结构像物理模型”和“中间量物理有效”拆开。
- 这类审计应成为物理引导恢复的最低证据门槛，而不是只看最终 PSNR/感知分。
- **可能关联**：适合转化为 ISP/恢复模块的机制验证清单，避免从漂亮中间图反推可解释性。

## References

- [arXiv abstract](https://arxiv.org/abs/2610.19763)
- [arXiv HTML v1](https://arxiv.org/html/2610.19763v1)
