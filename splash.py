import pyfiglet
from colorama import Fore, init, Style
import time
import shutil

# Initialize colorama
init(autoreset=True)

# Function to render ASCII text
def render_ascii_text(text, font='roman'):
    figlet = pyfiglet.Figlet(font=font)
    return figlet.renderText(text).splitlines()

# Typewriter effect for a single line of text centered in the box
def typewriter_effect_in_box(text, box_width, delay=0.14):
    centered_line = text.center(box_width - 4)
    print(Fore.BLUE + "* " + Style.RESET_ALL, end='')  # Left border (Blue)
    for char in centered_line:
        print(Fore.YELLOW + char, end='', flush=True)    # Yellow text for subtitle
        time.sleep(delay)
    print(Fore.BLUE + " *" + Style.RESET_ALL)           # Right border (Blue)

# Function to show splash screen with animated box and content
def show_splash_screen():
    # Terminal width and content prep
    terminal_width = shutil.get_terminal_size().columns
    box_width = min(terminal_width - 4, 100)  # safe max width
    ascii_lines = render_ascii_text("SAP", font='roman')
    subtitle = "Simple Agile Project"

    # Calculate box height: SAP lines + subtitle + top/bottom borders + padding
    content_height = len(ascii_lines) + 2  # 1 blank + 1 for subtitle
    box_height = content_height + 4  # Padding above/below

    # Determine gradient sections (divide lines into three parts for blue, green, yellow)
    total_lines = len(ascii_lines)
    third = total_lines // 3
    blue_end = third
    green_end = 2 * third

    # Build and animate box with content
    print(Fore.BLUE + "*" * box_width)  # Top border (Blue)
    time.sleep(0.1)  # Slower border

    for i in range(1, box_height - 1):
        if i == 1 or i == box_height - 2:
            # Empty padding lines (top and bottom of the box)
            print(Fore.BLUE + "*" + " " * (box_width - 2) + "*")  # Blue border
            time.sleep(0.1)  # Slower border
        elif 2 <= i < 2 + len(ascii_lines):
            # SAP ASCII lines with gradient (blue -> green -> yellow)
            line_idx = i - 2
            line = ascii_lines[line_idx].center(box_width - 4)
            if line_idx < blue_end:
                color = Fore.BLUE
            elif line_idx < green_end:
                color = Fore.GREEN
            else:
                color = Fore.YELLOW
            print(Fore.BLUE + "* " + color + line + Fore.BLUE + " *")  # Left and right borders with gradient color
            time.sleep(0.01)  # Faster SAP
        elif i == 2 + len(ascii_lines):
            # Empty line before subtitle
            print(Fore.BLUE + "*" + " " * (box_width - 2) + "*")  # Blue border
            time.sleep(0.1)  # Slower border
        elif i == 3 + len(ascii_lines):
            # Subtitle with typewriter effect (Yellow)
            typewriter_effect_in_box(subtitle, box_width, delay=0.04)  # Slower subtitle

    print(Fore.BLUE + "*" * box_width)  # Bottom border (Blue)
    time.sleep(0.1)  # Slower border

# Run it
show_splash_screen()











