#!/usr/bin/env python3
"""
Pipeline chính: Xử lý transcript thành article đã format.

Pipeline:
    Raw Transcript → clean_timestamps → clean_fillers → format_headings → format_inline → add_metadata → add_takeaways → Output

Sử dụng:
    # Chạy full pipeline (dùng Claude Code CLI cho LLM)
    python process.py input.md -o output.md

    # Chạy full pipeline, ghi đè file gốc
    python process.py input.md --inplace

    # Chỉ clean (không format)
    python process.py input.md --clean-only -o output.md

    # Chỉ format (không clean)
    python process.py input.md --format-only -o output.md

    # Tắt LLM, chỉ dùng regex
    python process.py input.md --no-llm -o output.md

    # Thêm metadata
    python process.py input.md --source "Alex Hormozi" --type "Business Advice" --context "Key lessons from 2026"

    # Xử lý cả thư mục
    python process.py ./raw_transcripts/ -o ./processed/
"""
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

from importlib import import_module

clean_timestamps     = import_module("01_clean_timestamps").clean_timestamps
clean_fillers        = import_module("02_clean_fillers").clean_fillers
format_headings      = import_module("03_format_headings").format_headings
parse_timestamp_file = import_module("03_format_headings").parse_timestamp_file
format_inline        = import_module("04_format_inline").format_inline
add_metadata         = import_module("05_add_metadata").add_metadata
add_takeaways        = import_module("06_add_takeaways").add_takeaways


# ── Content Integrity Validation ─────────────────────────────────────

import re as _re

# Regex to strip markdown formatting syntax (bold, italic, headings, etc.)
_MD_SYNTAX_RE = _re.compile(
    r'(\*\*|\*|__|_|`{1,3}|#{1,6}\s|>\s|---\s*$|\d+\.\s|-\s|→)',
    _re.MULTILINE,
)


def _extract_words(text: str) -> list[str]:
    """Trích xuất danh sách từ (words) từ text, loại bỏ markdown syntax."""
    cleaned = _MD_SYNTAX_RE.sub(' ', text)
    return cleaned.split()


def _detect_language_block(text: str) -> str:
    """Phát hiện ngôn ngữ chính của text dựa trên tỷ lệ ký tự Unicode.

    Returns:
        'vi' nếu có nhiều ký tự tiếng Việt (dấu)
        'en' nếu chủ yếu là ASCII
        'mixed' nếu hỗn hợp
    """
    if not text.strip():
        return 'unknown'

    # Đếm ký tự có dấu tiếng Việt (combining marks hoặc precomposed)
    viet_chars = 0
    ascii_alpha = 0
    for ch in text:
        if ch.isalpha():
            if ord(ch) < 128:
                ascii_alpha += 1
            else:
                # Ký tự non-ASCII alphabetic → likely Vietnamese/accented
                viet_chars += 1

    total = viet_chars + ascii_alpha
    if total == 0:
        return 'unknown'

    viet_ratio = viet_chars / total
    if viet_ratio > 0.15:
        return 'vi'
    elif viet_ratio < 0.02:
        return 'en'
    return 'mixed'


