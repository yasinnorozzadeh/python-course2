number1 = int(input("enter first number: "))
number2 = int(input("enter second number: "))
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
print(gcd(number1, number2))