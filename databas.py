import sqlite3
db =sqlite3.connect('database.db')
cr =db.cursor()
#cr.execute("create table login(UNAME text,UPASS text)")
x=input("enter the name")
y =input("enter the password")
#cr.execute("insert into login(UNAME,UPASS) VALUES('bbb','125')")
#cr.execute("insert into login(UNAME,UPASS) VALUES('x','y')") ---agar aise likhenge to x y hi print karenga
cr.execute("insert into login(UNAME,UPASS) VALUES('"+x+"','"+y+"')")
db.commit()
db.close()
print("databaseis created")

