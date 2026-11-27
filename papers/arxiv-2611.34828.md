# SPIRE: Sensor-Grounded Semantic–Spiking Learning for Robust Object Detection

ID: arxiv-2611.34828 | Hanwen Liang, Wenxuan Liu, Wenxin Huang et al. (Wuhan University of Technology, Peking University, Hubei University) | T01 / X01 | spike sensing, detection, ISP | GO-E | Sensor-grounded perception.
First verified: arXiv v1 2026-11-25; first covered/checked 2026-11-27. Original methods, Tables 1–5 and data/efficiency sections checked; no independent reproduction.
Decision key: one spike stream can supply both stable appearance and temporal count dynamics; gains must be separated from adaptive ISP and semantic backbone.

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [下一实验](#下一实验) · [References](#references)

## 快速回忆
- 同一 spike packet生成全窗 appearance ANN 与四个累积前缀的 rate/edge/difference SNN；ANN语义和测量统计共同初始化膜电位/阈值。
- 轻量可微 ISP 预测白平衡、曝光、gamma、对比度和锐化；传感器局部计数对比监督两支，并形成有界残差修正。
- 这是极端照明检测信号，不是手机摄影画质或通用事件相机结论。

## 精读记录
模拟VOC/COCO使用积分发放模拟器；真实集为PKU-Vidar-DVS单色spike。SPIRE-D在VOC欠曝/过曝AP50为79.59/77.69，在COCO为51.28/49.48；真实集67.07 AP50、40.10 AP75。其62.7 MAC、60.9ms相对SPFD 126.3/65.4ms，MAC减50.4%但时延仅小幅下降。
SPIRE-C消融显示去 adaptive ISP 在VOC掉7.46/6.84 AP50，是最大单项因素；真实集去跨流交互掉4.14。静态non-spiking在VOC略高于完整cumulative LIF（64.08/60.49 vs 63.98/60.24），而真实集完整模型更优，故不能把所有模拟增益归因于spiking时序。

## 证据边界
模拟RGB转spike不等于真实传感器域；真实集类别少、单色且沿用给定划分。MAC不是能耗，60.9ms硬件环境不是移动E2E；参数69.9M也不轻。没有代码可用性、温度、功耗或跨sensor复现证据。

## 下一实验
固定同一backbone/ISP，对比单帧、静态count、累积non-spiking、LIF；在两个真实spike sensor上做跨设备测试；记录从采集packet到检测输出的吞吐、功耗和延迟，而非只报MAC。

## References
- https://arxiv.org/abs/2611.34828v1
- https://arxiv.org/html/2611.34828v1
