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
├── build/                       # Build scripts and configuration (Phase 6)
├── cover/                       # Cover images and assets (Phase 5)
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

### Phase 3: Manuscript Edit (Pending)
- [ ] Final proofread
- [ ] Address critical issues from audit
- [ ] Style and consistency pass

### Phase 4: Production (Pending)
- [ ] Cover design
- [ ] Interior formatting
- [ ] eBook conversion
- [ ] Print formatting

### Phase 5: Distribution (Pending)
- [ ] ISBN assignment
- [ ] KDP upload
- [ ] IngramSpark upload (optional)
- [ ] Direct sales setup (optional)

### Phase 6: Launch (Pending)
- [ ] Pre-launch marketing
- [ ] Launch day activities
- [ ] Post-launch follow-up

## Getting Started

### Prerequisites

- Git
- Calibre (for ebook conversion)
- Pandoc (for markdown to HTML/EPUB conversion)
- LaTeX (for print PDF generation, optional)

### Installation

```bash
# Clone the repository
git clone https://github.com/Mattjhagen/the-gentle-conquest.git

# Navigate to the project directory
cd the-gentle-conquest

# Install dependencies (if needed)
# Note: Calibre, Pandoc, and LaTeX are system-level dependencies
# Install them using your package manager
```

### Usage

```bash
# Build ebook
./build/build-ebook.sh

# Build print
./build/build-print.sh

# Build all
./build/build-all.sh
```

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
