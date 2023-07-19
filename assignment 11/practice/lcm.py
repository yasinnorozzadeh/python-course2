# Lowest common multiple
def lcm(num1, num2):
    x = []
    y = []
    lcm = 0
    result = []
    if num2 > num1:
        print(num1, ",", num2)
        for i in range(1, num2+1):
            y.append(num1 * i)
            x.append(num2 * i)
    elif num1 > num2:
        print(num2, ",", num1)
        for i in range(1, num1+1):
            x.append(num2 * i) 
            y.append(num1 * i)
    else:
        lcm = num1
    for j in y:
        for i in x:
            if j == i:
                result.append(i)
    lcm = result[0]
    return lcm

num1 = int(input("enter number1: "))
num2 = int(input("enter number2: "))
print("lcm:", lcm(num1, num2))