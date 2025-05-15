from ascii_magic import AsciiArt
from PIL import Image
import os

# Path to your PNG file
image_path = "agile_logo.png"  # Ensure this is in the same directory or update with full path
output_path = "resized_agile_logo.png"  # Temporary file for resized image

# Resize image to 75x100 pixels to reduce height by ~4x
def resize_image(input_path, output_path, size=(75, 100)):
    try:
        with Image.open(input_path) as img:
            img = img.resize(size, Image.LANCZOS)  # High-quality resizing
            img.save(output_path)
    except FileNotFoundError:
        print(f"Error: Image file '{input_path}' not found. Please check the path.")
        return False
    except Exception as e:
        print(f"Error resizing image: {e}")
        return False
    return True

# Resize the image
if not resize_image(image_path, output_path):
    exit(1)

# Create ASCII art from the resized image
try:
    ascii_art = AsciiArt.from_image(output_path)
except Exception as e:
    print(f"Error creating ASCII art: {e}")
    exit(1)

# Output the ASCII art to the terminal, centered and compact
ascii_art.to_terminal(columns=40)  # Small column count for compact width

# Clean up the temporary resized image
os.remove(output_path)










