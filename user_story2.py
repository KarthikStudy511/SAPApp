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

def set_ride_choice(choice, el_ride_nos, bh_hours, chosen_ride_time):
    if choice in el_ride_nos and bh_hours >= chosen_ride_time:
        return True
    return False

def convert_min_to_hrs(choice, rides):
    try:
        choice_int = int(choice)
    except ValueError:
        return 0
    for ride in rides:
        if ride.get_ride_no() == choice_int:
            return ride.get_ride_duration() / 60
    return 0

def deduct_hours_from_balance(choice, balance_hrs, rides):
    return round(balance_hrs - convert_min_to_hrs(choice, rides), 2)

def check_bh(balance_hrs, min_ride_duration):
    return balance_hrs >= min_ride_duration

def set_ask_to_replay(ask_to_replay):
    if ask_to_replay == "1":
        return True
    elif ask_to_replay == "2":
        return False
    return False

def is_valid_ride_choice(choice, el_ride_nos, balance_hrs, rides):
    try:
        choice_int = int(choice)
        if str(choice_int) not in el_ride_nos:
            return False
    except ValueError:
        return False
    if choice != '9':
        ride_duration_hrs = convert_min_to_hrs(choice, rides)
        if ride_duration_hrs == 0 or balance_hrs < ride_duration_hrs:
            return False
    return True