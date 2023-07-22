row = int(input("enter row: "))
col = int(input("enter col: "))

for i in range(1, col+1):
    for j in range(1, row+1):
        print(j * i, end = "\t")

    print()