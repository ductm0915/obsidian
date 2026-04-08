# Antigravity

Personal knowledge base powered by Obsidian + LLM processing pipeline.

## Structure

```
├── raw/                     # Immutable source documents
│   ├── articles/            # Web articles, transcripts
│   ├── books/               # Books, PDFs
│   └── assets/              # Images, attachments
├── wiki/                    # LLM-generated wiki pages
│   ├── entities/            # People, organizations, tools
│   ├── concepts/            # Frameworks, mental models
│   ├── sources/             # Per-source summaries
│   ├── topics/              # Topic deep-dives
│   └── analyses/            # Comparisons, reports
├── Text Processing/         # Python pipeline: transcript → article
│   ├── process.py           # Main pipeline runner
│   ├── 01_clean_timestamps.py
│   ├── 02_clean_fillers.py
│   ├── 03_format_headings.py
│   ├── 04_format_inline.py
│   ├── 05_add_metadata.py
│   └── 06_add_takeaways.py
├── SCHEMA.md                # Wiki conventions & instructions
└── .agents/workflows/       # LLM agent workflows
```

## Text Processing Pipeline

Converts raw video transcripts into well-formatted markdown articles.

```
Raw Transcript → Clean Timestamps → Clean Fillers → Format Headings → Format Inline → Add Metadata → Add Takeaways → Output
```

### Usage

```bash
# Full pipeline
python process.py input.md -o output.md

# With LLM formatting (recommended)
python process.py input.md -o output.md --llm gemini

# Format only (skip cleaning)
python process.py input.md --format-only -o output.md

# Add metadata
python process.py input.md --source "Alex Hormozi" --type "Business Advice"

# Process entire directory
python process.py ./raw/ -o ./processed/
```

### Features

- **Heading formatting**: Auto-number sections, insert separators, H1 title + metadata block
- **Inline formatting**: Bold labels, italic quotes, numbered/bullet lists, example labels
- **LLM support**: OpenAI, Gemini, Anthropic for intelligent formatting
- **Regex fallback**: Basic formatting without LLM dependency
