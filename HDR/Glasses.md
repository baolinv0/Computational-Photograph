下面按你要的 **4 部分**收敛成最终版。

## 1. 数据基本构造方案

针对 SDR→HDR，一般可以按 **SDR/HDR 两端分别是真是假**分成 3 类：

| 类型                          | 构造方式                                                 | 优点                     | 问题                                    |
| --------------------------- | ---------------------------------------------------- | ---------------------- | ------------------------------------- |
| **A. 真实 HDR → 合成 SDR**      | 真实 HDR 母片 → Tone Mapping / ISP / Codec 模拟 → SDR      | **最容易大规模构造，HDR GT 可靠** | SDR 与真实眼镜 ISP 有 domain gap            |
| **B. 真实 SDR + 真实 HDR Pair** | 同一内容分别制作/采集 SDR 和 HDR                                | SDR/HDR 都是真实，最适合验证真实映射 | 很稀缺；很多 pair 是“两个发布版本”，不一定是物理 scene GT |
| **C. 真实 SDR + Pseudo HDR**  | 真实眼镜 SDR → teacher / offline HDR / 专业调色 → HDR target | SDR 完全匹配目标域            | HDR 不是严格真实 GT                         |

其中 A 类里的真实 HDR 来源又主要有：

* **Consumer HDR UGC**：手机真实拍摄 HDR；
* **专业 HDR camera / scene radiance**：HdM、LiU；
* **影视 HDR master**：专业制作 HDR；
* **multi-exposure HDR**：多曝光合成得到高动态范围参考。

---

# 2. 我们最适合哪一种？

我们的输入已经固定为：

> **眼镜输出的 same-EV、8-bit、压缩 SDR video**

因此最适合的主方案是：

> **A 类：真实 HDR → 模拟眼镜 SDR**

原因是我们需要：

1. 大量成对训练数据；
2. HDR GT 必须可信；
3. 能主动控制 **Fixed-EV**；
4. 能加入我们真正关心的：

   * Tone Mapping；
   * clipping；
   * 8-bit quantization；
   * compression；
   * temporal consistency。

然后再补少量：

> **B/C 类真实 SDR 数据做 target-domain adaptation / final validation。**

所以总体建议是：

```text
大规模训练：
Real HDR → glasses-like synthetic SDR

最终适配：
Real glasses SDR → real/pseudo HDR reference
```

---

# 3. 最终保留 3 个数据集

| 数据集              | 基本情况                                                          | 怎么得到                                                                                                       | 我们怎么用                                                    | 推荐理由                                                      |
| ---------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------- |
| **LIVE UGC-HDR** | **2,153 个 10-bit HDR videos**；1080p/4K、30/60fps、HLG、Rec.2100  | amateur users 使用 **iPhone 真实拍摄 HDR 视频**                                                                    | 作为主要 **真实消费级 HDR 母片**，再生成 glasses-like SDR               | **最接近眼镜/手机 UGC 内容分布**。([德克萨斯大学奥斯汀分校影像与视频工程实验室][1])        |
| **LIVE-TMHDR**   | 40 个 HDR source → **15,000 tone-mapped videos**；>750K ratings | 真实 HDR 经 **10 种开源 TMO + 2 proprietary TMO + 专业 colorist**；开源 TMO 又覆盖 4 spatial settings × 3 temporal modes | 参考/直接利用其多 TMO SDR，研究**未知前端 Tone Mapping 鲁棒性**            | **最适合解决真实眼镜 SDR 的 TM 不确定性**。([德克萨斯大学奥斯汀分校影像与视频工程实验室][2])  |
| **HdM-HDR-2014** | 专业 cinematic HDR video，动态范围最高约 **18 stops**                   | 两台专业电影摄影机通过 mirror-rig 同步采不同曝光，再对齐重建 HDR                                                                   | 自己构造 **Fixed-EV / AE-varying / compressed SDR**，专门验证多帧收益 | **最适合 Controlled Video Temporal 实验**。([HdM Stuttgart][3]) |

### 三者分工

```text
LIVE UGC-HDR
→ 真实消费级内容分布

LIVE-TMHDR
→ Tone Mapping / SDR formation 多样性

HdM-HDR
→ Fixed-EV Video Temporal 受控验证
```

