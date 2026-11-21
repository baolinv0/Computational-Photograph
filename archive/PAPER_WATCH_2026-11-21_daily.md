# 2026-11-21｜Paper Watch v3.2 增量 Topic Update（5 New）
这五项 arXiv v1 均在 **2026-11-19** 首传（2026-11-20 新公告），晚于上次成功覆盖的11-19公告；均是本轮首次检入，无同ID历史登记。原论文选定方法、表格、消融和附录已核验，非独立复现；未穷尽提前公开和OpenReview。

## 三个受影响的长期问题
| 论文与稳定位置 | 主要机制变化 | 强证据与最强替代解释 | 裁决与地图变化 |
|---|---|---|---|
| [FAIR 2611.26456](../papers/arxiv-2611.26456.md) T03/T06 | ROI与外部视觉/文字指导绑定到一次恢复；失败局部处的额外信息 | Synthetic FID63.28、ROI LPIPS0.0319 vs AdaRefSR81.93/0.0368；**参考来自 clean GT 区域辅助检索**，fully-LQ-driven FID67.97 | GO-E，New route+Boundary refinement |
| [RegionAgent 2611.26179](../papers/arxiv-2611.26179.md) T06/T03 | Step-DPO学习当前动作组件、trajectory-DPO学后续整轨迹后果 | 同专家/预算 Group C SFT20.01→step20.47→full20.90dB；10K步骤/20K轨迹GT-derived偏好；A100 18.60s/图 | PROBE，New route |
| [LG-FiLM 2611.25639](../papers/arxiv-2611.25639.md) T01/T02 | 共享 RAW ISP 中的 global/local scene-conditioned FiLM / soft experts | Fujifilm 24.998 vs RMFA-Net24.377dB，但 global-only24.857、local-only23.387与none23.366，MoE独立收益有限；ZRR需重训 | PROBE，Bridge+Boundary refinement |
| [AesDistill 2611.25635](../papers/arxiv-2611.25635.md) T02/T05 | 多生成教师颜色审美目标→结构保留小学生执行器 | 64,644教师编辑/约3360 H100 GPU小时→1.13M学生；16自动指标JS74.75 vs DeepLPF67.50；非真人总体MOS | GO-E，New route |
| [ApexFuse 2611.25453](../papers/arxiv-2611.25453.md) T05/T01 | 无唯一真实融合GT时，人机筛选多模态生成融合目标→FLUX LoRA | FMB分割mIoU59.05 vs Text-IF58.54，LLVIP检测mAP50:95 65.353 vs Mask-DiFuser63.872；任务模型重训、NR-IQA和Pseudo-GT并非物理真实 | PROBE，New route + Boundary refinement |

## 旧图—新增机制—不变判断
- T03/T06旧路线：AgenticIR、MAIR、DiTTo、RecurIR是行动与轨迹规划；SGVD、ExplicitIR为网络内部空间控制；ReFIR、AdaRefSR为外部参考。FAIR直接约束单次执行，RegionAgent训练多步动作策略，两者共同抽象是区域控制，未证实直接继承或组合有效。
- T02/T05旧路线：FiveK/PPR10K专家GT、PREEN与ATune显式目标、LC-ISP同设备多帧教师、DDFM等融合源保留。AesDistill生成**颜色外观**，ApexFuse生成**多模态融合目标**；二者目标与事实边界不同，“生成目标→训练学生”是分析者归纳的共同抽象而非已验证的统一系统。
- T01旧路线：AWNet/RMFA-Net/MetaISP等RAW→RGB架构及LC-ISP数据监督。LG-FiLM有显式条件化机制，但global-only已解释多数收益，不能从单幅图的局部路由推导AWB/AE/TM真机收益。
- 判断：采集信息/物理真值、期待外观、执行可达、策略可发现、评价可选择仍需分开；这些论文属于不同的离线教师、在线执行与Agent层，不能直接拼成部署系统。

