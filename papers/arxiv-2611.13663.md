# Overcoming Dynamic Range Limitations in Computational Hyperspectral Imaging

- Paper ID: arXiv:2611.13663
- Authors: Qianqian Yu, Jinhang Lin, Zhihai Yao, Shuo Wang, Chaofan Weng, Xiang Hao
- arXiv first upload: 2026-11-10 07:08 UTC, v1
- First covered: 2026-11-13
- Main theme: T01 — 相机、ISP、RAW、3A 与传感器边界
- Secondary themes: T02, X01
- Verdict: PROBE
- Verification: arXiv metadata and selected original-paper method, result and limitation sections checked; no independent reproduction.

## 30-second recall

把多曝光融合前移到九通道编码测量域：解析可靠性先验与学习到的空间/通道修正共同加权，再做光谱反演。受控光学密度靶上作者报告相对最佳固定单曝光的光谱重建动态范围增加 16.0 dB。

**记忆锚点：** 这是“先判断每个编码通道在每个曝光是否可信，再反演光谱”，不是普通 RGB HDR 合成。

## 完整系统回忆卡

- **问题：** 单一曝光无法同时让不同光谱响应通道避开饱和与噪声底。
- **机制：** 曝光归一化；hat-shaped 解析可靠性先验；空间/通道修正与 softmax 融合；μ-law L1 和测量域 spectral-angle 监督；支持可变曝光数。
- **证据：** ICVL 合成 HDR 的 20 个测试场景、四种三曝光配置；作者报告测量域 PSNR 60.362 dB，光谱 PSNR 44.606 dB。真实 ColorChecker 两/三曝光为 38.341/38.992 dB，最佳单曝光 35.792 dB。512²、RTX 5080 报告 8.45 ms，但这不是完整采集到显示或移动端时延。
- **边界：** 静态受控场景、专用九通道光谱相机；未处理多曝光运动，不能外推手机 Bayer/Quad Bayer；无功耗与热稳态。
- **竞争解释：** 增益可能来自专用标定、曝光覆盖和融合共同作用，不能单独归功于 learned adjustment。

## 判断与下一实验

优先价值是测量可靠性建模与曝光/编码联合门控。最小实验应固定反演器，比较解析先验、学习修正和二者结合，并加入运动物体与传感器响应漂移。

## References

- [arXiv:2611.13663](https://arxiv.org/abs/2611.13663)
