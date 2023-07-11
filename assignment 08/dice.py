import random
number1 = 0
list_numbers = []
count_rounds = 0
while not(number1 == 6):
    list_numbers.append(number1)
    number1 = random.randint(1, 6)
    count_rounds += 1
    if number1 == 6:
        print(f"round {count_rounds}| you win!")
    else:
        print(f"round {count_rounds} is:", number1)
print("total numbers of previous rounds =", sum(list_numbers))
print("sum of whole numbers =", sum(list_numbers) + 6)