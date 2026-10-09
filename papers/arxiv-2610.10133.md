# HarnessIR：以多模态基础模型执行真实图像恢复

- **身份**：arXiv:2610.10133
- **首次公开（已核）**：2026-10-07，v1；2026-10-08 更新 v2
- **本次核验**：2026-10-09；selected sections + author repository checked
- **独立复现**：未进行

## 快速回忆

**问题**：真实退化通常混合出现，按“去噪→去模糊→去雾”串接单任务工具会累积错误，也受工具库能力上限约束。

**机制**：五阶段 diagnosis → auxiliary evidence tools → prompt composition → MFM restoration → verification/refinement。OCR、脸、深度、分割等工具只提供证据，恢复由多模态基础模型一次执行；验证失败时重新从原图出发。

**证据**：作者在 MiO100、Real-Paired-200、Real-NoGT-200 上评价，并用 DF-Score 分拆退化去除与内容保持。作者仓库在 10 月 7 日标注发布代码、benchmark 与可视化；v2 的具体差异尚未核实。

**决策边界**：核心 executor 为闭源/外部 MFM；verification 可能与 executor 共享偏差。无真值真实图上的高分不能排除幻觉、文字/身份改变，也不是端侧 ISP 证据。

**下一步**：优先跑高风险 fidelity suite：文字、脸、重复纹理、局部颜色、未退化区域、RAW-to-sRGB round-trip；记录每阶段调用、重试率、成本和端到端时延。

## 精读记录

- **公司归属**：论文首页明确含 OPPO Research Institute 与香港理工大学作者，符合 CameraPaper 的论文时署名门槛。
- **竞争机制**：应与固定工具链、单次 MFM、同预算多次采样、带 oracle 退化标签的上界并列；否则无法把增益归因给“agent harness”。
- **工程含义**：价值在“证据编排 + 恢复执行 + 独立验证”接口，而非简单增加工具数量。
- **风险**：当 verifier 看不见高频细节、设备颜色或身份约束时，闭环可能稳定在错误但讨喜的输出。

## References

- [arXiv abstract / submission history](https://arxiv.org/abs/2610.10133)
- [作者代码与 benchmark 仓库](https://github.com/PolyU-VCLab/HarnessIR)
