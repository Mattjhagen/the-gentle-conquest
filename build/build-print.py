#!/usr/bin/env python3
import re
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent
MANUSCRIPT_DIR = PROJECT_DIR / "manuscript"
BUILD_DIR = PROJECT_DIR / "build" / "output"
BUILD_DIR.mkdir(parents=True, exist_ok=True)

print("Building KDP Paperback PDF (6x9)...")

# Combine manuscript
combined = []
front = MANUSCRIPT_DIR / "front-matter.md"
if front.exists():
    combined.append(front.read_text())
    combined.append('<div style="page-break-after: always;"></div>')

for ch in sorted((MANUSCRIPT_DIR / "chapters").glob("*.md")):
    combined.append(ch.read_text())
    combined.append('<div style="page-break-after: always;"></div>')

back = MANUSCRIPT_DIR / "back-matter.md"
if back.exists():
    combined.append(back.read_text())

md_text = "\n".join(combined)

# Simple markdown to HTML
html = md_text
html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
html = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', html)
html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
html = re.sub(r'^---+$', r'<hr>', html, flags=re.MULTILINE)

# Wrap paragraphs
lines = html.split('\n')
result = []
for line in lines:
    s = line.strip()
    if s and not s.startswith('<'):
        result.append(f'<p>{s}</p>')
    else:
        result.append(line)
html = '\n'.join(result)

full_html = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>The Gentle Conquest</title>
<style>
@page {{ size: 6in 9in; margin: 0.75in 0.625in; }}
@page :left {{ margin-left: 0.875in; margin-right: 0.625in; }}
@page :right {{ margin-left: 0.625in; margin-right: 0.875in; }}
body {{ font-family: "Palatino Linotype", "Book Antiqua", Palatino, serif; font-size: 11pt; line-height: 1.5; color: #1a1a1a; text-align: justify; }}
h1 {{ font-size: 18pt; text-align: center; margin-top: 2in; page-break-before: always; }}
h2 {{ font-size: 14pt; text-align: center; margin-top: 1.5in; page-break-before: always; }}
h3 {{ font-size: 12pt; margin-top: 1in; }}
p {{ text-indent: 0.5em; margin: 0 0 0.5em 0; orphans: 3; widows: 3; }}
h1 + p, h2 + p {{ text-indent: 0; }}
blockquote {{ margin: 1em 2em; font-style: italic; border-left: 2px solid #ccc; padding-left: 1em; }}
hr {{ border: none; border-top: 1px solid #ccc; margin: 2em 0; text-align: center; }}
hr::after {{ content: "* * *"; color: #666; }}
</style></head><body>{html}</body></html>"""

# Save HTML
html_path = BUILD_DIR / "the-gentle-conquest-print.html"
html_path.write_text(full_html, encoding='utf-8')
print(f"HTML: {html_path}")

# Build PDF
from weasyprint import HTML
pdf_path = BUILD_DIR / "the-gentle-conquest-print.pdf"
HTML(string=full_html).write_pdf(pdf_path)

size_mb = pdf_path.stat().st_size / (1024 * 1024)
est_pages = len(md_text) // 3000
print(f"PDF: {pdf_path} ({size_mb:.1f} MB, ~{est_pages} pages)")
print("Done!")
