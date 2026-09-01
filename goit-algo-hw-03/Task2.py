import random

def get_numbers_ticket(min, max, quantity):
    if min >= 1 and min < max and max <= 1000 and quantity >= 1:
        find_random_number = random.sample(range(min, max), quantity)
        find_random_number.sort()
        print(find_random_number)
        return find_random_number
    elif min < 0 or max < 0:
        print("min or max cannot be negative ")
        return []
    elif min == 0 or max == 0: 
        print("min or max cannot be 0")
        return []     
    
    
get_numbers_ticket(-5, 1000, 5)