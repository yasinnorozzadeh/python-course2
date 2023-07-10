
b = True # b = bool
while b:
    number = int(input("1_Celsius to Kelvin\t2_Celsius to Kelvin\t3_Kelvin to Celsius\n4_Kelvin to Fahrenheit\t5_Fahrenheit to Celsius\t6_Fahrenheit to Kelvin\nEnter number: "))
    if 1 <= number <= 6:
        number1 = float(input("enter youre number:\n"))
        # C + 273.15
        if number == 1:
            result = number1 + 273.15
        # (C × 9/5) + 32 = 32°F
        elif number == 2:
            result = (number1 * 9 / 5) + 32
        # K − 273.15
        elif number == 3:
            result = number1 - 273.15
        # (K − 273.15) × 9/5 + 32
        elif number == 4:
            result = (number - 273.15) * 9 / 5 + 32
        # (F − 32) × 5/9 
        elif number == 5:
            result = (number1 - 32) * 5 / 9
        # (F − 32) × 5/9 + 273.15 
        else:
            result = (number1 - 32) * 5 / 9 + 273.15
        print(result)
    else:
        print("youre number is not find")
    ask = input("do you want to try again:(y, n)\n")
    if ask == "y":
        b = True
    else:
        b = False
print("good bye!")