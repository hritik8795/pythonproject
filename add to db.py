from tkinter import *
import sqlite3
root = Tk()
root.geometry("600x600")
a =StringVar()
b =StringVar()
def show():
    db = sqlite3.connect('database.db')
    cr =db.cursor()
    cr.execute("insert into login values('"+a.get()+"','"+b.get()+"')")
    db.commit()
    db.close()
    print("data inserted")
    a.set(" ")
    b.set(" ")
e1 =Entry(textvariable =a)
e1.place(x=50,y =50)
e2 =Entry(textvariable =b)
e2.place(x=50,y=100)
b1 =Button(text ="add",command =show)
b1.place(x=75,y=150)

root.mainloop()