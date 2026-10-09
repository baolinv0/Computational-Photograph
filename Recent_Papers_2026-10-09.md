# 2026-10-09 周报快照

> 窗口：优先 2026-10-02—2026-10-09，向近 30 天补齐直接成像空缺。这里记录当周决策变化；技术正文只维护在 canonical paper cards。

## Executive Decision

本周更值得押注的不是单一新 backbone，而是三条系统边界：**任务目标开始反向约束 ISP、恢复 agent 以证据/验证包装基础模型、evaluator 本身成为必须审计的失效点**。直接移动端部署证据仍稀缺；0.884M 参数、少步推理或模型内 latency 均不能替代手机端到端功耗/热/带宽验证。

## 选择与评分

| 项目 | 类型 | E/T/S/A | 加权分 | 本周决策变化 |
|---|---|---:|---:|---|
| [RawVLA](papers/arxiv-2609.37530.md) | Camera/ISP + Agent | 4.4/4.7/4.8/3.7 | 4.49 | 新纳入近月证据：任务成功率可直接监督显式 ISP 控件；非人眼 IQ 结论 |
| [EditJudgeBias](papers/arxiv-2610.01670.md) | IQA/evaluator | 4.5/4.4/4.6/4.2 | 4.46 | 新：换序可使偏好反转最高 60.9%，judge 必须先体检 |
| [HarnessIR](papers/arxiv-2610.10133.md) | Restoration agent | 4.3/4.6/4.7/4.0 | 4.45 | 新：从单退化工具链转为 MFM executor + verification；10/08 v2 |
| [OPPO Find X10](https://github.com/baolinv0/CameraPaper/blob/main/raw/oppo/2026-10-08-find-x10-global-launch-preview.md) | Official industry | 4.7/4.1/4.5/4.4 | 4.44 | 日常 intake 已先通知；全球镜头级 4K120/8K30 与 Open Gate 边界 |
| [ARRO](papers/arxiv-2610.06021.md) | Editing/evaluator | 4.3/4.3/4.4/3.2 | 4.16 | 新：结构化最小改动 reward；代码尚未发布、推理预算高 |
| [FLASH](papers/arxiv-2609.37742.md) | HDR/security | 4.1/4.5/4.3/3.2 | 4.13 | 新纳入近月攻击面：跨曝光照明不一致成为融合安全变量 |
| [Dense Illuminant](papers/arxiv-2610.06508.md) | AWB/color | 4.2/4.0/4.0/4.3 | 4.10 | 新：74,321 合成密集光源标签；真实传感器域差距待证 |
| [UniSlider](papers/arxiv-2610.06831.md) | Editing/control | 4.2/4.2/4.1/3.7 | 4.09 | 新：连续编辑要做感知校准，而不是线性强度假设 |
| [LoopMoEVR](papers/arxiv-2610.05109.md) | UHD restoration | 3.8/4.1/3.9/3.4 | 3.84 | 新：小参数循环 MoE；V100 实验不等于移动实时 |

评分公式：0.30E + 0.25T + 0.30S + 0.15A。组合选择优先覆盖 Camera/ISP/3A、恢复、编辑、评价与产业边界，并非单纯按分数取前九。

## Act Now

1. 复现 RawVLA 风格的 **task-aware ISP ablation**：固定 ISP + task adapter、可学习曝光/WB/CCM/tone、RAW-native policy，在真实跨传感器留出上同算力比较。
2. 建立 **evaluator 红队套件**：顺序交换、未编辑区域、文字/脸/重复纹理、跨 judge 一致性；用同一套件审 HarnessIR 与 ARRO。
3. 对 OPPO Find X10 与 LoopMoEVR 分别准备 **端到端测量**：10 月 21 日后核模式组合/热/跨镜头一致性；循环 MoE 测 P95 迭代、NPU 带宽、功耗与热降频。

## Watchlist

- ASTRA（2610.10003）：出现公开数据/代码、跨风格模型外测后升级。
- RawSLAM（2609.20589）：代码与十个真实 RAW/depth/IMU 序列公开后升级。
- Visual Autoregressive Priors for RAW-to-sRGB ISP（2609.18302）：版本历史/全文可核并出现移动端或跨相机实验后升级。

## Negative Intelligence

- ARRO 仓库当前只有 README，不能按“代码已开源”计入可复现性。
- HarnessIR 的闭源 MFM executor 与 verifier 可能共享盲点；无真值真实集上的讨喜结果不能排除幻觉。
- LoopMoEVR 的 0.884M 参数和 V100 实验不能证明手机 4K 实时；FLASH 的防御也只是在受控夜间 proof-of-concept。

## Provenance / novelty audit

- 9 个选择中，7 个为本窗口 arXiv v1；2 个为近 30 天首次纳入且未在前一快照出现；0 个无材料更新的旧条目重复通知。
- OPPO 产品证据已由同日日常 intake 先通知，本周只作为支持证据，不重复标成新发现。
- 论文日期分别记录 arXiv 首次提交和当前版本；没有把 acceptance 或 v2 自动视为新研究。
- 覆盖缺口：未找到通过门槛的本周 AE/AF、demosaic 或独立手机功耗/热测试；不以泛恢复补位。
- 全部结论仍是作者实验或官方规格；无独立复现。社交热度未用于评分。
