#!/usr/bin/env python3
"""
Pipeline chính: Xử lý transcript thành article đã format.

Pipeline:
    Raw Transcript → clean_timestamps → clean_fillers → format_headings → format_inline → add_metadata → add_takeaways → Output

Sử dụng:
    # Chạy full pipeline
    python process.py input.md -o output.md

    # Chạy full pipeline, ghi đè file gốc
    python process.py input.md --inplace

    # Chỉ clean (không format)
    python process.py input.md --clean-only -o output.md

    # Chỉ format (không clean)
    python process.py input.md --format-only -o output.md

    # Thêm metadata
    python process.py input.md --source "Alex Hormozi" --type "Business Advice" --context "Key lessons from 2026"

    # Xử lý cả thư mục
    python process.py ./raw_transcripts/ -o ./processed/
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from importlib import import_module

clean_timestamps = import_module("01_clean_timestamps").clean_timestamps
clean_fillers    = import_module("02_clean_fillers").clean_fillers
format_headings  = import_module("03_format_headings").format_headings
format_inline    = import_module("04_format_inline").format_inline
add_metadata     = import_module("05_add_metadata").add_metadata
add_takeaways    = import_module("06_add_takeaways").add_takeaways

MD_EXTENSIONS = {".md", ".txt", ".markdown"}

# ── LLM factory ─────────────────────────────────────────────────────

def create_llm_func(provider: str, model: str | None = None):
    """Tạo llm_func(prompt) → response từ provider.

    Bạn cần cài SDK tương ứng và set API key trong env:
      - openai:    pip install openai,    OPENAI_API_KEY
      - gemini:    pip install google-genai, GEMINI_API_KEY
      - anthropic: pip install anthropic, ANTHROPIC_API_KEY
    """
    provider = provider.lower()

    if provider == "openai":
        from openai import OpenAI
        client = OpenAI()
        m = model or "gpt-4o"
        def _call(prompt: str) -> str:
            r = client.chat.completions.create(
                model=m,
                messages=[{"role": "user", "content": prompt}],
            )
            return r.choices[0].message.content
        return _call

    if provider == "gemini":
        from google import genai
        client = genai.Client()
        m = model or "gemini-2.0-flash"
        def _call(prompt: str) -> str:
            r = client.models.generate_content(model=m, contents=prompt)
            return r.text
        return _call

    if provider == "anthropic":
        import anthropic
        client = anthropic.Anthropic()
        m = model or "claude-sonnet-4-20250514"
        def _call(prompt: str) -> str:
            r = client.messages.create(
                model=m,
                max_tokens=8192,
                messages=[{"role": "user", "content": prompt}],
            )
            return r.content[0].text
        return _call

    raise SystemExit(f"Provider không hỗ trợ: {provider}. Dùng: openai, gemini, anthropic")


def run_pipeline(
    text: str,
    *,
    # Bật/tắt từng bước
    do_clean_timestamps: bool = True,
    do_clean_fillers: bool = True,
    do_format_headings: bool = True,
    do_format_inline: bool = True,
    do_add_metadata: bool = True,
    do_add_takeaways: bool = True,
    # Tham số cho từng module
    lines_per_para: int = 8,
    remove_openers: bool = False,
    timestamp_file: Path | None = None,
    llm_func: object = None,
    number_sections: bool = True,
    add_separators: bool = True,
    max_sentences: int = 3,
    source: str = "",
    content_type: str = "",
    context: str = "",
) -> str:
    """Chạy pipeline xử lý transcript.

    Args:
        text: Nội dung transcript gốc.
        do_*: Bật/tắt từng bước xử lý.
        Các tham số còn lại: tuỳ chỉnh cho từng module.

    Returns:
        Text đã xử lý qua pipeline.
    """
    # ── CLEAN ──
    if do_clean_timestamps:
        text = clean_timestamps(text, lines_per_para=lines_per_para)

    if do_clean_fillers:
        text = clean_fillers(text, remove_openers=remove_openers)

    # ── FORMAT ──
    if do_format_headings:
        text = format_headings(
            text,
            timestamp_file=timestamp_file,
            llm_func=llm_func,
            number_sections=number_sections,
            add_separators=add_separators,
        )

    if do_format_inline:
        text = format_inline(text, max_sentences=max_sentences, llm_func=llm_func)

    # ── METADATA & TAKEAWAYS ──
    if do_add_metadata:
        text = add_metadata(
            text,
            source=source,
            content_type=content_type,
            context=context,
        )

    if do_add_takeaways:
        text = add_takeaways(text)

    return text


def process_file(
    src: Path,
    dst: Path | None,
    **pipeline_kwargs,
) -> None:
    """Xử lý một file."""
    text = src.read_text(encoding="utf-8", errors="ignore")
    result = run_pipeline(text, **pipeline_kwargs)

    out_path = dst or src
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(result + "\n", encoding="utf-8")
    print(f"  ✓ {src.name} → {out_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Pipeline xử lý transcript → article. Kết nối các module: clean_timestamps, clean_fillers, format_headings, format_inline, add_metadata, add_takeaways.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # Input/Output
    parser.add_argument("src", help="File hoặc thư mục cần xử lý")
    parser.add_argument("-o", "--output", help="File hoặc thư mục output (mặc định: in ra stdout)")
    parser.add_argument("--inplace", action="store_true", help="Ghi đè file gốc (tạo .bak trước)")
    parser.add_argument("--no-backup", action="store_true", help="Không tạo file .bak khi dùng --inplace")

    # Pipeline mode
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--clean-only", action="store_true", help="Chỉ chạy bước clean")
    mode.add_argument("--format-only", action="store_true", help="Chỉ chạy bước format")

    # Clean options
    clean_group = parser.add_argument_group("Clean options")
    clean_group.add_argument("-n", "--lines-per-para", type=int, default=8, help="Số dòng tối đa mỗi đoạn (mặc định: 8)")
    clean_group.add_argument("--remove-openers", action="store_true", help="Xoá câu mở đầu filler (So, All right, ...)")

    # LLM options
    llm_group = parser.add_argument_group("LLM options")
    llm_group.add_argument("--llm", metavar="PROVIDER", help="Dùng LLM để format (ví dụ: openai, gemini, anthropic)")
    llm_group.add_argument("--llm-model", metavar="MODEL", help="Tên model (ví dụ: gpt-4o, gemini-2.0-flash, claude-sonnet-4-20250514)")

    # Format options
    fmt_group = parser.add_argument_group("Format options")
    fmt_group.add_argument("-t", "--timestamps", help="File timestamp để chèn heading (mỗi dòng: 0:00 Tiêu đề)")
    fmt_group.add_argument("--no-number", action="store_true", help="Không đánh số sections")
    fmt_group.add_argument("--no-separators", action="store_true", help="Không thêm --- giữa sections")
    fmt_group.add_argument("--max-sentences", type=int, default=3, help="Số câu tối đa mỗi đoạn (mặc định: 3)")

    # Metadata options
    meta_group = parser.add_argument_group("Metadata options")
    meta_group.add_argument("--source", default="", help="Nguồn (ví dụ: 'Alex Hormozi')")
    meta_group.add_argument("--type", dest="content_type", default="", help="Loại nội dung")
    meta_group.add_argument("--context", default="", help="Ngữ cảnh")
    meta_group.add_argument("--no-metadata", action="store_true", help="Không thêm metadata")
    meta_group.add_argument("--no-takeaways", action="store_true", help="Không thêm Key Takeaways")

    args = parser.parse_args()

    # Xác định bước nào được bật
    timestamp_file = Path(args.timestamps).resolve() if args.timestamps else None
    if timestamp_file and not timestamp_file.exists():
        raise SystemExit(f"Không tìm thấy file timestamps: {timestamp_file}")

    llm_func = create_llm_func(args.llm, args.llm_model) if args.llm else None

    pipeline_kwargs = {
        "lines_per_para": args.lines_per_para,
        "remove_openers": args.remove_openers,
        "timestamp_file": timestamp_file,
        "llm_func": llm_func,
        "number_sections": not args.no_number,
        "add_separators": not args.no_separators,
        "max_sentences": args.max_sentences,
        "source": args.source,
        "content_type": args.content_type,
        "context": args.context,
    }

    if args.clean_only:
        pipeline_kwargs.update(
            do_format_headings=False,
            do_format_inline=False,
            do_add_metadata=False,
            do_add_takeaways=False,
        )
    elif args.format_only:
        pipeline_kwargs.update(
            do_clean_timestamps=False,
            do_clean_fillers=False,
        )
    else:
        pipeline_kwargs.update(
            do_add_metadata=not args.no_metadata,
            do_add_takeaways=not args.no_takeaways,
        )

    src = Path(args.src).resolve()

    if not src.exists():
        raise SystemExit(f"Không tìm thấy: {src}")

    # Xử lý single file
    if src.is_file():
        if args.inplace:
            if not args.no_backup:
                shutil.copy2(src, src.with_suffix(src.suffix + ".bak"))
            process_file(src, None, **pipeline_kwargs)
        elif args.output:
            process_file(src, Path(args.output).resolve(), **pipeline_kwargs)
        else:
            # Stdout mode
            text = src.read_text(encoding="utf-8", errors="ignore")
            result = run_pipeline(text, **pipeline_kwargs)
            print(result)
        return

    # Xử lý directory
    files = [f for f in src.rglob("*") if f.is_file() and f.suffix in MD_EXTENSIONS]

    if not files:
        raise SystemExit(f"Không tìm thấy file .md/.txt trong: {src}")

    out_dir = Path(args.output).resolve() if args.output else None

    for fpath in sorted(files):
        if args.inplace:
            if not args.no_backup:
                shutil.copy2(fpath, fpath.with_suffix(fpath.suffix + ".bak"))
            process_file(fpath, None, **pipeline_kwargs)
        elif out_dir:
            rel = fpath.relative_to(src)
            dst = out_dir / rel
            process_file(fpath, dst, **pipeline_kwargs)
        else:
            text = fpath.read_text(encoding="utf-8", errors="ignore")
            result = run_pipeline(text, **pipeline_kwargs)
            print(f"\n{'='*60}\n{fpath.name}\n{'='*60}")
            print(result)

    print(f"\nDONE: {len(files)} files processed.")


if __name__ == "__main__":
    main()
