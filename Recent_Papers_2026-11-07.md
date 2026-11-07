# Paper Watch v3.2｜2026-11-07｜三个主题、五篇新证据

## 覆盖、时间与裁决

对比 2026-11-06 成功归档快照与 75 条 registry，检查 2026-11-06 arXiv cs.CV/eess.IV 官方新提交列表、开放题名搜索与核心学者 alphaXiv 重叠窗口（2026-10-24–11-07）。五篇均以 **2026-11-05 arXiv v1** 为最早本轮可核验公开材料，11-06 进入新提交公告。本轮阅读原文 HTML 方法、选定实验、消融和强近邻；不能宣称已遍历每个作者和分类，也不把摘要核验升级成独立复现。

| 论文 | 主主题/次主题；系统角色；地图变化 | 裁决 |
|---|---|---|
| [CoGenRec](papers/arxiv-2611.07665.md) | T01/T03+X01；采集/数据/执行；Bridge/Engineering maturity | GO-E |
| [OptIMerge](papers/arxiv-2611.07543.md) | T03/X01+T05；训练/部署；New route/Boundary refinement | GO-E |
| [WeLM-Image](papers/arxiv-2611.07392.md) | T02/T04+T05+X01；执行/训练/Reward；Engineering maturity | GO-E |
| [StitchEdit](papers/arxiv-2611.07922.md) | T02/T03+T06；训练/执行；New route/Boundary refinement | PROBE |
| [ArtiVidRM](papers/arxiv-2611.07301.md) | T04/T06+T05；评价/Reward；Supporting evidence/Boundary refinement | PROBE |

## T01｜物理额外观测与生成先验不是一回事

**历史锚点（非本轮新作）**：Tianmouc CVS 与 IGFNet/CBRDM、HIVE-Diff（1 LDR+events）、UGD-FM（RGB+NIR）。旧判断是新增时空/曝光测量可缩小恢复不确定性，但必须说明哪些信息真被观测到。

**本次**：CoGenRec 使用长曝光稠密 RGB 与高时率短曝光稀疏差分 CVS 联合视频扩散/细节VAE，处理去模糊、插帧、HDR。SportsSloMo-CVS作者报告对最强general CVS baseline分别 +4.40/+3.89/+5.04 dB，混合训练规模约一百万 clips。消融里生成主干先改善FID却降低PSNR，细节VAE才修复部分像素误差；不能将收益全算作diffusion，也不能忽略CVS硬件、数据和曝光增强差异。

**现在判断**：保留多传感器GO-E路线；单手机RAW/TM不变。离线实采+仿真+曝光增强→分段训练；在线CVS双测量→时空条件→扩散+细节解码→RGB。最小判别是同CVS输入/训练池分别对照deterministic extractor、+diffusion、+decoder，同时测设备全链时延。

[已更新sensor与Event-HDR专题](surveys/mobile-isp-and-event-hdr-efficiency.md)。

## T03｜恢复专家不一定需要在线MoE路由

**历史锚点（非本轮新作）**：Model Soups、Task Arithmetic、UniRestorer++层级MoE。旧路线有独立专项、联合训练backbone、层级条件路由。

**本次**：OptIMerge 基于相同底座已微调恢复扩散专家，用100–500图优化约3.2M融合系数，在attention通道和卷积空间核上做对齐；推理只剩一套网络但仍采用32 DDIM steps。作者OID+DPDD测试OID PSNR 22.72 vs simple soup20.88、joint22.59；DPDD 23.91 vs soup23.15、joint23.37。但其DPDD LPIPS 0.2191差于single expert0.2023，DPDD+SR任务的SR PSNR 21.12低于joint21.24。不能称零训练合并或手机实时恢复。

**现在判断**：新增后验参数合并作为与MoE竞争的路线，单任务小模型仍是强基线。离线多个FT专家→冻结→校准合并；在线一个merge diffusion network→恢复；不需要Agent。只有在确实存在多个同底座专家并需要合并时新增实验，当前TM不重构。

[已更新统一恢复专题](surveys/universal-restoration-degradation-routing.md)。

## T02/T04｜编辑执行能力和Judge偏好排序分开

**历史锚点（非本轮新作）**：Qwen-Image/Marigold、MT Forcing/TailSteer，以及VideoScore/VisionReward/CheckDistill。它们不构成被验证的单一工作流。

**本次**：WeLM-Image 是腾讯WeChat Vision的大规模多模态编辑/生成工程系统（MoT–MoE理解/生成路径、跨路径注意力、独立任务reward、蒸馏）。规模约31.7B stored/5.4B active generation，约50亿初始图像筛至6亿；规模/数据和模型结构分量贡献未被等预算完整归因，不能断言局部像素保护已解决。GO-E。

StitchEdit 先训练depth LoRA再用各层depth/edit梯度余弦选择保留和学习率，在自建150例几何编辑评测中DCS代理从同depth-init均匀FT的0.80升至0.92；简单fixed cosine已有0.90。训练编辑对/目标深度具有生成/模型代理偏差。只对3D位移、遮挡和视角编辑PROBE，不用于替换肤色/背景光度修图的mask控制。

ArtiVidRM 先预测视频伪影清单再评分，用伪影召回/长度和人类偏好联合训练Qwen3-VL；GenAI-Bench去ties作者准确率0.753 vs VisionReward0.744，但MonetBench0.697 < VisionReward0.721，T2VQA-DB Hit@1也非最优。PROBE视频Reward的证据表示，而非已经验证真实RAW/TM视觉保真。

**现在判断**：离线训练更强编辑器、迁移深度先验、训练证据型Reward是三个机制，互补但未联测。在线源图+指令→executor→候选；Judge应依据原始目标/ROI/可见伪影独立判断；Agent可调度但不能弥补不可达候选。当前区域编辑问题仍以target success和protected-region leakage双轴验收，不因本轮新增而改动方案。

[编辑器训练专题](surveys/editor-understanding-and-geometry-training.md) · [伪影Reward专题](surveys/artifact-grounded-reward-and-verification.md)。

## 回执和未完成

本轮新增五份canonical卡、两份有独立问题边界的survey；已改两份旧survey、LITERATURE_MAP、README、surveys索引并同步alphaXiv相关主主题。阅读状态未修改。GitHub registry与文件回读以实际后续检验为准。

待补：核心作者逐人成功水位、CVS真实硬件BOM/能耗、OptIMerge跨设备强基线、WeLM机制归因、StitchEdit独立真实深度GT、ArtiVidRM统一tie阈值与第三方评测。无以上证据不把作者结果当独立复现。
