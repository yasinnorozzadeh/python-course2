def f(x, y): 
    return x + 2 *  y

f = lambda x, y: x + 2 *  y
even = lambda x : x % 2 == 0
l = [2, 7, 8, 19, -3, 45, -2, 5]
f = filter(even, l)
print(list(f))
f = map(even, l)
print(list(f))
