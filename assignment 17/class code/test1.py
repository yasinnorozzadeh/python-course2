import sqlite3

connect = sqlite3.connect("data.db")

c = connect.cursor()

c.execute("INSERT INTO customers VALUES ('yasin' , 'Norozzadeh' , 'Norozzadehyasin@gmail.com')")

connect.commit()
connect.close()