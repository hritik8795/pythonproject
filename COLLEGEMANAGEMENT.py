from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import ttk
t =Tk()
t.title("CollegeManagementSystem")
t.geometry("1020x720")
t.resizable(0,0)
f55=None
def login():
    f2 = Frame(bg="#3B2F2F")
    f2.place(x=0, y=0, width=1020, height=720)

    g1 = StringVar()
    g2 = StringVar()

    name = Label(f2, text="Enter your name", bg="#3B2F2F", fg="white")
    name.place(x=350, y=200)
    e1 = Entry(textvariable=g1)
    e1.place(x=600, y=200)
    password = Label(f2, text="Enter your password", bg="#3B2F2F", fg="white")
    password.place(x=350, y=300)
    e2 = Entry(textvariable=g2)
    e2.place(x=600, y=300)

    def check():
        db=sqlite3.connect('registercollegeadmin.db')
        cr =db.cursor()
        r1=cr.execute("select * from ADMIN where ANAME ='"+g1.get()+"' AND PASSWORD='"+g2.get()+"'")
        for r in r1:
            collegePage()
            break
        else:
            messagebox.showinfo("title","invalid user name")
        db.commit()
        db.close()
        g1.set("")
        g2.set("")



    b1 = Button(f2, text="login",command =check)
    b1.place(x=500, y=450,width =100,height=40)

    b2 = Button(f2, text="<-", command=home)
    b2.place(x=20, y=650,width=100, height=40)

    b3 = Button(f2, text="register",command =register)
    b3.place(x=900, y=650, width=100, height=40)

def collegePage():
    f1 =Frame(bg ="#3B2F2F")
    f1.place(x=0,y=0,width =1020,height =720)
    l1 = Label(f1, text="Wellcome In Our College For Addmission Software ", font=("", 30),bg ="#3B2F2F",fg ="white")
    l1.place(x=50, y=50,width=900,height =50)
    l2 = Label(f1, text=" We are work for giving best and attractive future for your children:.", font=("", 25),bg ="#3B2F2F",fg ="white")
    l2.place(x=50, y=650,width =950,height =50)
    l3 = Label(f1, text="courses which we are providing:::>", font=("", 25),bg ="#3B2F2F",fg ="white")
    l3.place(x=50, y=250)
    # button for frame 1
    b1 = Button(f1, text="B.TECH", font=("", 25),command =my_menu)
    b1.place(x=580, y=240)

    b2 = Button(f1, text="M.TECH", font=("", 25),command =my_menu)
    b2.place(x=750, y=240)
    b3 = Button(f1, text="BBA", font=("", 25),command =my_menu)
    b3.place(x=600, y=500)
    b4 = Button(f1, text="BCA", font=("", 25),command =my_menu)
    b4.place(x=150, y=350)
    b5 = Button(f1, text="MBA", font=("", 25),command =my_menu)
    b5.place(x=300, y=350)
    b6 = Button(f1, text="MCA", font=("", 25),command =my_menu)
    b6.place(x=450, y=350)
    b7 = Button(f1, text="B.SC", font=("", 25),command =my_menu)
    b7.place(x=600, y=350)
    b8 = Button(f1, text="B.SC(Ag)", font=("", 25),command =my_menu)
    b8.place(x=750, y=350)
    b9 = Button(f1, text="B.Pharma", font=("", 25),command =my_menu)
    b9.place(x=400, y=500)
    b10 = Button(f1, text="D.pharma", font=("", 25),command =my_menu )
    b10.place(x=150, y=500)

def my_menu():
    t = ttk.Notebook()
    #t.place(x=0, y=0, width=600, height=400)
    t.place(x=0, y=0, width=1020, height=720)

    def demo(a):
        #print("hello world")
        if (t.index("current") == 5):
            home()
    t.bind("<<NotebookTabChanged>>", demo)

    insertData(t)
    showAllData(t)
    searchData(t)
    updateData(t)
    deleteData(t)
    logout(t)

