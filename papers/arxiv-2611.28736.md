# DSRC — Dynamic Spectrum Re-parameterized Convolution for Cost-free Image Enhancement
更新 2026-11-25｜Zhiyan Zhou, Hailong Yan, Hanlin Liu, Yongrui Zhang, Xiangtao Zhang, Le Zhang｜arXiv v1 2026-11-21，11-24 cs.CV 公告，首覆盖 11-25。
X01 / T03,T01｜训练、执行、部署｜GO-E（训练参数化的工程增量）｜Engineering maturity + Boundary refinement。
## 快速回忆
训练时对卷积权重进行频带分解与高低通调制，辅以1×1/identity线性支路，部署前融合为同尺寸固定卷积。动态指学习过程，不是推理时逐图动态 kernel。不是首创重参数化：MobileIE（ICCV2025，同作者交集）已使用重参数化；CSSC为同部署复杂度对照。
## 精读记录
离线 paired task GT → 对 kernel DFT 径向频带 gain、高低通调制及残差支路联合训练 → 等价融合 W_fused = W_HL + centered W_1x1 + W_identity。线性、同网格及兼容通道为等价条件。在线 RGB→原网络固定卷积→增强；无FFT、无额外分支或Agent。
原文 §3 Table2 RTX3090 MobileIE LOL：base23.01、CSSC23.29、DyConv23.31、FreqFusion23.72、DSRC23.74 dB；base/DSRC同表 latency1.82（作者表口径）、参数4.05K和FLOPs0.92G。Table3 HL-only23.51、FB+HL23.54、full23.74。12组骨干/任务作者报告正PSNR增量；LOL +0.23–0.89、UIEB +0.23–0.67、Set5 +0.03–0.17dB。非跨手机RAW、端侧实测或独立复现。训练开销增加未量化，缺多seed/等训练自由度的普通线性多支路对照，收益可能是优化条件而非频域特有。
## 判断与行动
与 MobileIE 的训练期重参数化直接相关（原文引用并作为骨干），与推理动态路由竞争的是成本合同，不是同一机制。与真实端侧 benchmark 互补，不继承原MobileIE真机速度。固定训练集、步数、部署卷积，比较 vanilla、同训练自由度线性rep、CSSC、DSRC；多seed报告PSNR与真实SoC量化后 latency、功耗。保留现有ISP结构，不重构。
## References
- [原文 v1](https://arxiv.org/html/2611.28736v1)
- [MobileIE ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/html/Yan_MobileIE_An_Extremely_Lightweight_and_Effective_ConvNet_for_Real-Time_Image_ICCV_2025_paper.html)（官方摘要）
- [部署 survey](../surveys/mobile-isp-and-event-hdr-efficiency.md)
