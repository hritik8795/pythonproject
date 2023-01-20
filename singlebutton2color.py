from tkinter import *
root =Tk()
root.geometry("500x500")
root.resizable(0,0)

b1 =Button(root,text ="click!",font =("Arial",25))
b1.bind("<Button>",lambda e:root.configure(background ="blue"))
b1.bind("<ButtonRelease>",lambda e:root.configure(background ="black"))
b1.bind("<1>",lambda e:root.configure(background ="cyan"))
b1.bind("<a>",lambda e:root.configure(background ="black"))

b1.pack()
root.mainloop()