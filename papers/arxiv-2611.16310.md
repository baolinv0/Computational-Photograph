# Selective Generative Restoration for Video Deraining via Uncertainty-Aware Diffusion (SGVD)

目录：[快速回忆](#快速回忆) · [研究问题与路线](#研究问题与路线) · [机制与系统接口](#机制与系统接口) · [论文证据](#论文证据) · [批判性判断](#批判性判断) · [References](#references)

- **身份**：arxiv-2611.16310，v1，作者 Yi'ang Chen、Han Li、Laibin Chang、Hui Liu、Kui Jiang、Junjun Jiang（HIT 等）
- **最早可核验公开**：2026-11-12 05:10:53 UTC，arXiv v1；其他提前公开渠道未穷尽
- **首次本库覆盖**：2026-11-15，**backfill（非新研究通知）**；该论文已出现在上轮成功覆盖的 2026-11-13 cs.CV 公告中
- **主主题**：T03 可信恢复；**连接**：T06 选择性策略、T04 保真评价、X01 端到端计算
- **角色**：区域不确定性证据、条件生成执行、训练期时序一致性、推理成本
- **地图变化**：Supporting evidence + Boundary refinement（空间级选择性生成，不能等同整图 KEEP/RESTORE）
- **裁决**：**PROBE**（机制与负例诊断有价值；原有思想有明确前序，非移动手机部署）
- **核验范围**：官方 arXiv v1 HTML 的 Related Work、§III、§IV 数据/消融/效率/限制的选段；未独立复现，未穷尽论文引用史

## 快速回忆

**一句话机制**：用同一视频生成器在两种噪声初始化下的清晰潜变量预测差异估计区域不确定性；在不可靠区域多借助生成结果，在可靠区域更多保留输入，并用训练期共享锚点减少跨帧漂移。

**旧→新**：不是首次提出“可靠区域保守、不可靠区域生成”的问题；其增量是把两次随机预测的差异用作空间门控，并与 one-step 视频生成及训练期时序 anchor 联合验证。

**区分三个选择层次**：（1）整图调用 KEEP / RESTORE；（2）同图区域的确定性/生成混合；（3）候选生成完后 Judge 选优。SGVD 实现（2），不是验证（1）或（3）的 Agent。

## 研究问题与路线

- **问题**：雨丝、遮挡、雾化造成不均匀退化。可观察区域过度生成可能篡改真实纹理，严重遮挡区域单纯保真又会模糊。
- **直接历史**：传统时序确定性去雨（论文引用 DeLiVR、RainMamba）；整图视频扩散恢复（作者对比 ZSVD、DiffIR2VR、Diff-Plugin、DOVE 等）。这些是竞争/互补前序，不是声称作者直接继承。
- **平行机制**：选择性恢复与任务效用 [专题](../surveys/selective-task-aware-restoration.md) 已含 Gate3DGen 整图路由；DeLang-SR 讨论区域恢复幅度，但方向/幅度控制与 SGVD 的 stochastic-uncertainty gating 不是一回事。该联系是综述层综合推断。

## 机制与系统接口

**离线**：NTURain-Syn 的 25 条合成雨视频序列来自 8 条 clean video；49 帧训练输入、256² crops；冻结 Wan2.1-T2V-1.3B 的 DiT/VAE/text encoder，训练 71.67M adapter 参数，加入 flow/one-step consistency 和五帧共享 anchor 时序损失（ATC）。固定文本指令，无 VLM Planner。

**在线**：有雨视频 → VAE LQ latent → 2 个随机扰动 clean-latent probe → 不确定性图 M → `z_sel = M * z_generated + (1-M) * z_LQ` → adapter conditioning + 冻结生成器 → 输出去雨视频。探测图像的不确定性来自**模型自身随机分歧**，不是经独立标定的物理可恢复置信度。真实雨景没有干净 GT。

**完整系统内的未证接口**：是否用 M 触发整图重试、如何限制文字/身份失真、如何选择多个结果、是否能移植到 RAW/多帧手机 ISP，本文没有验证。

## 论文证据

- **消融（NTURain-Syn）**：baseline（无 USG、无 ATC）PSNR 23.0013，LPIPS 0.1899，warping error 0.0287；+USG 为 26.2416 / 0.1362 / 0.0309；仅 +ATC 为 25.9347 / 0.1449 / 0.0225；联合 26.5174 / 0.1310 / 0.0207。USG 与 ATC 有不同贡献，单独空间门控并不改善时序 warping。
- **Probe 数量**：同测设 w/o uncertainty PSNR25.6821，single probe 26.0712，两 probe 26.5174，四 probe 26.4938。两次随机预测获得更好的画质/成本平衡，但与无探针时的**整体系统设定**对照，尚不足证明不确定性图独立于所有其他条件变化。
- **效率（论文 §IV-F，单张 RTX4090 48GB，BF16，49 帧 640×480，batch1）**：1 step + 2 probes = 296 ms/frame、3.37 FPS；无 probes = 133 ms/frame、7.52 FPS；30 steps = 2078 ms/frame、0.48 FPS。作者称 1 step，但两次探针明显有额外 DiT 计算；不等同一次完整模型前向。仅报告 warmup 后 3 次计时，不计模型加载/磁盘 I/O。
- **数据与比较**：作者在共同 NTURain-Syn split 训练对比模型，并于 RainSynLight25、RainSynComplex25 直接 cross-dataset；真实 NTURain-Real 主要使用 NR-IQA、光流 warping 和可视化，没有 GT 结构真实性证明。

上述均为**作者报告**，不是独立复现。

## 批判性判断

- **增量位置**：可用的不确定性控制变量以及与时序训练约束的分工；并非“选择性生成”概念首创。
- **替代解释**：大规模 Wan2.1 先验、固定 LQ 初始化+condition 的双重收益、两次额外 probe 算力、少量训练视频的分布偏置。论文确有组内消融，但跨骨干、等运行预算的确定性 selector 和区域 oracle 不足。
- **失败边界**：两次随机生成都自信但一致地幻觉时，分歧可低而内容仍错误；高分歧不等于真实信息缺失。Flow-based warping error 并非时序真实度或 HDR 色彩忠实度的完备判据。
- **研究判断**：作为 T03 的区域级保留/生成路线证据值得 PROBE，不需要推翻简单去雨器，也不应直接加到手机 ISP/TM 控制链。
- **最小判别实验**：在固定 backbone、数据、总 forward 数和 latent 初始化时，将作者 variance mask 与显式雨遮挡 mask、局部重建误差 proxy、随机 mask 比较，并单独统计未退化区域 leakage、重遮挡 GT 区域 fidelity、总推理延迟。优先拆清“估计不确定性”与“额外计算”的贡献。

## References

- [原论文 arXiv v1](https://arxiv.org/html/2611.16310v1) · [摘要与提交史](https://arxiv.org/abs/2611.16310)
- [选择性恢复与任务效用 living survey](../surveys/selective-task-aware-restoration.md)
- [DeLang-SR canonical card](arxiv-2611.10485.md)（相关问题，不代表直接方法继承）
