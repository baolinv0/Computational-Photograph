# CRIE-Agent: What Stays in the Picture? From Redundant Instructions to Dependency-Aware Image Editing
更新：2026-11-24｜canonical arxiv-2611.27388｜2026-11-20 v1 首传；11-23 arXiv 新公告；首次覆盖 11-24。主 T06；次 T02/T04/T05；角色：意图、计划、验证、benchmark；PROBE；Bridge + Boundary refinement。
目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)
## 快速回忆
- 一句话：先从冗长、含撤销和引用关系的单次请求还原最终有效意图，再按对象依赖顺序执行和检查。
- 不等于 TRACE 的跨真实轮次属性状态保持；不等于 AUTOREF 多张外部参考图绑定。这里主要是同一次请求中对象之间的引用依赖；与二者的联系是综合推断。
## 精读记录
- CRIE-S 基于 Style30K，10000 条，9000/800/200 train/val/test。训练意图解析模型；推理将请求整理成 final object goals → reference-first DAG 分块 → 编辑器执行 → VLM 验证；失败可从原图重试而非无限累积生成结果。
- Table 2 单步 VLM 重组 5.5% vs 训练意图解析 11.0%（完全成功）；Table 3 Qwen-Image-Edit2511 完整 39.5%，加入验证的阶段 21.5%，布局阶段 26.5%；Table 4 K=2 同块上限 random 23.2±1.4、left-to-right 30.8±1.2、reference-first 39.3±4.3。
- 五个后端在该困难测试中作者报告完整成功率从 0 到 27.5–50%，为自动 VLM 核验的全部条件通过率，不是人评；替代 GLM 核验提供有限支持。
- 外部 CompBench 两对象任务中 Qwen-Image-Edit2511 的 foreground alignment 有小幅变差；直接一次编辑与分块、重试未配平执行次数，完整成本含 VLM/规划/验证，不能只数编辑调用。
## 证据边界
已核验 v1 方法和表2–4/外部评估；无独立复现。数据为合成的复杂指令而非真实用户自然分布。强基线：只解析最终意图、reference-first 与随机/空间顺序、同候选预算、同 verifier、独立人工评价；单独测未编辑内容/颜色泄漏。适合把意图状态与调度分开，暂不证明图像恢复执行能力提高。
## References
- https://arxiv.org/abs/2611.27388v1
- [TRACE](arxiv-2611.25648.md)
- https://arxiv.org/abs/2609.35530 (AUTOREF, 历史锚点)
- [多轮编辑与保真专题](../surveys/multi-turn-editing-preservation.md)
