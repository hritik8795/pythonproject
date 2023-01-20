from tkinter import *
t =Tk()
t.geometry("400x400")
a =IntVar()
s1 =StringVar()
def show():
    if (a.get()==1):
        s1.set("male")
    else:
        s1.set("female")
r1 =Radiobutton(text ="male",variable =a,value=1,command =show)
r1.pack()
r2 =Radiobutton(text ="female",variable=a,value =2,command =show)
r2.pack()
e1 =Entry(textvariable =s1)
e1.pack()
t.mainloop()