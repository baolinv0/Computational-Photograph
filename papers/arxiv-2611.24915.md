# PrismRestore: A Compact Restoration Toolbox for Agentic Image Restoration

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [下一步](#下一步) · [References](#references)

身份：`arxiv-2611.24915`｜Zhaocheng Yu et al.｜arXiv v1 2026-11-18｜主题 Agent / Restoration  
核验：2026-11-20；原文方法、表1–8与消融选段；代码未核验；未独立复现。

## 快速回忆

- **问题**：多退化 Restoration Agent 的工具箱常要存几十个模型，规划器和执行器成本被混在一起。
- **旧→新**：多独立工具/adapter→从一个冻结 AdaIR 骨干按 activation+gradient response 搜索8组 channel modulation priors，再用 ResNet34+GRPO选择序列。
- **记住**：工具箱从多模型变成单骨干可调用动作是明确的工程增量；但 5 秒/图仍是桌面GPU级，真实集只以无参考指标验收。
- **下一步**：在同一骨干、相同调用数和相同 reward 下，比较 modulation action、adapter action 与简单 degradation-conditioned head。

## 精读记录

离线按八类单退化数据统计 channel activation/gradient，保留代表通道、搜索非代表通道调制系数，形成 prior bank。策略先SFT，再以分组归一的 fidelity/perceptual reward 与 stepwise return-to-go 做GRPO；在线每步调用同一骨干的不同 prior，NR-IQA不升即回退，最多6步。

MiO100三组中平均PSNR 21.14 dB，低于TIR-Agent 21.47、高于RAR 20.28；平均5.00 s/图。工具参数28.78M、planner约0.02B、平均4.65次调用；作者对比 AgenticIR 3579.67M工具参数与4KAgent 6205.92M。真实280图上以NIQE/MANIQA/CLIP-IQA/MUSIQ评价，未提供clean GT。

## 证据边界

训练为DIV2K/Flickr2K合成48种复合退化，真实集由LHP-Rain与RTTS挑选且只用无参考指标；reward与停止规则可被刷分。性能提升同时包含更好动作参数化、SFT、GRPO、reward设计和最终prior refinement，不能只归因“单骨干工具箱”。未报告手机端、功耗、显存与高分辨率；代码/权重截至核验未从原文确认可用。

## 下一步

1. 固定规划器、reward、调用数，仅替换动作参数化。
2. 加入原图KEEP、错误退化动作、NR-IQA攻击及真实配对/人评。
3. 在移动NPU友好骨干上测单步、平均轨迹和峰值内存，而不是只报参数量。

## References

- [arXiv v1](https://arxiv.org/abs/2611.24915v1)
- [AgenticIR](https://arxiv.org/abs/2507.03510)
