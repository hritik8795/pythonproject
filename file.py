from tkinter import *
from tkinter import messagebox
root =Tk()

name_var =StringVar()
age_var=StringVar()
m_box =StringVar()
def submit():
    name =name_var.get()
    age =age_var.get()
    if name=="" or age =="":
        messagebox.showerror('error','please fill both name and age')

label1 =Label(root,text ="enter your name",font =("Arial",25))
label1.grid(row =0,column =0,padx ="25",pady ="25")
e1 =Entry(root,font=("Arial",25),textvariable =name_var)
e1.grid(row=0,column =1,padx ="25",pady ="25")
label2 =Label(root,text ="enter your age",font =("Arial",25))
label2.grid(row =1,column =0,padx ="25",pady ="25")
e2 =Entry(root,font=("Arial",25),textvariable =age_var)
e2.grid(row=1,column =1,padx ="25",pady ="25")
b1 =Button(text ="submit",font=("Arial",25),padx ="5",pady ="5",bg ="black",fg ="white",command=submit)
b1.grid(row =2,column =1)

root.mainloop()