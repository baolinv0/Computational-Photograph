# 低光 RAW、照明光谱与 AWB 联合恢复：究竟该恢复什么？

版本 v0.1｜2026-11-05｜T01/T02/T05

## 一分钟回忆

**核心问题**：低光噪声同时破坏亮度恢复、色彩估计和后续颜色校正所需的证据。仅改善 RGB 可见度不等于恢复正确 illuminant、CCM 或 RAW 信号。数据的曝光、光谱和目标渲染必须分别标定。

## 竞争路线

| 路线 | 数据/条件 | 控制与监督 | 解决与不解决 |
|---|---|---|---|
| 传统级联 | RAW/低光 RGB | LLIE→AWB 或 AWB→LLIE | 模块复用；顺序与域漂移可能放大误差 |
| 联合低光/AWB | 多照明×多亮度 RAW | 色度/照度中间 GT + 最终 RGB | [CHROMA-MILL](../papers/arxiv-2611.04092.md) 给出条件受控实验；不等于所有动态夜景 |
| 标准夜级物理光照台 | 参考+五档夜间光照 | Lux/光谱/NIR/对应几何监督 | [3L-D](../papers/arxiv-2611.02695.md) 控制有效光子与可见-NIR 谱；微缩景物非真实夜景 |
| 光谱条件化 CCM | 可见光 white point + 多通道 ALS | SPD 字典、virtual chart、per-shot CCM | [Beyond CCT](../papers/arxiv-2610.40175.md) 解决同色异谱引起的相机颜色匹配歧义；需要测量硬件和标定 |
| RAW-guided 合成与通用增强 | 少量 RAW/多曝光条件 + RGB 数据 | 生成退化、保留目标 | [MESS](../papers/arxiv-2610.24680.md) 扩大训练数据；合成并不自动代表真实特定传感器信息 |

## 新证据与局限

- CHROMA-MILL（首次 2026-11-03）：50 场景，4 标定光源，11 强度档，DSLR+手机；linear RAW 光源加权生成 convex-hull 混色和色度 GT。CTI-Retinexformer 对 DSLR 最佳级联约 +0.7 PSNR_L 与 -1.1 ΔE00；手机 PSNR_L 24.352 vs 最强列示级联 24.421，ΔE00 8.881 vs 9.327。不能说所有指标都胜出。
- 3L-D（2026-11-02）：5 个物理标定夜晚照明等级，0.1–1000 mlx 级，含可见/NIR 与静态/运动对齐；光学实验台与户外真实夜景仍有域差异。
- Beyond CCT（2026-10-29）：300 illuminants×3100 reflectances，synthetic mean angular error 1.89°→1.20°；LED-like tail 4.79°→2.80°。保留 held-out CIE 光源上的谱字典失配负例，真实手机多通道 ALS 接口未证。

**历史与同类**：SID/LOL/MILL/OLiVES 的数据条件不同；传统 AWB 统计估计、FC4/DWB/RL-AWB、CCT/xy-conditioned CCM 与 spectral recovery 是并行任务层，不把 exposure control、AWB chromaticity 与 color correction matrix 混为一个网络变量。

## 方案回忆

离线：测量 camera SSF + illuminant SPD → 受控强度/照明 RAW 配对（含中间 GT）→ 训练 LLIE、AWB、联合方案 → 跨机型和真实混合灯测试。

在线：RAW + 可用 ALS/元数据 → 光照证据/低光风险 → 选择分开或联合增强 + white balance → CCM/tone rendering → 分别检验 PSNR_L、illuminant angle、ΔE00、皮肤/中性区颜色以及 latency。

## 新旧判断

**旧判断**：LLIE 与 AWB 可模块级串联；更大量曝光模拟数据有助增强。**新判断**：必须单独测试暗光下的光源推断及级联误差传播；如果目标涉及非黑体混合光，还应保留光谱/CCM 失配对照。**不变**：RAW 光谱混合需要响应线性与几何条件，数据增强不创造已丢失的真实高光信息。不存在已被证明的手机端通用最优联合架构。

## 下一步缺口

CHROMA-MILL 的真实非均匀照明混合与 motion，3L-D 的外场光谱匹配，Beyond CCT 的 ALS 器件校准及手机端计算；独立作者/品牌跨设备重复。

## References

- [CHROMA-MILL](https://arxiv.org/abs/2611.04092v1)
- [3L-D](https://arxiv.org/abs/2611.02695v1)
- [Beyond CCT](https://arxiv.org/abs/2610.40175v1)
- [既有 MESS 与相关合成路线](imaging-training-data-synthesis.md)
