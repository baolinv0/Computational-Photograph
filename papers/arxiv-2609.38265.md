# Raw Imagery Impacting Your AI: Should You Care?

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)

- 作者：Adrien Dorise、Marjorie Bellizzi、Stéphane May
- ID：arxiv-2609.38265；主题：Sensing / RAW / task-oriented imaging
- arXiv 公开元数据日期：2026-09-29；首次简报：2026-10-01；核验：2026-10-03。
- 核验范围：arXiv 索引中的原摘要与元数据；未读完全文、未复现。当前版本状态待确认。
- Decision key：sensor-quality-task-operating-matrix

## 快速回忆

**问题：**SNR、MTF、分辨率变好，是否一定让下游检测按比例提高？

**旧→新：**在受控退化下联合改变 SNR、Nyquist MTF 和地面采样距离，并比较不同轻量检测器。

**记住：**图像质量指标到任务性能不是一个可通用套用的单变量映射。

**下一步：**在具体目标任务上构造退化×分辨率×模型矩阵，而不是只按一个 IQ 分数选输入。

## 精读记录

[原摘要](https://arxiv.org/abs/2609.38265) 的对象是空间平台船舶检测，使用 Maxar 图像和 YOLOv5s、YOLOX-S、NanoDet。作者报告 GSD 对结果的影响较稳定，SNR/MTF 效应更依赖模型和分辨率，严重噪声与模糊组合损失较大。

待精读：退化合成与真实传感器统计是否一致；MTF/噪声的控制方法；训练时是否适配退化；测试划分与统计置信区间。

## 证据边界

这里的 raw/minimally processed space imagery 不能直接等同于手机 Bayer RAW。当前只支持该任务中的系统设计启发，不能推成通用的手机 ISP 选型结论，也不能说降低图像质量通常更有利于 AI。

## References

- [原论文](https://arxiv.org/abs/2609.38265)
- [alphaXiv 阅读入口](https://www.alphaxiv.org/abs/2609.38265)
- [归档协议](../ARCHIVE_PROTOCOL.md)
