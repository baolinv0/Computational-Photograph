# Dense Illuminant Estimation：以物理合成数据补足多光源监督

- **身份**：arXiv:2610.06508；CIC 2026
- **首次公开（已核）**：2026-10-05，v1
- **本次核验**：2026-10-09；selected sections checked
- **独立复现**：未进行

## 快速回忆

**问题**：密集、多光源 illuminant 标签难以实拍获取，限制了空间变化 AWB/颜色恒常研究。

**机制**：利用 Hypersim 的渲染分量构造逐像素 illuminant chromaticity，形成 74,321 张图的 Hypersim-WB；以合成预训练支持单光源与多光源估计。

**证据**：作者报告在所测设置中相对既有训练方案最高约 28%/57% 改善。论文贡献主要是监督生成管线和数据，不是新的手机 AWB 网络。

**决策边界**：室内合成域、材质与渲染器偏差可能放大；非漫反射区域使用保守 residual/掩码。外景、混合光谱、相机光谱响应和真实肤色尚未覆盖。

**下一步**：先做 sensor-specific spectral response、真实 RAW 与局部灯光留出测试；按材质/肤色/高光/混合照明分桶，而不是只看全图角误差。

## 精读记录

- **竞争解释**：收益可能来自数据量或 domain randomization，而非“物理监督”本身；需要同规模无物理标签合成集对照。
- **工业含义**：可作为 multi-illuminant AWB 的预训练源，但进入 3A 前必须验证时序稳定、闪烁与曝光联动。
- **专利边界**：更值得查的是监督构造、像素级 illuminant 分解与 sensor adaptation，而非泛化的“用合成数据训练 AWB”。

## References

- [arXiv abstract / v1](https://arxiv.org/abs/2610.06508)
- [arXiv HTML](https://arxiv.org/html/2610.06508v1)
