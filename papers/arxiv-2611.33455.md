# Recovering What Matters, Transferring Only What Is Reliable: Toward Precise Reference-Based Super-Resolution

ID: arxiv-2611.33455 | Sihan Ji, Wenxin Chen, Yue Shi, Jiezhang Cao (SJTU, Michigan, Shanghai AI Lab) | T03 / T02,T04 | restoration, reference transfer, evaluation | GO-E | Benchmark + reliability gate.
First verified: arXiv v1 2026-11-25; first covered/checked 2026-11-27. Original method, VeriRef benchmark and main/ablation tables checked; no independent reproduction.
Decision key: RefSR must separately measure exact information recovery and wrong-reference leakage.

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [下一实验](#下一实验) · [References](#references)

## 快速回忆
- PreciseRef 在 FLUX SR 上引入语义相关 gate 与双向局部一致性 gate，只传递“全局相关且局部可逆对应”的参考信息。
- VeriRef 把文字/条码/二维码和人脸身份变成可执行评价：不仅问看起来像不像，还问能否精确解码、是否泄露错误参考。
- 训练只有匹配参考；错误参考鲁棒性来自 gate 的归纳偏置，因此跨域安全仍需外部验证。

## 精读记录
VeriRef 含55个条码、25个二维码和100个身份。正确参考下，作者方法文字准确率.8560、代码解码.7625、PSNR23.4198、LPIPS.1797；Ada-RefSR文字.1735且解码为0。人脸正确参考 ID=.6675；错误参考时与目标 ID=.3891、对干扰者泄露=.1287，优于多数组合基线。双尺度 gate 在全局语义相关和局部反向注意对应处共同开门；随后将三步生成蒸馏为一步。

## 证据边界
VeriRef规模小且任务集中；没有手机实拍 RAW、真实裁切链路、移动端时延/功耗或独立人评。错误参考未进训练，可能在更相似干扰物、遮挡和复杂文本上崩溃。ArcFace/解码成功是重要但窄的保真指标，不能替代全部视觉质量。

## 下一实验
构造跨相机、跨年龄/姿态、反光与小字号干扰集；对比无 gate、单 gate、简单置信阈值和拒绝参考；将“保守退化到无参考 SR”设为安全基线，报告错误参考下最坏分位而非均值。

## References
- https://arxiv.org/abs/2611.33455v1
- https://arxiv.org/html/2611.33455v1
