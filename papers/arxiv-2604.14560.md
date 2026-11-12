# DVFace: Spatio-Temporal Dual-Prior Diffusion for Video Face Restoration

- Paper ID: arXiv:2604.14560
- Authors: Zheng Chen, Bowen Chai, Rongjun Gao, Mingtao Nie, Xi Li, Bingnan Duan, Jianping Fang, Xiaohong Liu, Linghe Kong, Yulun Zhang
- arXiv first upload: 2026-04-16 02:42 UTC, v1
- Current version: v2, submitted 2026-11-10 08:19 UTC
- First public listing of v2: 2026-11-11
- First covered in this archive: 2026-11-12
- Main theme: T03 — 可信恢复、生成式 SR 与高分辨率
- Secondary themes: T04, X01
- System roles: execution, training, evaluation, deployment
- Map change: Engineering maturity
- Verdict: GO-E
- Canonical survey: [Efficient Generative Restoration](../surveys/efficient-generative-restoration.md)
- Verification: v1/v2 full text, v2 efficiency table, datasets and failure discussion checked; no independent reproduction performed.

## 30-second recall

DVFace 用 spatial 与 temporal 两套 facial codebook 提供互补先验，再通过 asymmetric fusion 注入 Wan2.1 diffusion backbone，实现 one-step video face restoration。v2 的实质增量是补充了真实推理成本和更多对比，而不是改变核心架构。

**记忆锚点：** one-step 不等于 real-time；v2 报告 81 帧 512×512 在 A6000 上耗时 15.13 s，约 5.4 FPS。

## 旧路线与关系

- DicFace（2025）使用 Dirichlet-constrained variational codebook 建模跨帧人脸特征变化，是时序 codebook 路线的重要锚点。
- SVFR 与其他 diffusion-based video restoration 方法代表多步采样路线。
- DVFace 与这些方法竞争，核心增量是 spatial/temporal dual-codebook 与 asymmetric fusion；未发现作者声明其直接继承 DicFace 的具体实现。

## 技术机制

- Spatial codebook 提供局部身份/结构先验。
- Temporal codebook 提供跨帧稳定性先验。
- Asymmetric spatio-temporal fusion 根据两类先验的不同作用注入预训练 Wan2.1 diffusion backbone。
- 采用 one-step diffusion 生成恢复视频。

## 完整系统回忆卡

- **目标：** 真实退化视频中的人脸细节、身份保持与时序一致性恢复。
- **非目标：** 通用视频超分、全场景视频恢复、移动端实时人脸 ISP。
- **输入：** 低质量人脸视频帧序列。
- **输出：** 高质量、身份稳定、时间一致的人脸视频。
- **目标定义：** 训练期合成退化高质量人脸视频定义像素监督；真实场景通过无参考质量、身份和时序指标评估。
- **执行表示：** spatial/temporal dual codebook + asymmetric fusion + one-step Wan2.1 diffusion。
- **训练数据/监督：** 训练使用约 16,000 条 VFHQ 高质量人脸视频并合成退化；论文报告 codebook learning 250K iterations、LQ refinement 50K iterations、diffusion adaptation 15K iterations，4×A6000、batch size 4。合成评估覆盖 VFHQ-Test/HDTF；真实场景报告 50 条 RFV-LQ 与 100 条 VoxCeleb2 视频。
- **评价：** VFHQ/HDTF 合成测试，以及 RFV-LQ/VoxCeleb2 等真实视频测试；关注质量、身份保持和 temporal consistency。
- **反馈：** 训练期重建/感知/时序约束；无在线 reward model。
- **成本：** v2 在单张 A6000 上测得 81 frames、512×512、one step、15.13 s、约 1.604B parameters、230.21 TFLOPs；相对 SVFR 约 15.2×、Upscale-A-Video 约 23.1×。按 81/15.13 计算约 5.4 FPS，不是 30 FPS 实时。
- **强基线：** DicFace、SVFR、Upscale-A-Video、其他 diffusion-based video face restoration。
- **Agent 控制层：** 无。

## v2 更新与关键证据

v2 新增 efficiency comparison，并补充与近期 diffusion-based restoration 方法的比较和失败讨论。它把“one-step 更快”的结构性推断变成了可核验的单卡实测，但实测吞吐仍未达到实时视频帧率。

## 批判性评审

- **作者主张：** one-step diffusion 在质量、身份和时序一致性上优于近期方法。
- **局部证据：** 合成 benchmark 有参考 GT；真实视频主要依赖无参考和时序指标；v2 的效率表提供了 81-frame batch 的实际时间。
- **替代解释：** speedup 部分来自对比方法的多步采样；不能把 one-step 与完整系统成本等同。
- **失败边界：** 极端退化仍可能缺少身份细节；长视频需要 chunk-wise inference，chunk boundary 可能引入不一致；真实数据没有可靠 HR GT。
- **共识：** 视频人脸恢复中时序先验和少步生成是持续方向，但该单一模型不足以建立共识。

## 判断与行动

GO-E：v2 的价值是工程证据成熟度。可作为视频恢复效率对照，但不要宣称实时部署；后续验证应报告端到端吞吐、chunk 边界一致性和显存峰值。

## References

- [DVFace v2, arXiv:2604.14560](https://arxiv.org/abs/2604.14560)
- [DicFace, arXiv:2506.13355](https://arxiv.org/abs/2506.13355)