## 系统方案回忆
在线路径A：Bayer+相机元数据→global/local条件化→共享decoder→RGB（LG-FiLM）。
在线路径B：VIS+IR→FLUX条件融合→RGB（ApexFuse）；其离线先用人机筛选生成目标、训练LoRA。
在线路径C：用户/系统给定RGB/LQ、ROI+参考→单次区域恢复（FAIR）；或共享Base+当前ROI→多次LoRA专家动作直到停止（RegionAgent）。后者离线偏好需要clean GT，在线不得使用该GT。
离线颜色链：源RGB→四生成教师外观→有置信度的结构/颜色对应→1.13M学生训练（AesDistill），在线学生独立执行。不能将GAN/flow推理耗时、训练GPU小时和端侧整链成本混为同一数字。
当前动作：**不修改已有产品或私有研究执行链**，先验证目标/参考真假、global-only与MoE、固定工具池内step-only与step+trajectory，才决定有无必要引入复杂策略。

## 检索与漏检控制
- 覆盖：2026-11-19首次上传候选的跨学科最新索引；9个核心作者的alphaXiv作者级索引；开放RAW/HDR/TM/ISP、图像修复/IQA/PGT/多参考/Agent query；arXiv v1原文方法、关键表格、附录；本仓库过去两轮daily/weekly登记。至少五篇由论文原始版本与arXiv元数据交叉核对。
- 关键警告：作者索引在2026-11-19后返回“无新作”，但开放检索确实找到Junjun Jiang署名ApexFuse以及Chao Dong、Jinjin Gu署名FAIR。故作者级检索状态应标 partial / source lag，绝不把它说成核心作者查无新增。
- 历史排除：Life-IQA+ 2611.25510是Life-IQA的journal extension，局部跨域结果也有下降，WATCH / 版本变化待核；TRACE 2611.25648 是sequential editing 候选，需比较已有多轮属性/保留survey，暂入backlog，不挤占本轮前五。HDR增益图伪装攻击和地震Agent不属直接关注门槛。AUTOREF旧种子不冒充新研究。
- 无法完成：arXiv部分类别官方日列表返回过期缓存，未证明cs.CV/eess全量新公告检索；OpenReview全量、每位作者个人主页、项目代码、真正独立复现及研究者先期公开材料均待核验，不推进这些来源的覆盖水位。

## 归档
五份canonical cards：[FAIR](../papers/arxiv-2611.26456.md)、[RegionAgent](../papers/arxiv-2611.26179.md)、[LG-FiLM](../papers/arxiv-2611.25639.md)、[AesDistill](../papers/arxiv-2611.25635.md)、[ApexFuse](../papers/arxiv-2611.25453.md)。
living surveys：T01新增[场景条件ISP](../surveys/scene-conditioned-neural-isp.md)，并修订[摄影目标](../surveys/photo-attribute-targets-and-editor-control.md)、[数据/PGT](../surveys/imaging-training-data-synthesis.md)、[选择性恢复](../surveys/selective-task-aware-restoration.md)及[CameraPaper AgenticIR](https://github.com/baolinv0/CameraPaper/blob/main/knowledge/imaging-agent/agentic-image-restoration-survey.md)。[总图](../LITERATURE_MAP.md)、[survey索引](../surveys/README.md)、根README同步更新。
alphaXiv逐项查重后入 Agent/Restoration/ISP/Color/Restoration，membership 再查询均有相应文件夹且保留Reading/Completed；更新registry后按实际读回记录成功。

## Sources
- [FAIR](https://arxiv.org/abs/2611.26456v1)
- [RegionAgent](https://arxiv.org/abs/2611.26179v1)
- [LG-FiLM](https://arxiv.org/abs/2611.25639v1)
- [AesDistill](https://arxiv.org/abs/2611.25635v1)
- [ApexFuse](https://arxiv.org/abs/2611.25453v1)
