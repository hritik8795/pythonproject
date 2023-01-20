from tkinter import *
root =Tk()
root.geometry("427x350")
root.resizable(0,0)
root.title("shortklc")
root.configure(background ="black")
a=StringVar()
def show(c):
   a.set(a.get()+c)

def equ():
    ex =a.get()
    a.set(eval(ex))
def clr():
    a.set("")

entry =Entry(font =("",30),justify ="right",textvariable =a)
entry.place (height ='50',width ="427")

button =[Button()]*16
data =["7","8","9","+","4","5","6","-","1","2","3","0","*","C","=","/","."]
k =0
x =5
y =55
for i in range(4):
    for j in range(4):
        button[k]=Button(text =data[k],font=("",25),bg ="grey",fg ="white",activebackground ="red",activeforeground ="yellow")
        button[k].place(x =x,y =y,width =100,height =50)
        k +=1
        x +=105
    x =5

    y +=55
button[0].configure(command =lambda:show(data[0]))
button[1].configure(command =lambda:show(data[1]))
button[2].configure(command =lambda:show(data[2]))
button[3].configure(command =lambda:show(data[3]))
button[4].configure(command =lambda:show(data[4]))
button[5].configure(command =lambda:show(data[5]))
button[6].configure(command =lambda:show(data[6]))
button[7].configure(command =lambda:show(data[7]))
button[8].configure(command =lambda:show(data[8]))
button[9].configure(command =lambda:show(data[9]))
button[10].configure(command =lambda:show(data[10]))
button[11].configure(command =lambda:show(data[11]))
button[12].configure(command =lambda:show(data[12]))
button[13].configure(command =clr)
button[14].configure(command =equ)
button[15].configure(command =lambda:show(data[15]))


root.mainloop()