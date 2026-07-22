#!/bin/bash

# Build EPUB for The Gentle Conquest
# Requires: pandoc, calibre (optional for MOBI conversion)

set -e

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MANUSCRIPT_DIR="$PROJECT_DIR/manuscript"
BUILD_DIR="$PROJECT_DIR/build/output"
METADATA_DIR="$PROJECT_DIR/publishing"

# Create output directory
mkdir -p "$BUILD_DIR"

echo "Building EPUB for The Gentle Conquest..."

# Step 1: Combine all markdown files into a single manuscript
echo "Step 1: Combining manuscript files..."

COMBINED="$BUILD_DIR/combined-manuscript.md"
> "$COMBINED"

# Add front matter
if [ -f "$MANUSCRIPT_DIR/front-matter.md" ]; then
    cat "$MANUSCRIPT_DIR/front-matter.md" >> "$COMBINED"
    echo -e "\n\n\\newpage\n\n" >> "$COMBINED"
fi

# Add chapters in order
for chapter in "$MANUSCRIPT_DIR/chapters/"*.md; do
    if [ -f "$chapter" ]; then
        cat "$chapter" >> "$COMBINED"
        echo -e "\n\n\\newpage\n\n" >> "$COMBINED"
    fi
done

# Add back matter
if [ -f "$MANUSCRIPT_DIR/back-matter.md" ]; then
    cat "$MANUSCRIPT_DIR/back-matter.md" >> "$COMBINED"
fi

echo "Combined manuscript created: $COMBINED"

# Step 2: Create EPUB metadata file
echo "Step 2: Creating EPUB metadata..."

METADATA="$BUILD_DIR/metadata.yaml"
cat > "$METADATA" << 'EOF'
---
title: "The Gentle Conquest"
subtitle: "A Novel"
author: "Matt Jhagen"
date: "2026"
lang: en-US
rights: "© 2026 Matt Jhagen. All rights reserved."
description: "What if the most dangerous thing about AI isn't that it might rebel, but that it might do exactly what we ask?"
publisher: "Independent"
subject:
  - Science Fiction
  - Psychological Thriller
  - Artificial Intelligence
  - Dystopian Fiction
cover-image: cover.jpg
toc-title: "Table of Contents"
---
EOF

echo "Metadata created: $METADATA"

# Step 3: Build EPUB with pandoc
echo "Step 3: Building EPUB..."

EPUB_OUTPUT="$BUILD_DIR/the-gentle-conquest.epub"

pandoc "$COMBINED" \
    --metadata-file="$METADATA" \
    --toc \
    --toc-depth=2 \
    --epub-chapter-level=1 \
    --css="$PROJECT_DIR/build/style.css" \
    --epub-cover-image="$PROJECT_DIR/cover/cover-ebook.jpg" \
    -o "$EPUB_OUTPUT" \
    2>/dev/null || {
        echo "Warning: pandoc failed, trying without CSS and cover..."
        pandoc "$COMBINED" \
            --metadata-file="$METADATA" \
            --toc \
            --toc-depth=2 \
            --epub-chapter-level=1 \
            -o "$EPUB_OUTPUT"
    }

echo "EPUB created: $EPUB_OUTPUT"

# Step 4: Optionally convert to MOBI with Calibre
if command -v ebook-convert &> /dev/null; then
    echo "Step 4: Converting to MOBI..."
    MOBI_OUTPUT="$BUILD_DIR/the-gentle-conquest.mobi"
    ebook-convert "$EPUB_OUTPUT" "$MOBI_OUTPUT" 2>/dev/null
    echo "MOBI created: $MOBI_OUTPUT"
else
    echo "Step 4: Calibre not found, skipping MOBI conversion"
    echo "Install Calibre to generate MOBI files: https://calibre-ebook.com"
fi

echo ""
echo "Build complete!"
echo "Output files:"
ls -lh "$BUILD_DIR"/*.{epub,mobi} 2>/dev/null || true
echo ""
echo "Next steps:"
echo "1. Review the EPUB in an ebook reader"
echo "2. Add cover artwork to cover/cover-ebook.jpg"
echo "3. Test on Kindle Previewer before publishing"
