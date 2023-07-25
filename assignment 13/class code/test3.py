f = open("scores.txt", "w")

scores = [100, 120, 90, 126, 124, 90, 114, 115, 80]

for score in scores:
    myscore = str(score)
    myscore += "\n"

    f.writelines(myscore)

f.close()