def insertData(t):
    r1 =StringVar()
    r2 =StringVar()
    r3 = StringVar()
    r4 = StringVar()
    r5 = StringVar()
    r6 = StringVar()
    r7 = StringVar()
    r8 = StringVar()
    r9 = StringVar()
    r10 = StringVar()
    r11= StringVar()
    r12 = StringVar()
    r13 = StringVar()
    r14 = StringVar()
    r15 = StringVar()
    r16= StringVar()
    f4 = Frame(background="#3B2F2F")
    t.add(f4, text="insertstudentData")
    l1 = Label(f4, text="give  roll No ", bg="#3B2F2F", fg="white")
    l1.place(x=100, y=50)
    e1 = Entry(f4,textvariable =r1)
    e1.place(x=300, y=50)

    l2 = Label(f4, text="Name ", bg="#3B2F2F", fg="white")
    l2.place(x=100, y=100)
    e2 = Entry(f4,textvariable =r2 )
    e2.place(x=300, y=100)

    l3 = Label(f4, text="Father's Name", bg="#3B2F2F", fg="white")
    l3.place(x=100, y=150)
    e3 = Entry(f4,textvariable =r3 )
    e3.place(x=300, y=150)

    l4 = Label(f4, text="Mother's Name", bg="#3B2F2F", fg="white")
    l4.place(x=100, y=200)
    e4 = Entry(f4,textvariable =r4 )
    e4.place(x=300, y=200)

    l5 = Label(f4, text="Date of birth ", bg="#3B2F2F", fg="white")
    l5.place(x=100, y=250)
    e5 = Entry(f4, textvariable =r5)
    e5.place(x=300, y=250)

    l6 = Label(f4, text="Course ", bg="#3B2F2F", fg="white")
    l6.place(x=100, y=300)
    e6 = Entry(f4, textvariable =r6)
    e6.place(x=300, y=300)

    l7 = Label(f4, text="Branch ", bg="#3B2F2F", fg="white")
    l7.place(x=100, y=350)
    e7 = Entry(f4, textvariable =r7)
    e7.place(x=300, y=350)

    l8 = Label(f4, text="Contact Number ", bg="#3B2F2F", fg="white")
    l8.place(x=100, y=400)
    e8 = Entry(f4, textvariable =r8)
    e8.place(x=300, y=400)

    l9 = Label(f4, text="year", bg="#3B2F2F", fg="white")
    l9.place(x=100, y=450)
    e9 = Entry(f4,textvariable =r9)
    e9.place(x=300, y=450)

    l9 = Label(f4, text="12th marks %", bg="#3B2F2F", fg="white")
    l9.place(x=100, y=500)
    e9 = Entry(f4, textvariable =r10)
    e9.place(x=300, y=500)

    l10 = Label(f4, text="10th Marks %", bg="#3B2F2F", fg="white")
    l10.place(x=600, y=50)
    e10 = Entry(f4, textvariable =r11)
    e10.place(x=800, y=50)

    l11 = Label(f4, text="Email.id", bg="#3B2F2F", fg="white")
    l11.place(x=600, y=100)
    e11 = Entry(f4, textvariable =r12)
    e11.place(x=800, y=100)

    l12 = Label(f4, text="Address", bg="#3B2F2F", fg="white")
    l12.place(x=600, y=150)
    e12= Entry(f4, textvariable =r13)
    e12.place(x=800, y=150)

    l13 = Label(f4, text="district", bg="#3B2F2F", fg="white")
    l13.place(x=600, y=200)
    e13 = Entry(f4, textvariable =r14)
    e13.place(x=800, y=200)

    l14 = Label(f4, text="Pin code", bg="#3B2F2F", fg="white")
    l14.place(x=600, y=250)
    e14 = Entry(f4 ,textvariable =r15)
    e14.place(x=800, y=250)


    l16 = Label(f4, text="Adhaar No.", bg="#3B2F2F", fg="white")
    l16.place(x=600, y=300)
    e16 = Entry(f4, textvariable =r16)
    e16.place(x=800, y=300)

    def insert1():
        db=sqlite3.connect("registercollegeadmin.db")
        cr=db.cursor()
        cr.execute("insert into BTECH1 values('" + r1.get() + "','"+r2.get()+"','"+r3.get()+"','"+r4.get()+"','"+r5.get()+"','" + r6.get() + "','"+r7.get()+"','"+r8.get()+"','"+r9.get()+"','"+r10.get()+"','" + r11.get() + "','"+r12.get()+"','"+r13.get()+"','"+r14.get()+"','"+r15.get()+"','"+r16.get()+"')")
        db.commit()
        db.close()
        messagebox.showinfo("text","data inserted")
        r1.set("")
        r2.set("")
        r3.set("")
        r4.set("")
        r5.set("")
        r6.set("")
        r7.set("")
        r8.set("")
        r9.set("")
        r10.set("")
        r11.set("")
        r12.set("")
        r13.set("")
        r14.set("")
        r15.set("")
        r16.set("")
        showAllData1(f55)
    b1 =Button(f4,text="submit",command =insert1)
    b1.place(x =450,y =600 ,width =100,height =40)

    b2 =Button(f4,text ="back",command =collegePage)
    b2.place(x=600,y =600,width =100,height =40)
