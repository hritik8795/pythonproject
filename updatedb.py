import sqlite3
db = sqlite3.connect('database.db')
cr = db.cursor()
s1 =input("enter your uname =")
s2 =input("enter your pass =")
#cr.execute("update login set UPASS ='8795788447' where UNAME='hritik'")
cr.execute("update login set UPASS ='"+s2+"' where UNAME='"+s1+"'")
db.commit()
db.close()