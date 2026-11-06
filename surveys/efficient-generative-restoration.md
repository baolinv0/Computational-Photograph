# 高效生成式图像恢复：少步能力从哪里来？

版本 v0.1 | 首次建图 2026-10-24 | T03 / X01（跨 T01 低光）

目录：[一分钟回忆](#一分钟回忆) · [路线地图](#路线地图) · [横向证据](#横向证据) · [系统方案](#系统方案) · [判断与缺口](#判断与缺口) · [References](#references)

> Living survey，围绕恢复生成器的**训练目标、执行步数、潜空间与成本**组织，不是“一步模型列表”。首次由 GLOW-FM 的公开 v1 及其原文前序搭建；其余锚点并未在本轮逐篇全文复核，不能宣称穷尽或社区共识。

## 一分钟回忆

关键问题不是「一步是否比多步先进」，而是 **在源图可观察内容、生成自由度、质量与完整推理预算固定时，计算该分配给哪些步骤/表示？**

- **多步恢复**：Diff-Retinex / PyDiff 等，迭代控制更细，但 NFE 与重复计算高。
- **蒸馏少步**：ReDDiT（论文 GLOW-FM 所列对照 2 NFE），从 Teacher 轨迹迁移生成能力；受蒸馏目标和数据覆盖限制。
- **潜空间低层恢复**：ELIR / GLOW-FM，先减少自动编码器开销，再重新设计少步监督；低分辨率 latent 不代表原生 4K 恢复。
- **频域分工**：WCDM（论文列 10 NFE），将不同频率/结构信息安排至不同路径；相比纯训练加速，架构变化更明显。
- **直接一步传输**：GLOW-FM 在已发表 TVM 上增加 LLIE 端点条件运输；匹配 backbone 的 TVM vs MeanFlow/ConsistencyFM 才能部分隔离目标函数贡献。

## 路线地图

```text
低光观测（LQ）
  ├─ 判别式一步映射：Retinexformer / HVI-CIDNet / Multinex
  ├─ 生成式多步：Diff-Retinex / PyDiff / WCDM
  ├─ 教师蒸馏少步：ReDDiT
  └─ 潜空间直接迁移：ELIR / MeanFlow-like / TVM → GLOW-FM
                                                        ↓
                         PSNR / LPIPS / NIQE / MOS / source fidelity
                                                        ↓
                         设备时延、内存、能耗与预后处理成本
```

图示比较同一**低光增强目标**的竞争机制；并非这些方法都共享相同任务或训练源。

## 横向证据

GLOW-FM 原文 Tables 1, 3, 5 是本轮直接核验的主来源，详情见 [GLOW-FM card](../papers/arxiv-2610.31222.md)。

| 机制对照 | 作者报告（限定条件） | 不可推出 |
|---|---|---|
| TAESD + TVM vs TAESD + MeanFlow/ConsistencyFM | LSD-DLL、共同 48 GFLOPs / 124M 骨干：PSNR 20.3 vs 19.5 / 19.4 dB | TVM 对所有恢复任务和尺寸通用最优 |
| TAESD TVM vs SD-VAE TVM | LSD-DLL：TAESD 48 GFLOPs / PSNR 20.3；SD-VAE 471 GFLOPs / PSNR 19.6，但后者 MUSIQ 更高 | 小 VAE 在全部感知维度最好 |
| 判别式与生成式 | UHD-LOL4K 上 HVI-CIDNet PSNR 33.7 dB，GLOW-FM-S 30.3 dB | 一步生成已全面取代判别式恢复 |
| 数据规模 | GLOW-FM 将 LSD-DLL 对数增大时 PSNR 随之提升（论文 Fig.5） | 仅 TVM 解释跨域提升；仍有数据规模因素 |

表格中的 source fidelity 和实际手机部署是 **待验证问题**。作者对 DICM/LIME/MEF/NPE/VV 等无 GT 域主要报告 NR-IQA，不能当作内容准确性证据。

## 系统方案

**在线**：RGB 低光 → 观测/风险诊断 → 判别式 baseline 或少步生成增强 → 输出 → 事实保持与感知评价。除非额外设计 Router，否则两条是备选执行器而非必需联合链。

**离线**：真实配对或可审计的生成监督 → 匹配预算训练目标消融 → 可观察 GT 与无 GT 分层独立测试 → 同精度同输入尺寸比较完整设备延迟。生成器的 NFE 不等于完整时延，尤其 VAE 编解码不可忽略。

## 已知物理算子的少步联合流：与低光增强并行的 inverse-problem 分支（2026-11-06）

**问题边界**：此前“一步”路线大多从 LQ RGB 学映射或潜空间运输，不显式接收当前拍摄的线性前向算子。本分支讨论已知 **y=Ax+n** 的反问题与 posterior 采样，任务条件不同，不能仅比较 NFE 就声称某方法优越。

| 竞争路线上下文 | 在线输入与状态 | 物理监督与训练 | 证据/失败边界 |
|---|---|---|---|
| 常规单步判别式/生成式 LLIE（GLOW-FM 等） | RGB LQ → RGB HQ | paired GT/潜空间目标；通常不显式要求 A | 强在快速特定任务；不自动满足相机 forward consistency |
| 已知算子条件化后验（[BAM](../papers/arxiv-2609.39660.md)） | y+A → posterior flow samples | operator-conditioned 生成训练 | 少步、主要已知 A；与下行工作为共同机制而非证实直接继承 |
| PnP-Flow / Flower / OT-ODE | y、A 与 learned prior → 多次逆求解 | 先验+后验/数据一致性更新 | 可显式约束物理，但 NFE、超参和假定 A 精确度重要 |
| **[Dual Flow](../papers/arxiv-2611.05843.md)** | y 初始化 measurement state；与 image state 同步 evolve | 联合 x/y flow、operator-dependent correlated Gaussian denoising sufficient statistic | 在已知线性 A/高斯噪声的 CelebA 模拟上作者有优势；无法推出未知 ISP、真实 shot noise、mobile latency |

**2026-11-04 v1 新证据**：Dual Flow 作者 Table I 的 100 张 CelebA/五种线性逆问题报告 Dual Flow-T 0.18s/image；与 PnP-Flow1 0.99s 的比较含具体作者实现及实验硬件，不是跨平台复杂度定理。它同时估计 clean image 和 noise-free measurement，强制结束时 y_hat=A x_hat；该物理一致性**不保证未知真实纹理被正确恢复**。Multi-trajectory mean 可改善 PSNR 同时牺牲部分 LPIPS，必须区分 distortion 与感知效果。

**判断更新**：从“少步生成是否够快”拓展出**先验运算预算 vs 可核验测量约束**两轴。对于已知 forward operator，优先尝试在相同 A/噪声假设下比较 Dual Flow/PnP/BAM，而不是把它作为低光 image enhancement 的即插即用模块。已有 GLOW-FM 的 RGB LLIE 1-NFE 性价比结论保持不变。

**完整方案**：离线已知 A+标定噪声/clean x 训练 joint-flow / 等预算 baseline；在线 y、A→image/measurement joint sampling→x_hat，再在 y 域检验观测拟合、在 x 域检验保真与 LPIPS，必要时报告不确定性。Agent 并非必需。真实 RAW 需另对 Poisson-Gaussian、CFA、AWB/CCM/TM 非线性与未知算子进行校准；该组合**尚未验证**。

**历史待核**：PnP-Flow、Flower、D-Flow 的原文和 matched compute；BAM 实验前向算子失配；真实相机设备端总时延。本节为新的相关但不等价任务分支，不改变原 survey 的低光优势/失败边界。

## 判断与缺口

**旧判断**：采样步数是生成式恢复的主要资源瓶颈；多步方法会持续降低 NFE。

**新证据**：GLOW-FM 在 TVM / TAESD / HDiT 条件下以 1 NFE 获得部分数据的竞争性成绩，独立目标消融提供局部支撑；但 LOL-v1 和 UHD-LOL4K 保真指标不全优。

**当前判断**：1 NFE 是可信**设计点**，不是共同最优点；评估应以真实保真、训练预算、表示损失与硬件 Pareto 为依据。

**待补**：逐篇核验 ELIR、TVM 原始论文、IllumFlow/Consist-Retinex、ReDDiT 的同设置训练；多次采样/零步判别式基线；4K实测、端云边界、人物文字真实感。

**记忆反例**：GFLOPs 最少的方案不必是恢复 PSNR 最好；NR-IQA 优势不等于真细节恢复。

## References

- [GLOW-FM / arXiv 2610.31222v1](https://arxiv.org/abs/2610.31222v1)
- [该论文正文 Related Work 及 Tables 1–5](../papers/arxiv-2610.31222.md)
- [Dual Flow / arXiv 2611.05843v1](https://arxiv.org/abs/2611.05843v1)
- [T03 总图](../LITERATURE_MAP.md)
