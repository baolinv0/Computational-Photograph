# 已知测量算子的生成式反演：采样、训练与可信约束

版本 v0.1 | 2026-11-10 | 主 T03，连 T01/T04/X01。原论文核验范围按各 canonical card；作者结果≠独立复现。

目录：[问题边界](#问题边界) · [竞争路线](#竞争路线) · [证据与判断](#证据与判断) · [完整方案](#完整方案) · [覆盖缺口](#覆盖缺口) · [References](#references)

## 问题边界
有受损观测 `y=A(x)+n`，以及可调用的前向算子 A/噪声模型，如何充分利用生成先验恢复 x 而不让数据一致性优化把生成器推离可用分布？任务是**已知或足够准确的算子下的反问题**，不是未知 ISP 条件下无约束 photofinishing。保持「观测拟合」「结构保真」「纹理生成」「计算成本」四个独立判断轴。

记忆锚点：**符合 y 的 x 不一定像真图；像真图的 x 不一定符合 y。优化中的扩散状态本身也要位于先验支持的区域。**

## 竞争路线

| 路线 | 在线输入与控制变量 | 离线训练/先验 | 优势/风险/强基线 |
|---|---|---|---|
| 手工或判别式先验 | y、A→TV/regularized least squares或任务模型 | 无需大扩散 prior 或 paired clean GT | 最便宜强基线，难处理多模态缺失 |
| 分步 measurement guidance | y、A→DPS、DDRM（线性） | unconditional pre-trained diffusion | 容易实现，但弱近似/算子限制 |
| annealed x0 搜索 | DAPS，直接选 clean x0/后验 Langevin | pretrained diffusion | 长链、多优化；采样精细但昂贵 |
| annealed denoiser-input 搜索 | SITCOM，在 x_t 空间优化测量拟合 | 同上 | 能探索非线性解，却可能出现 `radial drift` |
| **锚定 forward-noise 搜索** | [FANO](../papers/arxiv-2611.08923.md)：固定 previous x estimate，优化 `e`、半径 `r` | 同一 DDPM，无 task fine-tune | 研究新变量及 Gaussian shell，数十层×梯度反传，非移动实时 |
| operator-aware trained posterior flow | [BAM](../papers/arxiv-2609.39660.md)、[Dual Flow](../papers/arxiv-2611.05843.md) | 可能需要显式 operator conditioning / training | 可用少步，但增加训练、接口与分布转移假设 |

其中 **FANO 直接讨论且引用 DAPS/SITCOM/FAST-DIPS/DiffRGD/INO**；与 BAM、Dual Flow 的并列属于本文献地图的分析者综合关系，不表示直接继承或作者相互比较。

## 证据与判断
此前总图强调引入已知 `A` 可以补充条件、减少幻觉，但没有细分**测量拟合过度优化导致先验失配**。FANO 2026-11-06 v1（PROBE，Boundary refinement）在 FFHQ/ImageNet 256² 100/域、模拟观测 Gaussian σ=0.05 上提供新反例：SITCOM 后期观测 residual 下降时 HDR/NL deblur PSNR 反而下降，噪声范数的偏移与失真相伴。作者通过零测量噪声、半径固定、极坐标 vs 欧氏噪声优化控制，支持问题不是简单 measurement-noise overfitting。

FFHQ HDR（clip factor 2）PSNR：DAPS 27.48、SITCOM 28.13、FANO 29.88 dB；FANO-Sphere 29.06、FANO-Euc 29.18，显示**e-search 是主要增量，polar/radius HDR 也有增益**；非线性模糊三 FANO 变体仅 0.11dB 差距。不同任务和模型不是普遍性定理。N=50、K=30 的内层上界 1500 denoiser forward+backward，显著不同于 Dual Flow 的少步/速度情境；不能把本分支命名为部署加速。

判断更新：之前「增加数据一致性约束可能有利」，现在追加「数据一致性优化的变量选择和 prior distribution 几何可以成为独立失败原因」。不变：测量 consistency 不能恢复未采集的真实细节，也不证明 sensor RAW、曝光/GT 实体成立条件；移动实时后端仍以确定性轻量算子为优先对照。

## 完整方案
**目标**：已知 A 下的可信 x；非目标：替代未知相机 CCM/AWB/Tone Mapping 风格映射。
**在线**：y+校准 A+噪声 law→预训练生成先验→选择 (a) stepwise guide，(b) annealed x/ε search，或 (c) operator-trained posterior flow→x_hat→测量一致性 + GT fidelity/LPIPS/结构验证。对 A mismatch 的偏差另作敏感性评估。
**离线**：模拟物理观测+真实配对 clean GT（若有）→固定模型/算子/预算对比→已知 A 的同域/真实相机外域评估。
**Agent**：不是必须；若加入，只可选择算子或接受/回退，不代表这些论文验证 Agent+posterior 集成。
**最小判别**：FFHQ/HDR 模拟上，在 SITCOM 不变 budget 下加 late-layer norm clamp，再比较 FANO-Sphere 和 FANO 完整，记录每一层 residual/PSNR 与峰后崩塌率。必须记录实际 GPU 时间。

## 覆盖缺口
DAPS、SITCOM、DiffRGD、INO、BAM、Dual Flow 的完整 matched-budget 复审尚未完成；真实 Bayer/Poisson-Gaussian、未知 CCM/TM、跨相机/真实传感器没有实证，不可自拟。大分辨率显存和 runtime 需作者/独立实机测试，剩余候选在本页继续 backfill。

## References
- [FANO 2611.08923v1](https://arxiv.org/abs/2611.08923v1) · [详细卡](../papers/arxiv-2611.08923.md)
- [Dual Flow](../papers/arxiv-2611.05843.md) · [BAM](../papers/arxiv-2609.39660.md)
- [既有高效生成式恢复](efficient-generative-restoration.md)
