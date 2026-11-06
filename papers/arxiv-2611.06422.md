# Unaligned Image Guided Denoising via Cross-modal Conditional Flow Matching (UGD-FM)

目录：[快速回忆](#快速回忆) · [机制与前序](#机制与前序) · [作者证据](#作者证据) · [系统位置与边界](#系统位置与边界) · [References](#references)

- **ID**: arxiv-2611.06422；**作者**: Runmin Zhang, Linshan Li, Si-Yuan Cao, Zhu Yu, Lingyu Zhu, Huaqi Zhang, Hui-Liang Shen（Zhejiang University / City University of Hong Kong / vivo）。
- **首次可核公开**: 2026-11-04 arXiv v1；**审查版本** v1；**首次覆盖/核验** 2026-11-06。
- **主主题**: T01（采集多模态信息）；**次主题**: T03/X01；**角色**: 辅助观测+配准/去噪执行器；**变化**: Bridge + Engineering maturity；**裁决**: GO-E（独立附加观测的系统价值，特定传感器条件）。
- **核验**: arXiv HTML 方法、相关工作、Tables 1–6、附录局限 selected_sections_checked；独立复现=否。

## 快速回忆

**抽象命题**：在可见光目标噪声太重而难以对齐时，让去噪与跨模态匹配相互改进；不是先把 NIR 强制精确配准、再单独去噪。

**先前并行路线**：单 RGB Restormer/NAFNet；近对齐 NIR 导引 denoising（CUNet、DVN、RFFNet、NAID、SANet）；以及预配准→guided restoration 两阶段。原文引用这些基线，但不是自动推定直接继承。变化是交替/联合条件化、稀疏跨视角引导和 1–2 step stage-focused flow。

## 机制与前序

在线：有噪声 RGB + 同场景但空间偏移且频谱不同的 NIR guide → flow 的中间 RGB 去噪表征 → 跨模态候选对应关系稀疏传播 → 更新图像并改进对应 → 1/2 步输出去噪 RGB。

离线：clean RGB 与真实 NIR 带跨视差关联 → 合成 Poisson–Gaussian RGB 噪声（训练 alpha∈[0,.03]、sigma∈[0,.3]）→ flow supervision + 对应一致性/感知几何正则。不是额外从单张 RGB 生成的“物理新观测”。

## 作者证据

- Table 1 FANVID、严重 Poisson-Gaussian alpha=.03/sigma=.3：Restormer 单图 30.69 dB；UGD-FM(Restormer block, 1-step)32.59 / 2-step32.82 dB；对应高层图像基线的推理网络和 guide 输入**不等价**，不能将收益全归 flow。其他跨模态引导基线也有公平对照。
- Table 6(a) 相同 Restormer block：直接回归 30.27，standard FM 1-step 30.28、2-step 30.34；加 stage-focused 后 2-step30.42；再加 inference-consistent state 30.58。Flow 本身的一步直接增益很小，收益来自训练/采样配套设计和跨模态引导。
- Table 6(b)：没有注意力 2-step 29.10，窗口匹配 30.03，adaptive sparse propagation 30.58；全局 attention OOM。证实 sparse aggregation 是重要负载模块。
- 明示局限：大三维视差、遮挡与跨视角缺信息时引导错误；联合对齐有计算开销；未展示实际手机完整双 sensor 捕获、功耗/时延。

## 系统位置与边界

适用前提是**确实采集到有信息的 NIR 或第二视角**。不改变单 RGB 的观测信息极限。移动端需计算第二摄像头/滤镜/校准/双路同步成本，避免将 NFE=2 写成实时部署。**GO-E**：多模态暗光质量研究；单传感器 RAW/TM 保留原流程。

## References

- [arXiv 2611.06422v1 方法、表及限制](https://arxiv.org/html/2611.06422v1)
- [跨模态无对齐导引恢复专题](../surveys/unaligned-guided-restoration.md)
