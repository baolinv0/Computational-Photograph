# FlowTool

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)

- 完整标题：FlowTool: Controlling Tool Parameter in Image Retouching via Flow Matching
- 作者：Thanh-Long V. Le、Steven Walton、Seunghyun Yoon、Branislav Kveton、Trung Bui、Eunho Yang、Viet Lai
- ID：arxiv-2609.35673；主题：Editing / Agent / continuous control
- 已核验公开版本：2026-09-28，v1；首次简报：2026-10-01；核验：2026-10-03。
- 核验范围：原论文摘要、方法设定及可复现性声明（p.1–4、7、11），未完整复现。
- Decision key：continuous-tool-parameters-fixed-renderer

## 快速回忆

**问题：**把连续修图参数逐 token 生成，可能引入数值和串行成本问题。

**旧→新：**VLM 理解图像与指令，条件 flow 生成连续参数，另一个 head 预测工具是否启用。

**记住：**它不是把所有编辑规划问题都连续化；工具存在与参数值分开，renderer 顺序仍有假设。

**下一步：**在固定 renderer 下对比参数回归、AR 参数输出与 flow；再测试改变 renderer/工具集后的泛化。

## 精读记录

[原论文](https://arxiv.org/abs/2609.35673v1) p.4 假设 renderer 按自身静态工具顺序执行；模型学习归一化连续参数和 tool-presence mask，再还原成执行参数。因此不能将其描述为已解决任意工具排序与动态工具发现。

p.7 列出 MMArt-Bench、ArtEdit-Bench、MIT-Adobe5K 与作者内部 FlowTool-Eval。摘要报告相对所比较方法的效率优势，本记录不把摘要的倍数外推成移动端端到端延迟。

p.11 的 reproducibility statement 明确代码、权重和数据访问受内部批准限制。状态应为“公开论文、资产开放未确认”，而不是“已开源可运行”。

## 证据边界

这是单项系统证据，不证明连续 flow 普遍优于 AR、直接回归或优化器。固定 renderer、训练数据规模、奖励评价器偏差和工具集合变化都可能影响结论。

公司署名为 Adobe Research / KAIST；本仓库保留技术正文。不因其是企业论文就加入 CameraPaper 的手机厂商归属表。

## References

- [论文 / v1](https://arxiv.org/abs/2609.35673v1)
- [alphaXiv 阅读入口](https://www.alphaxiv.org/abs/2609.35673)
- [归档协议](../ARCHIVE_PROTOCOL.md)
