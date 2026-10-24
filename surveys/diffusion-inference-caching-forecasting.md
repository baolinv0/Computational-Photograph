# 多步 Diffusion 推理加速：缓存、预测与少步蒸馏如何选择？

版本：v0.1｜2026-10-24｜X01 主主题，T03 交叉

目录：[一分钟回忆](#一分钟回忆) · [竞争路线](#竞争路线) · [判断与证据](#判断与证据) · [系统方案](#系统方案) · [References](#references)

> 这是已在 10-21 推荐的 SpecKCast 的地图补录，不是新论文通知。SpecKCast 原文关键章节已核对，其他前序主要依据其 Related Work 定位，尚未逐篇全文复核。

## 一分钟回忆

**问题**：保持同一多步生成器和任务条件，如何减少昂贵 DiT 前向并控制轨迹漂移？

**路线选择**：少步蒸馏改变模型；缓存复用旧特征；预测从历史推算未来；频带预测进一步考虑不同频率与噪声进度的不均匀性。

**记忆反例**：对 full-sampling 输出更接近，不等于对真实 GT 更忠实；在 1-NFE 模型上没有同样的跳步空间。

## 竞争路线

| 路线 | 关键假设 | 代表工作 | 代价/失败边界 |
|---|---|---|---|
| 训练型少步蒸馏 | 学生能近似教师多步轨迹/分布 | Consistency、DMD、PVD | 额外训练；生成分布变化 |
| Training-free 缓存 | 相邻步骤特征足够相似 | DeepCache、FORA、TeaCache | 跳得太远误差积累 |
| 时间预测 | 历史特征可预测未来 | TaylorSeer、Spectrum | 时间非均匀/轨迹非线性 |
| 频谱辅助决策 | 不同频率变化程度不同 | SeaCache | 与逐频带输出预测不是同一方法 |
| 频带时间校准预测 | 不同频带在不同噪声阶段演化 | **SpecKCast** | 时间校准与不确定性跨模型可靠性待验证 |

关系为机制比较，不因年份先后推断直接继承。

## 判断与证据

[SpecKCast](../papers/arxiv-2610.26837.md)（Rajabi、Karaimer、Lindell、Taati、Brown，arXiv v1 2026-10-19）通过 DCT 将输出 velocity 分频，按 noise schedule/log-SNR 构建 band-specific clock，以 Kalman 追踪系数并按不确定性调用 DiT。

作者报告 FLUX.1-dev、Qwen-Image、Wan2.1-14B、HunyuanVideo 最高约 6× 加速，额外内存 <0.05 GiB；未独立复现，不能推导手机端恢复真实性。

**旧判断**：多步扩散加速可用少步蒸馏或缓存。**新判断**：Training-free 必须分成 reuse 与 forecast；forecast 又有统一时间与分频时间校准路线。**不变**：没有证据证明任何路线对所有恢复任务、设备、NFE 都最好。

## 系统方案

在线：

```text
多步 DiT + sampler + noise schedule
   ├─ full steps（基线）
   ├─ cache/reuse（重用旧特征）
   ├─ forecast（预测整体特征）
   └─ band-aware forecast：velocity → DCT → 每频带 Kalman
                                    ↓
                           风险门控 DiT 调用
                                    ↓
                              inverse DCT
                                    ↓
                            原 sampler 更新
                                    ↓
                        生成输出 + 实际时延
```

离线：该方法无需重新训练模型，但需合理校准频带/门控超参，不能在测试集上选择最佳配置。

**选择条件**：多步模型、可访问速度输出和 sampler、denoiser 时间占主导时可试；黑盒编辑或一步模型不宜直接套用。恢复任务应另评估真实 GT fidelity、文字/细线/肤色幻觉、显存和完整延迟。

**最小可信实验**：同模型/采样器/退化输入/seed/实际 GPU 时延预算下对比 full、TeaCache、TaylorSeer、Spectrum、SpecKCast；按退化类型报告 PSNR、LPIPS、结构真实性和端到端延迟。

**覆盖缺口**：尚需独立核对 TeaCache、TaylorSeer、Spectrum、SeaCache 的论文消融与失败案例；尚无 Qwen-Image-2.1 restoration 与手机端实测。

## References

- [SpecKCast 原文](https://arxiv.org/abs/2610.26837v1)
- [作者项目页](https://rajabi2001.github.io/speckcast/)
- [高效生成式恢复专题](efficient-generative-restoration.md)
