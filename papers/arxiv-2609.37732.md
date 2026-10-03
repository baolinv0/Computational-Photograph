# The Camera Inside the Editor

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)

- 完整标题：The Camera Inside the Editor: Reading the Implicit Camera of Image Editors with Painted Calibration Patterns
- 作者：Sebastian Rückerl
- ID：arxiv-2609.37732；主题：Editing / camera geometry / evaluation
- arXiv 公开元数据日期：2026-09-29；首次简报：2026-10-01；核验：2026-10-03。
- 核验范围：arXiv 索引中的原摘要与元数据；未完成全文核验、未独立复现。当前版本状态待确认。
- Decision key：editing-camera-geometry-fidelity

## 快速回忆

**问题：**生成编辑即使保留主体，也可能改变拍摄几何。

**旧→新：**要求编辑器画校准图案，用消失点几何读出隐含相机，而不是让模型自报焦距。

**记住：**这里是对模型行为的 probe，不等同于通用相机标定器。

**下一步：**相同图像重复编辑，控制真实焦距和姿态，分开测几何偏差、主体身份和背景保留。

## 精读记录

[原摘要](https://arxiv.org/abs/2609.37732) 报告在合成及真实 zoom 场景中观察到编辑模型的默认相机倾向，包括姿态向水平靠拢、长焦透视向默认焦距偏移。

待精读：合成相机和真实相机的测试规模；平面/消失点假设；失败样本筛选；不同编辑模型是否重复出现；相机控制 LoRA 的独立作用。

## 证据边界

只支持“被测编辑模型/协议下存在值得检查的几何偏差”，不支持所有生成编辑器都有同样默认焦距。旧简报的精确角度、斜率与焦距换算本次未逐一核表，暂不作为已验证数值继承。

## References

- [原论文](https://arxiv.org/abs/2609.37732)
- [alphaXiv 阅读入口](https://www.alphaxiv.org/abs/2609.37732)
- [归档协议](../ARCHIVE_PROTOCOL.md)
