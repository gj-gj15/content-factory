# CHANGELOG - 双通道内容工厂（content-factory）

## [2.1.1] - 2026-10-15

### Added（视频通道 05 成片「本地渲染绕行」，OPC 选题实测）
- 视频通道 05 成片在无视频生成 API（灵映/可灵/即梦均无 key）的阻塞下，新增一条**本地渲染绕行路线**并跑通：本机 Python(Pillow) 逐帧绘制 → ffmpeg stdin(rawvideo) 编码 → edge-tts 合成旁白 → 与视频轨合并。
- 产物（`outputs/opc-one-person-company/`）：
  - `assets/`：6 张图卡素材（1080×1920，按 `visual-theme.json` 暖米白+橙红规范；旧的科技蓝 `92-826-chart.svg` 已移入 `_v1-old/`）
  - `opc-animated-demo.mp4`：纯动画静音演示片（9 镜，1:55，无真人、无音频）
  - `opc-animated-demo-voiced.mp4`：**带旁白版**（同画面 + 中文 TTS 旁白，1:55）
  - `render_video.py` / `make_voiceover.py`：渲染与配音脚本留档，可复现
  - `voiceover/`：逐镜旁白（`voice-01..08.mp3`）、对齐分段（`seg-01..09.wav`）、全轨（`voiceover-full.wav`）
- 配音要点：音色 `zh-CN-YunxiNeural`；逐镜旁白文本取自 `script-final.md` 各镜 TTS 行，逐字未改；按镜时长对齐（补静音 / 超长则 atempo ≤1.15），音轨总长精确对齐 115.000s；响度归一化 `loudnorm I=-16`，实测 mean −18.8 dB / max −1.4 dB；视频轨 `-c:v copy` 零重编码。

### Notes
- 环境依赖（本机）：ffmpeg 静态构建（BtbN，`~/.workbuddy/tools/`）、Pillow 12.3.0、edge-tts 7.3.1（venv `~/.workbuddy/binaries/python/envs/default`）。
- 本次**未改动任何流水线规则文件**（backbone/agents/references 均未动），仅新增产物与产物脚本。
- 绕行定位：这是**演示片**（用户明确"不一定发出去"），不等于正式成片；正式发布仍可走人工拍摄或后续接入视频 API。
- 已知短板：无 BGM；镜6 旁白需 1.1522 倍压缩，按规则以 1.15 封顶、0.035s 溢出进位到镜7 前导静音（无叠字）。

## [未发布] - 2026-10-16 开发中

### Added（选题评估确认门，桂哥要求：用户给出选题先评估再正式开跑）
- `skills/factory-orchestration/backbone/01-discover.md`：选题入口扩为双路——A 路工厂出榜（找热点引导式采集）/ B 路用户直供（用户拍选题跳过采集直接进评估，**无免检权**）；新增第 5 节「评估确认门（不可跳过）」——评估四联单（12 心法亮灯 / 8 维打分 / 标题 ≥4 套 / 我的建议）必须先拿给用户，明确说「确认/开跑/就它」才允许 init/派发；打回则针对打回点修订重评；评估淘汰如实告知（用户坚持则记录「用户坚持低分开工」）；直供低分题主动给 1-2 个替代方向
- `agents/content-factory-lead.md`（总控）：职责 3 升级为「选题入口（双路）」；标准流程插入 0.5 步「评估确认门」——init 的前置闸口
- **深评升级（topic-evaluator 联动，同日追加）**：`agents/content-factory-lead.md` 新增职责第 9 条「深评升级」——确认门前满足触发条件（用户明确要求深评 / 8 维打分 30-34 边缘区 / 大投入选题（出镜、系列化、商单）/ 心法亮灯有黄线或争议项）时，总控**自行派发** `topic-evaluator`（科技侠来了，subagent 派发，与派发视频/文案通道子智能体同一机制，不需要用户手动切换专家），附上选题陈述 + 定位 JSON 路径 + 工厂初步评估结果；深评报告（全网撞车现状/硬源/四维评分 40 分制/方向建议）并入确认门：≥30/40 放行、<26/40 如实告知+替代方向、方向建议写进 `discover.md` 随生产带下去；派发失败或未安装则降级快筛并注明「未经深评」。`backbone/01-discover.md` 第 5 节新增 5.1「深评升级」小节（触发条件表+派发内容+处置规则）。标准流程 0.5 步同步补深评路径
- **version 保持 2.2.0 不升**——与任务书任务2-4 合并定版
- 说明：选题评估机制本就存在（12 心法预筛红线淘汰 + 8 维打分 <30 回炉 + 标题公式），本次补齐的是「用户直供入口」与「评估不过不进 init」的闸口化

