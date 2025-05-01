# from pyfiglet import Figlet
# from colorama import init, Fore
# import math

# # Initialize colorama for Windows
# init()

# # Define available colors for the gradient (colorama's basic colors)
# colors = [
#     Fore.RED,
#     Fore.YELLOW,  # Used as an approximation for orange
#     Fore.GREEN,
#     Fore.CYAN,
#     Fore.BLUE,
#     Fore.MAGENTA
# ]

# # Generate ASCII art with pyfiglet
# f = Figlet(font='Starwars')
# text = f.renderText('Hello World')

# # Split the text into lines
# lines = text.split('\n')

# # Apply gradient effect by cycling through colors
# for i, line in enumerate(lines):
#     # Calculate color index based on line position
#     # Use a sine wave to create a smooth, cyclic gradient
#     color_index = int((math.sin(i / len(lines) * math.pi * 2) + 1) / 2 * (len(colors) - 1))
#     color = colors[color_index]
#     print(color + line + Fore.RESET)
import pyfiglet
import os

print(os.path.join(os.path.dirname(pyfiglet.__file__), 'fonts'))
