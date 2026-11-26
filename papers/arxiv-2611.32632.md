# HazeFlux: Few-Step Generative Priors for Real-World Image Dehazing

ID: arxiv-2611.32632 | Yunong Liu, Danna Xue, Javier Vazquez-Corral (UAB/CVC) | T03 / X01,T05 | training, execution | GO-E | Engineering maturity + Boundary refinement.
First verified arXiv v1 2026-11-24, 11-25 new listing; first covered/checked 2026-11-26. Earlier materials not found via exact-title search; not exhaustive. Original methods/selected results/appendix checked; no independent reproduction.
Decision key: adapt few-step image editor to restoration and bypass compressed latent detail loss.

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)
## 快速回忆
先学习去雾目标，再将源图空间结构通过额外路径送入 VAE decoder，避免完全依赖生成 latent。与 HNDiff 的物理 haze-noise 过程、DehazeXL 高分辨率全局/局部上下文为竞争路线；不是 skip connection 首创。
## 精读记录
离线 Stage1: FLUX.2 klein 4B rank32 LoRA，512x512 patches，3000 steps batch8；latent flow + pixel L1/LPIPS/SSIM。Stage2: 生成 stage1 latent（每输入6 seeds），训练 gated structure adapter + skip 到 decoder，1500 steps。单 RTX PRO 6000 Blackwell。
在线 LQ → VAE encoding + text condition → 从 Gaussian noise 4 step flow（guidance 1）→ skip-enhanced decoder，另从输入提取空间结构 → RGB；非直接从 hazy latent 初始化采样。无 Agent。
数据 Dense-Haze/I-HAZE/O-HAZE/NH-HAZE official splits，Merge-HAZE 合并各 train/test；受控真实雾不代表任意手机自然雾。
Table4 Merge-HAZE PSNR: 原始 FLUX 11.94 → Stage1 20.61 → Stage2 20.98；SSIM .506/.699/.722，Delta E 22.317/8.734/8.488。I-HAZE Stage2 PSNR 24.55→24.30，非全优。Table5 I-HAZE latent-only 23.62, full Stage1 24.55, LPIPS .438→.463，主要增益来自任务适配。
Table2 Merge Haze: best prior PSNR MB-TaylorFormer-B V2 20.37, full 20.98; FID 77.90 vs VIVNet 133.88, CLIPIQA .44 vs DeHamer .46. Table3 author reports 20/24 cross dataset comparisons; I-HAZE→O-HAZE 20.00 vs VIVNet21.68 dB is counterexample.
Appendix Table8 total 7.98B, trainable 12.55M LoRA +33.4M adapter; 1024 square RTX4090 3.44→3.75s with adapter. Model pipeline reported, not true phone E2E. Code promised on acceptance.
## 证据边界
不同 backbone 预训练/预算不可完全归因；增加33.4M参数的普通 decoder enhancement 或 source fusion 是强基线。保留源边缘不等于新纹理真实；雾的颜色/空间变化、夜景与手机 ISP 泛化未测。最小实验固定适配后的 checkpoint，比较原 decoder / 参数量匹配普通 decoder / gated skip / 简单源图频率融合，按雾浓度与边缘、颜色、残雾分层；不直接替换现有系统。
## References
- https://arxiv.org/abs/2611.32632v1 ; https://arxiv.org/html/2611.32632v1 (§3–4, Tables2–5,8)
- https://arxiv.org/abs/2608.10995 (HNDiff, abstract checked)
- https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Tokenize_Image_Patches_Global_Context_Fusion_for_Effective_Haze_Removal_CVPR_2025_paper.html (DehazeXL, official abstract)
- [高效生成恢复主综述](../surveys/efficient-generative-restoration.md)