def validate_content_integrity(
    original: str,
    result: str,
    step_name: str,
    max_word_change_pct: float = 0.15,
) -> str:
    """Kiểm tra tính toàn vẹn nội dung sau khi LLM xử lý.

    Checks:
      1. Word count: không được thay đổi quá max_word_change_pct (mặc định 15%)
      2. Language: ngôn ngữ output phải giống ngôn ngữ input

    Args:
        original: Text trước khi LLM xử lý.
        result: Text sau khi LLM xử lý.
        step_name: Tên bước (để hiển thị warning).
        max_word_change_pct: Ngưỡng thay đổi word count cho phép.

    Returns:
        result nếu pass validation, original nếu fail (kèm warning).
    """
    orig_words = _extract_words(original)
    result_words = _extract_words(result)

    orig_count = len(orig_words)
    result_count = len(result_words)

    # ── Check 1: Word count ──
    if orig_count > 0:
        change_pct = abs(result_count - orig_count) / orig_count
        if change_pct > max_word_change_pct:
            diff = result_count - orig_count
            direction = "THÊM" if diff > 0 else "XOÁ"
            print(f"  ⚠️  [{step_name}] CẢNH BÁO: LLM đã {direction} {abs(diff)} từ ({change_pct:.0%} thay đổi)!")
            print(f"       Gốc: {orig_count} từ → Kết quả: {result_count} từ")
            print(f"       → Giữ nguyên bản gốc để bảo toàn nội dung.")
            return original

    # ── Check 2: Language consistency ──
    orig_lang = _detect_language_block(original)
    result_lang = _detect_language_block(result)

    if orig_lang != 'unknown' and result_lang != 'unknown' and orig_lang != result_lang:
        print(f"  ⚠️  [{step_name}] CẢNH BÁO: Ngôn ngữ bị thay đổi! ({orig_lang} → {result_lang})")
        print(f"       LLM có thể đã dịch nội dung. Giữ nguyên bản gốc.")
        return original

    return result


def create_validated_llm_func(llm_func, step_name: str, max_word_change_pct: float = 0.15):
    """Bọc llm_func với validation tự động + early-stop.

    Sau mỗi lần gọi LLM, tự động kiểm tra:
    - Word count không thay đổi quá max_word_change_pct
    - Ngôn ngữ không bị thay đổi

    Early-stop: nếu validation fail 3 lần liên tiếp → bỏ qua LLM calls còn lại,
    trả về text gốc ngay lập tức (tiết kiệm ~30s/call).

    Args:
        max_word_change_pct: Ngưỡng thay đổi word count cho phép.
            - format_headings: 0.15 (chỉ chèn dòng heading, nội dung không đổi)
            - format_inline: 0.35 (cho phép chuyển prose → bullet list, loại bỏ từ nối)
    """
    consecutive_failures = [0]  # mutable container để closure có thể modify
    MAX_CONSECUTIVE_FAILURES = 3

    def _validated_call(prompt: str) -> str:
        # Trích xuất text gốc từ prompt
        # Prompt format: "...instruction...\nText:\n---\n{content}\n---"
        # Content có thể chứa --- (horizontal rules), nên phải tìm đúng boundaries
        start_marker = "\n---\n"
        end_marker = "\n---"

        start_idx = prompt.find(start_marker)
        end_idx = prompt.rfind(end_marker)  # rfind = tìm từ cuối

        if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
            original_text = prompt[start_idx + len(start_marker):end_idx].strip()
        else:
            original_text = prompt

        # Early-stop: nếu đã fail quá nhiều lần liên tiếp → skip LLM
        if consecutive_failures[0] >= MAX_CONSECUTIVE_FAILURES:
            print(f"  ⏭️  [{step_name}] Bỏ qua LLM (đã fail {consecutive_failures[0]} lần liên tiếp). Giữ nguyên bản gốc.")
            return original_text

        result = llm_func(prompt)
        validated = validate_content_integrity(original_text, result, step_name, max_word_change_pct)

        # Track consecutive failures
        if validated == original_text and result != original_text:
            consecutive_failures[0] += 1
        else:
            consecutive_failures[0] = 0  # Reset khi thành công

        return validated

    # Expose reset function để reset giữa các file
    def _reset():
        consecutive_failures[0] = 0

    _validated_call.reset_failures = _reset
    return _validated_call




def _ts_str_to_seconds(ts: str) -> int:
    """'H:MM:SS' hoặc 'MM:SS' → tổng số giây."""
    parts = ts.split(":")
    if len(parts) == 3:
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
    return int(parts[0]) * 60 + int(parts[1])


_SENT_END = _re.compile(r'[.!?]["\u201d\u2019)]*$')


