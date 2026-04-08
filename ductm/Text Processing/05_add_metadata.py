#!/usr/bin/env python3
"""
Module: Thêm metadata header cho transcript.

Chức năng:
  - Thêm hoặc cập nhật header: Source, Type, Context
  - Giữ nguyên title (# heading) nếu có
  - Tự phát hiện title từ dòng đầu tiên
"""
from __future__ import annotations

import re

METADATA_RE = re.compile(
    r"^\*\*Source:\*\*.*?\n\*\*Type:\*\*.*?\n\*\*Context:\*\*.*?\n",
    re.MULTILINE | re.DOTALL,
)


def add_metadata(
    text: str,
    source: str = "",
    content_type: str = "",
    context: str = "",
) -> str:
    """Thêm metadata header vào đầu file.

    Args:
        text: Nội dung transcript.
        source: Nguồn (ví dụ: "Alex Hormozi").
        content_type: Loại nội dung (ví dụ: "Business Advice / Lessons").
        context: Mô tả ngắn ngữ cảnh.

    Returns:
        Text với metadata header.
    """
    # Nếu đã có metadata → bỏ qua
    if METADATA_RE.search(text):
        return text

    lines = text.splitlines()
    title_line = ""
    body_start = 0

    # Tìm title (dòng # heading đầu tiên)
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("# ") and not stripped.startswith("## "):
            title_line = stripped
            body_start = i + 1
            break
        if stripped:  # dòng không trống đầu tiên không phải title
            break

    # Tạo metadata block
    metadata_parts: list[str] = []
    if title_line:
        metadata_parts.append(title_line)
        metadata_parts.append("")

    if source:
        metadata_parts.append(f"**Source:** {source}")
    if content_type:
        metadata_parts.append(f"**Type:** {content_type}")
    if context:
        metadata_parts.append(f"**Context:** {context}")

    if source or content_type or context:
        metadata_parts.append("")

    # Ghép lại
    remaining = "\n".join(lines[body_start:]).strip()
    header = "\n".join(metadata_parts)

    if header.strip():
        return f"{header}\n{remaining}"
    return text
