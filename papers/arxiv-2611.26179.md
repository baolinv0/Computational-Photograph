# RegionAgent: Two-Stage Preference Optimization for Regional Image Restoration
更新：2026-11-21｜canonical arxiv-2611.26179｜arXiv v1 首传 2026-11-19 14:29:56 UTC｜首次覆盖 2026-11-21｜主 T06；次 T03/T04/T05；系统角色：策略/区域控制/训练/执行；裁决 PROBE；地图 New route + Boundary refinement。

目录：[快速回忆](#快速回忆) · [技术与竞争路线](#技术与竞争路线) · [作者证据与替代解释](#作者证据与替代解释) · [系统回忆与行动](#系统回忆与行动) · [References](#references)

## 快速回忆
一句命题：同一恢复动作的即时收益与其对后续动作的影响不同，区域恢复策略应当分别学习**单步组件选择**和**整轨迹反事实选择**。
不是首次提出区域恢复、Agent 工具调度或 DPO；真实增量为固定其他决策、只改变一项动作的偏好对与两级 DPO。离线偏好来自**带 GT 的算法评价**，不是人类修图偏好。关键问题是额外调用/合成条件收益能否归因于策略训练。
历史参照：[AgenticIR/MAIR](https://github.com/baolinv0/CameraPaper/blob/main/knowledge/imaging-agent/agentic-image-restoration-survey.md) 的工具规划；[RecurIR](arxiv-2611.18006.md) 的条件策略反例；[ExplicitIR](arxiv-2611.22222.md) 的网络内部策略场。上述为同问题竞争/互补，直接继承须依原文引用关系判断。

## 技术与竞争路线
- 输入：混合退化图 I_LQ；共享 OSEDiff-based restorer 先生成 Base，冻结 U-Net Localizer 提议区域；四个 LoRA 专家、mask 和局部融合组成动作空间。
- 离线：在同一当前状态比较只改变动作一个参数的局部候选，以 PSNR/SSIM/LPIPS（需 clean GT）及 MANIQA/MUSIQ/CLIP-IQA、成本、泄漏惩罚构造 step preference 10K pairs；完整轨迹只改一动作构造 trajectory preference 20K pairs。Qwen3-VL-4B SFT→step-DPO→trajectory-DPO。
- 在线：Base→当前状态/ROI→VLM 选区域+专家+强度→执行与融合→再判继续或 STOP，最多8个 REFINE；没有在线 GT。评估信息预算与训练时 GT oracle 严格区分。
- 可达性：四 LoRA 专家是否有更好结果；可发现性：DPO 是否更会选；可选择性：推理时有没有可观测反馈。论文不能用总体性能为三个接口同时背书。

## 作者证据与替代解释
- MiO100 Group C 同执行器/推理上限的策略训练消融 Table 3(a)：SFT 20.01 dB；step-DPO 局部组件 20.47；直接 trajectory-DPO 20.37；两级完整 20.90 dB。两级相对仅 step +0.43 dB，平均 REFINE 从7.61降至7.12；不能把相对 SFT 的0.89 dB全归因轨迹优化。
- Group A Base 21.34→完整22.11 dB；有竞争方法在部分指标更优，如 RAR 的 LPIPS 0.1299 vs 本文0.2377。作者 Table 1–2 涵盖混合/单一退化，主要是有 paired GT 的 benchmark。
- 推理约18.60秒/图，A100，峰值显存9.28GB；模型单次执行耗时≠完整系统成本。
- 反解释：合成/混合退化是否贴近真实 ISP？新增专家池、局部 mask、融合与更高预算是否使最终提升；全参考 GT-derived reward 对真实无 GT 策略的迁移不明。未对真实手机 RAW、无 GT 人工偏好进行端到端独立复现。
- **价值**：训练条件化区域策略的可归因控制比较；不是“VLM 懂图更强”的独立证明。没有构成多团队共识。

## 系统回忆与行动
离线：clean+synthetic LQ→工具试验→组件级/轨迹级偏好→DPO 策略；在线：当前图+mask→选择区域/专家/强度→局部执行→评估停止。Agent 控制层决定动作，固定执行器产生候选，评价能力仍需独立核查。
**当前判断 PROBE：** 保留已有直接恢复/等预算 Best-of-K 强简单基线。最小试验固定专家与最多执行次数，比较 SFT、step DPO、trajectory DPO、两级 DPO，报告未见退化、越界区域损伤、人工/GT winner 与完整时延。
记忆锚点：一步看似改进的 ROI，可能破坏下一步可恢复性。

## References
- [论文 arXiv v1（§3–4、Tables 1–3）](https://arxiv.org/abs/2611.26179v1)
- [AgenticIR survey](https://github.com/baolinv0/CameraPaper/blob/main/knowledge/imaging-agent/agentic-image-restoration-survey.md)
- [选择性恢复路线](../surveys/selective-task-aware-restoration.md)
