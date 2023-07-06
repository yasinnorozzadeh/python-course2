numbers_list = []
number1 = float(input("enter youre number:\t"))
numbers_list.append(number1)
number2 = float(input("enter youre number:\t"))
numbers_list.append(number2)
number3 = float(input("enter youre number:\t"))
numbers_list.append(number3)
number4 = float(input("enter youre number:\t"))
numbers_list.append(number4)
number5 = float(input("enter youre number:\t"))
numbers_list.append(number5)

print(sorted(numbers_list))
print(sorted(numbers_list, reverse=True))