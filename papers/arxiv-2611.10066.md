# VLM as an Editing Pilot: VLM-Steered Velocity Control for Flow-Based Image Editing

元数据：Kuan-Shen Chiu, Jia-Wei Liao, Yu-Chieh Chao, Li-Xuan Peng, Wei-Yun Ma, Cheng-Fu Chou；arXiv **2611.10066v1**，**2026-11-06** 首传（本轮最早可核验公开全文）；2026-11-10 进入 cs.CV 新公告；首次覆盖 **2026-11-11**；原文 Method、Table 1/3/4/7 和附录选定节已核验，**非独立复现**。**GO-E**（可执行的闭环候选动作控制及明确成本），主 **T06**，次 **T02/T04/X01**；角色 **策略/执行/评价**；地图变化 **Bridge / Boundary refinement**。

目录：[快速回忆](#快速回忆) · [竞争与机制](#竞争与机制) · [证据与归因](#证据与归因) · [系统与边界](#系统与边界) · [References](#references)

## 快速回忆
**一句话技术命题**：固定的 source–target flow coupling 会让有些编辑「完全没改到」；在每个扩散/flow 时刻构造不同强度的 velocity，使用 VLM 对指令是否真正实现的语义判别动态选方向，并用空间 mask 约束泄漏。

**记忆锚点**：**编辑器可以有能力但被过强的 source coupling 锁住；逐时刻找到可用动作不是增大编辑器的模型容量。**

## 竞争与机制
- **FlowEdit (2025)**：反演免除、source-anchored flow coupling 和固定 switch time；简单、快，但可能 zero-edit。
- **FlowAlign (2026)** 与 **DNAEdit (2025)**：同为 training-free / source-constrained flow 操作的对照，不因发表先后就标直接继承。
- **V2C-Edit（本文）**：预训练 FLUX-dev 或 SD3-medium；每个 timestep 有 coupled、decoupled、extrapolated、persistent-decoupled 四类候选速度；对每个候选构造终态近似 preview，Qwen3-VL-8B 隐状态 **Instruction-Level Similarity (ILS)** 评分并选择；若 ILS 容许，再用差分幅度自适应 mask，逐时刻反复执行。
- **强简单替代**：FlowEdit 搜索固定切换点 t_cs、全程固定 aggressive coupling、只在最终图像做 best-of-K；它们决定 VLM 闭环相对于预算增大的实际净收益。

## 证据与归因
作者 MagicBrush **535**、PIE-Bench **700**、FLUX/SD3 比较。FLUX 的同一骨干消融（Table 3）coupled-only **IA_GPT 5.69 / background PSNR 17.78 dB**，全部 4 velocity **6.07 / 17.44 dB**：指令完成度提升，源图保护出现可测下降；不能称无代价增强。ILS 与 target-caption CLIP 的检查（Table 4）在人工编辑 GT vs source 的「打分反常」比例约 **2.43% vs 35.88%**，是评审信号的区分力测试，不是独立人类偏好准确率。

关键反例：论文附录对 FlowEdit **brute-force** 搜 t_cs，作者报告编辑 IA 可达 **6.22** 高于 V2C **6.07**，但 preservation PSNR **16.18** 低于 V2C **17.44**，H100 每图 **79.99s vs V2C 26.44s vs 原 FlowEdit 4.00s**（50图、单 H100）；V2C 峰值 **53GB**，不是手机端方案。需同时比较质量、保真、总 latency/cost，而非只比较 IA。

## 系统与边界
**在线**：RGB 源图+明确文本编辑 → 预训练 flow executor 生成一组 velocity → terminal previews → VLM ILS 选择 velocity → 在 semantic 条件满足时加保护 mask → 更新状态、重复多个 timestep → RGB 输出+后验人工/程序 ROI 验收。**离线**：无需新训练，但完全依赖已预训练的 FLUX/SD3 与 Qwen-VL，且需要评审信号校准、ground-truth edit cases 和等总预算测试。本文没有端到端 Agent 进行多工具决策，也没有证明高精度肤色或 Tone Mapping 数值幅度匹配。

**关键区分**：改善的是同一执行器轨迹内的**可发现性（which velocity/when）**，与执行器是否具有正确输出的**可达性**、最终编辑结果的**可选择性**分离。高成本逐时刻 VLM 判断可能令简单 K 候选 + deterministic mask 更有工程价值。

**裁决**：GO-E 作为动态闭环 velocity-control 工程路线，**不替换**现有确定性 ROI 修图；最小验证：固定 FLUX 和总 GPU time，比较 FlowEdit 不搜、fixed t_cs sweep、V2C，按 edited ROI success 和 protected ROI leakage 双指标检查。

## References
- [arXiv 2611.10066v1](https://arxiv.org/abs/2611.10066v1) · [HTML](https://arxiv.org/html/2611.10066v1)（§§5–6，Tables 3/4，Appendix Table 7）
- [作者实现](https://github.com/Kuanshen77/V2C-Edit)
- [既有 editing 控制 survey](../surveys/one-step-inversion-free-editing.md)
