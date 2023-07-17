numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
new_name = []
while True:
    error = 0
    name_input = input("enter file name:\n")
    if "." in name_input:
        new_name = name_input.split(".", 1)
        if "." in new_name[1]:
            error += 1
            print("error\nyou have 2 '.' in file name")
        elif new_name[1] == "err":
            error += 1
            print("error\nyour extension should not be 'err'")
        elif not(len(new_name[1]) == 3 or len(new_name[1]) == 2):
            error += 1
            print("error\nyour extension should not be more or less than 2-3 letters")
        for number in numbers:
            if number in new_name[1]:
                print("error\nyour extension should not contain numbers") 
    for number in range(len(numbers)):
        if name_input.startswith(numbers[number]):
            error += 1
            print("error\nyour filename must not start with a number")
    if error == 0:
        print("your file name is True!")
    try_again = input("do you want to try again?(y, n)")
    if try_again != "y":
        break