# 非配准跨模态导引恢复：外部观测何时真正补充信息？

版本 v0.1｜2026-11-06｜主主题 T01，次主题 T03/X01

目录：[问题边界](#问题边界) · [路线与前序](#路线与前序) · [可比较证据](#可比较证据) · [系统与判断](#系统与判断) · [积压与来源](#积压与来源)

## 问题边界

目标是利用**真实新增观测**（NIR、第二相机视角或另一谱段）支持严重低照 RGB 的纹理恢复；非目标是仅靠一张 RGB 幻觉出丢失的光子、或只预测 AWB/CCM。跨设备光谱不同、空间不对齐与严重噪声三个因素必须分别测试：新增硬件能提供哪些结构信息，与跨视差假匹配会伤害什么？

**记忆锚点**：第二张图像不是自动增益；只有能对应同一物体可见内容的引导才是新增有效信息。

## 路线与前序

| 竞争路线 | 观测与控制变量 | 在线机制 | 离线监督 | 适用/失败条件 |
|---|---|---|---|---|
| 单输入判别恢复 | noisy RGB；无辅助测量 | NAFNet/Restormer 单路去噪 | paired RGB HQ/LQ | 有效稳健基线；严重低光细节缺观测 |
| 对齐跨模态融合 | RGB+NIR，同视野近配准 | 对应特征/滤波、融合 | 配对 RGB/NIR；标准/物理标定 | 低视差可用；双谱纹理不同易错配 |
| 预先配准后去噪 | 几何配准参数，fixed guide | align→denoise | 参考对齐 GT 或一致性 | noisy RGB 使配准本身不稳，遮挡失效 |
| **联合对齐+迭代恢复** | noisy RGB 与未对齐 NIR | 随 1–2 stage flow 去噪，同时更新 sparse correspondence | 合成 Poisson-Gaussian RGB noise + 双路真实配对 | [UGD-FM](../papers/arxiv-2611.06422.md)；大视差/遮挡仍差 |
| 硬件低照采集强化 | 多帧/更长曝光/增益、NIR 辅助 | 改变曝光/SNR，而非只做后处理 | RAW radiometry/paired benchmark | 动态场景 motion，热与能耗是采集端成本 |

前序锚点：NAID、SANet、CUNet/DVN/RFFNet（按 UGD-FM 原文 Related Work 核对定位；其各自完整原文仍待补）；[CHROMA-MILL](../papers/arxiv-2611.04092.md) 是低照颜色与照明监督的**互补问题**，不代表本路线直接前作。

## 可比较证据

**2026-11-04 新证据 UGD-FM**：其 FANVID/RGB-NIR Scene/MS2 测试包含单图、guided 和 diffusion/flow 的作者对照。其 FANVID Table 6 观察为：直接回归 30.27、标准 FM 2 step 30.34、stage-focused 30.42、加 inference-consistent states 30.58 dB；另外从 window guidance 30.03 到 sparse propagation 30.58。由此不能将全部增益归结为“用了 flow”；引导聚合和训练时刻匹配均有贡献。

其 1–2 steps 是网络求解步数，不等于双相机采集、ISP 预处理、配准和端到端手机时延。作者局限明确为 3D parallax/occlusion 和联合恢复成本；未独立复现或做真实手机双摄外场。

**最强替代解释**：PSNR 提升可能来自 NIR 额外观测、骨干容量、稀疏匹配结构或 flow-stage 设计，须在同输入/同网络大小下拆解。消融已经部分区分 sparse/flow，但尚非等手机成本的综合实验。

## 系统与判断

**在线**：可选 RGB-only fallback ← [RGB / NIR capture + 同步/外参] → photometric + geometric evidence → conservative correspondence confidence → sparse NIR fusion + stage-wise denoising → preserve region and color checks → RGB render。若遮挡/错误匹配，应退回 RGB-only，不应强行将 NIR 纹理覆盖到 RGB。

**离线**：记录双目光谱/几何、真实和合成噪声 → clean RGB GT/可信局部 GT → 训练单图与 guided 等预算版本 → 视差/遮挡/运动/光照分层评价 → 真机全链成本。**Agent 层**：默认不必有 VLM 或 Agent；仅可选确定性观测质量判断与 fallback routing；现有论文未证明这一步。

**旧→新判断**：传统 NIR guided 关注有对应区域的特征融合；UGD-FM 给出“恢复中提高对应关系可用性”的实验证据和少步机制。**不变**：无第二真实观测的信息极限、错配风险和硬件成本都存在。**决策 GO-E**：在真实可用 NIR/第二谱段才纳入候选；单传感器训练不改。

## 积压与来源

待独立核验 NAID/SANet 等真实成像和外参协议；UGD-FM appendix 的真实噪声与 3D 视差统计；手机 Sensor/RGB-NIR ISP 的端到端电耗和逐区域误匹配率。本轮精读核验范围限定 UGD-FM 原文 selected sections，不称该分支历史已穷尽。

- [UGD-FM 2026 原文](https://arxiv.org/html/2611.06422v1)
- [UGD-FM card](../papers/arxiv-2611.06422.md)
- [低光/照明/颜色互补 survey](low-light-raw-awb-illumination.md)
