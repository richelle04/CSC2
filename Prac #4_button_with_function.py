from tkinter import * # imports everything form TK

root = Tk() # top level window
def callback():
    label.config(text="You clicked Me!",fg="red", bg="yellow")
# here I have added font colour and background
# colour on click

# Create label
label = Label(root, text = "Hello Python")
label.pack()

# Create button (now with the command function)
button = Button(root, text="Click Me!",command=callback) 
button["state"]="disabled" # can disable the button
button["state"]="normal" # back to normal
button.pack()

root.geometry("350x300")
root.mainloop()