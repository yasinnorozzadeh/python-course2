weight = float(input("enter youre weight(to KG):\n"))
height = float(input("enter youre height(to M):\n"))
BMI = weight / (height ** 2)
print("youre BMI :", BMI)
if BMI < 18.5:
    print("under weight")
elif 18.5 <= BMI < 25:
    print("normal")
elif 25 <= BMI < 30:
    print("over weight")
elif 30 <= BMI < 35:
    print("obese")
else:
    print("extremly obese")