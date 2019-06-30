#!/usr/bin/python3

import mysql.connector as mysql

u = 'root'
p = 'fuckyeah'
db = 'adhoc'
h = 'mysqldbserver.cacuhx7adcgb.ap-south-1.rds.amazonaws.com'

# connecting
conn = mysql.connect(user=u, password=p, database=db, host=h)

# generating cursor
cur = conn.cursor()

# now we can write sql query
out = cur.execute("show tables;")

print(out)

# closing connection
conn.close()
