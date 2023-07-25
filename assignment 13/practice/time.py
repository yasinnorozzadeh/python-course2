op = int(input("enter number of your operation:(1_sub, 2_sum):\n"))
hour = int(input("enter hours: "))
minut = int(input("enter minuts: "))
second = int(input("enter seconds: "))
time1_dict = {"hour":hour,
            "minut":minut,
            "second":second}
hour2 = int(input("enter hours: "))
minut2 = int(input("enter minuts: "))
second2 = int(input("enter seconds: "))
time2_dict = {"hour":hour2,
            "minut":minut2,
            "second":second2}
if op == 1:
    h = time1_dict["hour"] - time2_dict["hour"]
    m = time1_dict["minut"] - time2_dict["minut"]
    s = time1_dict["second"] - time2_dict["second"]
    while not(0 <= s <= 60 and 0 <= m <= 60):
        if s < 0:
            m -= 1
            s += 60
            if m < 0:
                h -= 1
                m += 60
    print(str(h) + ":" + str(m)  + ":" + str(s))

elif op == 2:
    seconds = time1_dict["second"] + time2_dict["second"]
    mins = time1_dict["minut"] + time2_dict["minut"]
    hours = time1_dict["hour"] + time2_dict["hour"]
    while not(0 <= seconds <= 60 and 0 <= mins <= 60):
        if seconds > 60:
            m_s = (seconds % 60)
            seconds -= (m_s * 60)
            mins += m_s
            # if mins >= 60:
            #     mins -= ((mins % 60) * 60)
            #     hours += (mins % 60)
    print(str(hours) + ":" + str(mins)  + ":" + str(seconds))
else:
    print("your number is out of range\ntry again")