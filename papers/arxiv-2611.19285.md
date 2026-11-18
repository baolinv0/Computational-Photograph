# Generate, Align, and Restore: MLLM-Empowered Diffusion for Generalizable Low-light Image Enhancement (MrLIE)
更新：2026-11-18｜canonical arxiv-2611.19285｜首次公开可核验：2026-11-14 arXiv v1｜首次覆盖：2026-11-18
主 T03；次 T06/T05/T04；角色：目标/执行/策略/评价；PROBE；地图 Bridge + Boundary refinement。
## 快速回忆
**一句话：** 先从低光输入生成正常曝光的参考，再用置信配准和原图结构约束把参考引导的信息转移至增强结果。
**记忆：** 自己生成的参考不是新的传感器观测；需隔离看起来合理的纹理与输入真实可证实的细节。
## 精读记录
- 输入 noisy/underexposed RGB。MLLM 生成并迭代自检查正常曝光参考；COM 学偏移与对齐置信度；SAI 合并输入结构、参考特征和 ControlNet 形式的条件，以 SD2.1 diffusion 输出增强图像。
- 作者使用 Gemini 3.1 生成与 Gemini 2.5 critic，分别为 LOL/U3D 数据设计训练；跨模型API费用和 H100 训练成本不可与单模型 ISP 模型时间混同。
- 选定 U3D ablation：添加 offset/confidence 的 NIQE 3.234→2.884，BRISQUE 7.258→5.368（作者报告；不是保真 GT）；人类偏好也不等于真实纹理恢复。
- 前序：Zero-DCE/EnlightenGAN 的无配对增强、AnlightenDiff 的输入锚点、MR. Illuminate 的生成先验；跨观测 UGD-FM 利用真实 NIR，**与生成参考不同**。
- 分层系统：离线无配对正曝光图+生成监督/训练结构锚点；在线输入图→MLLM 造参考→COM→结构受控 diffusion→结果；Agent/MLLM 决定参考修订而非直接输出可靠 GT。
## 证据边界
- 核验原论文 v1 选定方法、表格；偏好、NIQE、MUSIQ 只支持感知效果，不证明来源纹理真实。多轮 MLLM/生成/配准+diffusion 的成本与跨域能力是主要失效条件。
- **最小实验**：固定输入/下游执行器，比较真实 NIR 或外部参考、生成参考、无参考三路的遮挡/文字/人脸事实保持，控制总调用预算和生成随机性。
- 状态：PROBE，保留现有恢复架构，不替换成模型自造的图像参考。
## References
- https://arxiv.org/abs/2611.19285v1
- [生成参考导引专题](../surveys/generated-reference-guided-low-light-restoration.md)
- [非配准真实 NIR 导引](../surveys/unaligned-guided-restoration.md)
