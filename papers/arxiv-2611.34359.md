# RAWPrism: A Three-Task Dataset and a Unified Model for RAW-Domain Image Fusion

ID: arxiv-2611.34359 | Tianyi Hu, Yangdong Li, Shuyan Liu et al. (UESTC) | T01 / T03,X01 | capture, RAW fusion, ISP boundary | GO-E | New route + Benchmark.
First verified: arXiv v1 2026-11-25; first covered/checked 2026-11-27. Original methods, data/QC, Tables 1–5 and limitations checked; no independent reproduction.
Decision key: one CFA-aware RAW checkpoint spans exposure, focus and visible-thermal fusion, but only two tracks use captured RAW.

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [下一实验](#下一实验) · [References](#references)

## 快速回忆
- 3.58M 参数、单 checkpoint，使用方向性绿色插值、Hadamard 公共结构/颜色残差、任务适配器和可靠性门控，覆盖 MEF/MFF/IVIF。
- 数据为 422 组实拍 MEF、150 组配准实拍 MFF、1500 组 FMB 派生 IVIF；IVIF 的可见 RAW 是 ReRAW 逆 ISP 重建，并非传感器实拍。
- 决策含义不是“统一融合已经解决”，而是 RAW 表示与门控可共享；传感器真实性和评价协议必须逐任务拆开。

## 精读记录
MEF/MFF/IVIF 划分分别为338/42/42、120/15/15、1140/80/280。IVIF CycleISP round-trip 中位数31.7dB/0.96；作者明确记录跨划分近重复候选仍保留。共享 U-Net 前后由任务 adapter/head 接入，MEF 先做曝光归一化，IVIF 另微调适配器和 head 后合并回共享 checkpoint。
MEF（42景）RAWPrism MI 7.248、SCD .380、CC .957，QAB/F .443、MEF-SSIM .910，说明信息关联领先但边缘与结构指标并非全胜。MFF（15景）MI 5.758第一、QAB/F .581第三；与 SwinFusion 的 MI 置信区间跨零。IVIF Protocol-C（280景）EN 7.392、MI 5.284、VIF .495领先，但 CC .501、SSIM .699较低；换为标准 FMB Protocol-S 时 MI 5.284→3.492、VIF .495→.312。
固定权重干预中，Hadamard 换成恒等使 IVIF MI 5.187→4.545、VIF .489→.364；红外空间打乱使 QAB/F .716→.569、VIF .489→.332。绿色等权插值几乎不变，说明该组件未被当前指标支持。

## 证据边界
无融合 GT；多个指标可被复制源图抬高。MEF/MFF learned baselines 是 zero-shot，IVIF 各方法训练域不同。IVIF 是逆 ISP 重建 RAW，且主协议对该重建域有利；跨划分近重复候选没有清除。未给手机端到端时延、功耗、热或跨传感器验证，不能写成可部署 ISP。

## 下一实验
按场景/相机/内容哈希清理近重复后重划分；在真实可见 RAW+热红外同步设备上比较共享/分任务模型；固定 renderer 同时报告源拷贝、平均、物理一致性与人评；测 Bayer 输入到显示输出的手机 E2E。

## References
- https://arxiv.org/abs/2611.34359v1
- https://arxiv.org/html/2611.34359v1
