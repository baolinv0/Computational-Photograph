# Reframing Video Inverse Tone Mapping as Blind Posterior Inference via Latent Luminance Supervision

- **Canonical ID:** arxiv-2611.15146
- **Authors:** Hanwool Sul; Chang-Hoon Jeong; Kisung Shin; Bomseok Park; Donghoon Cha; Hansl von Kwon; DoHyung Ku; Byoung-Tak Zhang
- **First public verified:** 2026-11-11 07:36 UTC (arXiv v1); checked version: v1
- **First covered / checked:** 2026-11-14
- **Main theme:** T02; secondary T01/T03/T05
- **Roles:** observation/target modeling, offline training, execution, evaluation
- **Map change / verdict:** New route + Boundary refinement / **GO**
- **Verification:** arXiv full HTML §§2–6, Tables 1–4, appendix boundary, no independent reproduction
- **Canonical survey:** [未知 Tone Operator 与逆影调可辨识性](../surveys/blind-video-inverse-tone-mapping.md)

## 30 秒回忆
**一句技术命题：** 在不知道源SDR由哪种tone operator生成时，饱和区域的HDR辐射不可唯一确定；训练时需覆盖可能operator，并控制未可观测区域的有符号亮度估计偏差。
**记忆锚点：** 逆影调不是简单的反曲线：operator未知＋高光裁剪会同时造成分布不确定性和亮度偏差。

## 先前路线与关系
- Banterle等（2006）手工扩展、Eilertsen等（2017）CNN ITM、Kim等（2019）视频ITM：历史奠基，非本轮新作。
- HDRTVNet++ / LumiVid（LogC3）/ LumaFlux / X2HDR / LEDiff：对照或竞争路线；作者区分固定tone operator、隐含operator与生成式prior。
- [Dark Matters](arxiv-2611.13504.md) 与 LumiVid/DiffHDR 探究**VAE前颜色编码**；本篇研究**未标定观测算子与饱和区训练动作**，属于互补接口，不能当直接继承。
- 论文引用 Xu 等 (2026) 对退化嵌入做测试时推断作为最近似的已知operator处理竞争路线；本篇选择训练期边缘化而非在线估计。

## 完整方案与关键证据
- **目标：** SDR视频转换为可重曝光的HDR视频，在未知tone operator时降低高光/阴影有符号亮度偏差；**非目标：** 恢复被clip删除的唯一真实辐射、手机端实时TM。
- **输入/输出：** SDR序列 → HDR序列；操作隐变量为未知的tone curve，clip region的观测不足。
- **目标来源：** HDR源视频及已知操作族合成SDR，取高动态参考作监督。并非每张真实SDR均有HDR GT。
- **离线：** 真HDR clips→从五种tone operators随机采样生成SDR→冻结VAE编码→冻结视频flow backbone + LoRA学习；固定潜空间log亮度affine readout，按观测约束对clipped tokens加非对称expectile权重，其他token仍对称。
- **在线：** 输入真实SDR→编码与条件video model→生成HDR；不需要知道tone operator是哪一个。operator不是已识别的显式控制变量。无Agent。
- **关键证据：** 作者在三种clip/filmic/severe测试及84个配对clips分析：其全法均值有符号亮度RMSE 0.141，其他公开方法0.179–0.341；强对照LumiVid的CVVDP在Hard-Clip、Severe提升大，在Filmic很小。operator边缘化的同训练步骤对照把between-operator error fraction降到0.2%，single-operator为2.7%/8.0%；然而不同operator训练臂也改变样本变化数，需要额外数据等价控制。
- **限制/替代解释：** 作者明确一个单训练run；超出训练operator族（尤其Severe）仍有有符号残差，shadow PSNR较hard clip掉3.84dB；光度中值对齐、HDR语义和VAE表示可影响结果。不能等同跨手机未知ISP全面适配。
- **成本：** 冻结大视频生成backbone和LoRA，未报告手机端E2E部署证据。强基线包括固定曲线多样化数据增强、显式operator推断、同算力直接回归ITM。
- **可达/发现/选择：** 该文通过训练降低估计偏差，不是多候选Agent选择论文。

## 评审与决策
**GO（问题和机制增量）**：重要证据是同样输入条件下显式控制operator分布与clipping位置，而非“又一个更强diffusion模型”。建议最小实验：固定HDR→SDR源clips、五种训练TMO和完全相同数据量与模型预算，只变single/multi-operator、对称/非对称loss，分clipped/unclipped ROI报告signed bias、PU21/ΔEITP并测试未见operator。

## References
- [arXiv v1 full HTML](https://arxiv.org/html/2611.15146v1)
- [LumiVid](https://arxiv.org/abs/2604.11788)
- [DiffHDR](https://arxiv.org/abs/2604.06161)
- [Dark Matters canonical](arxiv-2611.13504.md)
- [HDRTV1K / HDRMovie datasets](../HDR/HDR_Dataset_References_and_PGT.md)
