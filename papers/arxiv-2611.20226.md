# Streaming across viewing conditions — The effect of viewing distance and display luminance on video quality
更新：2026-11-18｜canonical arxiv-2611.20226｜2026-11-15 arXiv v1；**源研究最早已于 2024-06 QoMEX 公开**，2026 文章为扩展版，非全新 HDR-VDC 数据/任务。首次覆盖本 Watch：2026-11-18。
作者：Dounia Hammou; Lukáš Krasula; Christos G. Bampis; Zhi Li; Rafał K. Mantiuk；Cambridge/Netflix。
主 T04；次 T02/X01；角色：评价/Benchmark/部署；**GO-E / material_update**；地图 Supporting evidence + Engineering maturity。
## 快速回忆
**命题：** 同一 HDR AV1 压缩或超分视频，在不同观看距离/显示亮度条件下的可见失真排序不相同；可用显示光度模型+PU21+投影缩放辅助一些常见 VQA 指标适配。
**时间去重：** 2024 QoMEX 论文 The effect of viewing distance and display peak luminance — HDR AV1 video streaming quality dataset（DOI 10.1109/QoMEX61742.2024.10598289）已包含 HDR-VDC 数据和两条件人评；2026 arXiv 扩展贡献集中在 **35 个 IQA/VQA 指标的横向评价、统计分析、preprocessing adaptation 和局限**，不得当成 2026 首创数据库。
## 方法与证据
- 12 组 4K + 4 组 FHD HDR 源，AV1 编码与 Lanczos 缩放，60/120ppd，显示平均亮度 51/5.6 cd/m²（factor8；不是峰值8×）；双 LG OLED 测试及 pairwise 人类评价。
- 用经过标定的显示 model 将输入映射为实际观察亮度，PU21 编码亮度感知，PPS 几何尺度表示距离；评估 35 类指标对跨观看条件变化的预测。
- 作者发现部分 VMAF/HaarPSI/ColorVideoVDP 等指标经适配有效，但常规 PSNR/SSIM/LPIPS 在该任务明显差；并无单一无争议全局赢家。
- 2026 实质增量：针对不同显示/距离下的指标层比较和 cross-condition 预测，已知条件只限 16 短片、一个 OLED 类型、一个 codec/upsampler、黑暗观看环境。
## 边界与方案
- 不是手机低光拍照 IQA、不是任意风格偏好或线性 HDR 真值；远视距/暗屏可能降低可见伪影，但不能说明恢复了真实细节。作者估计的 bitrate saving 不是实测真实客户端自适应部署。
- 离线：标定显示+距离+亮度→同视频不同压缩/缩放→人类配对→指标适配与校准；在线：参考/失真图+已知或估计观看条件→感知域表征→条件化 VQA；控制层用于编码决策，不改变源图真实内容。
## References
- https://arxiv.org/abs/2611.20226v1
- https://ieeexplore.ieee.org/document/10598289 （2024 QoMEX 前作，数据与实验首次公开）
- https://github.com/gfxdisp/HDR-VDC
- [显示与观看条件专题](../surveys/display-viewing-conditioned-visual-quality.md)
