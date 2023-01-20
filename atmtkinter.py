from tkinter import *
root=Tk()
root.title("Atm")
root.configure(background ="black")
#button 1
root.geometry("800x720")
l1 =Label(root, text ="welcome In Our Atm Service",font =("Arial",30),bg ="black", fg  ="white")
l1.place(x =400,y =50)
b1 =Button(root,text ="balance inquary" ,bg ="black",fg ="white")
b1.place(x =200,y =250)
b2 =Button(root,text ="credit balance" ,bg ="black",fg ="white")
b2.place(x =600,y =250)

b3 =Button(root,text ="debit balance" ,bg ="black",fg ="white")
b3.place(x =600,y =550)
b4 =Button(root,text =" exit" ,bg ="black",fg ="white")
b4.place(x =200,y =550)


root.mainloop()