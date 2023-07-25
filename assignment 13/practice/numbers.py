a_1 = float(input("enter a : "))
b_1 = float(input("enter b : "))
a_2 = float(input("enter a : "))
b_2 = float(input("enetr b : "))
dict_num = {"a1": a_1,
            "b1": b_1,
            "a2": a_2,
            "b2": b_2}  
sum_num = str(dict_num["a1"] + dict_num["a2"]) +","+ str((dict_num["b1"] + dict_num["b2"])) + "i"
sub_num = str(dict_num["a1"] - dict_num["a2"]) +","+ str((dict_num["b1"] - dict_num["b2"])) + "i"
print("sum:", sum_num)
print("sub:", sub_num)
