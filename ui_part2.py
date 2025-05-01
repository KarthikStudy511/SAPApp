import pyfiglet
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Gradient utility
def vertical_gradient(text, font, colors):
    ascii_art = pyfiglet.figlet_format(text, font=font)
    lines = ascii_art.split('\n')
    gradient_lines = []
    total_colors = len(colors)
    total_lines = len(lines)

    for i, line in enumerate(lines):
        color_index = int((i / max(1, total_lines - 1)) * (total_colors - 1))
        gradient_lines.append(colors[color_index] + line)
    return '\n'.join(gradient_lines)

# Color gradients
rushland_gradient = [Fore.LIGHTYELLOW_EX, Fore.YELLOW, Fore.LIGHTRED_EX, Fore.RED]
terms_gradient = [Fore.MAGENTA, Fore.LIGHTMAGENTA_EX, Fore.BLUE]
green_gradient = [Fore.LIGHTGREEN_EX, Fore.GREEN]

# Render headers
rushland_header = vertical_gradient("Rushland", "varsity", rushland_gradient)
terms_header = vertical_gradient("Terms & Conditions", "digital", terms_gradient)

# Static red available rides header
available_rides_raw = pyfiglet.figlet_format("Available Rides", font="digital")
available_rides_colored = ''.join(Fore.RED + line + '\n' for line in available_rides_raw.split('\n'))

# T&C points
terms_points = [
    "Minimum amount to enter: ₹100",
    "All payments must be in multiples of ₹100 and positive amounts",
    "For every ₹100 spent, you get 1 hour of playtime",
    "Unused time cannot be refunded or carried over to the next day",
    "Rushland is not responsible for lost personal belongings — keep them safe"
]

# Rides info
rides = [
    ("HORSE RIDING", "30 mins", "10 to 65 years"),  
    ("LASER TAG", "50 mins", "10 to 60 years"),
    ("PHOTO BOOTH", "20 mins", "1 to 100 years"),
    ("ROLLER COASTER", "20 mins", "15 to 50 years")
]

# Display output
# print(rushland_header)
# print(terms_header)

# for point in terms_points:
#     print(Fore.YELLOW + f"• {point}\n")

# print(available_rides_colored)

# for ride_name, duration, age in rides:
#     print(Fore.RED + Style.BRIGHT + '\033[4m' + ride_name + '\033[0m')  # Ride name in bold red + underline
#     print(Fore.BLUE + "Duration: " + green_gradient[0] + duration)
#     print(Fore.BLUE + "Age limit: " + green_gradient[1] + age)
#     print()

