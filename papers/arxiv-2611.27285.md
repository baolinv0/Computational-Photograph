# SIR-Agent: Skill-Augmented Image Restoration Agent with Recursive Self-Improvement
更新：2026-11-24｜canonical arxiv-2611.27285｜2026-11-20 v1 首传；11-23 arXiv 新公告；首次覆盖 11-24。主 T06；次 T03/T04/X01；角色：技能策略、修订、评价、成本；GO-E；Engineering maturity + Boundary refinement。
目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)
## 快速回忆
- 一句话：不只更新恢复技能，还更新怎样修订技能的外部规则，使用过程反馈定位出错的工具，同时回放旧任务阻止遗忘。
- SkillIR 是初始技能构建的明确前序；RecurIR 是主动构造反例、学习何时修订的竞争路线；RegionAgent 同作者线索但学习 DPO 策略权重，本篇更新外部技能/规则；AutoRef 是外层 harness 优化的共同抽象，不宣称直接继承。
## 精读记录
- 离线初始 PaAgent 训练样本工具试验→有效轨迹→条件、顺序、工具配置；在线执行冻结 MLLM（论文称 Qwen3.8-Max）与工具。新任务适配检查中间结果和链路反馈、检索候选替换可疑工具、保持动作顺序；回放旧任务，收益与 regression guard 约束覆盖，必要时保留分支。修订日志供 MLLM 生成新的外部修订规则，在验证上按收益、成本和旧任务退化选取。
- Table 5 新 desmoking 固定技能 13.45→固定修订规则 15.62 dB；旧 CDR 24.55→24.51；移除 regression guard 旧 CDR 23.88。
- Table 6 result-level→chain feedback：14.78→15.62 dB；26.8→19.6 tool calls。Table 7 固定→递归修订规则：新任务 15.62→16.00，旧 CDR 24.51→24.55，19.6→13.4 tool calls，24.8k→17.1k tokens，均为每次修订而非每图推理时延；去掉成本偏好 15.96 dB/18.4 calls。
- 机制价值：把工具可达性、技能发现、评价接受与元修订分离。收益主要是适配阶段的搜索/修订效率和旧技能保持，而非训练新图像执行器。
## 证据边界
已读 v1 方法和表5–7，作者实验非独立复现。七未见任务含适配，不是纯 zero-shot；初始工具遍历成本、评价 Q 来源及独立新旧验证充分性需要继续核对。相同工具池、候选次数、反馈信息、评估器下的简单固定规则/穷举、随机替换是必要基线。无真实手机部署或真实用户偏好结论。最小实验：固定工具池、数据、初始技能与独立评估，比较固定修订规则和可更新规则，报告可达上界、修订成功率、旧任务退化率、总调用与总 token。
## References
- https://arxiv.org/abs/2611.27285v1
- [RecurIR](arxiv-2611.18006.md)
- [RegionAgent](arxiv-2611.26179.md)
- [AgenticIR canonical survey](https://github.com/baolinv0/CameraPaper/blob/main/knowledge/imaging-agent/agentic-image-restoration-survey.md)
