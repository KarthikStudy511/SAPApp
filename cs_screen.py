import os
import pyfiglet
from colorama import Fore, init, Style
import shutil

init(autoreset=True)

def color_gradient_text(ascii_art, colors):
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

def show_selected_ride(ride_name):
    os.system('cls' if os.name == 'nt' else 'clear')

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
    colored_rushtastic = color_gradient_text(rushtastic_text, gradient_colors)
    print(colored_rushtastic)

    # "TIME !" in yellow
    time_text = straight_font.renderText("TIME !")
    print(Fore.YELLOW + time_text)





init(autoreset=True)

def color_gradient_text(ascii_art, colors):
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

def show_selected_ride(ride_name, balance_hours):
    os.system('cls' if os.name == 'nt' else 'clear')

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
    colored_rushtastic = color_gradient_text(rushtastic_text, gradient_colors)
    print(colored_rushtastic)

    # "TIME !" in yellow
    time_text = straight_font.renderText("TIME !")
    print(Fore.YELLOW + time_text)

    

    # New section: balance and next instructions
    # Line 1: balance remaining in blue (straight font)
   
    print(Fore.BLUE + f"YOU HAVE {balance_hours} BALANCE HOURS REMAINING")

    # Line 2: play again in green (straight font)
    
    print(Fore.GREEN + "TO PLAY AGAIN ENTER 1")

    # Line 3: exit in red (straight font)
    
    print(Fore.RED + "TO EXIT ENTER 2")

# Example usage
show_selected_ride("photo booth", "2.5")



