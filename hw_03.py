
# task_number_1
from datetime import datetime

def get_days_from_today(date):
    # Exception handling. If the date format is entered correctly.
    try:
        # Converting a date string in the 'YYYY-MM-DD' format into a datetime object.
        date_object = datetime.strptime(date, '%Y-%m-%d')
        # Getting the current date using datetime.today().
        date_now = datetime.today()
        # Calculating the difference between the current date and the specified date.
        result = date_now - date_object
        # Returning the difference in days as an integer.
        return result.days
    # Exception handling. If the date format is entered incorrectly.
    except ValueError:
        return "Invalid date format. Please enter the date in 'YYYY-MM-DD' format."

print(get_days_from_today("2020-10-09")) 






# task_number_2
import random

def get_numbers_ticket(min, max, quantity):
    # Ensure that the input parameters meet the specified constraints.
    if min >= 1 and \
       max <= 1000 and \
       quantity >= 1 and \
       quantity <= 1000 and \
       quantity >= min and \
       quantity <= max:
       numbers = []
       # We ensure the uniqueness of numbers.
       range_in_numbers = range(min, max)
       # We use the random module to generate random numbers.
       numbers = random.sample(range_in_numbers, k=quantity)
       # We add a random number to the list.
       return numbers
    else:
        return []
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)





# task_number_3
import re


def normalize_phone(phone_number):
    # We remove all characters from the phone number except
    # digits and the "+" sign.
    sanitized_number = re.sub(r"[^\d+]", "", phone_number)
    if not sanitized_number.startswith("+"):
        if sanitized_number.startswith("380"):
            sanitized_number = "+" + sanitized_number
        else:
            sanitized_number = "+38" + sanitized_number
        # We return the normalized phone number.
    return sanitized_number
    
    
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
# A list comprehension for normalizing each phone number.
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)




# task_number_4

from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()

    greetings = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days
        
        while birthday_this_year.weekday() <= 5:
            birthday_this_year += timedelta(days=1)
        
        if 0 <= days_until_birthday <= 7:
            greetings.append({"name": user["name"], "greeting_date": birthday_this_year})
    
    return greetings



users = [
    {"name": "John Doe", "birthday": "1985.04.24"},
    {"name": "Jane Smith", "birthday": "1990.05.24"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
