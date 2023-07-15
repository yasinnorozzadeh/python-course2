fruits = {"apple", "banana", "cherry", "mango", "pineapple", "papayo"}
fruits2 = set()
change = input("do you want to check fruits set?(y, n): ")
if change == "y":
    repeat = int(input("how much do you want to check ??\nenter your number: "))
else:
    repeat = 0
for i in range(repeat):
    print(fruits)
    method = int(input("1_add item\n2_remove item\n3_clear set\n4_copy set\n5_update set\nenter your choice number: "))
    if method == 1:
        fruit = input("enter fruit's name: ")
        result = fruits.add(fruit)
    elif method == 2:
        remove_fruit = input("enter fruit's name: ")
        result =  fruits.discard(remove_fruit)
    elif method == 3:
        result = fruits.clear()
    elif method == 4:
        result = fruits.copy()
    elif method == 5:
        repeat = int(input("eneter lenth of new fruits set: "))
        for i in range(repeat):
            fruit = input("enter fruit name: ")
            fruits2.add(fruit)
        result = fruits.update(fruits2)
    else:
        print("your number is not find")
    print(result)

