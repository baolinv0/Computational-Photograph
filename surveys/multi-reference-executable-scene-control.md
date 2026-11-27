# 多参考图像生成：参考绑定与可执行空间控制
T06 主 / T02,T04,T05,X01 | 2026-11-26 初建。与 [CameraPaper AgenticIR](https://github.com/baolinv0/CameraPaper/blob/main/knowledge/imaging-agent/agentic-image-restoration-survey.md) 互补；不是另一套恢复 Agent 总综述。
## 问题边界
输入多张参考+意图，输出满足指定主体/外观/相互关系的图像；区分选择哪个对象、长什么样、放在哪里、如何接触。非目标：真实恢复中的不可见事实重建或色彩-only修图。
## 竞争路线
| 路线 | 在线输入→控制→输出 | 训练/证据/失败 |
|---|---|---|
| Scone (2025-12-14, CVPR 2026) | refs+instruction→understanding expert→generation expert | 训练语义对齐/attention mask；SconeEval distinction 与 composition；不是外部几何执行 |
| [AutoRef](../papers/arxiv-2609.35530.md) (2026-09-28) | refs+instruction→优化后 harness→冻模型生成及诊断选择 | 离线 coding agent 搜索 harness、proposal/selection split；无 adapter 训练；不同 benchmark 与 MAGPIE 不可横比 |
| 文本/2D layout | refs+instruction→实体文字或 bbox→生成 | 表达遮挡、接触、姿势受限；MAGPIE Table4 分别适配对照 |
| MAGPIE (2026-11-24) | refs+instruction→Blender proxy program→几何+视觉检查/修订→render+refs→适配后 generator | target-assisted 3187对训练，LoRA；Table3/8 支持条件适配和场景修订；外观-only排除 |
| [LayoutRecall](../papers/arxiv-2611.33885.md) (2026-11-25) | current image + calibrated layouts/camera + history → box-local appearance tokens → adapted editor | historical observed appearance, not unseen geometry; per-op LoRA; returning objects and views, not arbitrary reference binding |
| Code-as-Room (2026-05-18) | top-down reference→Blender program→3D room | 相邻可执行表示，3D是最终输出而非2D生成条件；仅摘要核验 |
## 证据与判断更新
[新 MAGPIE 卡片](../papers/arxiv-2611.32462.md)。DreamOmni2 FLUX base 38.87, standard SFT 48.90, proxy only 46.08, full 67.08；Qwen proxy only 42.01→29.47 是反例。固定 adapted FLUX 0/3/6轮 53.61/61.13/67.08；SconeEval 同近似计时预算 best-of-six vs full 8.42/9.05。不是统一冻结 harness 的证明；人工选择时间未计。3D 先验不是新独立物理测量，也不保证最终生成准确。
旧判断：外层 harness 优化可改善多参考输入解释和候选选择。新判断：可检查中间状态（geometry proxy）是独立控制轴，但执行器对该表示的可读性是必要条件；有些模型 zero-shot 退化。不变：可达/发现/选择分开，几何验收不能替代像素验收。
## 2026-11-27：历史证据怎样绑定到移动的物体？
旧地图关注“参考是谁、放在哪里”。LayoutRecall 增加跨轮证据可用性：正确布局不足以恢复已经退出当前画面的物体外观。与 MAGPIE 的当前空间目标可执行验证互补，与 AutoRef 的参考解释/候选搜索处于不同控制轴。没有直接继承证据。
- **BoxCtrl / Thinking in Boxes**（2026-06，原摘要与后者项目页核验）：用户源/目标3D框给定几何变换，前者合成SFT+真实RL，后者合成场景+Objectron训练；为 LayoutRecall 直接引用和实验基线，不声称后者继承代码。
- **LayoutRecall**（11-25 v1，11-26 公告）：给定相机/3D框，SAM3+射线把历史VAE token寻址到物体ID和局部框表面，按目标视角投影；操作专属LoRA和匹配attention训练；非通用多参考生成。Table5 synthetic ten-round Back PSNR full/last2/no mem=23.75/19.18/15.71 dB；Table3 SeeThrough3D编辑成功率0.816高于LayoutRecall 0.732，保真与编辑成功仍存在 trade-off。真实COCO仅10条十轮，Back比较历史而非真实新视角GT。
- **AutoRef 旧锚点补齐**：Table4等3生成预算去complaint revision 7.37→6.99（以同prompt采样替代），因此不能说论文完全没有等预算修订对照；尚缺按诊断准确率与目标错误修复率拆分。Appendix I Qwen五参考1.89→1.87且87/96全部候选被hard-failure标记（作者判定）；候选可达、发现、选择独立。
判断变化：几何proxy不仅可作目标控制，也可作历史证据索引。关键区别是目标状态、历史观测、生成器对证据的利用三者独立。当前最强替代是同历史token/训练预算的原始参考检索；旧图可能被生成错误污染，不能把回忆等于事实恢复。
在线独立分支：已知布局+当前图+历史→对象绑定→重投影token→适配生成→写回；离线GT两编辑序列+对应监督；可选Agent判断历史是否可信再写回（设计假设，原文无独立验收层）。不将这些路线拼成已验证系统。GO-E：仅针对反复空间编辑。无手机、通用多参考或真实恢复增益证据。
## 完整系统与行动
目标由指令/引用关系定义；在线 parse→结构控制→候选→独立评价；离线从数据筛选/结构监督训练 adapter 或独立 harness 搜索；Agent 控制层独立记录 proxy 失败和 final output 失败。成本分别统计构造/校验/生成/人工，不能只报 generator。最小测试 fixed refs/target/seed/train budget，先无 proxy vs frozen proxy，再与适配、2D及等预算 sampling对照。若目标只涉及 texture/color，不使用几何 proxy。GO-E for structural composition only.
## 缺口
MAGPIE 代码/权重实可用性、正式人评 final fidelity、开放多参考冲突、与 AutoRef 同数据同预算匹配、ContextGen/ConsistCompose/SeeThrough3D 原文及 NVIDIA 3D-guided blueprint 实现；这些是 backlog，不是独立复现或新作。历史锚点不占新增名额。
## References
- https://arxiv.org/html/2611.33885v1 (LayoutRecall)
- https://arxiv.org/abs/2606.23270 (BoxCtrl, abstract)
- https://arxiv.org/abs/2606.20556 (Thinking in Boxes, abstract)
- https://arxiv.org/html/2609.35530v1 (AutoRef, Table4/Appendix I)
- https://arxiv.org/abs/2512.12675 (Scone)
- https://arxiv.org/abs/2609.35530 (AutoRef)
- https://arxiv.org/html/2611.32462v1 (MAGPIE)
- https://arxiv.org/abs/2605.18451 (Code-as-Room)
