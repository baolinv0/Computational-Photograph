# CycleISP: Real Image Restoration via Improved Data Synthesis

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)

- **ID**：`arxiv-2003.07761`；**简称**：CycleISP
- **作者**：Syed Waqas Zamir; Aditya Arora; Salman Khan; Munawar Hayat; Fahad Shahbaz Khan; Ming-Hsuan Yang; Ling Shao
- **发表**：CVPR 2020；**本次读取版本**：arXiv v1
- **最早可核验公开日**：2020-03-17
- **首次归档**：2026-10-23（历史回填，非新论文通知）；**checked_on**：2026-10-23
- **主题**：T05 数据与 Pseudo-GT；桥接 T01 / T03
- **verification_scope**：`selected_sections_checked`；独立复现：未执行
- **decision_key**：`learned-isp-cycle-noise-data-synthesis`

## 快速回忆

**问题：**怎样从现成照片构造贴近相机处理的 RAW/sRGB 去噪数据？

**记住：**成对 RAW–RGB 训练 RGB2RAW 与 RAW2RGB，先分别训练再联合微调；前向渲染的颜色分支利用模糊后的原 sRGB。合成时在伪 RAW 加入 shot/read noise，再前向传播得到带噪 sRGB；可用真实 RAW noise residual 微调噪声传播。

系统路线与横向比较见 [成像训练数据合成 survey](../surveys/imaging-training-data-synthesis.md)。

## 精读记录

**本轮证据位置：**§3.1–3.4、Fig.2、§4。

论文核心验证是噪声合成和 RAW/sRGB 去噪；不是通用曝光或饱和信息重建。

**前序与关系：**MESS §2 直接引用 [77]，为学习 ISP 后在 RAW 域造退化的前序。

## 证据边界

循环一致性不保证不可逆丢失信息有唯一正确逆解；颜色条件和训练相机分布仍影响生成数据。

作者结果不等于独立复现。作为训练数据方案时，至少在相同源场景、样本数、目标定义、下游模型和预算下比较，并用未参与生成/选优的真实相机测试检验收益。

## References

- [原论文](https://arxiv.org/abs/2003.07761v1)
- [官方补充入口](https://openaccess.thecvf.com/content_CVPR_2020/html/Zamir_CycleISP_Real_Image_Restoration_via_Improved_Data_Synthesis_CVPR_2020_paper.html)
- [专题综述与覆盖记录](../surveys/imaging-training-data-synthesis.md)
