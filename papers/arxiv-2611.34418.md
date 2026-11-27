# SPGSR: A Small Pixel-Space Generator for One-Step Super-Resolution

ID: arxiv-2611.34418 | Yun Yue, Luming Liang, Yiqi Zhong (Microsoft) | T03 / X01,T04 | restoration, efficient inference | GO-E | Engineering efficiency.
First verified: arXiv v1 2026-11-25; first covered/checked 2026-11-27. Original methods, Tables 1–3 and training/inference accounting checked; no independent reproduction.
Decision key: vision-only pixel-residual SR can be much smaller than large latent generators, but GPU efficiency is not mobile evidence.

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [下一实验](#下一实验) · [References](#references)

## 快速回忆
- 31.8M 参数生成器在像素空间预测 LR 上的 RGB 残差；冻结 DINOv2 提供对齐语义，PixelRRB 修补 patch 边界。
- 两阶段训练：flow/reconstruction与路由/特征监督，再固定一步加入 LPIPS 与 DINO-feature GAN。
- 价值是参数、显存和训练像素账本更清楚；不是“端侧 SR 已解决”。

## 精读记录
DRealSR上28.53dB/.7729，RealSR 26.12/.7507，DIV2K 24.38/.6140；在视觉-only组多数全参考/感知指标领先。总加载53.86M，RTX PRO 6000、FP16、batch1、128→512为18.05ms/0.293GiB；VOSR-0.5B为50.47ms/1.672GiB，VOSR-1.4B为60.46ms/3.628GiB。训练使用LSDIR/DIV2K/Flickr2K/FFHQ、Real-ESRGAN退化，两张RTX PRO 6000，约0.325T训练像素。
RealSR消融中去DINO-GAN使DISTS .2001→.1924却CLIPIQA .6765→.5839、MUSIQ70.05→60.74，显示无参考/感知指标对对抗监督高度敏感；PixelRRB增益很小。

## 证据边界
没有人评、手机 SoC E2E、热/功耗或相机链路；合成退化训练与三套小测试集不足以证明跨传感器。指标彼此冲突，GAN可提高无参考分而不保证事实细节。代码仅承诺公开，当前可用性待核。

## 下一实验
在相同53.86M预算比较普通CNN/Transformer残差基线、DINO冻结/蒸馏/移除、PixelRRB等参替代；加入OCR、身份、重复纹理和移动SoC全链路测量；盲评必须与PSNR/LPIPS及事实错误并列。

## References
- https://arxiv.org/abs/2611.34418v1
- https://arxiv.org/html/2611.34418v1
