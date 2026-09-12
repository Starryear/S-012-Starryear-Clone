<div align="center">

# 🪶 Starryear Surreal Proliferation｜星年·超现实增殖

**让复制失控到荒诞：原图在中间作证，上下脱离原构图，成为两种全新却同属一个世界的克隆灾变。**

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-000000?style=for-the-badge&logo=openai&logoColor=white)](#)
[![Usage](https://img.shields.io/badge/Usage-Personal%20%26%20Non--commercial-lightgrey?style=for-the-badge)](./LICENSE.md)
[![Language](https://img.shields.io/badge/🌐_中文-English-blue?style=for-the-badge)](#)

</div>

---

## ⚠️ 声明

> **仅限个人学习、非营利研究与非商业创作。**
> 任何商业使用均须事先取得 Starryear年 的书面许可。
>
> 分享作品时，欢迎标注来源并 **@Starryear年**。

---

## 📖 关于本项目

本 Skill 将一张照片转译为竖向三联画，核心表达“无尽复制的荒诞感”。上层把复制推向数量、密度与尺度失控；中层由脚本直接裁切源文件，只作现实证据；下层让大量克隆进一步扰乱空间、功能、因果、重力或层级关系。源图只提供主体身份与视觉 DNA，不提供上下层的构图模板；生成段必须更换锚点位置、镜头、流向、层级和空间骨架，同时共享同一色组、光线、材质、纹理与完成方式。

- ✅ 让源图主体或局部发生大量、递归、尺度失控的复制，使“克隆”成为作品主角
- ✅ 上下层分别使用“数量失控”与“规则失灵”两种不同的荒诞机制
- ✅ 保留主体辨识度但主动打破原图位置、朝向、尺度层级、深度顺序与留白地图
- ✅ 场景可折叠、翻转、建筑化或由克隆体构成，同时锁定统一色调与画面语言
- ✅ 使用确定性合成脚本嵌入源图真实像素，模型无法改动中间证据层
- ❌ 不适用于普通复制粘贴、全图重绘、统一滤镜或改造中间证据照片
- ❌ 不允许把上下层做成“原图构图加量”或在同一位置复刻主角

> 📝 The Skill includes the complete prompt in both **Chinese** and **English**.

---

## 🖼️ 示例作品

`assets/examples/` 收录 4 张由 Starryear年 明确认可的生成参考图，用于展示“数量失控—现实证据—规则失灵”的三联结构及可接受的完成度。参考图只用于理解视觉方向，不应被逐像素临摹。

- `reference-01-red-eggs.png`
- `reference-02-elephants.png`
- `reference-03-buddhas.png`
- `reference-04-shiba-inu.png`

---

## 📋 目录

- [使用方法](#-使用方法)
- [可自由调整的部分](#️-可自由调整的部分)
- [核心原则](#-核心原则)
- [内容结构](#-内容结构)
- [许可证](#-许可证)

---

## 🚀 使用方法

### 方式一：作为 Codex Skill 使用

1. 将整个 `starryear-surreal-proliferation` 文件夹复制到 Codex skills 目录，例如 `~/.codex/skills/`。
2. 开启新的 Codex 对话并上传一张照片。
3. 提出需求：

   > 使用 `starryear-surreal-proliferation`，把这张照片做成超现实增殖三联画。

4. Skill 会分开生成上下层，再用 `scripts/compose_triptych.py` 把原图裁切嵌入中间，最终只输出一张完整竖向三联画。

### 方式二：作为提示词直接使用

| 语言 | 文件 |
| :---: | :--- |
| 🇨🇳 中文 | [references/starryear-surreal-proliferation-prompt.zh-CN.md](references/starryear-surreal-proliferation-prompt.zh-CN.md) |
| 🇬🇧 English | [references/starryear-surreal-proliferation-prompt.en.md](references/starryear-surreal-proliferation-prompt.en.md) |

---

## 🎛️ 可自由调整的部分

| 参数 | 说明 |
| :--- | :--- |
| **画布比例** | 默认竖版 2:3；可在 4:5 至 9:16 之间调整，但必须保持上—中—下三段顺序 |
| **三段高度** | 默认约 34% / 24% / 42%；中层保持清晰但克制，让上下重构获得更大空间 |
| **复制强度** | 可控制克隆数量、尺度跨度、递归层级和聚集程度，但不能退化为规整图案 |
| **上层机制** | 数量、密度或尺度失控：裂变、潮汐、迁徙、嵌套、尺度瀑布、吞没场景 |
| **下层机制** | 空间、功能或因果失灵：互相承载、循环生产、克隆建筑、重力反转、递归空间 |
| **统一画风** | 可选择摄影、干燥绘画、丝网印刷、纸感拼贴或雕塑舞台等一种主语言，上下须一致 |
| **构图脱离度** | 默认强制更换主锚点分区、视点、流向和空间骨架；不得降低到复刻源图布局 |

---

## 💡 核心原则

1. **中层真实不可侵犯** — 中间层不交给生成模型；只由脚本从原文件裁切、等比缩放和定位。
2. **复制必须成为主命题** — 第一眼就能感到数量过剩、递归繁殖或克隆秩序失控，而不是装饰性重复。
3. **上下机制必须不同** — 上层表现数量/尺度/密度失控，下层表现空间/功能/因果/重力失灵。
4. **差异中保持同一世界** — 上下可以彻底重构场景，但核心色组、色温、光线气质、材质、纹理、边缘与完成度保持一致。
5. **所有主体可追溯** — 克隆体必须保留源图身份特征，不用无关幻想元素抢夺主题。
6. **身份可追溯，构图不可追摹** — 保留主体视觉 DNA，但生成段必须脱离中段的位置关系、镜头结构与留白形状。

---

## 📁 内容结构

```text
starryear-surreal-proliferation/
├── README.md
├── LICENSE.md
├── SKILL.md
├── agents/openai.yaml
├── scripts/
│   └── compose_triptych.py
├── references/
│   ├── starryear-surreal-proliferation-prompt.zh-CN.md
│   └── starryear-surreal-proliferation-prompt.en.md
└── assets/examples/
    ├── reference-01-red-eggs.png
    ├── reference-02-elephants.png
    ├── reference-03-buddhas.png
    └── reference-04-shiba-inu.png
```

> 这些图片由 Starryear年 明确提供为生成参考图；不要加入未经确认的测试图或临时输出。

---

## 📄 许可证

本项目采用 [LICENSE.md](./LICENSE.md) 中规定的使用条款。

---

<div align="center">

**如果这个项目对你有帮助，欢迎 Star ⭐ 支持！**

</div>
