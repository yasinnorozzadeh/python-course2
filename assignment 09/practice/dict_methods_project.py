info_dict = {"name":"yasin", "family":"norozzadeh", "years old":"15", "city":"Mashhad"}
print(info_dict)
change = input("do you want to check yasin's information?(y, n): ")
if change == "y":
    repeat = int(input("how much do you want to check yasin's information??\nenter your number: "))
else:
    repeat = 0
for i in range(repeat):
    method = int(input("1_copy info\n2_add info\n3_clear info\n4_info Item\n5_show info keys\n6_show info values\n enter choice number: "))
    if 1 <= method <= 6:
        if method == 1:
            result = info_dict.copy()
        elif method == 2:
            key = input("enter item key name: ")
            value = input("enter item value: ")
            result = info_dict.update({key:value})
        elif method == 3:
            result = info_dict.clear()
        elif method == 4:
            result = info_dict.items()
        elif method == 5:
            result = info_dict.keys()
        else:
            result = info_dict.values()
        print(result)
    else:
        print("your number is not find")