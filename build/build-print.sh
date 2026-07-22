#!/bin/bash

# Build print-ready PDF for The Gentle Conquest
# Requires: pandoc, LaTeX (texlive-latex-recommended)

set -e

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MANUSCRIPT_DIR="$PROJECT_DIR/manuscript"
BUILD_DIR="$PROJECT_DIR/build/output"

# Create output directory
mkdir -p "$BUILD_DIR"

echo "Building print-ready PDF for The Gentle Conquest..."

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

# Step 2: Create LaTeX template for print
echo "Step 2: Creating LaTeX template..."

LATEX_TEMPLATE="$BUILD_DIR/print-template.tex"
cat > "$LATEX_TEMPLATE" << 'EOF'
\documentclass[12pt,openany]{book}

% Page geometry for 6x9 trim
\usepackage[paperwidth=6in,paperheight=9in,top=0.75in,bottom=0.75in,inner=0.875in,outer=0.625in]{geometry}

% Fonts
\usepackage{mathpazo}  % Palatino for body text
\usepackage{microtype} % Better typography

% Line spacing
\usepackage{setspace}
\onehalfspacing

% Chapter styling
\usepackage{titlesec}
\titleformat{\chapter}[display]
  {\normalfont\huge\bfseries}
  {\chaptertitlename\ \thechapter}
  {20pt}
  {\Huge}
\titlespacing*{\chapter}{0pt}{50pt}{40pt}

% Headers and footers
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[RE]{\textit{The Gentle Conquest}}
\fancyhead[LO]{\textit{\leftmark}}
\renewcommand{\headrulewidth}{0pt}

% No paragraph indent, spacing between paragraphs
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.5em}

% Links
\usepackage[colorlinks=true,linkcolor=black,urlcolor=black]{hyperref}

% Opening chapter
\renewcommand{\bookname}{}

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

echo ""
echo "Build complete!"
echo "Output files:"
ls -lh "$BUILD_DIR"/*.pdf 2>/dev/null || true
echo ""
echo "Next steps:"
echo "1. Review the PDF layout"
echo "2. Adjust page margins if needed"
echo "3. Generate cover wrap for print"
