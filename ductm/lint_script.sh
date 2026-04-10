#!/bin/bash
WIKI_DIR="/Users/tranmanhduc/Desktop/Antigravity/ductm/wiki"

# 1. Check Index vs Disk
echo "=== Index vs Disk ==="
INDEX_COUNT=$(grep -c "^\- \[\[" "$WIKI_DIR/index.md")
DISK_COUNT=$(find "$WIKI_DIR" -name "*.md" -not -name "log.md" -not -name "index.md" -not -name "overview.md" | wc -l)
echo "Index: $INDEX_COUNT vs Disk: $DISK_COUNT"

# 2. Find Missing Frontmatter
echo "=== Missing Frontmatter ==="
find "$WIKI_DIR" -name "*.md" -not -name "log.md" -not -name "index.md" -not -name "overview.md" | while read -r file; do
  slug=$(basename "$file" .md)
  missing=""
  grep -q "^title:" "$file" || missing="$missing title"
  grep -q "^type:" "$file" || missing="$missing type"
  grep -q "^created:" "$file" || missing="$missing created"
  if [ -n "$missing" ]; then echo "$slug: missing$missing"; fi
done

# 3. Orphan Check
echo "=== Orphan Check ==="
find "$WIKI_DIR" -name "*.md" -not -name "log.md" -not -name "index.md" -not -name "overview.md" | while read -r file; do
  slug=$(basename "$file" .md)
  count=$(grep -rl "\[\[$slug\]\]" "$WIKI_DIR" --exclude="log.md" --exclude="$(basename "$file")" 2>/dev/null | wc -l)
  if [ "$count" -eq 0 ]; then echo "$slug is ORPHANED"; fi
done

# 4. Dead links (links to non-existent pages)
echo "=== Dead Links ==="
grep -roh '\[\[[^]]*\]\]' "$WIKI_DIR/" --exclude="log.md" | sed 's/\[\[//;s/\]\]//' | sort -u | while read -r link; do
  if ! find "$WIKI_DIR" -name "${link}.md" | grep -q .; then
    echo "Dead link found: $link"
  fi
done

