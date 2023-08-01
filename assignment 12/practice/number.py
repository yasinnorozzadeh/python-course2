# def num(number):
#     numbers_list = []
#     s = 0
#     for i in range (1, 4):
#         for j in str(number * i):
#             s += int(j)
#         numbers_list.append(str(s))
#         s = 0
#     number = " ".join(numbers_list)
#     number = number.replace(" ", "")
#     return number

# number = int(input("enter youre number: "))
# print(num(number))



# def number(num):
#     n1 = num
#     n2 = (num*10)+num
#     n3 = (num*100)+(num*10)+num
#     return n1 + n2 + n3
# number_user = int(input("enter youre number: "))
# print(number(number_user))



def number(num):
    num = str(num)
    n1 = num
    n2 = num+num
    n3 = num+num+num
    return int(n1) + int(n2) + int(n3)
number_user = int(input("enter youre number: "))
print(number(number_user))
