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
        # List of rides in yellow small font
    small_font = pyfiglet.Figlet(font='small')
    rides = [
        ("NO RIDES AVAILABLE ", Fore.BLUE),
        
    ]
    
    for ride, color in rides:
        ride_ascii = small_font.renderText(f"• {ride}")  # Bullet point with ride
        print(color + ride_ascii)

  
    

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