def showAllData(t):
    f5 = Frame(background="#3B2F2F")
    t.add(f5, text="showAllStudentData")
    global f55
    f55 =f5
    showAllData1(f5)

def showAllData1(f5):
    l0 =Label(f5,text ="roll no")
    l0.place(x=0,y =0,width =100)
    l1=Label(f5,text="Name")
    l1.place(x=105, y=0,width =100)
    l2 = Label(f5, text="Father's Name")
    l2.place(x=210, y=0,width=100)
    l3 = Label(f5, text="Mother's Name")
    l3.place(x=315, y=0,width=100)
    l4 = Label(f5, text="DOB")
    l4.place(x=420, y=0,width=100)
    l5 = Label(f5, text="Course",)
    l5.place(x=525, y=0,width=100)
    l6 = Label(f5, text="Branch")
    l6.place(x=630, y=0,width=100)
    l7 = Label(f5, text="CNO")
    l7.place(x=740, y=0,width=100)
    l8 = Label(f5, text="Year")
    l8.place(x=850, y=0,width=100)
    l10 = Label(f5, text="XII")
    l10.place(x=955, y=0,width=65)

    db = sqlite3.connect('registercollegeadmin.db')
    cr = db.cursor()
    r = cr.execute("select * from BTECH1")
    x = 0
    y = 50
    for r1 in r:
        Label(f5, text=r1[0]).place(x=x, y=y, width=100)
        x += 105
        Label(f5, text=r1[1]).place(x=x, y=y, width=100)
        x += 105
        Label(f5, text=r1[2]).place(x=x, y=y, width=100)
        x += 105
        Label(f5, text=r1[3]).place(x=x, y=y, width=100)
        x += 105
        Label(f5, text=r1[4]).place(x=x, y=y, width=100)
        x += 105
        Label(f5, text=r1[5]).place(x=x, y=y, width=100)
        x += 105
        Label(f5, text=r1[6]).place(x=x, y=y, width=100)
        x += 105
        Label(f5, text=r1[7]).place(x=x, y=y, width=100)
        x += 105
        Label(f5, text=r1[8]).place(x=x, y=y, width=100)
        x += 105
        Label(f5, text=r1[9]).place(x=x, y=y, width=100)
        x += 105
        y += 40
        x = 0

    db.commit()
    db.close()


