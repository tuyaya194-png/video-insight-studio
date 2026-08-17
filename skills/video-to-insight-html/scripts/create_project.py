#!/usr/bin/env python3
"""Create a dated dual-HTML project from the bundled final templates."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
from pathlib import Path


DEFAULT_ROOT = Path.cwd()


def safe_name(value: str) -> str:
    cleaned = re.sub(r'[\\/:*?"<>|\n\r\t]+', "_", value.strip())
    cleaned = re.sub(r"\s+", " ", cleaned).strip(" ._")
    return cleaned or "未命名主题"


def copy_once(source: Path, target: Path) -> bool:
    if target.exists():
        return False
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    return True


def write_once(target: Path, content: str) -> bool:
    if target.exists():
        return False
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    return True


def analysis_template(name: str, source_url: str, created: str, language: str) -> str:
    return f"""# {name}｜视频观点分析

## 来源信息

- 视频标题：
- 演讲者：
- 平台：
- 发布日期：
- 原始地址：{source_url or "待补充"}
- 字幕 / 逐字稿来源：
- 分析日期：{created}
- 输出语言：{language}

## 版权与使用边界

- 保留原始来源与链接。
- 本项目只生成分析、摘要、转述和理解辅助，不复制完整逐字稿或原视频素材。
- 如需公开分享或商业使用，请先确认引用、翻译和素材授权。

## 一句话总论点

待完成。

## 观点结构

### 1. 章节名

- 核心观点：
- 完整解释：
- 普通人例子：
- 常见误解 / 适用边界：
- 可以开始的行动：

## 内容母稿

### 第 1 页｜章节名

- 核心观点（claim）：
- 完整解释（body）：
- 普通人例子：
- 边界 / 误解：
- 补充说明 / 回顾提示（note）：
- 图形关系（diagram）：flow / compare / converge / layers / loop / divide
- 图形节点（nodes）：
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="初始化视频观点双版 HTML 项目")
    parser.add_argument("--name", required=True, help="主题名称")
    parser.add_argument("--source-url", default="", help="原始视频地址")
    parser.add_argument(
        "--language",
        choices=("zh-CN", "en", "bilingual"),
        default="zh-CN",
        help="文字精读版输出语言：中文、英文或中英双语",
    )
    parser.add_argument("--output-root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--date", default=dt.date.today().isoformat())
    args = parser.parse_args()

    skill_dir = Path(__file__).resolve().parent.parent
    text_template = skill_dir / "assets" / "text-version" / "index.html"
    presentation_template = skill_dir / "assets" / "presentation-version" / "index.html"
    for template in (text_template, presentation_template):
        if not template.is_file():
            raise SystemExit(f"缺少模板：{template}")

    topic = safe_name(args.name)
    project_dir = args.output_root.expanduser().resolve() / f"{topic}_视频观点双版HTML_{args.date}"
    analysis_dir = project_dir / "01_观点分析"
    text_dir = project_dir / "02_文字精读版"
    presentation_dir = project_dir / "03_图形速览版"
    for directory in (analysis_dir, text_dir, presentation_dir):
        directory.mkdir(parents=True, exist_ok=True)

    created_files: list[str] = []
    analysis_path = analysis_dir / "观点分析.md"
    if write_once(analysis_path, analysis_template(topic, args.source_url, args.date, args.language)):
        created_files.append(str(analysis_path))

    text_index = text_dir / "index.html"
    if copy_once(text_template, text_index):
        created_files.append(str(text_index))

    presentation_index = presentation_dir / "index.html"
    if copy_once(presentation_template, presentation_index):
        created_files.append(str(presentation_index))

    metadata = {
        "project_name": topic,
        "created_date": args.date,
        "source_url": args.source_url,
        "output_language": args.language,
        "analysis": str(analysis_path),
        "text_version": str(text_index),
        "visual_version": str(presentation_index),
    }
    metadata_path = project_dir / "project.json"
    if write_once(metadata_path, json.dumps(metadata, ensure_ascii=False, indent=2) + "\n"):
        created_files.append(str(metadata_path))

    print(json.dumps({
        "project_dir": str(project_dir),
        "analysis": str(analysis_path),
        "text_dir": str(text_dir),
        "visual_dir": str(presentation_dir),
        "created_files": created_files,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
