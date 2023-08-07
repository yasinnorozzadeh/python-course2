import sqlite3

connect = sqlite3.connect("mydata.db")

c = connect.cursor()

# c.execute("SELECT * FROM customers")
c.execute("SELECT * FROM customers ORDER BY DECD")

item = c.fetchall()

for i in item:
    print(item)

connect.commit()
connect.close()