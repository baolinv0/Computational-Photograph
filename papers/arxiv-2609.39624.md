# ExpandDiff

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)

- 完整标题：ExpandDiff: Dynamic Range Expanding Diffusion for Single-Image HDR Reconstruction
- 作者：Mehmet Emre Andıran、Zhuoqian Yang、Liying Lu、Mathieu Salzmann、Sabine Süsstrunk；作者拼写以原文为准。
- ID：arxiv-2609.39624；主题：HDR / inverse tone mapping
- arXiv 公开元数据日期：2026-09-30；首次简报：2026-10-01；核验：2026-10-03。
- 核验范围：arXiv 索引中的原摘要与元数据；本轮未完成全文和项目资产核验。当前版本状态待确认。
- Decision key：two-sided-clipping-training-hdr

## 快速回忆

**问题：**不同传感器和曝光导致暗部、高光丢失程度不同，固定训练裁剪分布可能不够。

**旧→新：**Dynamic Clipping Synthesis 随机采样两端裁剪范围，再用条件扩散预测感知编码的 HDR。

**记住：**适应更多 clipping 情况，不等于恢复了观测中不存在的真实细节。

**下一步：**将可观测与完全裁剪区域分开评价，检查颜色、结构与伪细节。

## 精读记录

[摘要](https://arxiv.org/abs/2609.39624) 描述像素空间扩散、空间自适应归一化及有界输出，统一重建两端裁剪。作者在 SI-HDR 上报告结果，但本次不继承旧简报的全部指标增幅，因为数据划分、基线与表格尚未逐项复核。

待精读：DCS 具体采样分布；PU21 编码与输出边界；不同曝光/相机上的泛化；推理步数与完整计时。

## 证据边界

目前是“可追溯的摘要级研究卡”，不是完整论文评审。项目入口由原摘要给出，代码、权重和许可证是否齐全仍待检查。不能从单篇论文得出 HDR 重建行业路线已经改变。

## References

- [原论文](https://arxiv.org/abs/2609.39624)
- [摘要提供的项目入口](https://memreandiran.github.io/expanddiff/)
- [归档协议](../ARCHIVE_PROTOCOL.md)
