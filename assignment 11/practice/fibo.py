def fib(n):
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        print(0, 1, end=" ")
        a = 0
        b = 1
        for i in range(2, n):
            s = a + b
            print(s, end=" ")
            a = b
            b = s
number = int(input("enter your number: "))
fib(number)