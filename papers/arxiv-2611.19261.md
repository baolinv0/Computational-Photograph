# dit.xpu: Taming DiT Sparse Inference on Mobile SoCs
更新：2026-11-18｜canonical arxiv-2611.19261｜首传 2026-11-14 arXiv v1｜首次覆盖：2026-11-18
主 X01；次 T03/T06；角色：部署/执行；GO-E；地图 Engineering maturity。
## 快速回忆
**一句话：** 对手机 NPU 友好的定长 tile 稀疏注意力、周期密集锚点误差补偿，以及 NPU+GPU 异构协作，可使 DiT 的注意力计算省时，而不把不规则动态稀疏直接丢给 NPU。
## 方法与证据
- 输入 DiT 多步降噪 latent、静态 halo mask、调度的 dense anchor；NPU 执行密集 anchor，GPU 做稀疏校正；共享 buffer 与 KV 加载/布局转换 pipeline 减少搬移。
- PKU 等作者报告两款 Snapdragon 手机、五个 DiT model，**端到端 denoising** 相比 Hexagon NPU baseline 最高 1.56×，attention kernel 最快 11.5×；两者分母不同。保持与 dense attention 近似的生成质量是作者测试条件下的结果，不等于准确原像素恢复。
- 先验：FlashAttention/Block sparse attention 与移动 NPU 部署、推理缓存是不同组合路线；不要误称单篇首创异构 NPU-GPU。
- 系统分层：离线预先设定 sparse/anchor 配置；在线固定 DiT steps→异构 attention 内核→denoising output→VAE/后处理。论文加速的 benchmark 主要计入 denoising，不是整个拍照、显示或温升过程。
## 边界与裁决
- 仅代表作者样机/模型/分辨率；手机相机 RAW→ISP、长时热稳态和运行功耗待测。对生成/编辑部署是 GO-E，但不要求当前 ISP 模块迁移。
## References
- https://arxiv.org/abs/2611.19261v1
- https://github.com/IF-LAB-PKU/dit.xpu
- [ISP 与端侧部署合同](../surveys/mobile-isp-and-event-hdr-efficiency.md)
