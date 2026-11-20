# Edge-Efficient Joint RAW Image Compression and Restoration for Smart Wearable Devices

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [下一步](#下一步) · [References](#references)

身份：`arxiv-2611.24805`｜Yunong Sun, Sicheng Chen, Fei Xia｜arXiv v1 2026-11-18｜主题 Raw / ISP / X01  
核验：2026-11-20；原文方法、表3–7与设备拆账选段；代码入口可见；未独立复现。

## 快速回忆

- **问题**：穿戴相机若先压缩 noisy RAW 再后端恢复，传统 codec 会花码率保存最终会被去掉的噪声。
- **旧→新**：JXL/VVC→NAFNet 串联，改为边端轻编码器直接面向 clean linear RGB 目标；后端统一解码、去噪和去马赛克。
- **记住**：价值在“表示目标与端云分工”，不是单纯压缩率；论文给出 12MP Xiaomi 13 / Rokid Glasses 发送端 NPU、I/O、CPU entropy coding 与 50Mbps 传输拆账。
- **下一步**：固定同一传感器/噪声/码率与后端容量，比较 joint latent、VVC/JXL+rate-adapted restorer、clean-signal codec，并加入功耗、温升和无线抖动。

## 精读记录

输入为 Bayer noisy RAW，输出为 clean linear RGB。边端 analysis/hyperprior 产生量化 latent bitstream，后端较大 synthesis network 完成重建、去噪与 demosaic；小编码器由中等编码器蒸馏。

作者报告：SIDD 约0.25 bpp，Ours-M 52.90 dB，对 adapted JXL/VVC cascades 51.34/51.18 dB；未压缩 NAFNet 53.95 dB。Rokid IMX681 ISO800 的 12MP 样例用32帧均值作参考，Ours-M 0.028 bpp、32.45 dB，对 VVC+NAFNet 0.038 bpp、31.95 dB。

Xiaomi 13 的 Ours-S 12MP 发送端：NPU 236.45 ms、I/O 15.82 ms、CPU 43.98 ms、50Mbps 传输46.72 ms、合计342.98 ms；Rokid Glass INT8 合计1290.8 ms。不是实时视频，但比未压缩 RAW 仅传输4027 ms更接近可用离线拍摄。

## 证据边界

SIDD真实噪声场景有限，LSDIR为逆ISP+Poisson–Gaussian合成；高码率下紧凑 learned transform 饱和。真实眼镜样例只有32帧均值近似参考，未证明运动场景或跨传感器鲁棒性。未报告完整后端延迟、系统功耗、热稳定、无线重传和隐私成本；“27.6×”是256×256 NPU encoder 相对 NAFNet，不是完整端到端速度。

## 下一步

1. 复现0.25 bpp处公平 rate match，并保留 codec-aware restorer。
2. 加入整机能耗、温升、内存、BLE/Wi-Fi实际吞吐和后端时延。
3. 做跨IMX681/SIDD五机型留一传感器测试，分离 noise-model 与 latent 架构收益。

## References

- [arXiv v1](https://arxiv.org/abs/2611.24805v1)
- [作者代码 CRAW](https://github.com/coolsyn2000/CRAW)
- [SIDD](https://openaccess.thecvf.com/content_cvpr_2018/html/Abdelhamed_A_High-Quality_Denoising_CVPR_2018_paper.html)
