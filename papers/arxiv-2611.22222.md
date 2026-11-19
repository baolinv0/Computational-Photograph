# ExplicitIR: Explicit Spatial Policy Fields for All-in-One Image Restoration

更新：2026-11-19｜canonical arxiv-2611.22222｜arXiv v1 首传 2026-11-17｜11-18 官方 cs.CV new 公告｜首次覆盖 2026-11-19

主主题 **T03**；次主题 T06/T04；系统角色：执行/空间策略/训练；地图变化：**Bridge + Boundary refinement**；裁决：**PROBE（显式区域控制研究价值，而非全任务最好）**。

目录：[快速回忆](#快速回忆) · [机制](#机制) · [证据与对照](#证据与对照) · [系统方案与行动](#系统方案与行动) · [边界](#边界) · [References](#references)

## 快速回忆

**去术语命题：**在一个恢复网络内部，为每个像素预测“改多少”及“从多大范围获取上下文”，使局部退化强度与处理策略有可检查的中间表示。

不要把神经网络内部的空间 Policy 当成具备语言推理和外部动作的 Agent；也不要把其预测的零更新预算等同最终输出像素原样保持。

## 机制

输入：未知混合退化 RGB。Restormer 式 encoder-decoder 的 Spatial Policy Estimator 估计两个场：Budget d（更新幅度）和 Style λ（窄/宽上下文分配）。Policy-Adaptive Decoder Blocks 归一化局部分支响应，以 d 约束 decoder state 更新幅度。训练以恢复目标的像素损失学习，无每像素 Policy 的真值标注、无需测试时任务标签和 Prompt。输出：恢复 RGB。

**分析者的可比路线**：PromptIR 通过提示式条件化，AdaIR/Restormer 通过特征适应和注意力，SGVD 通过图内不确定性混合观测与生成结果，ExplicitIR 则在同一个 decoder 内部明确控制 update/context。时间顺序不等于直接继承，SGVD 是跨任务共同抽象机制而非作者声称的前作。

## 证据与对照

作者 §4 的 3 任务去噪/去雨/去雾平均 PSNR：Restormer 31.98 dB；ExplicitIR 32.78 dB；外部退化条件化 DFPIR 32.88 dB（输入条件不同，不应称击败所有强模型）。§4.5 对比未采用 Policy 的基础结构、增加两场及其干预，支持 spatial field 的局部作用，但整体提升也可能来自额外分支容量、特征建模和结构归一化；不是同参数同 FLOPs 的机制纯归因。训练与测试仍主要是合成/既有恢复基准，未展示手机 RAW/端侧端到端验证。均为作者结果，非独立复现。

**负例与替代解释：**如果固定网络上的 learned attention mask 或简单局部门控在等计算预算下达到近似收益，则“显式双 Policy 场”的增量主要是可解释/可控接口而非性能机制；强模糊或全局雾霾没有清晰局部 KEEP 边界。

## 系统方案与行动

- 离线：混合退化 clean/LQ pairs → train baseline and Budget/Style fields → clean ROI leakage + degraded ROI recovery + cross-domain ablation。
- 在线：退化 RGB → shared encoder → Budget/Style maps → adaptive decoder → restored RGB；没有外部 Agent 的执行-评价-重试循环。
- Agent 控制（可选设计而非本文验证）：可把 Policy 场作为可见执行证据，再交独立 Judge；不会提升模型本身无法重建的细节。
- **行动：PROBE；保持现有恢复系统不改。** 固定 backbone 与训练/计算预算，比较普通空间注意力/1场强度/双场显式策略，分层测 ROI 改善与非目标泄漏。

## 边界

显式内部更新强度有助于审计恢复策略，但不能直接证明真实源图内容保真；评价器仍需独立检查清晰区是否被改坏。强结论需要真实噪声、复合混合退化及跨相机测试。

## References

- [arXiv v1 完整正文](https://arxiv.org/html/2611.22222v1)
- [Restormer 原始论文](https://arxiv.org/abs/2111.09881)
- [PromptIR 原始论文](https://arxiv.org/abs/2306.13090)
- [选择性恢复与区域控制 living survey](../surveys/selective-task-aware-restoration.md)
