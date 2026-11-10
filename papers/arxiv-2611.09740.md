# Zero-Shot Benchmarking of Unified Multimodal Models for Shallow-Water UAV Image Distortion Assessment and Restoration

元数据：Dario Scilla, Omar A. Lopez, Mattia Rosso, Kasper Johansen, Matthew F. McCabe；KAUST 等；arXiv 2611.09740v1，首次公开 **2026-11-06**，首次覆盖 2026-11-10；original methods, tables and limitations selected checked；非独立复现。裁决 **GO-E（重要负面基准/反证）**；T04 主、连 T03/T06/T05；角色 **评价/执行/数据**；地图变化 **Counter-evidence / Boundary refinement**。
目录：[快速回忆](#快速回忆) · [命题和证据](#命题和证据) · [与前序关系](#与前序关系) · [限制与行动](#限制与行动) · [References](#references)

## 快速回忆
技术命题：在一种真实感较强但领域特殊的水下 UAV 图像退化中，统一 MLLM 即使能描述部分失真，也不能仅凭零样本指令可靠地修复 RGB 内容；图像评估能力不等于可执行恢复能力。
记忆：**诊断得出“水浑浊/偏色”，与真正恢复未观察到的海底结构不是同一能力。**

## 命题和证据
作者建立 1000 张 paired 基准（600 半合成、400 完全合成），五个冻结 open-weight unified MLLM 不提供真值海底信息；测分类和质量诊断、以及 100 张图的直接零样本恢复；含人工标注与 prompt/difficulty 对照。作者报告最佳失真检测 balanced accuracy 约 **0.654**，恢复 PSNR 仅最大 **+0.255 dB**，**所有受测模型的 pooled LPIPS 未改善**，并见纹理幻觉；更具体的 per-subset 改善不能等价整体成功。人评在浊度上的标注一致性约 0.507，亦提醒 benchmark 标签本身并非绝对真值。
论文使用特殊 shallow-water UAV 传感域，真实退化难有完全干净 GT，配对部分合成所得 label 不能等价真实水下恢复上限。简单专项基线 InstructIR 等、显式水下光传输法和通用图像编辑应分为不同执行器。比起选出哪个 VLM，先确认所需清晰内容是否可从源图恢复。

## 与前序关系
与 NightIQA 的局部失真评价、低光 IQA/GT 审计、Gate3DGen 的先判定是否处理是共同抽象而非直接方法继承：**诊断/评价/策略/恢复器容量需分离**。一篇特定水域负例不能宣称 MLLM 在所有照片恢复中失效；此文是 GO-E 的高价值反证与数据基准，不是部署优势。

## 限制与行动
决策保持：不能仅因 VLM 给出正确方向就让其直接做高保真修图；当存在物理算子或分区域确定性修改时，优先强简单基线。最小试验：人工标注退化是否可从源图修复，固定 100 图比较 direct unified MLLM、VLM diagnosis+确定性 executor 和专用 restoration network，再分别评估 target PSNR/LPIPS、非目标保持和动作可达性。

## References
- [arXiv v1](https://arxiv.org/abs/2611.09740v1)，数据构造/Results/人工标注/Failure analysis
- [低光与GT/IQA survey](../surveys/low-light-iqa-and-gt-validity.md) · [选择性恢复 survey](../surveys/selective-task-aware-restoration.md)
