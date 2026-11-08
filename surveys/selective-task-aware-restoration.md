# 选择性图像恢复与任务效用：什么时候保留原图？

版本 v0.2 | 2026-11-08 | 主主题 T06，桥接 T03、T04、T01、X01

目录：[快速回忆](#快速回忆) · [问题树](#问题树) · [关键新证据](#关键新证据) · [完整方案与局限](#完整方案与局限) · [判断与积压](#判断与积压) · [References](#references)

> 研究任务是 KEEP / RESTORE / REJECT 决策，而不是默认增强越多越好。本页选段核验两项不同任务的证据：[Gate3DGen v1](../papers/arxiv-2610.31649.md)（3D 生成）和 [道路异常检测/SCI 路由](../papers/arxiv-2611.08393.md)（合成低光检测，2026-11-05 v1；2026-11-08 **backfill，非新作提醒**）。VetoNet、PreActIR、任务导向 ISP 等仍待在同一条件下复核，不能将跨任务工作加总成社区共识。

## 快速回忆

输入影像可能含有不同缺陷，也可能本来已经足够好。任意恢复器都可能改变结构，且下游任务不一定偏爱人眼看来最清晰的图。

重要分叉：
- **直接对所有图运行恢复器**：实现简单；有损害原本干净图的风险。
- **输入先路由 KEEP / RESTORE**：有选择成本和误分损失；净化器仍需要做得对。
- **候选后验证 ACCEPT / VETO**：能够拒绝失败结果，但验证器自身可能同源偏差。
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

## 完整方案与局限

**离线**：可校验 GT/几何资产 → 干净视角 → 受控及可审计退化 → 多任务目标和路由标签 → purifier 和 router 分别训练 → 独立真实照片/下游设备检查。

**在线**：真实图 → 证据化是否处理 → 保留/恢复候选 → 对最终任务条件评测（可做弱/部分反馈）→ 满足阈值才提交结果；保留原始图与选择日志。

**必须独立对照**：Always-KEEP / Always-PURIFY / Learned-Router；以及任务质量、失败处理、总耗时、原图影响。无可用 GT 时，proxy 不能成为“真实净化需要”的绝对标签。

## 判断与积压

旧认知：缺少可靠 GT 时，只能在恢复后用保真/感知指标做验收。

新证据：高保真目标任务提供了额外可用的比较信号，Gate3DGen 证明选择性净化框架可用，但其真实域路由的独立收益不成立（现有 proxy 评价条件下），应进一步区分路由价值和恢复本身。

当前路线裁决：**PROBE**，优先保留 KEEP、always-on 增强和按任务评价的强基线；暂不把 Gate3DGen 学习路由或道路检测亮度门控写成通用照片/移动 ISP 的已证最佳策略。2026-11-08 backfill 论文仅 **WATCH**。

相关待核：VetoNet 2610.21335（GT 风险控制）、PreActIR 2610.20384（执行前价值预测）、RawVLA 2609.37530（任务导向 ISP）；核心机制和公平性需各自核验，不把它们直接升级为 Gate3DGen 的方法前作。

## References

- [Gate3DGen arXiv v1](https://arxiv.org/abs/2610.31649v1)
- [论文细节与作者实验](../papers/arxiv-2610.31649.md)
- [Adaptive Low-Light Enhancement for Road Anomaly Detection, 2026-11-05 v1（backfill）](https://arxiv.org/abs/2611.08393v1)；[HTML Tables I–II](https://arxiv.org/html/2611.08393v1)
- [T03/T06 总图](../LITERATURE_MAP.md)
