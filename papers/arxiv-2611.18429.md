# Do Underwater Image Quality Metrics Agree with Human Perception? A Benchmark with Human Choices, Simple Edits and Generative Drift

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [前序与竞争路线](#前序与竞争路线) · [证据边界与判断](#证据边界与判断) · [系统回忆与最小实验](#系统回忆与最小实验) · [References](#references)

**身份**：arXiv:2611.18429，Rishii Kumar Singh、Abhinav Rajput、Dinesh Kumar Vishwakarma（Delhi Technological University）。arXiv v1 首传 2026-11-13 17:10:13 UTC；进入 2026-11-16 cs.CV 新公告；首次覆盖 2026-11-17。作者提及 WACV 2027 Workshop 并非本次技术首次公开的依据。原文方法、统计、对抗测试、局限阅读；未独立重跑；更早公开材料未穷尽。

**主题/角色**：主 T04；次 T03/T05；评价 / Benchmark / reward stress testing。**裁决 GO-E（强评价反证和 benchmark 工程）**；地图 Counter-evidence + Boundary refinement。

## 快速回忆

**一句技术命题（去作者术语）**：对同一场景的水下增强版本，不能假定 NR-IQA 分数更高便更符合人的选择；先用人的配对偏好校验排序，再用简单重复调色、微弱对抗扰动和多轮生成漂移主动寻找指标被“刷高”的失败边界。

**旧→新**：单数据集 MOS 相关或 NR-IQA 的越高越好 → 跨实验室同场景 pairwise 排序、简单编辑/梯度攻击、生成漂移、指标实现审计的系统 benchmark。不是首次指出 NR-IQA 可被攻击，而是一个更具体的水下评估组合。

## 精读记录

- **对象与监督**：73 个 metric 配置（7 handcrafted underwater、7 learned underwater、2 VLM、57 generic，部分同模型的多个 checkpoints/子项）；四个公开 MOS 数据：UID2021 960 images/60 scenes；SAUD 1000/100；SAUD2.0 2400/200；SOTA 8000/800；加自建 32 场景×12 编辑、20 名参与者共 1920 次双选。SAUD 与 SAUD2.0 来自同实验室且重叠 33 场景，1160 是按数据集相加，不应称 1160 独立场景。
- **评价对象**：同一原始图的不同增强结果进行 pairwise winner，计算与人选择的 Cohen κ；这不同于跨场景全局 MOS Spearman，也不是物理场景辐射真值。
- **作者结果**：五组人类偏好中，所有配置最好的跨组最差 κ 仅 0.23（Q-Align）；自建同组人类评委 median κ 0.41，说明任务本身含主观分歧。若只在训练同源数据上评估，一些 learned underwater metric κ 0.60–0.92；其他实验室数据最多 0.31。
- **刷分**：饱和度/锐化/CLAHE 简单编辑可让 UCIQE 偏好人们拒绝的结果；10 步 PGD ε=2/255 在作者测试的 5 个可微评价器上全部成功，而非攻击过全部 73 个。
- **漂移**：Nano Banana Pro/Nano Banana 2 exact-copy 和 enhancement 链共 2800 图。Pro exact-copy 链 50 步噪声增加约 2.5×，73 个指标仅 22 个在各检查点单调降低；单调性只是此类序列的压力测试，不是“任意编辑都必须每步分数下降”的公理。
- **数据资产**：作者开源 TrustUIQA，包含基础偏好数据、简单编辑、攻击和生成漂移样本及 73 指标分数，利于复核。

## 前序与竞争路线

| 历史锚点/路线 | 方法作用 | 本文与其关系 |
|---|---|---|
| UIQM、UCIQE（传统水下 IQA） | 无清晰 GT 时用对比度/颜色/锐度代理质量 | 评价对象/主要负例 |
| URanker、Q-Align、NIQE 等 | 学习水下主观分数、VLM 评分及通用 NR IQA | benchmark 多类受测对象；模型 checkpoints 不等于独立模型 |
| gMAD、BAPPS、一般 NR-IQA adversarial studies | 挑选分歧图片、pairwise 人评、攻击评分器 | 既有机制前序，不可声称首创“人类对比或 reward hacking” |
| Banana100（2026） | 多轮生成自拷贝后分数与可见漂移脱节 | 同抽象、扩展到水下多模型多提示；不是相互独立的发明 |
| EditJudge-Bench（2026-11-09） | 已知 3D 编辑指令真值审计 VLM | **互补**：指令执行真实性，不等于主观偏好或观测保真 |
| LOL/颜色 GT 审计、NightIQA、UWNature v2 | 颜色目标差异、低光问题问答、合成真实性/训练效用 | **综合推断**跨主题连接，不能以此宣称已形成统一共识 |

## 证据边界与判断

**结果有效范围**：水下增强图片、指定公开数据集和小规模偏好补充；最大最小 κ 是作者数据中 73 配置的比较，并不是证明所有未来评价器不可能可靠。32 场景自建偏好数据中个体意见仍分歧，不能把任意一个偏好当唯一真实复原目标。SAUD/SAUD2.0 共享实验室，不能按五个独立来源计算共识。算法攻击比较固定指定模型并有访问其梯度的条件，不可直接外推所有闭源模型；模型版本影响漂移。

**更新判断**：单看 NR-IQA 排名、跨场景 MOS 相关或 reward 改进不足以说明真实候选选择可靠。加入跨来源**同场景候选比较**、人评上限、操作稳定性和对抗编辑压力测试。保持不变：主观自然度、人类偏好和像素真实性不是同一目标；更好的 Judge 无法解决 executor 缺乏正确候选的问题。

## 系统回忆与最小实验

- **目标/非目标**：审计评价器能否选出人偏好候选，及其被优化后是否易错；不声称直接提高任何恢复模型保真或可达性。
- **离线评估**：原图 + 多个增强候选 + 人评/MOS → 场景内配对 → κ / 鲁棒性测试（饱和/锐化/CLAHE、PGD、生成链）→ 指标适用条件和失败清单。
- **在线**：退化图 + 固定候选 → 数值/语义/结构证据 + 经审计的 IQA/Judge → 排序/拒绝；这里是可行的系统设计假设，不是 TrustUIQA 原论文实现的 restoration agent。
- **Agent层**：可达性/搜索可发现性/Judge 可选择性拆开；优化前要检查奖励会不会鼓励过增强。
- **简单强基线**：人类偏好多数投票 + 固定规则简单调色与 sharpen 候选；指标需击败 random and simple-feature ranker 且有独立域性能。
- **最小判别**：相同候选池、固定 20–50 场景的人工 pairwise 真值，分不同设备/光照/内容分层，比较 UCIQE/NIQE/VLM Judge 与人工的一致率；再施加单调加重的轻微过锐/过饱和，验证排名是否发生 Goodhart 反转，报告成本和人评一致性。

## References

- [论文 arXiv v1](https://arxiv.org/abs/2611.18429v1)
- [TrustUIQA 作者代码](https://github.com/TrustUIQA/TrustUIQA)
- [TrustUIQA 数据集](https://huggingface.co/datasets/TrustUIQA/TrustUIQA)
- [EditJudge-Bench](https://arxiv.org/abs/2611.12524)
- [T04 living survey](../surveys/artifact-grounded-reward-and-verification.md)
