# Converting Cover to Image

## Option 1: Use the SVG Directly

The SVG file at `cover/output/cover-ebook.svg` can be:
1. Opened in any web browser
2. Screenshot at full resolution
3. Saved as PNG/JPG

### Steps:
1. Open `cover/output/cover-ebook.svg` in Chrome/Firefox
2. Press F12 to open DevTools
3. Set device pixel ratio to 2 for high resolution
4. Screenshot the full page
5. Crop to cover dimensions (1600x2560)

## Option 2: Online Converters

Use free online tools:
- https://svgtopng.com
- https://convertio.co/svg-png/
- https://www.cloudconvert.com/svg-to-png

Upload `cover/output/cover-ebook.svg` and download as PNG.

## Option 3: Command Line (if tools installed)

### Using Inkscape
```bash
inkscape -w 1600 -h 2560 cover/output/cover-ebook.svg -o cover/output/cover-ebook.png
```

### Using ImageMagick
```bash
convert -background none -density 300 cover/output/cover-ebook.svg cover/output/cover-ebook.png
```

### Using rsvg-convert
```bash
rsvg-convert -w 1600 -h 2560 cover/output/cover-ebook.svg -o cover/output/cover-ebook.png
```

## Option 4: Browser Screenshot (Recommended)

### Using Chrome DevTools:
1. Open `cover/output/cover-ebook.svg` in Chrome
2. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
3. Type "screenshot" and select "Capture full size screenshot"
4. The PNG will be saved to your Downloads folder
5. Rename to `cover-ebook.jpg` and place in `cover/` directory

### Using Firefox:
1. Open `cover/output/cover-ebook.svg` in Firefox
2. Press `Ctrl+Shift+S` (Windows/Linux) or `Cmd+Shift+S` (Mac)
3. Select "Save full page"
4. Choose PNG format
5. Save and rename to `cover-ebook.jpg`

## Option 5: Python with Dependencies

If you can install packages:
```bash
pip install cairosvg Pillow
python3 cover/generate-cover.py
```

This will generate both PNG and JPG files.

## After Conversion

Once you have the image file:
1. Place it at `cover/cover-ebook.jpg` (or .png)
2. The build script will automatically include it in the EPUB
3. For print, you'll need to create a full wrap (front + spine + back)

## Recommended Dimensions

- **eBook:** 1600 x 2560 pixels (minimum)
- **Print front:** 1800 x 2700 pixels (for 6x9" at 300 DPI)
- **Print full wrap:** 3600 x 2700 pixels (with bleed)

## Color Profile

- **eBook:** sRGB (default)
- **Print:** CMYK (convert before printing)

## Testing

After generating the cover:
1. View at 100% zoom
2. View at thumbnail size (ensure title is readable)
3. Test on different devices/screens
4. Check color accuracy
