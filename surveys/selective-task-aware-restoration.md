# 选择性图像恢复与任务效用：什么时候保留原图？

版本 v0.5 | 2026-11-21 | 主主题 T06，桥接 T03、T04、T01、X01

目录：[快速回忆](#快速回忆) · [问题树](#问题树) · [关键新证据](#关键新证据) · [完整方案与局限](#完整方案与局限) · [判断与积压](#判断与积压) · [References](#references)

> 研究任务是 KEEP / RESTORE / REJECT 决策，而不是默认增强越多越好。本页选段核验两项不同任务的证据：[Gate3DGen v1](../papers/arxiv-2610.31649.md)（3D 生成）和 [道路异常检测/SCI 路由](../papers/arxiv-2611.08393.md)（合成低光检测，2026-11-05 v1；2026-11-08 **backfill，非新作提醒**）。VetoNet、PreActIR、任务导向 ISP 等仍待在同一条件下复核，不能将跨任务工作加总成社区共识。

## 快速回忆

输入影像可能含有不同缺陷，也可能本来已经足够好。任意恢复器都可能改变结构，且下游任务不一定偏爱人眼看来最清晰的图。

重要分叉：
- **直接对所有图运行恢复器**：实现简单；有损害原本干净图的风险。
- **输入先路由 KEEP / RESTORE**：有选择成本和误分损失；净化器仍需要做得对。
- **候选后验证 ACCEPT / VETO**：能够拒绝失败结果，但验证器自身可能同源偏差。
- **图内局部保留 / 生成融合**：不是整图 KEEP/RESTORE，也不是完成后的候选 Judge；在高不确定区域增加生成成分，可靠区域以原观测为锚。
- **面向下游任务学习**：评价从纯 RGB 感知变为几何、识别、检测或其他效用，需要各任务特定 GT/Proxy。

这些分叉可组合但不是因果继承。路由判断质量与恢复器像素质量必须独立评估。

## 问题树

```text
真实输入图
  → 是否有退化/是否值得处理？
      ├ KEEP：保留原图
      └ PURIFY/RESTORE：条件化恢复器
                  → 下游任务或人类观看
                  → 任务效用 / 事实保真 / 感知质量分别判断
```

仅在有下游任务的情形，任务效用成为首要指标；消费照片恢复仍需考虑用户偏好、影像真实性、显示与相机条件。

### 2026-11-15 历史 backfill｜空间级选择性生成与整图路由是两类控制问题

[SGVD：Selective Generative Restoration for Video Deraining](../papers/arxiv-2611.16310.md) 的 v1 **2026-11-12** 首传，已在先前成功覆盖的 11-13 官方 cs.CV 列表，故本次归入 **backfill**，**不作为新论文通知**。该工作对 T03 建立独立的**区域级**路线：两个随机生成 clean-latent probe 的差异形成不确定性图 M，控制 `z_sel=M*z_generated+(1-M)*z_LQ`；训练期 ATC 五帧 anchor 约束视频一致性。没有整图 Agent 路由或事后 Listwise Judge。

| 决策位置 | 输入与控制变量 | 执行结果 | 必须比的简单对照 |
|---|---|---|---|
| **整图路由**（Gate3DGen / low-light detector） | 输入图/任务信号 → KEEP/PURIFY | 只选保留或调用一个执行器 | always-KEEP / always-PURIFY |
| **图内区域融合**（SGVD） | 雨视频 latent / 两次随机预测差异 → 空间连续 M | 在潜空间混合 LQ 与生成 proposal，adapter 送入 DiT | 统一 mix、显式 rain/occlusion mask、同 compute 的随机 mask |
| **候选后选择**（Agent Judge，本文未实现） | 固定候选池与质量证据 → accept/reject/rank | 从已生成结果中选优 | 等预算 best-of-K、人类 oracle |

**证据**：作者 §IV-G 同数据消融中无 USG/ATC PSNR 23.0013、warping error 0.0287；仅 USG 26.2416 / 0.0309；仅 ATC 25.9347 / 0.0225；联合 26.5174 / 0.0207。空间选择本身不保证时序稳定。§IV-F RTX4090 48GB、640×480、49帧，1 step + 2 probes 为296ms/frame (3.37FPS)；无 probes 133ms/frame (7.52FPS)。**一网络更新不等于一次网络评估**；probe 带来显著时间代价，端侧尚无证据。训练数据 NTURain-Syn 仅来自8段 clean clips 的25段合成雨序列，真实 NTURain-Real 缺干净 GT；作者 NR-IQA 改善不等于真实区域纹理保真。

**旧→新→保持**：原路由“是否执行”仍须与 always-KEEP 比；新增 “同图哪里借助生成、哪里保留观测” 的可检验连续控制。**不变**：生成结果的可达性、错误自信（低预测方差仍可能 hallucinate）、Judge 可选择性都没有被该机制解决。该工作与 [DeLang-SR](../papers/arxiv-2611.10485.md) 的方向/局部幅度分离是分析者归纳的共同问题，不可称直接继承或已形成共识。**裁决 PROBE / Supporting evidence + Boundary refinement**，目前不改任何手机 TM/ISP 系统。最小实验为固定 backbone 与总 forward 数，对比随机分歧 Mask、可见遮挡 Mask、固定/随机混合以及高置信错误区域的保真和泄漏。

## 2026-11-19｜内部执行策略场：ExplicitIR 与选择性恢复的边界

[ExplicitIR（2026-11-17 v1，PROBE）](../papers/arxiv-2611.22222.md) 是另一种“哪里改/改多少”：其输入是混合退化 RGB，网络内部预测 per-pixel **Budget d** 和 **Style λ**，前者显式约束恢复 decoder 更新的幅度，后者在 narrow/wide context 响应中选择。原论文只需恢复 GT 的图像监督，不需每像素 policy label 或外部 Agent，在线仍只单次 forward。

| 路线 | 决策位置与信息 | 可改变的变量 | 不能证明的能力 |
|---|---|---|---|
| Whole-image KEEP / RESTORE | 外部 router | 整图是否调用 purifier | 局部修复可靠性 |
| SGVD 的 uncertainty mixing | 生成恢复执行中 latent | 逐像素 LQ/generative latent 混合比 | 置信=事实正确性 |
| **ExplicitIR 的 Budget / Style fields** | 判别式恢复网络 decoder 内部 | 当前 feature 更新幅度/局部上下文范围 | 输出像素严格不变、外部工具策略/候选选优 |
| **区域参考条件恢复 FAIR（2026-11-19）** | LQ + ROI R + reference/text/contour → 一步生成 | ROI信息补充（来自额外可用证据）和作用域严格约束 | Oracle GT区域检索不可带到真实部署 |
| **RegionAgent（2026-11-19）** | Base + ROI候选 + 专家动作→分步DPO学习策略，至多8 refine | 学会单步行动和全轨迹延迟后果 | GT reward与在线无GT分离；执行器能力及调用预算固定验收 |
| 独立候选 Judge | 执行后的外部核验 | Accept/Reject、重试/停止 | 执行器候选不可达问题 |

作者的三任务平均 PSNR Restormer 31.98、ExplicitIR 32.78、外部标签条件化 DFPIR 32.88 dB；不是击败所有同条件模型。与 SGVD 的“局部选择”是分析者的共同抽象，并非方法继承。**替代解释**：更强特征容量、RMS 归一化、普通空间注意力或 gated updates 在等预算下也可能产生相似结果。需要分解归因，而非把 +0.80 dB 全部算成可解释 field。

**判断变更**：原来保留/恢复控制主要发生在整图路由或生成后的验证；新增第三种内部 feature 更新控制位置。**不变**：真实信息不可恢复时仍可能凭先验补细节；局部低 d 不等于像素完全无损，且只有一致 GT 下才能测量内容保持。该工作尚无真实相机 RAW / 手机 E2E 验证。离线 clean/LQ 配对训练，在线 input→Budget/Style→decoder→output；Agent 可选但未验证。当前实现不作扩容，最小判别实验固定 backbone/FLOPs/训练，比较 naive spatial attention、单 d field 和双场，记录 degraded ROI 收益与 clean ROI leakage。


## 2026-11-21｜控制区域是三种不同系统动作
**既有** SGVD/ExplicitIR 在单模型内部决定哪些像素混合/更新；新增 [FAIR](../papers/arxiv-2611.26456.md)（GO-E）用**外部可靠参考和ROI描述指导单次生成**；[RegionAgent](../papers/arxiv-2611.26179.md)（PROBE）用**多步策略优化决定每次局部动作和什么时候停**。彼此有空间控制共同抽象，不能称直接继承。
| 路线 | 新证据改变哪个接口 | 强简单替代 | 条件性判断 |
|---|---|---|---|
| FAIR | 外部 reference/outline/text 进入 frozen-ish 大生成执行器的区域condition；借助可靠额外参考处理不可恢复信息 | 相同reference与mask的直接ROI crop处理/简单融合；同背骨全图prompt | 120 synthetic区域：FAIR FID63.28/ROI LPIPS0.0319 vs AdaRefSR81.93/0.0368；但synthetic reference以 clean GT 区域辅助检索。无GT完全LQ驱动FID67.97而非63.28；20人×10案例有偏好证据，真实NR-IQA不全面胜出 |
| RegionAgent | 同一ROI修复动作的单步即时收益与跨轨迹的后续收益分开训练；推理最多8动作 | 固定四专家+mask，仅SFT或step-DPO；同预算Best-of-K | MiO100 Group C SFT20.01→step-DPO20.47→两级DPO20.90 dB；训练数据10K一步+20K轨迹偏好源于GT和自动指标；18.60s/图；没有真实RAW部署 |
| ExplicitIR | 单次内部逐像素decoder预算/上下文 | 单场+通常空间注意力 | 原结论仍PROBE；无外部参考不能恢复不可见内容 |
**旧→新→保持**：从“位置是否值得恢复、网络怎样抑制泄漏”拓展为“哪里需要外部事实引导”和“当前操作会否恶化后续状态”。不变：可达性（是否有正确候选）、可发现性（预算内得到）、可选择性（能否认出正确）必须独立试验，任何自动生成代理GT不能证明真实细节已经恢复。
**方案回忆**：离线分别 (FAIR) GT+合成退化→错误ROI定位→检索参考→单次条件恢复训练；(RegionAgent) GT+固定专家尝试→对动作/完整轨迹配对→SFT/DPO。在线 (FAIR) LQ+可靠额外reference+ROI→一次恢复；(RegionAgent) Base+当前图→区域动作→可选反馈→停止；Judge是外层可添加能力，不是两者已验证共同系统。**行动：**不改变现有执行器；最小对照同域真实失败ROI上固定候选/参考/预算，分开比较“有无可靠参考”的信息增益及“有无轨迹DPO”的策略增益。
**记忆锚点**：告诉模型“修哪里”不等于提供“正确内容”；告诉策略“这步有用”不等于证明“最终路径好”。

## 关键新证据

[Gate3DGen](../papers/arxiv-2610.31649.md) 用 3D assets 构造恢复监督，并将下游 3D 几何作为成功判据。对比非退化输入，合成 3D benchmark 的几何误差大幅改善，证明**任务相关恢复目标有价值的局部证据**。

但其 router 的关键负例尤其值得记忆：合成输入上 recall 88.45%、accuracy 90.77%；真实图片使用模型生成的 proxy label 时，router accuracy 58.33%，没有优于 always-PURIFY（同为 58.33%），即使其他评分较强。它不证明“先路由一定更好”。该任务的显著收益主要证实有任务监督的 **purifier** 的潜力，不等于 **router** 有真实域的可部署增益。

论文比较的 3D 任务在冻结 TRELLIS.2 / Pixal3D 上进行，不能推出通用 ISP 参数或 RAW 成像改善；同一作者报告还显示 3D Quality 的 VLM 打分不是最高。

### 2026-11-08 历史 backfill｜低光检测：规则门控不必然比不增强好

[Adaptive Low-Light Enhancement for Road Anomaly Detection](../papers/arxiv-2611.08393.md) 的 2026-11-05 arXiv v1（**非本轮新论文通知**）增加一个有价值的负例：固定 clean-only 检测器，给道路坑洞/减速带 RGB 人为 gamma+近似信号相关噪声；SCI 统一增强在 dusk 损害检测，基于图像平均亮度的三分支规则能挽回部分损失。研究有 **Jetson Nano** 处理阶段实际延迟表，但无真实夜间 RAW 和混合天气检测验证。

| 研究与目标 | 输入与控制 | KEEP vs 路由的对照 | 可靠结论/不能推出 |
|---|---|---|---|
| [Gate3DGen](../papers/arxiv-2610.31649.md)：单图 3D 重建 | 真实/合成照片，learned KEEP/PURIFY gate + task-aware purifier | 96 张真实图 proxy-label router accuracy 58.33%，等于 always-PURIFY；主要收益属于 purifier | 保真任务目标有价值，**但 learned router 独立收益不足** |
| [Low-Light Road Detection 2026](../papers/arxiv-2611.08393.md)：mAP@50 | 4,444 场景图两类道路缺陷；合成低光，mean-luminance 三分支和 SCI variants | YOLOv8n severe：KEEP **0.268**、统一 SCI **0.282**、router **0.218**；RT-DETR dusk：KEEP **0.861**、统一 SCI **0.722**、router **0.847**（作者 Table I） | 门控能减少某些无谓处理损害，但**并非总能超过 KEEP 或统一 SCI**；与 SCI 模型强度变化未隔离 |

**旧判断 → 本次增量 → 当前判断**：原已知 “真实域 learned router 可能不如 trivial default”；新的不同下游任务显示“无训练的明亮度规则路由同样可能在某些 detector/退化程度上劣于 always-KEEP”。保持 **PROBE（路线）**，该 backfill 论文单项裁决 **WATCH**。这不是对所有学习式路由的普遍反证，也不是新的共同学术共识。

**分层方案回忆**：离线用真实标注检测数据与不同光照生成（必要时真实夜间补集）固定训练 detector、单独评估 enhancer；在线 `image → measured luminance / optional task condition → KEEP | moderate-enhance | denoise+strong-enhance → frozen detector → detection`；Agent 可作为上层策略但本文**无 Agent**。必须用独立 held-out 真实夜间与多个 detector 报告 mAP、漏检、分支错误代价及分支+检测 **完整时延**。原 paper 在天气退化图上**不使用 SCI**，不能将这条规则扩展为混合雨雾去噪。

最小判别实验：同一真实低光测试切分，固定 detector 和 SCI variants，比较 always-KEEP / always-medium / always-strong / pre-fixed luminance router；再按 detector 分层评估。若路由仅挽回统一增强的伤害而没有超过相应强简单基线，则不增设在线控制器。

## 2026-11-10：跨域负证据——会诊断，不等于能恢复

[Zero-Shot Benchmarking of Unified Multimodal Models for Shallow-Water UAV Image Distortion Assessment and Restoration](../papers/arxiv-2611.09740.md)（2026-11-06 v1，GO-E / Counter-evidence，主 T04、连 T03/T06）是本路线的另一类负证据。它并不比较 KEEP vs 增强路由的算法，而是同时测量**统一 MLLM 的失真诊断能力与其直接恢复能力**：1000 张图、600 半合成+400 全合成，五个 frozen unified MLLM 的 zero-shot 诊断与 100 张图直接恢复。作者报告最佳失真识别 balanced accuracy 约 0.654，而直接恢复的 PSNR 平均增益最多 0.255dB，所有受测模型在 pooled LPIPS 上均无改善，部分内容被幻觉式重新生成。

**路线关系**：Gate3DGen/道路低光研究的是「要不要调用 purifier」，这篇则问「即使识别了退化，同一个统一模型是否具有恢复能力」。它们具有共同**识别→执行分离**的抽象，却是不同任务/域，不构成直接继承或跨领域共识。海水散射/水下 UAV 与真实手机 RAW 低光不是相同测量退化。原论文少量 human annotation 对浊度一致性约 0.507，合成 ground truth/人类评分同样要核查。

**判断变化**：此前的“路由可能不如 always-KEEP”保持；现在增加“**识别/分析质量不能作为直接 restoration executor 的能力代理**”，也不能把生成式回写的 NR-IQA 当作源结构保真。在线最小方案：image→可选退化诊断（硬数字能判时不必上 VLM）→强简单 deterministic/specialist/unified MLLM 候选→独立 PSNR/LPIPS/ROI leakage/人评；Agent 可以选择，但未验证与本论文共同集成。对当前系统**不改**，未解决的是图像本身信息不可恢复时的真实可达性。

## 完整方案与局限

**离线**：可校验 GT/几何资产 → 干净视角 → 受控及可审计退化 → 多任务目标和路由标签 → purifier 和 router 分别训练 → 独立真实照片/下游设备检查。

**在线**：真实图 → 证据化是否处理 → 保留/恢复候选 → 对最终任务条件评测（可做弱/部分反馈）→ 满足阈值才提交结果；保留原始图与选择日志。

**必须独立对照**：Always-KEEP / Always-PURIFY / Learned-Router；以及任务质量、失败处理、总耗时、原图影响。无可用 GT 时，proxy 不能成为“真实净化需要”的绝对标签。

## 判断与积压

旧认知：缺少可靠 GT 时，只能在恢复后用保真/感知指标做验收。

新证据：高保真目标任务提供了额外可用的比较信号，Gate3DGen 证明选择性净化框架可用，但其真实域路由的独立收益不成立（现有 proxy 评价条件下），应进一步区分路由价值和恢复本身。

当前路线裁决：**PROBE**，优先保留 KEEP、always-on 增强和按任务评价的强基线；暂不把 Gate3DGen 学习路由或道路检测亮度门控写成通用照片/移动 ISP 的已证最佳策略。2026-11-08 backfill 论文仅 **WATCH**。

**2026-11-15 补充边界**：整图路由与潜变量区域混合并列，不能把 SGVD 的 ROI 保真提升算成 learned KEEP/RESTORE selector 成功；见上方 backfill 表及卡片。

相关待核：VetoNet 2610.21335（GT 风险控制）、PreActIR 2610.20384（执行前价值预测）、RawVLA 2609.37530（任务导向 ISP）；核心机制和公平性需各自核验，不把它们直接升级为 Gate3DGen 的方法前作。

- [FAIR v1](https://arxiv.org/abs/2611.26456v1) · [canonical](../papers/arxiv-2611.26456.md)
- [RegionAgent v1](https://arxiv.org/abs/2611.26179v1) · [canonical](../papers/arxiv-2611.26179.md)

## References

- [Gate3DGen arXiv v1](https://arxiv.org/abs/2610.31649v1)
- [论文细节与作者实验](../papers/arxiv-2610.31649.md)
- [Adaptive Low-Light Enhancement for Road Anomaly Detection, 2026-11-05 v1（backfill）](https://arxiv.org/abs/2611.08393v1)；[HTML Tables I–II](https://arxiv.org/html/2611.08393v1)
- [2026-11-06 水下UAV unified MLLM 诊断/恢复基准](https://arxiv.org/abs/2611.09740v1) · [canonical card](../papers/arxiv-2611.09740.md)
- [SGVD v1：Spatial uncertainty-gated video deraining，2026-11-12 首传，2026-11-15 backfill](https://arxiv.org/html/2611.16310v1) · [canonical card](../papers/arxiv-2611.16310.md)
- [T03/T06 总图](../LITERATURE_MAP.md)
