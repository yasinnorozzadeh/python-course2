number = float(input("enter youre number:\n"))
if number < 0:
    print("D")
else:
    if (number // 2) * 2 == number:
        if (number % 10) > 6:
            print("A")
        elif number < 4:
            print("B")
        else:
            print("C")
    else:
        print("C")

        
# or
# number = float(input("enter youre number:\n"))
# if number < 0:
#     print("D")
# else:
#     if (number // 2) * 2 == number:
#         if (number % 10) > 6:
#             print("A")
#         elif (number % 10) < 4:
#             print("B")
#         else:
#             print("C")
#     else:
#         print("C")