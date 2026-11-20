# 科学成像 SR：物理光度保持、空间歧义与跨滤镜泛化

版本 v0.1｜2026-11-20｜主 T03，连接 T01/T04/T05｜canonical 专题（问题而非单篇名）
目录：[回忆](#回忆) · [目标和竞争路线](#目标和竞争路线) · [历史锚点与比较](#历史锚点与比较) · [证据和边界](#证据和边界) · [完整方案](#完整方案) · [判断与待补](#判断与待补) · [References](#references)

## 回忆
**稳定问题**：图像中的星点/微弱物体承担定量光度测量价值，SR 输出既要提高空间分辨率，又要不改变可测物体总能量与位置；不同滤镜、PSF 和采样模式引入域迁移。传统自然图SR指标 PSNR/SSIM 与光度 Flux Error 是不同评价轴。
**本次变化**：2025 STAR 已给 flux-consistent LR/HR、FE和FISR；2026 STAR++ 将 1 filter 扩为36，加入真实 HST 滤镜元数据适配和亚像素位置不确定性训练，7未见滤镜系统测试。新研究 **重大扩展/Engineering maturity**，不是首次引入 flux invariant constraint。
**一句话**：保持物理量，需要正确的退化生成和单独的物理评价，而非只追求看起来锐利。

## 目标和竞争路线
| 路线 | 输入 / 控制 | 输出 / 监督 | 成立条件 | 评价边界 |
|---|---|---|---|---|
| 物理PSF去卷积/多帧 | 已知PSF、天文观测/多次曝光 | 观测约束HR或较佳PSF恢复 | PSF已标定，观测足够 | 物理模型不匹配和噪声放大 |
| 通用判别式SR（EDSR/RCAN/SwinIR/HAT） | 模拟LR→HR paired | 像素重建 | 训练/测试退化近似 | 高PSNR可能同时错误估计flux |
| flux-constrained SR（STAR/FISR，2025） | 单滤镜、PSF光度保持合成对 | flux guide、flux weighted loss与FE指标 | 给定通量校准和特定滤镜 | 单滤镜外域不可靠 |
| metadata-conditioned cross-filter SR（STAR++/FISR++） | LR、波长/滤镜参数、PSF构造的训练域 | HR + 光度约束 + shift uncertainty | 可获滤镜元数据；相关物理条件 | 训练LR合成；真正跨望远镜实测未证 |
| 生成先验驱动细节补全（一般竞争方向） | LR + 生成先验/参考 | 视觉细节丰富HR | 内容可能有多解 | 未独立验证时无法保证星点位置与通量 |

本专题以测量忠实为主，不能用自然图美学偏好替代科学有效性，也不把 FISR++ 当手机 ISP 已实现方案。

## 历史锚点与比较
- 物理基线：PSF去卷积、Richardson–Lucy 一类方法，需结合望远镜噪声/边界验证（尚未逐篇独立读原文，历史检索backlog）。
- 通用 EDSR/RCAN/SwinIR/HAT：论文的竞争基线，本次只读 STAR++ 对比，不继承这些论文未复核实验结论。
- **STAR（2025-07-22）** [arxiv:2507.16385](https://arxiv.org/abs/2507.16385)：同作者直接前作，单滤镜 54,738对；原已引入 flux preserving data、Flux Error、FISR。
- **STAR++（2026-11-18）** [canonical card](../papers/arxiv-2611.24023.md)：36滤镜 1,697,816 对；7未见条件；FAA 与 SADL；作者明确声明是 STAR 的 expanded version，**直接继承**，不是不同独立团队。
- LC-ISP 的同设备多帧教师监督 [卡片](../papers/arxiv-2611.19284.md) 与本路线仅具有“目标来源可信性需单审”的**分析者跨主题联系**，其 sRGB 与测光科学合同不相同。

## 证据和边界
原文 STAR++ Table III/IV：STAR++ 数据训练、7个未见滤镜测试，x2 FISR 34.32dB/FE0.5304→FISR++ 35.42dB/0.4341；x4 31.52/0.7257→32.63/0.6803。STAR数据训练 FISR 32.04/0.6027→STAR++数据训练 FISR 34.32/0.5304，表明提升不能只归给FAA/SADL，**数据规模和滤镜覆盖本身是强竞争解释**。作者 Table V/VII 提供模块与flux损失消融，但仍需要真实跨仪器 OOD 证据。
**关键GT边界**：HR取自 HST science image，LR 经PSF/flux-conserving resize 合成，非双望远镜同场同步配对；射电和非均匀星点密集背景可能另有噪声物理；flux保真必须基于合适的星源检测/孔径和单位校准，FE不自动覆盖定位、假星点、弱目标召回。

## 完整方案
**离线**：高质且校准的 HR + 传感器/滤镜 PSF + 噪声/采样模型 → 物理flux-conserving 低分辨率合成、按真实sky region划分测试 → 训练有metadata的SR，使用像素/不确定性/flux损失 → 未见滤镜与真实采集评估，包含简单deconv、bicubic和强判别式SR。
**在线**：真实LR星场 + filter metadata/可用PSF → 物理/网络重建 → HR预测；用已知测量下采样一致性、stellar flux/centroid/false sources等独立验收；无必需 Agent 或生成器。
**尚未验证的接口**：FISR++给出的未见滤镜表现不直接推广手机多焦距/传感器光谱响应；在 ISP 色彩/TM 上如何设真实守恒量需另定义。

## 判断与待补
旧：可信SR需同时看像素与物理测量；新：多光谱条件与位置多解必须纳入训练和测试，不能只看同滤镜评分；保持：**模拟LR仍不能证明真实传感器域泛化**。**GO-E：保留专题，当前手机TM/恢复工程不重构。**
最小可信实验：同一 STAR++ split/骨干/训练预算，分别做无 FAA/SADL、独立 FAA、独立 SADL 和完整模型；加入测试时不同PSF与真实不同仪器观测，评价flux/centroid/幻觉目标。
Backlog：STAR 2025正文更多消融独立复核；真实跨仪器定标、滤镜同名但带通不同、数据/权重公开可用性；物理PSF经典前序核验。
**覆盖**：2026-11-20 原文v1 §III–V及STAR原始摘要；未独立复现，不能称共识。

## References
- [STAR++ v1](https://arxiv.org/html/2611.24023v1) · [canonical card](../papers/arxiv-2611.24023.md)
- [STAR 2025（直接前作）](https://arxiv.org/abs/2507.16385)
- [长期地图 T03/T05](../LITERATURE_MAP.md)
