import pyfiglet
from colorama import init, Fore, Style
import shutil
import os
import time
from infra.entities.ride import ride

init(autoreset=True)
UNDERLINE = '\033[4m'
BOLD = '\033[1m'
class slide:
    # this func is used to create the vertical gradient for the text in the header.
    def vertical_gradient(self, text, font, colors):
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
    
    def underline_text(self, text):
        return f"{UNDERLINE}{text}{Style.RESET_ALL}"

    def bold_text(self, text):
        return f"{BOLD}{text}{Style.RESET_ALL}"

    def color_lines(self, ascii_text, gradient_colors):
        lines = ascii_text.splitlines()
        colored_lines = []
        num_colors = len(gradient_colors)
        for i, line in enumerate(lines):
            color_index = int((i / max(len(lines) - 1, 1)) * (num_colors - 1))
            color = gradient_colors[color_index]
            colored_lines.append(f"{color}{line}")
        return "\n".join(colored_lines)
    
    # Gradient utility
    def vertical_gradient_2(self, text, font, colors):
        ascii_art = pyfiglet.figlet_format(text, font=font)
        lines = ascii_art.split('\n')
        gradient_lines = []
        total_colors = len(colors)
        total_lines = len(lines)

        for i, line in enumerate(lines):
            color_index = int((i / max(1, total_lines - 1)) * (total_colors - 1))
            gradient_lines.append(colors[color_index] + line)
        return '\n'.join(gradient_lines)
    
    def create_ticket(self, title, ticket_info, rides):
        # Get terminal width
        terminal_width = shutil.get_terminal_size().columns
        border_line = "*." * terminal_width

        # Title with gradient and varsity font
        GRADIENT_COLORS = [Fore.YELLOW, Fore.LIGHTRED_EX, Fore.RED + Style.BRIGHT]
        figlet = pyfiglet.Figlet(font='varsity')
        ascii_title = figlet.renderText(title)
        colored_title = self.color_lines(ascii_title, GRADIENT_COLORS)

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
            label_text = f"{Fore.GREEN}{self.bold_text(self.underline_text(label.upper()))}"
            value_text = f"{Fore.GREEN}{str(value)}"
            print(label_text)
            print(value_text)
            print()

        # Add "Rides for You" section in purple
        rides_for_you_label = pyfiglet.Figlet(font='digital').renderText("Rides for You")
        print(Fore.MAGENTA + rides_for_you_label)  # Print "Rides for You" in purple

        # List of rides in yellow small font
        small_font = pyfiglet.Figlet(font='small')
        # rides = ride_names
        
        for ride in rides:
            ride_ascii = small_font.renderText(f"{ride.get_ride_no()} . {ride.get_ride_name()}")  # Bullet point with ride
            if ride.get_ride_no() == 9:
                print(Fore.RED + ride_ascii)
            else:
                print(Fore.YELLOW + ride_ascii)  # Print each ride in yellow small font

        # Print bottom border
        print(border_line)
    
    #start of ui for US-2
    def color_gradient_text(self, ascii_art, colors):
        lines = ascii_art.splitlines()
        total_lines = len(lines)
        colored_lines = []

        for i, line in enumerate(lines):
            if not line.strip():
                colored_lines.append('')
                continue
            color_index = int((i / max(total_lines - 1, 1)) * (len(colors) - 1))
            color = colors[color_index]
            colored_lines.append(color + line)
        
        return "\n".join(colored_lines)
    
    def show_selected_ride(self, ride_name):
        # os.system('cls' if os.name == 'nt' else 'clear')

        terminal_width = shutil.get_terminal_size().columns
        

        

        # "YOU HAVE CHOSEN THE RIDE:"
        straight_font = pyfiglet.Figlet(font='straight')
        chosen_text = straight_font.renderText("YOU HAVE CHOSEN THE RIDE:")
        print(Fore.YELLOW + chosen_text)

        # Selected ride name in green
        ride_text = straight_font.renderText(ride_name.upper())
        print(Fore.GREEN + ride_text)

        # "HAVE A" in yellow
        have_a_text = straight_font.renderText("HAVE A")
        print(Fore.YELLOW + have_a_text)

        # "RUSHTASTIC" in red-orange-yellow gradient
        rushtastic_text = straight_font.renderText("RUSHTASTIC")
        gradient_colors = [Fore.RED, Fore.LIGHTRED_EX, Fore.YELLOW]
        colored_rushtastic = self.color_gradient_text(rushtastic_text, gradient_colors)
        print(colored_rushtastic)

        # "TIME !" in yellow
        time_text = straight_font.renderText("TIME !")
        print(Fore.YELLOW + time_text)
    
    def ask_for_replay(self, balance_hours):
        print(Fore.BLUE + f"YOU HAVE {round(balance_hours, 2)} BALANCE HOURS REMAINING")

        # Line 2: play again in green (straight font)
        
        print(Fore.GREEN + "TO PLAY AGAIN ENTER 1")

        # Line 3: exit in red (straight font)
        
        print(Fore.RED + "TO EXIT ENTER 2")
    
    def create_end_ticket(self, title, ticket_info):
    # Get terminal width
        terminal_width = shutil.get_terminal_size().columns
        border_line = "*." * terminal_width

        # Title with gradient and varsity font
        GRADIENT_COLORS = [Fore.YELLOW, Fore.LIGHTRED_EX, Fore.RED + Style.BRIGHT]
        figlet = pyfiglet.Figlet(font='varsity')
        ascii_title = figlet.renderText(title)
        colored_title = self.color_lines(ascii_title, GRADIENT_COLORS)

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
            label_text = f"{Fore.GREEN}{self.bold_text(self.underline_text(label.upper()))}"
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
            ("NO RIDES AVAILABLE ", Fore.BLUE)
            
        ]
        
        for ride, color in rides:
            ride_ascii = small_font.renderText(f"• {ride}")  # Bullet point with ride
            print(color + ride_ascii)

    
        

        # Print bottom border
        print(border_line)
    
    def typewriter_effect(text, delay=0.00125, color=Fore.RESET):
        for char in text:
            print(color + char, end='', flush=True)
            time.sleep(delay)
        print(Style.RESET_ALL)  # Reset style after printing

