number = int(input("enter youre number:\n"))
number = str(abs(number))
choose_odd = "13579"
choose_even = "02468"
odd = 0
even = 0

odd += number.count(choose_odd[0])
odd += number.count(choose_odd[1])
odd += number.count(choose_odd[2])
odd += number.count(choose_odd[3])
odd += number.count(choose_odd[4])
even += number.count(choose_even[0])
even += number.count(choose_even[1])
even += number.count(choose_even[2])
even += number.count(choose_even[3])
even += number.count(choose_even[4])

if odd > even:
    print("odd")
elif even > odd:
    print("even")
else:
    print("equal")
print("odd:", odd,"even:", even)




##or

# number = int(input("enter youre number:\n"))
# number = str(abs(number))
# choose_odd = "13579"
# choose_even = "02468"
# if choose_odd[0] in number:
#     number.replace(choose_odd[0], "0")
# elif choose_odd[1] in number:
#     number.replace(choose_odd[1], "0")
# elif choose_odd[2] in number:
#     number.replace(choose_odd[2], "0")
# elif choose_odd[3] in number:
#     number.replace(choose_odd[3], "0")
# elif choose_odd[4] in number:
#     number.replace(choose_odd[4], "0")
# if choose_even[0] in number:
#     number.replace(choose_even[0], "1")
# elif choose_even[1] in number:
#     number.replace(choose_even[0], "1")
# elif choose_even[2] in number:
#     number.replace(choose_even[0], "1")
# elif choose_even[3] in number:
#     number.replace(choose_even[0], "1")
# elif choose_even[4] in number:
#     number.replace(choose_even[0], "1")
# odd = number.count("0")
# even = number.count("1")

# if odd > even:
#     print("odd")
# elif even > odd:
#     print("even")
# else:
#     print("equal")
# print(odd, even)
