nameslist = ["ali", "atefe", "reza", "homa", "amir", "fateme"]
print(nameslist)
nameslist.insert(int(input("repeat your number:\n"))-1 if int(input("enter your number:\n")) <= 6 else int(input("enter another number(range 1 to 6):\n"))-1 , input("enter youre name:\n"))
print(nameslist) # update names list
nameslist.insert(int(input("repeat your number:\n"))-1 if int(input("enter your number:\n")) <= 7 else int(input("enter another number(range 1 to 7):\n"))-1 , input("enter youre name:\n")) # insert(index name, name)
print(nameslist) # update names list
nameslist.insert(int(input("repeat your number:\n"))-1 if int(input("enter your number:\n")) <= 8 else int(input("enter another number(range 1 to 8):\n"))-1 , input("enter youre name:\n"))
print(nameslist)
