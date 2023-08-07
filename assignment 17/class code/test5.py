import sqlite3

connect = sqlite3.connect("mydata.db")

c = connect.cursor()

c.execute("""
    UPDATE customers SET firstname = "ali"
    WHERE firstname = "Gholi" 
""")

connect.commit()
connect.close()