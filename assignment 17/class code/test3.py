import sqlite3

connect = sqlite3.connect("mydata.db")

c = connect.cursor()

# c.execute("SELECT * FROM customers")
c.execute("SELECT fistname FROM customers")


# c.fetchone()
# c.fetchmany(2)
item = c.fetchall()

for i in item:
    print(item)

connect.commit()
connect.close()