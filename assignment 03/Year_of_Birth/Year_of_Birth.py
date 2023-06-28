year_num = int(input("please select the year type number:\n1_solar\n2_Lunar\n"))
year = int(input("pelase enter youre bith year:\n"))
if year_num == 1:
    year = 1402 - year
    print(year)
elif year_num == 2:
    year = 1444 - year
    print(year)
else:
    print("the input number is not defined")
