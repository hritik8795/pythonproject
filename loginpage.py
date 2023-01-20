import sqlite3
db =sqlite3.connect('database.db')
cr =db.cursor()

x=input("enter your name")
y =input("enter your password")

r =cr.execute("select * from login where UNAME ='"+x+"' AND  UPASS ='"+y+"'")
for r1 in r:
    print("welcome")
    break
else:
    print("invalid username and password")
db.commit()
db.close()