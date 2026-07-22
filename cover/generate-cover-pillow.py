#!/usr/bin/env python3
"""
Generate cover image for The Gentle Conquest
Uses Pillow directly (no cairosvg needed)
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Cover dimensions
WIDTH = 1600
HEIGHT = 2560

# Colors (RGB tuples)
BG_TOP = (250, 250, 250)
BG_BOTTOM = (232, 232, 232)
TITLE_COLOR = (26, 26, 26)
SUBTITLE_COLOR = (102, 102, 102)
PLANT_GREEN = (76, 175, 80)
PLANT_DARK = (46, 125, 50)
LEAF_LIGHT = (102, 187, 106)
LEAF_MID = (67, 160, 71)
CRACK_LIGHT = (208, 208, 208)
CRACK_DARK = (144, 144, 144)
HAND_LIGHT = (232, 196, 168)
HAND_MID = (212, 165, 116)
LINE_COLOR = (153, 153, 153)

def create_gradient(width, height, color1, color2):
    """Create a vertical gradient image"""
    img = Image.new('RGB', (width, height))
    for y in range(height):
        ratio = y / height
        r = int(color1[0] + (color2[0] - color1[0]) * ratio)
        g = int(color1[1] + (color2[1] - color1[1]) * ratio)
        b = int(color1[2] + (color2[2] - color1[2]) * ratio)
        for x in range(width):
            img.putpixel((x, y), (r, g, b))
    return img

def draw_leaf(draw, cx, cy, angle, size=40):
    """Draw a leaf at position with rotation"""
    import math
    points = []
    for i in range(20):
        t = i / 19 * math.pi
        x = size * math.cos(t)
        y = size/2 * math.sin(t)
        # Rotate
        rad = math.radians(angle)
        rx = x * math.cos(rad) - y * math.sin(rad)
        ry = x * math.sin(rad) + y * math.cos(rad)
        points.append((cx + rx, cy + ry))
    draw.polygon(points, fill=LEAF_MID)

def draw_finger(draw, x, y, width, height, angle=0):
    """Draw a finger"""
    import math
    points = []
    # Create rounded rectangle shape
    for i in range(20):
        t = i / 19 * math.pi * 2
        rx = width/2 * math.cos(t)
        ry = height/2 * math.sin(t)
        rad = math.radians(angle)
        rrx = rx * math.cos(rad) - ry * math.sin(rad)
        rry = rx * math.sin(rad) + ry * math.cos(rad)
        points.append((x + rrx, y + rry))
    draw.polygon(points, fill=HAND_MID)

def main():
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    os.makedirs(output_dir, exist_ok=True)
    
    print("Creating cover image...")
    
    # Create gradient background
    print("  Creating background gradient...")
    img = create_gradient(WIDTH, HEIGHT, BG_TOP, BG_BOTTOM)
    draw = ImageDraw.Draw(img)
    
    # Draw subtle radial glow
    print("  Adding subtle effects...")
    for r in range(300, 0, -1):
        alpha = int(3 * (1 - r/300))
        color = (76, 175, 80, alpha)
        # Left glow
        x, y = int(WIDTH * 0.2), int(HEIGHT * 0.3)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=None, outline=(76+r//10, 175+r//5, 80+r//10))
        # Right glow
        x, y = int(WIDTH * 0.8), int(HEIGHT * 0.7)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=None, outline=(76+r//10, 175+r//5, 80+r//10))
    
    # Draw the crack
    print("  Drawing crack...")
    crack_x = WIDTH // 2
    crack_top = HEIGHT // 2 - 200
    crack_bottom = HEIGHT // 2 + 200
    for y in range(crack_top, crack_bottom):
        # Vary width based on position
        progress = (y - crack_top) / (crack_bottom - crack_top)
        width = int(4 + 4 * math.sin(progress * math.pi))
        for dx in range(-width, width+1):
            fade = 1.0 - abs(dx) / width
            color = tuple(int(CRACK_LIGHT[i] + (CRACK_DARK[i] - CRACK_LIGHT[i]) * (1-fade)) for i in range(3))
            if 0 <= crack_x + dx < WIDTH:
                img.putpixel((crack_x + dx, y), color)
    
    # Draw the plant
    print("  Drawing plant...")
    plant_x = WIDTH // 2
    plant_bottom = HEIGHT // 2 + 100
    
    # Stem
    stem_width = 6
    for y in range(plant_bottom - 180, plant_bottom):
        progress = (plant_bottom - 180 - y) / 180
        green = tuple(int(PLANT_GREEN[i] + (PLANT_DARK[i] - PLANT_GREEN[i]) * progress) for i in range(3))
        for dx in range(-stem_width//2, stem_width//2 + 1):
            if 0 <= plant_x + dx < WIDTH:
                img.putpixel((plant_x + dx, y), green)
    
    # Bud
    bud_y = plant_bottom - 200
    for dy in range(-16, 17):
        for dx in range(-12, 13):
            if dx*dx + dy*dy < 144:
                if 0 <= plant_x + dx < WIDTH and 0 <= bud_y + dy < HEIGHT:
                    img.putpixel((plant_x + dx, bud_y + dy), PLANT_GREEN)
    
    # Leaves
    leaf_positions = [
        (-50, -60, -30), (50, -60, 30),
        (-45, -20, -20), (45, -20, 20),
        (-55, 20, -40), (55, 20, 40),
    ]
    for lx, ly, angle in leaf_positions:
        draw_leaf(draw, plant_x + lx, HEIGHT//2 + ly, angle)
    
    # Draw the hand
    print("  Drawing hand...")
    hand_x = WIDTH // 2
    hand_y = HEIGHT // 2 + 280
    
    # Palm
    draw.ellipse([hand_x-100, hand_y-60, hand_x+100, hand_y+60], fill=HAND_MID)
    
    # Fingers
    fingers = [
        (-69, -140, 22, 80, 25),
        (-40, -160, 20, 100, 8),
        (0, -165, 20, 105, 2),
        (40, -160, 19, 95, -4),
        (69, -145, 18, 75, -12),
    ]
    for fx, fy, fw, fh, angle in fingers:
        draw_finger(draw, hand_x + fx, hand_y + fy, fw, fh, angle)
    
    # Draw decorative line
    print("  Adding decorative elements...")
    line_y = HEIGHT - 300
    draw.line([(WIDTH//2-100, line_y), (WIDTH//2+100, line_y)], fill=LINE_COLOR, width=1)
    
    # Draw title text
    print("  Adding text...")
    try:
        # Try to use a nice font
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Light.ttf", 142)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Light.ttf", 42)
        author_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Light.ttf", 52)
    except:
        # Fall back to default font
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        author_font = ImageFont.load_default()
    
    # Title
    title1 = "THE GENTLE"
    title2 = "CONQUEST"
    bbox1 = draw.textbbox((0, 0), title1, font=title_font)
    bbox2 = draw.textbbox((0, 0), title2, font=title_font)
    w1 = bbox1[2] - bbox1[0]
    w2 = bbox2[2] - bbox2[0]
    draw.text(((WIDTH - w1) // 2, 250), title1, fill=TITLE_COLOR, font=title_font)
    draw.text(((WIDTH - w2) // 2, 420), title2, fill=TITLE_COLOR, font=title_font)
    
    # Subtitle
    subtitle = "A NOVEL"
    bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    w = bbox[2] - bbox[0]
    draw.text(((WIDTH - w) // 2, 580), subtitle, fill=SUBTITLE_COLOR, font=subtitle_font)
    
    # Author
    author = "MATT JHAGEN"
    bbox = draw.textbbox((0, 0), author, font=author_font)
    w = bbox[2] - bbox[0]
    draw.text(((WIDTH - w) // 2, HEIGHT - 250), author, fill=TITLE_COLOR, font=author_font)
    
    # Save as PNG
    png_path = os.path.join(output_dir, 'cover-ebook.png')
    img.save(png_path, 'PNG')
    print(f"PNG saved: {png_path}")
    
    # Save as JPEG
    jpg_path = os.path.join(output_dir, 'cover-ebook.jpg')
    img_rgb = img.convert('RGB')
    img_rgb.save(jpg_path, 'JPEG', quality=95)
    print(f"JPEG saved: {jpg_path}")
    
    print("\nCover generation complete!")
    print(f"Files saved to: {output_dir}")

if __name__ == '__main__':
    import math
    main()
