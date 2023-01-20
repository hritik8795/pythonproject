from tkinter import *
import sqlite3
from tkinter import messagebox
t =Tk()
t.geometry("600x600")
s1 =StringVar()
s2 =StringVar()
l1 =Label(text ="enter your name", font =("",15))
l1.place(x=100,y =50)
l2 =Label(text ="enter your password", font =("",15))
l2.place(x =100,y =150)
e1 =Entry(font=("",15),textvariable =s1)
e1.place(x =300 ,y =50)
e1 =Entry(font=("",15),show ="*",textvariable =s2)
e1.place(x =300 ,y =150)
def show():
    db = sqlite3.connect('database.db')
    cr = db.cursor()

    r = cr.execute("select * from login where UNAME ='" + s1.get() + "' AND  UPASS ='" + s2.get() + "'")
    for r1 in r:
        #print("wellcome")
        messagebox.showinfo("title","welcome")
        break
    else:
        #print("invalid username and password")
        messagebox.showinfo("title", "invalid username and password")
    db.commit()
    db.close()


b1=Button(text ="insert data",command =show)
b1.place(x =250,y=200)
t.mainloop()1