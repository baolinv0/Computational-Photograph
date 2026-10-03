# LOCI: Spatial Linear Memory for Streaming World Models

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)

- 作者：Ji Xia、Tingting Liao、Xuezhi Liang、Hao Li、Guangyi Liu
- ID：arxiv-2609.40222；主题：World Model / temporal state / geometry
- arXiv 公开元数据日期：2026-09-30；首次简报：2026-10-01；核验：2026-10-03。
- 核验范围：arXiv 索引中的原摘要与元数据；未完成全文与资产核验。当前版本状态待确认。
- Decision key：geometry-indexed-hybrid-world-memory

## 快速回忆

**问题：**相机回到旧视角时，模型需要找回对应历史；完整 KV 贵，固定递归状态又会丢细节。

**旧→新：**保留一部分显式历史，另一部分采用相机几何条件化的递归线性记忆。

**记住：**压缩历史与保留可直接访问的观测可以混合，不必二选一。

**下一步：**固定相同显存预算，分别测重访一致性、持续长度与推理吞吐。

## 精读记录

[原摘要](https://arxiv.org/abs/2609.40222) 描述一半 transformer blocks 使用历史 KV，另一半当前 chunk attention 配合几何条件化的 recurrent memory。作者在 MIND 与保留轨迹上比较重访重建，并报告相同长度下显存下降、有界观测库下固定内存流式生成。

待精读：相机参数来源与误差敏感性；读写寻址公式；比较模型是否同预算；长时失败案例；真实相机与动态场景适用性。旧简报的 H200 时间、秒数和显存数值本轮不作为已逐项验证结果继承。

## 证据边界

constant memory 不是实时，更不是端侧可用；重访一致性也不是物理后果正确性。当前是相邻领域的结构启发，不是已验证的 ISP world model。

## References

- [原论文](https://arxiv.org/abs/2609.40222)
- [alphaXiv 阅读入口](https://www.alphaxiv.org/abs/2609.40222)
- [归档协议](../ARCHIVE_PROTOCOL.md)
