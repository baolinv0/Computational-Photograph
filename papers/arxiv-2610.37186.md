# VGIQA: Fine-Grained Image Quality Assessment with Visual Grounding Rewards

## 快速回忆

- **首次公开**：2026-10-27（arXiv v1）
- **主题**：IQA / Local grounding
- **核验范围**：selected_sections_checked；independent replication = not performed
- **一句话**：用 bbox + 缺陷语义奖励把 IQA 从整体分数推进到“哪里坏、为什么坏”，但当前证据仍主要是同源超分伪影数据。

## 精读记录

### 机制与证据

Xidian + Huawei Foundation Model Department。Qwen2.5-VL-7B 先用 Qwen3-VL-Plus 蒸馏 CoT 冷启动，再用 GRPO 联合优化局部缺陷定位、退化分类/强度和全局分数。VGSR-2K 基于 DiffIQA/SRBench，1,798 个 LR-SR 组由两个 MLLM 生成候选后经双盲人工选择/修订，并加入 LR-HR 空框负样本。VGSR-2K 上 VGIQA F1 0.3024、DIoU 0.3235，高于 Qwen2.5-VL-72B 的 0.1770/0.1997 与 Qwen3-VL-32B 的 0.1756/0.2185。

### 限制与竞争解释

训练/测试都来自同两套超分来源，bbox 定义偏向生成伪影、语义不一致和不真实 hallucination；候选由大模型产生再人工修订，容易继承候选覆盖盲区。F1/DIoU 提升不等于缺陷严重度与人类 MOS 因果一致，也没有跨相机、真实 ISP、编辑/压缩 OOD 或移动成本证据。数据/代码“将发布”与可访问、可复现实物需分开核验。

### 下一实验

做跨域冻结测试：真实手机去噪/锐化、局部 tone mapping、生成编辑与压缩；将 bbox 评价改为缺陷覆盖率、误报面积、严重度排序和可操作修复建议四维。

## References

- https://arxiv.org/abs/2610.37186v1
