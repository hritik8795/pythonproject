#fetching the data from database
import sqlite3
db =sqlite3.connect("database.db")
cr=db.cursor()
r=cr.execute("select *from login")
for r1 in r:
    print(r1[0] and r1[1])
db.commit()
db.close()