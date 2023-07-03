username = "admin"
password = 1234
user_name_input = input("enter username:\n")
password_input = int(input("enter password:\n"))

if user_name_input == username and password_input == password:
    print("log in")
else:
    print("youre username or password is not defined")