这三个基本覆盖了我们当前最重要的三件事：

> **内容像不像真实眼镜视频 → SDR 怎么形成 → 多帧到底有没有用。**

---

# 4. 如果已经有真实 HDR，怎么构造成对数据？

这是我们真正应该建立的 Data Engine。

### Step 1：统一 HDR GT

首先将各种 HDR source 解码到统一 working domain：

```text
HLG / PQ / EXR HDR
      ↓
linear HDR / unified color space
      ↓
HDR GT
```

保留：

* 原始 HDR；
* luminance；
* color space；
* peak/reference white；
* frame timestamp。

**不要先把 HDR clip 到 [0,1] 再当 GT。**

---

### Step 2：确定我们要模拟的眼镜 SDR

核心：

$$
SDR_t=D(HDR_t;\theta_t)
$$

对于当前 **same-EV** 项目：

$$
EV_t=EV_0
$$

整个 clip 保持固定。

建议 degradation pipeline：

```text
Real HDR
   ↓
① Fixed Exposure
   ↓
② Highlight clipping / dynamic-range compression
   ↓
③ Global + Local Tone Mapping
   ↓
④ Color / gamut mapping
   ↓
⑤ Denoise / sharpening approximation
   ↓
⑥ 8-bit quantization
   ↓
⑦ H.264 / H.265 compression
   ↓
Synthetic glasses SDR
```

得到严格配对：

```text
Synthetic SDR_t  ↔  Real HDR_t
```

---

### Step 3：不要只生成一个 SDR

同一个 HDR 建议生成多个版本：

```text
HDR
 ├─ SDR_A：weak TM
 ├─ SDR_B：strong shoulder
 ├─ SDR_C：highlight clipped
 ├─ SDR_D：shadow compressed
 ├─ SDR_E：different color rendering
 └─ SDR_F：different codec strength
```

这样训练的是：

$$
p(HDR|SDR,\ degradation)
$$

而不是某一个固定 TMO 的：

$$
T^{-1}
$$

这正是 LIVE-TMHDR 的价值：它证明同一个 HDR source 可以通过大量不同的 TMO、空间参数和 temporal mode 形成非常不同的 SDR。([德克萨斯大学奥斯汀分校影像与视频工程实验室][2])

---

### Step 4：针对 Video 专门生成三组

利用 HdM 这类真实 HDR video，可以明确做：

| 数据版本             | 曝光设置                 | 用途                                   |
| ---------------- | -------------------- | ------------------------------------ |
| **Fixed-EV**     | `0,0,0,0,0`          | **我们的主训练/验证条件**                      |
| **AE-varying**   | `0,-0.2,-0.4,-0.2,0` | 验证 AE variation 是否提供额外 temporal clue |
| **Bracket-like** | `0,-1,0,-1,0`        | 作为 exposure-diversity upper bound    |

然后统一比较：

> **Single-frame vs Multi-frame**

这会直接回答：

> **在我们真正的 Same-EV 条件下，多帧到底是在恢复额外信息，还是主要只做降噪/时序稳定。**

---

## 最终一句话

我们的数据策略可以压缩成：

> **以 LIVE UGC-HDR 提供真实消费级 HDR 内容，以 LIVE-TMHDR 提供 SDR/Tone-Mapping 多样性，以 HdM 提供可控 Video HDR GT；在真实 HDR 上模拟 Fixed-EV + ISP/TM + 8-bit + Codec，构造与眼镜输入更接近的 SDR/HDR paired data。**

这基本就是我建议当前项目采用的最终数据方案。

[1]: https://live.ece.utexas.edu/research/LIVE_UGC_HDR/index.html?utm_source=chatgpt.com "Laboratory for Image and Video Engineering - The University of Texas at Austin"
[2]: https://live.ece.utexas.edu/research/LIVE_TMHDR/index.html "Laboratory for Image and Video Engineering - The University of Texas at Austin"
[3]: https://hdm-stuttgart.de/vmlab/hdm-hdr-2014?utm_source=chatgpt.com "Visual Media Lab"
