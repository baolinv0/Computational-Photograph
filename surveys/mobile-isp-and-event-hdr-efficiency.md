# 端侧 ISP 与 Event-HDR：采集接口和硬件成本如何改变方案？

版本 v0.1｜2026-11-05｜X01/T01/T03

## 一分钟回忆

**两个完全不同的路线问题**：现有 RAW→RGB 网络能否部署到真手机 GPU；一帧 LDR+事件流能否作为高时间分辨 HDR 的采集接口。它们不能按单项 PSNR 比出统一赢家，因为观测与成本不同。

## 竞争方案

| 输入与任务 | 执行方式 | 测试关键 |
|---|---|---|
| 手机 Bayer RAW→目标 RGB | 轻量 Learned ISP / 传统 ISP / 显式参数化 TM | 真实 GPU 时延、质量、内存、设备与分辨率 |
| 多帧 LDR/HDR burst → 多帧 HDR | 曝光包围+对齐融合 | 原始帧数、ghost、延迟 |
| Event-only → HDR video | 利用时间对比度轨迹 | 全局亮度/颜色漂移，缺绝对 anchor |
| **1 帧 LDR + events → N 帧 HDR** | [HIVE-Diff](../papers/arxiv-2611.03465.md) | 高时间率但生成先验不可观察性与成本 |
| **长曝光RGB + 短曝光高时率差分 CVS → 视频/去模糊/HDR** | [CoGenRec](../papers/arxiv-2611.07665.md)，稀疏时空指导+video diffusion+detail VAE | 多观测硬件、时间同步、真实遮挡和完整端到端开销 |

## 新证据

**Mobile AI 2026 Learned Smartphone ISP Challenge（2026-11-03）**：用 Sony IMX586 Quad Bayer RAW→Fuji GFX100 reference，1920×2560，Snapdragon 8 Elite Gen 5 与 Dimensity 9500 的 Adreno/Mali GPU 实测；该报告对比算子选择、画质、实际推理时延。是移动 GPU 部署证据，不是完整拍摄管线持续功耗。

**HIVE-Diff（2026-11-02）**：单 LDR anchor + events 分解时间生成和 HDR 内容补偿。作者报告 512²、L40S、25 step 约 1.79 秒/帧；对比一些 feed-forward 基线 ~0.037 秒/帧，尚非实时。事件缺失的静态饱和区仍由先验补全而非观测。

## 2026-11-07｜新增 CVS 多模态重建（Bridge / Engineering maturity）

**旧判断**：多曝光HDR/event路线的改进通常必须区分物理新观测和算法先验。**新证据**：[CoGenRec](../papers/arxiv-2611.07665.md) 让CVS（稠密长曝光RGB endpoint + 高时间率稀疏短曝光差分）约束扩散视频；同一输入做deblur、插帧、HDR。其SportsSloMo-CVS作者对相同传感输入baseline的去模糊/插帧/HDR PSNR领先4.40/3.89/5.04dB；采用~1M训练clips与曝光增强。确定性仅extractor模型在作者IV-E可有高PSNR，扩散首先改善感知FID却令PSNR下降，再由细节VAE恢复结构保真，因此不能把完整提升全部归因diffusion。

**判断更新**：这里新增的是**有用的高速差分观测 + 统一重建机制**，而不是无新增测量的单幅逆Tone Mapping。与HIVE-Diff是传感互补输入的并行路线（综合推断），不是方法继承。**不变**：要在相同传感器测量/训练数据/运行时预算比较真实结果；CVS传感成本、极端遮挡和实时硬件部署没有完全证实。

**离线/在线**：CVS真实/模拟配对+曝光噪声标签→extractor / video diffusion / 细节VAE分段训练→真实硬件验证；在线长曝光RGB+短曝光差分→时空对齐/置信提取→conditioned diffusion→RGB序列。控制层是采集/曝光条件，不是Agent必需；任何HDR高光内容须分开标可观测与生成先验。

**行动**：保留GO-E的多模态sensor-aware HDR研究分支；不改变现有单RAW/单RGB手机TM方案。最小判别实验固定CVS输入和采集，比较deterministic extractor、+video diffusion、+细节VAE，并监测PSNR、时序与真实设备时延。

## 方案回忆

移动 ISP：传感器 RAW/metadata → 色彩/曝光/恢复网络 → GPU LiteRT/runtime → RGB output → GT fidelity、MOS、真实 end-to-end latency、带宽和热功耗。

事件 HDR：LDR reference + event stream → 对齐/时间约束 → HDR N frame 生成 → Scale/absolute luminance、时序一致性、运动/饱和区真实性和完整延迟。

## 判断

即使网络 GFLOPs 很低，也必须实机测 GPU 端到端性能；即使 HDR 生成很逼真，单参考与事件物理信息不足时也不能断言真实细节恢复。HIVE-Diff 是 sensor-aware HDR video 的 **PROBE**，Mobile AI 报告是部署技术成熟度 **GO-E**；CoGenRec属于CVS专用物理新观测+生成恢复的 **GO-E（研究/硬件条件）**，不是手机部署确认。

## References

- [Mobile ISP 2026](https://arxiv.org/abs/2611.05008v1)
- [HIVE-Diff](https://arxiv.org/abs/2611.03465v1)
- [CoGenRec](https://arxiv.org/html/2611.07665v1)
- [既有 HDR data 入口](../HDR/HDR_Data_Taxonomy.md)
