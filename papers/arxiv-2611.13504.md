# Dark Matters: VAE-Aware HDR Encoding for SDR-to-HDR Video Reconstruction

- Paper ID: arXiv:2611.13504
- Authors: Donghoon Cha, Bomseok Park, Hansl von Kwon, Ku DoHyung, Hanwool Sul
- arXiv first upload: 2026-11-10 03:16 UTC, v1
- First public new-listing coverage: 2026-11-11
- First covered in this archive: 2026-11-12
- Current version: v1
- Main theme: T02 — 影调颜色、意图、个性化与参考
- Secondary themes: T03, X01
- System roles: target, execution, training, evaluation
- Map change: New route
- Verdict: GO
- Canonical survey: [VAE-Aware HDR Representation](../surveys/vae-aware-hdr-representation.md)
- Verification: full arXiv text, VAE tests, end-to-end evaluation and ablations checked; no independent reproduction performed.

## 30-second recall

Dark Matters认为 SDR-to-HDR 视频扩散的瓶颈不只在 diffusion backbone，而在 HDR radiance 进入冻结 VAE 前的颜色表示：常见 log-like encoding 会压缩深暗区域的色度差异。它提出 13-parameter、可逆、exposure-equivariant 的 EquivFlow，在不改 VAE 的情况下保留深暗 chroma。

**记忆锚点：** 它改的是 VAE 前的输入坐标系，不是新 tone-mapping operator，也不是重新训练一个 HDR VAE。

## 旧路线与关系

- LumiVid（2026）使用 LogC3，将 HDR 映射到预训练生成模型更熟悉的分布，再轻量微调视频模型。
- DiffHDR（2026）使用 Log-Gamma，将 LDR-to-HDR 建模为视频扩散 latent 中的 radiance inpainting，并构建合成 HDR 视频训练数据。
- Dark Matters 与两者属于同一问题上的竞争表示路线；没有证据表明它直接继承 LumiVid 或 DiffHDR 的方法。

## 技术机制

EquivFlow 是紧凑的可逆颜色编码：曝光变化在编码空间表现为 additive shift，色度分量对曝光尺度保持不变。它被放在 inverse-tone-mapped scene-linear proxy 与冻结 VAE 之间，通过 chroma-preserving objective 约束深暗区域的信息传输。VAE 本身不修改。

## 完整系统回忆卡

- **目标：** 从 SDR 视频恢复 HDR 视频，尤其保留深暗区域的色度和可重曝光信息。
- **非目标：** 手机实时 ISP、纯确定性 tone mapping、单帧 HDR display enhancement。
- **输入：** SDR 视频；EquivFlow 路径还使用 inverse-tone-mapped scene-linear proxy。
- **输出：** HDR 视频。
- **目标定义：** 配对 HDR 视频定义监督目标；编码阶段通过冻结 VAE round-trip 和 chroma fidelity 目标选择表示。
- **执行表示：** 13-parameter invertible EquivFlow → frozen VAE → video diffusion。
- **训练数据/监督：** 论文报告 5,780 crops、来自 1,015 parent sequences；使用 LTX-2.3 22B video diffusion backbone 与 IC-LoRA 适配；VAE、diffusion backbone 和 text encoder 冻结，只训练 rank-32 adapter。训练集为 5,780 crops（5,388 train / 324 validation / 68 test），来自 1,015 parent sequences；是公开素材的固定派生数据，不是新公开数据集。
- **评价：** VAE round-trip chroma transport、DeltaEITP、PSNR 和视频级重建指标；端到端测试共 102 clips，覆盖 ARRI、HDRTV4K、UPIQ。
- **反馈：** 配对 HDR 监督、chroma-preserving loss、VAE latent reconstruction。
- **成本：** 使用 22B 级视频生成模型；EquivFlow 第一阶段拟合 15,000 steps；adapter 训练 6,500 steps，4×H100 80GB、effective batch 4；推理使用 30 diffusion steps。论文没有给出完整训练墙钟、端到端延迟或移动端成本。
- **强基线：** LogC3（LumiVid）、Log-Gamma（DiffHDR）；不能把不同输入预处理协议下的对比当作纯编码消融。
- **Agent 控制层：** 无；没有在线候选搜索或 judge。

## 关键证据与批判性评审

**作者主张：** EquivFlow 在多个冻结图像/视频 VAE 上保持 exposure structure 与 deep-dark chroma transport，并在 SDR-to-HDR 视频扩散测试中带来稳定的色度保真收益。

**局部证据：** VAE round-trip 表中 LogC3/Log-Gamma 的重建 R² 可与 EquivFlow 持平或略高，但在 -8/-10 EV 的深暗区域，LogC3/Log-Gamma 的 linearly recoverable chroma 明显衰减甚至不可恢复；EquivFlow 保留更多 chroma。端到端 102 clips 中，EquivFlow 在六个 chromatic columns 的 ΔEITP 指标上更优，但 unseen ACES-like curve 的 aggregate PSNR 仍由 LogC3 占优；chroma loss ablation 显示该项是暗部色度保持的关键。

**关键争议/替代解释：**
1. EquivFlow 与 LogC3 的端到端比较并非完全相同的输入合同：EquivFlow 使用 inverse-tone-mapped scene-linear proxy，LogC3 对照使用 raw SDR 输入。因此收益不能全部归因于编码函数本身。
2. 编码选择面板与 ARRI 测试集合存在少量重叠，未达到完全 image-disjoint 的选择/测试分离。
3. 在 unseen ACES-like curve 的 aggregate PSNR 上，LogC3 仍有优势；Dark Matters 的主要价值是 chromatic fidelity，不是所有指标和所有曲线都占优。
4. 未报告独立复现和完整系统成本。

**共同方向/共识：** LumiVid、DiffHDR、Dark Matters 都在验证“预训练 VAE 的输入表示是 HDR 生成的重要接口”；这是一个共同研究方向，但尚无统一最优编码或跨模型共识。

## 判断与行动

GO：值得精读的是 exposure-equivariant、scale-independent chroma 这一表示机制。不要把它误读成可直接替换移动 TM 的算法。若要做最小判别实验，应在同一 SDR 输入合同、同一冻结 VAE、同一 backbone 和同一训练预算下比较 LogC3、Log-Gamma、EquivFlow，并加入未见 tone curve 与 dark-chroma 指标。

## References

- [Dark Matters, arXiv:2611.13504](https://arxiv.org/abs/2611.13504)
- [LumiVid, arXiv:2604.11788](https://arxiv.org/abs/2604.11788)
- [DiffHDR, arXiv:2604.06161](https://arxiv.org/abs/2604.06161)
