# LayoutRecall: Preserving Appearance in Multi-Round 3D Layout-Controlled Image Editing

ID arxiv-2611.33885 | Yankuan Chi, Xin Lin, Baihan Yang, Yuheng Liu, Jason Li, Truong Nguyen (UCSD/UCI/NTU listed among affiliations) | T06 / T02,T03,T05,X01 | historical evidence memory, execution, training, data | GO-E | Bridge + Boundary refinement.
arXiv v1 submitted 2026-11-25, official new listing 2026-11-26; first covered 2026-11-27; earliest verified arXiv, prior disclosure not exhaustive. Selected original sections/tables/appendix checked; no independent replication.

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [References](#references)
## 快速回忆
问题：连续空间编辑后物体被遮挡/移出视野，当前图与当前布局不足以恢复其曾经可见的外观。
机制：以 object ID + 3D box-local surface cell 存历史 VAE token，按目标相机投影读取，再通过适配后的生成器作局部对应；不是增加文本历史，也不是重建真实不可见几何。
## 精读记录
在线：原图/当前图+已知物体3D框与相机+目标布局→SAM3分割/射线写入物体局部表面缓存→依据目标框与相机重投影读取→FLUX.2-klein-9B-base，memory token 作为第四参考流，目标空间 RoPE、局部 Fourier embedding、object-wise attention→输出→更新缓存。已有背景按视点保存；删除对象同时删除缓存。替换缓存需投影面积至少1.25倍，非真实性门控。
离线：LayoutLoop 为 BlenderKit 164场景/498 arrangements/25,964 renders，含标定布局和相机、mask与返回访问；每个操作单独 rank16 LoRA；20k 两编辑序列/adapter，GT历史写入，第二编辑监督，flow matching + correspondence attention loss，memory dropout 0.15。推理使用自身生成历史。作者附录A报每个 memory adapter 单 RTX PRO 6000 Blackwell 15小时，50采样步，24秒/轮；未独立核定计时范围。
Table3 synthetic 50条十轮序列：full Back 23.75 dB, Self 0.733；BoxCtrl 15.46/0.287, Thinking in Boxes 14.96/0.570。SeeThrough3D 编辑成功率0.816高于full 0.732，但保真较差。Table5 fixed family full / last2 / no memory Back=23.75/19.18/15.71, Self=0.733/0.678/0.601。Table6 real COCO selected 10条十轮：Back=28.80/24.57/16.55；Self=0.756/0.648/0.596；均为历史观测相似度等无真实目标GT指标。去BLC-Fourier synthetic Back22.54，真实MUSIQ变化反而小于full，不能将全部收益归到坐标编码。
## 证据边界
强归因：长期可访问历史比短窗口/无缓存有效（作者消融）。尚未单独排除同token/训练预算的原始多图参考检索，训练GT历史与推理生成历史有分布差。布局和相机为给定输入，真实集挑选WildDet3D匹配标注；仅10条真实序列，无独立人评、无未知视角真值、无移动端部署。粗框误投影、历史生成错误写回、背景未观测是风险；不能声称证实通用多参考或真实图像恢复。最小实验：固定已知框、backbone、适配数据、历史token预算；raw history vs object-local memory，分开报返回视图与未观测视图以及目标成功/保真。
## References
- https://arxiv.org/abs/2611.33885v1 ; https://arxiv.org/html/2611.33885v1 (§3, Tables3–6, App A–B)
- https://ykchizs.github.io/layoutrecall.github.io/
- https://arxiv.org/abs/2606.23270 (BoxCtrl，原摘要核验，引用前序/基线)
- https://arxiv.org/abs/2606.20556 (Thinking in Boxes，原摘要/项目核验，引用前序/基线)
- [主专题](../surveys/multi-reference-executable-scene-control.md)；[多轮保真](../surveys/multi-turn-editing-preservation.md)
