def num(number):
    numbers_list = []
    s = 0
    for i in range (1, 4):
        for j in str(number * i):
            s += int(j)
        numbers_list.append(str(s))
        s = 0
    number = " ".join(numbers_list)
    number = number.replace(" ", "")
    return number

number = int(input("enter youre number: "))
print(num(number))
