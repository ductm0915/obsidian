#!/usr/bin/env python3
"""
Module: Xoá timestamp khỏi transcript.

Chức năng:
  - Xoá dòng timestamp đứng riêng (0:00, 1:23:45, ...)
  - Xoá timestamp prefix đầu dòng (0:00: nội dung → nội dung)
  - Xử lý SRT format (00:00:00,000 --> 00:00:01,000 + sequence numbers)
  - Nối các dòng ngắn thành đoạn văn dựa trên sentence boundaries
"""
from __future__ import annotations

import re

PREFIX_TIME_RE = re.compile(r"^\+?\d{1,2}:\d{2}(:\d{2})?:\s*")
STANDALONE_TIME_RE = re.compile(r"^\+?\d{1,2}:\d{2}(:\d{2})?:?\s*$")
# SRT format: "00:00:00,080 --> 00:00:01,520"
SRT_TIMESTAMP_RE = re.compile(r"^(\d{2}):(\d{2}):(\d{2}),\d+ --> \d{2}:\d{2}:\d{2},\d+\s*$")
# SRT sequence number: a line with just a number
SRT_SEQ_RE = re.compile(r"^\d+\s*$")
SENTENCE_END_RE = re.compile(r"[.!?][\"'\u201d\u2019)]*$")

DEFAULT_LINES_PER_PARA = 8


def _ts_to_seconds(hh: int, mm: int, ss: int) -> int:
    return hh * 3600 + mm * 60 + ss


def clean_timestamps(
    text: str,
    lines_per_para: int = DEFAULT_LINES_PER_PARA,
    chapter_headings: dict[int, str] | None = None,
    tolerance: int = 3,
) -> str:
    """Xoá timestamp và nối dòng ngắn thành đoạn văn.

    Args:
        text: Nội dung transcript gốc.
        lines_per_para: Số dòng tối đa mỗi đoạn (mặc định 8).
        chapter_headings: Dict {total_seconds: '## Heading'} để chèn heading tại SRT timestamps.
                          Nếu None, tất cả SRT timestamps đều bị xoá.
        tolerance: Sai số tối đa (giây) khi match chapter heading.

    Returns:
        Text đã xoá timestamp và gộp đoạn.
    """
    inserted: set[int] = set()

    # Bước 1: Xử lý từng dòng
    cleaned: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()

        # Bỏ qua dòng chỉ chứa timestamp đơn giản (0:00, 1:23:45)
        if STANDALONE_TIME_RE.match(stripped):
            continue

        # Xử lý SRT timestamp (00:26:08,000 --> ...)
        m = SRT_TIMESTAMP_RE.match(stripped)
        if m:
            if chapter_headings:
                hh, mm, ss = int(m.group(1)), int(m.group(2)), int(m.group(3))
                line_sec = _ts_to_seconds(hh, mm, ss)
                # Tìm chapter gần nhất chưa được chèn
                best_sec, best_heading = None, None
                for target_sec, heading in chapter_headings.items():
                    if target_sec in inserted:
                        continue
                    diff = abs(line_sec - target_sec)
                    if diff <= tolerance:
                        if best_sec is None or diff < abs(line_sec - best_sec):
                            best_sec, best_heading = target_sec, heading
                if best_heading is not None:
                    inserted.add(best_sec)
                    cleaned.append(best_heading)
            # Luôn bỏ dòng SRT timestamp gốc
            continue

        # Bỏ qua dòng SRT sequence number (chỉ là số)
        if SRT_SEQ_RE.match(stripped) and not stripped.startswith("#"):
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

    # Bước 3: Merge đoạn ngắn (fragment) vào đoạn liền kề
    # Lặp nhiều lần cho đến khi không còn fragment nào nữa
    def _is_fragment(p: str) -> bool:
        return (
            not p.startswith("#")
            and len(p) < 80
            and not SENTENCE_END_RE.search(p)
        )

    for _ in range(5):  # Tối đa 5 lần pass
        merged: list[str] = []
        i = 0
        changed = False
        while i < len(paragraphs):
            para = paragraphs[i]
            if (
                _is_fragment(para)
                and i + 1 < len(paragraphs)
                and not paragraphs[i + 1].startswith("#")
            ):
                paragraphs[i + 1] = para + " " + paragraphs[i + 1]
                changed = True
            else:
                merged.append(para)
            i += 1
        paragraphs = merged
        if not changed:
            break

    return "\n\n".join(paragraphs)
