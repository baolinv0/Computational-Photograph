这 3 个数据集对应的论文/官方引用如下。需要注意：**LIVE UGC-HDR 本身没有独立发表的数据集论文，官方要求引用数据库页面；另外两个有明确论文。**

| 数据集              | 对应论文 / 官方引用                                                                                               | 作者                                                                                                           | Venue / 年份                   | 备注                                                                                                                |
| ---------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ---------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **LIVE UGC-HDR** | **LIVE User-Generated High Dynamic Range Database**                                                       | Shreshth Saini, Abhinau K. Venkataramanan, Alan C. Bovik                                                     | Dataset release, 2024        | 官方页面要求按数据库引用；**没有单独 dataset paper**。包含 2,153 个 iPhone 实拍 10-bit HLG/Rec.2100 HDR 视频。([德克萨斯大学奥斯汀分校影像与视频工程实验室][1])  |
| **LIVE-TMHDR**   | **Subjective Quality Assessment of Compressed Tone-Mapped High Dynamic Range Videos**                     | Abhinau K. Venkataramanan, Alan C. Bovik                                                                     | 2024；后续 IEEE publication     | 40 HDR sources → 15,000 tone-mapped videos，>750K ratings；这是 LIVE-TMHDR 的正式论文。([arXiv][2])                         |
| **HdM-HDR-2014** | **Creating Cinematic Wide Gamut HDR-Video for the Evaluation of Tone Mapping Operators and HDR-Displays** | Jan Fröhlich, Stefan Grandinetti, Bernd Eberhardt, Simon Hermentin Walter, Andreas Schilling, Harald Brendel | SPIE Electronic Imaging 2014 | HdM-HDR-2014 的原始数据/采集论文；提供 reconstructed original HDR camera data，后续还进入 MPEG HDR/WCG 标准化测试序列。([HdM Stuttgart][3]) |

### 论文入口

**1. LIVE UGC-HDR**
没有单独 paper，官方引用为：

> S. Saini, A. K. Venkataramanan, A. C. Bovik, *LIVE User-Generated High Dynamic Range Database*, 2024.

[LIVE UGC-HDR official dataset](https://live.ece.utexas.edu/research/LIVE_UGC_HDR/index.html?utm_source=chatgpt.com)

**2. LIVE-TMHDR**

> A. K. Venkataramanan, A. C. Bovik, *Subjective Quality Assessment of Compressed Tone-Mapped High Dynamic Range Videos*, 2024.

[LIVE-TMHDR paper](https://arxiv.org/abs/2403.15061?utm_source=chatgpt.com)

**3. HdM-HDR-2014**

> J. Fröhlich et al., *Creating Cinematic Wide Gamut HDR-Video for the Evaluation of Tone Mapping Operators and HDR-Displays*, SPIE Electronic Imaging, 2014.

[HdM author/project page with paper and data](https://www.hdm-stuttgart.de/~froehlichj/?utm_source=chatgpt.com)

如果你是为了提案里的 **“Reference Dataset”** 页面，我建议把 LIVE UGC-HDR 写成 **Dataset**，LIVE-TMHDR 和 HdM 写成 **Paper + Dataset**，不要把 LIVE UGC-HDR硬写成一篇正式论文。

[1]: https://live.ece.utexas.edu/research/LIVE_UGC_HDR/index.html?utm_source=chatgpt.com "Laboratory for Image and Video Engineering - The University of Texas at Austin"
[2]: https://arxiv.org/abs/2403.15061?utm_source=chatgpt.com "Subjective Quality Assessment of Compressed Tone-Mapped High Dynamic Range Videos"
[3]: https://www.hdm-stuttgart.de/~froehlichj/?utm_source=chatgpt.com "Hochschule der Medien (HdM) - Prof. Dr. Jan Fröhlich"
