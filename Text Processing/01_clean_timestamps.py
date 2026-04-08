#!/usr/bin/env python3
"""
Module: Xoá timestamp khỏi transcript.

Chức năng:
  - Xoá dòng timestamp đứng riêng (0:00, 1:23:45, ...)
  - Xoá timestamp prefix đầu dòng (0:00: nội dung → nội dung)
  - Nối các dòng ngắn thành đoạn văn dựa trên sentence boundaries
"""
from __future__ import annotations

import re

PREFIX_TIME_RE = re.compile(r"^\+?\d{1,2}:\d{2}(:\d{2})?:\s*")
STANDALONE_TIME_RE = re.compile(r"^\+?\d{1,2}:\d{2}(:\d{2})?:?\s*$")
SENTENCE_END_RE = re.compile(r"[.!?][\"'\u201d\u2019)]*$")

DEFAULT_LINES_PER_PARA = 8


def clean_timestamps(text: str, lines_per_para: int = DEFAULT_LINES_PER_PARA) -> str:
    """Xoá timestamp và nối dòng ngắn thành đoạn văn.

    Args:
        text: Nội dung transcript gốc.
        lines_per_para: Số dòng tối đa mỗi đoạn (mặc định 8).

    Returns:
        Text đã xoá timestamp và gộp đoạn.
    """
    # Bước 1: Xoá timestamp
    cleaned: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        # Bỏ qua dòng chỉ chứa timestamp
        if STANDALONE_TIME_RE.match(stripped):
            continue
        # Giữ nguyên heading markdown
        if stripped.startswith("#"):
            cleaned.append(line)
            continue
        # Xoá timestamp prefix đầu dòng
        line = PREFIX_TIME_RE.sub("", line)
        cleaned.append(line)

    # Bước 2: Nối dòng ngắn thành đoạn văn (tách theo sentence boundaries)
    stripped_lines = [l.strip() for l in cleaned if l.strip()]

    paragraphs: list[str] = []
    current: list[str] = []

    for line in stripped_lines:
        # Giữ nguyên heading như block riêng
        if line.startswith("#"):
            if current:
                paragraphs.append(" ".join(current))
                current = []
            paragraphs.append(line)
            continue

        current.append(line)

        # Tách đoạn khi đủ dòng HOẶC gặp câu kết thúc
        if len(current) >= lines_per_para or SENTENCE_END_RE.search(line):
            paragraphs.append(" ".join(current))
            current = []

    if current:
        paragraphs.append(" ".join(current))

    return "\n\n".join(paragraphs)
