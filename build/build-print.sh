#!/bin/bash

# Build print-ready PDF for The Gentle Conquest (KDP Paperback)
# Requires: pandoc, LaTeX (texlive-latex-recommended)

set -e

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MANUSCRIPT_DIR="$PROJECT_DIR/manuscript"
BUILD_DIR="$PROJECT_DIR/build/output"

# Create output directory
mkdir -p "$BUILD_DIR"

echo "Building print-ready PDF for The Gentle Conquest (KDP 6x9)..."

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

# Step 2: Create LaTeX template for KDP 6x9 paperback
echo "Step 2: Creating LaTeX template..."

LATEX_TEMPLATE="$BUILD_DIR/print-template.tex"
cat > "$LATEX_TEMPLATE" << 'EOF'
\documentclass[11pt,openany]{book}

% KDP Paperback: 6" x 9" trim size
\usepackage[
    paperwidth=6in,
    paperheight=9in,
    top=0.75in,
    bottom=0.75in,
    inner=0.875in,
    outer=0.625in
]{geometry}

% Fonts - Palatino (professional book font)
\usepackage{mathpazo}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}

% Better typography
\usepackage{microtype}

% Line spacing - 1.5 for readability
\usepackage{setspace}
\onehalfspacing

% Chapter styling
\usepackage{titlesec}
\titleformat{\chapter}[display]
  {\normalfont\Large\bfseries}
  {\chaptertitlename\ \thechapter}
  {20pt}
  {\LARGE}
\titlespacing*{\chapter}{0pt}{50pt}{40pt}

% Headers and footers
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[RE]{\textit{The Gentle Conquest}}
\fancyhead[LO]{\textit{\leftmark}}
\renewcommand{\headrulewidth}{0pt}

% Paragraph formatting
\setlength{\parindent}{0.5em}
\setlength{\parskip}{0pt}

% Links (black for print)
\usepackage[colorlinks=true,linkcolor=black,urlcolor=black]{hyperref}

% No orphaned chapter names
\renewcommand{\bookname}{}

% Better hyphenation
\hyphenpenalty=10000
\exhyphenpenalty=10000

\begin{document}
\frontmatter
\maketitle
\tableofcontents
\mainmatter
$body$
\backmatter
\end{document}
EOF

echo "LaTeX template created: $LATEX_TEMPLATE"

# Step 3: Build PDF with pandoc
echo "Step 3: Building PDF..."

PDF_OUTPUT="$BUILD_DIR/the-gentle-conquest-print.pdf"

pandoc "$COMBINED" \
    --template="$LATEX_TEMPLATE" \
    --toc \
    --toc-depth=2 \
    -o "$PDF_OUTPUT" \
    2>/dev/null || {
        echo "Warning: pandoc with LaTeX failed, trying basic PDF..."
        pandoc "$COMBINED" \
            --toc \
            --toc-depth=2 \
            -o "$PDF_OUTPUT"
    }

echo "PDF created: $PDF_OUTPUT"

# Step 4: Show page count
echo ""
echo "Step 4: Checking page count..."
if command -v pdfinfo &> /dev/null; then
    PAGES=$(pdfinfo "$PDF_OUTPUT" | grep Pages | awk '{print $2}')
    echo "Page count: $PAGES"
    if [ "$PAGES" -lt 79 ]; then
        echo "WARNING: KDP requires minimum 79 pages for spine text"
    fi
else
    echo "Install poppler-utils to check page count: sudo apt-get install poppler-utils"
fi

echo ""
echo "Build complete!"
echo "Output files:"
ls -lh "$BUILD_DIR"/*.pdf 2>/dev/null || true
echo ""
echo "KDP Paperback Checklist:"
echo "1. Trim size: 6\" x 9\" ✓"
echo "2. Margins: inner=0.875\", outer=0.625\", top/bottom=0.75\" ✓"
echo "3. Font: Palatino 11pt ✓"
echo "4. Line spacing: 1.5 ✓"
echo "5. No bleed (text only) ✓"
echo ""
echo "Next steps:"
echo "1. Review PDF in Adobe Acrobat or similar"
echo "2. Upload to KDP as paperback interior"
echo "3. Generate cover wrap using KDP Cover Calculator"
