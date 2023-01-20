#yahan ekproblem face kar rahe hai jab hum delete waale section me jaa rahe hai  to blank par bhi inserted success fully battati hai


from tkinter import *
import sqlite3
from tkinter import messagebox
t =Tk()
t.geometry("600x400")
t.resizable(0,0)
def login():
    f2 =Frame(bg ="#3B2F2F")
    f2.place(x=0, y=0, width=600, height=600)
    name =Label(f2,text ="Enter your name",bg ="#3B2F2F",fg ="white")
    name.place(x=50,y =100)
    e1 =Entry()
    e1.place(x =200,y=100)
    password=Label(f2,text="Enter your password", bg="#3B2F2F", fg="white")
    password.place(x=50, y=150)
    e2 = Entry()
    e2.place(x=200, y=150)

    b1 =Button(f2,text="login")
    b1.place(x=150,y =200)

    b2 = Button(f2, text="home" ,command=home)
    b2.place(x=5, y=350,width =100,height =40)

    b2 = Button(f2, text="register",command =register)
    b2.place(x=490, y=350, width=100, height=40)

def register():
    f3 =Frame(bg ="#3B2F2F")
    f3.place(x=0, y=0, width=600, height=600)
    r1 =StringVar()
    r2 =StringVar()
    r3 =StringVar()
    name =Label(f3,text ="Enter your name",bg ="#3B2F2F",fg ="white")
    name.place(x=50,y =100)
    e1 =Entry(textvariable =r1)
    e1.place(x =200,y=100)
    password=Label(f3,text="Enter your password", bg="#3B2F2F", fg="white")
    password.place(x=50, y=150)
    e2 = Entry(textvariable=r2)
    e2.place(x=200, y=150)

    contact = Label(f3, text="Enter your C.No.", bg="#3B2F2F", fg="white")
    contact.place(x=50, y=200)
    e1 = Entry(textvariable=r3)
    e1.place(x=200, y=200)

    # creating a button of regis1 for register in the data base
    def regis1():
        db = sqlite3.connect('new.db')
        cr = db.cursor()
        cr.execute("insert into regis values('" + r1.get() + "','"+r2.get()+"','"+r3.get()+"')")
        db.commit()
        db.close()
        messagebox.showinfo("title","data  is inserted")
        r1.set("")
        r2.set("")
        r3.set("")
    b1 =Button(f3,text="register", command =regis1)
    b1.place(x=150,y =250)

    b2 = Button(f3, text="home" ,command=home)
    b2.place(x=5, y=350,width =100,height =40)

    b2 = Button(f3, text="login", command =login)
    b2.place(x=490,y=350, width=100, height=40)

def home():
    f1 =Frame(bg="#3B2F2F")
    f1.place(x =0,y =0,width =600,height =600)
    b1 =Button(f1,text ="login",command =login)
    b1.place(x =220,y=150)
    b1 = Button(f1, text="register",command =register)
    b1.place(x=310, y=150)
home()
t.mainloop()








##########################################################____________aadhey ke baad -----------------------------------------------------

from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox
t =Tk()
t.geometry("600x400")
t.resizable(0,0)
f55 =None
def login():
    f2 =Frame(bg ="#3B2F2F")
    f2.place(x=0, y=0, width=600, height=600)

    g1 = StringVar()
    g2 = StringVar()

    name =Label(f2,text ="Enter your name",bg ="#3B2F2F",fg ="white")
    name.place(x=50,y =100)
    e1 =Entry(textvariable=g1)
    e1.place(x =200,y=100)
    password=Label(f2,text="Enter your password", bg="#3B2F2F", fg="white")
    password.place(x=50, y=150)
    e2 = Entry(textvariable=g2)
    e2.place(x=200, y=150)

    #writing a code for checking for user is genuine or not
    def check():
        db=sqlite3.connect('new.db')
        cr =db.cursor()
        r=cr.execute("select * from regis where UNAME ='"+g1.get()+"' AND UPASS='"+g2.get()+"'")
        for r in r:
            #messagebox.showinfo("text","welcome use in our system")
            my_menu()
            break
        else:
            messagebox.showinfo("text","user in valid or wrong name and password")
        db.commit()
        db.close()
        g1.set("")
        g2.set("")


    b1 =Button(f2,text="login",command=check)
    b1.place(x=150,y =200)

    b2 = Button(f2, text="home" ,command=home)
    b2.place(x=5, y=350,width =100,height =40)

    b2 = Button(f2, text="register",command =register)
    b2.place(x=490, y=350, width=100, height=40)

