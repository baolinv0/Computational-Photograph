# Paper Watch v3.2 — 2026-11-14 Topic Update（2 New + 1 substantive Update）

**成功检索窗口**：本轮核对2026-11-13（Friday）arXiv cs.CV / eess.IV / cs.LG / cs.MM new lists，基于2026-11-11为此前记录最后成功的部分分类public listing，重叠复查并按arXiv ID、2026-11-13周报和已有论文卡去重。所有结果来自arXiv v1官方HTML选定全文章节，未复现；开放检索和已有作者/团队线索并行，尚未穷尽所有OpenReview和团队个人站。

| 类型 | 工作 / 首次可核验公开 | 主/次主题与系统角色 | 实质变化 / 裁决 |
|---|---|---|---|
| **New** | [ATune](papers/arxiv-2611.16236.md) · Goyal/Ruiz/Meisami (Adobe) · arXiv v1 **2026-11-12** | T02 / T05/T06/T04/X01；目标、训练、执行、搜索 | 优质图自退化10M训练→13全局摄影目标→RawTherapee/darktable无学习数值滑杆求解；GO-E / New route + Bridge |
| **New** | [Video Blind ITM](papers/arxiv-2611.15146.md) · Sul等 (SNU等) · arXiv v1 **2026-11-11** | T02 / T01/T03/T05；观测、目标、训练、执行 | 未知TMO下clip位置不可辨识；5-TMO训练边缘化＋latent signed-luminance clip-gated expectile；GO / New route + Boundary refinement |
| **Update** | [FreeDeshadow](papers/arxiv-2611.14608.md) · Wu/Gu/Li等 · expanded arXiv v1 **2026-11-10**；[PACSRNet predecessor](https://arxiv.org/abs/2501.15043) **2025-01-25** | T03 / T02/T05/T06；数据、空间定位、执行/保护 | 2025已有object-selective shadow removal；2026新增文本提示＋source-protected local refiner＋154,571 prompt quadruples/28,573 base pairs，GO-E / material Update，不算新任务首创 |

## Topic 1 — T02 / 可解释摄影目标与执行器选择
**旧图**：FiveK、PPR10K专家pair监督；Distort-and-Recover动作序列；PREEN参考图→29预设。这些是历史锚点，非本轮新推荐。
**新**：ATune将修改目标与编辑器参数解耦。对强现有方法的作者人评占比：vs GPT-6 Astra 54.3%、vs Claude 50.5%、vs专家配对监督46.3%；并不意味着对全部对照获胜。全局仅13属性、工具搜索中位42秒且无手机E2E。**判断**：参数可解释并不必绑定专家pair，但全局表达能力和成本是硬边界。
**系统**：离线10M优质图→合成降质→属性目标训练；在线图→目标属性→数值编辑器搜索→图；Agent候选选优未实现。行动GO-E：保留确定性全局路线，新增等预算属性目标vs参数回归判别实验。
**记忆锚点**：目标控制与滑杆控制不是同一个函数。见[主survey](surveys/photo-attribute-targets-and-editor-control.md)。

## Topic 2 — T02 / 未知 Tone Operator 的逆影调可辨识性
**旧图**：手工ITM（Banterle2006）、回归HDRTVNet++、生成式LumiVid/DiffHDR。Dark Matters作用VAE前颜色表示，不与此等价。
**新**：视频ITM的未知TMO和clipping引入可测signed-luminance error；训练时边缘化5个TMO，局部clip非对称损失校正。作者mean L RMSE 0.141；与最强基线在Filmic差小，out-of-family Severe仍保留差异且每配置只有单次训练。
**系统**：离线HDR→多TMO SDR→冻结VAE+视频flow LoRA+局部expectile监督；在线未知TMO的SDR视频→HDR；无Agent。行动GO：补多operator同数据预算、训练族外曲线的最小消融，不改确定性TM主线。
**记忆锚点**：曲线未知与内容被clip损失是两个不同的不确定性源。见[主survey](surveys/blind-video-inverse-tone-mapping.md)。

## Topic 3 — T03/T02 / 物体—投影关系的局部恢复（Update）
**旧图**：PACSRNet（arXiv 2501.15043、IJCAI2025）已支持点/线/object mask指定目标物体阴影；MetaShadow与全局mask类是并行前序；Paste2Place在固定物体布局下生成投影，是相反作用的互补任务。
**新**：FreeDeshadow expanded 2026稿新增文本属性/空间/状态三个提示及PCSRD+高分辨率数据，拆对象语义→cast shadow grounding→local refiner source-preservation。作者消融：无grounding shadow IoU 0.832→0.051；无aggregation非目标PSNR下降11.7dB。样本来自28,573基础pair，不能声称154k独立场景。
**系统**：离线object-shadow pair+多提示+LLM/人工核验→generator/refiner训练；在线RGB+用户目标对象→对象/阴影对应→生成候选→目标shadow局部融合→RGB；无通用Agent验证。行动GO-E **Update**：保留原source-preserving简单合成对照，按shadow定位与非目标保护独立验收。
**记忆锚点**：用户指的物体不是应该改变的像素区域。见[互补survey](surveys/object-scene-composition-and-relighting.md)。

## 非通知候选、历史证据与开放缺口
- [ReasonText-SR 2611.15449](https://arxiv.org/abs/2611.15449)：新arXiv上传前已发现较早公开的[HuggingFace ReasonText实验输出](https://huggingface.co/datasets/Jasonleex1995/ReasonText-SR-outputs)，需核对项目/数据首次真实公开、是否有实质新稿，**pending chronology**，不按本轮纯新增推送。
- [HIFC-IQA 2611.16451](https://arxiv.org/abs/2611.16451)：NeurIPS2026论文是否在OpenReview早于arXiv v1公开需查、且train-free含冻结feature+memory/gallery；**pending prior disclosure**，暂不推送。
- 公开检索至11-13新公告，不代表已穷尽所有专业会议、核心作者独立水位；OpenReview与部分团队提前发布页待补。
- 对应论文作者的结果不是独立复现；跨手机真实成像和端到端功耗热稳定没有证据，不把全局修图强度优化扩张为AE-TM新课题。

## 本轮持久化与身份原则
三张唯一论文卡、两个稳定新主survey、既有物体光影/个人偏好/HDR表示survey交叉补齐、LITERATURE_MAP、surveys/README与仓库README更新；registry身份及alphaXiv folder receipts以实际本轮读回为准，不将存储成功提前冒充已验证。
