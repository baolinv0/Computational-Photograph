# EditJudge-Bench: Auditing VLM Image-Edit Judges with Synthetic Ground Truth

- Paper ID: arXiv:2611.12524
- Authors: Jens Parslov, Marco Schouten, Dim P. Papadopoulos
- arXiv first upload: 2026-11-09 14:59 UTC, v1
- Publication: NeurIPS 2026 Evaluations & Datasets Track (author-stated on arXiv)
- First covered: 2026-11-13
- Main theme: T04 — IQA、偏好与可行动评价
- Verdict: GO-E
- Verification: full arXiv benchmark construction, main tables and category analysis checked; no independent reproduction.

## 30-second recall

1,382 组 Blender 前后图、九类可控编辑和精确 3D 参数把“编辑器质量”与“裁判是否看懂指令”分开。25 个 judge 配置里，VIEScore+GPT-4o 仅 69.0 AUROC，prompt 排布可造成 14.1 点变化；最佳开放模型仍明显低于人类。

## 完整系统回忆卡

- **数据：** 1,000 个室内场景；removal/addition、材质、光照、相机、移动、尺度、形状、关节、旋转九类；含方向错误、错对象、跨类型和 no-edit 反事实。初始 1,500 对中剔除 118 对。
- **结果：** 25 个配置；fine-tuned judges 51.7–66.3 AUROC；作者报告开放模型最高 81.0，前沿闭源最高 88.5；人类 multiple-choice 95.2%。形状/旋转和低显著 no-edit 是主要失败。
- **外部相关：** judge 排名与两个真实图人类偏好基准 Spearman 相关为 .95/.71；这是相关性，不是跨域等价。
- **边界：** 合成室内、确定性编辑；不覆盖真实生成伪影、身份/文字/风格保真；pointwise binary 不等同 pairwise preference；模型版本与 prompt 高敏感。

## 判断与下一实验

任何编辑 reward/verifier 上线前应先做可控反事实、输入顺序交换与 no-edit 测试。扩展时优先加入真实编辑器伪影、人物身份和文字不变区，而不是仅增加更多合成类别。

## References

- [arXiv:2611.12524](https://arxiv.org/abs/2611.12524)
- [Project page](https://jenspars.github.io/EditJudgeBench/)