def my_menu():
    t =ttk.Notebook()
    t.place(x=0,y=0,width=600,height =400)
    insertData(t)
    showAllData(t)
    searchData(t)
    deleteData(t)
    updateData(t)
def insertData(t):
    f4 =Frame(background ="blue")
    t.add(f4,text ="insert")
    c1 =StringVar()
    c2 =StringVar()
    c3 =StringVar()
    c4 =StringVar()
    c5 =StringVar()
    l1 =Label(f4,text ="Enter roll No ",bg ="blue",fg ="white")
    l1.place(x =100,y=50)
    e1 =Entry(f4,textvariable =c1)
    e1.place(x=300,y=50)

    l2 = Label(f4, text="Enter Name ", bg="blue", fg="white")
    l2.place(x=100, y=100)
    e2 = Entry(f4,textvariable =c2)
    e2.place(x=300, y=100)

    l3 = Label(f4, text="Enter marks of phy", bg="blue", fg="white")
    l3.place(x=100, y=150)
    e3 = Entry(f4,textvariable =c3)
    e3.place(x=300, y=150)


    l4 = Label(f4, text="Enter marks of chem", bg="blue", fg="white")
    l4.place(x=100, y=200)
    e4 = Entry(f4,textvariable =c4)
    e4.place(x=300, y=200)


    l5 = Label(f4, text="Enter marks of math ",bg ="blue",fg ="white")
    l5.place(x=100, y=250)
    e5 = Entry(f4,textvariable =c5)
    e5.place(x=300, y=250)

    def insertDemo1():
        db=sqlite3.connect('new_project1.db')
        cr=db.cursor()
        cr.execute("insert into ins values('" + c1.get() + "','"+c2.get()+"','"+c3.get()+"','"+c4.get()+"','"+c5.get()+"')")
        db.commit()
        db.close()
        messagebox.showinfo("title", "data  is inserted")
        c1.set("")
        c2.set("")
        c3.set("")
        showAllData1(f55)

    b1=Button(text="insert",command =insertDemo1)
    b1.place(x=250,y=330,width =100)

def showAllData(t):
    f5 =Frame(background ="blue")
    t.add(f5,text ="show_all")
    global f55
    f55 =f5
    showAllData1(f5)
#insert ke andar show all button par sara data aana chahiye data base se
def showAllData1(f5):
    u1 =Label(f5,text ="roll no.")
    u1.place(x=0,y=0,width=120)

    u2 = Label(f5, text="Name")
    u2.place(x=120, y=0, width=120)

    u3 = Label(f5, text="physics")
    u3.place(x=240, y=0, width=120)

    u4 = Label(f5, text="chemistry")
    u4.place(x=360, y=0, width=120)

    u5 = Label(f5, text="Math")
    u5.place(x=480, y=0, width=120)

    db = sqlite3.connect('new_project1.db')
    cr = db.cursor()
    r = cr.execute("select * from ins")
    x =0
    y=50
    for r1 in r:
        Label(f5, text=r1[0]).place(x=x, y=y, width=120)
        x +=120
        Label(f5, text=r1[1]).place(x=x, y=y, width=120)
        x += 120
        Label(f5, text=r1[2]).place(x=x, y=y, width=120)
        x += 120
        Label(f5, text=r1[3]).place(x=x, y=y, width=120)
        x += 120
        Label(f5, text=r1[4]).place(x=x, y=y, width=120)
        y +=40
        x=0

    db.commit()
    db.close()





