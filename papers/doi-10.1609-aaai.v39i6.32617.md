# Enhancing Low-Light Images: A Synthetic Data Perspective on Practical and Generalizable Solutions

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)

- **ID**：`doi-10.1609-aaai.v39i6.32617`；**简称**：SynLLIE
- **作者**：Yu Long; Qinghua Lin; Zhihua Wang; Kai Zhang; Jianguo Zhang; Yuming Fang
- **发表**：AAAI 2025, 39(6):5784–5792；**本次读取版本**：AAAI 2025 official abstract；页面日期 2025-04-11
- **最早可核验公开日**：null（本轮未完成最早日期核对；不能以本次发现日期替代）
- **首次归档**：2026-10-23（历史回填，非新论文通知）；**checked_on**：2026-10-23
- **主题**：T05 数据与 Pseudo-GT；桥接 T01 / T03
- **verification_scope**：`official_abstract_checked`；独立复现：未执行
- **decision_key**：`explicit-isp-low-light-data-synllie`

## 快速回忆

**问题：**怎样用显式成像退化获得实用、可泛化的低光训练对？

**记住：**sRGB 反处理为近似 RAW，在其中合成低光、噪声等变化，再通过前向 ISP 渲染；用 tone curves/CCM 等拓展分布。这里仅记录官方摘要可支持的路线。

系统路线与横向比较见 [成像训练数据合成 survey](../surveys/imaging-training-data-synthesis.md)。

## 精读记录

**本轮证据位置：**官方摘要；PDF 本轮未成功取得。

官方论文身份和摘要已核验；具体训练配置、消融与数值仍待全文核验。

**前序与关系：**MESS 直接引用 [46]；是显式逆 ISP 与学习曝光生成的重要竞争路线。

## 证据边界

不能以摘要证明全面领先或确定每个参数的因果贡献；与 ISP-driven LLIE 存在明显作者和机制重叠，正式版本/扩展关系待查，不作独立证据重复计票。

作者结果不等于独立复现。作为训练数据方案时，至少在相同源场景、样本数、目标定义、下游模型和预算下比较，并用未参与生成/选优的真实相机测试检验收益。

## References

- [原论文](https://ojs.aaai.org/index.php/AAAI/article/view/32617)
- [官方补充入口](https://github.com/LongYu-LY/SynLLIE)
- [专题综述与覆盖记录](../surveys/imaging-training-data-synthesis.md)
