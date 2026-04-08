#!/usr/bin/env python3
"""Runner tạm: chạy pipeline với chapter_headings từ SRT timestamps."""
import re
from pathlib import Path
from importlib import import_module

clean_timestamps = import_module("01_clean_timestamps").clean_timestamps
clean_fillers    = import_module("02_clean_fillers").clean_fillers
format_headings  = import_module("03_format_headings").format_headings
format_inline    = import_module("04_format_inline").format_inline
add_metadata     = import_module("05_add_metadata").add_metadata
add_takeaways    = import_module("06_add_takeaways").add_takeaways

# ── Chapter headings từ timestamps ────────────────────────────────
def ts_to_sec(ts: str) -> int:
    h, m, s = map(int, ts.split(":"))
    return h * 3600 + m * 60 + s

CHAPTERS = {
    ts_to_sec("00:10:44"): "## Who is this video for?",
    ts_to_sec("00:21:03"): "## How are we going to wrap this video?",
    ts_to_sec("01:09:08"): "## Outline the video",
    ts_to_sec("02:42:50"): "## Make a decision: Scripted or Outlined",
    ts_to_sec("02:49:48"): "## Script Introduction",
    ts_to_sec("03:39:49"): "## Develop your production plan",
}

SRC = Path("/Users/tranmanhduc/Desktop/Antigravity/Tran Manh Duc/ductm/raw/articles/Caleb Ralston/Content Strategy Workshop.md")
DST = Path("/Users/tranmanhduc/Desktop/Antigravity/Tran Manh Duc/ductm/raw/articles/Caleb Ralston/Content Strategy Workshop.md")
TMP = DST.with_suffix(".tmp.md")

print("Reading...")
text = SRC.read_text(encoding="utf-8", errors="ignore")

# Bỏ metadata header cũ nếu có (do run trước để lại)
text = re.sub(r"^\*\*Source:\*\*.*?\n(\*\*Type:\*\*.*?\n)?(\*\*Context:\*\*.*?\n)?\n*", "", text, flags=re.MULTILINE)

print(f"  → {len(text)} chars sau khi bỏ header cũ")

print("Step 1: clean_timestamps (với chapter headings)...")
text = clean_timestamps(text, lines_per_para=8, chapter_headings=CHAPTERS, tolerance=30)
print(f"  → {len(text)} chars")

print("Step 2: clean_fillers...")
text = clean_fillers(text, remove_openers=True)

print("Step 3: format_headings (no LLM, headings đã có)...")
text = format_headings(text, llm_func=None, number_sections=True, add_separators=True)

print("Step 4: format_inline (regex)...")
text = format_inline(text, max_sentences=3, llm_func=None)

print("Step 5: add_metadata...")
text = add_metadata(text, source="Caleb Ralston", content_type="Content Strategy")

print("Step 6: add_takeaways...")
text = add_takeaways(text)

# Ghi ra file tạm trước, rồi rename (tránh corrupt nếu src == dst)
TMP.write_text(text + "\n", encoding="utf-8")
TMP.replace(DST)
print(f"Done → {DST} ({DST.stat().st_size} bytes)")
