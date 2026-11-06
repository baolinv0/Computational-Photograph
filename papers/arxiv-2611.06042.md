# UniRestorer++: Scalable Universal Image Restoration with Multi-Granularity Degradation Modeling

目录：[快速回忆](#快速回忆) · [方法与前序](#方法与前序) · [证据审计](#证据审计) · [系统与边界](#系统与边界) · [References](#references)

- **ID**: arxiv-2611.06042；**authors**: Jingbo Lin, Zhilu Zhang, Fan Li, Renjing Pei, Wenbo Li, Hang Xu, Hongzhi Zhang, Wangmeng Zuo。
- **earliest_public_verified**: 2026-11-04（arXiv v1，另有 2026 ICLR 的不同前作 UniRestorer）；**source_version**: v1；**first_covered / checked_on**: 2026-11-06。
- **主主题**: T03；**次主题**: T05/X01；**系统角色**: 统一恢复执行器/训练/复合退化数据与容量扩展。
- **地图变化**: Engineering maturity + Boundary refinement；**裁决**: GO-E（统一恢复架构与复合退化 benchmark；不是全新 MoE 思想）。
- **核验**: 原文 HTML 的背景、方法、Tables II–IX、ablation 及成本段 selected_sections_checked；independent_replication=not_performed。

## 快速回忆

**一句话命题**：不要仅扩大一个万能恢复骨干，而是按退化层级扩容、依据退化估计置信度选粗细专家，并按空间位置路由专家。

**前序→真实增量**：ICLR 2026 [UniRestorer](https://proceedings.iclr.cc/paper_files/paper/2026/hash/04fb0ea2010694af12735724a601a3b4-Abstract-Conference.html) 已有层次退化聚类、多粒度 MoE 及 granularity estimation；本篇增加可扩层级与区域密集退化表征、局部路由，发布 CDD-50（最多五类复合退化）并量化 154M–2.9B 的扩容行为。不得称层次 MoE 首创。

**记忆**：更多专家不一定更好；不确定的退化判断，应退回覆盖更宽的粗专家。

## 方法与前序

离线：单项/复合退化合成与真实数据 → 退化层次及图像/区域标签 → 共享 Restormer 主干+不同层级 LoRA experts → 多任务重建和退化表征监督。

在线：RGB LQ → 稠密退化表征/退化置信估计 → 选一条 coarse-to-fine 专家路径+每像素/区域专家粒度 → shared base + top-1 LoRA expert → RGB restored。部署端必须计路由、存储及内存带宽。

**竞争/互补（综合推断）**：PromptIR、InstructIR 用共享网络或 prompt 控制；MoCE-IR 用专家分工；UniRestorer 2026 为明确作者前作；AgenticIR 工具调度与训练期内置专家路由是不同层次，不应把后者解释为 Agent 学会规划。

## 证据审计

- 作者 Table II–V：同论文设置 UniRestorer 的七单退化 PSNR 均值 31.81→32.24 dB；CDD-50 OOD 23.09→23.46 dB；少量但多组一致。
- 作者 Table VI：512×512 RGB、NVIDIA A6000：UniRestorer 171M/1156G/0.484s；UniRestorer++ 176M/1255G/0.515s。对这组**相近尺寸**基线，增加约 6.4% 时延、约 8.6% FLOPs，并非零成本。
- 作者 Table VII：154M–2.9B 总参的层次 experts 预测 OOD/真实集 PSNR 增益，但总权重、路由内存与训练代价增加；文中同活跃专家路径近似保持 FLOPs/latency 的论断不是手机端证明。
- 作者 Table VIII：在 SIDD，2.9B zero-shot PSNR 38.72，专用 NAFNet 40.30；5-shot 39.26。**不能推论巨型万能模型无条件击败专用恢复器**；同训练数据、同尺寸、同容量的严谨归因仍有限。
- 控制变量疑点：CDD-50 是本文提出的合成空间；极大模型在真实测试上的优势可能同时来自总容量、合成数据和优化预算。比较 dense scaling/vanilla MoE 是有意义的作者对照，仍无独立复现。

## 系统与边界

本篇改变的是 **训练期专家分配与统一执行器的覆盖能力**，不是取得新 RAW 信息，也不自动优化 AWB/TM 色彩目标。对真实跨手机、RAW Poisson-Gaussian 噪声、未见复合退化、手机端内存带宽均应独立确认。当前行动：**保留单任务轻量 baseline，作为大模型统一恢复研究与复合退化 benchmark GO-E；不自动替换端侧执行器**。

## References

- [原文 arXiv 2611.06042v1](https://arxiv.org/html/2611.06042v1)
- [ICLR 2026 UniRestorer（作者明确的前作）](https://proceedings.iclr.cc/paper_files/paper/2026/hash/04fb0ea2010694af12735724a601a3b4-Abstract-Conference.html)
- [路线综述](../surveys/universal-restoration-degradation-routing.md)
