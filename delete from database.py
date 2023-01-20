from tkinter import *
import sqlite3
from tkinter import messagebox
t =Tk()
t.geometry("600x600")
s1 =StringVar()
l1 =Label(text ="enter your name", font =("",15))
l1.place(x=100,y =50)
e1 =Entry(font=("",15),textvariable =s1)
e1.place(x =300 ,y =50)
def show():
    db = sqlite3.connect('database.db')
    cr = db.cursor()
    cr.execute("delete  from login where UNAME ='" + s1.get()+"'")
    messagebox.showinfo("title","data delete")
    db.commit()
    db.close()


b1=Button(text ="delete data",command =show)
b1.place(x =250,y=200)
t.mainloop()