def searchData(t):
    f6 =Frame(background ="blue")
    t.add(f6,text ="search")
    v1 =StringVar()
    u8 =Label(f6,text ="Enter roll no. ",bg ="blue", fg ="white")
    u8.place(x=100,y=50)
    e9 =Entry(f6,textvariable =v1)
    e9.place(x =200,y =50)
    def searchData1():
        db =sqlite3.connect('new_project1.db')
        cr =db.cursor()
        r =cr.execute("select * from ins where UROLLNO ='"+v1.get()+"' ")
        for r1 in r:
            u3 =Label(f6, text=" Name is ", bg="blue", fg="white")
            u3.place(x=200, y=100)
            u4 = Label(f6, text=r1[1], bg="blue", fg="white")
            u4.place(x=290, y=100)
            u5 = Label(f6, text="Physics", bg="blue", fg="white")
            u5.place(x=200, y=130)
            u6 = Label(f6, text=r1[2], bg="blue", fg="white")
            u6.place(x=290, y=130)

            u7 = Label(f6, text=" Chemistry ", bg="blue", fg="white")
            u7.place(x=200, y=160)
            u8 = Label(f6, text=r1[3], bg="blue", fg="white")
            u8.place(x=290, y=160)

            u9 = Label(f6, text=" Math", bg="blue", fg="white")
            u9.place(x=200, y=190)
            u10 = Label(f6, text=r1[4], bg="blue", fg="white")
            u10.place(x=290, y=190)
            break
        else:
            messagebox.showinfo("text","the data is not exists")
            u3 = Label(f6, text="", bg="blue", fg="white")
            u3.place(x=200, y=100,width =300)
            u5 = Label(f6, text="", bg="blue", fg="white")
            u5.place(x=200, y=130,width =300)

            u7 = Label(f6, text="", bg="blue", fg="white")
            u7.place(x=200, y=160,width =300)

            u9 = Label(f6, text="", bg="blue", fg="white")
            u9.place(x=200, y=190,width =300)

        db.commit()
        db.close()


    b9 =Button(f6,text ="Search",command =searchData1)
    b9.place(x=350,y=50,height=20)
def updateData(t):
    f7 =Frame(background ="blue")
    s1 =StringVar()
    t.add(f7,text ="update")
    u1 =Label(f7, text="Roll no.",bg ="blue",fg ="white")
    u1.place(x=75, y=50, width=120)
    e1 =Entry(f7,textvariable=s1)
    e1.place(x=200,y =50)

    def updateData1():
        db =sqlite3.connect('new_project1.db')
        cr =db.cursor()
        r =cr.execute("select * from ins where UROLLNO ='"+s1.get()+"' ")
        for r1 in r:
            u3 =Label(f7, text=" Name is ", bg="blue", fg="white")
            u3.place(x=200, y=100)
            u4 = Entry(f7, text=r1[1], fg="black")
            u4.insert(0,r1[1])
            u4.place(x=290, y=100)

            u5 = Label(f7, text="Physics ",bg ="blue", fg="white")
            u5.place(x=200, y=150)
            u6 = Entry(f7, text=r1[2], fg="black")
            u6.insert(0, r1[2])
            u6.place(x=290, y=150)

            u7 = Label(f7, text="Chemistry ", bg="blue", fg="white")
            u7.place(x=200, y=200)
            u8 = Entry(f7, fg ="black")
            u8.insert(0, r1[3])
            u8.place(x=290, y=200)

            u9 = Label(f7, text=" Math ",bg ="blue", fg="white")
            u9.place(x=200, y=250)
            u10= Entry(f7, fg="black")
            u10.insert(0, r1[4])
            u10.place(x=290, y=250)

            b11 =Button(f7,text ="update",)
            b11.place(x=300,y =300)

            break
        else:
            messagebox.showinfo("text","the data is not exists")
            u3 = Label(f7, text="", bg="blue", fg="white")
            u3.place(x=200, y=100,width =300)
            u5 = Label(f7, text="", bg="blue", fg="white")
            u5.place(x=200, y=130,width =300)

            u7 = Label(f7, text="", bg="blue", fg="white")
            u7.place(x=200, y=160,width =300)

            u9 = Label(f7, text="", bg="blue", fg="white")
            u9.place(x=200, y=190,width =300)

        db.commit()
        db.close()
    b1 =Button(f7,text ="Update",command =updateData1)
    b1.place(x =350,y =50,height=20)


