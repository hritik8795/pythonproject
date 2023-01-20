from tkinter import *
from tkinter import ttk
t =Tk()
t.geometry("425x350")
n =ttk.Notebook()
n.place(x=0,y=0,width=425,height =350)
f1 =Frame(bg ="cyan")
n.add(f1,text="Insert")
b1 =Button(f1,text="insert page")
b1.place(x =100,y =100)
f2 =Frame(bg ="blue")
n.add(f2,text="search")
b2 =Button(f2,text="search page")
b2.place(x =110,y =150)
f3 =Frame(bg ="black")
n.add(f3,text="view_all")
b3 =Button(f3,text="view page")
b3.place(x =100,y =100)


t.mainloop()