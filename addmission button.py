#----------------------addmission button work for btech
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("ADDMISSION DATA SOFTWARE")
root.geometry("1280x720")
root.resizable(0, 0)
root.configure(background="cyan")
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////---------
def btech():
    f2 = Frame(bg="blue")
    f2.place(x=0, y=0, width=1280, height=720)
    e1 =Entry(f2)
    e1.pack()
    e2=Entry(f2)
    e2.pack()
    b1 =Button(f2,text ="back",command =home)
    b1.pack()



def home():
    f1 =Frame(bg ="cyan")
    f1.place(x =0,y=0,width =1280,height =720)
    l1 = Label(f1,text="Wellcome In Our College For Addmission Software ", font=("", 30))
    l1.place(x=300, y=50)
    l2 = Label(f1, text=" We are work for giving best and attractive future for your children:.", font=("", 25))
    l2.place(x=200, y=650)
    l3 = Label(f1, text="courses which we are providing:::>", font=("", 25))
    l3.place(x=200, y=250)
# button for frame 1
    b1 = Button(f1, text="B.TECH", font=("", 25),command =btech)
    b1.place(x=750, y=240)

    b2 = Button(f1, text="M.TECH", font=("", 25),command =btech)
    b2.place(x=950, y=240)
    b3 = Button(f1, text="BBA", font=("", 25),command =btech)
    b3.place(x=1150, y=240)
    b4 = Button(f1,text="BCA", font=("", 25),command =btech)
    b4.place(x=150, y=350)
    b5 = Button(f1, text="MBA", font=("", 25),command =btech)
    b5.place(x=300, y=350)
    b6 = Button(f1, text="MCA", font=("", 25),command =btech)
    b6.place(x=450, y=350)
    b7 = Button(f1, text="B.SC", font=("", 25),command =btech)
    b7.place(x=600, y=350)
    b8 = Button(f1, text="B.SC(Ag)", font=("", 25),command =btech)
    b8.place(x=750, y=350)
    b9 = Button(f1, text="B.Pharma", font=("", 25),command =btech)
    b9.place(x=1000, y=350)
    b10 = Button(f1, text="D.pharma", font=("", 25),command =btech)
    b10.place(x=150, y=500)
home()
root.mainloop()




# update 24/10/2021
from tkinter import *
root = Tk()
root.title("ADDMISSION DATA SOFTWARE")
root.geometry("1280x720")
root.resizable(0, 0)
root.configure(background="cyan")
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////---------
def btech():
    f2 = Frame(bg="blue")
    f2.place(x=0, y=0, width=1280, height=720)
    l0 =Label(f2,text ="welcome to B.TECH addmission page::- ",font =("",25))
    l0.place(x=350,y=20)
    l1 =Label(f2,text ="Enter The Student Name",font =("",15))
    l1.place(x=25,y=100)
    e1 =Entry(f2,font=("",15))
    e1.place(x=320,y=100)
    l2 =Label(f2,text ="Enter The Course",font =("",15))
    l2.place(x =25,y=200)
    e2=Entry(f2,font =("",15))
    e2.place(x=320,y=200)

    l3 =Label(f2,text ="Enter the Intermediate mark",font =("",15))
    l3.place(x =25,y=300)
    e3=Entry(f2,font =("",15))
    e3.place(x=320,y =300,width =70)
    e32=Entry(f2,font =("",15))
    e32.place(x=410,y =300,width =70)

    l3 =Label(f2,text ="Enter the highschool mark",font =("",15))
    l3.place(x =25,y=400)
    e3=Entry(f2,font =("",15))
    e3.place(x=320,y =400,width =70)
    e31=Entry(f2,font =("",15))
    e31.place(x=410,y =400,width =70)

    l4 =Label(f2,text ="Enter the Registration Id",font =("",15))
    l4.place(x =25,y=500)
    e4=Entry(f2,font =("",15))
    e4.place(x=320,y =500)

    l5 =Label(f2,text ="Father Name",font =("",15))
    l5.place(x =700,y=100)
    e5=Entry(f2,font =("",15))
    e5.place(x=900,y =100)


    l6 =Label(f2,text ="Mother's Name",font =("",15))
    l6.place(x =700,y=200)
    e6=Entry(f2,font =("",15))
    e6.place(x=900,y =200)

    l7 =Label(f2,text ="Email",font =("",15))
    l7.place(x =700,y=300)
    e7=Entry(f2,font =("",15))
    e7.place(x=900,y =300)

    l8 =Label(f2,text ="Mobile No.",font =("",15))
    l8.place(x =700,y=400)
    e8=Entry(f2,font =("",15))
    e8.place(x=900,y =400)

    l8 =Label(f2,text ="Gender",font =("",15))
    l8.place(x =700,y=500)
    e8=Entry(f2,font =("",15))
    e8.place(x=820,y =500,width =60)

    l8 =Label(f2,text ="Cotegory",font =("",15))
    l8.place(x =950,y=500)
    e8=Entry(f2,font =("",15))
    e8.place(x=1080,y =500,width =60)

    b1 =Button(f2,text ="Back",command =home)
    b1.place(x=500,y=600,width =100)

    b1 =Button(f2,text ="Insert Data.")
    b1.place(x=650,y=600,width =100)



def home():
    f1 =Frame(bg ="cyan")
    f1.place(x =0,y=0,width =1280,height =720)
    l1 = Label(f1,text="Wellcome In Our College For Addmission Software ", font=("", 35))
    l1.place(x=100, y=80)
    l2 = Label(f1, text=" We are work for giving best and attractive future for your children:.", font=("", 25))
    l2.place(x=200, y=650)
    l3 = Label(f1, text="courses which we are providing:::>", font=("", 25))
    l3.place(x=200, y=250)
# button for frame 1
    b1 = Button(f1, text="B.TECH", font=("", 25),command =btech)
    b1.place(x=750, y=240)

    b2 = Button(f1, text="M.TECH", font=("", 25),command =btech)
    b2.place(x=950, y=240)
    b3 = Button(f1, text="BBA", font=("", 25),command =btech)
    b3.place(x=1150, y=240)
    b4 = Button(f1,text="BCA", font=("", 25),command =btech)
    b4.place(x=150, y=350)
    b5 = Button(f1, text="MBA", font=("", 25),command =btech)
    b5.place(x=300, y=350)
    b6 = Button(f1, text="MCA", font=("", 25),command =btech)
    b6.place(x=450, y=350)
    b7 = Button(f1, text="B.SC", font=("", 25),command =btech)
    b7.place(x=600, y=350)
    b8 = Button(f1, text="B.SC(Ag)", font=("", 25),command =btech)
    b8.place(x=750, y=350)
    b9 = Button(f1, text="B.Pharma", font=("", 25),command =btech)
    b9.place(x=1000, y=350)
    b10 = Button(f1, text="D.pharma", font=("", 25),command =btech)
    b10.place(x=150, y=500)
home()
root.mainloop()