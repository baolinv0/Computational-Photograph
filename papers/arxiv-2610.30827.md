# One Evaluation Is Enough: Inversion-Free Image Editing with Trajectory Correction

目录：[快速回忆](#快速回忆) · [方法](#方法) · [证据与限制](#证据与限制) · [系统定位](#系统定位) · [References](#references)

- **ID**: arxiv-2610.30827; **版本**: v1，论文首页 2026-10-22；首次覆盖与核验 2026-10-24。
- **作者/团队**: Lifan Jiang, Taiyang Chen, Senlin Cheng, Bolei Xu, Xiaobo Li, Can Ye, Dehai Zhao, Deng Cai, Boxi Wu；浙江大学、蚂蚁集团、重庆邮电大学。
- **主主题**: T02 图像编辑与可控渲染；**连接**: T06 动作控制，X01 一步推理。**地图事件**: Boundary refinement / Engineering maturity。
- **核验范围**: alphaXiv 提取的原文全文，重点 §3–4、Tables 1–3、附录 E/J；未独立运行实验。
- **裁决**: PROBE（封闭形式免反演编辑，只针对 epsilon-prediction VP 一步模型）。

## 快速回忆

**问题**：已经蒸馏为一步的 VP 扩散编辑器，是否一定需要两个噪声时刻来稳定源到目标的编辑方向？

**真正增量**：Endpoint-Calibrated Transport (ECT) 在同一个带噪状态下用原始/目标文本条件得到两条预测：一条确定语义方向的局部角度切向，一条约束干净终点位移；先沿已知 VP 角度外推，再用端点投影约束过度修改。只查询一个噪声时刻，无反演/多步采样/额外学习；**两种文本条件合成一个 denoiser batch，并不是只做一次条件预测。**

**记住**：ChordEdit 依赖多个噪声时刻的编辑场；ECT 缩到单时刻并加入端点校准。与 ER-Chord 的“固定总强度下按空间可靠性重新分配”属于不同机制，不能从一个优于 ChordEdit 推断优于 ER-Chord。

## 方法

shared noised state → epsilon-VP one-step model 对 source 与 target 条件的两路前向（batched）→ nominal angular transport → endpoint-constrained correction → 一次 latent update。无可执行的独立区域 mask 约束，本方法不自动保证所有未编辑像素完全保持。

## 证据与限制

- Table 1 PIE-Bench、SD-Turbo matched backbone: ChordEdit → ECT, 非编辑区 PSNR 22.63 → **23.74 dB**；LPIPS×1000 122.64 → **109.04**；同步编辑 pipeline 0.265 → **0.212 s**；目标 CLIP×100 从 30.60 降至 30.20（小幅牺牲）。
- 同表 SwiftBrush-v2: PSNR 22.04 → **22.86**；但 MSE×1000 7.13 → **7.56** 且 LPIPS×1000 120.49 → 122.81，平均 PSNR 改善不等于每个样本或每个保真指标改善。
- Table 2 SNR-Bench：两套相同骨干上保真度改善，CLIP 有小幅下降；实验是作者报告，尚无第三方复现。
- Table 3 的 1-step/2-step 对照和 transport ablation 支持局部计算节省，但部分无额外 NFE 变体保真更好、目标 CLIP 更低，收益反映控制强度与编辑完成度之间的冲突。
- 延迟来自 NVIDIA H20 GPU 上带同步的编辑核心调用，不包括图像读取、tensor-to-image、输出写盘与评价；不是手机端到端时延。
- 作者限制：epsilon-prediction、variance-preserving schedule、共享噪声状态、适用的一步模型。Flow-matching v-prediction 大模型、黑盒 Qwen/FLUX API、RAW/TM 物理算子均不能直接套用。
- 表中的 IQA/judge 与 masked preservation 不能唯一证实人物身份或纹理的真实性，统计波动范围与跨设备结果仍需验证。

## 系统定位

**编辑执行器内部优化**，不是上层 Agent 规划器，也不是直接的轻量 tone-map renderer。给模型开放时序/速度参数时可探索融合；闭源 API 当前只可借鉴一时刻动作控制与端点保真约束的思想。

**Decision delta**：将少步编辑的“多时刻收集控制场”变成与扩散调度和预测类型相关的选择；没有普遍证明单时刻比多时刻更好。

## References

- [arXiv v1](https://arxiv.org/abs/2610.30827v1)
- [alphaXiv](https://www.alphaxiv.org/abs/2610.30827)
- [相关分支综述](../surveys/one-step-inversion-free-editing.md)
