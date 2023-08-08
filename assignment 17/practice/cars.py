import csv
import sqlite3

cars = [] 
with open("cars_dataset.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        cars.append(tuple(row))

connect = sqlite3.connect("carsdata.db")
data = connect.cursor() 
data.execute("""
    CREATE TABLE cars (
            Car TEXT,
            MPG TEXT,
            Cylinders TEXT,
            Displacement TEXT,
            Horsepower TEXT,
            Weight TEXT,
            Acceleration TEXT,
            Model TEXT,
            Origin TEXT
    )
""")
data = connect.cursor() 
for i in range(len(cars)):
    data.execute("INSERT INTO cars VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", cars[i])

def japan_cars():
    data.execute("SELECT * FROM cars WHERE Origin LIKE 'J%'")
    item = data.fetchall()
    for i in item:
        print(i)
def longe_name():
    data.execute("SELECT * FROM cars ORDER BY Car DESC")
    item = data.fetchall()
    print(item[-1])
def small_name():
    data.execute("SELECT * FROM cars ORDER BY Car DESC")
    item = data.fetchall()
    print(item[0])
def Cylinders_average():
    c = 0
    data.execute('SELECT * FROM cars WHERE Cylinders')
    item = data.fetchall()
    for i in range(len(item)):
        c += int(item[i][2])
    print(float(c // len(item)))
def Horsepower_average():
    c = 0
    data.execute('SELECT * FROM cars WHERE Horsepower')
    item = data.fetchall()
    for i in range(len(item)):
        c += float(item[i][4])
    print(float(c // len(item)))
def Light_cars():
    data.execute("SELECT * FROM cars ORDER BY Weight DESC")
    item = data.fetchall()
    for i in range(1, 51):
        print(item[-1*i])

print("Japan_cars:")
japan_cars()
print("shortest_cars_name:")
small_name()
print("longest_cars_name:")
longe_name()
print("cylinders_average:")
Cylinders_average()
print("horsepower_average:")
Horsepower_average()
print("50_light_cars:")
Light_cars()
connect.commit()
connect.close()