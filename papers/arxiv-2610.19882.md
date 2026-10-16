# BluePixel：原生 4K 模型与 Agent 协同的图像编辑系统

- **身份**：arXiv:2610.19882
- **首次公开（已核）**：2026-10-14，v1
- **本次核验**：2026-10-16；selected sections + project links checked
- **独立复现**：未进行

## 快速回忆

**问题**：单一端到端编辑器难同时完成精确参数调节、垂直专家任务、模糊指令理解与 4K 保真。

**机制**：从 1K 预训练编辑器逐步适配 VAE 到 4K，continual learning 吸收长尾技能，RL 调整美学—保真权衡；SATP 将 50 步蒸馏到 4 步。Agent 把指令拆成专家/通用操作，用同一 reward model 验证并限次重试。

**证据**：作者报告单张 Kunlunxin P800 XPU 上 4K 编辑 8.7 s；VINS-4KEval++ 含 3,305 个原生 4K 样例，七模型中非编辑区域一致性仅次于 GPT Image 2。首页明确 vivo、南京大学、上海交大署名，并给出项目、代码和模型入口。

**决策边界**：8.7 s 是服务器级 XPU 的单次模型结果，不是手机端时延/功耗。训练与验证复用 reward model，可能形成共同偏差；排名不等于身份、文字或局部颜色绝对安全。

**下一步**：复核代码/权重许可证与可下载性；用脸、文字、重复纹理、局部色彩和极小编辑区域测试 SATP 与 agent 重试的保真回归。

## 精读记录

- 主要工业意义是把 native 4K 编辑公开成系统工程，而非只公布 backbone。
- 参数工具与生成模型的路由边界可能比继续放大单模型更可控。
- **可能关联**：适合作为编辑器“确定性工具优先、生成模型兜底、统一 verifier”的产品架构样板。

## References

- [arXiv abstract](https://arxiv.org/abs/2610.19882)
- [Project page](https://tech.vivo.com/BluePixel)
- [Author repository](https://github.com/vivo/BluePixel)
