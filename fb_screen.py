import pyfiglet
from colorama import Fore, init, Style
import shutil

# Initialize colorama
init(autoreset=True)

# Function to print centered ASCII text in a color (no animation)
def print_ascii_centered(text, color, font='standard'):
    figlet = pyfiglet.Figlet(font=font)
    ascii_art = figlet.renderText(text)
    terminal_width = shutil.get_terminal_size().columns

    for line in ascii_art.splitlines():
        centered_line = line.center(terminal_width)
        print(color + centered_line + Style.RESET_ALL)

# Final farewell screen function
def show_farewell_screen():
    print_ascii_centered("THANK YOU", Fore.MAGENTA)
    print_ascii_centered("WE HOPE TO", Fore.LIGHTRED_EX)
    print_ascii_centered("SEE YOU SOON!", Fore.YELLOW)

# Run it
show_farewell_screen()
