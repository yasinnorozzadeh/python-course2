names = ["ali", "nima", "sina", "taha", "navid", "mahdi"]
scores = [20, 19.25, 18.5, 19.75, 18, 20]
students = {}
i = 0
for name in names:
    students[str(name)] = scores[i]
    i += 1

print(students)