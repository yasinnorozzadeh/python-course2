def number(numerator, denumerator):
    d = {"num": numerator, "dnum": denumerator}
    return d

class Deduction:
    def __init__(self, dict1 , dict2):
        # Properties
        self.d1 = dict1
        self.d2 = dict2
    # Methods
    def mul(self):
        result_num = self.d1["num"] * self.d2["num"]
        result_dnum = self.d1['dnum'] * self.d2['dnum']
        return result_num , result_dnum
    def sub(self):
        result_num = (self.d1["num"] * self.d2['dnum']) - (self.d2["num"] * self.d1['dnum'])
        result_dnum = self.d1['dnum'] * self.d2['dnum']
        return result_num , result_dnum
    def sum(self):
        result_num = (self.d1["num"] * self.d2['dnum']) + (self.d2["num"] * self.d1['dnum'])
        result_dnum = self.d1['dnum'] * self.d2['dnum']
        return result_num , result_dnum
    def div(self):
        if not(self.d2['dnum'] == 0 or self.d2["num"] == 0):
            result_num = self.d1["num"] * self.d2['dnum']
            result_dnum = self.d1['dnum'] * self.d2["num"]
            return result_num , result_dnum
        else:
            return "Your second fraction is undefined because it has a zero denominator"
op = int(input("1_sum\n2_sub\n3_mul\n4_div\nenter number of operation: "))
dct1 = {}
dct2 = {}
for i in range (1, 3):
    num = int(input(f"enter numerator{i}: "))
    denum = int(input(f"enter denumerator{i}: "))
    if i == 1:
        dct1  = number(num, denum)
    else:
        dct2 = number(num, denum)

d = Deduction(dct1, dct2)
if op == 1:
    a , b = d.sum()
    print(a, "\n-----\n", b)
elif op == 2:
    a , b = d.sub()
    print(a, "\n-----\n", b)
elif op == 3:
    a , b = d.mul()
    print(a, "\n-----\n", b)
elif op == 4:
    try:
        a , b = d.div()
        print(a, "\n-----\n", b)
    except:
        print(d.div(dct1, dct2))