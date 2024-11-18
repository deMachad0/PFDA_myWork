# Dropping a table
# Author: Andre

import sqlite3

connect = sqlite3.connect('pfda')
cursor = connect.cursor()

# or can be also done this way
con = sqlite3.connect("pfda.db")
cur = con.cursor()

# Drop a table
sql2 = "DROP TABLE IF EXISTS book"
result = cursor.execute(sql2)   

sql = "DROP TABLE IF EXISTS movie"
result = cur.execute(sql)


