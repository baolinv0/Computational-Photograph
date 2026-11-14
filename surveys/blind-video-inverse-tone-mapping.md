# 未知 Tone Operator 下的视频逆影调：可辨识性、算子分布与亮度偏差

更新：2026-11-14｜主 T02，连接 T01/T03/T05/X01；与[冻结VAE前HDR表示](vae-aware-hdr-representation.md)是**相邻但不同**的问题。

目录：[问题](#问题) · [竞争路线](#竞争路线) · [本轮判断变更](#本轮判断变更) · [可恢复系统方案](#可恢复系统方案) · [最小实验与缺口](#最小实验与缺口) · [References](#references)

## 问题
输入只有已经经历未知 Tone Mapping Operator (TMO) 与裁剪的8-bit SDR视频。**TMO未知**时，未裁剪信号可能部分约束其反变换，**饱和像素**对应一整段可能HDR辐射，无法仅凭输入辨识真实值。问题不是单纯“采用LogC3还是Log-Gamma”，而是观测模型的不确定性、归一化和潜空间亮度估计如何造成系统性过亮/过暗偏差。
目标是给出合理的 HDR 视频与明确的估计条件；非目标是宣称消失信息有唯一GT或手机camera端已实装。

## 竞争路线（不同系统接口，不画继承箭头）
| 路线/历史锚点 | 在线输入/控制/输出 | 离线训练与成立条件 | 失败/边界 |
|---|---|---|---|
| 手工反曲线（Banterle et al., 2006） | SDR + 选定扩张曲线→HDR | 人工经验/显示假设 | 在clip处无法还原真值 |
| 有监督回归（Eilertsen et al. 2017；HDRTVNet++） | SDR视频→RGB/HDR回归 | 配对HDR真值、固定/近似TMO | 训练tone operator域外错配 |
| diffusion 视频先验（LumiVid、DiffHDR、LumaFlux、X2HDR） | SDR + latent video generator→HDR | 预训练/多曝或合成HDR/SDR | 生成内容可能合理但辐亮度有方向性偏差 |
| 显式测试时估计/识别退化（Xu et al., 2026 相邻路线） | SDR→operator/embedding估计→ITM | operator可估计、可泛化 | 被clip区域T无法唯一观测 |
| **多TMO训练边缘化+clipping-gated expectile（[新作](../papers/arxiv-2611.15146.md)）** | SDR→不需单独operator ID的video flow→HDR | 五TMO覆盖可能形成机制；需HDR训练母数据 | 超出TMO族时边缘化失效；非对称损失/表示依赖对照 |

历史锚点Banterle/Eilertsen等从新作Related Work确认，除本轮论文之外未完成逐篇全文重读，需留backlog。与Dark Matters/LumiVid的**VAE表示**联系是综合抽象，不表示相互方法继承。

## 本轮判断变更
**新作 [Reframing Video Inverse Tone Mapping...](../papers/arxiv-2611.15146.md)**，v1首次公开 2026-11-11：
- 作者先量化clipping区域有符号luminance error，并分析它随未知TMO变化；用冻结视频latent的固定affine log-luminance readout监督局部估计。
- 训练时把HDR母数据用5个TMO合成SDR，使模型对训练operator分布进行边缘化；对于不可观测的clipped tokens，仅在这些位置对上下偏差使用非对称expectile类权重。
- 同一主干与部分预算控制下，作者报告mean luminance RMSE 0.141相对其他公开方法0.179–0.341；within-paper单TMO对照的between-operator variance分量从2.7%/8.0%压到0.2%，但operator变化也增加了数据多样性。
- Filmic增益明显小于Hard-Clip/Severe，一种soft Grading operator上并非最优；out-of-family Severe仍失败，作者只训练一次独立run，且评价依赖光度对齐与HDR视频数据。
- 不能把三组测试或一篇论文称为通用operator不变性共识；这是新问题诊断+局部实证。

**旧→新：** 原地图关注如何在VAE前编码HDR或提升image fidelity；现在新开一条“未知成像算子与不可辨识区域”的T02路线，要求单独报告operator-generalization、signed bias、clipped-region fidelity；仍保留表示/超分/真实采集分离的旧判断。

## 可恢复系统方案
**目标/非目标：** 未知TMO下SDR视频升级HDR，降低有符号偏差；不是恢复场景唯一radiance truth。
**训练离线：** HDR源数据→物理/感知TMO族合成SDR视频→冻结VAE潜坐标log-luminance readout→以已知HDR supervision训练视频latent流LoRA→损失基于是否饱和选择对称或非对称权重→独立未见operator与素材评价。
**在线：** SDR流→（TMO未知）条件视频流模型→HDR radiance proxy→HDR编码/显示交付；推理无需隐含测试时operator oracle。视频模型及编码的真实E2E成本未有手机实测。
**Agent层：** 原论文没有；外部代理选定保守/生成强度是尚未验证的组合。
**强简单baseline：** 同样五TMO训练的对称损失、one-TMO训练的非对称损失、仅固定曲线回归，以及online operator estimation；必须同数据量、同VAE/网络及训练预算。
**评测：** CVVDP/PU21-PSNR之外记录operator分层、clipped/unclipped、signed L error、跨TMO偏差、时间稳定与绝对亮度对齐依赖。
**成本：** frozen video backbone + LoRA及潜VAE和视频解码；不能用训练步数代替部署时延。

## 最小实验与缺口
固定相同HDR clip总数、不同曲线所产生的图像总数、冻结VAE与backbone；2×2比较 single/multi TMO × symmetric/expectile loss，在训练族内和族外各分clipped/unclipped报告signed bias及真实内容评价。
**Backlog：** 从正文链接独立重读HDRTVNet++、LumaFlux、多operator family的数据泄漏与HDR capture母数据；检查可辨识性论证的成立条件（曝光标定、color space、未知非单调local TMO、真实设备ISP串扰），下一轮不把该问题直接扩张为手机AE/TM闭环。

## References
- [arXiv v1 full HTML](https://arxiv.org/html/2611.15146v1) · [card](../papers/arxiv-2611.15146.md)
- [LumiVid](https://arxiv.org/abs/2604.11788)
- [DiffHDR](https://arxiv.org/abs/2604.06161)
- [Dark Matters card](../papers/arxiv-2611.13504.md)
- [VAE-aware HDR survey](vae-aware-hdr-representation.md)
- [HDR数据与Pseudo-GT专题](../HDR/HDR_Dataset_References_and_PGT.md)
