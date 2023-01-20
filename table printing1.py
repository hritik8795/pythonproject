from tkinter import *
root=Tk()
root.geometry('500x500')
root.resizable(0,0)
x =IntVar()
e1 =Entry(root,font =('Arial',25),textvariable =x)
e1.pack()
def show():
    a =x.get()
    for i in range(1,11):
        print(a*i)
b1 =Button(root,text ="click",font=("Arial",25),command =show)
b1.pack()

root.mainloop()