# Function to print centered ASCII text in a color
    def print_ascii_centered(self, text, color, font='standard', delay=0.00125):
        figlet = pyfiglet.Figlet(font=font)
        ascii_art = figlet.renderText(text)
        terminal_width = shutil.get_terminal_size().columns

        for line in ascii_art.splitlines():
            centered_line = line.center(terminal_width)
            self.typewriter_effect(centered_line, delay, color)

# Final farewell screen function
    def show_farewell_screen(self):
        self.print_ascii_centered("THANK YOU", Fore.MAGENTA)
        self.print_ascii_centered("WE HOPE TO", Fore.LIGHTRED_EX)
        self.print_ascii_centered("SEE YOU SOON!", Fore.YELLOW)



                



    # Color gradients
    # blue_green_gradient = [Fore.CYAN, Fore.GREEN]                    # Neon Blue to Neon Green
    # yellow_red_gradient = [Fore.YELLOW, Fore.RED]                   # Neon Yellow to Neon Red
    # darkblue_pink_gradient = [Fore.BLUE, Fore.LIGHTMAGENTA_EX]      # Dark Blue to Bright Pink

    # # Generate ASCII art with vertical gradients
    # slide_1 = slide_1()
    # welcome_text = slide_1.vertical_gradient("Welcome to", font="tombstone", colors=blue_green_gradient)
    # rushland_text = slide_1.vertical_gradient("Rushland", font="varsity", colors=yellow_red_gradient)
    # opening_hours_text = slide_1.vertical_gradient("[ 9:00am to 6:00pm ]", font="tombstone", colors=darkblue_pink_gradient)



