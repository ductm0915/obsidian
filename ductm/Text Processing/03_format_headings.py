#!/usr/bin/env python3
"""
Module: Định dạng headings cho transcript.

Chức năng:
  - Có file timestamp (-t) → chèn heading từ file
  - Không có file timestamp → dùng LLM tự phát hiện sections
  - Đánh số sections: ## Title → ## 1. Title
  - Thêm --- (horizontal rule) giữa các sections lớn
  - Chèn H1 title + metadata block (Source, Type, Context)
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Callable

TIME_LINE_RE = re.compile(r"^\d{1,2}:\d{2}(:\d{2})?$")


def _ts_to_seconds(ts: str) -> int:
    """'H:MM:SS' hoặc 'MM:SS' → tổng số giây."""
    parts = ts.split(":")
    if len(parts) == 3:
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
    return int(parts[0]) * 60 + int(parts[1])

HEADINGS_PROMPT = """Bạn là chuyên gia biên tập nội dung. Hãy đọc transcript dưới đây và chèn heading (## Tiêu đề) vào đúng chỗ để chia thành các sections rõ ràng.

Quy tắc:
- Dùng ## cho section chính, ### cho sub-section.
- Heading ngắn gọn, tóm tắt nội dung section (3-8 từ).
- Heading phải viết cùng ngôn ngữ với transcript. Nếu transcript tiếng Anh thì heading tiếng Anh.
- Giữ nguyên 100% nội dung gốc và ngôn ngữ gốc. Chỉ chèn thêm dòng heading, không sửa bất kỳ từ nào.
- Không dịch, không tóm tắt, không diễn giải lại.
- Trả về toàn bộ text với heading đã chèn, không giải thích gì thêm.

Transcript:
---
{text}
---"""


# ── Đọc file timestamp ─────────────────────────────────────────────

def _normalize_ts(ts: str) -> str:
    """'00:05' → '0:05' để so khớp linh hoạt."""
    parts = ts.split(":")
    parts[0] = str(int(parts[0]))
    return ":".join(parts)


def parse_timestamp_file(path: Path) -> dict[str, str]:
    """Đọc file timestamp → dict {normalized_ts: heading}.

    Format file (mỗi dòng = timestamp + tiêu đề):
        0:00 Giới thiệu
        5:30 Phần chính
        12:00 ## Mục tự chọn level
        15:00 ### Mục nhỏ hơn

    Nếu tiêu đề không bắt đầu bằng #, mặc định dùng ## (h2).
    """
    headings: dict[str, str] = {}
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(None, 1)
            if len(parts) < 2:
                continue
            ts, title = parts
            if not title.startswith("#"):
                title = f"## {title}"
            headings[_normalize_ts(ts)] = title
    return headings


# ── Chèn heading từ timestamp ──────────────────────────────────────

def insert_headings_from_timestamps(text: str, headings: dict[str, str], tolerance: int = 3) -> str:
    """Xoá dòng timestamp trong transcript, chèn heading tại vị trí tương ứng.

    Dùng fuzzy matching (±tolerance giây) để xử lý lệch nhỏ giữa YouTube timestamps
    và SRT timestamps.
    """
    # Build lookup: seconds → heading (sorted để match gần nhất trước)
    headings_by_sec: list[tuple[int, str, str]] = []
    for ts, heading in headings.items():
        headings_by_sec.append((_ts_to_seconds(ts), ts, heading))
    headings_by_sec.sort()

    inserted: set[int] = set()  # Track các heading đã chèn (theo giây)

    lines = text.splitlines()
    result: list[str] = []

    for line in lines:
        stripped = line.strip()

        if TIME_LINE_RE.match(stripped):
            normalized = _normalize_ts(stripped)
            line_sec = _ts_to_seconds(normalized)

            # Tìm chapter gần nhất chưa được chèn
            best_sec, best_heading = None, None
            for target_sec, _, heading in headings_by_sec:
                if target_sec in inserted:
                    continue
                if abs(line_sec - target_sec) <= tolerance:
                    if best_sec is None or abs(line_sec - target_sec) < abs(line_sec - best_sec):
                        best_sec, best_heading = target_sec, heading

            if best_heading is not None:
                inserted.add(best_sec)
                if result and result[-1].strip() != "":
                    result.append("")
                result.append(best_heading)
                result.append("")
            continue  # Luôn bỏ dòng timestamp

        result.append(line)

    return "\n".join(result)


# ── Chèn heading bằng LLM ─────────────────────────────────────────

_CHUNK_WORDS = 1500  # ~6-8 đoạn văn, vừa đủ context cho LLM


def _split_into_chunks(text: str, max_words: int = _CHUNK_WORDS) -> list[str]:
    """Tách text thành các chunks theo số từ, tách tại ranh giới đoạn văn."""
    paragraphs = text.split("\n\n")
    chunks: list[str] = []
    current: list[str] = []
    current_words = 0

    for para in paragraphs:
        word_count = len(para.split())
        if current_words + word_count > max_words and current:
            chunks.append("\n\n".join(current))
            current = [para]
            current_words = word_count
        else:
            current.append(para)
            current_words += word_count

    if current:
        chunks.append("\n\n".join(current))

    return chunks


def insert_headings_with_llm(text: str, llm_func: Callable[[str], str]) -> str:
    """Dùng LLM phát hiện sections và chèn heading, tách chunk để tránh quá context."""
    chunks = _split_into_chunks(text)

    if len(chunks) == 1:
        return llm_func(HEADINGS_PROMPT.format(text=text))

    formatted: list[str] = []
    for chunk in chunks:
        result = llm_func(HEADINGS_PROMPT.format(text=chunk.strip()))
        formatted.append(result)

    return "\n\n".join(formatted)


# ── Đánh số + separator ────────────────────────────────────────────

def insert_title_and_metadata(
    text: str,
    title: str | None = None,
    source: str | None = None,
    content_type: str | None = None,
    context: str | None = None,
) -> str:
    """Chèn H1 title và metadata block vào đầu văn bản.

    Nếu text đã có H1 (# ...) ở đầu → bỏ qua.
    Metadata chỉ chèn khi có ít nhất 1 field được cung cấp.
    """
    lines = text.lstrip("\n").splitlines()

    # Nếu đã có H1 ở đầu → không chèn lại
    if lines and re.match(r"^#\s+", lines[0]):
        return text

    header_lines: list[str] = []

    if title:
        header_lines.append(f"# {title}")
        header_lines.append("")

    meta_fields = [
        ("Source", source),
        ("Type", content_type),
        ("Context", context),
    ]
    meta_lines = [f"**{label}:** {value}" for label, value in meta_fields if value]

    if meta_lines:
        header_lines.extend(meta_lines)
        header_lines.append("")
        header_lines.append("---")
        header_lines.append("")

    if not header_lines:
        return text

    return "\n".join(header_lines) + text


def number_and_separate(text: str, number_sections: bool = True, add_separators: bool = True) -> str:
    """Đánh số sections và thêm --- giữa các sections."""
    lines = text.splitlines()
    result: list[str] = []
    section_count = 0

    for line in lines:
        stripped = line.strip()

        h2_match = re.match(r"^##\s+(.+)$", stripped)
        if h2_match and not stripped.startswith("###"):
            title = h2_match.group(1)
            section_count += 1

            title = re.sub(r"^\d+\.\s*", "", title)

            if add_separators and section_count > 1:
                if result and result[-1].strip() != "---":
                    result.append("")
                    result.append("---")
                    result.append("")

            if number_sections:
                result.append(f"## {section_count}. {title}")
            else:
                result.append(f"## {title}")
            continue

        result.append(line)

    return "\n".join(result)


# ── Hàm chính ──────────────────────────────────────────────────────

def format_headings(
    text: str,
    timestamp_file: Path | None = None,
    llm_func: Callable[[str], str] | None = None,
    number_sections: bool = True,
    add_separators: bool = True,
    title: str | None = None,
    source: str | None = None,
    content_type: str | None = None,
    context: str | None = None,
) -> str:
    """Xử lý heading theo thứ tự ưu tiên:

    1. Có file timestamp → chèn từ file
    2. Không có file timestamp → bắt buộc dùng LLM phát hiện sections
    3. Chèn H1 title + metadata block nếu được cung cấp
    """
    if timestamp_file:
        headings = parse_timestamp_file(timestamp_file)
        if headings:
            text = insert_headings_from_timestamps(text, headings)
    else:
        if not llm_func:
            raise ValueError("Lỗi: Không có timestamp file và không có LLM. Bắt buộc phải dùng AI để phát hiện sections.")
        text = insert_headings_with_llm(text, llm_func)

    text = number_and_separate(text, number_sections, add_separators)
    text = insert_title_and_metadata(text, title, source, content_type, context)

    return text

