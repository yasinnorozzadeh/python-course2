number = int(input("enter youre number:\n"))
outside_the_number_field = number // 7
if number % 7 == 0:
    print(f"{number} is madarib 7")
else:
    print(f"{number} is not madarib 7 ")
    outside_the_number_field += 1
    outside_the_number_field *= 7
    print(f"The closest multiple of 7 is close to {outside_the_number_field}")
