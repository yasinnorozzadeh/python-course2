import sqlite3

connect = sqlite3.connect("mydata.db")

c = connect.cursor()

c.execute("DELETE FROM customers WHERE rowid = 2")

item = c.fetchall()
for i in item:
    print(item)

connect.commit()
connect.close()
