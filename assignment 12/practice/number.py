def num(number):
    numbers_list = []
    for i in range (1, 4):
        numbers_list.append(str(number * i))
    number = " ".join(numbers_list)
    number = number.replace(" ", "")
    return number

number = int(input("enter youre number: "))
print(num(number))