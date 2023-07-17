number_list = [21, 11, -2, -54, 54, -1, -1, 2, 3]
numbers_dict = {}

for number in number_list:
    if not(number in number_list):
        numbers_dict[number] += 1
    else:
        numbers_dict[number] = 1
        # numbers_dict[number] = numbers_dict[number] + 1

print(numbers_dict)