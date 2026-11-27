# Towards a Multimodal Aesthetic Agent for Photographic Reference Grading

ID: arxiv-2611.32299 | Kunjie Lin, Haitao Zhang, Bosheng Chen et al. (Xiamen University, Huawei Central Media Technology Institute) | T02 / T04,T06 | color grading, reference transfer, agent | GO-E | Executable parametric editing.
First verified: arXiv v1 2026-11-24; first covered/checked 2026-11-27. Front-page affiliation, methods, dataset construction, benchmark and selected result sections checked; no independent reproduction.
Decision key: reference aesthetics become editable photographic parameters instead of flattened generated pixels.

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [下一实验](#下一实验) · [References](#references)

## 快速回忆
- JarvisAura接收源图、参考图和自然语言意图，输出可继续编辑的摄影调色参数，避免像素生成器把结果压成不可逆平图。
- 三阶段为 PG-CPT 参数生成预训练、RG-SFT 参考调色监督微调、RA-GRPO 奖励对齐；配套 Ref-CPT/Ref-SFT/Ref-RL 与 Ref-Bench。
- 论文前页两位作者署名 Huawei Central Media Technology Institute；这只证明公司参与研究，不证明手机/图库产品采用。

## 精读记录
任务把“参考中哪些外观应采用”与“如何落到可执行参数”联合建模。训练数据通过可渲染参数和不精确指令动态派生，使模型能从最终图像反推并选择性迁移色调/色彩特征。作者报告 Ref-Bench 自动指标领先，人工任务成功率74%，较 GPT-Image-2.5 高9个百分点；需按原评审协议理解，不能跨 benchmark 横比。

## 证据边界
结果来自作者；参数空间覆盖范围、局部遮罩、HDR/RAW、不同显示与肤色群组泛化仍有限。动态合成数据可能让模型学会参数模板而非真实审美意图。人工成功率没有证明身份、文字、局部色彩或显示一致性。未给手机端 E2E、内存、功耗或产品部署；暂无明确权威社会评论。

## 下一实验
固定同一编辑器参数空间，比较图像-only匹配、语言选择、JarvisAura和专业调色师；按肤色、混合光、局部/全局意图、跨显示器和可逆性分层；验证参数重放是否严格一致，并记录模型拒绝不可靠参考的能力。

## References
- https://arxiv.org/abs/2611.32299v1
- https://arxiv.org/html/2611.32299v1
- https://github.com/baolinv0/CameraPaper/blob/main/raw/huawei/2026-11-27-jarvisaura-affiliation.md
