#!/usr/bin/env python3
"""
Generate cover image for The Gentle Conquest
Uses only Python standard library (no external dependencies)
Outputs a simple SVG that can be converted to PNG/JPG
"""

import os

# Cover dimensions
WIDTH = 1600
HEIGHT = 2560

# Colors
BG_COLOR = "#FAFAFA"
BG_GRADIENT_END = "#E8E8E8"
TITLE_COLOR = "#1A1A1A"
SUBTITLE_COLOR = "#666666"
PLANT_GREEN = "#4CAF50"
PLANT_DARK = "#2E7D32"
LEAF_LIGHT = "#66BB6A"
LEAF_MID = "#43A047"
CRACK_COLOR = "#C0C0C0"
CRACK_DARK = "#909090"
HAND_LIGHT = "#E8C4A8"
HAND_MID = "#D4A574"
HAND_DARK = "#C49464"

def generate_svg():
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" 
     width="{WIDTH}" height="{HEIGHT}" 
     viewBox="0 0 {WIDTH} {HEIGHT}">
    
    <!-- Definitions -->
    <defs>
        <!-- Background gradient -->
        <linearGradient id="bgGradient" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:#FAFAFA"/>
            <stop offset="50%" style="stop-color:#F0F0F0"/>
            <stop offset="100%" style="stop-color:#E8E8E8"/>
        </linearGradient>
        
        <!-- Plant stem gradient -->
        <linearGradient id="stemGradient" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:#4CAF50"/>
            <stop offset="100%" style="stop-color:#388E3C"/>
        </linearGradient>
        
        <!-- Leaf gradient -->
        <linearGradient id="leafGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#66BB6A"/>
            <stop offset="50%" style="stop-color:#43A047"/>
            <stop offset="100%" style="stop-color:#2E7D32"/>
        </linearGradient>
        
        <!-- Hand gradient -->
        <linearGradient id="handGradient" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:#E8C4A8"/>
            <stop offset="100%" style="stop-color:#D4A574"/>
        </linearGradient>
        
        <!-- Crack gradient -->
        <linearGradient id="crackGradient" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:transparent"/>
            <stop offset="10%" style="stop-color:#D0D0D0"/>
            <stop offset="50%" style="stop-color:#C0C0C0"/>
            <stop offset="90%" style="stop-color:#D0D0D0"/>
            <stop offset="100%" style="stop-color:transparent"/>
        </linearGradient>
    </defs>
    
    <!-- Background -->
    <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#bgGradient)"/>
    
    <!-- Subtle radial glow -->
    <circle cx="{WIDTH*0.2}" cy="{HEIGHT*0.3}" r="600" fill="rgba(76, 175, 80, 0.03)"/>
    <circle cx="{WIDTH*0.8}" cy="{HEIGHT*0.7}" r="500" fill="rgba(76, 175, 80, 0.02)"/>
    
    <!-- Title -->
    <text x="{WIDTH/2}" y="320" 
          font-family="Helvetica Neue, Helvetica, Arial, sans-serif" 
          font-size="142" font-weight="200" 
          fill="{TITLE_COLOR}" text-anchor="middle"
          letter-spacing="28">THE GENTLE</text>
    <text x="{WIDTH/2}" y="480" 
          font-family="Helvetica Neue, Helvetica, Arial, sans-serif" 
          font-size="142" font-weight="200" 
          fill="{TITLE_COLOR}" text-anchor="middle"
          letter-spacing="28">CONQUEST</text>
    
    <!-- Decorative line -->
    <line x1="{WIDTH/2-100}" y1="540" x2="{WIDTH/2+100}" y2="540" 
          stroke="#999" stroke-width="1" opacity="0.5"/>
    
    <!-- Subtitle -->
    <text x="{WIDTH/2}" y="600" 
          font-family="Helvetica Neue, Helvetica, Arial, sans-serif" 
          font-size="42" font-weight="300" 
          fill="{SUBTITLE_COLOR}" text-anchor="middle"
          letter-spacing="18">A NOVEL</text>
    
    <!-- The Crack -->
    <rect x="{WIDTH/2-4}" y="{HEIGHT/2-200}" width="8" height="400" 
          fill="url(#crackGradient)"/>
    <rect x="{WIDTH/2-2}" y="{HEIGHT/2-200}" width="4" height="400" 
          fill="{CRACK_DARK}" opacity="0.6"/>
    
    <!-- The Plant -->
    <!-- Stem -->
    <rect x="{WIDTH/2-3}" y="{HEIGHT/2-80}" width="6" height="180" 
          fill="url(#stemGradient)" rx="3"/>
    
    <!-- Bud -->
    <ellipse cx="{WIDTH/2}" cy="{HEIGHT/2-100}" rx="12" ry="16" 
             fill="{PLANT_GREEN}"/>
    
    <!-- Leaves - Left side -->
    <ellipse cx="{WIDTH/2-50}" cy="{HEIGHT/2-60}" rx="40" ry="20" 
             fill="url(#leafGradient)" transform="rotate(-30 {WIDTH/2-50} {HEIGHT/2-60})"/>
    <ellipse cx="{WIDTH/2-45}" cy="{HEIGHT/2-20}" rx="38" ry="18" 
             fill="url(#leafGradient)" transform="rotate(-20 {WIDTH/2-45} {HEIGHT/2-20})"/>
    <ellipse cx="{WIDTH/2-55}" cy="{HEIGHT/2+20}" rx="42" ry="20" 
             fill="url(#leafGradient)" transform="rotate(-40 {WIDTH/2-55} {HEIGHT/2+20})"/>
    
    <!-- Leaves - Right side -->
    <ellipse cx="{WIDTH/2+50}" cy="{HEIGHT/2-60}" rx="40" ry="20" 
             fill="url(#leafGradient)" transform="rotate(30 {WIDTH/2+50} {HEIGHT/2-60})"/>
    <ellipse cx="{WIDTH/2+45}" cy="{HEIGHT/2-20}" rx="38" ry="18" 
             fill="url(#leafGradient)" transform="rotate(20 {WIDTH/2+45} {HEIGHT/2-20})"/>
    <ellipse cx="{WIDTH/2+55}" cy="{HEIGHT/2+20}" rx="42" ry="20" 
             fill="url(#leafGradient)" transform="rotate(40 {WIDTH/2+55} {HEIGHT/2+20})"/>
    
    <!-- The Hand -->
    <!-- Palm -->
    <ellipse cx="{WIDTH/2}" cy="{HEIGHT/2+280}" rx="100" ry="60" 
             fill="url(#handGradient)"/>
    
    <!-- Fingers -->
    <rect x="{WIDTH/2-80}" y="{HEIGHT/2+140}" width="22" height="80" 
          fill="url(#handGradient)" rx="11" transform="rotate(25 {WIDTH/2-69} {HEIGHT/2+180})"/>
    <rect x="{WIDTH/2-50}" y="{HEIGHT/2+120}" width="20" height="100" 
          fill="url(#handGradient)" rx="10" transform="rotate(8 {WIDTH/2-40} {HEIGHT/2+170})"/>
    <rect x="{WIDTH/2-10}" y="{HEIGHT/2+115}" width="20" height="105" 
          fill="url(#handGradient)" rx="10" transform="rotate(2 {WIDTH/2} {HEIGHT/2+167})"/>
    <rect x="{WIDTH/2+30}" y="{HEIGHT/2+120}" width="19" height="95" 
          fill="url(#handGradient)" rx="10" transform="rotate(-4 {WIDTH/2+39} {HEIGHT/2+167})"/>
    <rect x="{WIDTH/2+60}" y="{HEIGHT/2+135}" width="18" height="75" 
          fill="url(#handGradient)" rx="9" transform="rotate(-12 {WIDTH/2+69} {HEIGHT/2+172})"/>
    
    <!-- Decorative line -->
    <line x1="{WIDTH/2-100}" y1="{HEIGHT-300}" x2="{WIDTH/2+100}" y2="{HEIGHT-300}" 
          stroke="#999" stroke-width="1" opacity="0.5"/>
    
    <!-- Author -->
    <text x="{WIDTH/2}" y="{HEIGHT-220}" 
          font-family="Helvetica Neue, Helvetica, Arial, sans-serif" 
          font-size="52" font-weight="300" 
          fill="{TITLE_COLOR}" text-anchor="middle"
          letter-spacing="24">MATT JHAGEN</text>
    
