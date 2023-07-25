f = open("names.txt", "r")
# print(f.read())
d = {}
data = f.readlines()
for each_data in data:
    mydata = each_data.rstrip()
    name, title = mydata.split(" - ")
    d[name] = title

print(d)
