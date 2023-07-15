import random

number_for_reapeat = int(input("enter your number to repeat:\n"))
numbers = [] 

for i in range(number_for_reapeat):
    number = random.randint(0, 100)
    if number not in numbers:
        numbers.append(number)
    
print(numbers)