def deleteData(t):
    f8 =Frame(background ="blue")
    t.add(f8,text ="delete")


def register():
    f3 =Frame(bg ="#3B2F2F")
    f3.place(x=0, y=0, width=600, height=600)
    r1 =StringVar()
    r2 =StringVar()
    r3 =StringVar()
    name =Label(f3,text ="Enter your name",bg ="#3B2F2F",fg ="white")
    name.place(x=50,y =100)
    e1 =Entry(textvariable =r1)
    e1.place(x =200,y=100)
    password=Label(f3,text="Enter your password", bg="#3B2F2F", fg="white")
    password.place(x=50, y=150)
    e2 = Entry(textvariable=r2)
    e2.place(x=200, y=150)

    contact = Label(f3, text="Enter your C.No.", bg="#3B2F2F", fg="white")
    contact.place(x=50, y=200)
    e1 = Entry(textvariable=r3)
    e1.place(x=200, y=200)

    # creating a button of regis1 for register in the data base
    def regis1():
        db = sqlite3.connect('new.db')
        cr = db.cursor()
        cr.execute("insert into regis values('" + r1.get() + "','"+r2.get()+"','"+r3.get()+"')")
        db.commit()
        db.close()
        messagebox.showinfo("title","data  is inserted")
        r1.set("")
        r2.set("")
        r3.set("")
    b1 =Button(f3,text="register", command =regis1)
    b1.place(x=150,y =250)

    b2 = Button(f3, text="home" ,command=home)
    b2.place(x=5, y=350,width =100,height =40)

    b2 = Button(f3, text="login", command =login)
    b2.place(x=490,y=350, width=100, height=40)

def home():
    f1 =Frame(bg="#3B2F2F")
    f1.place(x =0,y =0,width =600,height =600)
    b1 =Button(f1,text ="login",command =login)
    b1.place(x =220,y=150)
    b1 = Button(f1, text="register",command =register)
    b1.place(x=310, y=150)
home()
t.mainloop()


---------------------------third devlop stage-----------------------

from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox
t =Tk()
t.geometry("600x400")
t.resizable(0,0)
f55 =None
def login():
    f2 =Frame(bg ="#3B2F2F")
    f2.place(x=0, y=0, width=600, height=600)

    g1 = StringVar()
    g2 = StringVar()

    name =Label(f2,text ="Enter your name",bg ="#3B2F2F",fg ="white")
    name.place(x=50,y =100)
    e1 =Entry(textvariable=g1)
    e1.place(x =200,y=100)
    password=Label(f2,text="Enter your password", bg="#3B2F2F", fg="white")
    password.place(x=50, y=150)
    e2 = Entry(textvariable=g2)
    e2.place(x=200, y=150)

    #writing a code for checking for user is genuine or not
    def check():
        db=sqlite3.connect('new.db')
        cr =db.cursor()
        r=cr.execute("select * from regis where UNAME ='"+g1.get()+"' AND UPASS='"+g2.get()+"'")
        for r in r:
            #messagebox.showinfo("text","welcome use in our system")
            my_menu()
            break
        else:
            messagebox.showinfo("text","user in valid or wrong name and password")
        db.commit()
        db.close()
        g1.set("")
        g2.set("")


    b1 =Button(f2,text="login",command=check)
    b1.place(x=150,y =200)

    b2 = Button(f2, text="home" ,command=home)
    b2.place(x=5, y=350,width =100,height =40)

    b2 = Button(f2, text="register",command =register)
    b2.place(x=490, y=350, width=100, height=40)

