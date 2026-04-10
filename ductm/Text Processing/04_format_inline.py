#!/usr/bin/env python3
"""
Module: Định dạng inline cho nội dung transcript.

Chức năng:
  - Có LLM → LLM format thông minh (bold, italic, quotes, lists, tách đoạn)
  - Không có LLM → regex format cơ bản
  - Bold labels generic (cụm từ viết hoa + : hoặc —)
  - Numbered lists & bullet lists
  - Italic cho quotes nội tuyến
"""
from __future__ import annotations

import re
from typing import Callable

# ── Regex patterns ──────────────────────────────────────────────────

SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z\u00C0-\u024F])")
SENTENCE_END_RE = re.compile(r"[.!?][\"'\u201d\u2019)]*$")


INLINE_PROMPT = """Bạn là chuyên gia biên tập markdown. Hãy format lại đoạn text dưới đây theo quy tắc:

1. **Bold** cho key terms, concepts quan trọng — cả ở đầu dòng (label) lẫn inline trong câu
2. *Italic* cho quotes nội tuyến hoặc nhấn mạnh đặc biệt (VD: *"What would it take?"*)
3. Label ví dụ rõ ràng: **Example —**, **Examples:**, **Case study:**
4. Bold label ở đầu đoạn theo pattern: **Label:** hoặc **Label —** (VD: **Key insight:**, **On vacations:**, **Presentation:**, **Solution:**, **Hack:**, **Application:**)
5. Chuyển quotes thành blockquotes (> "quote" — Author)
6. Tạo bullet points (- item) từ danh sách ngầm trong text
7. Tạo numbered lists (1. item) cho quy trình, framework, bước tuần tự
8. Format framework/steps: 1. **Label — description:** nội dung (VD: 1. **S — Start:** Whatever...)
9. Dùng arrow → cho chuỗi liên kết, flywheels, ví dụ thương hiệu (VD: North Face → Everest → ...)
10. Tách đoạn văn dài thành đoạn ngắn (1-3 câu/đoạn)
11. Giữ nguyên heading (##, ###) và separator (---)

Lưu ý quan trọng:
- Giữ nguyên 100% nội dung gốc và ngôn ngữ gốc. Chỉ thêm markdown formatting, không sửa từ ngữ.
- Không dịch, không tóm tắt, không diễn giải lại, không thêm heading mới.
- Mỗi từ gốc phải xuất hiện y nguyên trong kết quả.
- Trả về text đã format, không giải thích gì thêm.

Text:
---
{text}
---"""


# ── Regex-based utilities ──────────────────────────────────────────

def _split_long_paragraphs(text: str, max_sentences: int = 3) -> str:
    paragraphs = text.split("\n\n")
    result: list[str] = []

    for para in paragraphs:
        stripped = para.strip()

        if (stripped.startswith("#") or
            stripped.startswith(">") or
            stripped.startswith("-") or
            stripped.startswith("*") or
            stripped.startswith("---") or
            stripped.startswith("<!--") or
            re.match(r"\d+[.)]\s", stripped)):
            result.append(para)
            continue

        sentences = SENTENCE_SPLIT_RE.split(stripped)

        if len(sentences) <= max_sentences:
            result.append(para)
            continue

        chunks: list[str] = []
        current: list[str] = []
        for sent in sentences:
            current.append(sent)
            if len(current) >= max_sentences:
                chunks.append(" ".join(current))
                current = []
        if current:
            chunks.append(" ".join(current))

        # Merge incomplete trailing chunk (no sentence ending) into previous chunk
        if len(chunks) > 1 and not SENTENCE_END_RE.search(chunks[-1]):
            last = chunks.pop()
            chunks[-1] = chunks[-1] + " " + last

        result.extend(chunks)

    return "\n\n".join(result)


# ── LLM-based formatting ───────────────────────────────────────────

_SECTION_SEP = re.compile(r"\n\n---\n\n")


def _split_sections(text: str) -> list[str]:
    """Tách text thành các sections theo dấu phân cách ---."""
    return _SECTION_SEP.split(text)


_BATCH_MAX_WORDS = 2000  # Gộp nhiều sections nhỏ thành batch ~2000 từ


def _format_with_llm(text: str, llm_func: Callable[[str], str]) -> str:
    """Format inline qua LLM, gộp sections thành batches lớn để giảm số lần gọi LLM.

    Thay vì gọi LLM cho mỗi section riêng (20-30 calls), gộp thành batches
    ~2000 từ (3-5 calls). Giữ nguyên separator --- trong mỗi batch.
    """
    sections = _split_sections(text)

    # Nếu chỉ 1 section (không có ---), gửi thẳng
    if len(sections) == 1:
        return llm_func(INLINE_PROMPT.format(text=text))

    # Gộp sections thành batches lớn hơn
    batches: list[list[str]] = []
    current_batch: list[str] = []
    current_words = 0

    for section in sections:
        stripped = section.strip()
        word_count = len(stripped.split()) if stripped else 0

        if current_words + word_count > _BATCH_MAX_WORDS and current_batch:
            batches.append(current_batch)
            current_batch = [section]
            current_words = word_count
        else:
            current_batch.append(section)
            current_words += word_count

    if current_batch:
        batches.append(current_batch)

    print(f"  📦 format_inline: {len(sections)} sections → {len(batches)} batches")

    formatted: list[str] = []
    for batch in batches:
        batch_text = "\n\n---\n\n".join(s.strip() for s in batch)
        if not batch_text.strip():
            formatted.append(batch_text)
            continue
        result = llm_func(INLINE_PROMPT.format(text=batch_text))
        formatted.append(result)

    return "\n\n---\n\n".join(formatted)


# ── Hàm chính ──────────────────────────────────────────────────────

def format_inline(
    text: str,
    max_sentences: int = 3,
    llm_func: Callable[[str], str] | None = None,
) -> str:
    """Format inline cho transcript.

    Bắt buộc sử dụng LLM. Nếu không có LLM, báo lỗi vì Regex formatting đã bị loại bỏ.
    """
    if not llm_func:
        raise ValueError("Lỗi: Không có LLM. Chế độ dùng Regex để format đã bị vô hiệu hóa, bắt buộc phải dùng AI.")
    
    # Optional: split long paragraphs before sending to LLM, or let LLM do it.
    text = _split_long_paragraphs(text, max_sentences)
    
    return _format_with_llm(text, llm_func)
