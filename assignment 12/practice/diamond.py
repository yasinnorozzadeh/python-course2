length = int(input("ernter length of diamond range(odd numbers): "))

for i in range(length):
    print((length - i) * " ", end='')
    print((i * 2 - 1) * '*')

for i in range(length, 0, -1):
    print((length - i) * " ", end='')
    print((i * 2 - 1) * '*')
