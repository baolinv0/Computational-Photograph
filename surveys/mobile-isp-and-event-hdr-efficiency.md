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

## 新证据

**Mobile AI 2026 Learned Smartphone ISP Challenge（2026-11-03）**：用 Sony IMX586 Quad Bayer RAW→Fuji GFX100 reference，1920×2560，Snapdragon 8 Elite Gen 5 与 Dimensity 9500 的 Adreno/Mali GPU 实测；该报告对比算子选择、画质、实际推理时延。是移动 GPU 部署证据，不是完整拍摄管线持续功耗。

**HIVE-Diff（2026-11-02）**：单 LDR anchor + events 分解时间生成和 HDR 内容补偿。作者报告 512²、L40S、25 step 约 1.79 秒/帧；对比一些 feed-forward 基线 ~0.037 秒/帧，尚非实时。事件缺失的静态饱和区仍由先验补全而非观测。

## 方案回忆

移动 ISP：传感器 RAW/metadata → 色彩/曝光/恢复网络 → GPU LiteRT/runtime → RGB output → GT fidelity、MOS、真实 end-to-end latency、带宽和热功耗。

事件 HDR：LDR reference + event stream → 对齐/时间约束 → HDR N frame 生成 → Scale/absolute luminance、时序一致性、运动/饱和区真实性和完整延迟。

## 判断

即使网络 GFLOPs 很低，也必须实机测 GPU 端到端性能；即使 HDR 生成很逼真，单参考与事件物理信息不足时也不能断言真实细节恢复。HIVE-Diff 是 sensor-aware HDR video 的 **PROBE**，Mobile AI 报告是部署技术成熟度 **GO-E**。

## References

- [Mobile ISP 2026](https://arxiv.org/abs/2611.05008v1)
- [HIVE-Diff](https://arxiv.org/abs/2611.03465v1)
- [既有 HDR data 入口](../HDR/HDR_Data_Taxonomy.md)
