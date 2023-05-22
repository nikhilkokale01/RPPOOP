#This widget implements a displaybox where we can place text or images
#Text diplayed using it can be updated at any time

from tkinter import *

#Creating a tkinter window
root=Tk()
root.geometry('900x500')

#StringVar() is a class with default value "" 
str1=StringVar()
str2=StringVar()
#We created instance of that class so that we can modify its value afterwards


lbl=Label(root,textvariable=str1,relief=RAISED,bg='orange',bd=3,padx=15,pady=20,cursor=DOTBOX)
#relied specifies the appearance of decorative border , default is flat 
lbl2=Label(root,textvariable=str2,relief=RAISED,bg='grey',bd=3,padx=15,pady=20,cursor=DOTBOX)


#Using set func we have modified the default value of StringVar's str object
str1.set("This is Label 1")
str2.set("This is Label 2")

#Pack the labels
lbl.pack()
lbl2.pack()

root.mainloop()