# VAE-Aware HDR Representation for SDR-to-HDR Video Diffusion

- Last updated: 2026-11-12
- Main themes: T02
- Secondary themes: T03, X01
- Status: new living survey; historical backfill of LumiVid and DiffHDR plus Dark Matters
- Scope: how HDR radiance is represented before a pretrained/frozen VAE or video diffusion model. This is not a survey of deterministic tone mapping or HDR display pipelines.

## 1. Stable problem definition

Pretrained image/video VAEs are usually trained on bounded, perceptually compressed SDR-like distributions. HDR radiance has a much wider dynamic range and different chromatic statistics. A poor input encoding can collapse shadow chroma or distort highlight/shadow structure before the generative model has any opportunity to recover it.

The central question is:

**Which invertible or near-invertible representation maps HDR radiance into a pretrained VAE's effective latent domain while preserving exposure behavior, chroma and recoverable scene information?**

## 2. Competing representation routes

| Route | Representative work | HDR representation | VAE/model adaptation | Main evidence | Main boundary |
|---|---|---|---|---|---|
| LogC3 latent alignment | LumiVid (2026) | Cinematic LogC3 encoding | Lightweight fine-tuning of pretrained video model; no encoder redesign | Shows HDR generation using pretrained visual priors and camera-mimicking degradations | Fixed log encoding may not preserve deep-dark chroma equally across exposure ranges |
| Log-Gamma radiance inpainting | DiffHDR (2026) | Log-Gamma color space | Video diffusion in latent space; controllable by text/reference | Reconstructs plausible radiance in clipped/underexposed regions and builds synthetic HDR video data | Generative radiance can be plausible without being uniquely recoverable from SDR |
| Exposure-equivariant encoding | Dark Matters (2026) | 13-parameter invertible EquivFlow; exposure changes become additive shifts, chroma is scale-independent | Frozen VAE remains unchanged; encoding is adapted before VAE | Multiple frozen VAE tests and 102-clip end-to-end evaluation report deep-dark chroma gains | LogC3 comparison uses a different input reference contract; unseen ACES-like curve favors LogC3 on aggregate PSNR |

## 3. Historical anchors and relationships

- **LumiVid (2026):** argues that a cinematic logarithmic encoding can align HDR imagery with pretrained generative-model latents and enable lightweight fine-tuning.
- **DiffHDR (2026):** formulates LDR-to-HDR as generative radiance inpainting in a video diffusion latent, using Log-Gamma and a synthetic HDR video data pipeline.
- **Dark Matters (2026):** shares the same representation-level problem, but explicitly models exposure equivariance and scale-independent chroma.

These are competing representation choices under a shared abstraction, not a proven method lineage. The fact that all use logarithmic or log-like representations does not make their encodings interchangeable.

## 4. Dark Matters: evidence and critical boundary

Dark Matters introduces EquivFlow, a compact invertible encoding that places exposure changes into additive shifts while retaining scale-independent chroma. The encoding is evaluated with pretrained image/video VAEs and integrated into an SDR-to-HDR video diffusion system using LTX-2.3 22B and IC-LoRA.

Reported setup:

- 5,780 training crops from 1,015 parent sequences;
- 102 end-to-end clips across ARRI, HDRTV4K and UPIQ;
- chroma-preserving objective is load-bearing in ablations;
- chromatic-fidelity gains are reported across tested settings.

Important limits:

1. The EquivFlow and LogC3 end-to-end paths do not share an identical input contract: EquivFlow uses an inverse-tone-mapped scene-linear proxy, while the LogC3 comparison uses raw SDR input.
2. The encoding-selection panel has limited overlap with the ARRI test subset; the selection and test sets are not fully image-disjoint.
3. LogC3 remains stronger on aggregate PSNR for the unseen ACES-like curve. EquivFlow's strongest evidence is deep-dark chroma transport, not universal superiority across every metric.
4. The 22B video diffusion system has no reported mobile or real-time deployment cost.

## 5. Full system reconstruction

### Online inference

SDR video → scene-linear proxy / inverse tone mapping → selected HDR encoding → pretrained VAE → video diffusion prior → decode and inverse encoding → HDR video.

### Offline data and training

Paired SDR/HDR clips → representation selection and VAE round-trip tests → fit EquivFlow parameters → train/finetune video diffusion adapter with paired HDR supervision → evaluate chroma and radiance fidelity under seen/unseen tone curves.

### Agent/control layer

No agent is used. The encoding is a fixed representation module; there is no online candidate search or semantic judge.

## 6. What is supported, assumed and not established

- **Literature-supported:** the input distribution seen by a pretrained VAE can constrain downstream generative reconstruction; log-like encodings can make HDR more compatible with pretrained priors.
- **Paper-local evidence:** EquivFlow transports deep-dark chroma across the tested VAE hosts and improves reported chromatic metrics in the selected end-to-end settings.
- **Design hypothesis:** exposure-equivariant coordinates may be more transferable across camera exposure and tone-curve variation than a fixed log encoding.
- **Not established:** universal superiority over LogC3/Log-Gamma, cross-camera robustness, mobile runtime, or recovery of physically unique HDR radiance from heavily clipped SDR.

## 7. Open bottlenecks and minimal discriminating experiment

The decisive experiment is a matched-input, matched-backbone comparison of LogC3, Log-Gamma and EquivFlow:

- same SDR input and inverse-tone-mapping contract;
- same frozen VAE, video backbone, adapter budget and training clips;
- held-out scenes and unseen tone curves;
- separate metrics for deep-shadow chroma, highlight reconstruction, temporal stability and aggregate radiance fidelity.

Do not conflate representation quality with the quality of the inverse-tone-mapped proxy or the strength of the diffusion prior.

## 8. Current judgment

A representation-level research branch is emerging around making HDR radiance compatible with pretrained VAE latents. The important variable is not “log versus linear” alone; it is whether the representation preserves exposure structure and chroma through the actual encoder. No single encoding is established as the winner.

## References

- [LumiVid, arXiv:2604.11788](https://arxiv.org/abs/2604.11788)
- [DiffHDR, arXiv:2604.06161](https://arxiv.org/abs/2604.06161)
- [Dark Matters, arXiv:2611.13504](https://arxiv.org/abs/2611.13504)
