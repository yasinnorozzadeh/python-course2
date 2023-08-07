import sqlite3

connect = sqlite3.connect("mydata.db")

c = connect.cursor()

many_customers = [
    ("yasin", "norozzadeh", "norozzadehyasin@gmail.com"),
    ("ali", "yaghubian", "ayaghoubian2000@gmail.com"),
    ("yasin", "norozzadeh", "norozzadehyasin@gmail.com")
]

c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customers)

connect.commit()
connect.close()