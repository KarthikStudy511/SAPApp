from user_story1 import *
from infra.entities.amusement_park import amusement_park
from infra.entities.ride import ride
from infra.entities.ticket import ticket
from infra.entities.customer import customer
from datetime import *
import random
import pyfiglet

from colorama import init, Fore, Style
from ui_part1 import *
RED = Fore.RED + Style.BRIGHT
sl_2 = slide()
def set_ride_choice(choice, el_ride_nos):
    # to be true, the ride choice must be a number 
    if choice in el_ride_nos:
        return True
    else:
        return False

def convert_min_to_hrs(choice, rides):
    # this func takes only the ride with the ride no same as the choice and converts the duration of that ride to hrs
    try:
        choice_int = int(choice)
    except ValueError:
        return 0
    for ride in rides:
        if ride.get_ride_no() == choice_int:
            return round(ride.get_ride_duration() / 60, 2)
    return 0  # Return 0 if no ride matches
def deduct_hours_from_balance(choice, balance_hrs, rides):
    # this func takes the ride choice and the balance hrs and deducts the ride duration from the balance hrs
    # for ride in rides:
    #     if ride.get_ride_no() == int(choice):
    #         return round(balance_hrs - (ride.get_ride_duration() / 60), 2)
    #     else:
    #         pass
    return balance_hrs - convert_min_to_hrs(choice, rides)

def check_bh(balance_hrs, min_ride_duration):
    # this func checks if the balance hrs is less than 0
    if balance_hrs < min_ride_duration:
        return False
    else:
        return True

def set_ask_to_replay(ask_to_replay):
    # this func checks if the ask to leave is 1 or 2
    if ask_to_replay == "1":
        return True
    elif ask_to_replay == "2":
        return False
    else:
        return False

def is_valid_ride_choice(choice, el_ride_nos, balance_hrs, rides):
    """
    Validates if the ride choice is a valid ride number and if the customer has enough balance hours.
    Returns True if valid, False otherwise.
    """
    # Check if choice is a valid ride number
    try:
        choice_int = int(choice)  # Ensure choice can be converted to int
        if choice_int not in el_ride_nos:
            return False
    except ValueError:
        return False  # Invalid if choice is not a number
    
    # Check if balance hours are sufficient for the ride
    ride_duration_hrs = convert_min_to_hrs(choice, rides)
    if ride_duration_hrs == 0:  # No ride found for choice
        return False
    if balance_hrs < ride_duration_hrs:
        return False  # Insufficient balance hours
    
    return True

def get_valid_ride_choice(balance_hrs, el_ride_nos, el_rides):
    while True:
        
        ask_ride_choice = input()
        
        if is_valid_ride_choice(ask_ride_choice, el_ride_nos, balance_hrs, el_rides):
            return ask_ride_choice
        else:
            print("{RED}OOPS! YOU HAVE ENTERED AN INVALID RIDE CHOICE, PLEASE TRY AGAIN!")
# 1 - roller coaster, 2 - photo booth, 3- laser tag, 4 - horse riding