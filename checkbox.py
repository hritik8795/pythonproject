from tkinter import *
t =Tk()
t.geometry("420x420")
a =IntVar()
b =IntVar()
s =StringVar()
def show():
    s1=""
    if (a.get()==1):
         s1 +="PYTHON"
    if (b.get()==1):
        s1 +="JAVA"
    s.set(s1)
c1 =Checkbutton(font=("",15),variable =a,text ="PYTHON",command =show)
c1.pack()
c2 =Checkbutton(font=("",15),variable =b,text ="java",command =show)
c2.pack()
#b1 =Button(text ="click",font =("",15),command =show)
#b1.pack()
e1 =Entry(font =("",15),textvariable =s)
e1.pack()
t.mainloop()