# ParamISP: Learned Forward and Inverse ISPs using Camera Parameters

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)

- **ID**：`arxiv-2312.13313`；**简称**：ParamISP
- **作者**：Woohyeok Kim; Geonu Kim; Junyong Lee; Seungyong Lee; Seung-Hwan Baek; Sunghyun Cho
- **发表**：CVPR 2024；**本次读取版本**：arXiv v2, 2024-04-15
- **最早可核验公开日**：2023-12-20
- **首次归档**：2026-10-23（历史回填，非新论文通知）；**checked_on**：2026-10-23
- **主题**：T05 数据与 Pseudo-GT；桥接 T01 / T03
- **verification_scope**：`selected_sections_checked`；独立复现：未执行
- **decision_key**：`camera-parameter-conditioned-forward-inverse-isp`

## 快速回忆

**问题：**同一相机在不同曝光、ISO 等参数下的 ISP 变化怎样进入模型？

**记住：**CanoNet 完成标准 Bayer/WB/CCM 操作，LocalNet/GlobalNet 学习局部处理与全局 tone/color；ParamNet 编码曝光时间、ISO、光圈、焦距来调制映射。采用 paired RAW/sRGB 重建监督，多相机预训练后目标相机微调。

系统路线与横向比较见 [成像训练数据合成 survey](../surveys/imaging-training-data-synthesis.md)。

## 精读记录

**本轮证据位置：**§3.1–3.3、§4。

原文研究 forward/inverse ISP 以及数据生成、RAW 去模糊、HDR、camera-to-camera transfer 等应用。

**前序与关系：**MESS §2 直接引用 [31]；在 survey 中保留为显式参数控制接口，未被学习型 RGB 曝光生成普遍替代。

## 证据边界

不是 metadata-free 的未知 JPEG 通用逆 ISP；参数条件与目标相机适配是成立条件。

作者结果不等于独立复现。作为训练数据方案时，至少在相同源场景、样本数、目标定义、下游模型和预算下比较，并用未参与生成/选优的真实相机测试检验收益。

## References

- [原论文](https://arxiv.org/abs/2312.13313)
- [官方补充入口](https://openaccess.thecvf.com/content/CVPR2024/html/Kim_ParamISP_Learned_Forward_and_Inverse_ISPs_using_Camera_Parameters_CVPR_2024_paper.html)
- [专题综述与覆盖记录](../surveys/imaging-training-data-synthesis.md)
