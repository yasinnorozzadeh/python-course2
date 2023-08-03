import csv

dicts = [
    {"name":"mamd","imbi":"10", "year":"2002"}, 
    {"name":"ekhrajee ha","imbi":"30", "year":"2000"},
    {"name":"bat man","imbi":"80", "year":"1800"}
]
fields = ["name", "imbi", "year"]

with open("test_file.csv", "w") as test_csv_file:
    writer = csv.DictWriter(test_csv_file, fieldnames=fields)
    
    writer.writeheader()
    writer.writerow(dicts)