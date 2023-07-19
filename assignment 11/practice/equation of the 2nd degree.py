import math
def e_2nd_d(a, b, c):

    # calculate the discriminant
    d = (b**2) - (4*a*c)
    # find two solutions
    sol1 = (-b-math.sqrt(d))/(2*a)
    sol2 = (-b+math.sqrt(d))/(2*a)
    return sol1, sol2
a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))
print(e_2nd_d(a, b, c))