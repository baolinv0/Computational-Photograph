# 一步免反演图像编辑：时间控制、空间控制与端点保真

版本 v0.3 | 2026-11-11 | 主主题 T02，关联 T06 / X01

目录：[快速回忆](#快速回忆) · [竞争路线](#竞争路线) · [系统接口](#系统接口) · [证据边界](#证据边界) · [判断变更](#判断变更) · [References](#references)

> 专题聚焦低延迟文本引导图像编辑，不将语义编辑等同真实恢复或物理 TM。当前详细证据来自 ECT 原文；ChordEdit、ER-Chord、FlowEdit 等其余前序/并行工作本轮只核对 ECT 中的引用和比较，独立文献仍待逐篇核验。

## 快速回忆

**要解决的问题**：蒸馏一步模型的模型评估很贵，单个大幅语义更新容易破坏未编辑区域；如何在同等可控条件下使用更少时刻、更少像素漂移完成目标？

三种轴应分开：

1. **时序动作估计**：ChordEdit 多个噪声时刻收集编辑方向；[ECT](../papers/arxiv-2610.30827.md) 在同一个共享状态估计切向和端点，并做解析外推/校准。
2. **空间强度分配**：ER-Chord 关注控制场在不同空间区域的可信度与能量再分配。**不是** ECT 的多时刻化，也不因 ECT 优于 ChordEdit 而自动败退。
3. **编辑执行与保真**：FlowEdit / SDEdit / inversion 系列使用不同采样链及结构保持约束。多步可能更强但更慢；都需与同 backbone / 相同总调用预算比较。

## 竞争路线

```text
真实输入 + 编辑意图
   ├─ 显式反演 / 多步时间积分 → 结构保留可调、计算较大
   ├─ 零反演但多时刻控制场 → ChordEdit
   ├─ 同时刻解析传输 + 端点校准 → ECT（仅 ε-VP 一步骨干）
   ├─ 空间可靠性重分配 → ER-Chord（不同控制维度）
   └─ 多步免反演 flow 的逐时刻方向决策 → V2C-Edit（需 VLM）
                      ↓
       未编辑区 fidelity + 编辑目标完成度 + 总预算
```

条件差异：只适用 ε-prediction VP 的 ECT，不能直接照搬 FLUX/Qwen 等 v-prediction 流模型。公开黑盒模型也不允许内部编辑场访问。

### 2026-11-11 竞争分支：编辑轨迹内逐时刻选择，而非只调固定耦合点

**问题**：FlowEdit 的 source coupling 过强时产生 zero-edit，但不锚定则有背景泄漏。此前 ECT 关注「一次可否估计端点」，AR-Edit 关注「是否缓存视频 source-V」；本轮 **[V2C-Edit](../papers/arxiv-2611.10066.md)** 关注「在 FLUX/SD3 多步轨迹的每一时刻应执行哪一种编辑速度」。是不同优化轴，不是 ECT / AR-Edit 的升级继承。

| 竞争路线 | 相同执行器内的控制 | 作者证据 / 代价 | 成立条件 |
|---|---|---|---|
| FlowEdit fixed coupling | 预设 source–target coupling 和 switch point | H100/50 图，4.00s/图；可保真但 zero-edit | FLUX/SD3 可访问 flow trajectory |
| FlowEdit brute-force switch | 遍历 t_cs，选成功的较激进方向 | IA 6.22、protected PSNR 16.18；79.99s/图 | 高候选预算、没有很强保护约束 |
| **V2C per-step ILS** | coupled / decoupled / extrapolated / persistent direction，VLM 隐状态检查 terminal previews，mask 抑制未编辑区 | IA 6.07 / protected PSNR 17.44；26.44s/图、53GB H100 | 需可访问速度场与 Qwen3-VL-8B，不能黑盒 API/手机直接使用 |
| Explicit deterministic mask + end-point selection | 已知 ROI，预设有限 edit actions + 多候选筛选 | 强简单系统对照，论文未在同预算中完成 | 已知可编辑区域与局部光度目标 |

**判断变化**：训练免费 != 推理免费，**动态闭环让已存在的 executor 更易找到可编辑轨迹（可发现性）**，但没有补足输出目标量化精度、错误 mask 的证据或 executor 容量。该论文 Table 3 耦合单候选 IA 5.69→四候选 6.07，保护区 PSNR 17.78→17.44，证明 trade-off 未消失。与 T06 [AgenticIR survey](https://github.com/baolinv0/CameraPaper/blob/main/knowledge/imaging-agent/agentic-image-restoration-survey.md) 仅为控制机制互补关系，不将多步 generator 变成已经验证的多工具 Agent。

**方案**：在线源图+指令→每步候选 velocity 与 terminal preview→ILS 打分→局部 mask→更新→输出后分开验证编辑成功与非目标泄漏；离线不训练 V2C 但需已训练 FLUX/SD3+VLM，独立标定评审和真实 photofinishing 的绝对幅度误差。行动：保持现有一步/确定性局部修图基线；研究性最小比较固定 GPU 预算的 FlowEdit、t_cs sweep、V2C。适用门槛是语义 zero-edit 而非精细肤色 ΔLab 对齐。

## 系统接口

**在线**：输入 RGB/latents + source/target prompt → 凝缩的时间控制/空间控制 → 执行 latent edit → 还原图像 → 检查编辑效果与非目标保持；必要时 KEEP 原图。

**离线**：该 ECT 方案无需新增训练，但原始一步模型与配套图像条件已经预训练。和直接参数化 tone curve 的模型比较，需要固定「允许修改的内容与输出域」，不能随意跨类别做 SOTA 排名。

## 证据边界

ECT 原文 Table 1：PIE-Bench SD-Turbo matched ChordEdit→ECT，未编辑区 PSNR 22.63→23.74 dB，单图同步核心延迟 0.265→0.212 s；CLIP 30.60→30.20（缩放×100），并非所有指标同时上升。SwiftBrush-v2 上平均 PSNR↑但 MSE、LPIPS 略差。

因缺少作者外部实验与同预算 ER-Chord 直接对比，只能判断在上述报告协议中 ECT 相比 ChordEdit 的资源和部分保真收益，不得外推出对其他路线的全面胜利。作者的 H20 核心时延不含 I/O、转图写盘，不是手机端到端表现。

## 判断变更

**过去**：需要多时刻编辑场来稳定一步生成器的跳跃。

**本次**：ECT 显示至少对两种 ε-VP 一步骨干，可以从同一时刻构造“语义方向+端点约束”，降低部分时序开销；性能仍依赖模型、prompt 和编辑强度。

**不变**：局部 Mask、身份保护、source fidelity 与指令完成度存在权衡。端点一阶分析不证明不会幻觉。

**待补前序**：ChordEdit、ER-Chord 原始论文主表、SDEdit、FlowEdit、不同 backbone 实验、面向修图而非物体操作的局部 Tone Mapping。

**记忆反例**：“一次 temporal evaluation”仍可在一个 batch 中跑两种文本条件，不能写成一次条件模型算力等于标准单图前向。

## 2026-11-10：流式视频的 source-V 复用是新的约束条件，不是一步图像 ECT 的后继

**新增 [AR-Edit](../papers/arxiv-2611.09795.md)，GO-E / New route（T02/T06/X01）**。在 DMD-distilled 3–4-step 自回归视频 diffusion 中，Q/K 在时刻间相对稳定、V 承载可重用源内容。此方法不做 inversion：从 clean source 前向提取 V，对 target-prompt 的当前 chunk 分时/分层注入，保留未来 chunk 的 target KV-cache。属于**模型可见 attention 级条件控制**；ECT 是 ε-prediction VP 一步 *图像* 的同一时刻方向/端点校准，二者并未相互继承，输入、模型训练与评测不同。

| 受控编辑分支 | 前提与控制 | 对照 & 结果（作者原文，非独立复现） | 适用边界 |
|---|---|---|---|
| ECT / ChordEdit | ε-VP 一步图像模型； temporal support/ endpoint | PIE-Bench：matched ChordEdit→ECT，保护区 PSNR 22.63→23.74dB | 不适用任意 flow-v-prediction 模型 |
| **AR-Edit** | 3–4-step DMD-distilled causal video；t=0 source-V cache + target prompt | Reward Forcing 4 steps：source 7.28、text 6.11、TF 0.47、6NFE/10.50FPS；DynaEdit 7.17/5.96/0.39、13NFE/4.66FPS（单 H100） | 无通用 API 权限或 30FPS 手机运行证据 |
| StreamEdit / FlowEdit / DynaEdit | 自回归/多步 velocity 差、可用 attention cache | 相同 Self Forcing 4步 StreamEdit 6.12FPS vs AR-Edit 10.25；但15步 StreamEdit source 8.11 > AR-Edit 7.22 | Edit-step 增减会影响源保留/指令完成权衡 |

**判断增量**：从单图「时间端点估计 vs 空间调节」扩展到视频「源特征的哪个 attention 子空间值得保留」，**未改变** ROI source leakage 和编辑完成度独立评价的基本要求。论文 VLM Judge 不是人类真值，作者另有小样本选优；相邻系统质量对照时必须固定 backbone 和步骤。

**系统回忆**：离线先获得已训练、蒸馏的因果视频骨干；在线 streaming source video+instruction→t=0 V cache→target-prompt 逐 chunk 生成（选择性注入 V，KV 缓存保持 target consistency）→编辑视频，测源保留+文字要求+色调保真+GPU成本。Agent 只可作为上层策略，本文未验证自动工具选择。**行动**：保留作为流视频编辑的专用工程路线；不替换单帧手机 Tone Mapping 或 Reference Retouch。待查跨相机色彩、人工保真与移动端编解码全链延迟。

## References

- [ECT 2610.30827v1](https://arxiv.org/abs/2610.30827v1)
- [论文卡片](../papers/arxiv-2610.30827.md)
- [AR-Edit v1（2026-11-06）](https://arxiv.org/abs/2611.09795v1) · [canonical card](../papers/arxiv-2611.09795.md)
- [V2C-Edit v1](https://arxiv.org/abs/2611.10066v1) · [canonical card](../papers/arxiv-2611.10066.md)
- [T02/T06 总图](../LITERATURE_MAP.md)
