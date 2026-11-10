# AR-Edit: Training-Free Autoregressive Video Editing without Inversion

元数据：Hovhannes Margaryan, Quentin Bammey, Christian Sandor, Vicky Kalogeiton；arXiv 2611.09795v1，首次公开 **2026-11-06**，首次覆盖 2026-11-10；selected sections checked；非独立复现。**GO-E**，T02 主，连 T06/X01；角色 **执行/策略/部署（服务器演示）**；地图变化 **New route / Boundary refinement**。
目录：[快速回忆](#快速回忆) · [机制](#机制) · [量化和归因](#量化和归因) · [边界和方案](#边界和方案) · [References](#references)

## 快速回忆
技术命题：蒸馏成 3–4 步的因果自回归视频生成器若不能有效执行逆扩散编辑，可使用单次 clean-source forward 提取 self-attention V 特征，将其选择性注入 target-prompt 的生成轨迹，避免 inversion 并保留运动流的源内容。
记忆锚点：**在所测 DMD-distilled backbone 中 Q/K 跨去噪时刻相对稳定、V 承载源内容；缓存 V 与反演整个噪声轨迹不同。**

## 机制
在线 causal stream chunks：源帧/源文本/目标文本 → 一次 source V-cache（t=0）→ target prompt 从随机噪声生成，每个 chunk 的部分 block/timestep 注入 source V，并用 commit-then-anchor 控制源/编辑权衡 → 输出编辑流，AR KV-cache 始终存储 target 的上下文。无需针对编辑重新训练，但依赖可以访问 DiT attention 的 DMD 蒸馏视频 backbone（Reward Forcing/CausVid/Self Forcing）；不是任意 VLM 视频 API。

## 量化和归因
作者自建 120 支 Pexels 视频/10 类编辑任务，主 Table 1 在 **Reward Forcing** 下：AR-Edit source adherence **7.28**、text adherence **6.11**、tonal fidelity **0.47**、每 chunk **6 NFE**、吞吐 **10.50 FPS**；DynaEdit **7.17/5.96/0.39/13 NFE/4.66FPS**；SDEdit 文本 **6.54** 但 source 仅 **3.81**。**Self Forcing** 4步：AR-Edit 10.25 FPS/0.85s time-to-first-frame，相同4步 StreamEdit 6.12FPS/1.38s；其15步 StreamEdit source adherence 8.11，高于 AR-Edit 7.22（并非全部指标碾压）。单 **H100** GPU，10.5 FPS≠30FPS实时移动视频，不应笼统表述为 30FPS 实时。
作者 Figure 8：加大 V 注入可提升 source adherence 但损害 text adherence；anchoring 改善权衡。基线 FlowEdit/DynaEdit/StreamEdit 是相关竞争，不是由 ECT 直接派生。Judge 采用 Qwen2.5-VL-72B，与独立人评需分层；作者另有20人33视频强迫选优，规模有限。

## 边界和方案
已知上游 AR distilled backbone，基础模型 pretraining/diffusion distillation 和 causal cache 昂贵；方法只减编辑阶段的控制调用。强简单对照是固定相同步数的 SDEdit/FlowEdit/StreamEdit，不是随机静图编辑。没有证明同摄像头 RAW 线性信息、局部肤色光度精确或手机功耗。行动：**保留为流视频 Agent/编辑路径，暂不修改静态照片增强和 Tone Mapping。**

## References
- [arXiv v1](https://arxiv.org/abs/2611.09795v1)，Table 1、§§3–5、Appendix Tables 3–4
- [现有一步图像编辑 survey](../surveys/one-step-inversion-free-editing.md)
