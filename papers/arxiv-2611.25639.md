# LG-FiLM: Local–Global Mixture-of-Experts Modulation for RAW-to-RGB Reconstruction
更新：2026-11-21｜canonical arxiv-2611.25639｜arXiv v1 首传2026-11-19｜首次覆盖2026-11-21｜Fei Li; Xilei Cao; Shichang Zhai; Kun Zhan (LiAuto)｜主 T01，次 T02/X01/T05；执行/训练；PROBE；Bridge + Boundary refinement。

目录：[快速回忆](#快速回忆) · [路线比较](#路线比较) · [作者实验](#作者实验) · [系统边界](#系统边界) · [References](#references)
## 快速回忆
一句命题：单个 RAW ISP 网络可以共享编码/解码权重，但通过由全局+局部场景特征驱动的仿射调制改变处理风格，而不按场景复制整个模型。注意输入依赖卷积网络并非“固定 ISP”，本论文真正新增在瓶颈显式条件化的设计与实验。
直接机制前序/架构依据：作者述及 RMFA-Net 编码路径；MetaISP 的跨设备场景色彩条件、AWNet全局上下文、传统 FiLM 和 BPAM 的参数化处理是共同问题竞争/互补，并非发表顺序等于继承。
## 路线比较
输入 Bayer RAW→共享 encoder→全局池化 scene descriptor + 局部邻域 features→空间路由多个仿射专家、预测 gamma/beta→共享 decoder→RGB。专家没有各自的完整 ISP 参数；不是动态替换整套 ISP 处理模块。
离线是 RAW/RGB paired supervision；在线一次前向生成图。无外部 VLM/Agent、无真实场景测量真值控制；颜色/影调改变混在目标 RGB 中。
## 作者实验
- Fujifilm UltraISP：LG-FiLM 24.998dB/SSIM0.88366 vs 同作者复现 RMFA-Net24.377/0.87354（+0.621dB）；其余 challenge published scores非严格同训练/预算，不能强求直接公平性。
- ZRR 跨设备重新训练 PSNR21.249 vs published PyNET21.19；**不是训练在 Fujifilm 上直接零样本跨传感器**。
- InvISP-derived COCO 合成 RAW 重新训练 35.802dB；只能证实可拟合该模拟域。
- 关键 Table4/10 控制：no conditioning 23.366，full24.998(+1.632)；local-only23.387、global-only24.857（距离 full 仅0.141）。匹配容量单仿射 FiLM 路线也达到24.840甚至更轻模型24.912。故**全局条件化更关键**，8专家和局部路由独立增益有限、非必要机制证明。
- 全文没有手机 SoC真实端到端时延/温升/功耗证据；参数量/FLOPs不等于部署成本。
## 系统边界
**PROBE（调制机制实证 + 主收益归因不足）**。若验证，固定 RAW数据、GT、base encoder/decoder、参数和 FLOPs，比较全局 FiLM、局部 FiLM、局部+全局单变换、MoE，再分低光/逆光/多光源ROI测真实域误差和局部泄漏；不替换现有AE/AWB/TM。
记忆锚点：自适应 ISP 的主提升可能来自**全局 scene descriptor**，而不是多个专家本身。
## References
- [原论文 v1，§4, Tables 1–5/10](https://arxiv.org/abs/2611.25639v1)
- [同机 RAW/capture 数据监督](arxiv-2611.19284.md)
- [成像数据专题](../surveys/imaging-training-data-synthesis.md)
