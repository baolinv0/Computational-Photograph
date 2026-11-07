# CoGenRec: A Unified Generative Framework for Complementary Vision Reconstruction

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据与争议](#证据与争议) · [行动与方案](#行动与方案) · [References](#references)

- ID: arxiv-2611.07665；首次可核验公开：**2026-11-05**（arXiv v1）；source_version: **v1**；first_covered: **2026-11-07**；checked_on: **2026-11-07**。
- 作者/团队：Yapeng Meng, Yuguo Chen, Xiangru Chen et al.; 清华大学/厦门大学等。
- 主主题：**T01**；次主题：T03 / X01；系统角色：采集、数据、执行；地图变化：Bridge / Engineering maturity。
- Verdict：**GO-E**（研究价值/工程适用性分开）；核验范围：arXiv v1 HTML 方法与选定实验、未独立复现；尚未做全站更早公开检索。

## 快速回忆
**去术语命题**：用长曝光稠密RGB与短曝光高时间分辨率差分测量，把运动去模糊、插帧和HDR重建建成有物理观测约束的统一生成问题。

**与前序关系**：既有 CVS / Tianmouc 路线及 Tianmouc-UNet、IGFNet、CBRDM、STGDNet 是已知直接竞争的特定观测基线；HIVE-Diff 1 LDR+events 是同抽象机制但传感输入不同，非直接方法继承。

## 精读记录
**输入→输出**：CVS 的稠密低帧率长曝光 RGB endpoint + 稀疏高时率 short-exposure spatiotemporal difference (Mid-SD) → 中间时刻的RGB视频帧/去模糊及HDR融合结果。不是单张LDR无条件推断真实饱和内容。

**离线**：硬件DLP转换、噪声感知仿真和曝光增强约一百万CVS clips；分三阶段训练多尺度时空指导提取器、视频扩散与观测引导的细节VAE。**在线**：双观测→曝光感知特征与双向时序传播→ControlNet约束video diffusion→细节注入VAE→序列RGB。

**作者证据**：SportsSloMo-CVS 相对各任务最强一般基线 PSNR +4.40 dB 去模糊、+3.89 dB 插帧、+5.04 dB HDR（Abstract、IV-C）。IV-E 表V中仅确定性 extractor 的 SportsSloMo PSNR 30.56dB (无曝光增强)；引入diffusion提升感知指标却一度降低PSNR；VAE观测补偿恢复像素指标。作者同时提供129实机场景定性对照、1515/3030 fps差分流示例。

**最强替代解释与反证**：额外真实CVS传感测量、训练池规模、曝光增强及任务条件不同共同影响收益；并不是单纯“扩散替代传统RAW恢复”带来数字。NR指标变好不证明幻觉处保真。缺相机功耗、完全端到端实时ISP、跨硬件/光谱泛化；暂不能移植普通手机单RGB/RAW。

## 证据与争议
证据均来自作者报告，不能称独立重复验证；比较同输入、同监督/预算、同执行器后的实际收益才足以归因到该模块。跨设备/跨相机与真实部署尚需针对性验证。见上段具体反例。

## 行动与方案
保留作为多模态实际采集-重建路线，当前单路手机TM不采用。判别：相同真实CVS测量和训练配额下拆掉扩散、细节VAE、曝光增强逐项比较结构保真和延迟。

**记忆锚点**：用长曝光稠密RGB与短曝光高时间分辨率差分测量，把运动去模糊、插帧和HDR重建建成有物理观测约束的统一生成问题。

## References
- https://arxiv.org/html/2611.07665v1
- https://arxiv.org/abs/2611.03465 (HIVE-Diff; 异种传感路线，历史锚点)
