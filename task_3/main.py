

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
