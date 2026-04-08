#!/usr/bin/env python3
"""
Module: Xoá filler words, transcript markers, speaker markers.

Chức năng:
  - Xoá filler words: um, uh (khi dùng như filler, không phải trong từ)
  - Xoá transcript markers: [laughter], [applause], [music], [snorts], etc.
  - Xoá speaker markers: >> (dấu hiệu chuyển người nói)
  - Xoá câu mở đầu thừa: "So,", "All right,", "So, here's..."
"""
from __future__ import annotations

import re

# Filler words đứng riêng hoặc đầu câu (word boundary)
FILLER_RE = re.compile(
    r"\b(um|uh|uh huh)\b[,.]?\s*",
    re.IGNORECASE,
)

# Transcript markers trong ngoặc vuông
MARKER_RE = re.compile(
    r"\[(laughter|laughing|applause|music|snorts|coughs?|sighs?|gasps?|clears? throat|inaudible|crosstalk)\]",
    re.IGNORECASE,
)

# Speaker markers: >> hoặc >> Name:
SPEAKER_RE = re.compile(r"^\s*>>\s*(\w+\s*:)?\s*", re.MULTILINE)

# Câu mở đầu filler phổ biến trong transcript
OPENER_RE = re.compile(
    r"^(So,?\s+|All right[,.]?\s+|Okay[,.]?\s+|Well[,.]?\s+|Now[,.]?\s+|And so[,.]?\s+)",
    re.IGNORECASE | re.MULTILINE,
)


def clean_fillers(text: str, remove_openers: bool = False) -> str:
    """Xoá filler words, markers, speaker marks khỏi transcript.

    Args:
        text: Nội dung transcript.
        remove_openers: Có xoá câu mở đầu filler không (mặc định False vì có thể
                        làm mất nghĩa trong một số trường hợp).

    Returns:
        Text đã dọn dẹp.
    """
    # Xoá transcript markers trước (ít ảnh hưởng nhất)
    text = MARKER_RE.sub("", text)

    # Xoá speaker markers
    text = SPEAKER_RE.sub("", text)

    # Xoá filler words
    text = FILLER_RE.sub("", text)

    # Optional: xoá câu mở đầu filler
    if remove_openers:
        text = OPENER_RE.sub("", text)

    # Dọn dẹp khoảng trắng thừa sau khi xoá
    text = re.sub(r"  +", " ", text)          # nhiều space → 1 space
    text = re.sub(r" ([,.])", r"\1", text)    # space trước dấu câu
    text = re.sub(r"^\s+$", "", text, flags=re.MULTILINE)  # dòng chỉ có space

    return text
