# RMGNet / UWOT — Thermal-Guided Low-Light UAV Image Enhancement
更新 2026-11-25｜Zhicheng Zhao, Yu Wang, Jiangong Xu, Lixiang Xu, Chenglong Li, Jin Tang（安徽大学等）｜arXiv v1 2026-11-23，11-24 官方 cs.CV 公告，首覆盖 11-25。
T01 / T03,T05,T04｜采集、数据、配准、执行、评价｜GO-E（数据及工程证据）｜Supporting evidence + Boundary refinement。
## 快速回忆
额外热红外信息既需要空间对应，也要判断在可见光局部是否有必要使用。区别于 TANGO 的跨谱 SR，目标是正常照明 RGB；热响应不等于真实可见亮度/颜色。RT-X Net（ICIP 2025）已用 RGB-T cross-attention，本次不是首次热引导。
## 精读记录
UWOT 5000 triplets，4000/500/500；DJI Mavic 3T 实采日间 RGB 参考和同地点夜间 RGB/T，另有 DroneVehicle 白天配对经 inverse sRGB、全图暗化0.05–0.08、Gaussian read/shot-like noise 合成低光；不能称5000组同步真实夜间GT，真实/合成数量及 scene-disjoint 核验不足。日夜照明/运动改变导致 reference 非物理夜景真值。
在线：RGB/T→RGB轻度预清理、Sobel/Laplacian priors→粗细 displacement + 对齐置信/可见证据可用性→encoder-decoder→保细节、保护高光的relight、热补偿三候选→空间加权 RGB。离线使用配对参考监督 L1/感知/smooth/heuristic；无外部 Agent。
作者 Table2 UWOT：ICLRNet 24.31、ICLRNet-M 25.16、完整25.38 dB；Retinexformer 24.06→25.05 dB（仅4通道输入）；RT-X 24.53。Table3 单独重训的 DroneVehicle 合成测试 Ours22.88 vs RT-X22.78。Table4 组件全无24.34、仅 RAGCM24.43、RAGCM+MSERM24.89、全25.38；Table5 best双候选24.98 vs 全25.38。新增观测贡献不可混作复杂路由收益。2.93M/30.89 GFLOPs 非完整真机延迟。SAM3 分割指标是日间参考的 pseudo-label 一致性，不是真实标注分割精度。Table9固定 YOLOv8m-OBB 的 DroneVehicle mAP50:95 51.62 vs RT-X46.78，非跨相机真实部署证据。
## 判断与行动
前序 RT-X Net（ICIP2025）已验证热引导；UGD-FM/TANGO 是不同谱段、不同目标的共同机制而非继承。新证据支持双置信（空间可靠性、源信息可用性）再路由；简单 concat 已解释大部分 PSNR 收益。固定相同 RGB/T、数据和预算，对比 RGB-only、concat、置信门控，按实采/合成、视差及高光分层；不改当前单相机 ISP。数据下载与真实独立复现未核验。
## References
- [arXiv v1](https://arxiv.org/abs/2611.30114v1)（alphaXiv 原文提取 §3–5/Table2–9 核验）
- [RT-X Net](https://ieeexplore.ieee.org/abstract/document/11084466)（摘要）
- [跨模态 survey](../surveys/unaligned-guided-restoration.md)
