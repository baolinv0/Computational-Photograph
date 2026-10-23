# RAW-Diffusion: RGB-Guided Diffusion Models for High-Fidelity RAW Image Generation

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)

- **ID**：`arxiv-2411.13150`；**简称**：RAW-Diffusion
- **作者**：Christoph Reinders; Radu Berdan; Beril Besbinar; Junji Otsuka; Daisuke Iso
- **发表**：WACV 2025；**本次读取版本**：arXiv v1
- **最早可核验公开日**：2024-11-20
- **首次归档**：2026-10-23（历史回填，非新论文通知）；**checked_on**：2026-10-23
- **主题**：T05 数据与 Pseudo-GT；桥接 T01 / T03
- **verification_scope**：`selected_sections_checked`；独立复现：未执行
- **decision_key**：`rgb-guided-camera-specific-raw-diffusion`

## 快速回忆

**问题：**怎样把现成 RGB 数据转换为适合 RAW 下游任务的训练输入？

**记住：**RGB guidance 在多尺度残差块中调制扩散特征，以成对 RAW/RawPy 渲染 RGB 训练 RAW 预测器；损失组合 MSE、L1 和 log-L1。

系统路线与横向比较见 [成像训练数据合成 survey](../surveys/imaging-training-data-synthesis.md)。

## 精读记录

**本轮证据位置：**§3.2–3.3、§4.1、§4.5、§5。

将 Cityscapes/BDD100K 转为 RAW 输入用于检测等下游验证；原文说明每个传感器需要专门训练。

**前序与关系：**RawGen 显式引用和比较；与其形成直接 RAW 预测/规范 XYZ 再映射的表示与适配对照。

## 证据边界

相机专属训练与成对渲染监督限制跨设备直接迁移；生成 RAW 不自动成为观测真值。

作者结果不等于独立复现。作为训练数据方案时，至少在相同源场景、样本数、目标定义、下游模型和预算下比较，并用未参与生成/选优的真实相机测试检验收益。

## References

- [原论文](https://arxiv.org/abs/2411.13150v1)
- [官方补充入口](https://arxiv.org/html/2411.13150v1)
- [专题综述与覆盖记录](../surveys/imaging-training-data-synthesis.md)
