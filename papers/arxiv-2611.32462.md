# MAGPIE: Agentic Multi-Reference Image Generation via Executable Scene Construction

ID: arxiv-2611.32462 | Yifan Dai, Daili Hua, Bohan Zeng et al. (SJTU, PKU, KlingAI Research and collaborators) | T06 / T02,T04,T05,X01 | planning, execution, training, verification | GO-E | New route + Boundary refinement.
First verified: arXiv v1 2026-11-24; 11-25 new listing; first covered / checked 2026-11-26. Earlier disclosure not found by exact title search, not exhaustive. Selected original methods/results/appendix checked, no independent reproduction.
Decision key: executable geometric proxy plus matched generator adaptation; not universal zero-shot guidance.

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)

## 快速回忆
- 将多参考图的对象与空间意图转为可执行 Blender 简化场景，在生成真实感像素之前验证实体、位置、遮挡、接触。再将灰模渲染与原始参考联合输入生成器。
- 与 AutoRef 冻结双模型、搜索 harness 代码不同，MAGPIE 在线修订场景程序，离线还需训练 LoRA 使生成器读懂 proxy。Scone 是有作者/数据/benchmark 联系的前序；AutoRef 为竞争/共同抽象，不宣称直接继承。
- 适合复杂几何组合，不直接用于仅纹理、色彩或风格编辑；其训练筛选明确排除纯外观变化。

## 精读记录
在线：参考+指令 → Qwen3.8-flash 生成实体/参考/关系规格 → Blender 程序 → 渲染+几何检测（mesh ID、投影 bbox、可见性、深度、接触距离）+ VLM review → 修改代码，最多6轮 → proxy+参考+指令 → Qwen-Image-Edit-2511 或 FLUX.2-klein-base-9B LoRA → 结果。几何和视觉验收作用于 proxy；最终像素不受硬约束。
离线：已有多参考数据（Scone等）按目标可结构化程度筛选，使用训练 target 辅助构建/过滤 proxy，3187 对；rank32 LoRA 5 epochs，1024以内，base 权重冻结、adapter训练；测试时仅参考和指令。
Table 3 DreamOmni2 overall (%), Qwen base 42.01 / proxy-only 29.47 / standard SFT 44.83 / full 64.26; FLUX 38.87 / 46.08 / 48.90 / 67.08。SFT 使用相同样本不含 proxy。增量主要需 guidance 与适配配合；不能把 28.21pp 全归于 agent。Table 4 FLUX generation text 58.77 / 2D box 47.37 / 3D 67.54（分别训练 adapter）；不是冻结模型通用证明。
Appendix Table 8，固定 adapted FLUX，0/3/6 refinement: 53.61/61.13/67.08 overall，proxy time 76.97/211.44/272.17s。
Appendix Tables 6–7 SconeEval，FLUX base 8.07，人工 best-of-six 8.42，full 9.05，估计预算418.56 vs 415.77s（未计人工筛选及未计时 orchestration）。Qwen 8.22/8.54/8.93。支持并非仅增加采样，但未隔离训练与结构的所有贡献。FLUX full 415.77s/例为已计时阶段和；非手机时延。

## 证据边界
原文作者报告，不是独立复现。benchmark 自动评估、训练样本筛选与 target-assisted proxy 可能限制域；不能把 proxy 成功等同像素身份/事实保真。无外观-only证据；真实恢复既有构图不应被新几何替换。最小对照固定目标/训练样本/adapter预算，比较无 proxy、文本/2D/3D proxy、同预算搜索，独立评审身份和关系。先测试冻结 executor 对条件的可达性，若负收益不扩搜索。代码权重实际可用性待核。
## References
- https://arxiv.org/abs/2611.32462v1 ; https://arxiv.org/html/2611.32462v1 (§3–4, Tables 3–4,6–8, §7)
- https://arxiv.org/abs/2609.35530 (AutoRef, Yuta Oshima et al., 2026-09-28; historical anchor)
- https://arxiv.org/abs/2512.12675 (Scone, 2025-12-14)
- https://arxiv.org/abs/2605.18451 (Code-as-Room, executable scene as output not 2D conditioning; abstract-level)
- [主专题](../surveys/multi-reference-executable-scene-control.md)
