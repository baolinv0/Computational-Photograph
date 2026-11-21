# Fixing the Last Mile: Failure-Aware Image Restoration with Region-Specific Guidance (FAIR)
更新：2026-11-21｜canonical arxiv-2611.26456｜arXiv v1 首传 2026-11-19 17:21:15 UTC｜首次覆盖 2026-11-21｜作者 Hongyu An; Fanghua Yu; Kainan Yan; Luc Van Gool; Chao Dong; Jinjin Gu｜主 T03；次 T05/T06/T04；角色：目标/训练数据/执行/区域约束；GO-E；New route + Boundary refinement。

目录：[快速回忆](#快速回忆) · [问题和技术](#问题和技术) · [作者实证](#作者实证) · [评价边界](#评价边界) · [方案回忆](#方案回忆) · [References](#references)
## 快速回忆
一句命题：整图恢复近乎可用时，**局部人物/文字/纹理错误仍可使整体不可接受**；要在单次生成前同时指定“修哪里”和“依据什么真实信息修”，而不是整图统一先验。
与 SeeSR/SUPIR/HYPIR 的全图语义引导、ReFIR/AdaRefSR 的参考引导、ExplicitIR 的无外部参考空间策略场为互补/竞争路线，不等同直接方法继承。
## 问题和技术
输入 LQ 图、区域控制 R（phrase/bbox/outline/mask）、细节引导 P=(text, retrieved visual reference or Canny/identity)。离线合成退化、执行基准恢复、对照 clean GT 识别失败区域并检索参考；169,257 候选区域经筛查留下 66,989 训练区域。两阶段训练 FLUX.2-klein-9B，LoRA 条件共享，单步区域引导恢复。在线 LQ→失败区域检测/指定→查询参考/指令→区域绑定条件一次前向→整图；不等于无 GT 时自动知道真实字符内容。
**关键区分**：已知 clean GT/人工提供参考的模拟指导，是一个条件化能力实验；完全由 LQ 自动提供参考，才更接近真实无 GT 应用。

## 作者实证
- 120 region synthetic benchmark Table 1：FAIR FID 63.28、ROI LPIPS_in 0.0319、非目标 LPIPS_out 0.2429；最强参考基线 AdaRefSR FID 81.93、LPIPS_in 0.0368、LPIPS_out 0.277；但 AdaRefSR PSNR 21.23 > FAIR 20.91，不是所有像素指标SOTA。
- **oracle/辅助信息边界**：作者说明 synthetic 的参考通过 **clean GT 区域裁剪作查询**检索；使用 annotation-assisted instructions。相同 final checkpoint 下 generic Restore FID 71.79；完全 LQ-driven 67.97；annotation-assisted 63.28（Table4）。最好的 headline 包含优质参考来源的优势，不全来自执行器机制。
- 20名观察者×10案例，匿名9候选中 Top-2：FAIR overall 79.5% vs HYPIR40.0%，局部修正77.5% vs44.0%，保护78.5% vs45.0%；样本量有限，不是独立跨场景复现。
- 独立实测/真实无 GT：真实数据集 MUSIQ FAIR69.62而 CODSR69.93，不能称绝对胜出。WR-SR 作者报告端到端模型推理约3.16s/图，1024px上限，未包含实时手机采集/部署。训练阶段含32 H200，成本与1-step inference应分开。
- Table2 同框架分阶段/LoRA/region reweight：shared LoRA 训练 FID64.63，全文63.22（不同实验切分/口径别与Table1强行同数），主收益不能全归 region reweight。

## 评价边界
无参考时无法保证外部 crop 含目标真值；未知区域错误的鉴定可错；人物 identity/原字形如源观测丢失只能借额外可靠参考；源图保真与审美分开。论文报告文字 CER、Character recall、ArcFace 等附加指标，但 OCR 识别与真实字形不完全等价。强基线是同参考同 mask 的简单 ROI inpaint/composite、固定 Flux 模型和一般全图编辑，而不是无参考方法单独对照。

## 方案回忆
离线：LQ/GT/基线结果→失败类型/区域→参考/指令对应→单模型区域约束微调；在线：LQ+可核验参考/可见证据→ROI/文本/轮廓→单次输出→目标内成功、目标外保持、真假内容核验；Agent 若自检重试只是后续设计假设，不是本文已实施闭环。
**GO-E**：作为局部保真基准+区域执行表示值得归档；不重构现有 Agent。最小实验固定执行器、mask与总预算，比整图 prompt、同参考 ROI 融合、FAIR 条件化，分文字/人脸/纹理三个不可恢复类型人工评价。记忆：坏了的10%可决定照片失败；附加参考的内容来源才是可信度关键。

## References
- [FAIR arXiv v1，§3–4，Tables 1–5，Appendix](https://arxiv.org/abs/2611.26456v1)
- [局部选择与保留的连续路线](../surveys/selective-task-aware-restoration.md)
- [生成参考并非观测真值](../surveys/generated-reference-guided-low-light-restoration.md)
