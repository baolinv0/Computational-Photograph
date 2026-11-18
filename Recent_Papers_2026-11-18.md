# Paper Watch v3.2｜2026-11-18：成像采集目标、生成参考、训练损失、手机DiT与观看条件

**正式裁决：4 New + 1 Material Update。** 11 月 17 日官方 arXiv 新公告较前次已成功覆盖的 11 月 16 日 /new 有新公开；全部 T01–T06/X01 及10位核心研究者近期索引与开放机制检索完成。此处的“新”以可核验原文最早公开为准，不把本次首次归档当首发。**2026 HDR-VDC 论文经原文 Related Work 发现自述扩展 2024 QoMEX HDR-VDC dataset**，已从候选“新”纠为 material_update。OpenReview/提前完整公开未穷尽。

目录：[新增与Update](#新增与update) · [T01T05数据与目标](#t01t05数据与目标) · [T03可信生成与训练](#t03可信生成与训练) · [X01部署](#x01部署) · [T04观看条件](#t04观看条件) · [核验与待办](#核验与待办)

## 新增与Update

| ID/首次公开可核验 | 论文/作者或团队 | 主/次主题，系统角色 | 地图变化/裁决 |
|---|---|---|---|
| 2611.19284, 2026-11-14 arXiv v1 | [LC-ISP](papers/arxiv-2611.19284.md), Kai Chen 等 | T01 / T05、X01；采集/目标/训练 | New route + Engineering maturity / GO-E |
| 2611.19285, 2026-11-14 arXiv v1 | [MrLIE](papers/arxiv-2611.19285.md), 低光生成式增强 | T03 / T06、T05；参考生成/执行/策略 | Bridge + Boundary refinement / PROBE |
| 2611.20805, 2026-11-16 arXiv v1 | [Improved Fréchet Loss FDIR](papers/arxiv-2611.20805.md) | T03 / T04、X01；训练/执行 | New route + Boundary refinement / GO-E |
| 2611.19261, 2026-11-14 arXiv v1 | [dit.xpu](papers/arxiv-2611.19261.md), PKU 等 | X01 / T03、T06；部署 | Engineering maturity / GO-E |
| 2611.20226, **2024-06 QoMEX conference origin → 2026-11-15 expanded v1** | [HDR-VDC观看条件评价](papers/arxiv-2611.20226.md), Cambridge/Netflix | T04 / T02、X01；评价/基准 | **Material Update**, Supporting evidence + Engineering maturity / GO-E |

## T01T05数据与目标
**旧：** DPED/ZRR 不同设备高质量参考、SID 曝光成对测量、逆 ISP / MESS / RawGen 模拟数据。**新：** LC-ISP 使用同 iPhone 16 Pro live 单帧 RAW/sRGB 与 capture burst/fused photograph sRGB 形成中间及最终监督；1000 实拍场景、53,892 cropped patches；Lite 约 2.5 GFLOPs 的作者 PSNR 对照，同方法去中间监督 22.78→完整 23.36 dB。比较的目标构成可能带来主要增益，**capture 输出是设备 ISP 生成的高质目标，不是场景辐射 GT**。

离线 same-device 采集/配准→恢复监督+渲染监督→轻量模型训练；在线单帧 RAW→恢复→渲染 RGB。Agent 控制无必要。判断：把数据/目标定义前置，但不更换既有 AE–TM 目标。见 [既有 T05 survey 增补](surveys/imaging-training-data-synthesis.md)。

## T03可信生成与训练
**旧：** 无监督/零参考 LLIE（Zero-DCE/EnlightenGAN）、源观测锚点扩散（AnlightenDiff）、真实 NIR 观测的外部参考（UGD-FM）；一步恢复训练来自 teacher distillation（OSEDiff）或 adversarial（HYPIR）。

**MrLIE / PROBE：** MLLM 先自生成正曝光参考、迭代 critic，再用 COM 的偏移+置信度与 SAI 源结构注入约束 diffusion。作者 U3D 的 NIQE/BRISQUE 等感知指标改善，**生成的参考不能提供额外真实测量**；不应把主观偏好等同细节真实性。离线学习低光/亮图域与条件生成；在线 LQ→多轮 MLLM 提案→置信匹配→source-anchored diffusion→候选与事实验收。Agent/critic 是目标假设层而非 radiometric GT。新增 [generated-reference-guided-low-light-restoration](surveys/generated-reference-guided-low-light-restoration.md)。

**FDIR / GO-E：** 用冻结图像及 patch-level features 的 Fréchet 分布匹配+EMA 统计训练一步恢复器，替代部分教师轨迹或 GAN 判别器损失。Representation Fréchet Loss 是直接机制前序；FDIR 是训练工程适配，不是首创 FD。作者相近成本的 MUSIQ 对照较强，但 DIV2K-Val PSNR 低于 OSEDiff/RealESR，故未证实更真实。**离线训练目标改变，在线仍是一 NFE 恢复，不能将训练开销与手机 E2E 混同。**见 [高效生成式恢复 survey](surveys/efficient-generative-restoration.md)。

## X01部署
**dit.xpu / GO-E：** 手机 DiT 稀疏 attention 通过 tile/static mask、dense anchors 与 NPU/GPU 异构/共享 buffer/异步 KV 适配不规则稀疏；两 Snapdragon 手机上五类 DiT，作者最高 kernel 11.5×，**denoising E2E 最多 1.56×**（不同基线）。并未测相机 RAW/ISP 全链、长时热、持续功耗、整张图后处理。旧端侧研究已揭示 common-I/O NPU 与 vendor-native E2E 差异；本研究推进具体部署机制，不改变传统 ISP 方案。见 [移动端部署 survey](surveys/mobile-isp-and-event-hdr-efficiency.md)。

## T04观看条件
**2024→2026 Update 而非新论文**：2024 QoMEX [HDR-VDC原作](https://ieeexplore.ieee.org/document/10598289) 已公开 HDR AV1 编码与超分、两观看距离/两亮度的人评；2026 arXiv 扩展论文系统对比 **35 IQA/VQA指标**，用 display response + PU21 + PPS 适配，拆分观看条件贡献。12个4K+4个FHD源，60/120ppd，平均亮度51/5.6cd/m²；该设置不代表手机户外或全局 TM 失真。作者的 35指标分析显示一些 VMAF / HaarPSI/ColorVideoVDP 可适配，PSNR/SSIM/LPIPS 表现较差。新判断：**对观测者的可见失真评价必须以显示与观看条件为条件变量**；旧事实“更远/更暗伪影较少可见”在 2024 已有证据，新扩展主要改善 metric 选择与适用范围。见 [显示观看条件 survey](surveys/display-viewing-conditioned-visual-quality.md)。

## 核验与待办
- 官方 arXiv 六分类（cs.CV/LG/AI/MM,eess.IV/SP）2026-11-17 新公告；前次 2026-11-16 已成功覆盖；候选按 7–14 日重叠去重。作者索引 10 位 alphaXiv [Brown, PolyU Lei Zhang, Timofte, Tianfan Xue, Afifi, Zuo, Zhilu Zhang, Kai Zhang, Sida Peng, Xiaowei Zhou] 核对 11-09 以来，未得到另外合格同时间窗的新增。
- 论文证据：arXiv v1 正文选定方法/表格/限制，HDR-VDC 原论文 2024 QoMEX 官方页面；均不是独立复现。OpenReview、作者提前公开、当前未验证其它最新作者索引未穷尽。
- 归档：单篇 canonical cards、旧 T05/T03/X01 surveys、两份新长期专题、LITERATURE_MAP、索引、registry，alphaXiv 先查重收藏再读回。状态以真实结果为准。
- 待补：LC-ISP 真正场景 GT 和动态对齐；MrLIE 虚构纹理的独立 GT/非生成参考对照；FDIR 损失/target/预算控制；dit.xpu 手机电功耗/温升；HDR-VDC 明亮环境与小显示屏迁移；其它源并无完整“无新增”保证。
