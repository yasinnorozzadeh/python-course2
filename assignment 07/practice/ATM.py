password = "1234"
false_password = 1
conter = 0
while password == "1234":
    password_input = input("enter youre password:\n")
    if password_input == password:
        print("log in")
        exit()
    if str(len(password_input)) < str(len(password)):
        print("The number of characters in the password is low")
        password_input = "0000"
    list_password = list(password)
    list_password_input = list(password_input)
    for i in range(4):
        if list_password[i] == list_password_input[(i+1) * -1]:
            conter += 1
    if false_password == 3:
        print("lock!")
        exit()
    elif conter == 4:
        print("call to police")
        exit()
    elif str(len(password_input)) > str(len(password)):
        password == "1234"
    else:
        print("The password is wrong!")
        false_password += 1
