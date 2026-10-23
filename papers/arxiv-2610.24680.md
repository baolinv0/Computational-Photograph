# MESS: Multi-Exposure Sequence Synthesis for Generalizable Image Enhancement

## 快速回忆

- **首次公开**：2026-10-17（arXiv v1；按本轮可核验来源）
- **主题**：ISP / Enhancement data
- **核验范围**：selected_sections_and_repository_checked；independent replication = not performed
- **一句话**：从少量高位深 RAW 学会生成多曝光序列，再把这种曝光退化扩展到海量普通 RGB；价值在训练数据生成，不是把 diffusion 放进手机 ISP。

## 精读记录

### 机制与证据

先用仿真 ISP 把 RAW 渲染成多曝光序列与多种 tone/MEF 风格，再训练 RGB-to-MES diffusion generator。由单张 8-bit 高质量 RGB 合成 plausible exposure variants，原图作 target，形成 500K pairs。固定 FourLLIE backbone 的跨任务宏平均中，MESS 数据在 ARNIQA/MUSIQ/MANIQA 上均优于比较数据源；规模从 5K 到 500K 继续改善。

**证据范围**：论文选定章节、官方 GitHub 与 Hugging Face 模型页；NeurIPS 2026 接收状态见论文/作者记录。Ruodai Cui 明确同署 Qualcomm Technologies，Shuaizheng Liu 与 Rongyuan Wu 同署 OPPO Research Institute。未独立复现。

### 限制与竞争解释

500K 是合成对而非真实多曝光测量；生成的是 plausible RGB exposure，不保留特定相机真实 RAW/CRF。NR-IQA 改善不等于无伪色或真实物理一致性，也没有手机端部署证据。

### 下一实验

固定轻量增强 backbone，对真实跨手机/跨 ISP 测试；加入 CRF/噪声参数错配、混合局部照明、文字/肤色保真与手机端完整耗时。

## References

- https://arxiv.org/abs/2610.24680
- https://github.com/PolyU-VCLab/MESS
- https://huggingface.co/lahaina/MESS
