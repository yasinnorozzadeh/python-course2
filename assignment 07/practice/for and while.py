numbers = list()
update_numbers = []
counter = 0
for i in range(10):
    number = int(input("enter youre number:\n"))
    numbers.append(number)

while counter < len(numbers):
    update_number = numbers[counter] + 2
    counter += 1
    update_numbers.append(update_number)

print(numbers)
print(update_numbers)
