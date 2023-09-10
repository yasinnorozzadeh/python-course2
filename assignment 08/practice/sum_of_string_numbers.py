string = input("enter a sentence:\n")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
other_characters = []
sum_numbers = 0
for i in numbers:
    for idx in string:
        if str(i) == idx:
            sum_numbers += i
        else:
            other_characters.append(idx)
print(sum_numbers)
