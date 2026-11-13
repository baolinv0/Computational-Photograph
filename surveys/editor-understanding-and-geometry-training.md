# 图像编辑执行器的理解、几何与训练：什么能力由数据和表示获得？

版本 v0.1｜2026-11-07｜主主题 T02，连接 T03/T04/T05/T06/X01

目录：[稳定问题](#稳定问题) · [竞争路线](#竞争路线) · [前序与本次变化](#前序与本次变化) · [证据与边界](#证据与边界) · [完整系统回忆](#完整系统回忆) · [缺口](#缺口) · [References](#references)

## 稳定问题
在多条件图像编辑中，失败究竟来自**语义/参考理解、几何信息不足、目标编辑的可执行性还是独立验收能力**？本专题研究执行器训练及可表示能力；不把外部Agent路由或Judge正确率直接当作其能力。

记忆锚点：**统一理解与生成提高通用表达容量；保留深度先验修复特定几何失败；二者不能直接推导文本区域锁定能力。**

## 竞争路线
| 路线 | 运行时输入/控制 | 离线监督/训练 | 强项与失败条件 |
|---|---|---|---|
| 直接多模态编辑 | 源图+文本，多图参考可选 | 通用编辑pair、VLM指令监督；Qwen-Image-Edit等 | 通用语义；区域漏改、保护区泄漏 |
| 分开的理解/生成路径、共享信息 | 源图+多参考+长指令→MoT/MoE | [WeLM-Image](../papers/arxiv-2611.07392.md)：大规模筛选、多任务混合、独立生成/编辑Reward与蒸馏 | 复杂任务与高吞吐系统；能力归因和真实光度保真不可分 |
| 物理几何显式条件 | 图/目标depth等附加条件 | Depth ControlNet、几何pair | 强几何约束但目标depth在真实编辑时常不可得（oracle） |
| **深度先验的层级兼容迁移** | 源图+编辑指令，推理免显式目标depth | [StitchEdit](../papers/arxiv-2611.07922.md)：depth LoRA→逐层gradient cosine探针→删冲突层+分层LR | 3D移动/遮挡/视角，不能推断皮肤/背景光度隔离 |
| 推理时空间锁定与原图回退 | ROI mask/累积指令/原图 | 专用局部执行器、合成边缘 | 可约束保护区；局部边缘/阴影连续仍待处理 |

## 前序与本次变化
Qwen-Image、HunyuanImage3.0、SenseNova-U1 已探索语义与生成协同；[WeLM-Image](../papers/arxiv-2611.07392.md)（2026-11-05 v1，GO-E，Engineering maturity）展示 MoT理解/生成参数分离而cross-attention沟通、31.7B stored/5.4B activated以及大量数据蒸馏的产品训练路线。**公开技术报告对机制分量缺乏等数据/参数/算力消融**，不能把发布系统的总体能力算成某一组件的因果收益。

Marigold、Lotus-2 等把扩散先验迁移到深度感知；[StitchEdit](../papers/arxiv-2611.07922.md)（2026-11-05 v1，PROBE，New route/Boundary refinement）转而研究如何保留深度能力用于编辑。它发现 early/late 梯度目标兼容性有别，不能以“全层共享/全部冻结”概括其作用。已知前作是引用的几何知识路线；与WeLM的并列关系由本survey综合，不等于相互引用或依赖。

[MT Forcing](../papers/arxiv-2610.25404.md)/[TailSteer](../papers/arxiv-2611.06741.md) 处理**多轮漂移**，与单轮几何编辑是并列错误轴；[专门的多轮保真survey](multi-turn-editing-preservation.md) 保持canonical，不复制。

## 证据与边界
- StitchEditBench 自建150例，目标深度和训练pairs由生成器/深度模型形成，DCS只是算法构造的代理。作者DCS 0.92 vs 同深度初始化均匀FT 0.80；固定cosine 0.90，说明大部分收益可由简单层级学习率捕获。较昂贵的3M深度pair与10K编辑pair不应隐藏。
- WeLM 数据清洗50亿→6亿和MoT–MoE规模可给工程系统线索，但预训练数据/模型预算远大于通常实验；单个指标或短样图不能证实未编辑区逐像素保持、RAW颜色准确或真人肤色意图一致。
- 两种训练能力均不是Agent规划成功率。执行器可达、搜索发现和Judge选对必须另做等预算实验。

## 完整系统回忆
**离线数据与训练**：源图/目标编辑对+多参考或深度pair → 检查合成标签/目标几何 → (A) 大规模混合MoT–MoE+任务Reward+蒸馏，或 (B) depth LoRA+梯度兼容探针+分层fine-tune → 测单步目标达成/非目标保持与成本。
**在线推理**：源图+目标文本/参考/可选mask → 编辑执行器 → 编辑结果；保真/几何验收独立外接。**Agent控制（可选）**：诊断→候选→独立验证/接受/重试，不是以上两文实验已经验证的系统拼接。
**决策**：保留既有region-assisted/mask基线，几何变换才PROBE层级迁移，不由WeLM大规模榜单直接更换当前执行器。最小实验：固定同图+ROI，比较模型候选target success、ROI leakage、边缘连续；几何任务另加真人判定和同成本深度baseline。

## 缺口
需要等预算WeLM组件消融、真实开源权重与可访问性、不同相机的颜色保持、深度先验在非几何编辑是否负迁移，以及真实3D/人工ground truth对StitchEditBench进行外部核验。

## 2026-11-13｜评价器主归属修正（历史索引，不是新论文）

[EditJudge-Bench](../papers/arxiv-2611.12524.md) 的新证据是**可控 before/after 编辑的 VLM 判断正确性**，并非生成器的几何训练能力。为避免错误归类及重复全文，其主 survey 统一调整到 [T04 伪影证据与反事实 Judge 审计](artifact-grounded-reward-and-verification.md)；本专题仅保留交叉链接，用于提醒“执行器完成编辑”和“Judge 看出操作”不能混为同一种能力。

## References
- [WeLM-Image 原文](https://arxiv.org/html/2611.07392v1)
- [StitchEdit 原文](https://arxiv.org/html/2611.07922v1)
- [StitchEdit 项目](https://guoqincode.github.io/StitchEdit/)
- [多轮保真](multi-turn-editing-preservation.md)
- [CameraPaper AgenticIR已有survey](https://github.com/baolinv0/CameraPaper/blob/main/knowledge/imaging-agent/agentic-image-restoration-survey.md)
