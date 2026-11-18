# LC-ISP Benchmark: Leveraging Capture Frames for Real-Time Learned ISP
更新：2026-11-18｜canonical arxiv-2611.19284｜首次公开可核验：2026-11-14 arXiv v1｜首次覆盖：2026-11-18
主 T01；次 T05/X01/T02；系统角色：采集/数据/目标/训练/部署；裁决 GO-E；地图 New route + Engineering maturity。
目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)
## 快速回忆
- 命题：用同设备实时单帧预览与多帧照片输出之间的成像质量差构成可信的中间/最终监督，训练轻量单帧 ISP。
- 前序区别：DPED/ZRR 的跨相机参考、SID 的曝光配对、MAI/Neural ISP 的目标渲染，与本研究的同设备 live/capture 同时监督是并行路线，**非声称直接继承**。
- 决策：作为真实数据构建 GO-E，不等于采集真实辐照度 GT；不因本论文更换现有 AE–TM 路线。
## 精读记录
- 输入：iPhone 16 Pro 同场景单帧 RAW、实时预览 sRGB、对应多帧照片流及 Capture sRGB。输出：单帧质量提升的两阶段 Neural ISP。
- 数据：1,000 原始不同场景，按场景拆分后裁剪得到 53,892 组监督 patch；不能将 patch 数当独立场景数。
- 作者在约 2.5 GFLOPs 的 Lite 模型报告相对最强同预算单帧基线约 +2dB PSNR；同方法去中间监督 22.78 dB，完整 23.36 dB（论文选定表格，详见原文）。
- 最强替代解释：优势可能来自同设备监督、高质量多帧目标、两阶段网络或监督条目更多，需要固定架构/数据规模及目标质量作解耦。
- 离线：真实同设备 live/capture 成对采集→配准/过滤→中间融合监督与最终风格监督→训练单帧 ISP。
- 在线：单帧 RAW→恢复模块→渲染模块→RGB。多帧融合只服务离线监督，**不代表在线需要同时执行多帧融合**。
## 证据边界
- Capture sRGB 已含融合、降噪、调色与色调映射，属于设备拍摄的目标呈现，不等于场景物理真值或无误伪 GT。
- 对齐运动/遮挡、不同手机与色彩管理泛化、真实持续帧率/温升/功耗尚未独立复现。
- 核验：原论文 v1 方法与选定数据表/消融；不是独立复现。建议固定相同输入、训练预算、两阶段结构比较同设备高质目标与其他目标、以及去除中间监督。
## References
- https://arxiv.org/abs/2611.19284v1
- [训练目标与数据来源 living survey](../surveys/imaging-training-data-synthesis.md)
- [端侧 ISP 与真实成本](../surveys/mobile-isp-and-event-hdr-efficiency.md)
