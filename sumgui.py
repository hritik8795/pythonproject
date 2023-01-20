from tkinter import *
root=Tk()
root.geometry("500x500")
root.resizable(0,0)

x=DoubleVar() #Int var bhi ho skta hai par floa me kaam nhi karega
y =DoubleVar()
z =DoubleVar()

e1 =Entry(root,font =("Arial",25),textvariable=x)
e1.pack()
e2 =Entry(root,font =("Arial",25),textvariable =y)
e2.pack()
def show():
    a=x.get()
    b=y.get()
    c =a+b
    z.set(c)
b1 =Button(root,text ="sum",font =("Arial",25),command =show)
b1.pack()
e3 =Entry(root,font =("Arial",25),textvariable=z)
e3.pack()
root.mainloop()
