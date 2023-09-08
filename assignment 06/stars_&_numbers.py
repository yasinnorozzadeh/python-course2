number = int(input("enter your number: "))
c = 2
for x in range(number):
    print(x, "*" * c, end="", sep="")
    c += 2
print(number, end="")