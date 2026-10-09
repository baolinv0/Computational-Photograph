# FLASH：脉冲光攻击时序 HDR 融合

- **身份**：arXiv:2609.37742
- **首次公开（已核）**：2026-09-29，v1
- **本次核验**：2026-10-09；selected sections checked
- **独立复现**：未进行

## 快速回忆

**问题**：时序 HDR 假设多曝光帧的场景照明一致；攻击者可用脉冲光只污染部分曝光，使融合结果产生局部亮度/颜色操纵。

**机制**：物理 FLASH attack 针对曝光序列的时间窗触发；论文覆盖 8 种物理相机平台（含 iPhone 16 Pro），并给出 exposure rejection 概念防御。

**证据**：作者在受控场景展示跨设备的 HDR 操纵与夜间防御 stress test。它建立的是攻击面，不是普遍成功率或已落地修复。

**决策边界**：不针对同步 spatial/single-shot HDR；效果依赖设备时序、场景、光强和融合策略。防御只在受控夜间测试，不能推断商业固件已安全。

**下一步**：复现实拍时记录 rolling shutter、帧时间戳、AE 状态、motion compensation 与 burst selection；测试拒帧对低照 SNR、运动鬼影和可用动态范围的副作用。

## 精读记录

- **工程含义**：HDR 评价应加入主动照明扰动和跨曝光一致性，而不只测静态 tone/ghosting。
- **竞争机制**：可比较时间异常检测、物理光传感器、跨帧光流一致性与鲁棒融合；注意“更严格拒帧”可能损失正常低照质量。
- **专利含义**：关注曝光序列异常检测、融合权重隔离及安全/画质联合控制的 prior art。

## References

- [arXiv abstract / v1](https://arxiv.org/abs/2609.37742)
- [作者代码链接](https://anonymous.4open.science/r/Lights-Camera-Attack-HDR-Manipulation-with-FLASH-Attacks-CB90/)
