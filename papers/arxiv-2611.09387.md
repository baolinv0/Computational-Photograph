# Paste2Place: A Bridge from Paste to Place

元数据：Hongzhen Li, Youwei Pan, Yingfang Zhu, Sen Zhu, Fengjie Zhu, Leilei Cao；Transsion；arXiv 2611.09387v1，首次公开 **2026-11-06**，首次覆盖 2026-11-10；selected original sections checked，非独立复现。**GO-E**（数据+工程和组件消融）；主 T02，连 T05/X01；角色 **目标/数据/执行/训练/评价**；地图变化 **Bridge / Engineering maturity**。
目录：[快速回忆](#快速回忆) · [机制和数据](#机制和数据) · [量化与归因](#量化与归因) · [边界与判断](#边界与判断) · [References](#references)

## 快速回忆
技术命题：用户已固定物体的姿态、位置、大小时，合成不仅要改变物体的光照，还要合理改变物体*外部*的阴影/反射/照明；把物体与环境物理变化作为显式可监督信号，引导一次源图到目标图的 latent bridge。
记忆锚点：**粘贴物体的内部颜色与外部光影是一次光传输事件的两种空间后果。**

## 机制和数据
在线 RGB 已粘贴图+对象 mask → 保留源图结构的 latent bridge（FLUX.2 Klein 9B 蒸馏骨干）→ 预测 object albedo/shading/residual 与 environment change → 按 `I=A⊙S+R` 解析重组，插入物体/背景两区域导引 → 一步 RGB 输出；不需额外文本、3D GT 或 Agent。与几何/内容重生成任务分开。
离线 Blender 同布局 **G 完整、B 无物体、O 异光独立物体** 提供对齐 RGB 和光照分解监督；77,218 Blender pairs + 9,055 OBER-derived photographic pairs，计 86,273 pairs；benchmark 1,000 Syn/250 Real 具配对 GT，250 Wild 无配对 GT 人评。215k updates、2×H100 80GB，真实数据子集没有物理层标注。

## 量化与归因
论文 Table 1，1250 paired 的作者报告：PSNR **30.83 dB** vs MV-CoLight **24.35**，LPIPS **0.0396** vs DreamFuse **0.0665**；前景 fMSE **713.2**、效果区 MAE **0.0589**。Wild 人评 15 志愿者、3340 ratings：均分 **4.01/5** vs Qwen-Image **3.60**。单 H100 平均 0.743s（作者自己的完整方法）；与其他模型/托管 API 的推理硬件和统计范围不同，**不得声称严格公平的加速倍数**。
关键 Table 2 归因：预训练 FLUX.2 9B **22.07 dB** → **同任务 bridge 训练但无物理 injection 29.68 dB** → full physical guidance **30.83 dB**；物理导引净改善 **+1.15 dB**（且 shift guidance 得 28.20，提示空间正确性有用）。所以主要收益更可能来自**针对已知姿态与数据的桥接训练**，不能把 8.76dB 全算给解析物理约束。

## 边界与判断
已有竞争：Intrinsic Harmonization、IC-Light（只更改前景光照）、SHINE（联合环境效果）、ObjectDrop、PS-Diffusion、MV-CoLight、LBM (ICCV 2025) source bridge。本文引用/采用源图 bridge 与 intrinsically decomposed correction，非首次提出 single-step image transfer。测试不代表真实移动 RAW ISP 的光源谱准确性、混合光面部肤色或设备级延迟。用于纯摄影后处理时须分别验证 source fidelity 和 shadow/environment leakage。行动：**保留为物理条件化合成的数据+系统基线，暂不替换用户现有确定性 photofinishing**。

## References
- [arXiv v1](https://arxiv.org/abs/2611.09387v1)，Methods §§3–4、Tables 1–2、Figure 7
- [独立问题 survey](../surveys/object-scene-composition-and-relighting.md)
