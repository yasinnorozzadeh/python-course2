import csv
import json

cars = [] 

with open("cars_dataset.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        cars.append(row)
# print(header)
# print(cars)

def show(cars):
    for i in range(len(cars)):
        print("="*100)
        print(cars[i])
# show(cars)

def japan_cars(cars):
    japancars = []
    for i in range(len(cars)):
        if cars[i][8] == "Japan":
            japancars.append(cars[i])
    print(japancars)
    return japancars
# japan_cars(cars)
# show(japancars)

def longe_name(cars):
    c = 0
    for i in range(len(cars)):
        if len(cars[i][0]) > c:
            heighestname = tuple(cars[i])
            c = len(cars[i][0])
    print(heighestname)
    return heighestname
# longe_name(cars)

def small_name(cars):
    c = 10
    for i in range(len(cars)):
        if len(cars[i][0]) < c:
            shortestname = tuple(cars[i])
            c = len(cars[i][0])
    print(shortestname)
    return shortestname
# small_name(cars)

def Cylinders_average(cars):
    c = 0
    for i in range(len(cars)):
        c += int(cars[i][2])
    print(int(c // len(cars)))
    return int(c // len(cars))
# Cylinders_average(cars)
def Horsepower_average(cars):
    c = 0
    for i in range(len(cars)):
        c += float(cars[i][4])
    print(int(c // len(cars)))
    return int(c // len(cars))
# Horsepower_average(cars)
def Light_cars(cars):
    weights = []
    names = []
    for i in range(len(cars)):
        weights.append(float(cars[i][5]))
    weights.sort()
    for i in range(0, 50):
        for j in range(len(cars)):
            if float(cars[j][5]) == weights[i]:
                x = cars[j][0], weights[i]
                names.append(x)
    print(names)
    return(names)
# Light_cars(cars)

data = {"Japan_cars":japan_cars(cars) ,
        "shortest_cars_name":small_name(cars),
        "longest_carS_name":longe_name(cars),
        "cylinders_average":Cylinders_average(cars),
        "horsepower_average":Horsepower_average(cars),
        "light_cars":Light_cars(cars)
        }
with open("cars_dataset.json", "w") as f:
    json.dump(data, f)