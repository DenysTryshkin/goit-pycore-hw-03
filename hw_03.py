
#task_number_1
from datetime import datetime

def get_days_from_today(date):
    #"Exception handling. If the date format is entered correctly."
    try:
        #"Converting a date string in the 'YYYY-MM-DD' format into a datetime object."
        date_object = datetime.strptime(date, '%Y-%m-%d')
        #"Getting the current date using datetime.today()."
        date_now = datetime.today()
        #"Calculating the difference between the current date and the specified date."
        result = date_now - date_object
        #"Returning the difference in days as an integer."
        return result.days
    #"Exception handling. If the date format is entered incorrectly."
    except ValueError:
        return "Invalid date format. Please enter the date in 'YYYY-MM-DD' format."

print(get_days_from_today("2020-10-09")) 






#task_number_2
import random

def get_numbers_ticket(min, max, quantity):
    #"Ensure that the input parameters meet the specified constraints."
    if min >= 1 and \
       max <= 1000 and \
       quantity >= 1 and \
       quantity <= 1000 and \
       quantity >= min and \
       quantity <= max:
       numbers = []
       #"We ensure the uniqueness of numbers."
       range_in_numbers = range(min, max)
       #We use the random module to generate random numbers."
       numbers = random.sample(range_in_numbers, k=quantity)
       #"We add a random number to the list."
       return numbers
    else:
        return []
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)





#task_number_3


        