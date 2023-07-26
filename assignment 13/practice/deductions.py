  op = int(input("1_sum\n2_sub\n3_mul\n4_div\nenter number of operation: "))
def number(numerator, denumerator):
    d = {"num": numerator, "dnum": denumerator}
    return d

def mul(d1, d2):
    result_num = d1["num"] * d2["num"]
    result_dnum = d1['dnum'] * d2['dnum']
    return result_num , result_dnum
def sub(d1, d2):
    result_num = (d1["num"] * d2['dnum']) - (d2["num"] * d1['dnum'])
    result_dnum = d1['dnum'] * d2['dnum']
    return result_num , result_dnum
def sum(d1, d2):
    print(d1 , "\n" , d2)
    result_num = (d1["num"] * d2['dnum']) + (d2["num"] * d1['dnum'])
    result_dnum = d1['dnum'] * d2['dnum']
    return result_num , result_dnum
def div(d1, d2):
    if not(d2['dnum'] == 0 or d2["num"] == 0):
        result_num = d1["num"] * d2['dnum']
        result_dnum = d1['dnum'] * d2["num"]
        return result_num , result_dnum
    else:
        return "Your second fraction is undefined because it has a zero denominator"
dct1 = {}
dct2 = {}
for i in range (1, 3):
    num = int(input(f"enter numerator{i}: "))
    denum = int(input(f"enter denumerator{i}: "))
    if i == 1:
        dct1  = number(num, denum)
    else:
        dct2 = number(num, denum)

if op == 1:
    a , b = sum(dct1, dct2)
    print(a, "\n-----\n", b)
elif op == 2:
    a , b = sub(dct1, dct2)
    print(a, "\n-----\n", b)
elif op == 3:
    a , b = mul(dct1, dct2)
    print(a, "\n-----\n", b)
elif op == 4:
    try:
        a , b = div(dct1, dct2)
        print(a, "\n-----\n", b)
    except:
        print(div(dct1, dct2))
