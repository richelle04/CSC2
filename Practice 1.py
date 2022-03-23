#Practice 1
from tkinter import * # imports everything from TK - tki
from tkinter import ttk # ttk is a sub module if tkinter

root = Tk() # top level window

# Create a Label Widget (because modules are made up of widget)
label = Label(root, text="Hello Pyhton") # what you on screen

# font colour, config is for properties
label.config(text="Hello Python", fg="black")
label.config(bg="brown") # background colour
label.config(font="Times 20")

label.config(text="Python is a great program and we can do lots with it")
label.config(wraplength="150") # wrap text if long label
label.config(justify="right") # alignment - where will the text aligned

# Showing it on the screen
label.pack() 
root.geometry("300x250") #size of window

root.mainloop() # GUI is always looping (GUI - Graphical User Interface)
# when you run your mouse over and you can click on any buttons/labels
