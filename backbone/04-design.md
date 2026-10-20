# 04 设计（design）

> 本阶段先产**共享核心文案 `core-copy.md`**（视频脚本与图文文案的双用母体，形态无关），再按本通道做形态化加工。
> 铁律与字段定义见 `04-core-copy.md`、`core-copy-schema.md`、`dual-use.md`。

## 步骤① 核心文案（两通道共享，必做）
读 `backbone/04-core-copy.md`，产出 `outputs/<topic>/core-copy.md`。这份文案视频通道与文案通道**共用**，是"双用"的本体——写一遍，两边加工。

## 步骤② 形态化设计（按本通道选做）
- **视频通道**：基于 `core-copy.md`，套用下方脚本铁律，产出 `script-final.md`（分镜）+ `visual-theme.json`。
- **文案通道**：基于 `core-copy.md`，产出 `copy-structure.md`（标题×3 + 钩子 + 逻辑链 + 行动号召 + 排版骨架），不产分镜。

## 脚本创作铁律（视频通道形态化用，逐条执行）
1. 开场场景先行，禁数字堆叠（第一句=人/场景/处境，不是数字对比）
2. 同系列开场场景禁重复
3. 数字密度：正文一段 ≤3 组，多余转可视化
4. 比喻全篇 ≤3 次（首尾呼应+正文各一）
5. verdict/收尾必含可转发具体意象，禁总结腔、禁正确废话
6. 共情不嘲讽（讽刺指向机制不指向人；数据后跟一句人话）
7. 标题默认单行，禁教材味副题
8. 心理危机信号红线：单独成期、禁"翻译"成需求、发布前单独过确认
9. 开场禁问候/自我介绍/铺垫（"大家好""今天聊聊"见一个删一个）
10. 时长/字数体检写稿阶段清零（禁渲完再砍）
11. 承诺-兑现一致，禁标题党

**自检纪律**：每条铁律自检**必须引用脚本实际句子作证据**，禁只打 ✅。拿不准标 ⚠️ 上报。

## B. 视觉主题字段（拾光社 `visual-theme.json` 真源字段）
写视觉方案时填这份结构（纯 JSON，下游成片/封面直接读）：
```
theme_name, design_notes,
palette(9个色), texture, typography,
layout_params,
cover.size, cover.layout, cover.crop, cover.main_text, cover.badge
```

## 产物
`outputs/<topic>/script-final.md`：分镜脚本（`## 镜N [00:00-00:03]` / `- TTS文本：` / `- 字幕：` / `- 高亮：`）
`outputs/<topic>/visual-theme.json`：上述字段填好的视觉主题。
