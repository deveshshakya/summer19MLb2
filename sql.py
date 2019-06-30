#!/usr/bin/python3

import mysql.connector as mysql

u = 'root'
p = ''
db = 'adhoc'
h = ''

# connecting
conn = mysql.connect(user=u, password=p, database=db, host=h)

# generating cursor
cur = conn.cursor()

# now we can write sql query
out = cur.execute("show tables;")

print(out)

# closing connection
conn.close()
