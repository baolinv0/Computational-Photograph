# 显示与观看条件下的画质：从测量空间到观看者可见失真
版本 v0.1｜2026-11-18｜主 T04；连接 T02、X01、Display
目录：[长期问题](#长期问题) · [竞争路线](#竞争路线) · [2026实质扩展](#2026实质扩展) · [完整方案](#完整方案) · [判断与缺口](#判断与缺口) · [References](#references)

## 长期问题
同样的像素/压缩码流，在不同的亮度、显示器、观看距离和环境光下会产生不同的可感知失真；固定 SDR pixel-domain PSNR/LPIPS 不必预测该变化。**物理保真不随观察环境改变，失真可见度会改变**。

## 竞争路线
| 路线 | 输入/观测条件 | 评价机制 | 成立与失败条件 |
|---|---|---|---|
| 传统 FR-IQA/VQA PSNR/SSIM/LPIPS | 参考与失真视频 | 像素或 learned features 对比 | 未编码观看条件 |
| 视距感知 CSF/HDR-VDP / ColorVideoVDP | HDR 亮度与观看几何 | CSF/视觉阈值 | 标定、视距和亮度信任度；不同失真类型 |
| HDR 编码 + 可视距离的经验模型 (Hammou et al. MMSP 2023; QoMEX 2024) | HDR 视频、压缩伪影、不同观看条件 | 主观排序、CSF / PPS | 2024 已发布 HDR-VDC 与两距离/亮度人评 |
| **2026 Journal Extension** (arxiv 2611.20226) | 同一 HDR-VDC 数据，35 个 VQA/IQA | 显示 model → PU21 → PPS 适配，跨条件分离分析 | 两距离/亮度，一种 OLED、AV1 和 Lanczos；仅流媒体伪影 |
| 真实手机画质感知（待补） | 手持距离/环境亮度/周边光 | 多条件主观测试 | 不能由大屏暗室结果直接外推手机 |

## 2026实质扩展
[论文卡](../papers/arxiv-2611.20226.md)｜**Update**：2024 年已由 [QoMEX 2024](https://ieeexplore.ieee.org/document/10598289) 公开同一数据集/主结果，2026-11-15 arXiv v1 新增 35 metrics、显示模型适配/统计分析与 failures。**新在评价机制横向验证，不在新建数据集。**
- 12 4K + 4 FHD 源，AV1+Lanczos，共 132 distortion videos；视距 1.1m/2.2m=60/120ppd，内容均值 51/5.6 cd/m²；两 LG OLED 与暗室条件。
- 统一指标适配链：已标定 display response → photometric domain/PU21 → perspective projection scaling (PPS) → FR-VQA score；一些 VMAF/HaarPSI/ColorVideoVDP 表现好，PSNR/SSIM/LPIPS 在该 4K HDR 失真任务差。
- 作者报告视距变化为中等 effect size eta²=0.101，亮度更小 eta²=0.015；不能把 8× 平均亮度缩小误读成 peak HDR capability 8×降低（峰值 700/600cd/m²）。
- 与作者 2024 QoMEX 的关联属于**作者明确自述的扩展**；与其他显示感知评价路线是竞争/互补，不把年份排序当直接继承。

## 完整方案
**离线：** 标定真实显示 photometry + 观看距离 → 多内容多码率/尺寸 → 主观配对 JOD → 对比物理观看条件模型与感知映射指标 → 跨设备与明亮环境验证。
**在线：** 参考视频 + 压缩/重采样输出 + display setting/估计视距 → 显示 model + PU21 + PPS 或原生 CSF-VQA → 输出条件相关质量分 → （可选）编码码率/分辨率选择。这是设计接口，不是论文已经验证的真实移动产品。
**Agent：** 一般情况下无关，不因属于 IQA 自动添加 Agent Judge。

## 判断与缺口
旧判断：固定观看条件指标可用于 HDR 压缩质量比较。新研究支持**指标必须对部署观看条件校准**，但原 2024 论文已证明部分现象，2026 提供横向可适配性证据。**GO-E（2026 material update）**。
最强未证实接口：用户实际视距测量、环境光、移动端动态高光、肤色/全局 Tone Mapping 失真非作者测试范围。当前 ISP/TM 方案无需改动。
记忆锚点：**物理上的压缩误差不变，距离与亮度改变的是观察者能看见多少。**

## References
- [2026 扩展全文](https://arxiv.org/abs/2611.20226v1)
- [2024 QoMEX 原始工作](https://ieeexplore.ieee.org/document/10598289)
- [HDR-VDC 项目/数据](https://www.cl.cam.ac.uk/research/rainbow/projects/hdr-vdc/)
- [HDR-VDC 代码](https://github.com/gfxdisp/HDR-VDC)
