# FLASH: High-Resolution Image Editing with Sparse Halo Attention

## 快速回忆

- **类型 / 问题**：高分辨率可控编辑；在冻结 1K 分支保留语义/结构，局部分支处理高分辨率细节。
- **本周变化**：arXiv v1 于 2026-11-03 公开，并公开代码。
- **决策含义**：提供高分辨率编辑的结构锚定与稀疏跨分支注意力路线，但服务器分钟级成本排除移动端直接采用。
- **证据边界**：核验架构、4K 评测和时延表；未独立复现。

## 精读记录

### 机制与证据

FLASH 保持冻结的 1K 语义分支，并在高分辨率局部分支中用 sparse halo target-reference attention 融合；同时使用分辨率映射与 YaRN 处理坐标外推。VINS-4KEval 中作者报告直接 4K 模式结构保真领先；progressive 路径相对 direct 约降 30.5% 时延。直接 4K R=3 仍约 309.69 s，属于服务器离线编辑。

### 限制与竞争解释

结构分数和感知指标不等于文字、身份或局部无损；稀疏注意力可能在长距离一致性上失效。实验是高端 GPU，未报告手机内存、功耗或交互 P95。

### 下一实验

对文字、脸、重复纹理和跨图长程约束做区域级审计；与 1K 编辑+确定性重渲染/compositor 比较同等时间预算。

## References

- [arXiv:2611.04416 v1](https://arxiv.org/abs/2611.04416v1)
- [Official code](https://github.com/FLASH-edit/FLASH)
