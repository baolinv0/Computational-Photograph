# Lost in Read-out: Locating the Image Quality Gap in Vision-Language Models with a Closed-Form Edit

更新：2026-11-19｜canonical arxiv-2611.22564｜arXiv v1 首传 2026-11-17｜11-18 官方 cs.CV new 公告｜首次覆盖 2026-11-19

主主题 **T04**；次主题 T06/X01/T02；系统角色：评价/表示读出/校准训练；地图变化：**New route + Boundary refinement + Counter-evidence**；裁决：**GO-E（评价机制诊断，不等于通用强 Judge）**。

目录：[快速回忆](#快速回忆) · [机制](#机制) · [证据](#证据) · [竞争路线与边界](#竞争路线与边界) · [系统方案与行动](#系统方案与行动) · [References](#references)

## 快速回忆

**去术语命题：**视觉语言模型对图像质量的中间表示可能含有足够质量信号，但最终自然语言读出没有把它正确投射成与人类评分一致的答案；因此失败未必发生在视觉编码器。

**机制区分**：感知表征的可分性、输出读出/校准以及最终的候选排序是三个不同环节。更改读出不能保证输入缺失的细节被识别，更不能替代候选可达性。

## 机制

对冻结 VLM 的 vision encoder/LLM 各层表示做 ridge linear probes；找出 quality MOS 信息在哪层存在并与回答的相关性比较。作者找到部分模型最后语言层能线性解码较多质量信息，随后根据 KonIQ MOS 和多种提示，对最后语言层的一个 neuron 做 closed-form edit，以改善 good-vs-poor 的最终文字打分。不需要微调整个模型，但需要标注 MOS 数据、训练期探测/拟合与模型内部激活访问权限。

## 证据

作者测 Qwen3.5 多个尺寸与 Gemma 变体，KonIQ、LIVE-C、BID、KADID 等数据。例：Qwen3.5-0.8B 在 KonIQ 的 Spearman 相关 0.642 → 0.800（作者的 matched prompts 条件），但大型模型读出可恢复空间较小，部分条件甚至出现下降。论文显示最后层 ridge head 对质量的相关性可以优于原始自然语言回答，证明有必要将“编码未看见”和“答案读错”分开诊断。百级别 MOS 标注可见改善；整体并非零监督方法。对图像质量之外的情感极性、其他问题格式可能出现副作用或不迁移。

## 竞争路线与边界

- Q-Align / 训练式 IQA VLM：通过监督改变能力；本作主张冻结视觉/语言主干，仅编辑激活读出。
- CLIP-IQA、NR-IQA：另一组独立特征与映射，不应以不同训练分布直接排名。
- EditJudge-Bench：编辑指令事实正确性；TrustUIQA：跨数据源人偏好与指标可刷分；本作评估单图质量 MOS 的可读出性。三者有共同评价可靠性问题，但不是同一标签定义或直接继承。
- **最强替代解释**：轻量线性校准头、训练集内风格相关、颜色/清晰度偏差和特定 good/poor prompt 本身造成收益。非等价于真实纹理保持、跨相机多区域修图指令完成、或任意输出格式可迁移。

## 系统方案与行动

- 离线：有 MOS 的原图 → 冻结 VLM 提取多层表示 → probe 定位信息位置 → 对照独立 scalar head 与 closed-form edit → 盲测不同 prompt/domain/小区域。
- 在线：图像 → VLM frozen vision/language →（可选）已校准的 quality read-out → 质量判断；还须独立证明对固定候选池的 pairwise winner 准确率与副作用。
- Agent：可以辅助候选选择，但这篇没有证明完整 image restoration agent 的闭环收益。
- **行动：GO-E 作为诊断路线，不默认更换 Judge。** 固定 VLM、标注预算、候选集，比较直接回答 / 末层 probe / edited readout 在同场景修图中的人工 winner 与伪细节错误率。

## References

- [arXiv v1 原文与附录](https://arxiv.org/html/2611.22564v1)
- [Q-Align 原文](https://arxiv.org/abs/2309.17012)
- [评价/Reward living survey](../surveys/artifact-grounded-reward-and-verification.md)
- [低光与跨来源 IQA 审计](../surveys/low-light-iqa-and-gt-validity.md)
