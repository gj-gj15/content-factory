#!/usr/bin/env python3
"""AI自媒体运营流水线状态机（纯标准库）

进度唯一真源：<EASEL_ROOT>/outputs/<topic>/pipeline-state.json
与 content-pipeline 的 manifest.py（.easel.json）共存于同一目录，互不冲突。

用法:
  python pipeline_state.py init   --topic <主题>
  python pipeline_state.py show   --topic <主题>
  python pipeline_state.py stage  --topic <主题> --stage discover --status running [--note "..."]
  python pipeline_state.py gate   --topic <主题> --gate plan-confirm --value passed
  python pipeline_state.py pending --topic <主题> --text "等待用户确认选题"
  python pipeline_state.py resume --topic <主题>
  python pipeline_state.py reset  --topic <主题>   # 危险：删除状态文件重开

阶段: discover / plan / collect / design / produce / review / publish / attribute
状态: pending / running / done / blocked
确认门: plan-confirm / publish-confirm（waiting / passed / rejected）
"""
import argparse
import datetime
import json
import os
import sys

STAGES = ["discover", "plan", "collect", "design", "produce", "review", "publish", "attribute"]
STAGE_STATUS = ["pending", "running", "done", "blocked"]
GATES = ["plan-confirm", "publish-confirm"]
GATE_VALUES = ["waiting", "passed", "rejected"]


def state_path(root: str, topic: str) -> str:
    return os.path.join(root, "outputs", topic, "pipeline-state.json")


def load(path):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return None


def save(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def now():
    return datetime.datetime.now().isoformat(timespec="seconds")


def main():
    p = argparse.ArgumentParser(description="AI自媒体运营流水线状态机")
    p.add_argument("command", choices=["init", "show", "stage", "gate", "pending", "resume", "reset"])
    p.add_argument("--topic", required=True, help="本期主题（目录名）")
    p.add_argument("--root", default=os.environ.get("EASEL_ROOT", os.getcwd()))
    p.add_argument("--stage", choices=STAGES)
    p.add_argument("--status", choices=STAGE_STATUS)
    p.add_argument("--gate", choices=GATES)
    p.add_argument("--value", choices=GATE_VALUES)
    p.add_argument("--note", default="")
    p.add_argument("--text", default="")
    a = p.parse_args()

    path = state_path(a.root, a.topic)

    if a.command == "reset":
        if os.path.exists(path):
            os.remove(path)
            print("RESET OK", path)
        else:
            print("NO STATE FILE", path)
        return

    if a.command == "init":
        if load(path):
            print("EXISTS", path)
            return
        data = {
            "topic": a.topic,
            "created": now(),
            "updated": now(),
            "current_stage": "discover",
            "stages": {s: {"status": "pending", "note": ""} for s in STAGES},
            "gates": {g: {"value": "waiting", "note": ""} for g in GATES},
            "pending": None,
            "history": [{"t": now(), "event": "init"}],
        }
        save(path, data)
        print("INIT OK", path)
        return

    data = load(path)
    if not data:
        print("NOT_FOUND: 先执行 init --topic", a.topic)
        sys.exit(1)

    if a.command == "show":
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return

    if a.command == "stage":
        if not a.stage or not a.status:
            print("BAD ARGS: 需要 --stage 和 --status")
            sys.exit(1)
        data["stages"][a.stage] = {"status": a.status, "note": a.note}
        if a.status == "running":
            data["current_stage"] = a.stage
        data["history"].append({"t": now(), "event": "stage", "stage": a.stage, "status": a.status, "note": a.note})
    elif a.command == "gate":
        if not a.gate or not a.value:
            print("BAD ARGS: 需要 --gate 和 --value")
            sys.exit(1)
        data["gates"][a.gate] = {"value": a.value, "note": a.note}
        data["history"].append({"t": now(), "event": "gate", "gate": a.gate, "value": a.value, "note": a.note})
    elif a.command == "pending":
        data["pending"] = a.text or "(未注明)"
        data["history"].append({"t": now(), "event": "pending", "text": data["pending"]})
    elif a.command == "resume":
        data["pending"] = None
        data["history"].append({"t": now(), "event": "resume"})

    data["updated"] = now()
    save(path, data)
    print("OK", a.command, "| stage:", data["current_stage"], "| pending:", data["pending"])


if __name__ == "__main__":
    main()
