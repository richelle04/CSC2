from tkinter import * # imports everything from tkinter

root = Tk() # top level window

# Create label
label = Label(root, text="Hello Python")
label.pack()

#Create button (without command does not do anything)
button = Button(root, text="Click Me!")
button.pack()

root.geometry("350x300")
root.mainloop() # this is always at the end of the code