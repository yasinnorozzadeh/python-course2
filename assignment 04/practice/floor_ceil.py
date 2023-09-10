import math
from unittest import result
number = float(input("enter youre number:\n"))
# Round numbers down to the nearest integer
result = math.floor(number)
print("math_floor:", result)
# Round a number upward to its nearest integer
result = math.ceil(number)
print("math_ceil:",result)
