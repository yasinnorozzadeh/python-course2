def sum_2list(first_list, second_list):
    if  len(first_list) != len(second_list):
        return "not equal length"

    final_list = []
    for i in range(len(first_list)):
        answer = first_list[i] + second_list[i]
        final_list.append(answer)

    return final_list



l1 = [1, 2, 3 ,4, 5]
l2 = [2, 2, 2, 2, 2]

answer = sum_2list(l1, l2)
print(answer)