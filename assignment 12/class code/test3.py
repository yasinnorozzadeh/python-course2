def f(num):
    return num + 2

l = [1, 2, 3, 4, 5]
new_l = list(map(f, l))
print(new_l)