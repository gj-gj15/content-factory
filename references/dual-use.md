# 双用 / 双向互转规则

核心：一份 `core-copy.md` 是视频脚本与图文文案的**共享母体**。两通道都先产它再各自加工；任一条通道完成后，也能从它的产物**反推** core-copy，供另一通道复用——写一遍，出两形态。

## 正向：core-copy → 双形态（新选题双发时）
- 视频通道：`core-copy.md` → `script-final.md`（分镜/TTS/字幕/高亮）+ `visual-theme.json`
- 文案通道：`core-copy.md` → `wechat-draft.md`（推文）+ `xhs-note.md`（笔记）

## 反向：单通道产物 → core-copy → 另一通道（补形态时）
### 已有视频脚本，要出图文
1. 从 `script-final.md` 提取：核心观点、钩子句、逻辑链、金句、行动号召、关键数据 → 回填 `core-copy.md`。
2. 文案通道读 core-copy 生成 `wechat-draft.md` / `xhs-note.md`。
3. 视频的高亮句 / verdict 意象 → 直接做图文标题与金句卡片。

### 已有图文推文，要出视频
1. 从 `wechat-draft.md` / `xhs-note.md` 提取同上字段 → 回填 `core-copy.md`。
2. 视频通道读 core-copy 生成 `script-final.md`（按铁律加 分镜/口播/TTS）。
3. 图文的标题×3 → 视频开场钩子候选；逻辑链 → 分镜节奏。

## 总控职责（唯一枢纽）
- 派发目标=双形态时：先令任一通道产 `core-copy.md`，再并行派两通道基于**同一份** core-copy 加工（互为副本，不直连）。
- 已完成一通道、用户要另一形态时：总控触发"反推 core-copy + 另一通道加工"，不重写。
- 不变量：子智能体之间永不互读对方形态化产物，只经 core-copy 中转。
