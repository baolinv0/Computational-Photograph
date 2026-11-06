# ILLRAW: Illumination-Aware Learning for Object Detection in RAW Images

## 快速回忆

- **类型 / 问题**：RAW 域目标检测；避免先做 RAW→sRGB ISP。
- **本周变化**：arXiv v1 于 2026-11-02 公开；新增 illumination mask、Bayer 通道敏感嵌入与注意力融合。
- **决策含义**：支持“任务头直接读取 RAW”的路线，但当前证据仍是桌面 GPU 和有限数据集，不能视为移动 ISP 替代。
- **证据边界**：核验方法、数据集和主要表格；未独立复现。

## 精读记录

### 机制与证据

ILLRAW 以轻量适配器将 RAW 映射为检测特征：估计照度 mask，编码 Bayer 通道身份，再通过注意力与 backbone 特征融合。AODRaw 含 7785 张真实 RAW，覆盖日光、低光、雨、雾；LOD 含 2230 张真实低光 RAW；PascalRAW 为合成曝光。AODRaw 上 Cascade R-CNN 的 ILLRAW mAP 23.3，高于 RAOD 21.1 和 RAW-Adapter 19.9；D-DETR 为 22.3 对 raw baseline 20.5。

### 限制与竞争解释

性能仍可能来自合成预训练、照度先验或特征容量，而非 RAW 结构本身。速度仅在 RTX 3090 报告；无手机内存/功耗、跨传感器、错误 ISP baseline 或真实产品检测链路。

### 下一实验

用同一 backbone 比较 RAW、最低成本 ISP、learned ISP 与 RAW adapter；跨 CFA/传感器和曝光域测试，并记录端到端设备成本。

## References

- [arXiv:2611.02995 v1](https://arxiv.org/abs/2611.02995v1)
