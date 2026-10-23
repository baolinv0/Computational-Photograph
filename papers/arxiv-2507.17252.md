# Unsupervised Exposure Correction

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)

- **ID**：`arxiv-2507.17252`；**简称**：UEC / RCD
- **作者**：Ruodai Cui; Li Niu; Guosheng Hu
- **发表**：ECCV 2024；**本次读取版本**：arXiv v1, 2025-07-23；ECCV 2024 先于预印本
- **最早可核验公开日**：null（本轮未完成最早日期核对；不能以本次发现日期替代）
- **首次归档**：2026-10-23（历史回填，非新论文通知）；**checked_on**：2026-10-23
- **主题**：T05 数据与 Pseudo-GT；桥接 T01 / T03
- **verification_scope**：`selected_sections_checked`；独立复现：未执行
- **decision_key**：`exposure-color-separation-uec-rcd`

## 快速回忆

**问题：**如何将曝光变换与修图风格分开，并减少人工校正标签依赖？

**记住：**模拟 ISP 构造曝光序列与 EV 监督来学习曝光变换；RCD 调整 Expert C 参考的曝光并固定其他后处理风格，覆盖 −2 至 +3 EV。

系统路线与横向比较见 [成像训练数据合成 survey](../surveys/imaging-training-data-synthesis.md)。

## 精读记录

**本轮证据位置：**§3、§4 RCD。

原文分别提供曝光校正方法和 RCD 数据。MESS 中 RCD 属于 RAW-Syn，UEC-based 属于 RGB-Syn，二者不能合并为同一数据源。

**前序与关系：**MESS 直接引用，作为曝光与颜色分离、RAW-Syn 与 RGB-Syn 的双重对照。

## 证据边界

方法无需手工校正标签训练不等于评测参考没有人工风格；曝光变换不等于任意局部重渲染或可靠补回缺失细节。2025 年 arXiv 上传不能当作首次提出。

作者结果不等于独立复现。作为训练数据方案时，至少在相同源场景、样本数、目标定义、下游模型和预算下比较，并用未参与生成/选优的真实相机测试检验收益。

## References

- [原论文](https://arxiv.org/abs/2507.17252)
- [官方补充入口](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/986_ECCV_2024_paper.php)
- [专题综述与覆盖记录](../surveys/imaging-training-data-synthesis.md)