### Added（上下游双向挂接，桂哥要求：起号专家与内容工厂必须配合使用）
- `agents/content-factory-lead.md`（总控）：职责新增第 8 条「定位检查（上游联动）」——每次开工先问「这个号做过起号定位吗」；没做过 → 提示召唤 account-positioning（新媒体起号定位），用户坚持跳过才放行并记录「无定位开工」；做过 → 读 `account-positioning.json`，把受众/人设/内容支柱/变现带进 01 找热点范围与 12 心法评估（心法①以定位的 target_audience 作答）。标准流程插入 -1 步「定位检查」；参考区加上游配套项
- `README.md`：新增「上游配套」章节（无定位先召唤 account-positioning；有定位交 JSON 路径给总控）；标题版本号修正 v1.0.0 → v2.2.0
- `.codebuddy-plugin/plugin.json`：description 补「account-positioning 固定下游」表述。**version 保持 2.2.0 不升**——本改动与任务书任务2-4（发布执行台/平台矩阵/内容预填适配）合并定版。（曾试加 tags/quickPrompts 第 4 项，被 validate 的「必须正好 3 项」规则驳回，上下游关联改由 description/displayDescription/agent/README 承载）
- `skills/factory-orchestration/SKILL.md`：新增「上游关系」段（定位检查机制 + 上下游分工一句话）
- 配套联动：account-positioning 侧同步升 v1.1.0（上游挂接，见其 CHANGELOG）

### Added（任务书任务1：拍摄执行稿）
- 新增 `skills/factory-orchestration/backbone/04b-shooting-script.md`：视频通道 04 与 05 之间的拍摄执行环节——先确认拍摄条件（真人/TTS、固定场地、固定机位），再产三件套：`口播稿.md`（标停顿/重音/语气+时长，真人TTS共用）、`拍摄执行单.md`（镜号/景别/运镜/画面/台词/道具/场地/服装，机位固定）、`拍摄清单.md`（场地/设备/道具/服装/时间/自检）。
- `agents/video-channel.md`：阶段列表在 04 与 05 间插入 `04b-shooting-script.md` 引用。
- 拍摄条件依据：真人出镜 + 纯 TTS 双路、固定场地、无移动镜头（桂哥确认）。

### Pending
- 任务2 发布执行台框架、任务3 平台矩阵、任务4 内容预填适配（进行中，完成后与任务1 合并定版本号）

## [2.2.0] - 2026-10-15

### Fixed（首轮实跑 3 个问题）
- **配音无参数选择** → `agents/video-channel.md` 05 段新增「05.1 配音参数选择」：生成前必须出参数单选（音色/语速/语调情绪/背景音乐），选定才出片，参数存 `voice-params.json` 供下次默认。
- **交付物无真实路径** → 新增 `skills/factory-orchestration/references/delivery-spec.md`：交付必给真实绝对路径（铁律），并给交付清单表格式。
- **分发命名看不懂** → 交付规范定义「按平台中文文件夹 + 中文文件名」：`outputs/<topic>/公众号/`、`小红书/`、`抖音/`…，文件如 `公众号-主稿.md`；`07-publish.md` 产物段重写；`08-attribute.md` 产物改 `汇总/数据回填.md`。
- `agents/content-factory-lead.md`：职责新增第 7 条「交付规范」（绝对路径 + 中文命名）。
- `06-review.md` 定稿呈现、`06b-hook-delivery.md` 交付段：补齐绝对路径要求。
- 版本号升至 2.2.0。

## [2.1.0] - 2026-10-14

