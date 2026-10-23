# Invertible Image Signal Processing

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)

- **ID**：`arxiv-2103.15061`；**简称**：InvISP
- **作者**：Yazhou Xing; Zian Qian; Qifeng Chen
- **发表**：CVPR 2021；**本次读取版本**：arXiv v2, 2021-04-06
- **最早可核验公开日**：null（本轮未完成最早日期核对；不能以本次发现日期替代）
- **首次归档**：2026-10-23（历史回填，非新论文通知）；**checked_on**：2026-10-23
- **主题**：T05 数据与 Pseudo-GT；桥接 T01 / T03
- **verification_scope**：`selected_sections_checked`；独立复现：未执行
- **decision_key**：`joint-forward-inverse-invertible-isp`

## 快速回忆

**问题：**能否共同设计前向 ISP 和逆向恢复，使输出 RGB 保留更多可逆信息？

**记住：**采用可逆网络共同构造 RAW→RGB 与 RGB→RAW，训练时加入可微 JPEG 模拟。

系统路线与横向比较见 [成像训练数据合成 survey](../surveys/imaging-training-data-synthesis.md)。

## 精读记录

**本轮证据位置：**§1、§3、§4.1–4.2、Fig.1。

原文验证在所设计前向成像/编码条件下的 RAW 重建；适合解释可控管线中的可逆性。

**前序与关系：**MESS 与 RawGen 都引用；在本综述中单列为前向管线可控的条件分支。

## 证据边界

前向 ISP 也由该方法设计，这是核心成立条件；不能把重建效果外推为任意互联网 JPEG 的真实 RAW 逆恢复。

作者结果不等于独立复现。作为训练数据方案时，至少在相同源场景、样本数、目标定义、下游模型和预算下比较，并用未参与生成/选优的真实相机测试检验收益。

## References

- [原论文](https://arxiv.org/abs/2103.15061)
- [官方补充入口](https://arxiv.org/html/2103.15061v2)
- [专题综述与覆盖记录](../surveys/imaging-training-data-synthesis.md)