def my_menu():
    t =ttk.Notebook()
    t.place(x=0,y=0,width=600,height =400)
    insertData(t)
    showAllData(t)
    searchData(t)
    updateData(t)
    deleteData(t)
    logout(t)
def insertData(t):
    f4 =Frame(background ="blue")
    t.add(f4,text ="insert")
    c1 =StringVar()
    c2 =StringVar()
    c3 =StringVar()
    c4 =StringVar()
    c5 =StringVar()
    l1 =Label(f4,text ="Enter roll No ",bg ="blue",fg ="white")
    l1.place(x =100,y=50)
    e1 =Entry(f4,textvariable =c1)
    e1.place(x=300,y=50)

    l2 = Label(f4, text="Enter Name ", bg="blue", fg="white")
    l2.place(x=100, y=100)
    e2 = Entry(f4,textvariable =c2)
    e2.place(x=300, y=100)

    l3 = Label(f4, text="Enter marks of phy", bg="blue", fg="white")
    l3.place(x=100, y=150)
    e3 = Entry(f4,textvariable =c3)
    e3.place(x=300, y=150)


    l4 = Label(f4, text="Enter marks of chem", bg="blue", fg="white")
    l4.place(x=100, y=200)
    e4 = Entry(f4,textvariable =c4)
    e4.place(x=300, y=200)


    l5 = Label(f4, text="Enter marks of math ",bg ="blue",fg ="white")
    l5.place(x=100, y=250)
    e5 = Entry(f4,textvariable =c5)
    e5.place(x=300, y=250)

    def insertDemo1():
        db=sqlite3.connect('new_project1.db')
        cr=db.cursor()
        cr.execute("insert into ins values('" + c1.get() + "','"+c2.get()+"','"+c3.get()+"','"+c4.get()+"','"+c5.get()+"')")
        db.commit()
        db.close()
        messagebox.showinfo("title", "data  is inserted")
        c1.set("")
        c2.set("")
        c3.set("")
        c4.set("")
        c5.set("")
        showAllData1(f55)

    b1=Button(text="insert",command =insertDemo1)
    b1.place(x=250,y=330,width =100)

def showAllData(t):
    f5 =Frame(background ="blue")
    t.add(f5,text ="show_all")
    global f55
    f55 =f5
    showAllData1(f5)
#insert ke andar show all button par sara data aana chahiye data base se
def showAllData1(f5):
    for w in f5.winfo_children():
        w.destroy()
    u1 =Label(f5,text ="roll no.")
    u1.place(x=0,y=0,width=120)

    u2 = Label(f5, text="Name")
    u2.place(x=120, y=0, width=120)

    u3 = Label(f5, text="physics")
    u3.place(x=240, y=0, width=120)

    u4 = Label(f5, text="chemistry")
    u4.place(x=360, y=0, width=120)

    u5 = Label(f5, text="Math")
    u5.place(x=480, y=0, width=120)

    db = sqlite3.connect('new_project1.db')
    cr = db.cursor()
    r = cr.execute("select * from ins")
    x =0
    y=50
    for r1 in r:
        Label(f5, text=r1[0]).place(x=x, y=y, width=120)
        x +=120
        Label(f5, text=r1[1]).place(x=x, y=y, width=120)
        x += 120
        Label(f5, text=r1[2]).place(x=x, y=y, width=120)
        x += 120
        Label(f5, text=r1[3]).place(x=x, y=y, width=120)
        x += 120
        Label(f5, text=r1[4]).place(x=x, y=y, width=120)
        y +=40
        x=0

    db.commit()
    db.close()





