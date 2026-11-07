# OptIMerge: Optimization-Based Merging of Diffusion Models

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据与争议](#证据与争议) · [行动与方案](#行动与方案) · [References](#references)

- ID: arxiv-2611.07543；首次可核验公开：**2026-11-05**（arXiv v1）；source_version: **v1**；first_covered: **2026-11-07**；checked_on: **2026-11-07**。
- 作者/团队：Viraj Shah, Ashwini Pokle, Peyman Milanfar, Mauricio Delbracio, Hossein Talebi (Google)。
- 主主题：**T03**；次主题：X01 / T05；系统角色：训练、部署；地图变化：New route / Boundary refinement。
- Verdict：**GO-E**（研究价值/工程适用性分开）；核验范围：arXiv v1 HTML 方法与选定实验、未独立复现；尚未做全站更早公开检索。

## 快速回忆
**去术语命题**：对同一个底座分别微调的恢复扩散专家，不直接平均权重，而用少量配对样本校准跨专家的通道与卷积空间对齐，使单个合并网络覆盖多种退化。

**与前序关系**：Model Soups (Wortsman 2022)、Task Arithmetic (Ilharco 2023)、TIES-Merging/DARE 是明确引用的权重合并前序；UniRestorer++ 层级条件路由是竞争部署路线，不是方法继承。

## 精读记录
**输入→输出**：共享预训练 U-Net 的运动去模糊、离焦去模糊和超分专家权重 + 每任务100–500张校准图 → 一份多任务合并权重。不是按每张图片在线路由的MoE；推理依旧DDIM 32 steps，也不是低功耗ISP证明。

**离线**：冻结完整专家权重；只优化 attention 低秩特征对齐/偏置和卷积的 Cayley 正交旋转及融合系数，约3.2M可训练参数（相对890M U-Net <0.4%）；与 0参数均值、TIES/DARE、联合全参数训练对比。**在线**：退化输入→单合并扩散U-Net→输出；训练成本与单次推理成本区分。

**作者证据**：原文 Table 1 OID+DPDD: OID PSNR 简单soup 20.88、joint 22.59、Opt 22.72、单专家22.92；DPDD soup 23.15、joint23.37、Opt23.91、单专家23.39（每任务300 test）。但DPDD LPIPS Opt 0.2191 > 单专家0.2023（更差）；DPDD+DF2K SR 组合中 SR PSNR Opt 21.12 < joint 21.24。附录 Table3/4 证实 attention 对齐主增益，卷积旋转能进一步提升。

**最强替代解释与负例**：100–500样本+优化可能相当于小规模额外联合微调；不是零训练合并。PSNR改进依赖任务组合、校准采样和冻结底座；多专家长尾和跨相机RGB/RAW尚未验证。相对独立单任务专家仍有折中损失。

## 证据与争议
证据均来自作者报告，不能称独立重复验证；比较同输入、同监督/预算、同执行器后的实际收益才足以归因到该模块。跨设备/跨相机与真实部署尚需针对性验证。见上段具体反例。

## 行动与方案
保留为多个同底座恢复任务 checkpoint 的参数合并实验候选；若任务专用模型已经满足成本/质量，无需增设动态专家池。最小实验同样本预算比较简单平均、joint FT、LoRA微调和 OptIMerge。

**记忆锚点**：对同一个底座分别微调的恢复扩散专家，不直接平均权重，而用少量配对样本校准跨专家的通道与卷积空间对齐，使单个合并网络覆盖多种退化。

## References
- https://arxiv.org/html/2611.07543v1
- https://arxiv.org/abs/2203.05482 (Model Soups)
