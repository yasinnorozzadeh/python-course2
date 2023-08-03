import csv
feilds = ["name", "year", "gener", "country"]
madias = [
    ["spider man", "2022", "90", "action", "america"],
    ["star war", "1979", 99, "sci-fi", "america"]
]

with open("films.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writer(feilds)
    writer.writer(madias)