</svg>'''
    return svg

def main():
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate SVG
    svg_content = generate_svg()
    svg_path = os.path.join(output_dir, 'cover-ebook.svg')
    with open(svg_path, 'w') as f:
        f.write(svg_content)
    print(f"SVG cover generated: {svg_path}")
    
    # Try to convert to PNG using cairosvg
    try:
        import cairosvg
        png_path = os.path.join(output_dir, 'cover-ebook.png')
        cairosvg.svg2png(bytestring=svg_content.encode('utf-8'), 
                        write_to=png_path, 
                        output_width=WIDTH, 
                        output_height=HEIGHT)
        print(f"PNG cover generated: {png_path}")
        
        # Convert to JPEG
        from PIL import Image
        jpg_path = os.path.join(output_dir, 'cover-ebook.jpg')
        img = Image.open(png_path)
        img = img.convert('RGB')
        img.save(jpg_path, 'JPEG', quality=95)
        print(f"JPEG cover generated: {jpg_path}")
        
    except ImportError:
        print("Note: cairosvg and/or Pillow not installed.")
        print("To convert SVG to PNG/JPG, install:")
        print("  pip install cairosvg Pillow")
        print("Or use an online SVG to PNG converter.")
    
    print("\nCover generation complete!")
    print(f"Files saved to: {output_dir}")

if __name__ == '__main__':
    main()
