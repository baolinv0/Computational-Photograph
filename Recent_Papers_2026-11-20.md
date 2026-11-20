# 2026-11-20 周度影像研究增量

目录：[本周组合](#本周组合) · [决策变化](#决策变化) · [负面情报](#负面情报) · [覆盖与归档](#覆盖与归档)

本快照只链接 canonical card；11月14–19日已由 Paper Watch 通知的工作在这里标为“本周已日更”，不重新包装为周度新发现。当前新增5张11月18日 arXiv v1 卡，均为原文选段核验、未独立复现。

## 本周组合

| 研究 / 事件 | 状态 | E/T/S/A | 加权分 | 决策增量 |
|---|---|---:|---:|---|
| [Joint RAW compression-restoration](papers/arxiv-2611.24805.md) | New | 4.7/4.6/4.8/4.5 | 4.68 | noisy RAW传输目标改为clean reconstruction；给出12MP真机发送端拆账 |
| [LC-ISP](papers/arxiv-2611.19284.md) | 本周已日更 | 4.2/4.0/4.5/4.4 | 4.28 | 同iPhone live/capture建立中间+最终监督，但capture不是radiance GT |
| [TrustUIQA](papers/arxiv-2611.18429.md) | 本周已日更 | 4.0/4.1/4.6/4.5 | 4.28 | NR-IQA跨人评域与metric hacking进入硬门槛 |
| [PrismRestore](papers/arxiv-2611.24915.md) | New | 4.0/4.2/4.2/4.2 | 4.13 | 单冻结骨干调制出8个可调用动作，工具箱存储显著下降 |
| [DetailScale-SR](papers/arxiv-2611.24212.md) | New | 4.0/4.1/4.0/4.2 | 4.03 | 将detail偏好轴从恢复能力中分离，但高detail不等于事实恢复 |
| [ALIVE](papers/arxiv-2611.24579.md) | New | 4.1/4.3/3.9/3.8 | 4.05 | event直接刷新VFM features，避免每5ms重跑encoder |
| [GRAM IQA coreset](papers/arxiv-2611.24233.md) | New | 3.8/3.9/4.2/4.1 | 4.00 | annotation selection显式建模质量/内容/失真结构；有KADID泄漏边界 |
| [TANGO/DUET](papers/arxiv-2611.22699.md) | 本周已日更 | 4.1/4.1/3.7/4.0 | 3.96 | 真实双相机RGB/HR-HSI观测；LR-HSI仍为模拟退化 |
| [Samsung One UI 9.5 Beta](https://github.com/baolinv0/CameraPaper/blob/main/views/products/samsung/galaxy-s26-one-ui-9-5-camera.md) | 官方Update/已日更 | 4.8/2.4/3.6/3.8 | 3.69 | Pro/Pro Video控制可复用性提升，稳定版与模式矩阵未知 |
| [Xiaomi 18 Pro Max评测补证](https://github.com/baolinv0/CameraPaper/blob/main/views/products/xiaomi/xiaomi-18-pro-series-imaging.md) | 独立评测Update/已日更 | 3.6/2.8/4.0/4.0 | 3.58 | 跨镜头偏黄、30×噪声、风噪成为待复测失败场景 |

## 决策变化

1. 移动/穿戴影像的系统边界开始从“模型是否轻量”转向“RAW表示、无线传输、后端恢复如何联合分工”；但342.98ms/12MP仍是离线拍摄量级。
2. Agentic restoration出现“单骨干、多动作”工程路线，存储成本下降不代表Judge或真实域可靠性已解决。
3. 可控SR把detail量变成连续控制轴；需在产品定义中明确“保守恢复”和“创作增强”不能共用真实性KPI。
4. IQA数据预算研究开始审计选样表示，但group leakage足以改变结论，暂不据此削减真实人评预算。
5. 产品端的专业控制UI更成熟；公开证据仍没有证明隐藏ISP/NPU拓扑或稳定版组合能力。

## 负面情报

- GRAM的KADID upstream/downstream可共享reference或distorted sample，必须按scene/content重做split。
- PrismRestore真实集仅NR-IQA；停止规则直接依赖同类分数，存在reward hacking闭环。
- DetailScale-SR的Detail-CFG把MUSIQ推高同时PSNR/LPIPS/FID回退；“更细”不能写成“更真”。

## 覆盖与归档

学术检索覆盖arXiv/alphaXiv 11月18日首传及11月14–19日日更；OpenReview全量、全部作者主页、独立复现与专利全量未完成。八家厂商与供应商使用同日已读回的daily intake来源结果；Huawei聚合、部分OEM研究/开发者入口仍不完整。五张新卡及本快照进入registry；alphaXiv/Notion同步状态以读回结果为准。
