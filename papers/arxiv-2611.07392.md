# WeLM-Image: A Unified Image Generation Model towards Visual Intelligence

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据与争议](#证据与争议) · [行动与方案](#行动与方案) · [References](#references)

- ID: arxiv-2611.07392；首次可核验公开：**2026-11-05**（arXiv v1）；source_version: **v1**；first_covered: **2026-11-07**；checked_on: **2026-11-07**。
- 作者/团队：WeChat Vision, Tencent（Canmiao Fu 等）。
- 主主题：**T02**；次主题：T04 / T05 / T06 / X01；系统角色：目标、数据、训练、执行、评价；地图变化：Engineering maturity / Bridge。
- Verdict：**GO-E**（研究价值/工程适用性分开）；核验范围：arXiv v1 HTML 方法与选定实验、未独立复现；尚未做全站更早公开检索。

## 快速回忆
**去术语命题**：把理解与生成拆成不同参数路径、在每层共享注意力并配合专家稀疏激活，再用独立编辑Reward与蒸馏构建大规模图像生成编辑一体模型。

**与前序关系**：Qwen-Image、HunyuanImage3.0、SenseNova-U1 与 WeLM 都研究理解-生成协同；是系统层竞争/共同机制，不假定直接继承。已有编辑奖励/工具链验证是互补的外部控制。

## 精读记录
**输入→输出**：文本、源图、多参考和混合指令序列→图像生成、图像编辑或多参考合成。32B级别的通用图像编辑器，不是端侧RAW恢复或可直接替代手机ISP的网络。

**离线**：WeChat Vision 报告约50亿图像原池筛至6亿，构造图文、编辑、多参考训练集；MoT理解/生成分开的专家参数，attention跨路径交互；预训练/SFT、生成和编辑分别RL、on-policy/few-step distillation。**在线**：源图/参考/指令→统一多模态表示→理解path辅助约束生成path→视觉token解码；31.7B储存规模、生成token激活约5.4B，8-step latency在H20，不等于手机部署。

**作者证据**：Table1在受控256x256 ImageNet生成测试WeLM VAE FID 12.21、IS 97.96，和FLUX.2-VAE FID 9.87、IS90.85存在tradeoff（不能称全部维度第一）；作者声称多个生成/编辑benchmark具竞争力。数据规模、底座容量与混合训练的贡献尚未被完备等预算消融区分；处理平台的15k QPS是离线数据系统吞吐，非图像模型推理QPS。

**最强替代解释与边界**：大量筛选数据、31.7B总参数及训练预算可能主导优势；跨不同底座和数据的榜单不能归因为MoT、Reward或蒸馏各自独立的增益。报告尚不足以证明“给文本就能零泄漏局部修图”或目标光度保真。

## 证据与争议
证据均来自作者报告，不能称独立重复验证；比较同输入、同监督/预算、同执行器后的实际收益才足以归因到该模块。跨设备/跨相机与真实部署尚需针对性验证。见上段具体反例。

## 行动与方案
保留为产品级训练/服务工程路线 GO-E；不替换区域编辑的 mask-based 强基线。仅在同源图与保护区下检验 target success 和 leakage，再判断该新执行器能否实际提高可达性。

**记忆锚点**：把理解与生成拆成不同参数路径、在每层共享注意力并配合专家稀疏激活，再用独立编辑Reward与蒸馏构建大规模图像生成编辑一体模型。

## References
- https://arxiv.org/html/2611.07392v1
- https://arxiv.org/abs/2508.02324 (Qwen-Image; 历史锚点，具体版本待复核)
