import random

first_number = random.randint(0, 100)
second_number = random.randint(0, 100)

def sum(first_number, second_number):
    if second_number == 0:
        return first_number
    elif first_number == 0:
        return second_number
    else:
        return sum(first_number+1, second_number-1)

print(f"Sum of numbers {first_number} and {second_number} is : {sum(first_number, second_number)}")