
number = abs(int(input("enter youre number:\n")))
numbers = []
for i in range(1, number):
    if (number % i) == 0:
        numbers.append(i)

if sum(numbers) == number:
    print("youre number is whole!")
else:
    print("youre number is not whole!")
