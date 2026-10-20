# 04a 核心文案（core-copy，两通道共享）

> 取材自拾光社 `温成稿` 文案编辑职责 + `viral-toolkit` 文案规则 + opc `opc-copywriting` 结构。
> 本地零依赖。产出 `outputs/<topic>/core-copy.md`，是**视频脚本与图文文案的双用母体**——两边共用同一份，不写两遍。

## 执行
1. 读 `02-plan.md` 的转化路径与受众定位。
2. 读 `03-collect.md` 的素材（有则引用，无则人工看片/采集降级）。
3. 按 `core-copy-schema.md` 写满**必填块**：核心观点 / 目标受众 / 钩子 / 逻辑链 / 关键数据 / 金句 / 行动号召 / 情绪基调。
4. 套 `references/anti-ai-tone.md` 的去 AI 味铁律（开场禁问候铺垫、数字密度≤3、比喻≤3、verdict 含可转发意象、共情不嘲讽、禁 B 端黑话）。**母体生成即去味——第一句就按人话写，不等质检救火。**
5. 自检：每条铁律引用实际句子作证据；拿不准标 ⚠️ 上报总控。

## 产物
`outputs/<topic>/core-copy.md` —— 两通道共用，向下分叉：
- 视频通道 → `script-final.md`（分镜/TTS/字幕/高亮）+ `visual-theme.json`
- 文案通道 → `wechat-draft.md`（公众号推文）+ `xhs-note.md`（小红书笔记）

## 状态机
`pipeline_state.py stage --topic <slug> --stage design --status done --note "core-copy.md 已产出，待分叉"`

---

## 变更记录
- 2026-10-14：第 4 步悬空引用 `creative-ironrules.md` 改为 `references/anti-ai-tone.md`（原文件不存在，是 AI 味去不干净的根因）；明确"母体生成即去味，不等质检救火"。（去 AI 味增强，双写制同步 CHANGELOG.md）