def _merge_broken_paragraphs(text: str) -> str:
    """Merge các đoạn kết thúc giữa câu (không có .!?) vào đoạn tiếp theo.

    Xử lý artifact từ việc chia SRT theo batch line trước khi sentence kết thúc.
    Không merge nếu đoạn tiếp theo là heading hoặc separator.
    """
    paras = text.split("\n\n")
    for _ in range(5):
        merged: list[str] = []
        changed = False
        i = 0
        while i < len(paras):
            p = paras[i]
            stripped = p.strip()
            if (
                stripped
                and not stripped.startswith("#")
                and not stripped.startswith("---")
                and not stripped.startswith(">")
                and not stripped.startswith("-")
                and not _SENT_END.search(stripped)
                and i + 1 < len(paras)
                and not paras[i + 1].strip().startswith("#")
                and not paras[i + 1].strip().startswith("---")
            ):
                paras[i + 1] = stripped + " " + paras[i + 1].strip()
                changed = True
            else:
                merged.append(p)
            i += 1
        paras = merged
        if not changed:
            break
    return "\n\n".join(paras)

MD_EXTENSIONS = {".md", ".txt", ".markdown"}

# ── LLM via Claude Code CLI (OAuth) ─────────────────────────────────

import shutil
import time
import glob


def _find_claude_binary() -> str:
    """Tìm đường dẫn tới Claude Code CLI binary.

    Thứ tự ưu tiên:
      1. `claude` có sẵn trong PATH
      2. Claude Code app bundle (macOS)
      3. Claude Code VM binary
    """
    # 1. Kiểm tra PATH trước
    path = shutil.which("claude")
    if path:
        return path

    # 2. Claude Code app bundle (macOS) — tìm version mới nhất
    app_pattern = str(
        Path.home()
        / "Library/Application Support/Claude/claude-code/*/claude.app/Contents/MacOS/claude"
    )
    app_matches = sorted(glob.glob(app_pattern), reverse=True)
    if app_matches:
        return app_matches[0]

    # 3. Claude Code VM binary — tìm version mới nhất
    vm_pattern = str(
        Path.home()
        / "Library/Application Support/Claude/claude-code-vm/*/claude"
    )
    vm_matches = sorted(glob.glob(vm_pattern), reverse=True)
    if vm_matches:
        return vm_matches[0]

    raise SystemExit(
        "❌ Không tìm thấy Claude Code CLI.\n"
        "   Hãy đảm bảo Claude Code Extension đã được cài đặt trong IDE.\n"
        "   Hoặc thêm `claude` vào PATH."
    )


def create_llm_func(max_retries: int = 10, base_wait: float = 20.0):
    """Tạo llm_func(prompt) → response qua Claude Code CLI (OAuth).

    Features:
      - Tự động tìm claude binary (không cần thêm vào PATH)
      - Retry tự động khi bị rate-limit (tối đa max_retries lần)
      - Exponential backoff giữa các lần retry
    """
    claude_bin = _find_claude_binary()
    print(f"  🤖 Claude CLI: {claude_bin}")

    def _call(prompt: str) -> str:
        for attempt in range(1, max_retries + 1):
            result = subprocess.run(
                [claude_bin, "--print"],
                input=prompt,
                capture_output=True,
                text=True,
            )

            output = result.stdout.strip()
            stderr = result.stderr.strip()

            # Thành công
            if result.returncode == 0 and output:
                return output

            # Rate limit — retry với backoff
            combined = (output + " " + stderr).lower()
            if "limit" in combined or "rate" in combined or "reset" in combined:
                wait_time = base_wait * (2 ** (attempt - 1))  # 10s, 20s, 40s, 80s, 160s
                print(f"  ⏳ Rate limit (lần {attempt}/{max_retries}). Chờ {wait_time:.0f}s...")
                time.sleep(wait_time)
                continue

            # Lỗi khác — dừng ngay
            error_msg = stderr or output or "(không có output)"
            raise SystemExit(
                f"❌ Claude CLI lỗi (exit code {result.returncode}):\n"
                f"   {error_msg}\n"
                f"   Hãy kiểm tra OAuth session trong Claude Code Extension."
            )

        raise SystemExit(
            f"❌ Đã thử {max_retries} lần nhưng vẫn bị rate-limited.\n"
            f"   Hãy đợi một lúc rồi chạy lại."
        )

    return _call


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
    llm_headings: object = None,
    llm_inline: object = None,
    number_sections: bool = True,
    add_separators: bool = True,
    max_sentences: int = 3,
    title: str = "",
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
    # Nếu có timestamp file, chuyển thành chapter_headings để clean_timestamps
    # chèn headings trực tiếp vào SRT (trước khi xoá timestamps).
    chapter_headings = None
    ts_file_for_format = timestamp_file
    if do_clean_timestamps and timestamp_file:
        raw_headings = parse_timestamp_file(timestamp_file)
        chapter_headings = {_ts_str_to_seconds(ts): heading for ts, heading in raw_headings.items()}
        ts_file_for_format = None  # headings đã được chèn bởi clean_timestamps

    if do_clean_timestamps:
        text = clean_timestamps(text, lines_per_para=lines_per_para, chapter_headings=chapter_headings)

    if do_clean_fillers:
        text = clean_fillers(text, remove_openers=remove_openers)

    # ── FORMAT ──
    # Sử dụng validated LLM func nếu có, fallback về llm_func gốc
    _llm_headings = llm_headings or llm_func
    _llm_inline = llm_inline or llm_func

    if do_format_headings:
        text = format_headings(
            text,
            timestamp_file=ts_file_for_format,
            llm_func=_llm_headings,
            number_sections=number_sections,
            add_separators=add_separators,
            title=title or None,
        )

    if do_format_inline:
        text = format_inline(text, max_sentences=max_sentences, llm_func=_llm_inline)

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

    # ── FINAL CLEANUP ──
    # Merge các đoạn bị cắt giữa câu (artifact từ SRT batch processing)
    text = _merge_broken_paragraphs(text)

    return text


