# Addition and subtraction of numbers
number_1 = float(input("enter number 1:\n"))
number_2 = float(input("enter number 2:\n"))
operation = input("enter youre operration:(sum => + , minus => -)\n")
if operation == "+":
    sum = number_1 + number_2
    print(sum)
elif operation == "-":
    minus = number_1 - number_2
    print(minus)
else:
    print("Your operation is not defined")
