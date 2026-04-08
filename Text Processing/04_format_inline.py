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

# ── Label patterns ─────────────────────────────────────────────────
# Generic: cụm 1-5 từ viết hoa ở đầu dòng, theo sau bởi : hoặc — hoặc -
# Ví dụ: "Key insight:", "My emphasis:", "On vacations:", "Steve Jobs approach:"
# Loại trừ sentence starters để tránh false positives
_SENTENCE_STARTERS = (
    r"(?!(?:Here|This|That|There|It|What|How|Why|When|Where|Who|If|But|And|So|Or"
    r"|Just|Let|As|Now|Well|Then|Also|Because|Since|After|Before|Once|While)\s)"
)
GENERIC_LABEL_RE = re.compile(
    rf"^{_SENTENCE_STARTERS}((?:[A-Z\u00C0-\u024F][a-z\u00C0-\u024F'\"]*(?:\s+(?:of|the|for|on|in|and|vs|not|is|a|an|to|&))?(?:\s+[A-Za-z\u00C0-\u024F'\"]+)*))\s*[:—–-]\s+",
    re.MULTILINE,
)

EXAMPLE_RE = re.compile(
    r"^(For example|Examples?|For instance|Case study|Case in point|Content example)\s*[:—,\-–]\s*",
    re.IGNORECASE | re.MULTILINE,
)

QUOTE_RE = re.compile(
    r'^["\u201c](.+?)["\u201d]\s*[—\-–]\s*(.+?)$',
    re.MULTILINE,
)

# Inline quote: "text" → *"text"* (italic cho nhấn mạnh)
INLINE_QUOTE_RE = re.compile(
    r'(?<!\*)("(?:[^"]{3,80})")\s*(?=[.?!,;]|\s+[A-Z]|$)',
    re.MULTILINE,
)

# Numbered list: dòng bắt đầu bằng số + dấu chấm/phẩy/ngoặc + nội dung
NUMBERED_LIST_RE = re.compile(
    r"^(\d+)[.)]\s+",
    re.MULTILINE,
)

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

Quy tắc quan trọng:
- KHÔNG thêm, bớt, hoặc thay đổi ý nghĩa nội dung
- KHÔNG thêm heading mới
- Trả về text đã format, không giải thích gì thêm

Text:
---
{text}
---"""


# ── Regex-based formatting ──────────────────────────────────────────

def _bold_labels(text: str) -> str:
    def _replace_label(m: re.Match) -> str:
        return f"**{m.group(1)}:** "
    return GENERIC_LABEL_RE.sub(_replace_label, text)


def _format_examples(text: str) -> str:
    def _replace_example(m: re.Match) -> str:
        return f"**{m.group(1)} —** "
    return EXAMPLE_RE.sub(_replace_example, text)


def _format_quotes(text: str) -> str:
    def _replace_quote(m: re.Match) -> str:
        return f'> "{m.group(1)}" — {m.group(2)}'
    return QUOTE_RE.sub(_replace_quote, text)


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


def _format_numbered_lists(text: str) -> str:
    """Chuẩn hóa numbered lists: đảm bảo format `1. content`."""
    return NUMBERED_LIST_RE.sub(r"\1. ", text)


def _format_inline_quotes(text: str) -> str:
    """Italic cho quotes nội tuyến: "text" → *"text"*.

    Bỏ qua dòng heading (##) và dòng đã có bold (**).
    """
    lines = text.splitlines()
    result: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#") or stripped.startswith("**"):
            result.append(line)
        else:
            result.append(INLINE_QUOTE_RE.sub(lambda m: f"*{m.group(1)}*", line))
    return "\n".join(result)


def _format_with_regex(text: str, max_sentences: int = 3) -> str:
    text = _bold_labels(text)
    text = _format_examples(text)
    text = _format_quotes(text)
    text = _format_inline_quotes(text)
    text = _split_long_paragraphs(text, max_sentences)
    text = _format_numbered_lists(text)
    return text


# ── LLM-based formatting ───────────────────────────────────────────

def _format_with_llm(text: str, llm_func: Callable[[str], str]) -> str:
    prompt = INLINE_PROMPT.format(text=text)
    return llm_func(prompt)


# ── Hàm chính ──────────────────────────────────────────────────────

def format_inline(
    text: str,
    max_sentences: int = 3,
    llm_func: Callable[[str], str] | None = None,
) -> str:
    """Format inline cho transcript.

    - Có LLM → format thông minh
    - Không có LLM → format bằng regex
    """
    if llm_func:
        return _format_with_llm(text, llm_func)
    return _format_with_regex(text, max_sentences)
