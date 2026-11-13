# Joint Activation and Weight Quantization for Learned Image Compression

- Paper ID: arXiv:2611.13707
- Authors: Yile Tu, Heming Sun
- arXiv first upload: 2026-11-10 08:00 UTC, v1
- Publication: IEEE VCIP 2026 (author-stated on arXiv)
- First covered: 2026-11-13
- Main theme: X01 — 学习式编解码与端侧部署
- Secondary themes: T03
- Verdict: GO-E
- Verification: full five-page paper, method and RD tables checked; no independent reproduction.

## 30-second recall

先用 SmoothQuant 在 activation/weight 间迁移量化难度，再用 GPTQ 适配变换后权重；关键不是串联两种 PTQ，而是按 LIC 的 rate-distortion 目标联合搜索每个模块的迁移参数。

## 完整系统回忆卡

- **设置：** Ballé2018、Cheng2020、Liu2023；Kodak/CLIC/Tecnick；32 张 ImageNet 256² crop 校准；W8A8/W9A9/W10A10；tensor-wise 或 channel-wise activation。
- **关键结果：** tensor-wise W8A8 的 BD-rate 增量在 Ballé2018/Kodak 从 SmoothQuant 155.56%、AWDB-PTQ 61.83% 降到 21.15%；Cheng2020/Kodak 为 12.01/8.74/4.68%；Liu2023/Kodak 为 34.66/21.60/14.69%。
- **机制：** 五个模块级 search unit；α∈{0.1…0.9}；每个候选执行 SmoothQuant+GPTQ，再以全局 RD loss 选择并提交。
- **边界：** 只证明 RD 保持；RTX PRO 6000 用于实验，没有整数 kernel、真实 NPU/手机时延、内存、能耗、熵编解码端到端测量。32 张校准数据的跨域稳定性未充分验证。

## 判断与下一实验

联合目标优于各自局部最优是可信的局部信号，但“可部署”仍未成立。下一步应在一个真实 edge NPU 上报告整数覆盖率、fallback、bit-exact entropy decoding、端到端吞吐/能耗和跨域校准漂移。

## References

- [arXiv:2611.13707](https://arxiv.org/abs/2611.13707)