def searchData(t):
    f6 = Frame(background="#3B2F2F")
    t.add(f6, text="searchStudentData")
    v1 = StringVar()
    u8 = Label(f6, text="Enter roll no. ", bg="#3B2F2F", fg="white")
    u8.place(x=100, y=50)
    e9 = Entry(f6, textvariable=v1)
    e9.place(x=200, y=50)
    def searchData1():
        db =sqlite3.connect("registercollegeadmin.db")
        cr=db.cursor()
        r=cr.execute("select * from BTECH1 where give_roll_no ='"+v1.get()+"'")
        for r1 in r:
            u3 = Label(f6, text=" Name is ", bg="#3B2F2F", fg="white")
            u3.place(x=200, y=100)
            u4 = Label(f6, text=r1[1], bg="#3B2F2F", fg="white")
            u4.place(x=340, y=100)
            u5 = Label(f6, text=" Father's Name ", bg="#3B2F2F", fg="white")
            u5.place(x=200, y=140)
            u6 = Label(f6, text=r1[2], bg="#3B2F2F", fg="white")
            u6.place(x=340, y=140)
            u7 = Label(f6, text=" Mother's Name", bg="#3B2F2F", fg="white")
            u7.place(x=200, y=180)
            u8 = Label(f6, text=r1[3], bg="#3B2F2F", fg="white")
            u8.place(x=340, y=180)
            u9 = Label(f6, text="DOB", bg="#3B2F2F", fg="white")
            u9.place(x=200, y=220)
            u10 = Label(f6, text=r1[4], bg="#3B2F2F", fg="white")
            u10.place(x=340, y=220)
            u11 = Label(f6, text="course", bg="#3B2F2F", fg="white")
            u11.place(x=200, y=260)
            u12 = Label(f6, text=r1[5], bg="#3B2F2F", fg="white")
            u12.place(x=340, y=260)
            u9 = Label(f6, text="Branch", bg="#3B2F2F", fg="white")
            u9.place(x=200, y=300)
            u13 = Label(f6, text=r1[6], bg="#3B2F2F", fg="white")
            u13.place(x=340, y=300)
            u14 = Label(f6, text="Cno", bg="#3B2F2F", fg="white")
            u14.place(x=200, y=340)
            u15 = Label(f6, text=r1[7], bg="#3B2F2F", fg="white")
            u15.place(x=340, y=340)

            u16 = Label(f6, text="year", bg="#3B2F2F", fg="white")
            u16.place(x=200, y=380)
            u17 = Label(f6, text=r1[8], bg="#3B2F2F", fg="white")
            u17.place(x=340, y=380)

            u18 = Label(f6, text="XII Marks", bg="#3B2F2F", fg="white")
            u18.place(x=200, y=420)
            u19 = Label(f6, text=r1[9], bg="#3B2F2F", fg="white")
            u19.place(x=340, y=420)

            u20 = Label(f6, text="Xth Marks", bg="#3B2F2F", fg="white")
            u20.place(x=200, y=460)
            u21 = Label(f6, text=r1[10], bg="#3B2F2F", fg="white")
            u21.place(x=340, y=460)

            u22 = Label(f6, text="Email Id", bg="#3B2F2F", fg="white")
            u22.place(x=200, y=500)
            u23 = Label(f6, text=r1[11], bg="#3B2F2F", fg="white")
            u23.place(x=340, y=500)

            u24 = Label(f6, text="Address", bg="#3B2F2F", fg="white")
            u24.place(x=200, y=540)
            u25 = Label(f6, text=r1[12], bg="#3B2F2F", fg="white")
            u25.place(x=340, y=540)

            u26 = Label(f6, text="District", bg="#3B2F2F", fg="white")
            u26.place(x=200, y=580)
            u27 = Label(f6, text=r1[13], bg="#3B2F2F", fg="white")
            u27.place(x=340, y=580)

            u26 = Label(f6, text="Pincode", bg="#3B2F2F", fg="white")
            u26.place(x=200, y=580)
            u27 = Label(f6, text=r1[14], bg="#3B2F2F", fg="white")
            u27.place(x=340, y=580)

            u28 = Label(f6, text="Adhaar no", bg="#3B2F2F", fg="white")
            u28.place(x=200, y=620)
            u29 = Label(f6, text=r1[15], bg="#3B2F2F", fg="white")
            u29.place(x=340, y=620)
            break
        else:
            messagebox.showinfo("text","the data is not exists")

    bu =Button(f6,text ="search",command =searchData1)
    bu.place(x =350,y =50)

