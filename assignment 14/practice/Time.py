class Time:
    # constructor
    def __init__(self, hour, minut, second, hour2, minut2, second2, op):
        # Properties
        self.hour_s = hour + hour2
        self.minut_s = minut + minut2
        self.second_s = second + second2
        self.hour_m = hour - hour2
        self.minut_m = minut - minut2
        self.second_m = second - second2
        self.op = op
    # Methods
    def sum(self):
        while not(0 <= self.second_s <= 60 and 0 <= self.minut_s <= 60):
            if self.second_s >= 60:
                self.second_s -= ((self.second_s // 60) * 60)
                self.minut_s += (self.second_s // 60)
            if self.minut_s >= 60:
                self.minut_s -= ((self.minut_s // 60) * 60)
                self.hour_s += (self.minut_s // 60)
        print(str(self.hour_s) + ":" + str(self.minut_s)  + ":" + str(self.second_s))
    def sub(self):
            while not(0 <= self.second_m <= 60 and 0 <= self.minut_m <= 60):
                if self.second_m < 0:
                    self.minut_m -= 1
                    self.second_m += 60
                    if self.minut_m < 0:
                        self.hour_m -= 1
                        self.minut_m += 60
            print(str(self.hour_m) + ":" + str(self.minut_m)  + ":" + str(self.second_m))

t = input("enter time1:for exampel (20:45:30)\n")
t2 = input("enter time2:for exampel (20:45:30)\n")
op = int(input("1_sub\n2_sum\nenter number of your choice: "))
t = t.split(":")
t = [eval(i) for i in t]
t2 = t2.split(":")
t2 = [eval(i) for i in t2]
time = Time(t[0], t[1], t[2], t2[0], t2[1], t2[2], op)
if op == 1:
    time.sub()
elif op == 2:
    time.sum()
else:
    print("youre numner is out of range\ntry again")


    