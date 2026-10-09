# UniSlider：感知均匀的连续图像编辑滑杆

- **身份**：arXiv:2610.06831
- **首次公开（已核）**：2026-10-05，v1
- **本次核验**：2026-10-09；selected sections checked
- **独立复现**：未进行

## 快速回忆

**问题**：生成式编辑的数值 strength 往往不是单调、也不是感知等距，导致产品滑杆出现跳变、平台区和身份漂移。

**机制**：以轻量 LoRA 促进编辑轨迹单调，再用 DreamSim proxy 驱动自适应采样，把内部强度重映射为感知更均匀的 slider。

**证据**：作者构造 300 个连续编辑 benchmark，覆盖 uniformity、monotonicity、edit fidelity、identity preservation，并进行 15 人偏好研究。

**决策边界**：proxy 与真实感知并不等价；基础模型失败会沿轨迹传播。论文示例在 RTX Pro 6000 上生成 11 帧约 7.02–7.16 s，不是移动端交互时延。

**下一步**：在肤色、年龄、身份、文字和局部编辑上做多观察者 psychometric calibration；比较固定采样、isotonic mapping 与用户个体化映射。

## 精读记录

- **产品含义**：连续编辑应被当成“校准问题”，而非 UI 线性插值；可把感知 JND、单调性与身份安全做成独立验收项。
- **竞争解释**：改善可能来自 LoRA 轨迹平滑或采样重排，需分离二者贡献。
- **风险**：如果 evaluator 偏好流畅而非忠实，滑杆会把系统性偏差包装成均匀体验。

## References

- [arXiv abstract / v1](https://arxiv.org/abs/2610.06831)
- [作者项目页](https://color.cvc.uab.cat/unislider/)
