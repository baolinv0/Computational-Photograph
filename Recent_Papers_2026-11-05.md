# Paper Watch v3.2｜2026-10-25—11-05 停用缺口补查（2026-11-05）

目录：[范围与证据](#范围与证据) · [本轮最重要的地图变化](#本轮最重要的地图变化) · [9 篇补录](#9-篇补录) · [历史去重与限制](#历史去重与限制) · [同步与继续覆盖](#同步与继续覆盖)

## 范围与证据

本次由用户明确要求补查原每日 Watch 自 2026-10-24 后停用的窗口。核对 Computational-Photograph registry，截至本轮开始，2026-10-30 已有 8 篇论文入库；本轮不把它们重新包装为新论文。

通过 alphaXiv 跨 RAW/HDR/TM/ISP/IQA/Reward/数据/恢复/Agent/X01 的新作检索、指定核心作者检索与公开 arXiv 索引，筛选 2026-10-25 至 11-05 的候选。对九篇检查了原文的摘要、相关方法、主要实验、边界并建立卡片；核验层级是 selected sections，**均未独立复现**。这不是对期间全部 arXiv 日列表、全部核心作者和全部正式发表的无遗漏核验。所有首发日期按原论文 v1，不能将本次归档日期当首发日期。

## 本轮最重要的地图变化

**T04｜Benchmark 和 evaluator 的有效性**：LOL-v1/LOLv2-Real 的 GT 风格差异、数据重叠与 test-time tuning 会改变 PSNR 排名；MLLM 可以识别粗颜色偏差，但 CCT 数值与精细 ΔE 有未校准误差；夜景问答准确率也不能代替真实用户候选偏好。详见 [专题](surveys/low-light-iqa-and-gt-validity.md)。

**T01/T02/T05｜联合 LLIE–AWB 与光谱**：CHROMA-MILL 使受控暗光和照明色度变化成为可配对任务；3L-D 通过实测低光照度/光谱补充数据物理真实性；Beyond CCT 引入多通道 ALS 估计 SPD 再计算 CCM。它们分别解决不同层，不应合称一个已验证的端侧系统。详见 [专题](surveys/low-light-raw-awb-illumination.md)。

**T05/T03/X01｜无 GT 的生成训练与真实成本**：非高斯独立噪声测量 + consistency 条件下可学习 clean generative process；Event-HDR 一帧 LDR 与 events 可扩展时序，但严重饱和且无事件时仍只能先验补足；移动端 ISP Challenge 提供同硬件的真实时延和质量 Pareto。见 [noisy-only 专题](surveys/noisy-measurements-to-clean-generators.md) 和 [部署/Event-HDR 专题](surveys/mobile-isp-and-event-hdr-efficiency.md)。

## 9 篇补录

| 首次公开 | 论文 | 主主题 / 决策 | 一句话要点与关键风险 |
|---|---|---|---|
| 2026-10-28 | [What Does LOL Measure?](papers/arxiv-2610.38121.md) | T04 / GO | 官方配对标签风格偏移 + 测试调参可能改变排名；并非否定所有 LLIE 模型 |
| 2026-10-29 | [CIE-computable Color Judgment](papers/arxiv-2610.40212.md) | T04 / GO | MLLM 颜色词与物理色差分开标定；合成色卡、固定 prompt 是边界 |
| 2026-10-29 | [Beyond CCT](papers/arxiv-2610.40175.md) | T02 / GO-E | WP+ALS 估计 SPD 再做 CCM；谱字典 OOD 与真手机 ALS 未证 |
| 2026-10-30 | [Noisy Measurements → Clean Generators](papers/arxiv-2610.42036.md) | T05 / GO | N2N + 非高斯测量专属生成过程 + consistency；依赖已知噪声 law |
| 2026-11-02 | [3L-D](papers/arxiv-2611.02695.md) | T05 / PROBE | 标定夜级光谱与配对；实验台/微缩景物不等于自然夜景 |
| 2026-11-02 | [HIVE-Diff](papers/arxiv-2611.03465.md) | T01 / PROBE↑ | 1 LDR + events → N HDR；无事件的静态饱和内容不可测且运行慢 |
| 2026-11-03 | [CHROMA-MILL](papers/arxiv-2611.04092.md) | T01 / GO | 四光源十一亮度等级 RAW、AWB/LLIE 联合；手机 PSNR_L 不保证最佳 |
| 2026-11-03 | [NightIQA](papers/arxiv-2611.04811.md) | T04 / GO-E | 真实夜景+结构化 QA；80.71% 为 MCQ 非 MOS |
| 2026-11-03 | [Learned Smartphone ISP Mobile AI 2026](papers/arxiv-2611.05008.md) | X01 / GO-E | IMX586 RAW→Fuji reference，在 Adreno/Mali 真机 GPU 测时延；非完整相机链 |

这九篇分布于多个日期，不是某一天通知 9 篇。最高优先级精读：LOL label shift、CHROMA-MILL、CIE color judge；单独研究线优先：noisy-only generative learning、Mobile AI 2026 硬件基线。

## 历史去重与限制

2026-10-30 已入库的八篇，主要包括：双摄平滑变焦、PREEN 手机预设风格迁移、MoI-Bench 端侧图像生成/编辑、reasoning-IQA 的 RL 评审、VGIQA、物理扩散曝光插值 HDR、zero-shot 视频恢复、EditJev 路由。它们已保留在 registry，不重新称作本次新增。

其他本轮检索到、需要另行精读再决定的候选：PBSR 伪 Burst（其 NVS 是否增加可观测高频有争议）、HiFiPix Pixel-space SR、2026 Mobile AI 其他 denoise/RGB enhancement/4K-SR challenge、EditAgent 及相关 Agent 工作（部分已在此前单独讨论）。候选不因首次看到被立即归档为高价值新增。

**覆盖边界**：未完成 11 月 4–5 日全部 cs.CV、eess.IV 的逐条官方日列表审计；也未核对所有候选论文最新版本的实质改动，九篇卡片锚定到已读 v1；已知已发表版本可在下次核验后补 version event。不能把这次补查当作高召回率得到测量的证明。

## 同步与继续覆盖

- GitHub：9 张 canonical paper cards、4 份 living survey、总图、索引、registry；本报告只为补查快照，不复制正文。
- alphaXiv：9 篇按 IQA/Color/Restoration/Raw/ISP/HDR 保存，并已查询 membership。保留其他收藏和用户阅读状态。
- 下一步优先补：不同 benchmark 评价协议跨版本核实、手机外场与 OOD 数据、同训练/推理预算对照、作者级 7–14 天重叠窗口实测。
- 这是一轮由用户主动要求的研究补查，不修改每日 Watch 的原 schedule、通知开关及静默规则。
