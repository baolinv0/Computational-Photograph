# Psychometrics-Inspired Coreset Selection for Image Quality Assessment

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [下一步](#下一步) · [References](#references)

身份：`arxiv-2611.24233`｜Susu Jiang, Xuelin Shen, Baoliang Chen｜arXiv v1 2026-11-18｜主题 IQA / T04  
核验：2026-11-20；原文方法、表1–2与数据拆分选段；代码承诺未落地核验；未独立复现。

## 快速回忆

- **问题**：IQA标注贵，通用视觉feature的多样性不等于质量空间多样性。
- **旧→新**：DINO语义/普通quality feature→用psychometric graded-response把latent quality、内容敏感度、失真阈值拆开，再与DINO融合做coreset selection。
- **记住**：5%标注预算下K-Center平均SRCC相对提升8.44%；但论文明确KADID upstream/downstream独立split仍可能共享reference或distorted samples。
- **下一步**：必须做reference-content严格去重和跨相机/跨处理链外推，才能判断是否真省人评。

## 精读记录

GRAM在合成失真上用severity ranking与content/distortion关系学习6维表示，不用MOS；随后用K-Center/Moderate/CD/PGCS选样，再对选中图片做人评并训练MANIQA/LIQE/DBCNN。九个数据集覆盖合成、真实和AI生成图；5%预算下对三种下游模型平均SRCC相对提升13.59%、6.55%、8.44%。

## 证据边界

方法依赖合成severity排序可代表人类质量顺序；真实相机pipeline、局部失真和观察条件未建模。结果并非所有数据/策略单项都提升。尤其KADID表注说明upstream与downstream split可能共享reference image或distorted sample，存在泄漏/近重复风险；代码仅称将公开。

## 下一步

按reference content、相机、场景和编辑链做group split；比较随机、DINO、quality-only、GRAM，并报告相同人评预算下的worst-domain SRCC/PLCC与置信区间。

## References

- [arXiv v1](https://arxiv.org/abs/2611.24233v1)
- [KADID-10K](https://database.mmsp-kn.de/kadid-10k-database.html)
