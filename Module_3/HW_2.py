import random


def get_numbers_ticket(min_number, max_number, quantity):
    empty_list = []
    if min_number >= 1 and max_number <= 1000 and (max_number - min_number) > quantity:
        return sorted(random.sample(range(min_number, max_number + 1), quantity))
    else:
        return empty_list


lottery_numbers = get_numbers_ticket(10, 15, 3)
print("Ваші лотерейні числа:", lottery_numbers)