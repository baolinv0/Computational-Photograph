# An Efficient Training Paradigm for Image Restoration via Improved Fréchet Loss (FDIR)
更新：2026-11-18｜canonical arxiv-2611.20805｜首次公开可核验：2026-11-16 arXiv v1｜首次覆盖：2026-11-18
主 T03；次 T04/T05/X01；角色：训练/执行/评价；GO-E；地图 New route + Boundary refinement。
**注意：** 与 2026 年 8 月其它同名缩写 FDIR 不是同一个研究对象，须按 ID 区分。
## 快速回忆
**命题：** 用冻结视觉表征的全局+局部 Fréchet 特征分布匹配训练一步恢复模型，替代代价高的对抗判别器或教师轨迹损失。
**前序：** SinSR/OSEDiff 蒸馏、HYPIR/OMGSR GAN/score，Representation Fréchet Loss 2026 为直接相关机制前序，FDIR 将其适配低层恢复，不是声称首次发明 FD。
## 精读记录
- 固定图像恢复输入及高质量训练目标，冻结预训练 feature encoders，构造图像级/patch级 target-vs-output moments、历史 EMA 和 instance-adaptive alignment，微调一步扩散 backbone（含 LoRA）。
- 作者在 RealPhoto60 比较相近 40 A100 GPU hours 条件报告 MUSIQ 73.579 (FDIR), 42.595 (VSD), 52.089 (GAN); 对应数据与调参公平性仍需要进一步查证。
- **反向证据**：DIV2K-Val 公开对照 FDIR PSNR 19.414 dB，OSEDiff 20.529 dB、RealESR 20.781 dB；偏好得分/NR-IQA 上升不能推理像素内容更真实。
- 离线：HQ+LQ→冻结特征→FD matching+额外空间保持项→单步恢复器训练；在线：LQ→单步模型→恢复结果，训练成本不能按在线时延计算。
- 评价必须包含 GT/结构 ROI、强基线、MOS、真实数据 OOD 和完整推理开销。
## 证据边界
- 摘要/方法与选定实验/消融已核对，未独立训练；部署未知。最强替代解释：更强特征编码器、选定目标质量、损失权重、训练样本与预算相较 VSD/GAN 的差异。
- 结论 GO-E 是对**训练工程替代路线**，不是宣称真实保真最优。
## References
- https://arxiv.org/abs/2611.20805v1
- [高效生成式恢复总图](../surveys/efficient-generative-restoration.md)
