# ALIVE: Bring Foundation Features to Life with Events

目录：[快速回忆](#快速回忆) · [精读记录](#精读记录) · [证据边界](#证据边界) · [下一步](#下一步) · [References](#references)

身份：`arxiv-2611.24579`｜Rong Zou, Haiqing Hao, Davide Scaramuzza｜arXiv v1 2026-11-18｜主题 ISP / Event / X01  
核验：2026-11-20；原文方法、表1与数据/消融选段；未独立复现。

## 快速回忆

- **问题**：相邻RGB帧之间，foundation feature会过时；每次重跑DINOv3太贵。
- **旧→新**：event→重建帧/光流warp→再编码，改为事件包直接transport+correct多层DINOv3 feature，并以anchor moment matching抑制漂移。
- **记住**：2.5M参数、65 GFLOPs、GH200上4.66 ms/更新，200Hz可达；这是高频感知特征更新，不是照片ISP或移动端真机证明。
- **下一步**：测长anchor age、照明闪烁/静止区域、跨事件传感器和移动SoC端到端。

## 精读记录

DINOv3只在anchor RGB帧运行。每5ms事件包进入recurrent updater：共享位移transport feature/memory、ConvGRU累计、residual correction、3×3零和spatial refinement；训练仅用TartanAir V2合成RGB-event序列的teacher features，无任务标签。实测DSEC/DDD17/CoSEC多任务零样本迁移。

作者报告DSEC 200ms旧anchor时，相对stale feature提升30.9 mAP、11.6 mIoU，depth AbsRel改善15.9%；单次更新65 GFLOPs、4.66 ms（GH200 FP32，含event preprocessing，不含anchor encoder和task heads）。

## 证据边界

训练全部合成；event噪声、极低运动、绝对亮度缺失和强照明变化仍可能破坏更新。moment matching假设channel统计相对anchor稳定，长时间场景替换时未必成立。GH200不是移动硬件，4.66ms不是摄像头到应用的完整延迟。

## 下一步

固定DINO/head，比较event feature update、event optical-flow warp、reconstruct-then-encode；按anchor age、运动边界、照明变化和静止区分层，并在目标SoC测功耗/带宽。

## References

- [arXiv v1](https://arxiv.org/abs/2611.24579v1)
- [DSEC](https://dsec.ifi.uzh.ch/)