def updateData(t):
    f7 = Frame(background="#3B2F2F")
    s1 =StringVar()
    t.add(f7, text="updatestudentdata")
    u1 = Label(f7, text="Roll no.", bg="#3B2F2F", fg="white")
    u1.place(x=50, y=30, width=120)
    e1 = Entry(f7, textvariable=s1)
    e1.place(x=150,y =30)
    def update1():
        s2 = StringVar()
        s3 = StringVar()
        s4 = StringVar()
        s5 = StringVar()
        s6 = StringVar()
        s7 = StringVar()
        s8 = StringVar()
        s9 = StringVar()
        s10 = StringVar()
        s11= StringVar()
        s12 = StringVar()
        s13 = StringVar()
        s14 = StringVar()
        s15 = StringVar()
        s16 = StringVar()
        db = sqlite3.connect('registercollegeadmin.db')
        cr = db.cursor()
        r = cr.execute("select * from BTECH1 where give_roll_no='" + s1.get() + "' ")
        for r1 in r:
            l2 = Label(f7, text="Name ", bg="#3B2F2F", fg="white")
            l2.place(x=100, y=100)
            e2 = Entry(f7, text =r1[1],textvariable=s2)
            e2.insert(0, r1[1])
            e2.place(x=300, y=100)


            l3 = Label(f7, text="Father's Name", bg="#3B2F2F", fg="white")
            l3.place(x=100, y=150)
            e3 = Entry(f7, text =r1[2],textvariable=s3)
            e3.insert(0, r1[2])
            e3.place(x=300, y=150)

            l4 = Label(f7, text="Mother's Name", bg="#3B2F2F", fg="white")
            l4.place(x=100, y=200)
            e4 = Entry(f7, text =r1[3],textvariable=s4)
            e4.insert(0,r1[3])
            e4.place(x=300, y=200)

            l5 = Label(f7, text="Date of birth ", bg="#3B2F2F", fg="white")
            l5.place(x=100, y=250)
            e5 = Entry(f7,text =r1[4], textvariable=s5)
            e5.insert(0, r1[4])
            e5.place(x=300, y=250)

            l6 = Label(f7, text="Course ", bg="#3B2F2F", fg="white")
            l6.place(x=100, y=300)
            e6 = Entry(f7, text =r1[5],textvariable=s6)
            e6.insert(0, r1[5])
            e6.place(x=300, y=300)

            l7 = Label(f7, text="Branch ", bg="#3B2F2F", fg="white")
            l7.place(x=100, y=350)
            e7 = Entry(f7,text =r1[6], textvariable=s7)
            e7.insert(0, r1[6])
            e7.place(x=300, y=350)

            l8 = Label(f7, text="Contact Number ", bg="#3B2F2F", fg="white")
            l8.place(x=100, y=400)
            e8 = Entry(f7, text =r1[7],textvariable=s8)
            e8.insert(0, r1[7])
            e8.place(x=300, y=400)

            l9 = Label(f7, text="year", bg="#3B2F2F", fg="white")
            l9.place(x=100, y=450)
            e9 = Entry(f7, text =r1[8],textvariable=s9)
            e9.insert(0, r1[8])
            e9.place(x=300, y=450)

            l15 = Label(f7, text="12th marks %", bg="#3B2F2F", fg="white")
            l15.place(x=100, y=500)
            e15 = Entry(f7,text =r1[9], textvariable=s10)
            e15.insert(0, r1[9])
            e15.place(x=300, y=500)

            l10 = Label(f7, text="10th Marks %", bg="#3B2F2F", fg="white")
            l10.place(x=600, y=50)
            e10 = Entry(f7, text =r1[10],textvariable=s11)
            e10.insert(0, r1[10])
            e10.place(x=800, y=50)

            l11 = Label(f7, text="Email.id", bg="#3B2F2F", fg="white")
            l11.place(x=600, y=100)
            e11 = Entry(f7, text =r1[11],textvariable=s12)
            e11.insert(0, r1[11])
            e11.place(x=800, y=100)

            l12 = Label(f7, text="Address", bg="#3B2F2F", fg="white")
            l12.place(x=600, y=150)
            e12 = Entry(f7, text =r1[12],textvariable=s13)
            e12.insert(0, r1[12])
            e12.place(x=800, y=150)

            l13 = Label(f7, text="district", bg="#3B2F2F", fg="white")
            l13.place(x=600, y=200)
            e13 = Entry(f7, text =r1[13],textvariable=s14)
            e13.insert(0, r1[13])
            e13.place(x=800, y=200)

            l14 = Label(f7, text="Pin code", bg="#3B2F2F", fg="white")
            l14.place(x=600, y=250)
            e14 = Entry(f7,text =r1[14], textvariable=s15)
            e14.insert(0, r1[14])
            e14.place(x=800, y=250)

            l16 = Label(f7, text="Adhaar No.", bg="#3B2F2F", fg="white")
            l16.place(x=600, y=300)
            e16 = Entry(f7, text =r1[15],textvariable=s16)
            e16.insert(0, r1[15])
            e16.place(x=800, y=300)

            def updateButton():
                db =sqlite3.connect('registercollegeadmin.db')
                cr =db.cursor()
                cr.execute("update BTECH1 set STUDENT_NAME='"+s2.get()+"' ,FATHER_NAME ='"+s3.get()+"', MOTHER_NAME='"+s4.get()+"',DOB ='"+s5.get()+"',COURSE='" + s6.get() + "',BRANCH='"+s7.get()+"',CNO='"+s8.get()+"',YEAR ='"+s9.get()+"',intermediatemark='"+s10.get()+"',highschoolthmark='" + s11.get() + "',Emailid='"+s12.get()+"',Address ='"+s13.get()+"',district='"+s14.get()+"',Pincode='"+s15.get()+"',Adhaarno='"+s16.get()+"'where give_roll_no='"+s1.get()+"'")
                db.commit()
                db.close()
                showAllData1(f55)
        else:
            messagebox.showinfo("text","the data does not exist")
            b11 =Button(f7,text ="update",command=updateButton)
            b11.place(x=600,y=560)


        db.commit()
        db.close()

    bo =Button(f7,text="search",command=update1)
    bo.place(x=300,y=30)
