# TRACE: Attribute Execution for Sequential Image Editing

更新：2026-11-23｜canonical: arxiv-2611.25648｜作者 Xiyang Zhang、Yuanhe Tian、Hongzhi Wang、Yan Song｜arXiv v1 首传：2026-11-19 07:32 UTC｜首次归档：2026-11-23（backfill，非新论文通知）
主 T06，次 T02/T03/T04；角色：目标状态/动作执行/候选验证；裁决 **PROBE**；地图 **Bridge + Boundary refinement**；核验：arXiv v1 正文 §1–4、Tables 1–5、Supplement S1–S2 选段；未核验作者代码，非独立复现。

目录：[快速回忆](#快速回忆) · [机制与证据](#机制与证据) · [竞争路线与判断](#竞争路线与判断) · [系统回忆](#系统回忆) · [References](#references)

## 快速回忆

**一句话命题：**连续编辑时应保留的是仍然有效的属性目标（如蓝色），不是以前承载该属性的旧图像表面（如玻璃）；必须在当前材质/结构上执行该属性，缺少载体时再有限调用生成器。

**例子：**把蓝色玻璃花瓶改为金属花瓶，历史蓝色应保留，但玻璃透明质感已失效；直接复制历史像素会把旧玻璃表面带回。仅靠找历史图片或精确区域 mask，并不能解决同一区域的属性冲突。

**记忆边界：**独特的 narrow color+material 联合保留有实证；一般完整多轮编辑 benchmark 收益小，且部分 source-disjoint 指标逊于更简单控制；不应宣称通用新系统显著优于所有历史基线。

## 机制与证据

- **目标状态**：记录仍然有效的 complete-request 属性；新指令替换旧值时要退休旧目标。早期编辑失败不表示目标失效。
- **当前载体（carrier）**：先用固定编辑器产生当前 proposal A；观测当前材质是否成立。若当前金属表面存在，则对 A 的当前 ROI 做色彩参数更新；若材质缺失，再用额外生成候选取得新载体，仅局部合成。
- **执行**：通过独立 SAM2.1 mask 绑定历史目标/当前载体，在 Oklab 上从历史图估计颜色中位数，再对当前图实施局部 chroma/必要 lightness 变换，附加 tonal endpoint calibration，背景保持当前 proposal。
- **准入**：对当前及适用历史 complete requests 做质量检查；仅满足要求的候选返回。失败可局部重试或有条件整图 fallback。模型参数冻结但外部 VLM/segmenter/额外图片生成增加系统成本。
- **实验设置**：冻结 FLUX.2 [klein] 4B（512²、4步）及 Qwen-Image-Edit-2511（1024²、40步）两类执行器；Qwen3-VL-32B 作为控制器，Qwen2-VL-7B 检查 request，额外 Qwen3-VL-8B 与 GLM-4.1V-9B target-blind 阅读外观。EdiVal 572×3 个编辑位置、MagicBrush 1053 独立编辑/535 session。
- **Table 1（窄任务）**：56 个先颜色后材质 conversation×2 seeds，Native Both 96/108，All-history 83/108；target-blind 双属性成功（8B）41/112 vs All-history 28/112；均属作者结果，不能互换为整体 benchmark 准确率。
- **Table 4（同一 proposal 控制）**：Core target-blind 22/112（8B）、18/112（GLM），直接历史像素 21/112、18/112，历史 chroma 26/112、29/112，完整 TRACE 41/112、45/112。该对照较好隔离“属性执行 vs 像素复制”，但同时含 carrier acquisition、calibration、adaptive retry。
- **Table 2（通用 EdiVal）**：Klein 第3轮 IF TRACE 31.12%，内部 Core 30.77%，ReSpec 29.72%；O 66.93 vs Core 66.87，**一般任务提升很小**。Qwen 第3轮 TRACE 43.01% vs Core 42.83%。
- **反例**：Supplement S2 source-disjoint Klein complete-request joint TRACE 60/125，而 Core 63/125、ReSpec 64/125；Qwen TRACE/Core 均 84/125。MagicBrush full own-history L1 TRACE .1313，而 All-history .1251；必须明确保持/执行存在 trade-off。

## 竞争路线与判断

| 路线 | 相同问题的机制 | TRACE 独立价值与限制 |
|---|---|---|
| 原图串行 / All-history | 用历史图与全部指令继续编辑 | 旧表面可能与当前材质冲突，简单方案在 MagicBrush 像素保持上仍可更好 |
| ReSpec / SEAM：历史引用/对象记忆 | 确定哪些目标和历史证据仍有价值 | TRACE 的额外贡献是历史属性在当前表面执行；作者引用/对照，不代表所有方法直接方法继承 |
| MT Forcing / TailSteer | 训练编辑器缓解长期 drift | TRACE 是冻结执行器外部状态管理和局部确定性算子；机制互补，不能拿不同设置分数比较 |
| ROI copying / mask compositing | 硬约束外部像素不变 | 不能仅靠 mask 解决 same-region material–color conflicts；简单基线仍需配平候选数与完整验证预算 |

**最强替代解释：**来自更明确的 active-goal prompt、额外生成修正图、独立 VLM 验收和更多算力，而非单独的颜色算子。因此应优先在固定同一 candidate A、历史证据、mask、生成次数与相同 Judge 下比较像素复制 / chroma transfer / calibrated transform / carrier acquisition。

**裁决：PROBE（局部可执行属性状态）**。局部强支持，通用外推弱；没有人类偏好、真实摄影保真或移动部署证明。不是本轮新论文；论文 2026-11-19 已在先前成功覆盖的 11-20 公告内，2026-11-21 backlog 指名待补。

## 系统回忆

- **目标/非目标**：连续指令当前和有效历史属性同时成立；不是提升 RAW ISP 或真实图像恢复的物理信息量。
- **在线输入→输出**：原图 + 新指令 + 有效历史目标/历史图 → 冻结生成编辑 proposal → 当前实体/材质检查 → 合格 carrier + ROI Oklab 参数变换（缺 carrier 才生成新图）→ 当前和历史完整要求验证→接受/重试/拒绝，输出最终 RGB。
- **离线**：原论文并不训练生成器或额外模型；定义规则、参数和任务，实验依赖已训练的视觉执行器及读出器。没有外部 clean GT 到在线。
- **评价与成本**：complete-request 检查、target-blind appearance readers、像素/语义保持、调用次数/总时延分开计；局部算子不是完整系统运行成本。
- **最小判别实验**：固定50例颜色→材质同区冲突和相同冻结编辑器/提案/编辑预算，比较历史像素回贴、历史 chroma、完整 calibrated/chroma+carrier；输出 joint instruction success、非目标泄漏、人工 winner 和 E2E latency。不要用原论文窄任务代替真实 restoration。
- **适用决策**：为 T06↔T02 建桥；若主要任务是单轮真实 IR/textural restoration，当前路线暂不改变。

## References

- [TRACE arXiv v1 2026-11-19](https://arxiv.org/abs/2611.25648v1)
- [TRACE full paper HTML](https://arxiv.org/html/2611.25648v1)
- [MT Forcing](https://arxiv.org/abs/2610.25404)
- [TailSteer](https://arxiv.org/abs/2611.06741)
- [多轮编辑长期专题](../surveys/multi-turn-editing-preservation.md)
