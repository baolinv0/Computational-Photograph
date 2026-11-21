# Beyond Resemblance: Image Fusion Reimagined (ApexFuse)
更新：2026-11-21｜canonical arxiv-2611.25453｜arXiv v1 首传2026-11-19 03:32:47 UTC｜首次覆盖2026-11-21｜Hao Zhang; Yumin Huang; Linfeng Tang; Junjun Jiang; Jiayi Ma｜主 T05，次 T01/T03/T04/T02；目标/数据/训练/执行/评价；PROBE；New route + Counter-evidence-to-source-proxy。

目录：[快速回忆](#快速回忆) · [问题重构与路线](#问题重构与路线) · [作者证据与限制](#作者证据与限制) · [完整方案和行动](#完整方案和行动) · [References](#references)
## 快速回忆
一句命题：多模态融合没有唯一可测量GT时，强制输出同时像多种物理不同的输入可能互相冲突；可以先用受人监督的生成模型构造“理想融合外观”作为训练分布，再微调融合网络。该想法改写的是**目标定义**，不是额外采到真实融合GT。
竞争/前序包括 DDFM、SegMiF、ControlFusion、RFC 等无GT源保持目标，以及生成式 fusion / Pseudo-GT 方法。作者称历史多数以输入相似度为约束；“训练目标转分布”本身并非无先例，不能将相关生成监督或 human-in-loop 全部视为首创。
## 问题重构与路线
- 真实输入 VIS + IR 对齐图像；无唯一物理融合成品。
- 离线：Gemini整合通用目标prompt，GPT-6生成场景描述，GPT-Image-2.0初始每对3个目标候选，GPT基于内容保真、关键信息完整度和自然度审查不合格的再生成，人工筛选；生成 fused pseudo-GT 监督 FLUX.2-klein-base-4B的 LoRA 条件 flow matching。
- 在线：VIS/IR + 固定融合指令→已适配FLUX融合图；不是每次都需要生成人工GT，也无需在线人类多轮循环。Multi-exposure/Multi-focus/Visible-depth的零微调泛化由作者报告。
- 生成目标会同时改变自然度与纹理，尤其在热目标形状、文字、微小行人与不可见光谱信息中，可能创造无传感证据的新内容；作者的human selection与单个生成式评判器无法证明独立事实正确性。
## 作者证据与限制
- Table1 LLVIP (训练)/MFNet/FMB (跨集) 4个 NR-IQA：LLVIP MUSIQ70.206 vs RFC65.332；FMB MUSIQ68.630 vs ControlFusion56.341。均为代理质量指标，不能推断热红外测量真实保真。
- FMB 重新训练分割器、其 mIoU59.05 vs Text-IF58.54、ControlFusion58.41（增量不大）；LLVIP检测器重新训练作者报告 mAP50:95 65.353 vs Mask-DiFuser63.872，改变了下游训练数据源，不能归因于融合像素本身/无复训下游任务增益。
- 必须比较强简单基线：将原有源保持融合器作 GT 引导的学生、人工精选RGB目标不经大生成器、同等教师生成成本数据量、独立盲评/真实热目标位置一致性；原文不足以隔离目标质量、骨干升级与训练预算。
- 没有手机 sensor-to-display 真机部署、独立硬件推理时延、跨物理传感器测量一致性或逐物体伪影零错误证明。
## 完整方案和行动
**目标**是显著/自然的多模态可视化，**非目标**是估计唯一物理辐射真值。离线配对传感观测→源保持/生成偏好候选→独立结构与目标验证→pseudo-GT→LoRA训练；在线配对观测→条件融合→人/任务/IQA检查。Agent若实现可负责目标/候选审计，但论文并非已验证Agent融合系统。
**PROBE**：有价值的问题重新定义与数据路线，但生成目标和判分同源偏差尚待排除；保留现有测量一致性损失，不按本文将物理源约束整体替换为生成GT。最小实验在同配准VIS/IR、相同FLUX骨干/教师预算下对比源约束和已核结构审计的pseudo-GT，逐项报告热目标是否丢失/虚构与真正人评。
记忆：融合输出不必长得像每一个输入，但不能捏造输入从未测到的对象。
## References
- [论文 arXiv v1，Figure 2、Tables 1–4](https://arxiv.org/abs/2611.25453v1)
- [成像数据目标与可信度](../surveys/imaging-training-data-synthesis.md)
- [真实跨模态观测/对齐](../surveys/unaligned-guided-restoration.md)
