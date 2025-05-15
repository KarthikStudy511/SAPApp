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

print(welcome_text)
print(rushland_text)
print(opening_hours_text)
while run:
    # ask for name and age
    print(f"{GREEN}INPUT NAME:{RESET}")
    ask_name = input()
    print(f"{GREEN}INPUT AGE:{RESET}")
    ask_age = input()
    if set_name_of_player(ask_name):
        # by now, name has been validated
        if set_age_of_player(ask_age):
            # by now, age has been validated
            
            # these 10 lines prinout the availiable rides and the TOC 
            # fix: print these 2 as a func
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
                    
            while True:
                # here, we prompt the user whether they wanna keep going in a while loop in case they enter an invalid input.
                print(f"{GREEN} Do you agree to the terms and conditions? 1 for yes and 2 for no{RESET}")
                ask_continue = input()
                if ask_continue == "1":
                    while True:
                        # here, we keep asking for spending amt if invalid is given (reason for while loop)
                        print(f"{GREEN}Please enter the spending amount:{RESET}")
                        ask_amt = input()
                        if input_spending_amt(cast_spending_amt(ask_amt)):

                            # by now, spending amt has been validated
                            # balance hrs var is set up here.
                            balance_hrs = money_to_hours(cast_spending_amt(ask_amt))
                            cus.set_balance_hours(balance_hrs)
                            el_ride_names = []
                            el_ride_nos = []
                            for el_ride in filter_rides([ride_1, ride_2, ride_3, ride_4], cus.get_player_age(), cus.get_balance_hours()):
                                el_ride_names.append(el_ride.get_ride_name())
                                el_ride_nos.append(str(el_ride.get_ride_no()))

                            el_ride_nos.append('9')
                            
                            # ... (Previous code for name, age, spending amount, and ticket creation remains unchanged)

                            # Initialize ticket and eligible rides
                            ticket_info = {
                                "Ticket ID": set_random_id(),
                                "Name": cus.get_player_name(),
                                "Age": cus.get_player_age(),
                                "Balance Hours": cus.get_balance_hours(),
                                "Applicable Rides": el_ride_names,
                            }
                            el_rides = filter_rides([ride_1, ride_2, ride_3, ride_4], cus.get_player_age(), cus.get_balance_hours())
                            el_rides.append(end_ride)

                            # Create initial ticket
                            sl_1.create_ticket(f"{ap.get_park_name()} Ticket", ticket_info, el_rides)

                            # Main ride selection loop
                            while True:
                                # Check if there are enough balance hours to continue
                                # if not check_bh(cus.get_balance_hours(), min([ride.get_ride_duration()/60 for ride in el_rides if ride.get_ride_no() != 9])):
                                #     # print(f"{RED}No time left to ride. Thank you for visiting!{RESET}")
                                # #     ticket_info = {
                                # #     "Ticket ID": "A1B2C3",
                                # #     "Name": "Jane Doe",
                                # #     "Age": "16",
                                # #     "Balance Hours": "4.5"
                                # # }
                                    
                                # #     sl_2.create_end_ticket(f"{ap.get_park_name()} Ticket", ticket_info, el_rides)
                                # #     print("thank you")
                                # #     run = False
                                #     break

                                print(f"{GREEN}Please select a ride number from the list above:{RESET}")
                                ask_ride_choice = input()
                                chosen_ride_name = None
                                for ride in el_rides:
                                    if str(ride.get_ride_no()) == ask_ride_choice:
                                        chosen_ride_name = ride.get_ride_name()
                                        break

                                if set_ride_choice(ask_ride_choice, el_ride_nos):
                                    if ask_ride_choice == '9':
                                        # print(f"{GREEN}Thank you for visiting. Goodbye!{RESET}")
                                        show_farewell_screen()
                                        run = False
                                        break

                                    elif ask_ride_choice not in el_ride_nos:
                                        print("OOPS! YOU HAVE ENTERED AN INVALID RIDE CHOICE! TRY AGAIN!")
                                    
                                    else:

                                    # Deduct balance hours and show selected ride
                                        cus.set_balance_hours(deduct_hours_from_balance(ask_ride_choice, cus.get_balance_hours(), el_rides))
                                        sl_2.show_selected_ride(chosen_ride_name)

                                        # Replay loop
                                        while True:
                                            if cus.get_balance_hours() < ride_1.get_ride_duration()/60:
                                                # show end ticket here
                                                ticket_info = {
                                                "Ticket ID": set_random_id(),
                                                "Name": cus.get_player_name(),
                                                "Age": cus.get_player_age(),
                                                "Balance Hours": cus.get_balance_hours(),
                                            }
                                                
                                                sl_1.create_end_ticket(f"{ap.get_park_name()} Ticket", ticket_info)
                                                show_farewell_screen()
                                                
                                                run = False
                                                break
                                            sl_2.ask_for_replay(cus.get_balance_hours())
                                            ask_to_replay = input()
                                            if ask_to_replay == "1":
                                                print(f"{GREEN}You have selected to play again.{RESET}")
                                                # Update ticket_info with current balance hours
                                                ticket_info["Balance Hours"] = cus.get_balance_hours()
                                                # Re-create ticket with updated balance hours
                                                el_rides = filter_rides([ride_1, ride_2, ride_3, ride_4], cus.get_player_age(), cus.get_balance_hours())
                                                el_rides.append(end_ride)

                                                sl_1.create_ticket(f"{ap.get_park_name()} Ticket", ticket_info, el_rides)
                                                break  # Return to ride selection loop
                                            elif ask_to_replay == "2":
                                                show_farewell_screen()
                                                run = False
                                                break  # Exit both loops
                                            else:
                                                print(f"{RED}OOPS! YOU HAVE ENTERED AN INVALID INPUT. PLEASE ENTER A VALID INPUT.{RESET}")

                                        if not run:  # Exit if user chose to quit
                                            break
                                else:
                                    print(f"{RED}OOPS! YOU HAVE ENTERED AN INVALID RIDE CHOICE. PLEASE ENTER A VALID INPUT.{RESET}")

                            # End of program
                            # print(f"{GREEN}Thank you for using the program. Goodbye!{RESET}")
                                    # create ticket
            # sl_1.create_ticket(f"{ap.get_park_name()} Ticket", ticket_info, el_rides)     
                            break

                            
                
                        # filter rides based on age
                        # filter_rides([ride_1, ride_2, ride_3, ride_4], 2)

                        #display ticket with cus_name, cus_age, balance hours, list of eliglbe rides and their duration, (extra, ticket id and expiration time)
                    
                    break
                
                    

                elif ask_continue == "2":
                    # print(f"{GREEN}Thank you for using the program. Goodbye!{RESET}")
                    show_farewell_screen()
                    run = False
                    break
                    
                else:
                    print(f"{RED}OOPS! YOU HAVE ENTERED AN INVALID INPUT. PLEASE ENTER A VALID INPUT.{RESET}")

                

        else:
            print(f"{RED}OOPS! YOU HAVE ENTERED AN INVALID AGE. PLEASE ENTER A VALID AGE.{RESET}")
    else:
        print(f"{RED}OOPS! YOU HAVE ENTERED AN INVALID NAME. PLEASE ENTER A VALID NAME.{RESET}")










