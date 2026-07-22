# Building The Gentle Conquest

## Prerequisites

### Required Tools

#### For EPUB/MOBI (eBook)
```bash
# Ubuntu/Debian
sudo apt-get install pandoc calibre

# macOS (with Homebrew)
brew install pandoc calibre

# Windows
# Download from:
# - Pandoc: https://pandoc.org/installing.html
# - Calibre: https://calibre-ebook.com/download
```

#### For PDF (Print)
```bash
# Ubuntu/Debian
sudo apt-get install pandoc texlive-latex-recommended texlive-fonts-recommended

# macOS (with Homebrew)
brew install pandoc --cask mactex-no-gui

# Windows
# Download Pandoc + MiKTeX or TeX Live
```

## Quick Start

### Build eBook (EPUB + MOBI)
```bash
cd the-gentle-conquest
./build/build-ebook.sh
```

### Build Print (PDF)
```bash
cd the-gentle-conquest
./build/build-print.sh
```

### Build Everything
```bash
cd the-gentle-conquest
./build/build-all.sh
```

## Output Files

After building, find output files in:
```
build/output/
├── the-gentle-conquest.epub      # eBook
├── the-gentle-conquest.mobi      # Kindle format
└── the-gentle-conquest-print.pdf # Print-ready PDF
```

## Cover Artwork

Before building, add your cover image:
1. Place cover at: `cover/cover-ebook.jpg`
2. Ensure dimensions: 1600x2560 pixels (minimum)
3. Format: JPEG (quality 95%+) or PNG

## Testing

### Test EPUB
```bash
# Using Calibre's ebook-viewer
ebook-viewer build/output/the-gentle-conquest.epub

# Or transfer to e-reader device
```

### Test PDF
```bash
# Open in PDF viewer
open build/output/the-gentle-conquest-print.pdf

# Or preview on Kindle
```

### Test on Kindle
1. Download Kindle Previewer: https://www.amazon.com/Kindle-Previewer/b?ie=UTF8&nodeId=G5QU7MHRVHY6KQ25
2. Open the .epub or .mobi file
3. Test on different device emulators

## Troubleshooting

### "pandoc: command not found"
Install pandoc using instructions above.

### "calibre: command not found"
Install calibre using instructions above.

### EPUB validation errors
```bash
# Install epubcheck
# https://github.com/w3c/epubcheck

epubcheck build/output/the-gentle-conquest.epub
```

### PDF compilation errors
Ensure LaTeX is installed:
```bash
# Ubuntu/Debian
sudo apt-get install texlive-latex-recommended texlive-fonts-recommended

# Check installation
pdflatex --version
```

## Customization

### Change fonts
Edit `build/style.css` for EPUB fonts.

### Change page size
Edit `build/build-print.sh` and modify the LaTeX template.

### Add images
Place images in `manuscript/images/` and reference in markdown.

## Publishing

### Amazon KDP
1. Upload EPUB to KDP
2. KDP will convert to Kindle format automatically
3. Upload print PDF separately

### IngramSpark
1. Upload EPUB for eBook distribution
2. Upload print PDF for print distribution

### Direct Sales
1. Use EPUB for Gumroad, Payhip, etc.
2. Use PDF for direct downloads

## Support

For issues with the build system, check:
1. Tool versions are up to date
2. All prerequisites are installed
3. File paths are correct
4. Markdown syntax is valid
