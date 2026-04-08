#!/usr/bin/env python3
"""
Module: Tạo phần Key Takeaways cuối file.

Chức năng:
  - Thu thập các section headings (## ) làm danh sách takeaways
  - Tạo section ## Key Takeaways ở cuối file
  - Bỏ qua nếu đã có Key Takeaways
"""
from __future__ import annotations

import re

H2_RE = re.compile(r"^##\s+(?:\d+\.\s+)?(.+)$", re.MULTILINE)
TAKEAWAY_SECTION_RE = re.compile(r"^##\s+Key Takeaways", re.IGNORECASE | re.MULTILINE)


def add_takeaways(text: str, custom_takeaways: list[str] | None = None) -> str:
    """Thêm phần Key Takeaways cuối file.

    Args:
        text: Nội dung transcript đã format.
        custom_takeaways: Danh sách takeaways tuỳ chỉnh. Nếu None, tự tạo từ headings.

    Returns:
        Text với phần Key Takeaways.
    """
    # Nếu đã có Key Takeaways → bỏ qua
    if TAKEAWAY_SECTION_RE.search(text):
        return text

    if custom_takeaways:
        takeaways = custom_takeaways
    else:
        # Thu thập headings h2 làm takeaways
        matches = H2_RE.findall(text)
        takeaways = [m.strip() for m in matches if m.strip().lower() != "key takeaways"]

    if not takeaways:
        return text

    # Tạo section
    section_lines = [
        "",
        "---",
        "",
        "## Key Takeaways",
        "",
    ]

    for i, item in enumerate(takeaways, 1):
        section_lines.append(f"{i}. **{item}**")

    section_lines.append("")

    return text.rstrip() + "\n" + "\n".join(section_lines)
