# Reading the Unreadable: Text-Aware Image Super-Resolution Needs Reasoning

身份：`arxiv-2611.15449`｜Jaeseong Lee, Jinwoo Kim, Jinho Jeong, Seon Joo Kim（Yonsei University）｜NeurIPS 2026｜主 T03，次 T04/T06/X01
首次 arXiv v1：**2026-11-11 13:19 UTC**；早于此的公开实验产物：ReasonText-SR-outputs（第三方存档 2026-10-28 已收录，记录其来源创建日期 2026-08-04；官方提交历史未直接核实，**不得将该日期当作论文全文首次公开**）。
首次进入 Watch 记录：2026-11-14（pending chronology）；本次 canonical backfill：2026-11-16；核验：arXiv v1 HTML 的 §2–6、Tables 1–4 与附录选段、作者 GitHub/HF 公开产物，未复现。
裁决：**GO-E / backfill, not a new-paper alert**；系统角色：evaluation benchmark、inference evidence、execution conditioning；地图变化：**Boundary refinement / Bridge**。

目录：[快速回忆](#快速回忆) · [机制与前序](#机制与前序) · [证据审查](#证据审查) · [系统边界与行动](#系统边界与行动) · [References](#references)

## 快速回忆

- **无作者术语命题：** 文字像素本身不够时，外部场景线索可以帮助推断字词，再把推断结果交给具文本条件的超分模型；但“猜对字”与“把字正确画出来”是两个独立瓶颈。
- 旧：整体 PSNR/LPIPS/NR-IQA，或把 scene text 作为局部超分区域。新：按是否需要上下文推理标注文本实例，独立评价精确字符，并在推理侧注入 MLLM 文本证据。
- 记住：**contextual plausibility ≠ pixel-grounded factual certainty**；识别正确 ≠ 渲染正确。
- 行动：保留 text ROI 的 GT OCR + 无 GT OCR 两套评价，以及字符不允许猜测/允许推断两个运行配置；最小预算归因先检查文字生成质量，再讨论 Judge 或 Agent 策略。

## 机制与前序

**任务和输入输出：** 输入严重退化的 LR 自然图像，输出 HR 图像，期望恢复可读、与 HR 转录一致的文字。ReasonText 使用 513 对 LR–HR 自然图及 3,985 个文本实例；主要实验仅用 Level 1 可局部读出 1,754 与 Level 2 借助上下文 709，Level 3 不可读 1,522 排除主统计。不同文字实例标签来自有限的人类读者，不能等同信息论上的可恢复性。

**评价：** GTTCA 使用人工 GT polygon 裁剪重定向 SR 文字，再调用 OCR 比对 GT transcription；避免检测框漏检干扰，但使用 GT 定位是 Oracle 输入，不能作为无 GT 部署运行时直接指标。HR 图像的该 OCR 指标也未达到 100%，量化其测量上限。

**执行：** 固定原有 SR backbone，仅用 Gemma 4 31B 在 LR 全图上结合上下文推断文字并输出 caption，替换六类 text-conditioned SR 模型默认 caption。论文控制对照固定预生成的一条 caption、相同 SR 模型流程，测试于 H200；不是模型训练改造，也不是单帧实时 ISP。

**直接对照与历史锚点（已在本文 Related Work 引用，尚未逐篇独立精读）：**
- 2021 Scene Text Telescope / 传统文本检测+局部复原：强调视觉和几何文本区域。
- 2025 DiT4SR、FaithDiff：real-world SR / faithful generation，是非特化 SR 对照。
- 2025 TeReDiff、UniT：text-aware SR，用文字感知模块指导超分。论文作者有引用，但不能仅凭后发判断 RTC 直接继承其方法。
- 与 [VHA hallucination 审计](arxiv-2610.25770.md) / [EditJudge-Bench](arxiv-2611.12524.md) 是分析者的**评价边界连接**，不是相同数据集的公平效果排序。

## 证据审查

**主要证据（作者 Table 1/3/4）：**
- 12 个 baseline 中，Level 2 GTTCA 远低于 Level 1；作者指出 Level 1 最差 baseline 45.7% 仍高于 Level 2 最好 24.5%。
- Gemma 4 31B 在 Level 2 上的 transcript recall：不要求推理 45.84%，要求推理 70.38%；只保留目标文字、遮去场景时跌到 29.90%，支持周围线索重要，但不能完全排除训练泄漏/语言先验。
- 同一 DiT4SR 输入流程，仅更换 caption：Level 2 GTTCA 24.54% → 45.84%；六个 text-conditioned backbones 均有作者报告改善。
- **独立瓶颈：** 即使有 GT transcript，最高相关模型在 Level 2 仅 47.70%，明显低于 HR oracle 90.69%。文字推理正确不保证 SR renderer 忠实执行。
- PSNR/LPIPS/NR-IQA 并非单向一致：如 SUPIR Level 2 22.57→38.79，但 PSNR-Y 24.30→23.95。不能把 OCR 增益等同全图真实保真。

**关键争议与替代解释：**
- Dataset 只有 513 对、以 alphanumeric 为主，Level 3 标签依赖标注群体；外语、罕见文字、隐私号码、无法由局部像素唯一确定的字符串有不同风险。
- GT polygon 消除了 detection error，因此 GTTCA 是**定位后识别准确率**；真实不带 GT 的系统需要独立检测与定位。
- 图像上下文可能改善模型猜测，也可能生成自信但错误的新字符。作者仅展示数据集 GT 统计，不验证司法/真实性要求或无真值保真。
- “training-free”仅指无额外 SR/MLLM fine-tuning，依然需要额外 31B MLLM 与 SR 前向；未给出手机端 E2E/能耗验证。GT transcript oracle 和未做的人工双盲保真审查不能混同。

## 系统边界与行动

**离线：** 原始照片/标注 GT 字符 → 依据局部/全局证据标定可读性 → 分离文字准确率、非文字质量、可信度/伪字率测试集；评测要包含原图罕见字符串与上下文诱导错误。

**在线（作者方案）：** LR → 外部多模态文本推断 → caption → 固定 text-conditioned SR → HR；**可选工程设计，尚未由论文验证**：推断文字作为 unverified suggestion，原始可见字符与确证 OCR 作为保护边界，最后以可验证字符和结构审核是否提交。

**强简单基线：** 原 SR 默认 caption / 不带推断、普通 OCR caption / 同算力更强 OCR / GT transcript oracle 仅作上限。分别测 GT 文本保真（有真值）、无 GT 的 OCR 可读性、人评事实性和完整 E2E 耗时。

**可达性**受 renderer 限制；**可发现性**是 caption 或候选搜索能否获得正确字符；**可选择性**是评审能否区分真实字符与合理幻觉。这篇论文只给三者中的部分证据，未证明端到端 Agent 可靠。

**最小判别实验：** 取同一组含可核验文字的 LR，固定 SR backbone、seed、推理成本记录，对比默认 caption / OCR caption / MLLM reasoning caption / GT transcript oracle；分离 recognition-input accuracy、output GTTCA、非文字 leakage 与 SR 总成本。高风险文本目标要求“不造字”，合理可读但无证据字符应算失败。

## References

- [arXiv v1 论文与 HTML，§2–6 / Tables 1–4 / Appendix C–D](https://arxiv.org/html/2611.15449v1)
- [项目及代码](https://github.com/jasonleex1995/TAISR_needs_Reasoning)
- [ReasonText benchmark](https://huggingface.co/datasets/Jasonleex1995/ReasonTextDataset)
- [作者公开模型输出](https://huggingface.co/datasets/Jasonleex1995/ReasonText-SR-outputs)
- [第三方 HF 历史快照（仅用于早期 artifact chronology，非论文首发证明）](https://silytics.si/datasets/Jasonleex1995/ReasonText-SR-outputs)
- [Scene Text Telescope 2021 / DiT4SR 2025 / TeReDiff / UniT 的原始引用信息](https://arxiv.org/html/2611.15449v1#S2)
