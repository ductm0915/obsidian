#!/bin/bash
WIKI_DIR="/Users/tranmanhduc/Desktop/Antigravity/ductm/wiki"

# 1. Check Index vs Disk
echo "=== Index vs Disk ==="
INDEX_COUNT=$(grep -oh '\[\[[^]]*\]\]' "$WIKI_DIR/index.md" | sed 's/\[\[//;s/\]\]//;s/|.*//' | sort -u | wc -l)
DISK_COUNT=$(find "$WIKI_DIR" -name "*.md" -not -name "log.md" -not -name "index.md" -not -name "overview.md" | wc -l)
echo "Index: $INDEX_COUNT vs Disk: $DISK_COUNT"

# Find files on disk NOT in index
grep -oh '\[\[[^]]*\]\]' "$WIKI_DIR/index.md" | sed 's/\[\[//;s/\]\]//;s/|.*//' | sort -u > /tmp/_wiki_index_slugs.txt
find "$WIKI_DIR" -name "*.md" -not -name "log.md" -not -name "index.md" -not -name "overview.md" | \
  sed 's|.*/||;s|\.md$||' | sort -u > /tmp/_wiki_disk_slugs.txt
UNREGISTERED=$(comm -23 /tmp/_wiki_disk_slugs.txt /tmp/_wiki_index_slugs.txt)
if [ -n "$UNREGISTERED" ]; then
  echo "Files on disk NOT in index:"
  echo "$UNREGISTERED" | sed 's/^/  - /'
else
  echo "✅ All disk files are registered in index"
fi

# 2. Find Missing Frontmatter
echo ""
echo "=== Missing Frontmatter ==="
MISSING_FM=0
find "$WIKI_DIR" -name "*.md" -not -name "log.md" -not -name "index.md" -not -name "overview.md" | while read -r file; do
  slug=$(basename "$file" .md)
  missing=""
  grep -q "^title:" "$file" || missing="$missing title"
  grep -q "^type:" "$file" || missing="$missing type"
  grep -q "^created:" "$file" || missing="$missing created"
  if [ -n "$missing" ]; then echo "  $slug: missing$missing"; MISSING_FM=1; fi
done
[ "$MISSING_FM" -eq 0 ] 2>/dev/null && echo "✅ All files have required frontmatter" || true

# 3. Orphan Check
echo ""
echo "=== Orphan Check ==="
ORPHANS=0
find "$WIKI_DIR" -name "*.md" -not -name "log.md" -not -name "index.md" -not -name "overview.md" | while read -r file; do
  slug=$(basename "$file" .md)
  # Check both [[slug]] and [[slug|...]] formats
  count=$(grep -rl "\[\[$slug\(|\|]\)" "$WIKI_DIR" --include="*.md" --exclude="log.md" --exclude="$(basename "$file")" 2>/dev/null | wc -l)
  if [ "$count" -eq 0 ]; then echo "  $slug is ORPHANED"; ORPHANS=1; fi
done
[ "$ORPHANS" -eq 0 ] 2>/dev/null && echo "✅ No orphaned pages found" || true

# 4. Dead Links (links to non-existent pages) — handles [[slug|alias]] format correctly
echo ""
echo "=== Dead Links ==="
# Extract wikilinks properly: match [[...]] then strip alias and surrounding brackets
grep -roh '\[\[[^]]*\]\]' "$WIKI_DIR/" --include="*.md" --exclude="log.md" | \
  grep -oh '\[\[[^]]*\]\]' | \
  sed 's/\[\[//;s/\]\]//;s/|.*//' | \
  grep -v '#' | grep -v '^$' | \
  sort -u | while read -r link; do
    if ! find "$WIKI_DIR" -name "${link}.md" 2>/dev/null | grep -q .; then
      echo "  Dead link: [[$link]]"
    fi
  done | sort -u
echo "(scan complete)"

echo ""
echo "=== Lint Complete ==="
