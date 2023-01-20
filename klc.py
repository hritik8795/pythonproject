from tkinter import *
root =Tk()
root.geometry("500x500")
root.resizable(0,0)
x=DoubleVar()
y =DoubleVar()
z =DoubleVar()
e1 =Entry(root,font =("Arial",25) ,textvariable =x)
e1.pack()
e2 =Entry(root,font =("Arial",25) ,textvariable =y)
e2.pack()
def show1():
    a =x.get()
    b= y.get()
    c= a+b
    z.set(c)

def show2():
    a =x.get()
    b= y.get()
    c= a-b
    z.set(c)

def show3():
    a =x.get()
    b= y.get()
    c= a*b
    z.set(c)
def show4():
    a =x.get()
    b= y.get()
    c= a/b
    z.set(c)

b1 =Button(root,text ="+",font =("Arial",25),command =show1)
b1.pack()

b2 =Button(root,text ="-",font =("Arial",25),command =show2)
b2.pack()
b3 =Button(root,text ="*",font =("Arial",25),command =show3)
b3.pack()
b4 =Button(root,text ="/",font =("Arial",25),command =show4)
b4.pack()

e3 =Entry(root,font =("Arial",25) ,textvariable =z)
e3.pack()

root.mainloop()