def deleteData(t):
    f8 = Frame(background="#3B2F2F")
    d1=StringVar()
    t.add(f8, text="DeletestudentData")
    l1 = Label(f8, text="Enter rollno.", bg="#3B2F2F", fg="white")
    l1.place(x=100, y=50)
    e1 = Entry(f8, textvariable=d1)
    e1.place(x=200, y=50)

    def deletedata1():
        db =sqlite3.connect('registercollegeadmin.db')
        cr =db.cursor()
        cr.execute("delete from BTECH1 where give_roll_no ='"+d1.get()+"'")
        db.commit()
        db.close()
        showAllData1(f55)
        messagebox.showinfo("title","data delete successfully" )


    b11 =Button(f8,text ="delete",command =deletedata1)
    b11.place(x =350,y =50,height =20)

def logout(t):
    f9 = Frame(background="#3B2F2F")
    t.add(f9, text="logoutAdmin")

def register():
    f3 =Frame(bg ="#3B2F2F")
    f3.place(x=0, y=0, width=1020, height=720)
    r1 =StringVar()
    r2 =StringVar()
    r3 =StringVar()
    name =Label(f3,text ="Enter your name",bg ="#3B2F2F",fg ="white")
    name.place(x=350, y=200)
    e1 =Entry(textvariable =r1)
    e1.place(x =600,y=200)
    password=Label(f3,text="Enter your password", bg="#3B2F2F", fg="white")
    password.place(x=350, y=300)
    e2 = Entry(textvariable=r2)
    e2.place(x=600, y=300)

    contact = Label(f3, text="Enter your C.No.", bg="#3B2F2F", fg="white")
    contact.place(x=350, y=400)
    e1 = Entry(textvariable=r3)
    e1.place(x=600, y=400)

    def regis1():
        db =sqlite3.connect('registercollegeadmin.db')
        cr=db.cursor()
        cr.execute("insert into ADMIN values('" + r1.get() + "','"+r2.get()+"','"+r3.get()+"')")
        db.commit()
        db.close()
        messagebox.showinfo("title", "data  is inserted")


    b1 = Button(f3, text="register",command =regis1)
    b1.place(x=500, y=550,width=100,height=40)

    b2 = Button(f3, text="home", command=home)
    b2.place(x=20, y=650,width=100, height=40)

    b2 = Button(f3, text="login", command=login)
    b2.place(x=900, y=650, width=100, height=40)


def home():
    f1 =Frame(bg ="#3B2F2F")
    f1.place(x=0,y=0,width =1020,height =720)
    b1 =Button(f1,text ="login",command =login)
    b1.place(x=300,y =300)
    b2 =Button(f1,text ="register new user",command =register)
    b2.place(x =400,y =300)
home()
t.mainloop()