def searchData(t):
    f6 =Frame(background ="blue")
    t.add(f6,text ="search")
    v1 =StringVar()
    u8 =Label(f6,text ="Enter roll no. ",bg ="blue", fg ="white")
    u8.place(x=100,y=50)
    e9 =Entry(f6,textvariable =v1)
    e9.place(x =200,y =50)
    def searchData1(f5):
        db =sqlite3.connect('new_project1.db')
        cr =db.cursor()
        r =cr.execute("select * from ins where UROLLNO ='"+v1.get()+"' ")
        for r1 in r:
            u3 =Label(f6, text=" Name is ", bg="blue", fg="white")
            u3.place(x=200, y=100)
            u4 = Label(f6, text=r1[1], bg="blue", fg="white")
            u4.place(x=290, y=100)
            u5 = Label(f6, text="Physics", bg="blue", fg="white")
            u5.place(x=200, y=130)
            u6 = Label(f6, text=r1[2], bg="blue", fg="white")
            u6.place(x=290, y=130)

            u7 = Label(f6, text=" Chemistry ", bg="blue", fg="white")
            u7.place(x=200, y=160)
            u8 = Label(f6, text=r1[3], bg="blue", fg="white")
            u8.place(x=290, y=160)

            u9 = Label(f6, text=" Math", bg="blue", fg="white")
            u9.place(x=200, y=190)
            u10 = Label(f6, text=r1[4], bg="blue", fg="white")
            u10.place(x=290, y=190)
            break
        else:
            messagebox.showinfo("text","the data is not exists")
            u3 = Label(f6, text="", bg="blue", fg="white")
            u3.place(x=200, y=100,width =300)
            u5 = Label(f6, text="", bg="blue", fg="white")
            u5.place(x=200, y=130,width =300)

            u7 = Label(f6, text="", bg="blue", fg="white")
            u7.place(x=200, y=160,width =300)

            u9 = Label(f6, text="", bg="blue", fg="white")
            u9.place(x=200, y=190,width =300)

        db.commit()
        db.close()


    b9 =Button(f6,text ="Search",command =searchData1)
    b9.place(x=350,y=50,height=20)
def updateData(t):
    f7 =Frame(background ="blue")
    s1 =StringVar()
    t.add(f7,text ="update")
    u1 =Label(f7, text="Roll no.",bg ="blue",fg ="white")
    u1.place(x=75, y=50, width=120)
    e1 =Entry(f7,textvariable=s1)
    e1.place(x=200,y =50)

    def updateData1():
        s2 =StringVar()
        s3 = StringVar()
        s4 = StringVar()
        s5= StringVar()
        db =sqlite3.connect('new_project1.db')
        cr =db.cursor()
        r =cr.execute("select * from ins where UROLLNO ='"+s1.get()+"' ")
        for r1 in r:
            u3 =Label(f7, text=" Name is ", bg="blue", fg="white")
            u3.place(x=200, y=100)
            u4 = Entry(f7, text=r1[1], fg="black",textvariable=s2)
            u4.insert(0,r1[1])
            u4.place(x=290, y=100)

            u5 = Label(f7, text="Physics ",bg ="blue", fg="white")
            u5.place(x=200, y=150)
            u6 = Entry(f7, text=r1[2], fg="black",textvariable=s3)
            u6.insert(0, r1[2])
            u6.place(x=290, y=150)

            u7 = Label(f7, text="Chemistry ", bg="blue", fg="white")
            u7.place(x=200, y=200)
            u8 = Entry(f7, fg ="black",textvariable=s4)
            u8.insert(0, r1[3])
            u8.place(x=290, y=200)

            u9 = Label(f7, text=" Math ",bg ="blue", fg="white")
            u9.place(x=200, y=250)
            u10= Entry(f7, fg="black",textvariable=s5)
            u10.insert(0, r1[4])
            u10.place(x=290, y=250)
            def updateButton():
                db =sqlite3.connect('new_project1.db')
                cr =db.cursor()
                cr.execute("update ins set UNAME ='"+s2.get()+"' ,Uphy ='"+s3.get()+"', Uche ='"+s4.get()+"',UMATH ='"+s5.get()+"'where UROLLNO ='"+s1.get()+"'")
                db.commit()
                db.close()
                showAllData1(f55)


            b11 =Button(f7,text ="update",command =updateButton)
            b11.place(x=300,y =300)

            break
        else:
            messagebox.showinfo("text","the data is not exists")
            u3 = Label(f7, text="", bg="blue", fg="white")
            u3.place(x=200, y=100,width =300)
            u5 = Label(f7, text="", bg="blue", fg="white")
            u5.place(x=200, y=130,width =300)

            u7 = Label(f7, text="", bg="blue", fg="white")
            u7.place(x=200, y=160,width =300)

            u9 = Label(f7, text="", bg="blue", fg="white")
            u9.place(x=200, y=190,width =300)

        db.commit()
        db.close()
    b1 =Button(f7,text ="Update",command =updateData1)
    b1.place(x =350,y =50,height=20)

