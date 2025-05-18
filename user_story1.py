import pyfiglet

from colorama import init, Fore, Style
from ui_part1 import *


import random

from infra.entities.amusement_park import amusement_park
from infra.entities.ride import ride
from infra.entities.ticket import ticket
from infra.entities.customer import customer
from datetime import *
from f_screen import *

#INITIALIZE COLORAMA FOR WINDOWS
GREEN = Fore.GREEN + Style.BRIGHT
RED = Fore.RED + Style.BRIGHT
RESET = Style.RESET_ALL

# ANSI escape code for underline and bold
UNDERLINE = '\033[4m'
BOLD = '\033[1m'

# # Color gradients
blue_green_gradient = [Fore.CYAN, Fore.GREEN]                    # Neon Blue to Neon Green
yellow_red_gradient = [Fore.YELLOW, Fore.RED]                   # Neon Yellow to Neon Red
darkblue_pink_gradient = [Fore.BLUE, Fore.LIGHTMAGENTA_EX]      # Dark Blue to Bright Pink
rushland_gradient = [Fore.LIGHTYELLOW_EX, Fore.YELLOW, Fore.LIGHTRED_EX, Fore.RED]
terms_gradient = [Fore.MAGENTA, Fore.LIGHTMAGENTA_EX, Fore.BLUE]
green_gradient = [Fore.LIGHTGREEN_EX, Fore.GREEN]

# INIT PARK OBJECT
ap = amusement_park()  # Opening time set to 9:00 AM
ap.set_opening_time(timedelta(hours=10, minutes=0))
ap.set_closing_time(ap.get_opening_time() + timedelta(hours=9))
ap.set_no_of_rides(4)
ap.set_park_name("Rushland")
ap.set_per_hr_rate(100)  # Assuming 100rs per hour
# print(ap.get_opening_time())
# print(ap.get_closing_time())
# print(ap.get_working_hours())

# GENERATE SLIDE_1 OBJECT
sl_1 = slide()
# ap = amusement_park()  # Opening time set to 9:00 AM
# welcome_text = sl_1.vertical_gradient("Welcome to", font="tombstone", colors=blue_green_gradient)
welcome_text = sl_1.vertical_gradient(f"Welcome to", font="varsity", colors=yellow_red_gradient)
rushland_text = sl_1.vertical_gradient(f"{ap.get_park_name()}", font="varsity", colors=yellow_red_gradient)
opening_hours_text = sl_1.vertical_gradient(f"[{ap.get_opening_time()} to {ap.get_closing_time() - timedelta(hours=12)}]", font="tombstone", colors=darkblue_pink_gradient)

# 4 ride objects of the ride class with their corresponding attributes
# name, duration, minage, max age
ride_1 = ride('Roller Coaster',20, 15, 50, 1)
ride_2 = ride('Photo Booth',20, 1, 100, 2)
ride_3 = ride('Laser Tag',50, 10, 60, 3)
ride_4 = ride('Horse Riding',60, 10, 65, 4)
end_ride = ride("QUIT", 0, 0, 0, 9)

#Render headers
rushland_header = sl_1.vertical_gradient(f"{ap.get_park_name()}", "varsity", rushland_gradient)
terms_header = sl_1.vertical_gradient("Terms & Conditions", "digital", terms_gradient)

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

rides = [
    (f"{ride_4.get_ride_name()}", f"{ride_4.get_ride_duration()} mins", f"{ride_4.get_min_age()} years to {ride_4.get_max_age()} years"),
    (f"{ride_3.get_ride_name()}", f"{ride_3.get_ride_duration()} mins", f"{ride_3.get_min_age()} years to {ride_3.get_max_age()} years"),
    (f"{ride_2.get_ride_name()}", f"{ride_2.get_ride_duration()} mins", f"{ride_2.get_min_age()} year to {ride_2.get_max_age()} years"),
    (f"{ride_1.get_ride_name()}", f"{ride_1.get_ride_duration()} mins", f"{ride_1.get_min_age()} years to {ride_1.get_max_age()} years"),
]

# print(welcome_text)
# print(rushland_text)
# print(opening_hours_text)



# this func does some more chekcs on the spending amt input and assigns the var if all checks are passed
# note: dont keep any funcs orphaned, not very logical for many pages, 
def input_spending_amt(spending_amt):
    casted_spending_amt = cast_spending_amt(spending_amt)
    if(casted_spending_amt is None):
        
        return False
    if casted_spending_amt > 0 and casted_spending_amt % 100 == 0 and casted_spending_amt <= 900:
        cus.set_spending_amt(spending_amt)
        return True
    else:
        
        return False 

def money_to_hours(spend_amt):
    # Assuming 1 hour of ride time costs 100rs
    # we check if the spending amount is a multiple of 100 and the quotient is the hour count
    # this func returns the spending amount divided by 100 to get the balance hours
    return spend_amt / 100
        
def cast_spending_amt(spending_amt):
    # this func checks if the spending amt is a valid int or float and returns it as a float or int
    casted_spending_amt = 0.00
    if cus.int_value(spending_amt):
        if cus.float_value(spending_amt):
            casted_spending_amt = float(spending_amt)
        else:
            casted_spending_amt = int(spending_amt)    
    else:
        casted_spending_amt = None     
    return casted_spending_amt

def check_quit(prompt):
    if prompt == 'q':
        return True
    else:
        return False

def set_name_of_player(name):
    # checks if the name is a valid string or not and sets it to the player name attribute of the customer class after checks are passed
    
    if cus.str_value(name):
        if name == "":
            return False
        else:
            ascii_val = ord(name[0])
            for char in name:
                ascii_val = ord(char)
                if ((65 <= ascii_val <= 90) or (97 <= ascii_val <= 122)):
                    cus.set_player_name(name) 
                    return True
                else:
                    return False
        
            if cus.int_value(name):
                
                return False
            elif cus.float_value(name):
                
                return False
            else:
                cus.set_player_name(name)
                return True
        
    else:
        
        return False

def cast_age(age):
    # this func checks if the age is a valid int or float and returns it as a float or int
    casted_age = 0.00
    if cus.int_value(age):
        if cus.float_value(age):
            casted_age = float(age)
        else:
            casted_age = int(age)
    else:
        casted_age = None
    return casted_age

def set_age_of_player(age):
    # checks the age prompt further and sets it to the player age attribute of the customer class if chekcs are passed.
    casted_age = cast_age(age)
    if casted_age is None:
        
        return False
    if casted_age >= 1 and casted_age % 1 == 0 and casted_age <= 100:
        cus.set_player_age(age)
        return True
    else:
        
        return False
    
def set_random_id():
    # this func generates a random ticket id using the random library and returns it
    ticket_id = ""
    for i in range(6):
        ticket_id += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    return ticket_id



def filter_rides(rides, cus_age, bh_hours):
    # this func takes the rides min age and max age and compares with the cus age and appends the name in a alist if statemet is satisfied
    available_rides = []
    # available_rides_nos = []
    no = 0
    for i in range(len(rides)):
        if rides[i].get_min_age() <= int(cus_age) <= rides[i].get_max_age() and rides[i].get_ride_duration()/60 <= bh_hours:
            available_rides.append(rides[i])
            # available_rides_nos.append(rides[i].get_ride_no())
            no += 1
        
    return available_rides

def get_ride_nos(eligible_rides):
    eligible_ride_nos = []
    for ride in eligible_rides:
        eligible_ride_nos.append(ride.get_ride_no())
    return eligible_ride_nos

cus = customer()
run = True

   


