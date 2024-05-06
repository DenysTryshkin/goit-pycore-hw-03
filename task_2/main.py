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