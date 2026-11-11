# DynOLAT: OLAT Video Prediction for Controllable Dynamic Full-Body Relighting

元数据：Taoming Liu, Yinji ShenTu, Guangzhao He, Yudong Jin, Yukang Ye, Siyu Zhang, Fan Jia, Wei Hua, Hujun Bao, Xiaowei Zhou；浙江大学/Cornell/4DV.ai/Ant Group 等；arXiv **2611.11210v1** 首传 **2026-11-08**，进入 2026-11-10 cs.CV 公告；首次覆盖 **2026-11-11**；SIGGRAPH Asia 2026 TOG 接收/DOI 不作为独立新事件，项目更早可公开日期待进一步校验。原文 Methods/Dataset/§5 和消融已读，非独立复现。**GO-E**（数据/物理可控执行/现实硬件成本完整揭示），主 **T02**、次 **T05/T01/X01**；角色 **采集/数据/执行/目标/训练/部署**；地图变化 **New route / Engineering maturity / Boundary refinement**。

目录：[快速回忆](#快速回忆) · [旧问题与新机制](#旧问题与新机制) · [证据与反例](#证据与反例) · [完整系统](#完整系统) · [References](#references)

## 快速回忆
**一句话技术命题**：不直接猜整幅「新光照视频」，而是先从同一人的视频预测各单独方向的 One-Light-At-a-Time (OLAT) 响应基视频，再按目标环境光方向/强度在**线性光域**加权重组，使照明方向和强度成为可检查的变量。

**记忆锚点**：**先学不同入射光的响应基，再重组环境光，不等于让生成模型直接按文本「变暖/变亮」。**

## 旧问题与新机制
前序：**Lux Post Facto (CVPR 2025)** 用 conditional video diffusion 做动态人像 relighting；**HumanOLAT (ICCV 2025)** 提供 full-body OLAT 静态/采集训练基底；**UniRelight / RelightVid / DiffusionRenderer (2025)** 直接生成视频重照明。论文引用并比较；不把几种不同数据/生成机制画成直接继承。
本文新增 **24M+ 帧**、**224 identity-outfit combinations** 的动态+静态 full-body OLAT 实采：101 照明单元、同步多相机采集，光学流将交替 flat-lit / OLAT 帧对齐；采用 source-to-OLAT video latent bridge、球谐方向条件预测各方向的基视频；目标环境图做线性光域加权；in-the-wild 输入先 delight 近似 flat-lit。
关系：与 Paste2Place 都是 source-anchored bridge 和物理分解的共同抽象，但不同任务、数据和 target，不宣称直接继承。

## 证据与反例
作者 Table 2 于自身 OLAT paired 数据、并对各比较法进行了 **channel aligned** 消除整体强度尺度歧义：PSNR **26.23 dB**、LPIPS **0.0567** vs DiffusionRenderer **23.11/0.0900**、UniRelight **22.91/0.0928**。这支持测试集的颜色与光照响应但**单一尺度对齐的 PSNR 不独立证明绝对亮度精度**。Table 3 temporal LPIPS **0.02532** vs DiffusionRenderer **0.02629**，RAFt warping error **0.00065 vs 0.00078**。
Ablation Table 4：full PSNR **27.61**，Frame Concat **27.67** 更高（LPIPS full 0.0727 vs Frame Concat 0.0750）；不能说 latent bridge 对所有指标独立最优。实际端到端昂贵：在 **8×A100** 上，**57 帧 1920×1088、101 OLAT bases 需约 26.89 分钟**；101 张基生成后 relight 合成可快速重用，但初始化不是实时。视频 VAE 细节丢失；in-the-wild delight 仍留强阴影及有色照明；**不同 OLAT 基之间、跨相机并无严格一致性保证**。

## 完整系统
**目标**：给真实人物相同动作的视频更准确改变方向/相对光强；**非目标**：现成手机端实时重照明、准确真实场景背景/混合色光、手机 AWB/CCM。**输入**：已有 flat-lit video（或需 delight 的普通视频）+ 环境 HDR light map；**输出**：被重照明 RGB video；**目标由**环境图和人工/数据集指定，不由 VLM 文本自行定义。
**离线**：LightStage、多相机时分 OLAT/flat capture → 对齐监督 → 训练 Wan2.1 类 source bridge OLAT predictor → 真实 human/outfit 隔离测试及光照方向强度对照；训练 8 A100 约一周。
**在线**：源视频→（非平光时 delight）→预测 101/201 direction OLAT basis 并缓存→按环境图在线线性组合→检查身份纹理、shadow direction、relative intensity、temporal flicker。没有真实验证的 Agent 控制环或手机编解码闭环。
**最小判别**：固定同一批真 OLAT GT，对比直接 image/video relight 与先预测 OLAT bases 重组，分开报告方向误差、可控强度曲线、source preservation、生成 101 bases 总时间。
## References
- [arXiv 2611.11210v1](https://arxiv.org/abs/2611.11210v1) · [HTML](https://arxiv.org/html/2611.11210v1)（§§3–5、Table 2/3/4、Appendix D）
- [作者项目与数据](https://zju3dv.github.io/DynOLAT/)
- [独立 canonical survey](../surveys/lighting-conditioned-portrait-video-relighting.md)
