from tkinter import *
import sqlite3
db=sqlite3.connect()
root = Tk()
root.title("ADDMISSION DATA SOFTWARE")
root.geometry("1280x720")
root.resizable(0, 0)
root.configure(background="cyan")
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////---------
''''def btech():
    f2 =Frame()
    f2.place(x=0,y=1280,width =1280,height =720)
    b12 =Button(f2,text="enter")
    b12.place(x=0,y=0)'''
def btech():
    f2 = Frame(bg="blue")
    f2.place(x=0, y=0, width=1280, height=720)
    e1 =Entry(f2)
    e1.pack()
    e2=Entry(f2)
    e2.pack()
    b1 =Button(f2,text ="back",command =home)
    b1.pack()

# button for frame 1
def home():
    f1 =Frame(bg ="cyan")
    f1.place(x =0,y=0,width =1280,height =720)
    l1 = Label(f1,text="Wellcome In Our College For Addmission Software ", font=("", 30))
    l1.place(x=400, y=50)
    l2 = Label(f1, text=" We are work for giving best and attractive future for your children:.", font=("", 25))
    l2.place(x=200, y=650)
    l3 = Label(f1, text="courses which we are providing:::>", font=("", 25))
    l3.place(x=200, y=250)

    b1 = Button(f1,text="B.TECH", font=("", 25),command=btech)
    b1.place(x=750, y=240)
    b2 = Button(f1, text="M.TECH", font=("", 25), command=btech)
    b2.place(x=950, y=240)
home()
root.mainloop()