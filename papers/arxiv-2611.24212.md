# DetailScale-SR: Decoupling Restoration and Continuous Detail Control for Real-World Super-Resolution

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [下一步](#下一步) · [References](#references)

身份：`arxiv-2611.24212`｜Shengchuan Gao et al.｜arXiv v1 2026-11-18｜主题 Raw / Restoration / Editing  
核验：2026-11-20；原文方法、表1–3与实验选段；模型入口可见；未独立复现。

## 快速回忆

- **问题**：生成式SR常把“恢复正确”与“纹理更丰富”混成一个固定输出。
- **旧→新**：固定fidelity-realism trade-off→冻结Qwen-Image 2.1 SR LoRA，仅训练scalar detail template，连续控制detail；可选双分支Detail-CFG外推。
- **记住**：s从0→1时PSNR/SSIM单调下降、MUSIQ/MANIQA上升；这更像可解释的偏好轴，不等于事实细节恢复。
- **下一步**：把“细节量”与文本/身份/几何正确性分开，用同一LR源的反事实审计。

## 精读记录

Stage I 用40k LSDIR与2k文字样本训练rank-64 SR LoRA；Stage II 从RTV平滑图到原HR线性插值构造连续目标，只训练block-wise attention template。RealSR上 s=0 的PSNR 26.69、MUSIQ 60.94；s=1为25.48/65.53；Detail-CFG γ=2为24.06/67.86。DRealSR同样呈现fidelity下降、NR quality上升。模型权重在ModelScope公开。

## 证据边界

训练输入为合成blur/downsample/noise/compression；文字恢复在重退化时可把可见文本内容作为prompt，不能算纯观测恢复。Detail-CFG生成“比GT更丰富”纹理，作者指标本身显示PSNR、LPIPS与FID回退；没有OCR准确率、身份一致性、跨尺度用户校准或移动部署。控制轴可能同时改变风格/语义，而不只高频量。

## 下一步

固定seed/prompt/source，测跨s的OCR、face/identity、geometry、non-target leakage和频谱单调性；把γ外推单独标为创作增强，不与事实恢复同分数。

## References

- [arXiv v1](https://arxiv.org/abs/2611.24212v1)
- [公开模型](https://modelscope.cn/models/DiffSynth-Studio/Qwen-Image-2.1-SR)
