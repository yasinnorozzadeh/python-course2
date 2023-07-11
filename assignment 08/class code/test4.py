numbers = []
# s = 0
while True:
    num = float(input("num : "))
    if num == -1:
        break
    else:
        numbers.append(num)
        # s = s + num
print("avg:", sum(numbers)/len(numbers))