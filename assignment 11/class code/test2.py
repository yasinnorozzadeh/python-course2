
def Myscore(s):
    father_name = input("enter father name = ")
    name = input("enter your name")
    if father_name == "Mohsen":
        s += 2
    if name == "Atefeh":
        s = 20 
    elif name == "Ashvan":
        s -= 1

    return s



raw_score = float(input("raw score: "))
better_score = Myscore(raw_score)

if better_score > 20:
    better_score = 20
elif better_score < 0:
    better_score = 0

print(better_score)