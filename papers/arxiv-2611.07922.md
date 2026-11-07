# StitchEdit: Stitching Depth Priors into Image Editors via Per-Layer Gradient Probing

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据与争议](#证据与争议) · [行动与方案](#行动与方案) · [References](#references)

- ID: arxiv-2611.07922；首次可核验公开：**2026-11-05**（arXiv v1）；source_version: **v1**；first_covered: **2026-11-07**；checked_on: **2026-11-07**。
- 作者/团队：Qin Guo, Dan Xu (HKUST)。
- 主主题：**T02**；次主题：T03 / T06；系统角色：训练、执行、评价；地图变化：New route / Boundary refinement。
- Verdict：**PROBE**（研究价值/工程适用性分开）；核验范围：arXiv v1 HTML 方法与选定实验、未独立复现；尚未做全站更早公开检索。

## 快速回忆
**去术语命题**：迁移同一扩散模型中的深度先验到空间几何编辑时，用逐层梯度兼容性决定哪些LoRA层保留和更新，避免统一微调覆盖几何能力。

**与前序关系**：Marigold/Lotus-2 等深度能力激活是作者引用的基础；一般Depth ControlNet需目标深度or oracle条件，与隐式逐层迁移不同。与TailSteer保护区漂移是不同错误类型。

## 精读记录
**输入→输出**：源图+几何编辑文本（缩放/遮挡/视角）→保持目标3D关系的编辑图。并非只改光度肤色的局部TM模型。

**离线**：Qwen-Image-Edit，先用约300万图/深度对训练depth LoRA；以1000校准pair统计各层 depth/edit梯度余弦；在60层MMDiT中确定l_s=20、l_e=45，裁剪后层LoRA，对前中层分组学习率；10k合成编辑pair来自Gemini规划+Nano-Banana生成，并以Gemini筛选。**在线**：普通text+source image→编辑输出，不需要额外输入depth map（学习式隐式条件）。

**作者证据**：StitchEditBench 150例（60空间变换/50遮挡/40视角），DCS(Depth Anything V2估计编辑图深度与生成目标深度Pearson) 0.92 vs 同depth-init但均匀微调0.80；LPIPS 0.10 vs 0.14。Ablation固定cosine 0.90，random schedule0.83，剪TopK 0.87，说明层级动态探针增量0.02而非0.12全部来自探针。50名受试者作者用户评价58%选StitchEdit。

**边界与反证**：训练GT和target depth来自生成模型/深度估计，DCS不是独立物理3D GT。深度初始化+更多数据/100k迭代成本高，固定cosine效果接近，其他底座或光度色彩任务未验证。

## 证据与争议
证据均来自作者报告，不能称独立重复验证；比较同输入、同监督/预算、同执行器后的实际收益才足以归因到该模块。跨设备/跨相机与真实部署尚需针对性验证。见上段具体反例。

## 行动与方案
针对几何编辑PROBE；对仅面部提亮/背景去黄的区域修图问题暂不采用。最小判别为同depth初始化/同编辑pairs预算比较probe与固定cosine，在真实图上人工检查遮挡和结构。

**记忆锚点**：迁移同一扩散模型中的深度先验到空间几何编辑时，用逐层梯度兼容性决定哪些LoRA层保留和更新，避免统一微调覆盖几何能力。

## References
- https://arxiv.org/html/2611.07922v1
- https://guoqincode.github.io/StitchEdit/
