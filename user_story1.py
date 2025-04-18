# comment

# achievements: generate ticket displaying the ticket id at random, name of park, name and age of customer, expiry date and available ride names only, balance hrs
# processes: inputs need to be asked, bg prcessing: spending amt to hrs calculation, all usecases should be handled

# step 1: import all files and def all user functions
from infra.entities.amusement_park import amusement_park
from infra.entities.ride import ride
from infra.entities.ticket import ticket
from infra.entities.customer import customer

# this asks the user for spending amt and checks if it is a valid int or not
def input_spending_amt(spending_amt):
    casted_spending_amt = cast_spending_amt(spending_amt)
    if(casted_spending_amt is None):
        print("Invalid input. Please enter a valid spending amount.")
        return False
    if casted_spending_amt > 0 and casted_spending_amt % 100 == 0 and casted_spending_amt <= 5000:
        cus.set_spending_amt(spending_amt)
        return True
    else:
        print("Invalid input. Please enter a valid spending amount. must be a multiple of 100 and less than or equal to 5000rs")
        return False

def money_to_hours(spend_amt):
    # Assuming 1 hour of ride time costs 100rs
    # we check if the spending amount is a multiple of 100 and the quotient is the hour count
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

# step 2: input spending amt and validate it
cus = customer()
ask_amt = input("Enter spending amount: ")

if input_spending_amt(ask_amt):
    balance_hrs = money_to_hours(cast_spending_amt(ask_amt))
    print(balance_hrs)

# import all libraries (ride, customer, ticket, amusement_park)
# ask for spending amt and validate it using int_value function as a check
# convert spending amt to hours using money_to_hours function while checking if the spending amt is a multiple of 100 and the quotient is the hour count, max is 5000rs
# if spending amt is greater than 5000rs, return None and print a message saying spending amt is too high and break if not multiple of 100
# ask for the name and age of the customer and validate it using str_value and int_value functions respectively
# get a proper array of all the rides with their names, duration, min age and max age criterion and availability, instantiating the ride class
# the age inputted by the user must be compared with the min and max age of the ride and if it is in range, keep it in the array of available rides, else remove it from the array of available rides
# create a ticket object and set the ticket id, available rides, expiry duration and balance hours using the ticket class
# the expiry duration is set to 8 hours from the current time and the ticket id is generated randomly using the random library
# the ticket is generated after a prompt, displaying the ticket id, name of park (amusement park class), name and age of customer, expiry duration of the ticket, available rides and balance hours




