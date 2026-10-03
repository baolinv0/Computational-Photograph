# RelayVSR

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)

- 完整标题：RelayVSR: Large-Small Model Collaboration for Efficient Real-World Video Super-Resolution
- 作者：Xijun Wang、Xin Li、Zirui Lang、Suhang Yao、Haoran Li、Zhibo Chen
- ID：arxiv-2609.37850；主题：Restoration / Video / reference-based rendering
- 已核验公开版本：2026-09-29，v1；首次简报：2026-10-01；核验：2026-10-03。
- 核验范围：原文摘要及选定段落（p.1–6、7 的时间口径文字、18）；未运行代码，未独立复现。
- Decision key：sparse-reference-vsr-system-reward

## 快速回忆

**问题：**大生成模型逐帧运行太贵；共享关键帧的错误又可能传播。

**旧→新：**大模型只提供稀疏参考 latent，小模型逐帧恢复；训练参考生成器时同时看关键帧和最终视频质量。

**记住：**好的参考图不一定是对下游视频最有用的参考。

**下一步：**扫关键帧间隔，分别测因果模式和双端参考模式的画质、错误传播、输入等待和模型时间。

## 精读记录

[原文](https://arxiv.org/abs/2609.37850v1) 的 Sparse Generative Relay 将参考信息缓存复用，轻量 Dual-Memory Video Transformer 同时保留关键帧和近期视频上下文。VARO 固定轻量 VSR 网络，用参考级和系统级奖励更新大模型。

作者摘要报告：1080p、单张 A100 80GB、15 帧间隔、双端模式下 29.29 FPS、13.82 GB、首帧模型时间 0.327 s；这些是作者测量，不是移动端结果。

**重要补充：**p.7 明确计时排除输入等待与模型外操作。双端模式还要等未来参考帧；30 FPS 输入下最多约 0.5 s。不得把 0.327 s 写成用户端完整首帧延迟。

## 证据边界

本次没有验证下载权重、环境安装或实际运行。摘要给出[代码仓库](https://github.com/kopperx/RelayVSR)，故状态为“有作者代码入口”，不写“已跑通”。参考生成错误、切镜和固定间隔仍需测试。

**横向对照待办：**固定相同退化、硬件与输入等待口径，对照逐帧生成 VSR 和传统确定性 VSR；不能只按 FPS 数字跨协议排名。

## References

- [论文 / v1](https://arxiv.org/abs/2609.37850v1)
- [作者代码入口](https://github.com/kopperx/RelayVSR)
- [归档协议](../ARCHIVE_PROTOCOL.md)
