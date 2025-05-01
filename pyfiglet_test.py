# comment
# import pyfiglet
import pyfiglet
from colorama import init, Fore, Style

init(autoreset=True)

def neon_vertical_gradient(text, font='varsity'):
    ascii_art = pyfiglet.figlet_format(text, font=font)
    lines = ascii_art.split('\n')
    total_lines = len(lines)
    colored_lines = []

    for i, line in enumerate(lines):
        if not line.strip():
            colored_lines.append('')
            continue

        # Top third = Neon Yellow, Middle = Neon Orange, Bottom = Neon Red
        if i < total_lines / 3:
            color = Style.BRIGHT + Fore.YELLOW
        elif i < 2 * total_lines / 3:
            color = Style.BRIGHT + Fore.LIGHTRED_EX  # Simulated neon orange
        else:
            color = Style.BRIGHT + Fore.RED

        colored_lines.append(color + line)

    return '\n'.join(colored_lines)
