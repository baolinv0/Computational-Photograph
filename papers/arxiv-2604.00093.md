# RawGen: Learning Camera Raw Image Generation

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)

- **ID**：`arxiv-2604.00093`；**简称**：RawGen
- **作者**：Dongyoung Kim; Junyong Lee; Abhijith Punnappurath; Mahmoud Afifi; Sangmin Han; Alex Levinshtein; Michael S. Brown
- **发表**：ECCV 2026（作者项目页标注）；**本次读取版本**：arXiv v1
- **最早可核验公开日**：2026-03-31
- **首次归档**：2026-10-23（历史回填，非新论文通知）；**checked_on**：2026-10-23
- **主题**：T05 数据与 Pseudo-GT；桥接 T01 / T03
- **verification_scope**：`selected_sections_and_author_project_checked`；独立复现：未执行
- **decision_key**：`canonical-xyz-many-to-one-camera-raw-generation`

## 快速回忆

**问题：**如何借助海量 RGB 生成先验，获得可跨相机适配的线性训练数据？

**记住：**同一真实 RAW 经多种 WB、tone、contrast 设置生成多个 sRGB rendition，共用一个规范化 XYZ anchor；微调 FLUX.1-Kontext 的 LoRA denoiser 与 VAE decoder。推理时从 sRGB 条件或文本生成的 sRGB latent 预测 XYZ，再用目标相机 DNG 标定矩阵与选定光源进行确定性 RAW 映射；噪声和 CFA 重采样为可选后处理。

系统路线与横向比较见 [成像训练数据合成 survey](../surveys/imaging-training-data-synthesis.md)。

## 精读记录

**本轮证据位置：**§3.1–3.4、Fig.2、§4.2–4.4、§5。

作者比较专家修图风格变化下的 XYZ 重建，并验证照明估计、neural ISP、RAW 去噪的数据增强。§4.2 的其他 baseline 以默认 ISP 的 one-to-one 数据训练；其结果不能单独证明架构优于全部同条件 many-to-one 方案。

**前序与关系：**原文引用 UPI、CIE XYZ Net、InvISP、RAW-Diffusion；与 MESS 的关系由本综述建立，为并行/互补，不是已核实的直接继承。

## 证据边界

规范化线性生成结果不是该场景唯一真实传感器观测。相机映射要求标定信息；简单噪声模型不能代表所有传感器、光学和 ISP 特性。任意相机适配不等于无需相机信息。

作者结果不等于独立复现。作为训练数据方案时，至少在相同源场景、样本数、目标定义、下游模型和预算下比较，并用未参与生成/选优的真实相机测试检验收益。

## References

- [原论文](https://arxiv.org/abs/2604.00093v1)
- [官方补充入口](https://dy112.github.io/rawgen-page/)
- [专题综述与覆盖记录](../surveys/imaging-training-data-synthesis.md)
