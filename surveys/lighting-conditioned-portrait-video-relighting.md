# 人物动态视频重照明：从直接生成到可控制明响应基

版本：v0.1｜2026-11-11｜主 T02，连接 T05/T01/X01
目录：[问题边界](#问题边界) · [竞争路线](#竞争路线) · [证据与判断](#证据与判断) · [系统方案](#系统方案) · [覆盖缺口](#覆盖缺口) · [References](#references)

## 问题边界
给定人的动态视频（尽量保持表情、衣服纹理和动作）与目标光场，输出在**方向和相对照明强度**上符合目标、跨帧稳定的重照明视频。并非单纯图像美化、白平衡偏色校正或 3D 捏脸；光照真实度不能只用好看的 MOS 检验。

记忆锚点：**「预测结果像不像在某种灯下」与「灯从哪个方向、亮度增减能否正确响应」是两个不同测量目标。**

## 竞争路线
| 路线 / 历史锚点 | 在线输入/控制变量 | 训练与监督 | 成立条件及失败边界 |
|---|---|---|---|
| 显式 inverse rendering / 3D avatar | 视频、多视角/几何、environment map、法线材质 | 3D 多视角/几何/光照分解，显式 render | 物理解释较强，身份/运动建模与真实采集成本高 |
| 直接条件生成（Lux Post Facto 2025、RelightVid/UniRelight 2025） | 原人像视频 + image/光环境条件，直接生成结果 | 视频生成先验、paired/synthetic relighting | 外观自然；照明方向、相对强度与 temporal consistency 可能有偏差 |
| 静态/半动态 OLAT 数据（HumanOLAT 2025） | OLAT 正射/多视角参考 | LightStage capture; 标注多方向照明 | 可作监督/定量评估，不等于即插即用的单视频泛化生成器 |
| **动态 OLAT 基预测 + 线性重组（[DynOLAT](../papers/arxiv-2611.11210.md)）** | flat-lit video + spherical harmonic lighting direction + environment map weights | 24M+ 光照实采帧、224 identity-outfit combinations；source video latent bridge 预测多方向 bases | 需稳定平光代理、生成多方向 bases 的时间/显存巨大；线性组合的可控性依赖基预测准确 |

**关系说明**：DynOLAT 引用上述工作作为问题前序/竞争系统；基于 source-anchored bridge 的设计与 [Paste2Place](../papers/arxiv-2611.09387.md) 属分析者识别的共同抽象，不能凭时间顺序称直接方法继承。人物视频照明的测量/数据与单帧 object insertion 不同，不复制同一 survey。

## 证据与判断
**本轮证据**：arXiv [2611.11210v1](https://arxiv.org/abs/2611.11210v1)，2026-11-08 公开，§5 Table 2/3/4。
- Channel-aligned capture benchmark：DynOLAT 26.23 PSNR / 0.0567 LPIPS vs DiffusionRenderer 23.11/0.0900；Temporal LPIPS 0.02532 vs 0.02629。
- 同预算训练的输入源处理消融，bridge full 27.61dB 略低于 frame concatenation 27.67，但 SSIM/LPIPS/FLIP 较优。**不能把数据量+桥接+方向 OLAT 组合的全部改善归因某个单一模块。**
- **反例**：作者利用通道尺度对齐，无法单凭 PSNR 证明绝对亮度/色准；H100/A100 设备消耗显著；真实有色多光源下 delight 残留/遮挡、基预测相互不一致未完全解决；无 30FPS 移动端。
- **判断（GO-E / New route + Engineering maturity）**：相较直接条件生成，把目标环境光拆为物理响应基提供了一个可检验的**控制接口**；尚非可靠端侧 pipeline。状态：原文作者单系统局部证据，不是社区共识。

## 系统方案
**在线**：source video → delight/flat-lit → predict + cache OLAT direction videos → combine in linear color using environment HDR weights → 输出重照明视频；对光方向、明暗单调性、彩色物体色差、身份和时序分别验收。预测所有 bases 前，online 不能承诺实时；缓存重组合成可加速重复光照编辑。
**离线**：101 单独方向光源和 synchronized cameras 的 LightStage → 交替 flat-lit/OLAT，光流配准 → paired supervision → 训练 video latent bridge (Wan family) → 垂直隔离 person/outfit/lighting scenes 做外部验证。评估应引入 true OLAT 或已知方向，并加同 backbone 直接 relighting、frame concatenation 等强 baseline。
**Agent 控制层**：非必要；如未来有编辑 Agent，可选光方向/强度、在真实光谱和身份错乱时回退，但论文并未验证此联合系统。

**目标/非目标**：可控光照方向及相对强度，不等于 RAW sensor color calibration、混合光谱 AWB、背景阴影精确传输。**未验证接口**：手机 sRGB/RAW 场景到 flat-lit 域；真实暗光保真；light-stage 数据到日常多手机拍摄；全链 latency、能源、模型压缩。
**决策**：保留为物理可控生成编辑的数据/机制对照；暂不替换局部 Tone Mapping 或参考确定性修图。最小判别：已知真实 OLAT 的同人物视频，等算力 compare direct video relighting 与 basis prediction/linear recombination，做 direction/intensity error + spatial fidelity。
## 覆盖缺口
HumanOLAT、Lux Post Facto、UniRelight、RelightVid、DiffusionRenderer、OLATverse 的独立全文/训练配置需核验；项目首次公开时间、真实环境 HDR 绝对亮度标定、肤色显色以及每基视频时序相位偏差均待验证。无需新增独立“修图 Agent”重复索引。
## References
- [DynOLAT v1](https://arxiv.org/abs/2611.11210v1)
- [项目与数据入口](https://zju3dv.github.io/DynOLAT/)
- [DynOLAT card](../papers/arxiv-2611.11210.md)
- [既有 object-scene relighting](object-scene-composition-and-relighting.md)
