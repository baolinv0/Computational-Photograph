# TailSteer: Trajectory-Tail Steering for Drift-Resistant Multi-turn Image Editing

目录：[快速回忆](#快速回忆) · [机制与前序](#机制与前序) · [证据与反证](#证据与反证) · [系统方案](#系统方案) · [References](#references)

- **ID**: arxiv-2611.06741；**作者**: Ruikang Li, Zixuan Chen, Jiarui Wu, Mingde Yao, Yiyuan Zhang, Yujin Wang, Hanming Deng, Lewei Lu, Tianfan Xue。
- **首次公开**: 2026-11-04 arXiv v1；**source_version** v1；**first_covered / checked_on** 2026-11-06；核验 selected_sections_checked，no_independent_replication。
- **主主题**: T06（执行与多轮控制）；**次主题**: T02/T05；**角色**: 编辑器训练/多轮执行稳定性，不是新 planner/judge。
- **地图变化**: New route + Boundary refinement；**裁决**: GO（多轮区域保真训练机制，关键反例明确）。

## 快速回忆

**一句话命题**：保持预训练编辑器前段去噪轨迹不变，只在末段利用原图未编辑区域约束轻度修正，降低每次小错误累积成长期漂移。

**背景前序**：MT Forcing（2026-10-18，跨回合 self-rollout 与 teacher）偏训练多轮历史；常见 mask compositing 偏推理阶段硬复制；ConsLoRA/FreqEdit 偏保持能力或额外机制。TailSteer 在相同“反漂移”目标下把纠错显式定位到单次生成轨迹尾部；对 MT Forcing 是竞争/互补的综合判断，不断言作者直接继承。

## 机制与前序

离线：原图与身份/局部编辑指令 → 冻结 base editor 自生成编辑轨迹 → 按 mask/局部性过滤（不是人工完整的目标编辑对）→ 对编辑区保留模型自己产生的结果，对保护区用源图覆盖构造 preservation endpoint → 训练新模型：早期 velocity 模仿 base，尾段渐混 base velocity 与指向 preservation endpoint 的 velocity，rollout 采用当前学生状态 on-policy。

在线：原图/上一轮编辑 + 文字意图 → **一次常规编辑器采样** → 输出；无额外 judge、mask、base model 或外部 compositor 的推理调用。多轮再用输出作为下一轮输入，因此单轮小损伤叠加很关键。

## 证据与反证

- 原文 4 个编辑器、3 家族 FLUX.1 Kontext、FLUX.2 Klein、SenseNova、Qwen-Image-2.1；每个 backbone 2,000 updates, 8×H100 BF16、effective batch16，训练昂贵。
- 100 图的十轮 Add & Preserve 定量评估：SenseNova 指定 onset=42，保护区第十轮 PSNR 11.23→18.22 dB，SSIM .166→.489；object completion 94.93%→94.78%。该比较是同 paper 结果，不可直接外推真实用户无限轮编辑。
- 20轮展示是案例可视化，并非 20轮同样充分的定量证明。
- **重要负例**：Table 2 单轮某些 RISE 基准下降：FLUX.2 onset=48 spatial accuracy 14.17→11.39；Qwen model onset=30 为 20.56→18.06。称“完全保留原能力”不准确。
- 最后一步独立微调然后全程用同模型，会出现过平滑/去饱和；前段 base-prior regularization 的设计有因果动机。不同 backbone 和不同 onset 是超参数选择，不应自动假设无需调参。

## 系统方案

研究位置：**提升现有生成编辑器的局部可达性/多轮保真**。对 Agent 额外的动作选择、可发现性、候选 judge 准确率并无直接结论。用于区域编辑先测单步 targeted delta、protected-region leakage，再测多轮；本篇不是为 photometric accuracy/多光源白平衡设计。强对照：从原图平行生成每个候选、原图外区 compositing 与 MT Forcing（等预算才能比）。

## References

- [原文 HTML/v1](https://arxiv.org/html/2611.06741v1)
- [历史 MT Forcing card](arxiv-2610.25404.md)
- [多轮编辑保真专题](../surveys/multi-turn-editing-preservation.md)
