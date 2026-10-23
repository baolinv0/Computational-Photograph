# CIE XYZ Net: Unprocessing Images for Low-Level Computer Vision Tasks

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)

- **ID**：`arxiv-2006.12709`；**简称**：CIE XYZ Net
- **作者**：Mahmoud Afifi; Abdelrahman Abdelhamed; Abdullah Abuolaim; Abhijith Punnappurath; Michael S. Brown
- **发表**：IEEE TPAMI（online 2021；44(9), 2022）；**本次读取版本**：arXiv v1 method; journal metadata separately checked
- **最早可核验公开日**：null（本轮未完成最早日期核对；不能以本次发现日期替代）
- **首次归档**：2026-10-23（历史回填，非新论文通知）；**checked_on**：2026-10-23
- **主题**：T05 数据与 Pseudo-GT；桥接 T01 / T03
- **verification_scope**：`selected_sections_checked`；独立复现：未执行
- **decision_key**：`device-independent-xyz-learned-unprocessing`

## 快速回忆

**问题：**低层处理如何借助设备无关的线性域，而不为每台相机建立一个孤立 RAW 表示？

**记住：**学习 sRGB 与 XYZ 之间的映射，将全局颜色变换与局部残差分开；在 XYZ 中实施低层处理再映射回显示域。配对监督来自 FiveK RAW 经软件管线渲染。

系统路线与横向比较见 [成像训练数据合成 survey](../surveys/imaging-training-data-synthesis.md)。

## 精读记录

**本轮证据位置：**§III-B、III-E、IV-A、Fig.4。

论文展示线性中间表示对低层视觉处理的用途；该表示选择是理解 RawGen 的重要前序。

**前序与关系：**RawGen 显式引用并在 XYZ 重建中比较；与 MESS 的关系是本综述的生成表示对照。

## 证据边界

训练管线覆盖范围和重渲染风格决定适用边界；不代表可以无条件消除任意未知 photo-finishing。

作者结果不等于独立复现。作为训练数据方案时，至少在相同源场景、样本数、目标定义、下游模型和预算下比较，并用未参与生成/选优的真实相机测试检验收益。

## References

- [原论文](https://arxiv.org/abs/2006.12709)
- [官方补充入口](https://github.com/mahmoudnafifi/CIE_XYZ_NET)
- [专题综述与覆盖记录](../surveys/imaging-training-data-synthesis.md)
