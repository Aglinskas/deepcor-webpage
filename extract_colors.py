from PIL import Image
from collections import Counter
import os

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

def is_colorful(rgb):
    # Check if the color has some saturation (difference between max and min channel)
    # and is not too dark or too light
    r, g, b = rgb
    if max(r, g, b) - min(r, g, b) < 20: # It's gray-ish
        return False
    if max(r, g, b) < 30: # Too black
        return False
    if min(r, g, b) > 240: # Too white
        return False
    return True

def get_dominant_colors(image_path):
    try:
        print(f"Processing {image_path}...")
        img = Image.open(image_path)
        # Use a slightly larger size to capture details
        img = img.resize((300, 300))
        img = img.convert('RGBA')
        
        # Get pixels (ignore alpha 0)
        pixels = []
        data = list(img.getdata())
        for r, g, b, a in data:
            if a > 50: # If not transparent
                pixels.append((r, g, b))
                
        counts = Counter(pixels)
        
        # Filter for colorful pixels
        colorful_counts = Counter()
        for color, count in counts.items():
            if is_colorful(color):
                colorful_counts[color] = count
                
        common = colorful_counts.most_common(20)
        
        print("\nTop Colorful Colors:")
        for color, count in common:
            hex_val = rgb_to_hex(color)
            print(f"Color: {hex_val}, RGB: {color}, Count: {count}")
            
    except Exception as e:
        print(f"Error: {e}")

image_path = "Assets/logos/DeepCor-logo-v2-px.png"
if os.path.exists(image_path):
    get_dominant_colors(image_path)
else:
    get_dominant_colors("assets/logos/DeepCor-logo-v2-px.png")
