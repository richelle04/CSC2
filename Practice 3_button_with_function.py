from tkinter import * # imports everything form TK

root = Tk() # top level window
def callback():
    label.config(text="How are you",fg="red", bg="yellow")
# here I have added font colour and background
# colour on click

# Create label
label = Label(root, text = "I'm good, thank you")
label.pack()

# Create button (now with the command function)
button = Button(root, text="How are you",command=callback) 
button["state"]="disabled" # can disable the button
button["state"]="normal" # back to normal
button.pack()

root.geometry("350x300")
root.mainloop()