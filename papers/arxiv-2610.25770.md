# VHA: VQA-based Hallucination Assessment for Generative Image Super-Resolution

## 快速回忆

- **首次公开**：2026-10-19（arXiv v1；按本轮可核验来源）
- **主题**：IQA / SR hallucination
- **核验范围**：full_paper_and_repository_checked；independent replication = not performed
- **一句话**：把生成式 SR 的 hallucination 变成可问答的事实差异：围绕 GT 与 SR 构造同一 taxonomy 的问题，以图像条件 log-probability 比较答案，再训练更轻的 VHA+。

## 精读记录

### 机制与证据

benchmark 含 90 张 GT、6 种 SR 方法产生的 540 对样本与 200 位参与者；双向 GT/SR QA 形成可解释的细节错误分数。VHA+ 学习该分数，作者仓库提供 benchmark/权重下载入口。

**证据范围**：全文、arXiv metadata 与作者仓库均已核对；下载入口可访问但未下载文件，未独立复现。

### 限制与竞争解释

需要 ground-truth reference，不是部署时无参考 detector；VHA+ 继承 VLM label 和训练分布。benchmark 由下采样 GT 构造，不能覆盖所有真实未知退化。

### 下一实验

在真实手机长焦/数字变焦上加入无 GT 的多帧一致性与 RAW 证据；单列文字、人脸身份、重复结构和品牌 logo 的事实错误。

## References

- https://arxiv.org/abs/2610.25770
- https://github.com/dhryougit/Hallucination-Assessment
