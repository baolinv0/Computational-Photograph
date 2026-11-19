# TANGO: Real-World Unregistered RGB-Guided Hyperspectral Super-Resolution with Two-Camera Acquisitions

更新：2026-11-19｜canonical arxiv-2611.22699｜arXiv v1 首传 2026-11-17｜11-18 官方 cs.CV new 公告｜首次覆盖 2026-11-19

主主题 **T01**；次主题 T03/T05；系统角色：采集/数据/配准/执行/评价；地图变化：**New route + Engineering maturity + Boundary refinement**；裁决：**GO-E（实拍异构相机基准与错配机制）**。

目录：[快速回忆](#快速回忆) · [采集和问题定义](#采集和问题定义) · [机制与证据](#机制与证据) · [竞争路线](#竞争路线) · [完整方案和决策](#完整方案和决策) · [References](#references)

## 快速回忆

**去术语命题：**当低分辨率多光谱测量与真实 RGB 参考来自不同相机、视角不对齐时，先全局校准再局部匹配，遇到遮挡和错误对应就减弱 RGB 引导，可利用额外真实观测而少造成假纹理。

## 采集和问题定义

作者 **DUET** 403 组真实两机静态场景；Sony α6100 RGB 6000×4000 和 Specim IQ HSI 512²、原始 204 波段约 397–1004 nm，选择可见 400–700nm 的31 bands；两机光心间距约15cm，白卡反射率标定。按 scene 划 327 train /36 val/40 test，基于 SIFT/匹配和 homography 近似矫正粗视场，保留真实视差与遮挡。**不能称“真实 LR HSI 直接成像”：HR HSI 是真实采集，网络 LR 输入由对 HR HSI 做受控 Gaussian blur/下采样 x4/x8/x16 生成**；RGB 参考来自另一真实相机。训练/测试不是完全模拟 RGB-HSI 配对，亦不是全部四路都真实传感器测量。

## 机制与证据

输入 LR-HSI + unregistered HR-RGB；全局光流/几何估计（RAFT 及训练适配）→ 残差 local feature alignment → confidence/occlusion gate 限制引导 → 高分辨率 HSI。
作者 DUET x8 PSNR 38.116 dB，而同一作者对照的最强其他方法 36.403 dB；相对提升约 1.71 dB；部分倍率最高约 +2.29 dB。总体性能改善的主要来源有全局变换与 RAFT 适配，不能把全部提升归功于 gate；光谱真实采集 + 训练数据分布也可能解释跨合成数据的优势。
据正文几何审计，跨机错位在不少场景达数个到十余像素，无法把粗校准后称 pixel-aligned；强视差、运动与遮挡仍需分层评测。论文自称代码/数据将公开，但 2026-11-19 检索其 GitHub 发布地址尚未成功访问，发布状态 pending。

## 竞争路线

- 真实 RGB/NIR 辅助恢复 UGD-FM：不同光谱和任务，只在真实跨模态引导 + 错配边界上互补。
- 既有 HSI guidance 的 synthetic aligned/人工 affine warp 数据：高性能不一定能迁移到真实双机视差。
- 2024/2025 unaligned RGB-guided HSI SR：直接问题前序，需继续逐篇全文核对，不以 arXiv 年份推导方法继承。
- 与 LC-ISP same-device capture 教师不同：TANGO 是**真实新增的第二传感器信息**，对齐失败是主要负面条件。

## 完整方案和决策

- 离线：两物理相机与标定记录 → 高光谱实拍 + RGB 配对 → 白卡光谱标定、粗视场匹配 → 从 HR HSI 合成 LR HSI → 训练 global/local alignment + gating → scene-disjoint GT eval。
- 在线：LR HSI + RGB 参考 → global registration → local/gated fusion → HR HSI；没有代理或 VLM Agent。
- **行动：GO-E，保留为新增观测+错配路线上新的 benchmark；不改已有单手机 AE/TM。** 最小实验固定网络和传感观测，对比 global-only、global+local、+gate，按视差/遮挡量分层测 SAM、PSNR 与伪纹理。
- **边界**：不包含真正低分辨率 HSI 传感器读数、不支持 31 bands 外的全光谱补全、不代表手机端真实部署/功耗。

## References

- [arXiv v1 原文和补充](https://arxiv.org/html/2611.22699v1)
- [论文给出的未来代码地址（截至本轮未可核验）](https://github.com/FagiolottoConSombrero/TANGO-DUET)
- [跨模态错配 living survey](../surveys/unaligned-guided-restoration.md)
- [同机采集监督 LC-ISP 比较](arxiv-2611.19284.md)
