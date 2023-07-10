import math
condition = "t"
result = 0
while condition == "t":
    op = int(input("1_sum\t2_subtraction\t3_multiplication\t4_Division\n5_power\t6_log\t7_sin\t8_cos\t9_tan\t10_cot\n11_factorial\t12_radical\t13_abs\t14_round\nenter number of operation: "))
    if 1 <= op <= 14:
        if 1 <= op <= 5:
            number_1 = float(input("enter youre first number:\n"))
            number_2 = float(input("enter youre second number:\n"))
            if op == 1:
                result = number_1 + number_2
            elif op == 2:
                result = number_1 - number_2
            elif op == 3:
                result = number_1 * number_2
            elif op == 4:
                if number_2 == 0:
                    result = None
                else:
                    result = number_1 / number_2
            else:
                result = math.pow(number_1, number_2)
        else:
            number_1 = float(input("enter youre number:\n"))
            if op == 6:
                result = math.log(number_1)
            elif op == 7:
                result = math.sin(math.radians(number_1))
            elif op == 8:
                result = math.cos(math.radians(number_1))
            elif op == 9:
                result = math.tan(math.radians(number_1))
            elif op == 10:
                result = math.cos(math.radians(number_1) / math.sin(math.radians(number_1)))
            elif op == 11:
                result =  math.factorial(number_1)
            elif op == 12:
                result = math.sqrt(number_1)
            elif op == 13:
                result = abs(number_1)
            else:   
                result = round(number_1)
    else:
        print("try again")

    if result == None:
        print("Can not divide by zero(0)")
    else:
        print(result)
    ask = input("do you want to try again?(y, n)\n")
    if ask == "y":
        condition = "t"
    else:
        condition = "f"
print("good bye!")