# Multidimensional Observer Model

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)

- 完整标题：Multidimensional Observer Model and Perceptual Dimensions of Human Image Quality Assessment
- 作者：Sheng Zhao、Weikai Lin、Yuhao Zhu
- ID：arxiv-2609.38487；主题：IQA / perceptual modeling
- arXiv 公开元数据日期：2026-09-29；首次简报：2026-10-01；核验：2026-10-03。
- 核验范围：arXiv 索引中的原摘要与元数据；全文、会议归属、当前版本与资产状态未完整核验。
- Decision key：task-dependent-perceptual-quality-subspace

## 快速回忆

**问题：**图像表征很高维，人类判断质量实际使用多少维？

**旧→新：**不只训练一个 MOS 分数，而把图像表示成感知空间中的分布，用带噪采样比较建模人类判断。

**记住：**低维且依任务变化，不是“所有 IQA 只需要二维”。

**下一步：**分色彩、纹理、结构和语义任务，检查维度变化与跨数据集迁移。

## 精读记录

[原摘要](https://arxiv.org/abs/2609.38487) 描述以神经表征约束并拟合行为数据的多维 observer model；作者报告不同层级质量判断需要不同结构的低维感知空间。

待精读：维度选择方法；被试与任务协议；训练/测试分割；模型可辨识性；相比现有感知指标的统计显著性。旧简报中二维坐标轴的具体解释在本轮未核表，不作为一般规律继承。

## 证据边界

模型能解释特定行为数据，不自动证明这些维度是大脑唯一真实机制。不同任务和失真分布可能需要不同空间。当前不作“新行业标准”或“替代 VLM-IQA”的判断。

## References

- [原论文](https://arxiv.org/abs/2609.38487)
- [alphaXiv 阅读入口](https://www.alphaxiv.org/abs/2609.38487)
- [归档协议](../ARCHIVE_PROTOCOL.md)
