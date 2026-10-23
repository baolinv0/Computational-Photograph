# Towards Realistic Low-Light Image Enhancement via ISP Driven Data Modeling

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)

- **ID**：`arxiv-2504.12204`；**简称**：ISP-driven LLIE
- **作者**：Zhihua Wang; Yu Long; Qinghua Lin; Kai Zhang; Yazhu Zhang; Yuming Fang; Li Liu; Xiaochun Cao
- **发表**：arXiv preprint 2025；**本次读取版本**：arXiv v1
- **最早可核验公开日**：2025-04-16
- **首次归档**：2026-10-23（历史回填，非新论文通知）；**checked_on**：2026-10-23
- **主题**：T05 数据与 Pseudo-GT；桥接 T01 / T03
- **verification_scope**：`selected_sections_checked`；独立复现：未执行
- **decision_key**：`explicit-isp-noise-wb-exposure-data-modeling`

## 快速回忆

**问题：**缺少网络照片相机元数据时，怎样构造覆盖真实低光的退化输入？

**记住：**高质 RGB unprocessing 后线性曝光缩放、RAW shot/read 噪声近似、demosaic，再随机 WB、CCM、tone mapping、gamma；不依赖原网络照片的设备 metadata。

系统路线与横向比较见 [成像训练数据合成 survey](../surveys/imaging-training-data-synthesis.md)。

## 精读记录

**本轮证据位置：**§3.1–3.6。

作者用普通 U-Net 和已有模型研究训练数据贡献；本卡不继承未经本轮核对的性能数值。

**前序与关系：**MESS 直接引用 [69]；显式采样变量与 MESS 学到的曝光变化应作同源、同规模对照。

## 证据边界

退化模型和采样覆盖决定真实性，不自动恢复原始相机状态；与 SynLLIE 的正式身份关系待核实，不能算两份独立方向证据。

作者结果不等于独立复现。作为训练数据方案时，至少在相同源场景、样本数、目标定义、下游模型和预算下比较，并用未参与生成/选优的真实相机测试检验收益。

## References

- [原论文](https://arxiv.org/abs/2504.12204v1)
- [官方补充入口](https://github.com/SMBU-MM/LLIE)
- [专题综述与覆盖记录](../surveys/imaging-training-data-synthesis.md)
