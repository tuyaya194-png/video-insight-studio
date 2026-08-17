#!/usr/bin/env python3
"""Serve the deep-reading and visual-review versions from one process."""

from __future__ import annotations

import argparse
import functools
import socket
import threading
import time
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: object) -> None:
        return


def pick_port(host: str, preferred: int, used: set[int]) -> int:
    for port in range(preferred, preferred + 31):
        if port in used:
            continue
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                sock.bind((host, port))
            except OSError:
                continue
        used.add(port)
        return port
    raise RuntimeError(f"无法在 {preferred}–{preferred + 30} 中找到可用端口")


def make_server(host: str, port: int, directory: Path) -> ThreadingHTTPServer:
    handler = functools.partial(QuietHandler, directory=str(directory))
    return ThreadingHTTPServer((host, port), handler)


def validate_directory(directory: Path, label: str) -> Path:
    resolved = directory.expanduser().resolve()
    if not (resolved / "index.html").is_file():
        raise SystemExit(f"{label}目录缺少 index.html：{resolved}")
    return resolved


def main() -> int:
    parser = argparse.ArgumentParser(description="同时启动文字精读版和图形速览版本地预览")
    parser.add_argument("--text-dir", type=Path, required=True)
    parser.add_argument("--presentation-dir", type=Path, required=True)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--text-port", type=int, default=8765)
    parser.add_argument("--presentation-port", type=int, default=8766)
    args = parser.parse_args()

    text_dir = validate_directory(args.text_dir, "文字版")
    presentation_dir = validate_directory(args.presentation_dir, "图形速览版")
    used: set[int] = set()
    text_port = pick_port(args.host, args.text_port, used)
    presentation_port = pick_port(args.host, args.presentation_port, used)
    servers = [
        make_server(args.host, text_port, text_dir),
        make_server(args.host, presentation_port, presentation_dir),
    ]
    threads = [threading.Thread(target=server.serve_forever, daemon=True) for server in servers]
    for thread in threads:
        thread.start()

    print(f"TEXT_URL=http://{args.host}:{text_port}/?clean=1&autoplay=1", flush=True)
    print(f"PRESENTATION_URL=http://{args.host}:{presentation_port}/?clean=1", flush=True)
    print("按 Ctrl+C 停止两个预览服务。", flush=True)

    try:
        while all(thread.is_alive() for thread in threads):
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        for server in servers:
            server.shutdown()
            server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
