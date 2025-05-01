import pyfiglet
from colorama import init, Fore, Style

init(autoreset=True)

def vertical_gradient(text, font, colors):
    ascii_art = pyfiglet.figlet_format(text, font=font)
    lines = ascii_art.split('\n')
    total_lines = len(lines)
    colored_lines = []

    for i, line in enumerate(lines):
        if not line.strip():
            colored_lines.append('')
            continue

        # Choose color based on vertical position
        third = total_lines // len(colors)
        index = min(i // third, len(colors) - 1)
        color = Style.BRIGHT + colors[index]

        colored_lines.append(color + line)

    return '\n'.join(colored_lines)

# Color gradients
blue_green_gradient = [Fore.CYAN, Fore.GREEN]                    # Neon Blue to Neon Green
yellow_red_gradient = [Fore.YELLOW, Fore.RED]                   # Neon Yellow to Neon Red
darkblue_pink_gradient = [Fore.BLUE, Fore.LIGHTMAGENTA_EX]      # Dark Blue to Bright Pink

# Generate ASCII art with vertical gradients
welcome_text = vertical_gradient("Welcome to", font="tombstone", colors=blue_green_gradient)
rushland_text = vertical_gradient("Rushland", font="varsity", colors=yellow_red_gradient)
opening_hours_text = vertical_gradient("[ 9:00am to 6:00pm ]", font="tombstone", colors=darkblue_pink_gradient)

