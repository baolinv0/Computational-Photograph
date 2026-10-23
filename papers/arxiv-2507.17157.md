# UNICE: Training A Universal Image Contrast Enhancer

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)

- **ID**：`arxiv-2507.17157`；**简称**：UNICE
- **作者**：Ruodai Cui; Lei Zhang
- **发表**：arXiv preprint 2025（本轮未核实正式接收）；**本次读取版本**：arXiv v1
- **最早可核验公开日**：2025-07-23
- **首次归档**：2026-10-23（历史回填，非新论文通知）；**checked_on**：2026-10-23
- **主题**：T05 数据与 Pseudo-GT；桥接 T01 / T03
- **verification_scope**：`selected_sections_checked`；独立复现：未执行
- **decision_key**：`raw-mes-mef-pseudotarget-two-stage-enhancement`

## 快速回忆

**问题：**怎样用自动构造的多曝光监督统一多种照明和对比度增强？

**记住：**真实 RAW 经模拟 ISP 得到 −3…+3 EV 序列，用多种 MEF、加权组合和 NR-IQA 选优产生 pseudo-GT；训练 MES-Net 和 MEF-Net，推理时依次生成曝光序列与融合增强结果。

系统路线与横向比较见 [成像训练数据合成 survey](../surveys/imaging-training-data-synthesis.md)。

## 精读记录

**本轮证据位置：**§3.1–3.3。

作者建立自动 RAW/MEF 监督并验证多类增强。原始 RAW 收集量、过滤后 RAW 数与派生训练对是不同计量单位。

**前序与关系：**MESS 直接引用且作者有重叠，是解释 RAW-derived MES 的关键前序；区别在生成器系统位置和最终目标来源。

## 证据边界

融合选优目标依赖 MEF 和 IQA 偏好，不是测量的真实 GT；两阶段推理成本不能与只部署轻量学生的 MESS 混同。

作者结果不等于独立复现。作为训练数据方案时，至少在相同源场景、样本数、目标定义、下游模型和预算下比较，并用未参与生成/选优的真实相机测试检验收益。

## References

- [原论文](https://arxiv.org/abs/2507.17157v1)
- [官方补充入口](https://github.com/BeyondHeaven/UNICE)
- [专题综述与覆盖记录](../surveys/imaging-training-data-synthesis.md)
