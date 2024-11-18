# Printing all the tables data
# Author: Andre

import sqlite3

# data base name
db_name = "pfda"
# get the connection
connect = sqlite3.connect(db_name)
# get cursor
cursor = connect.cursor()
# or can be also done this way
con = sqlite3.connect("pfda.db")
cur = con.cursor()

# Queries return a result - fetchone() and fetchall()
result = cursor.execute("SELECT * FROM movie WHERE title = 'Holy Grail'")
print(result.fetchone()) # to assume that there is only one
#print(result.fetchall()) # to assume that there are more than one

# Select * FROM table
sql3 = "SELECT * FROM movie"
result = cursor.execute(sql3)
print(f"first row: {result.fetchone()}")

for row in cur.execute("SELECT * FROM book"):
    print(f"row{row}")