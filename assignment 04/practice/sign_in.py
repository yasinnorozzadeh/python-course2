username = "admin"
password = 1234
username2 = "admin2"
password2 = 2314
user_name_input = input("enter username:\n")
password_input = int(input("enter password:\n"))

if user_name_input == username and password_input == password or user_name_input == username2 and password_input == password2 :
    print("log in")
elif user_name_input == username or password_input == password and user_name_input == username2 or password_input == password2:
    print("youre username or password is not defined")
    user_name_input = input("enter username:\n")
    password_input = int(input("enter password:\n"))
    if user_name_input == username and password_input == password or user_name_input == username2 and password_input == password2 :
        print("log in")
    else:
        print("youre username or password is not defined")
else:
    print("youre username or password is not defined")
