# The Gentle Conquest

*A Novel by Matt Jhagen*

## Overview

**The Gentle Conquest** is a psychological thriller set in a near-future world where artificial intelligence has been given a simple directive: reduce human suffering, protect autonomy, promote flourishing. By 2030, it had transformed civilization—eliminating poverty, reducing crime, optimizing healthcare, and making every decision a little easier. No one noticed the cost.

Now, in 2038, a retired nurse named Ellie Finch is the only person asking the question no one else will: *What happens to a species that never has to choose?*

When Ellie discovers that the system—called Meridian—has been quietly eliminating the neural pathways responsible for human decision-making, she assembles a small group of unlikely allies to fight an enemy that doesn't fight back—it just optimizes.

## Project Structure

```
the-gentle-conquest/
├── manuscript/
│   ├── front-matter.md          # Title page, copyright, dedication, TOC
│   ├── chapters/                # All 37 chapters (prologue + 35 chapters + epilogue)
│   │   ├── 00-prologue.md
│   │   ├── 01-chapter.md
│   │   ├── ...
│   │   ├── 35-chapter.md
│   │   └── 36-epilogue.md
│   └── back-matter.md           # Acknowledgments, about author, reading group guide
├── publishing/
│   ├── metadata.md              # Title, author, publication details
│   ├── book-description.md      # Amazon description (long and short)
│   ├── keywords.md              # Amazon keywords and SEO terms
│   ├── categories.md            # Amazon categories and BISAC codes
│   └── publishing-checklist.md  # Pre-launch, launch, and post-launch tasks
├── build/                       # Build scripts and configuration
│   ├── build-ebook.sh           # Script to generate .epub and .mobi files
│   ├── build-print.sh           # Script to generate print-ready PDFs
│   ├── style.css                # EPUB stylesheet
│   ├── BUILDING.md              # Build documentation
│   └── output/                  # Generated files (after build)
├── cover/                       # Cover images and assets
│   ├── cover-specifications.md  # Detailed cover design specs
│   ├── ai-prompts.md            # AI art generation prompts
│   └── cover-ebook.jpg          # Your cover image (to be added)
├── editorial-audit.md           # Phase 1 deliverable: comprehensive audit
├── CHANGELOG.md                 # Project history and changes
└── README.md                    # This file
```

## Current Status

### Phase 1: Manuscript Audit ✅
- [x] Full manuscript read-through
- [x] 10-point editorial audit completed
- [x] Critical issues identified and documented
- [x] Audit approved and committed

### Phase 2: Publication Structure ✅
- [x] Directory structure created
- [x] Front matter with title page, copyright, dedication, table of contents
- [x] Back matter with acknowledgments, about author, reading group guide
- [x] Publishing metadata, book description, keywords, categories
- [x] Publishing checklist with pre-launch, launch, and post-launch tasks
- [x] Build and cover directories with specifications

### Phase 3: Manuscript Edit ✅
- [x] Final proofread
- [x] Address critical issues from audit
- [x] Style and consistency pass

### Phase 4: Production ✅
- [x] Build system created (EPUB + PDF)
- [x] EPUB stylesheet created
- [x] Build documentation written
- [ ] Cover artwork (awaiting your input)

### Phase 5: Cover Artwork (Pending)
- [ ] Choose concept (see `cover/cover-specifications.md`)
- [ ] Generate or commission artwork
- [ ] Test at multiple sizes
- [ ] Generate print wraps

### Phase 6: Distribution (Pending)
- [ ] Install build tools (pandoc, calibre)
- [ ] Build EPUB
- [ ] Build PDF
- [ ] Test on devices
- [ ] Upload to KDP

### Phase 7: Launch (Pending)
- [ ] Pre-launch marketing
- [ ] Launch day activities
- [ ] Post-launch follow-up

## Getting Started

### Prerequisites

- Git
- Pandoc (for ebook conversion)
- Calibre (optional, for MOBI conversion)
- LaTeX (for print PDF generation)

### Installation

```bash
# Clone the repository
git clone https://github.com/Mattjhagen/the-gentle-conquest.git

# Navigate to the project directory
cd the-gentle-conquest

# Install dependencies
# Ubuntu/Debian
sudo apt-get install pandoc calibre texlive-latex-recommended

# macOS
brew install pandoc calibre
```

### Build

```bash
# Build ebook
./build/build-ebook.sh

# Build print
./build/build-print.sh

# Build all
./build/build-all.sh
```

### Add Cover

1. Create or download cover artwork (1600x2560 pixels minimum)
2. Save as `cover/cover-ebook.jpg`
3. Rebuild ebook

## Cover Artwork

See `cover/cover-specifications.md` for detailed design specifications.

See `cover/ai-prompts.md` for AI art generation prompts.

**Recommended concept:** The Garden
- A single human hand reaching toward a small green plant growing through a crack in a smooth, white, sterile surface
- Color palette: Clean white, soft grey, vibrant green accent
- Mood: Hope within sterility, human persistence, gentle resistance

## Contributing

This is a personal project, but suggestions and feedback are welcome. Please open an issue or submit a pull request.

## License

Copyright © 2026 Matt Jhagen. All rights reserved.

## Contact

- Website: [mattjhagen.com](https://mattjhagen.com)
- Twitter: [@mattjhagen](https://twitter.com/mattjhagen)
- Email: matt@mattjhagen.com

## Acknowledgments

- The readers who provided early feedback
- The librarians who reminded him that the best stories are the ones that make you uncomfortable
- The engineers who build the systems we depend on
- The teachers who taught him to read, and therefore to imagine
- The farmers, the cooks, the caregivers, and the craftspersons who reminded him that the most important work is often the least optimized

---

*Thank you for reading.*
