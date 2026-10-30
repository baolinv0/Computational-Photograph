# ISP / Computational Photography Weekly Update｜2026-10-30

## 决策摘要

本周高价值增量不是“更大模型”，而是三种系统边界被显式化：双摄切换需要几何—光度联合数据、端侧生成/编辑必须把质量与部署成本分轴、IQA 的显式推理和局部解释都需要反事实审计。Sony LYTIA 720 的量产公告则把 1/1.56 英寸、4K60 单帧 HDR+全像素 AF、低光降噪推进到供应链层，但厂商数字仍待整机验证。

## 新增卡片与评分

评分 = 0.30E + 0.25T + 0.30S + 0.15A。

| 对象 | E/T/S/A | 分数 | 裁决 | 关键边界 |
|---|---:|---:|---|---|
| [Dual-Camera Smooth Zoom](papers/arxiv-2610.34854.md) | 4.5/4.5/4.7/4.5 | 4.56 | Act now | 真实测试无中间帧 GT，NR-IQA 会奖励模糊；无手机端测量 |
| [MoI-Bench](papers/arxiv-2610.37599.md) | 4.3/4.2/4.6/4.8 | 4.46 | Act now | 设备侧共同任务主要是 T2I；VLM judge、能耗与热稳态缺失 |
| [Sony LYTIA 720](https://www.sony-semicon.com/en/info/2026/2026102801.html) | 4.5/4.2/4.7/4.0 | 4.39 | Track product | 官方量产规格，不是整机 IQ 或独立验证 |
| [Chains and Gains](papers/arxiv-2610.33203.md) | 4.4/4.2/4.5/3.8 | 4.28 | Incorporate | RLVR 增益分布内更强；CoT 可用不等于被因果使用 |
| [PREEN](papers/arxiv-2610.36896.md) | 3.7/4.5/4.5/3.6 | 4.13 | Probe | 315M backbone、PST50 小样本；283 ms 不含编辑器应用 |
| [VGIQA](papers/arxiv-2610.37186.md) | 3.8/4.0/4.3/3.5 | 3.96 | Probe | 同源 SR 数据与 MLLM 候选覆盖限制 OOD 结论 |
| [EditJev](papers/arxiv-2610.32635.md) | 3.8/4.0/4.0/3.1 | 3.81 | Watch/Probe | 质量和速度依赖 judge 与模型均值估计 |
| [HDR Exposure Interpolation](papers/arxiv-2610.37135.md) | 3.7/3.8/4.2/2.9 | 3.76 | Watch | 受控对齐曝光序列，不是动态双曝光器件验证 |
| [TINDER](papers/arxiv-2610.37290.md) | 3.8/3.8/4.0/2.8 | 3.71 | Watch | 零训练但高采样成本；真实手机退化/端侧成本未知 |

## 本周改变的判断

1. **镜头连续切换问题从“VFI 后处理”前移到数据与标定**：几何和光度不应被一个黑盒过渡模块耦合；但合成训练与无 GT 真实评价必须分开。
2. **端侧生成评测从 MAC/模型时延前移到完整部署结果**：存储、峰值内存、端到端等待和任务覆盖不能压成单一总分。
3. **可解释 IQA 分裂成两条互补证据**：VGIQA 提供“哪里坏”，Chains and Gains 证明“说得像理由”未必是评分因果路径。
4. **低维编辑器重新成为生成模型的交付接口**：PREEN 的价值是 29 维可逆预设，而不是像素 SOTA；大 backbone 与小 benchmark 是当前产品风险。
5. **产业侧单帧 HDR/低光推进到中端尺寸传感器**：LYTIA 720 官方称 1/1.56 英寸、约 50MP、4K60 HDR+全像素 AF，计划 2026 年 11 月初量产；采用机型与整机收益未知。

## 发现与核验范围

- 8 篇均核验 arXiv v1 首页、方法和选定实验页；DCSZ/MoI 另核验作者项目页。未做独立复现。
- 统一 paper-search 接口仅 arXiv 可用，OpenReview/其他源依赖缺失且一次超时；最终依靠 alphaXiv 日期发现、原 PDF 与一手项目页补足。不能声称覆盖全量 cs.CV/eess.IV。
- 社交热度未进入评分；暂无可核验的相关权威社交评论。
- Qualcomm 10-27 CAMSS/RAW 与 OPPO 10-29 验证矩阵已在当日日报出现，本周只作支持，不重新标新。

## References

- https://arxiv.org/abs/2610.34854
- https://arxiv.org/abs/2610.36896
- https://arxiv.org/abs/2610.37599
- https://arxiv.org/abs/2610.33203
- https://arxiv.org/abs/2610.37186
- https://arxiv.org/abs/2610.37135
- https://arxiv.org/abs/2610.37290
- https://arxiv.org/abs/2610.32635
- https://www.sony-semicon.com/en/info/2026/2026102801.html
