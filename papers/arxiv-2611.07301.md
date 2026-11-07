# ArtiVidRM: Verifiable Artifact-as-Rubric Reward Modeling for Explicit Quality Articulation in Video Generation

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据与争议](#证据与争议) · [行动与方案](#行动与方案) · [References](#references)

- ID: arxiv-2611.07301；首次可核验公开：**2026-11-05**（arXiv v1）；source_version: **v1**；first_covered: **2026-11-07**；checked_on: **2026-11-07**。
- 作者/团队：Caorui Li, Yangguang Ji, Shuxia Lin et al.（Opus AI/Southeast University等）。
- 主主题：**T04**；次主题：T06 / T05；系统角色：评价、Reward、策略；地图变化：Boundary refinement / Supporting evidence。
- Verdict：**PROBE**（研究价值/工程适用性分开）；核验范围：arXiv v1 HTML 方法与选定实验、未独立复现；尚未做全站更早公开检索。

## 快速回忆
**去术语命题**：视频奖励先列具体可观察伪影、再基于列表打分；对伪影召回、列表长度和人类偏好分别训练，检验解释过程能否改善奖励可用性。

**与前序关系**：VideoScore(2024)、VideoAlign/VideoScore2(2025)、VisionReward(2026) 是同任务前序与竞争；CheckDistill、NightIQA 等结构化视觉评价是共同抽象机制而非该论文引用继承。

## 精读记录
**输入→输出**：提示与两个生成视频→每视频结构化artifact list +质量分+pairwise preference。主要任务是T2V生成奖励，不是手机真实视频保真或IQA/MOS通用替代。

**离线**：多VLM/检测器产生伪影候选→合并/视频检验/人类抽查→Qwen3-VL-8B两阶段SFT+GRPO，多reward包含格式、参考伪影semantic recall、双视频偏好及非对称长度惩罚。**在线**：视频证据→缺陷列表→得分→可选重写prompt（Veo3.1）或作为RL奖励训练Wan2.1。

**作者证据**：Table1在OOT GenAI-Bench w/o ties准确率0.753 vs VisionReward 0.744；VBench2 w/o ties 0.524 vs VideoAlign 0.473；**MonetBench 0.697 < VisionReward 0.721**，不是所有场景第一。T2VQA-DB（1000 prompt×10候选、27 human raters）Kendall与Hit@3/5作者最优，但VideoAlign的Hit@1和Spearman更优。Table2显示未SFT时对某些benchmark劣于无训练Qwen，且参考artifact语义匹配依赖LLM judge。

**反证/边界**：误差列表可能不完整或受同源VLM标注偏置；reward上升也可能诱导视觉取悦和不忠于输入的内容。主要是生成视频数据，未验证真实RAW/低光TM/局部事实保持。零偏差或独立因果解释不能从作者消融得出。

## 证据与争议
证据均来自作者报告，不能称独立重复验证；比较同输入、同监督/预算、同执行器后的实际收益才足以归因到该模块。跨设备/跨相机与真实部署尚需针对性验证。见上段具体反例。

## 行动与方案
PROBE 结构化故障证据作为视频judge学习机制；当前修图不默认把judge视为瓶颈。固定候选池/标签与计算预算，比较“直接scalar”“自由理由”“可验证artifact list”，报告人工pairwise winner和受保护内容真实性。

**记忆锚点**：视频奖励先列具体可观察伪影、再基于列表打分；对伪影召回、列表长度和人类偏好分别训练，检验解释过程能否改善奖励可用性。

## References
- https://arxiv.org/html/2611.07301v1
- https://arxiv.org/abs/2610.26740 (CheckDistill; 跨任务历史锚点)
