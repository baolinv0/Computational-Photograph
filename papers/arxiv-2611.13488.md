# When Reconstruction Helps Event-Camera Person Triggers

- Paper ID: arXiv:2611.13488
- Author: Yifan Shuai
- arXiv first upload: 2026-11-10 02:56 UTC, v1
- Paper-time affiliation: Li Auto
- First covered: 2026-11-13
- Main theme: T01 — 传感器到任务与常开相机
- Secondary themes: X01
- Verdict: PROBE
- Verification: full arXiv text, ancillary protocol/score tables and selected experiments checked; no independent reproduction.

## 30-second recall

在固定视觉模型前，事件流先重建为强度图，比直接积累/时间编码显著提高行人触发召回；但连续触发仍暴露准备成本、阈值敏感和误启动。E2VID 在 192 个 DSEC 窗口上得到 40/52 人、12/140 背景误触发；最佳直接编码为 14/52、7/140。

**记忆锚点：** 重建不是“画得更好”，而是给通用视觉模型提供更可解释的输入接口。

## 完整系统回忆卡

- **比较对象：** 灰度/极性/时间表面/三时间桶直接表示，与 E2VID、FireNet+ 强度重建。
- **评价：** 四段 held-out DSEC、52 人/140 背景窗口；阈值仅在独立 64-window 开发集标定。Qwen3-VL-4B 上 E2VID 为 33/52、2/140，三时间桶为 9/52、9/140。
- **成本：** FireNet+ 37,777 参数，E2VID 10.71M；Apple M1 Pro 上十个 30 ms step 的准备时间分别约 0.48 s 与 2.03 s。离线路径慢于更新节奏，不能称实时部署。
- **连续回放：** 96 s 探索性回放中，全分辨率重建捕获 7/9 episode、7 次背景启动；半分辨率 8/9、3 次背景启动。
- **边界：** 仅四段车载 DSEC；无长时 wearable 背景、功耗/热、独立人工标注；未穷尽 learned event-native encoder。公司署名只证明作者当时从属，不证明产品采用。

## 判断与下一实验

决策受影响的是“常开视觉前端是否需要重建”。下一步必须在同一功耗预算下比较事件原生轻量编码器、半分辨率 FireNet+ 与全重建，并报告每小时误触发和端到端能耗。

## References

- [arXiv:2611.13488](https://arxiv.org/abs/2611.13488)
