# Gate3DGen: A Pre-processing Model that Selectively Purifies Real-World Images for 3D Generation

目录：[快速回忆](#快速回忆) · [机制](#机制) · [证据与关键反例](#证据与关键反例) · [迁移边界](#迁移边界) · [References](#references)

- **ID**: arxiv-2610.31649；**来源版本**: v1，论文首页 2026-10-22；first_covered/checked_on = 2026-10-24。
- **作者/团队**: Xiaolin Li, Zihao Huang, Fanpeng Meng, Chen Yang, Guanjun Wu, Kai Zhang, Jiemin Fang, Qi Tian；清华大学、华为、华中科技大学。
- **主题**: T06 选择性动作/跳过；桥接 T03 图像恢复与 T04 任务级评价；**地图变化**: Bridge + Counter-evidence about router evaluation.
- **核验范围**: alphaXiv 提取论文全文，检查 §2–5、Tables 1–5；代码链接论文提供，未运行；无独立复现。
- **裁决**: PROBE（与图像恢复直接关联但下游任务是单图 3D 生成，非手机摄影增强）。

## 快速回忆

**问题**：下游固定 3D 模型输入真实照片时，是否应该对所有图片统一增强？“2D 看着更好”会不会毁掉 3D 所需的物体轮廓和身份？

**核心结构**：原图 → router 判断 KEEP/PURIFY（干净图直接旁路）→ 有退化时以 router 特征条件化的一步图像 purifier → 冻结 3D 模型。数据来自约 3,961 个 3D asset 多视角渲染、人工/生成退化，形成 43,936 配对与 1,082 个 held-out 3D GT case；100K 路由训练 pairs。净化器来自 FireRed-Image-Edit-1.1，使用区域、边缘、重建与 LPIPS 约束，GT 只在训练/合成评测可得。

**记住**：评价目标是 downstream geometry 而不只是恢复 RGB 美观；Router 的任务级收益需要独立证明，不能因「模型能判断退化」就断言「最优跳过策略」。

## 机制

clean/degraded image → Qwen2.5-VL-based router 生成二类 logits 和条件特征 → threshold `P(PURIFY)` 选择 KEEP 或 PURIFY → 单步 DiT、latent/pixel/edge/foreground 加权监督 → 冻结 TRELLIS.2 / Pixal3D → 几何、rendering、图像评价。

其中“selective”是**整图 KEEP 或 PURIFY**，不是区域级 mask 是否执行；区域权重只在训练损失中存在。

## 证据与关键反例

- Table 2 合成干净 GT 图配对：退化输入 foreground LPIPS **0.2262**，Gate3DGen **0.1378**；PSNR **20.254→22.514 dB**，均为作者合成 benchmark 条件。
- Table 3 TRELLIS.2 全表面 Mesh Distance ×10^-3：退化输入 **1.984**、Gate3DGen **0.764**、真实干净 reference oracle **0.517**。相对于退化输入有较大增益，但与干净 oracle 仍有差距。
- Table 1 synthetic router PURIFY recall **88.45%**，accuracy **90.77%**。但 96 张真实照片用 GPT-5 agent 从编辑前后 3D 结果/无参考指标构造 proxy label：真实样本 router recall **89.29%**、accuracy **58.33%**，与**总是 PURIFY** 的正确率相同；作者原文也明确指出真实 proxy 协议下没有击败 trivial always-purify 策略。这是不能忽视的失败证据。
- Table 4 真实图片的 VLM 身份/净化评分较高，但 3D Quality 评分 **6.58** 低于 FireRed 和被比较的商用编辑器 **6.92**；画质/保真/任务目标非同一排序。
- Table 5 purifier 消融：添加 router 特征 improves geometry，但完整 Spatial Loss 版本虽改善其他边缘/perceptual 项，在 mesh distance 上由特征版 **0.755** 变 **0.764**（略差）。不能把所有模块贡献宣称为所有指标单调改善。
- 推理净化器约 **2.3s/图像**（论文计时条件），不是手机真实端侧性能；若router运行耗时、3D生成、I/O未包含，则不能视为全链路延迟。

## 迁移边界

任务级目标函数可以改变图像恢复的最优解：保护 3D 几何可能需要不同于人眼修图的监督。与 VetoNet/PreActIR 的“选择性执行或拒绝”思想相通，但任务、模型、证据和认证目标不同；不应画未验证的直接继承箭头。

**Decision delta**：给真实恢复系统增加可审计的 KEEP baseline 与 downstream utility 指标有价值；当前真实域路由有效性的关键证据不足，不作为已证明的 Gate 最优方案。

## References

- [arXiv v1](https://arxiv.org/abs/2610.31649v1)
- [alphaXiv](https://www.alphaxiv.org/abs/2610.31649)
- [作者项目（原文列出，未本轮复测）](https://supra-3d.github.io/gate3dgen/)
- [Selective-restoration living survey](../surveys/selective-task-aware-restoration.md)
