from tkinter import * # imports everything form TK
from tkinter import ttk # sub moduel of tkinter with more widgets

root = Tk()
def callback():
    val1=entry.get()
    val2=entry2.get()
    print("Your Name is :" +val1)
    print("Your Password is:" + val2)

# Create entry boxes
entry = ttk.Entry(root, width=30) # size of the field for entry
entry2 = ttk.Entry(root, width=30) 
entry.insert(0,"Please enter your name") # 0 is the index - first character
entry2.config(show="*") # this will hide the password or the text entered

# Add a button to the window
button=ttk.Button(root, text="Click ME!", command=callback) # when you put in a command you need to write a function under root

