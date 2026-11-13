# 端侧 ISP 与 Event-HDR：采集接口和硬件成本如何改变方案？

版本 v0.2｜2026-11-13｜X01/T01/T03

## 一分钟回忆

**两个完全不同的路线问题**：现有 RAW→RGB 网络能否部署到真手机 GPU；一帧 LDR+事件流能否作为高时间分辨 HDR 的采集接口。它们不能按单项 PSNR 比出统一赢家，因为观测与成本不同。

## 竞争方案

| 输入与任务 | 执行方式 | 测试关键 |
|---|---|---|
| 手机 Bayer RAW→目标 RGB | 轻量 Learned ISP / 传统 ISP / 显式参数化 TM | 真实 GPU 时延、质量、内存、设备与分辨率 |
| 通用 edge NPU（非手机 ISP） → 视觉任务输出 | [Edge NPU 三层基准](../papers/arxiv-2611.13563.md) | model-call 与 full E2E 的速度/精度/排名可能不同，不外推手机 |
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


## 2026-11-13｜端侧模型调用与完整部署合同分离（历史地图补齐）

[Benchmarking Vendor-Guided Optimizations on Edge NPUs](../papers/arxiv-2611.13563.md)（Youngjin Jo 等；arXiv v1 2026-11-10）已在 2026-11-13 周报和 alphaXiv 收录，本次为 **missing_map_integration**，并非新论文。主主题 X01，次主题 T01；角色 deployment / evaluation；GO-E；Engineering maturity / Boundary refinement。

**一句技术命题：**固定统一输入输出的模型转换优化，与采用厂商原生输入、预后处理和运行时的完整部署优化，是两种不同的实验合同。

| 配置 | 改变哪一层 | 有效比较和风险 |
|---|---|---|
| Baseline | 标准转换、通用 host 处理 | 基线，不代表硬件上限 |
| VG-NPU | **保持 host I/O 和 pre/post 不变**，优化模型转换 | 较可控地归因 NPU-side 加速；不等于产品总时延 |
| VG-E2E | vendor-native I/O、pre/post、runtime、转换一起改变 | 测实际部署组合；不能把所有改善归因到 kernel |

作者测试 Hailo-8、Hailo-10H、DeepX DX-M1、Mobilint Regulus 四款 **edge NPU**，ResNet-50 / YOLOv5m / YOLOv8s-pose 三任务共 12 组。VG-NPU 在 10/12 组同时降低 runtime-call latency 并改善精度；VG-E2E 相比 VG-NPU 在全部 12 组降低 **system latency 10.4%–70.7%**，但只有 4/12 组相较 baseline 改善精度；设备排名可能改变。**这是原作者的 edge vision 测试，不是手机 SoC ISP 部署证据**。Regulus 的 host 不同，且没有统一功耗、热稳态、camera RAW/TM 或手机端 P95。

**历史竞争关系：**[Mobile AI 2026 Learned Smartphone ISP](../papers/arxiv-2611.05008.md) 报告在实际 Snapdragon/Dimensity GPU 的 RAW→RGB 任务；两者的**实验合同**互补，但模型、硬件和输入不同，不能直接形成快慢排名。HIVE-Diff 的 event+LDR 与 CoGenRec 的 CVS 改变的是物理观测，属于 T01 额外信息路线，不应与三层 edge-NPU 评测混为同一对照。

**判断更新：**过去“要看端到端实测而非 NFE/GFLOPs”仍成立；现在明确再拆两种真实部署结果：common-I/O 模型转换的能力与 vendor-native 整链的能力。两者需要一起报告画质/精度。不能将端侧执行器性能等同 sensor→display 成像流程的完整成本。

**系统回忆：**
- 在线：RAW 或图像数据 → 转换/数据搬运 → GPU/NPU 模型 → 色彩/影调后处理 → 输出；分层记录 runtime-call、system-level latency、峰值内存、最终画质及功耗/热。
- 离线：冻结设备/模型/数据与画质目标 → Baseline/VG-NPU/VG-E2E 三合同编译 → 端到端 profiling 和 P50/P95 → 质量–时延/能耗 Pareto；注意 CPU fallback。
- Agent 控制层：**无**，该研究不涉及 image agent 的动作选择。
- 行动：保留真实手机 GPU 的 Learned ISP 基线；在可用手机上对一条 RAW→RGB 子链做统一 I/O 与原生 E2E 的 matched 画质实验，不直接修改现有 ISP/TM 执行器。

**记忆锚点：**“NPU kernel 更快”不等于“完整拍照链更快”；系统加速可能伴随精度损失。

一手证据：[原文 §3–4](https://arxiv.org/html/2611.13563v1)。

## 方案回忆

移动 ISP：传感器 RAW/metadata → 色彩/曝光/恢复网络 → GPU LiteRT/runtime → RGB output → GT fidelity、MOS、真实 end-to-end latency、带宽和热功耗。

事件 HDR：LDR reference + event stream → 对齐/时间约束 → HDR N frame 生成 → Scale/absolute luminance、时序一致性、运动/饱和区真实性和完整延迟。

## 判断

即使网络 GFLOPs 很低，也必须实机测 GPU 端到端性能；即使 HDR 生成很逼真，单参考与事件物理信息不足时也不能断言真实细节恢复。HIVE-Diff 是 sensor-aware HDR video 的 **PROBE**，Mobile AI 报告是部署技术成熟度 **GO-E**；CoGenRec属于CVS专用物理新观测+生成恢复的 **GO-E（研究/硬件条件）**，不是手机部署确认。

## References

- [Edge NPU Benchmark v1](https://arxiv.org/html/2611.13563v1)
- [Mobile ISP 2026](https://arxiv.org/abs/2611.05008v1)
- [HIVE-Diff](https://arxiv.org/abs/2611.03465v1)
- [CoGenRec](https://arxiv.org/html/2611.07665v1)
- [既有 HDR data 入口](../HDR/HDR_Data_Taxonomy.md)