def deleteData(t):
    f8 =Frame(background ="blue")
    d1 =StringVar()
    t.add(f8,text ="delete")
    l1 =Label(f8,text ="Enter rollno.",bg ="blue",fg ="white")
    l1.place(x=100,y =50)
    e1 =Entry(f8,textvariable =d1)
    e1.place(x =200,y =50)
    def deletedata1():
        db =sqlite3.connect('new_project1.db')
        cr =db.cursor()
        cr.execute("delete from ins where UROLLNO ='"+d1.get()+"'")
        db.commit()
        db.close()
        showAllData1(f55)
        messagebox.showinfo("title","data delete successfully" )


    b11 =Button(f8,text ="delete",command =deletedata1)
    b11.place(x =350,y =50,height =20)

def logout(t):
    f9 =Frame(background ="blue")
    t.add(f9,text ="logout")



def register():
    f3 =Frame(bg ="#3B2F2F")
    f3.place(x=0, y=0, width=600, height=600)
    r1 =StringVar()
    r2 =StringVar()
    r3 =StringVar()
    name =Label(f3,text ="Enter your name",bg ="#3B2F2F",fg ="white")
    name.place(x=50,y =100)
    e1 =Entry(textvariable =r1)
    e1.place(x =200,y=100)
    password=Label(f3,text="Enter your password", bg="#3B2F2F", fg="white")
    password.place(x=50, y=150)
    e2 = Entry(textvariable=r2)
    e2.place(x=200, y=150)

    contact = Label(f3, text="Enter your C.No.", bg="#3B2F2F", fg="white")
    contact.place(x=50, y=200)
    e1 = Entry(textvariable=r3)
    e1.place(x=200, y=200)

    # creating a button of regis1 for register in the data base
    def regis1():
        db = sqlite3.connect('new.db')
        cr = db.cursor()
        cr.execute("insert into regis values('" + r1.get() + "','"+r2.get()+"','"+r3.get()+"')")
        db.commit()
        db.close()
        messagebox.showinfo("title","data  is inserted")
        r1.set("")
        r2.set("")
        r3.set("")
    b1 =Button(f3,text="register", command =regis1)
    b1.place(x=150,y =250)

    b2 = Button(f3, text="home" ,command=home)
    b2.place(x=5, y=350,width =100,height =40)

    b2 = Button(f3, text="login", command =login)
    b2.place(x=490,y=350, width=100, height=40)

def home():
    f1 =Frame(bg="#3B2F2F")
    f1.place(x =0,y =0,width =600,height =600)
    b1 =Button(f1,text ="login",command =login)
    b1.place(x =220,y=150)
    b1 = Button(f1, text="register",command =register)
    b1.place(x=310, y=150)
home()
t.mainloop()