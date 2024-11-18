# Messing with SQL in Python
# Author: Andre

import sqlite3

# data base name
db_name = "pfda"
# get the connection
connect = sqlite3.connect(db_name)
# get cursor
cursor = connect.cursor()
# execute
sql="create table movie(title, year, score)"
cursor.execute(sql)

# or can be also done this way
con = sqlite3.connect("pfda.db")
cur = con.cursor()
cur.execute("CREATE TABLE book(title, author, ISB)")
con.close()
