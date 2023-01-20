from tkinter import *
import sqlite3
t=Tk()
t.geometry("300x600")
db=sqlite3.connect("database.db")
cr=db.cursor()
r=cr.execute("select * from login")
x=50
y=50
for r1 in r:
    Label(text=r1[0]).place(x=x,y=y)
    x +=100
    Label(text=r1[1]).place(x=x,y=y)
    x=50
    y+=50
db.commit()
db.close()
t.mainloop()