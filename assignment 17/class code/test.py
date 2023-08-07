# MySQL
# SQlite
# Grafana
import sqlite3
# connect
connect = sqlite3.connect("mydata.db")
# cursor
c = connect.cursor()
# execute
c.execute("""
    CREATE TABLE customers (
          firstname TEXT, 
          lastname TEXT,
          email TEXT
    )
""")
# commit
connect.commit()
# close
connect.close()