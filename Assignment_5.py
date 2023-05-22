#Menu bar assignment 
from tkinter import *

#Creating tkinter window
root=Tk()
root.title("Menu Bar Assignment")
root.geometry("600x400")

#This creates a Menu widget called as menubar - this menubar is added to root window we create 
menubar=Menu(root)

#Adding file menu and commands for it

#Another Menu widget is created which is added to menubar
#Tearoff option equals to zero prevents user from detaching the menu from menubar
filemenu=Menu(menubar,tearoff=0)
#This menu is added as submenu to menubar

#This line adds "filemenu" widget as cascade of menubar widget - All other options from filemenu will
#get added to it as waterfall of cascade
menubar.add_cascade(label="File",menu=filemenu)

#Now in that filemenu add following options in to that cascade
filemenu.add_command(label="New",command=None)
filemenu.add_command(label="Open",command=None)
filemenu.add_command(label="Save",command=None)
filemenu.add_command(label="Save as",command=None)

#This line creates a grey seperator line between options
filemenu.add_separator()
filemenu.add_command(label="Close",command=root.destroy)

#Adding edit menu & commands
editmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut",command=None)
editmenu.add_command(label="Copy",command=None)
editmenu.add_command(label="Paste",command=None)
editmenu.add_command(label="Select All",command=None)
editmenu.add_separator()
editmenu.add_command(label="Find",command=None)
editmenu.add_command(label="Find again",command=None)

#Adding help menu
helpmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = helpmenu)
helpmenu.add_command(label ='Linux Help', command = None)
helpmenu.add_command(label ='Demo', command = None)
helpmenu.add_separator()
helpmenu.add_command(label ='About Us', command = None)

root.config(menu=menubar)
root.mainloop()


