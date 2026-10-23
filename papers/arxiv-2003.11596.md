# Learning Multi-Scale Photo Exposure Correction

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)

- **ID**：`arxiv-2003.11596`；**简称**：MSEC
- **作者**：Mahmoud Afifi; Konstantinos G. Derpanis; Björn Ommer; Michael S. Brown
- **发表**：CVPR 2021；**本次读取版本**：arXiv v3, 2021-03-30
- **最早可核验公开日**：2020-03-25
- **首次归档**：2026-10-23（历史回填，非新论文通知）；**checked_on**：2026-10-23
- **主题**：T05 数据与 Pseudo-GT；桥接 T01 / T03
- **verification_scope**：`selected_sections_checked`；独立复现：未执行
- **decision_key**：`raw-exposure-rendering-expert-retouch-target`

## 快速回忆

**问题：**如何为欠曝和过曝校正建立大规模可控输入与高质量目标？

**记住：**将 FiveK RAW 通过 Adobe Camera Raw SDK 渲染为 −1.5、−1、0、+1、+1.5 EV 输入，目标取 Expert C 修图。多尺度网络学习曝光校正。

系统路线与横向比较见 [成像训练数据合成 survey](../surveys/imaging-training-data-synthesis.md)。

## 精读记录

**本轮证据位置：**§3 Dataset。

原文记录 24,330 个 sRGB 输入，并处理 RAW crop metadata 引起的配对错位。

**前序与关系：**MESS 直接引用并用作 RAW-Syn 对照。应同时记录输入侧的曝光控制与目标侧的审美定义。

## 证据边界

目标是人工修图结果，不是 0 EV 或物理辐射真值；RAW 来源与人工目标的规模限制仍存在。

作者结果不等于独立复现。作为训练数据方案时，至少在相同源场景、样本数、目标定义、下游模型和预算下比较，并用未参与生成/选优的真实相机测试检验收益。

## References

- [原论文](https://arxiv.org/abs/2003.11596)
- [官方补充入口](https://openaccess.thecvf.com/content/CVPR2021/html/Afifi_Learning_Multi-Scale_Photo_Exposure_Correction_CVPR_2021_paper.html)
- [专题综述与覆盖记录](../surveys/imaging-training-data-synthesis.md)
