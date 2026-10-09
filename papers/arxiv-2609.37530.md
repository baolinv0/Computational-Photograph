# RawVLA：面向机器人操作的具身神经 ISP

- **身份**：arXiv:2609.37530
- **首次公开（已核）**：2026-09-29，v1
- **本次核验**：2026-10-09；selected sections checked
- **独立复现**：未进行

## 快速回忆

**问题**：固定 ISP 为人眼观感渲染，而冻结的 VLA 策略需要的是任务可用视觉；拍摄条件变化会直接伤害动作决策。

**机制**：输入 6 帧因果 RAW burst；固定 FFT 融合后，以分离的亮度/色度 GRU 建模时序，再显式预测曝光、白平衡、CCM 与共享单调 Bernstein tone curve，只训练约 0.887M 参数。

**证据**：作者在 LIBERO 报告总体成功率从最佳对照 43.01% 提升到 68.82%，训练说明为 A100 80GB、2,000 steps。该结果支持“下游任务可反向定义 ISP”，不支持手机摄影画质结论。

**决策边界**：输入是已 demosaic 的 linear RAW，部分数据来自 unprocessing/simulation；没有解决 demosaicing，也没有端侧时延、功耗、热或人类 IQ 证据。

**下一步**：把真实多机 RAW、传感器噪声和曝光漂移加入跨传感器留出集；同时报告任务成功率、颜色/保真度、能耗与失效案例。

## 精读记录

- **分层**：这是 capture-to-policy 的可微系统边界实验，不是通用摄影 ISP 替代品。
- **可竞争解释**：收益可能部分来自任务域自适应、小参数 recurrent front-end 或更合适的曝光训练分布，而非显式 ISP 控件本身。
- **产品/专利含义**：值得关注“任务目标约束 ISP 参数轨迹”及 burst-state/颜色状态的权利要求；部署前需与 fixed ISP + task adapter、RAW-native VLA 做等算力比较。
- **关联提醒**：对任何相机 agent / world-model 工作，先把“看起来更好”和“行动更成功”拆成两套 evaluator。

## References

- [arXiv abstract / v1](https://arxiv.org/abs/2609.37530)
- [作者项目页](https://shuhongll.github.io/rawvla/)
