# Inserting data into our tables
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


# UPDATES - INSERT INTO book VALUES();
sql2 = """ 
    INSERT INTO book VALUES
    ('Harry Pothead', 'Just kidding', '112344'),
    ('Harry Potter does something', 'JK Rowling', '123444')
"""
# This can lead to SQL injection 
cur.execute(sql2)
con.commit() # Remember to commit your updates

# Also can be done avoiding sql injection, by using placeholders
data = [
    ('Monty Pythons life of Brian', 1978, 8.0),
    ('Holy Grail', 1977, 9.2)
]
cursor.executemany('INSERT INTO movie VALUES(?,?,?)', data)
connect.commit()

