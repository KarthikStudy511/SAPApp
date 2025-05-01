import pyfiglet

from colorama import init, Fore, Style
from ui_part1 import *
from ui_part2 import *
import random
from ui_part3 import *
from infra.entities.amusement_park import amusement_park
from infra.entities.ride import ride
from infra.entities.ticket import ticket
from infra.entities.customer import customer
from user_story1 import *

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
                            ticket_info = {
                            "Ticket ID": set_random_id(),
                            "Name": cus.get_player_name(),
                            "Age": cus.get_player_age(),
                            "Balance Hours": cus.get_balance_hours(),
                            "Applicable Rides": filter_rides([ride_1, ride_2, ride_3, ride_4], cus.get_player_age()),
                            }

                            # this func creates a ticket object and sets the ticket id, available rides, expiry duration and balance hours using the ticket class
                            create_ticket("Rushland Ticket", ticket_info, ticket_info["Applicable Rides"])
                            run = False
                            break

                            
                
                        # filter rides based on age
                        # filter_rides([ride_1, ride_2, ride_3, ride_4], 2)

                        #display ticket with cus_name, cus_age, balance hours, list of eliglbe rides and their duration, (extra, ticket id and expiration time)
                    run = False
                    break
                
                    

                elif ask_continue == "2":
                    print(f"{GREEN}Thank you for using the program. Goodbye!{RESET}")
                    run = False
                    break
                    
                else:
                    print(f"{RED}OOPS! YOU HAVE ENTERED AN INVALID INPUT. PLEASE ENTER A VALID INPUT.{RESET}")

                

        else:
            print(f"{RED}OOPS! YOU HAVE ENTERED AN INVALID AGE. PLEASE ENTER A VALID AGE.{RESET}")
    else:
        print(f"{RED}OOPS! YOU HAVE ENTERED AN INVALID NAME. PLEASE ENTER A VALID NAME.{RESET}")










