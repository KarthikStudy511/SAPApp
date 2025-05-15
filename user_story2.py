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

sl_2 = slide()
def set_ride_choice(choice, el_ride_nos):
    # to be true, the ride choice must be a number 
    if choice in el_ride_nos:
        return True
    else:
        return False

def convert_min_to_hrs(choice, rides):
    # this func takes only the ride with the ride no same as the choice and converts the duration of that ride to hrs
    for ride in rides:
        if ride.get_ride_no() == int(choice):
            return round(ride.get_ride_duration() / 60, 2)
        
        else:
            pass

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


# 1 - roller coaster, 2 - photo booth, 3- laser tag, 4 - horse riding


