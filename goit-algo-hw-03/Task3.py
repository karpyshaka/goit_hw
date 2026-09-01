import re

def normalize_phone(phone_number):

    numbers = re.findall(r"\d+", phone_number)
    joined_numbers = "".join(numbers)

    if re.fullmatch(r"380\d{9}", joined_numbers):
        joined_numbers = re.sub(r"^380", "+380", joined_numbers)
        

    elif re.fullmatch(r"0\d{9}", joined_numbers):
        joined_numbers = re.sub(r"^0", "+380", joined_numbers)
        
    print(joined_numbers)        
    return joined_numbers
normalize_phone("(066)-488-27-21")

