# AutoRef: Harness Optimization for Agentic Multi-Reference Image Generation

ID arxiv-2609.35530 | Yuta Oshima, Ku Onoda, Yusuke Iwasawa, Masahiro Suzuki, Yutaka Matsuo, Hiroki Furuta | T06 / T02,T04,X01 | harness search, planning, execution, selection | GO-E (historical anchor).
v1 2026-09-28, prior public evidence not exhaustive; already covered by at least 2026-11-17 (exact first coverage unknown); canonical backfill 2026-11-27. Not a new alert. Original selected §6,7 and Appendix I checked, not independently replicated.
目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)
## 快速回忆
固定生成器和推理模型，离线让编码agent修改可执行harness；训练反馈与验证选择分离，保留beam候选。在线将参考绑定写成prompt，两种布局组织的draft、一次定向修订、hard failure筛选及双顺序pairwise。
## 精读记录
Table4 held-out MultiBanana FLUX.2 klein 4B generator only 5.72, grounding only 6.91 (1生成), selection only 6.15, full 7.37 (3生成)。用重复采样替代complaint revision 得6.99，去结构多样draft得7.01，替换选择器得6.93。提示grounding单独取得约72%绝对增量，不能把比例当成模块独立因果贡献。等生成次数修订消融已存在，但没有按诊断正确性/具体错误消失/非目标变化拆分。
Appendix I Qwen-Image-Edit-2511 3/4/5 refs：5.06→6.95 / 4.44→5.69 / 1.89→1.87；五参考96例中87例三张候选均被hard-failure检查标记。这个统计是作者评价器的判定，不是独立人审的不可达证明。
## 证据边界
可达性、可发现性、可选择性不同。负例说明当前预算/控制下无法找到可接受候选；不能证明生成器理论上永远不可达。最小判别：固定首个失败输出、执行器/seed配对/三图预算与独立评价器，对照原prompt重采样、grounded prompt重采样、oracle准确诊断修订、结构条件适配；按具体错误纠正率和保护内容损伤归因。不是已经完成的实验。
## References
- https://arxiv.org/abs/2609.35530 ; https://arxiv.org/html/2609.35530v1 (Table4, §7, Appendix I)
- https://github.com/KuOnoda/AutoRef (原作者给出代码链接；未复现)
- [主专题](../surveys/multi-reference-executable-scene-control.md)
