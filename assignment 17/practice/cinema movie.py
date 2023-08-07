import sqlite3
import pyfiglet
from termcolor import colored
connect = sqlite3.connect("mydata.db")
data = connect.cursor()
# data.execute("""
#     CREATE TABLE media (
#             filmname TEXT,
#             imdb TEXT
#     )
# """)
def add():
    name = input("enter name of movie: ")
    imdb = input("entre movie imdb: ")
    data.execute("INSERT INTO media VALUES (?, ?)",(name, imdb))
    connect.commit()
def show_list():
    data.execute("SELECT * FROM media")
    item = data.fetchall()
    for i in item:
        print(item)

def show_imdb():
    data.execute("SELECT * FROM media ORDER BY imdb DESC")
    item = data.fetchall()
    for i in range(5):
        try:
            print(item[i])
        except:
            pass
print(colored(pyfiglet.figlet_format(('Welcome to movies store'), font = "digital"), "green"))
while True:
    op = int(input("1_add movie\n2_show sort of movies list\n3_show heighest imdb\n4_exit\nenter number of operation: "))
    if op == 1:
        add()
    elif op == 2:
        show_list()
    elif op == 3:
        show_imdb()
    elif op == 4:
        connect.commit()
        break
    else:
        print("your number is out of range(1 to 4)")
    try_again = input("do you want to try?(y, n): ")
    if not(try_again ==  "y"):
        break
print(colored(pyfiglet.figlet_format(('Good Bye'), font = "digital"), "red"))
connect.close()