from tkinter import *
t =Tk()
t.geometry("420x420")
a =StringVar()
def show():
    #t.configure(background =a.get())
    print(a.get())
#s1 =Spinbox(font =("",15),textvariable =a,command =show,values =["blue","red","green","cyan",])
s1 =Spinbox(font =("",15),textvariable =a,command =show,from_=5,to=15)
s1.pack()
#b1 =Button(font =("",15),text="changecolor",command =show)
#b1.pack()
t.mainloop()