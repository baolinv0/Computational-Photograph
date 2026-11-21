# 场景条件化 Neural ISP：共享表示、局部控制与多专家路线
更新：2026-11-21｜主 T01；连接 T02/T05/X01｜稳定问题：一个共享 RAW→RGB 网络如何适应场景照明与局部差异，而不依赖为每种场景训练完整 ISP？

目录：[问题边界](#问题边界) · [一页路线图](#一页路线图) · [竞争路线和证据](#竞争路线和证据) · [离线与在线完整方案](#离线与在线完整方案) · [判断变更与缺口](#判断变更与缺口) · [References](#references)

## 问题边界
目标：把 RAW 中已经测到的颜色、亮度、纹理映射成场景合适的 RGB，同时减少不同光源、背光、局部噪声场景的误差。非目标：证明一个模型可从缺失曝光中恢复真实物理信息，也不等于动态 AWB/AE 联合采集。**场景输入条件、是否有偏好的目标外观、局部信息、模型容量、真实部署成本**是相互独立的变量。
主问题：全局 descriptor 是否足够？局部 context 何时额外带来收益？MoE 是否真正优于同容量 FiLM，而不是多参数的重新包装？

## 一页路线图
| 竞争路线 | 输入、控制、机制、输出 | 训练目标/成立条件 | 必须比较的简单基线 |
|---|---|---|---|
| 固定共享 encoder–decoder（AWNet、RMFA-Net 等历史锚点） | Bayer→共享网络→RGB | 真实相机 RAW/RGB pairing，隐式上下文适应 | 同参数+FLOPs的 shared ISP |
| 全局场景条件（MetaISP 一类） | Bayer+全局颜色/scene特征→FiLM / gating / LUT→RGB | 色彩外观有场景级结构且GT对齐 | Global-only FiLM + 低维 scene histogram |
| 全局+局部条件 / 多仿射专家（**LG-FiLM, 2026-11-19**） | Bayer→encoder→global pool + neighborhood→token级 soft MoE (gamma/beta)→共享 decoder→RGB | 真实 Fujifilm sensor RAW/Ground Truth | global-only、local-only、同容量 single FiLM |
| 内容自适应高分辨率颜色调节（BPAM/双边网格等） | RGB→小网格/逐像素曲线→RGB | 已有可靠结构与颜色输入；偏渲染，不可代替去噪 | 全局曲线 / 3D LUT |
| 同机双流数据中间监督（LC-ISP） | 单 Bayer→恢复中间 RGB→渲染sRGB | 同设备多帧拍照教师，目标与真实独立测量不同 | 只最终 GT / 保持架构中间监督 |

**关系**：LG-FiLM 作者明确以 RMFA-Net 路径为架构起点；与 MetaISP、BPAM、LC-ISP 是问题与机制的竞争/互补，不能用年份声称直接继承。历史相关工作需要后续逐篇重查全文，本页已核验 LG-FiLM v1 §2–4 和关键消融。

## 竞争路线和证据
[LG-FiLM](../papers/arxiv-2611.25639.md) 的 Fujifilm UltraISP作者 Table1：同作者 RMFA-Net24.377 vs LG-FiLM24.998 dB（+0.621dB）。关键同模型消融（Tables 4/10）：
- no-condition 23.366 vs full 24.998：证明网络中注入显式可训练条件在此域有效；
- local-only 23.387，global-only 24.857，full 比 global 只多0.141 dB；
- 相近参数量的单一 FiLM 24.840／轻量单变换24.912：不能把 headline +0.621 dB归因“MoE专家数量”。
- ZRR 在该数据集**重新训练**后21.249 vs PyNET 21.19，非跨传感器零样本；COCO InvISP逆RAW也是从模拟数据重新训练，无法充当真实新相机适应。
- 论文强调 scene-adaptive 但真正适配效果的强支持来自全局特征；local expert/soft mixture的增量和实际手机部署尚无充分独立数据。

## 离线与在线完整方案
目标定义：RAW-to-RGB预定拍照 GT（可能有厂商风格），非 radiance GT/个人偏好；训练数据需保存camera_id、黑白电平、WB/exposure、ROI与GT来源。离线：真实 RAW配对→固定划分场景/相机→相同架构+预算下学共享处理和条件化→分背光、肤色、复杂纹理、混光独立测 GT loss/色差/高光/泄漏。在线：RAW+元数据→场景编码→global/local处理条件→共享 decoder→sRGB；Agent不必需、外层可选择风格但未经本文验证。全链成本包括 Bayer预处理、内存/CPU、NPU/GPU转换、曝光/AV pipeline、热与功耗；FLOPs只是一部分。

## 判断变更与缺口
旧：统一ISP多依赖隐式学习或全局条件；新：LG-FiLM提供同数据同骨干的显式条件增益，但局部MoE未击败强 global-only多少；保持：复杂环境对目标渲染/采集有信息限制，不能假定同手机AE/AWB/TM可直接替换。**PROBE**：优先在真实跨光源样本上用 global-only 单FiLM作为强替代，而非直接部署8专家。
最小判别实验：固定真实RAW/GT、模型参数、训练预算、执行FLOPs，比较 unconditioned/global-only/local+global-singleFiLM/local+global-MoE，测普通/逆光/混光/肤色的PSNR、ΔE、局部曝光与真实设备时延。未读完历史MetaISP与BPAM完整消融、不完整产业设备证据列为 backfill。

记忆锚点：调节同一个 ISP 的处理方式很有价值；多数增益可能只需要全局场景条件，不一定需要多专家。

## References
- [LG-FiLM arXiv v1](https://arxiv.org/abs/2611.25639v1) · [canonical](../papers/arxiv-2611.25639.md)
- [LC-ISP canonical](../papers/arxiv-2611.19284.md)
- [BPAM/摄影目标对照](photo-attribute-targets-and-editor-control.md)
- [边缘效率与真机合同](mobile-isp-and-event-hdr-efficiency.md)
