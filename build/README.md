# Build Directory

This directory contains build scripts and configuration for generating ebook and print files.

## Files (to be created in Phase 6)

- `build-ebook.sh` — Script to generate .epub and .mobi files
- `build-print.sh` — Script to generate print-ready PDFs
- `BUILDING.md` — Documentation for the build process

## Requirements

- Calibre (for ebook conversion)
- Pandoc (for markdown to HTML/EPUB conversion)
- LaTeX (for print PDF generation, optional)
- ImageMagick (for cover processing, optional)

## Usage

```bash
# Build ebook
./build-ebook.sh

# Build print
./build-print.sh

# Build all
./build-all.sh
```

## Notes

- Build scripts will be created in Phase 6
- All builds should be tested before publication
- Keep build logs for debugging
