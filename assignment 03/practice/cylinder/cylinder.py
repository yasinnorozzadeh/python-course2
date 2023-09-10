r = float(input("please enter Radius:\n"))
h = float(input("please enter Height:\n"))
#cylinder volume
Volume = 3.14 * h * (r **2)
#Lateral area of the cylinde
s_a = 2 * 3.14 * (r ** 2) + 2 * 3.14 * r * h
# The total area of the cylinder 
s = 2 * 3.14 * r * h
print("cylinder volume is:", Volume)
print("Lateral area of the cylinder is: ", s_a)
print("The total area of the cylinder is", s)
