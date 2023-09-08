# list1
l1 = ["py", "i", " ", "popul", "lang"]
print("list1 :", l1)
# list2
l2 = ["thon", "s", "a", "are", "uage."]
print("list2 :", l2)
# result list
l_result = [x+l2[y] for y, x in enumerate(l1)]
print("result list:", l_result)
