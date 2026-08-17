#!/usr/bin/env python3
"""Run fast structural checks for both HTML deliverables."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def count_entries(source: str, variable: str) -> int:
    match = re.search(rf"const\s+{re.escape(variable)}\s*=\s*\[(.*?)\]\s*;", source, re.S)
    if not match:
        return 0
    body = match.group(1)
    if variable == "scenes":
        return len(re.findall(r"\bnarration\s*:", body))
    return len(re.findall(r"\bclaim\s*:", body))


def common_checks(source: str) -> list[str]:
    failures: list[str] = []
    lower = source.lower()
    if "<!doctype html" not in lower:
        failures.append("缺少 HTML doctype")
    if 'name="viewport"' not in lower and "name='viewport'" not in lower:
        failures.append("缺少 viewport")
    if "aspect-ratio: 3 / 4" not in source and "aspect-ratio:3/4" not in source.replace(" ", ""):
        failures.append("未检测到 3:4 画布")
    if "clean" not in source:
        failures.append("未检测到 clean 模式")
    if re.search(r'<(?:script|link)[^>]+(?:src|href)=["\']https?://', source, re.I):
        failures.append("存在外部脚本或样式依赖")
    return failures


def validate_text(path: Path) -> dict[str, object]:
    source = path.read_text(encoding="utf-8")
    failures = common_checks(source)
    scene_count = count_entries(source, "scenes")
    if scene_count < 6:
        failures.append(f"场景数量过少或无法识别：{scene_count}")
    for token, label in (("durationFor", "自动时长"), ("autoplay", "自动播放"), ("narration", "旁白字段")):
        if token not in source:
            failures.append(f"未检测到{label}")
    return {"file": str(path), "scene_count": scene_count, "failures": failures}


def validate_presentation(path: Path) -> dict[str, object]:
    source = path.read_text(encoding="utf-8")
    failures = common_checks(source)
    slide_count = count_entries(source, "slides")
    if slide_count < 6:
        failures.append(f"页面数量过少或无法识别：{slide_count}")
    required = {
        "system-node": "统一节点系统",
        "translateY(-12cqw)": "下半屏统一上移",
        "lucidePaths": "本地图标路径",
        "marker-end": "箭头标记",
    }
    for token, label in required.items():
        if token not in source:
            failures.append(f"未检测到{label}")
    return {"file": str(path), "slide_count": slide_count, "failures": failures}


def html_path(directory: Path, label: str) -> Path:
    resolved = directory.expanduser().resolve()
    path = resolved if resolved.is_file() else resolved / "index.html"
    if not path.is_file():
        raise SystemExit(f"{label}缺少 index.html：{resolved}")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="校验视频观点双版 HTML 的基础结构")
    parser.add_argument("--text-dir", type=Path, required=True)
    parser.add_argument("--presentation-dir", type=Path, required=True)
    args = parser.parse_args()

    result = {
        "text": validate_text(html_path(args.text_dir, "文字版")),
        "presentation": validate_presentation(html_path(args.presentation_dir, "图形速览版")),
    }
    failures = result["text"]["failures"] + result["presentation"]["failures"]
    result["ok"] = not failures
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
