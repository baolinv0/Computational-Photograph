# FreeDeshadow: Shadow Removal for User-Specified Objects With Multimodal Prompts

- **Canonical ID:** arxiv-2611.14608 (journal/expanded manuscript distinct from cited predecessor)
- **Authors:** Zhiliang Wu; Jihao Gu; Kun Li; Hanyu Xuan; Hehe Fan; Meng Wang; Weisi Lin
- **Current expanded version first public:** 2026-11-10 18:55 UTC (arXiv v1); checked v1
- **Predecessor's earliest public:** 2025-01-25, [Prompt-Aware Controllable Shadow Removal](https://arxiv.org/abs/2501.15043), IJCAI 2025; **core object-selective shadow task is NOT new in 2026**
- **First covered / checked:** 2026-11-14
- **Main theme:** T03; secondary T02/T05/T06
- **Roles:** user objective, spatial localization, data, execution, preservation evaluation
- **Map change / verdict:** **Update (material extension), Engineering maturity + Boundary refinement / GO-E**
- **Verification:** current arXiv full HTML intro, prior-work comparison, ablations, dataset counts; predecessor official IJCAI 2025 entry and arXiv; no independent reproduction
- **Canonical survey:** [物体—环境光影协调](../surveys/object-scene-composition-and-relighting.md), explicitly marked as inverse/complementary task

## 30 秒回忆
**一句话命题：** 用“指定哪个物体”而非“直接圈出哪块阴影”决定要恢复的投影区域；生成候选与保留其他区域由两个组件分工。
**记忆锚点：** object mask 不等于 cast-shadow mask；能找到目标阴影、能只改目标阴影是两种不同能力。

## 更新历史和真正增量
- **2025 先前工作 PACSRNet**（Chen, Wu et al., IJCAI 2025，arXiv 2501.15043）：点/线/对象mask指定物体→目标阴影定位并恢复；旧 PCSRD 11,900 quadruples、256²。其2025论文**已经提出**对象指定的选择性阴影去除，不能把2026扩展文当行业首创。
- **2026 FreeDeshadow**：从仅视觉提示扩充至视觉+文本（属性/关系/状态），提出object-aware generator + shadow-aware local refiner；新PCSRD+在1024²共154,571 prompt-example quadruples，来自DESOBAv2 **28,573个基础object-shadow pairs**，不是154k幅独立拍摄。
- 相邻路线：传统全局ShadowFormer、mask-guided、MetaShadow object-centric、[Paste2Place](arxiv-2611.09387.md)的向场景**添加**物体受光/投影；本篇在固定场景中**删除**一个已存在物体的投影。是相邻但不同任务的互补，不是论文之间自然继承。

## 完整方案回忆
- **目标/非目标：** 删除被用户指定物体的cast shadow，保护其余纹理、光影和其他物体；非替换肤色或任意TM，非恢复真实未遮挡直接观测。
- **输入/输出：** 单幅RGB+点/线/object-mask或描述物体属性/空间关系/状态的text → 仅目标投影已移除的RGB。
- **离线：** DESOBAv2 28,573基础pairs→6种提示构造→VLM验证歧义+人工修正→154,571 prompt-conditioned examples→训练generator和shadow-aware local refiner。
- **在线：** user object cue→object-aware generator预测无影候选→跨尺度shadow grounding估计目标shadow support→局部aggregation/refiner在target shadow内采用候选、其余从source保持→RGB输出。
- **Agent层：** 无自学习工具路由；提示由用户定义，VLM验证主要在离线数据；仅将其作为具有强空间条件的tool是设计建议。
- **关键证据：** 作者PCSRD+模块消融：去掉cross-scale grounding目标影IoU 0.832→0.051；去掉context aggregation，非阴影区PSNR降约11.7 dB但IoU仍近似0.819→0.832，清楚分离定位能力与非目标保护能力。
- **限制与替代解释：** 154k样例来自28.6k base pairs且多提示复用，规模提升不能等同跨真实场景泛化；实景shadow GT不足，容易在强纹理/交叠影/物体语义不清场景失败；需要同基础数据/同模型预算消融新prompt与refiner贡献。
- **成本：** 依赖diffusion和SAM2编码/局部refiner，并非手机NPU端到端实测；要分开衡量生成、grounding与refine成本。
- **最强简单基线：** 对object mask几何估计shadow mask，使用确定性逆照明模型或传统inpainting+源图外区硬保持；对照同用户提示/相同数据/算力。

## 判断
**GO-E / material Update**：价值是「语义选择对象→投影定位→空间保护」闭环扩展，并非2026新问题定义。尚未证明真实手机局部阴影恢复达到产业品质。最小测试：固定基础场景和用户指令，比较global generation、generator+grounding、generator+grounding+hard source composite，记录目标阴影正确性、非目标变化及边缘光度一致性。

## References
- [FreeDeshadow arXiv v1 HTML](https://arxiv.org/html/2611.14608v1)
- [PACSRNet 2025 arXiv](https://arxiv.org/abs/2501.15043)
- [IJCAI 2025 official](https://www.ijcai.org/proceedings/2025/89)
- [MetaShadow CVPR 2025](https://ieeexplore.ieee.org/document/11094664)
- [Existing object-scene relighting survey](../surveys/object-scene-composition-and-relighting.md)
