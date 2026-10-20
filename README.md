# 双通道内容工厂（content-factory）v2.2.0

一个「总控智能体 + 两个通道子智能体」的专家团，负责把内容选题跑完整条流水线：**找热点 → 策划 → 采集 → 设计 → 生产 → 审核 → 发布 → 归因**。

## 上游搭配（必须配合）

本工厂是**执行端**，上游固定搭配**新媒体账号定位师（account-positioning）**：

- 没做过定位的号 → 先召唤 account-positioning，拿到定位 JSON
- 做过定位的号 → 把 JSON 交给总控，01 找热点按定位收敛范围
- 定位回答「做什么号、给谁看」，本工厂回答「每期发什么、怎么发」

## 结构

- `SKILL.md` — 技能入口（总控工作流）
- `agents/` — 子智能体定义（content-factory-lead 总控 / video-channel 视频通道 / copy-channel 文案通道）
- `backbone/` — 流水线阶段卡（01-08），状态落地 `pipeline_state.py`
- `references/` — 路由、文案规范、反 AI 腔、交付规范等

## 怎么用

1. 召唤本团队 → 默认进入**总控**
2. 给总控一个内容目标（例如："做一条阿岩宅基地盘活的内容"）
3. 总控按 `references/routing.md` 决定通道，派发任务
4. 对应子智能体逐步执行 `backbone/` 的阶段卡
5. 总控聚合，给你一张全局视图

## 安装

- **通用 Agent Skill 平台（Claude / CodeBuddy / Cursor 等）**：将本目录放入平台的 skills 目录即可
- **TeleAgent / Octop**：导入本技能包后启用

## License

MIT