### Added（交付物定稿闭环 + 钩子交付，v2 增量不改原逻辑）
- `skills/factory-orchestration/backbone/06-review.md`：新增「交付物呈现与定稿闭环」章节——质检过关后先把成稿作为可见交付物呈现，与用户反复探讨、迭代、直到明确"定稿"才进下一步；原有去 AI 味质检（Part A/B/裁决）完整保留。
- 新增 `skills/factory-orchestration/backbone/06b-hook-delivery.md`：定稿后单独触发的钩子交付环节——提取成稿里所有"承诺型钩子"（领模板/送方案/事件整理/技能文档…），逐个生产**完整版实体交付物**（调搜索采集真实信息，缺料标 ⚠️），落盘 `outputs/<topic>/hooks/` + 对话呈现清单。
- `agents/copy-channel.md` / `agents/video-channel.md`：阶段列表在 06 与 07 间插入 `06b-hook-delivery.md` 引用。
- 版本号升至 2.1.0（桂哥要求"不改动 v2，新建 v2.1 增量"）。

### Notes
- 钩子定义修正：非"传播钩子话术"，而是"文案承诺给读者的实体诱饵资料"（事件整理/方案文档/skills 文档等）。

## [1.2.0] - 2026-10-14

### Added（去 AI 味增强）
- 新增 `skills/factory-orchestration/references/anti-ai-tone.md`：去 AI 味权威参考（定义 + 坏特征对照表 + 去味操作 + 人味注入 + 生成期铁律），填补此前缺失的源头约束。
- `skills/factory-orchestration/backbone/04-core-copy.md`：第 4 步悬空引用 `creative-ironrules.md`（文件不存在）改为 `references/anti-ai-tone.md`，并明确"母体生成即去味，不等质检救火"。
- `skills/factory-orchestration/backbone/06-review.md`：顶部补注去味权威标准来源，定位为生成期约束的复核。
- `agents/copy-channel.md`：05 成文步加"零 AI 味"铁律（说人话/有观点/给细节/不讨好收尾）。
- `agents/video-channel.md`：05 成片步加台词"零 AI 味"铁律（口语化/有立场/TTS 念不尴尬）。

### Added（市场提交规范对齐：SKILL.md frontmatter 补齐）
- `skills/factory-orchestration/SKILL.md`：frontmatter 补齐 WorkBuddy 开放平台技能市场提交字段——`version: 2.2.0` / `author: GuiGe` / `display_name` / `display_name_en` / `description_zh` / `description_en` / `category`；原 `name` / `description` 保留不动；技能正文零改动
- 分发策略不变：`outputs/` 历史产物仍不入分享包

### Notes
- 动因：桂哥要求把本插件与 account-positioning 分享给好友并评估上传 WorkBuddy 技能市场；开放平台文档（open.workbuddy.cn/docs/skill）要求上述字段，本地格式缺项会导致提交解析失败
- `category` 暂按开放平台文档示例值 `writing` 填写，正式提交前需与运营核对可选分类列表
- content-factory 整体为团队专家包（plugin.json + 3 agents），专家包的发布通道文档未覆盖，需邮件运营（openworkbuddy@tencent.com）确认；本次仅对齐包内技能的 frontmatter

### Notes
- 根因：此前 04 引用的铁律文件 `creative-ironrules.md` 从未存在，去 AI 味仅落在质检（06）救火，人味注入常被跳过，故试验仍带 AI 味。现改为源头卡死。

## [1.1.0] - 2026-10-14

### Changed（节奏优化：找热点引导式流程）
- `skills/factory-orchestration/backbone/01-discover.md`：新增第 0 步「找热点引导式采集」：
  - 固定问答顺序：平台多选单（微博/抖音/百度/知乎/头条/B站/小红书/快手/全网）→ 行业或关键词 → 平台默认值确认 → 行业默认值确认
  - 默认值持久化：`outputs/factory-config.json`（platforms / industry / keywords / updatedAt），有默认值时开场先报默认范围、用户不改直接搜
  - 定向出榜：按所选平台逐个搜当日热榜，按行业/关键词过滤，出 4-8 条候选表（话题/平台/热度/时效），停在选题等用户选
  - 选题未确认前禁止 init 状态机、禁止派发子智能体、禁止进入 12 心法评估
- `agents/content-factory-lead.md`：职责新增「找热点引导」；铁律加唯一例外（找热点引导问答与搜索由总控亲手做）；标准流程插入第 0 步（选题确认后才 init/派发）。

### Notes
- 1.0.0：双通道内容工厂首版（总控 + 视频通道 + 文案通道，8 段骨架，04 内容母体双用层）。注册过程与排障见 workspace 日志 2026-10-13/14。
