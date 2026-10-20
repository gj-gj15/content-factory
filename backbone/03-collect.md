# 03 素材采集（collect）

> 取材自 `video-dissection/1.0.0/skills/douyin-resolver` + `douyin-script-analyzer`。
> ⚠️ 这两个技能**需要外部依赖**：ffmpeg（必须）+ SiliconFlow API Key（语音识别）+ 火山方舟 API Key（视频理解）。
> 无 key 时降级为「人工看片记要点」，照样能产出素材表。

## 用途
把竞品/参考抖音视频拆成可复用的拍摄脚本与口播文案，供 04-design 套用。不依赖灵映/各平台 OAuth。

## 有依赖时（自动拆解）
```bash
# 抖音解析：视频+音频+语音转文本
node douyin-resolver/scripts/douyin_resolver.js resolve "<抖音链接>" -o ./output
# 拍摄脚本分析：景别/运镜/剪辑节奏 + 按镜头裁片段
python douyin_script_analyzer.py "<抖音链接>" -o ./output
```
产出：`output/<vid>/拍摄脚本分析.md` + `shots/序号_景别_主题.mp4`。

## 无依赖时（人工降级）
打开参考视频，按下面表格手抄要点即可：

| 字段 | 记什么 |
|------|--------|
| 黄金前 3 秒 | 第一句说了什么、什么画面 |
| 钩子类型 | 数字冲击/反差/悬念/身份点名 |
| 景别节奏 | 中景/近景/特写切换频率 |
| 口播结构 | 铺垫→冲突→反转→verdict |
| 可抄的句式 | 原句（去 AI 味前先原样记） |

## 产物
`outputs/<topic>/collect.md`：参考拆解表（自动或人工），标注来源链接、可复用手法。
