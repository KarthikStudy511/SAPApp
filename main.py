import pyfiglet
from colorama import init, Fore, Style
from ui_part1 import *
import random
from infra.entities.amusement_park import amusement_park
from infra.entities.ride import ride
from infra.entities.ticket import ticket
from infra.entities.customer import customer
from user_story1 import *
from user_story2 import *

# Initialize colorama
init()
GREEN = Fore.GREEN + Style.BRIGHT
RED = Fore.RED + Style.BRIGHT
RESET = Style.RESET_ALL

# Display splash screen
sl_1.show_splash_screen()
print(welcome_text)
print(rushland_text)
print(opening_hours_text)

run = True
while run:
    # Ask for name and age
    print(f"{GREEN}INPUT NAME:{RESET}")
    ask_name = input()
    print(f"{GREEN}INPUT AGE:{RESET}")
    ask_age = input()

    if set_name_of_player(ask_name):
        if set_age_of_player(ask_age):
            # Display terms and conditions and available rides
            print(rushland_header)
            print(terms_header)
            for point in terms_points:
                print(Fore.YELLOW + f"• {point}\n")
            print(available_rides_colored)
            for ride_name, duration, age in rides:
                print(Fore.RED + Style.BRIGHT + '\033[4m' + ride_name + '\033[0m')
                print(Fore.BLUE + "Duration: " + green_gradient[0] + duration)
                print(Fore.BLUE + "Age limit: " + green_gradient[1] + age)
                print()

            while True:
                # Prompt for terms agreement
                print(f"{GREEN}Do you agree to the terms and conditions? 1 for yes and 2 for no{RESET}")
                ask_continue = input()
                if ask_continue == "1":
                    while True:
                        # Ask for spending amount
                        print(f"{GREEN}Please enter the spending amount:{RESET}")
                        ask_amt = input()
                        if input_spending_amt(cast_spending_amt(ask_amt)):
                            # Initialize customer and balance hours
                            balance_hrs = money_to_hours(cast_spending_amt(ask_amt))
                            cus.set_balance_hours(balance_hrs)
                            el_ride_names = []
                            el_ride_nos = []

                            # Filter eligible rides
                            el_rides = filter_rides([ride_1, ride_2, ride_3, ride_4], cus.get_player_age(), cus.get_balance_hours())
                            for el_ride in el_rides:
                                el_ride_names.append(el_ride.get_ride_name())
                                el_ride_nos.append(str(el_ride.get_ride_no()))
                            el_rides.append(end_ride)
                            el_ride_nos.append('9')  # Add exit option

                            # Create initial ticket
                            ticket_info = {
                                "Ticket ID": set_random_id(),
                                "Name": cus.get_player_name(),
                                "Age": cus.get_player_age(),
                                "Balance Hours": round(cus.get_balance_hours(), 2),
                                "Applicable Rides": el_ride_names,
                            }
                            sl_1.create_ticket(f"{ap.get_park_name()} Ticket", ticket_info, el_rides)

                            # Main ride selection loop
                            min_ride_duration = min([r.get_ride_duration() / 60 for r in [ride_1, ride_2, ride_3, ride_4]])
                            while True:
                                
                                print(f"{GREEN}Please select a ride number from the list above:{RESET}")
                                ask_ride_choice = input()

                                # Validate ride choice
                                if is_valid_ride_choice(ask_ride_choice, el_ride_nos, cus.get_balance_hours(), el_rides):
                                    if ask_ride_choice == '9':
                                        show_farewell_screen()
                                        run = False
                                        break

                                    # Find chosen ride
                                    chosen_ride_name = None
                                    chosen_ride_duration = None
                                    for each_ride in el_rides:
                                        if str(each_ride.get_ride_no()) == ask_ride_choice:
                                            chosen_ride_name = each_ride.get_ride_name()
                                            chosen_ride_duration = each_ride.get_ride_duration() / 60
                                            break

                                    # Deduct balance hours
                                    cus.set_balance_hours(deduct_hours_from_balance(ask_ride_choice, cus.get_balance_hours(), el_rides))
                                    
                                    sl_2.show_selected_ride(chosen_ride_name)

                                    # Replay loop
                                    while True:
                                        if not check_bh(cus.get_balance_hours(), min_ride_duration):
                                            ticket_info = {
                                                "Ticket ID": set_random_id(),
                                                "Name": cus.get_player_name(),
                                                "Age": cus.get_player_age(),
                                                "Balance Hours": round(cus.get_balance_hours(), 2),
                                            }
                                            sl_1.create_end_ticket(f"{ap.get_park_name()} Ticket", ticket_info)
                                            show_farewell_screen()
                                            run = False
                                            break

                                        sl_2.ask_for_replay(cus.get_balance_hours())
                                        ask_to_replay = input()
                                        if set_ask_to_replay(ask_to_replay):
                                            print(f"{GREEN}You have selected to play again.{RESET}")
                                            ticket_info["Balance Hours"] = round(cus.get_balance_hours(), 2)
                                            el_rides = filter_rides([ride_1, ride_2, ride_3, ride_4], cus.get_player_age(), cus.get_balance_hours())
                                            el_ride_names = [r.get_ride_name() for r in el_rides]
                                            el_ride_nos = [str(r.get_ride_no()) for r in el_rides]
                                            el_rides.append(end_ride)
                                            el_ride_nos.append('9')
                                            sl_1.create_ticket(f"{ap.get_park_name()} Ticket", ticket_info, el_rides)
                                            break
                                        elif ask_to_replay == "2":
                                            show_farewell_screen()
                                            run = False
                                            break
                                        else:
                                            print(f"{RED}OOPS! YOU HAVE ENTERED AN INVALID INPUT. PLEASE ENTER A VALID INPUT.{RESET}")
                                else:
                                    print(f"{RED}OOPS! YOU HAVE ENTERED AN INVALID RIDE CHOICE. PLEASE ENTER A VALID INPUT.{RESET}")

                                if not run:
                                    break
                            break
                        else:
                            print(f"{RED}OOPS! YOU HAVE ENTERED AN INVALID SPENDING AMOUNT. PLEASE ENTER A VALID AMOUNT.{RESET}")
                    break
                elif ask_continue == "2":
                    show_farewell_screen()
                    run = False
                    break
                else:
                    print(f"{RED}OOPS! YOU HAVE ENTERED AN INVALID INPUT. PLEASE ENTER A VALID INPUT.{RESET}")
        else:
            print(f"{RED}OOPS! YOU HAVE ENTERED AN INVALID AGE. PLEASE ENTER A VALID AGE.{RESET}")
    else:
        print(f"{RED}OOPS! YOU HAVE ENTERED AN INVALID NAME. PLEASE ENTER A VALID NAME.{RESET}")