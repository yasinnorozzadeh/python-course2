# input : 3
# output : 01'2''3'''

n = int(input('n: '))
c = 0

# if n >= 0:
while c <= n:
    # print(c,end = "")
    # print("'"*c, end = "")
    print(c, "'"*c, end='', sep='')
    c += 1