import pyfiglet
from colorama import Fore, init, Style
import time
import shutil

# Initialize colorama
init(autoreset=True)        

# Typewriter effect function
def typewriter_effect(text, delay=0.00125, color=Fore.RESET):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)  # Reset style after printing

# Function to print centered ASCII text in a color
def print_ascii_centered(text, color, font='standard', delay=0.00125):
    figlet = pyfiglet.Figlet(font=font)
    ascii_art = figlet.renderText(text)
    terminal_width = shutil.get_terminal_size().columns

    for line in ascii_art.splitlines():
        centered_line = line.center(terminal_width)
        typewriter_effect(centered_line, delay, color)

# Final farewell screen function
def show_farewell_screen():
    print_ascii_centered("THANK YOU", Fore.MAGENTA)
    print_ascii_centered("WE HOPE TO", Fore.LIGHTRED_EX)
    print_ascii_centered("SEE YOU SOON!", Fore.YELLOW)

 #Run it
# show_farewell_screen()









