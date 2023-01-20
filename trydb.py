from tkinter import *
import sqlite3
db =sqlite3.connect('database.db')

t =Tk()
t.geometry("400x400")
a =StringVar()
b=StringVar()
def show():
    db =sqlite3.connect('database.db')
    cr=db.cursor()
    db.commit()
    db.close()
    print("database added")
    a.set(" ")
    b.set(" ")

e1=Entry(font=("",15),textvariable =a)
e1.pack()
e2 =Entry(font =("",15),textvariable =b)
e2.pack()
b1 =Button(text ="insert",command =show)
b1.pack()
t.mainloop()