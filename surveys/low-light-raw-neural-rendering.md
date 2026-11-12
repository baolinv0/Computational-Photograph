# Low-Light RAW Neural Rendering: Noise-Aware NeRF and 3DGS

- Last updated: 2026-11-12
- Main themes: T03
- Secondary themes: T01, X01
- Status: living survey; first structured backfill from RawNeRF/LE3D to RetinexGS
- Scope: multi-view low-light RAW scene reconstruction and novel-view synthesis. This is not a survey of single-image RAW denoising or conventional mobile ISP.

## 1. Stable problem definition

Given multiple posed low-light RAW observations of a mostly static scene, reconstruct a scene representation that can render clean novel views while retaining linear sensor information, dynamic range and controllable exposure/tone mapping.

The core difficulty is not simply low-light enhancement. The system must jointly manage:

- photon/read noise in each RAW observation;
- weak or unstable geometry from low-SNR views;
- appearance changes across viewpoints and illumination;
- representation capacity and rendering efficiency;
- the mismatch between sensor-domain reconstruction metrics and display-domain visual metrics.

## 2. Competing routes

| Route | Representative work | Representation and main control | Supervision | Main strength | Main boundary |
|---|---|---|---|---|---|
| RAW NeRF | RawNeRF (2021) | NeRF directly on linear RAW; relies on multi-view noise averaging | Multi-view RAW | Strong radiance and exposure recovery with many views | Slow optimization/rendering; needs substantial view redundancy |
| RAW 3DGS | LE3D (2024) | 3DGS, Cone Scatter Initialization, Color MLP, depth distortion and near/far regularization | Multi-view RAW | Faster training and real-time rendering | Geometry/SfM still fragile in very dark regions |
| Noise-prior 3DGS | From Chaos to Clarity (2024) | Noise extractor plus noise-distribution prior to prevent elongated Gaussians fitting sensor noise | Noisy RAW, self-supervised noise modeling | Directly targets RAW-noise overfitting in 3DGS | Quality depends on noise-prior calibration and view count |
| HDR-aware 3DGS | HDRSplat (2024) | 14-bit RAW, linear HDR loss and rasterization tuning | Multi-view linear RAW | Fast high-dynamic-range scene reconstruction | Requires careful RAW/rasterizer setup; per-scene cost remains |
| Retinex/noise-metadata 3DGS | RetinexGS (2026) | Retinex-style base-color/modulation factorization, DNG noise weighting, distortion-aware rendering and depth initialization | 3 public RawNeRF scenes + 2 custom RAW scenes | Integrates appearance control and sensor-informed loss; reports real-time rendering | Five-scene evidence only; camera generalization untested |

## 3. Historical anchors and relationships

- **RawNeRF (2021):** direct RAW-domain NeRF; 25–200 noisy RAW views are used to exploit the zero-mean nature of sensor noise. This establishes the multi-view RAW/HDR reconstruction problem.
- **LE3D (2024):** moves the task to 3DGS and explicitly addresses low-SNR SfM, linear RAW color capacity and geometry regularization.
- **From Chaos to Clarity (2024):** shows that 3DGS can overfit RAW noise as elongated Gaussians, motivating explicit noise-distribution priors.
- **HDRSplat (2024):** another RAW 3DGS route, emphasizing HDR loss design and rasterization rather than a learned noise extractor.

RetinexGS directly compares against RawNeRF and LE3D under the same RAW input per scene. Its relationship to From Chaos to Clarity and HDRSplat is competitive/orthogonal at the mechanism level; publication order alone does not imply inheritance.

## 4. RetinexGS: evidence and critical boundary

RetinexGS factorizes each Gaussian's color into a view-independent base color and a shared position/view-dependent modulation field. It uses DNG noise metadata to weight signal-dependent reconstruction error, avoids spatial resampling of RAW targets, and initializes sparse dark geometry with depth guidance.

The paper reports:

- 3 public RawNeRF scenes and 2 custom low-light RAW scenes;
- mean sRGB PSNR gains of 2.18 dB over LE3D and 2.71 dB over RawNeRF across those five scenes;
- 15k iterations for RetinexGS versus 30k for the compared baselines in the reported setup;
- 91–145 FPS novel-view rendering on RTX 4090.

The gain is not attributable to one component alone. Appearance factorization is a major contributor; DNG noise weighting and depth initialization add further gains. The iteration budgets are not equal, the custom scene count is small, and sRGB metrics include per-channel affine alignment. The result is author-reported, not an independent reproduction.

## 5. Full system reconstruction

### Offline capture and training

Multi-view RAW + camera metadata → RAW calibration/packing → pose and geometry initialization → depth-guided 3DGS initialization → Retinex appearance factorization → DNG-noise-weighted RAW reconstruction → regularization and optimization.

### Online rendering

Trained Gaussian scene → view/exposure/tone-map controls → rasterization → novel-view RAW or display-domain output.

### Agent/control layer

No agent is used. The system is an explicit scene optimization and rendering pipeline.

## 6. What is supported, assumed and not established

- **Literature-supported:** multi-view redundancy can suppress zero-mean RAW noise; RAW-domain optimization retains information lost by LDR processing; 3DGS can provide real-time rendering.
- **Paper-local evidence:** RetinexGS improves the reported five-scene benchmark and reaches the stated RTX 4090 rendering rate.
- **Design hypothesis:** DNG metadata can improve camera-specific noise weighting when metadata is accurate and calibrated.
- **Not established:** cross-vendor sensor generalization, dynamic-scene robustness, robustness to inaccurate DNG noise metadata, or applicability to single-frame mobile ISP.

## 7. Open bottlenecks and minimal discriminating experiments

1. Separate the effect of appearance capacity from sensor-noise weighting: hold the Gaussian representation fixed and toggle only DNG-weighted versus fixed noise loss.
2. Test at least two sensors with known noise metadata and one sensor with missing/mismatched metadata.
3. Report linear RAW error, display-domain quality, geometry accuracy and full optimization/rendering cost separately.
4. Test view-count sensitivity: 3–5 views versus 25+ views.
5. Test dynamic objects and exposure variation rather than assuming static-scene results transfer.

## 8. Current judgment

The field has moved from “RAW NeRF can exploit multi-view noise averaging” toward faster RAW 3DGS with explicit noise and appearance controls. RetinexGS is an engineering/system refinement, not a new problem definition. Keep it as a T01/T03 adjacent branch; do not transfer its claims to single-image ISP.

## References

- [RawNeRF, arXiv:2111.13679](https://arxiv.org/abs/2111.13679)
- [LE3D, arXiv:2406.06216](https://arxiv.org/abs/2406.06216)
- [From Chaos to Clarity, arXiv:2406.08300](https://arxiv.org/abs/2406.08300)
- [HDRSplat, arXiv:2407.16503](https://arxiv.org/abs/2407.16503)
- [RetinexGS, arXiv:2611.13280](https://arxiv.org/abs/2611.13280)