def process_file(
    src: Path,
    dst: Path | None,
    **pipeline_kwargs,
) -> None:
    """Xử lý một file."""
    # Reset validation failure counters cho mỗi file mới
    for key in ('llm_headings', 'llm_inline'):
        func = pipeline_kwargs.get(key)
        if func and hasattr(func, 'reset_failures'):
            func.reset_failures()

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
    parser.add_argument("--inplace", action="store_true", help="Ghi đè file gốc")

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
    # --no-llm removed as per user requirement, MUST USE LLM


    # Format options
    fmt_group = parser.add_argument_group("Format options")
    fmt_group.add_argument("-t", "--timestamps", help="File timestamp để chèn heading (mỗi dòng: 0:00 Tiêu đề)")
    fmt_group.add_argument("--no-number", action="store_true", help="Không đánh số sections")
    fmt_group.add_argument("--no-separators", action="store_true", help="Không thêm --- giữa sections")
    fmt_group.add_argument("--max-sentences", type=int, default=3, help="Số câu tối đa mỗi đoạn (mặc định: 3)")

    # Metadata options
    meta_group = parser.add_argument_group("Metadata options")
    meta_group.add_argument("--title", default="", help="Tiêu đề H1 (nếu không có sẵn trong file)")
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

    # Khởi tạo LLM connector bắt buộc
    raw_llm_func = create_llm_func()

    # Bọc LLM func với validation (tùy bước sẽ set step_name khác)
    # Validation sẽ được áp dụng trong từng module khi gọi llm_func
    llm_func = raw_llm_func

    # Tạo validated versions cho từng bước (ngưỡng khác nhau)
    # headings: 25% — LLM thêm heading nhưng cũng cleanup nhẹ filler words
    # inline:   35% — cho phép chuyển prose → bullet/list (từ nối bị loại bỏ hợp lệ)
    llm_headings = create_validated_llm_func(raw_llm_func, "format_headings", max_word_change_pct=0.25)
    llm_inline   = create_validated_llm_func(raw_llm_func, "format_inline",   max_word_change_pct=0.35)


    pipeline_kwargs = {
        "lines_per_para": args.lines_per_para,
        "remove_openers": args.remove_openers,
        "timestamp_file": timestamp_file,
        "llm_func": llm_func,
        "llm_headings": llm_headings,
        "llm_inline": llm_inline,
        "number_sections": not args.no_number,
        "add_separators": not args.no_separators,
        "max_sentences": args.max_sentences,
        "title": args.title,
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
