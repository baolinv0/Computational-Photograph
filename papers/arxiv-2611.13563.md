# Benchmarking Vendor-Guided Optimizations on Edge NPUs: From NPU Only to End-to-End Performance

- Paper ID: arXiv:2611.13563
- Authors: Youngjin Jo, Jihwan Kim, Minseok Choi, Kwanghoon Choi, Jusung Kang, Jaein Kim
- arXiv first upload: 2026-11-10 04:31 UTC, v1
- First covered: 2026-11-13
- Main theme: X01 — 端侧部署、成本与系统边界
- Secondary themes: T01
- Verdict: GO-E
- Verification: full technical report tables and methodology checked; no independent reproduction.

## 30-second recall

四款商业 edge NPU、三种视觉任务的受控分层基准显示：vendor-guided NPU-only 与 vendor-native end-to-end 不是同一结论。后者相对前者再降 10.4–70.7% 系统时延，但 12 组中仅 4 组精度提高，且硬件排名可反转。

**记忆锚点：** “NPU kernel 更快”不等于“整条相机/视觉链更快”。

## 完整系统回忆卡

- **平台：** Hailo-8、Hailo-10H、DeepX DX-M1、Mobilint Regulus；前三者同用 Jetson Orin Nano host，Regulus 用 vendor Yocto host。
- **任务：** ResNet-50、YOLOv5m、YOLOv8s-pose；5k 样本、batch 1、同步单流、10 次 warmup、四次运行。
- **三层条件：** Baseline；VG-NPU（同 I/O 与 host pre/post，只变模型转换）；VG-E2E（采用 vendor-native 输入、前后处理和 runtime）。
- **关键结果：** VG-NPU 在 10/12 组合同时改善精度和 runtime-call；VG-E2E 在全部 12 组降系统时延，但 8 组精度下降。ResNet-50 的平台排序由 NPU-only 的 Hailo8 < Hailo10 < DX 变为 E2E 的 DX < Hailo8 < Hailo10。
- **边界：** 无统一功耗/能耗；Regulus host 不同；VG-E2E 同时改变多个组件，无法逐项归因；没有移动 ISP 或相机 pipeline。

## 判断与下一实验

移动影像基准应强制同时报告 model-call、pre/post、memory movement、fallback 和端到端 P50/P95。下一步用一条 RAW→RGB 或恢复链复刻三层条件，并加能耗与热稳态。

## References

- [arXiv:2611.13563](https://arxiv.org/abs/2611.13563)
