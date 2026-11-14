# 图像合成中的物体—环境光影协调：从前景融合到物理可监督一步编辑

版本 v0.2 | 2026-11-14（新增物体指定阴影去除竞争/互补分支，非新研究任务首创） | 主 T02，连 T05/T03/X01；特定研究分支，与基于参考的手机人像后处理不可混为一谈。
目录：[长期问题](#长期问题) · [路线对比](#路线对比) · [关键证据与判断](#关键证据与判断) · [系统回忆](#系统回忆) · [待补历史与边界](#待补历史与边界) · [References](#references)

## 长期问题
给定人物或物体已经固定粘贴在背景的 RGB image + object mask，真实感失败可能来自两个域：**物体表面的受光/材质呈现**，与**物体反过来给周边环境制造的接触阴影、投影、反射和发光**。编辑的目标不是重新设计物体姿态或场景内容；参考图不是当前源图的 ground truth。

核心问题：不改变物体细节、姿态和原本背景结构的前提下，怎样同时控制内部重照明与外部环境影响？

## 路线对比
| 竞争路线 | 在线输入 / 控制变量 | 训练来源/监督 | 成立条件 / 典型失败 |
|---|---|---|---|
| 传统区域颜色/Poisson/局部曲线 | 原图+mask→确定性像素/LUT | 不训练/人工修图对 | 肤色调节可控；无法凭空合成合理真实投影/反射 |
| 图像 Harmonization | 拼接图、前景 mask、目标背景 | 对齐 foreground appearance 数据（DoveNet、Intrinsic Harmonization 等） | 改物体颜色与亮度，但背景被默认固定，欠缺 scene effects |
| 专门 foreground relighting | IC-Light 等，以 RGB / illumination control 重照明 | relighting supervision、预训练 diffusion | 可以重照明，但投影、反射或遮挡处理有限 |
| 生成式插入 / 场景交互 | AnyDoor / OmniPaint / SHINE / ObjectDrop / PS-Diffusion | 多源图像编辑/显式或弱成对合成 | 开放但更容易变化物体身份、花纹、文字、姿态 |
| **指定物体的cast-shadow移除（与物体插入的互补逆问题）** | [FreeDeshadow](../papers/arxiv-2611.14608.md)：RGB+点/线/物体mask或描述文本→仅目标投影移除 | PCSRD+ 154,571 prompt cases / 28,573 base pairs；生成+target-shadow grounding+局部refiner | 目标物体不等于阴影ROI；2025已有PACSRNet，2026是扩展文本提示和高分辨率，真实GT/遮挡交叠仍缺口 |
| **显式物理分解 + source bridge** | [Paste2Place](../papers/arxiv-2611.09387.md)：RGB 已粘图+object mask→一次 bridge | 77,218 Blender 同几何对齐 G/B/O + 9,055 real OBER-derived pairs；物理参数 supervision | 适合固定 placement 的 object-scene pair；并非一切真实图像修复器 |

这几条为**同一问题下的竞争路线**；LBM 是 source-anchored latent bridge 的前序机制，Intrinsic Harmonization 是分解的引用前序，SHINE/ObjectDrop/PS-Diffusion 是直接相邻任务/竞争（不推断直接继承）。

## 关键证据与判断
**新证据（arXiv 2611.09387v1，2026-11-06）**：Paste2Place 将 scene-linear `I=A⊙S+R` 视作监督侧描述，物体内部校正 `M⊙(A_obj⊙ΔS_obj+ΔR_obj)`，环境外部 `(1−M)⊙(ΔD_env+ΔR_env)`，在同一推理前向导引 bridge。这区别于只给 VLM 语言“让物体更像背景”，物理量在 Blender 控制生成中有对齐训练标签。

作者 1,250 paired Bench：PSNR **30.83** vs MV-CoLight **24.35**；full vs w/o physical injection **30.83 vs 29.68 dB**；源 FLUX.2 9B **22.07**。归因结论：**主要大幅提升来自任务特定 bridge 训练+成对数据；物理分解带来可归因的约 1.15dB 增量**。Spatially shifted physical guidance 降至 28.20dB，是对空间正确性的一项反向对照。Wild 250 张人工贴图无 paired GT，使用有限人评，不能与 synthetic paired PSNR 混合。

变化类型 **Bridge / Engineering maturity**，裁决 **GO-E**（物理标注数据引擎 + 可控单步执行），不是首次提出物理编辑或一步模型。固定 pose 条件、专业 H100 0.743s/图，不能推断手机实时落地或真实手机 ISP 光谱色准。未提供“真实混合光源与多摄颜色一致性”的独立检验。强基线除了 IC-Light，应加入 region-wise deterministic retouch，避免只比较泛用生成编辑器。

## 系统回忆
**目标**：保留 pose/身份/小纹理；改变前景 shading 和必要外部 scene effects。**非目标**：跨相机风格模仿、RAW→sRGB 校正、场景物体新增位置规划。
**离线**：Blender 已知 geometry/material/illumination → 固定布局 G完整、B无物、O异光对 → 提取 RGB + albedo/shading/residual 与 masked edits → 合并真实 object-removal pairs → train one-step latent bridge + physical injection heads → held-out synthetic/real/Wild 评估。
**在线**：拼接 RGB+mask → model 预测空间物理变化 → source anchored latent update → RGB 合成。**评价**：foreground identity/texture/文字、background preservation、effect MAE、shadow geometry 与人评分别报告。
**Agent**：mask/位置由用户事先提供；不存在经论文证明的 Agent 自动决定区域、版本或何时回滚。若想延伸到手机后处理，先证实输出无需改场景内容时的强确定性修图路线能否达到目标；不能自动将用户的目标颜色偏差变成阴影合成任务。
**最小判别**：固定原图+ROI、同数据和同预算，compare (i) no injection bridge, (ii) physical injection, (iii) shifted guidance，分别按内外区域量化变化，检验是否真正分离光度控制与生成内容变化。


## 2026-11-14｜历史2025对象选择性移影的实质扩展（Update，不是全新任务）

**时间/同一性纠错：** IJCAI 2025 [PACSRNet](https://arxiv.org/abs/2501.15043) 已在 2025-01-25 公开“通过点/线/物体mask仅去除指定物体投影”的任务；[FreeDeshadow 2611.14608v1](../papers/arxiv-2611.14608.md) 2026-11-10 首传，是明确自认的 conference extension，不可把 object-aware shadow removal 包装成2026首次发现。

**真正新机制**：新增属性/空间关系/状态三种文本提示，将用户语义对象定位和其**空间分离**的cast shadow位置分为object-aware generator与cross-scale shadow grounding/local refiner；PCSRD由11,900/256²扩充为154,571提示样例/1024²，但基础只28,573独立object-shadow pairs，不能将prompt复用算作不同场景覆盖。

**横向机制关系（分析综合）**：Paste2Place 是“给新物体加上正确光影”；FreeDeshadow 是“在原场景里只删指定物体的投影”，两者方向相反。MetaShadow（CVPR2025）已有object-centered shadow analysis；传统global shadow removal与mask-guided shadow removal是直接替代，但使用不同输入控制合同，必须审查公平性。它们不是学术继承关系。

**关键消融**：作者报告去掉cross-scale grounding时目标shadow IoU 0.832→0.051；去掉shadow-aware aggregation时non-shadow PSNR下降约11.7dB、定位IoU仍相近。这直接显示**定位对错**与**非目标区域保持**是两个独立瓶颈。对真实手机还缺遮挡复杂场景、真实地面纹理GT与手机成本。

**完整系统（该分支）**：离线DESOBAv2真实/合成object-shadow pairs→多提示生成与MLLM+人工验证→generator/refiner训练；在线RGB+目标物体描述/点/线/mask→语义对象理解→shadow grounding→生成候选→target-shadow局部融合→输出；没有论文验证的Agent自动路由。强简单基线是object cue→shadow geometry/mask→确定性relight或inpaint+原图外区硬保留。最小判别实验固定基础样本、同提示/算力比较有无grounding与aggregation，并测shadow IoU、preservation及边缘不连续。

**判断更新**：过去把source-object mask作为光影生成支点；现在补充“提示指定的object并非实际修改区域，且源内容应保护”的逆任务。GO-E / material Update；前序完整证明不继承为本轮新文核验。

## 待补历史与边界
需要进一步独立重读：Intrinsic Harmonization、LBM、IC-Light、SHINE、ObjectDrop、MV-CoLight、PS-Diffusion 的原文主表、训练数据和预算；这里的 prior 标签依据 Paste2Place 原文 Related Work，不升级为逐篇已核验。一键模型能否恢复在 source 中没有的准确 shadow/reflection、现实拍摄材质可靠性与不同照明 SPD 的泛化仍未知。

## References
- [FreeDeshadow 2026 扩展原文](https://arxiv.org/html/2611.14608v1) · [卡片](../papers/arxiv-2611.14608.md)
- [PACSRNet / IJCAI 2025](https://www.ijcai.org/proceedings/2025/89) · [arXiv](https://arxiv.org/abs/2501.15043)
- [Paste2Place 2611.09387v1](https://arxiv.org/abs/2611.09387v1) · [详情卡](../papers/arxiv-2611.09387.md)
- [既有编辑器能力与几何训练](editor-understanding-and-geometry-training.md)
- [低光 RAW/AWB/光谱](low-light-raw-awb-illumination.md)
