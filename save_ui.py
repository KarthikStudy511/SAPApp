 #slide 1
from PIL import Image
from ascii_magic import AsciiArt
import ascii_magic
import shutil

# # Load the image
# img = Image.open("cam.jpg")

# # Resize to passport size (roughly 40 chars wide)
# ascii_art = AsciiArt.from_image(img)
# ascii_output = ascii_art.to_ascii(columns=40)

# Get terminal width
# terminal_width = shutil.get_terminal_size().columns

# # Center each line
# centered_output = "\n".join(
#     line.center(terminal_width) for line in ascii_output.splitlines()
# )

# # Print centered ASCII image




  # slide 2
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

# Print all parts
print(welcome_text)
print(rushland_text)
print(opening_hours_text)

#slide 4 (terms and conditions)
import pyfiglet
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Gradient utility
def vertical_gradients(text, font, colors):
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
rushland_header = vertical_gradients("Rushland", "varsity", rushland_gradient)
terms_header = vertical_gradients("Terms & Conditions", "digital", terms_gradient)

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
print(rushland_header)
print(terms_header)

for point in terms_points:
    print(Fore.YELLOW + f"• {point}\n")

print(available_rides_colored)

for ride_name, duration, age in rides:
    print(Fore.RED + Style.BRIGHT + '\033[4m' + ride_name + '\033[0m')  # Ride name in bold red + underline
    print(Fore.BLUE + "Duration: " + green_gradient[0] + duration)
    print(Fore.BLUE + "Age limit: " + green_gradient[1] + age)
    print()



#slide 5(amount validation)
#slide 6(ticet generation)n    
import pyfiglet
from colorama import Fore, Style, init
import shutil

# Initialize colorama
init(autoreset=True)

# ANSI escape code for underline and bold
UNDERLINE = '\033[4m'
BOLD = '\033[1m'

def underline_text(text):
    return f"{UNDERLINE}{text}{Style.RESET_ALL}"

def bold_text(text):
    return f"{BOLD}{text}{Style.RESET_ALL}"

def color_lines(ascii_text, gradient_colors):
    lines = ascii_text.splitlines()
    colored_lines = []
    num_colors = len(gradient_colors)
    for i, line in enumerate(lines):
        color_index = int((i / max(len(lines) - 1, 1)) * (num_colors - 1))
        color = gradient_colors[color_index]
        colored_lines.append(f"{color}{line}")
    return "\n".join(colored_lines)

def create_ticket(title, ticket_info):
    # Get terminal width
    terminal_width = shutil.get_terminal_size().columns
    border_line = "*." * terminal_width

    # Title with gradient and varsity font
    GRADIENT_COLORS = [Fore.YELLOW, Fore.LIGHTRED_EX, Fore.RED + Style.BRIGHT]
    figlet = pyfiglet.Figlet(font='varsity')
    ascii_title = figlet.renderText(title)
    colored_title = color_lines(ascii_title, GRADIENT_COLORS)

    # Print top border
    print(border_line)

    # Print centered title
    for line in colored_title.splitlines():
        print(line.center(terminal_width))

    # Space after title
    print()

    # Print each ticket field
    for label, value in ticket_info.items():
        if label.lower() == "applicable rides":
            continue  # Skip the applicable rides section
        label_text = f"{Fore.GREEN}{bold_text(underline_text(label.upper()))}"
        value_text = f"{Fore.GREEN}{str(value)}"
        print(label_text)
        print(value_text)
        print()

    # Add "Rides for You" section in purple
    rides_for_you_label = pyfiglet.Figlet(font='digital').renderText("Rides for You")
    print(Fore.MAGENTA + rides_for_you_label)  # Print "Rides for You" in purple

    # List of rides in yellow small font
    small_font = pyfiglet.Figlet(font='small')
    rides = [
        "1 . Horse Riding", 
        "2 . Roller Coaster",
        "3 . Laser Tag",
        "4 . Photo Booth"
    ]
    
    for ride in rides:
        ride_ascii = small_font.renderText(f"• {ride}")  # Bullet point with ride
        print(Fore.YELLOW + ride_ascii)  # Print each ride in yellow small font

    # Print bottom border
    print(border_line)

# Example usage
ticket_info = {
    "Ticket ID": "A1B2C3",
    "Name": "Jane Doe",
    "Age": "16",
    "Balance Hours": "4.5"
}

create_ticket("Rushland Ticket", ticket_info)












