# Imaging and ISP domain-specific review

Do not use a single generic image score to infer truth, editing quality and deployability.

| Topic | Essential distinctions and checks |
|---|---|
| AE/AWB/AF | Sensor acquisition controls versus post-capture enhancement; convergence, latency, stability, ROI vs global scores |
| Tone Mapping / Color | Brightness / tone curve / local contrast / chromaticity / AWB vs color rendering; skin tone, halo, scene-conditional aesthetics |
| HDR, LOFIC and fusion | Sensor full well, noise floor, motion and exposure timing; advertised EV vs effective dynamic range and display |
| SR, deblur, denoise, restoration | Ill-posed recovery versus perceptual generation; GT provenance, degradation consistency, hallucinated text and faces |
| Editing / Retouch | Actual target success, all protected invariants, masks versus structural fidelity, invisible changes in edited pixels |
| Native 4K | Exact height x width and tokens; native compute vs tiled 4K output; VAE codec-only loss, human-visible high-frequency degradation |
| Agent / Harness | Controller vs executor vs external experts vs verifier; equal tool and budget comparison; accepted state and rollback |
| IQA / RL / preference | Metric alignment, scorer contamination, independent human evaluation, reference vs no-reference bias |
| NPU / ISP deployment | Model params, precision, MACs/FLOPs and practical kernel support, weights, activations, DRAM, end-to-end latency, memory and energy |

## Task-level checklist

1. Identify input/output domains: RAW, Bayer, YUV, RGB, HDR linear, encoded image, latent, or video. Report exact pixels, bit depth and color space when relevant.
2. Measure faithfulness distinct from attractiveness. Sharper synthetic texture is not necessarily recovered information.
3. For unobservable original details (clipped highlights, hidden faces, illegible plates) recognize epistemic uncertainty; avoid claiming reconstruction of unknowable information.
4. Separate codec-only VAE reconstruction from editor-induced modifications using matched paired controls.
5. A fixed binary edit mask may fail for global TM or WB. Evaluate preserved geometry, identity and ordering of light/shadow relationships, not simply unchanged pixel values.
6. Mobile benchmarks must specify actual device/SoC, model checkpoint, prompt encoding policy, NPU/CPU/GPU mix, thermal state and complete interactive time. Do not infer latency by TOPS alone.
7. Hardware estimate: compare weight capacity and bandwidth as well as attention token count. A 9B INT4 theoretical weight size is ~4.5GB before scale factors and buffers. Do not convert server XPU speed into phone numbers.
