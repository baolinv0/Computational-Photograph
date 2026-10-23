# Unprocessing Images for Learned Raw Denoising

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)

- **ID**：`arxiv-1811.11127`；**简称**：Unprocessing / UPI
- **作者**：Tim Brooks; Ben Mildenhall; Tianfan Xue; Jiawen Chen; Dillon Sharlet; Jonathan T. Barron
- **发表**：CVPR 2019；**本次读取版本**：CVPR 2019 author PDF
- **最早可核验公开日**：null（本轮未完成最早日期核对；不能以本次发现日期替代）
- **首次归档**：2026-10-23（历史回填，非新论文通知）；**checked_on**：2026-10-23
- **主题**：T05 数据与 Pseudo-GT；桥接 T01 / T03
- **verification_scope**：`selected_sections_checked`；独立复现：未执行
- **decision_key**：`analytic-unprocessing-synthetic-raw-denoising`

## 快速回忆

**问题：**缺少足量真实 RAW 配对时，怎样从普通照片构造 RAW 去噪监督？

**记住：**近似反转 tone mapping、gamma、颜色矩阵、白平衡和增益，获得合成干净 RAW；加入 shot/read noise 构造带噪输入。训练时可将前向 ISP 纳入损失计算。

系统路线与横向比较见 [成像训练数据合成 survey](../surveys/imaging-training-data-synthesis.md)。

## 精读记录

**本轮证据位置：**Fig.2、§3.5–3.7、§4.1–4.4。

原文在 RAW 去噪任务中研究处理/反处理和噪声合成的效果；它是显式近似逆 ISP 的基础对照。

**前序与关系：**MESS 与 RawGen 均引用；属于显式合成基础，不是学习型生成器。

## 证据边界

简化的 ISP 与 smoothstep tone curve 不代表所有未知照片处理管线；合成 RAW 不应当作从 JPEG 精确找回的真实 RAW。

作者结果不等于独立复现。作为训练数据方案时，至少在相同源场景、样本数、目标定义、下游模型和预算下比较，并用未参与生成/选优的真实相机测试检验收益。

## References

- [原论文](https://people.csail.mit.edu/tfxue/papers/cvpr2019_unprocess.pdf)
- [官方补充入口](https://arxiv.org/abs/1811.11127)
- [专题综述与覆盖记录](../surveys/imaging-training-data-synthesis.md)
