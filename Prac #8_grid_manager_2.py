# This program shows Grid Manager - which helps us to organise our widgets easily
# Formatting out title, label and button placements
from tkinter import *
from tkinter import ttk

root = Tk()

# create entires
entry = ttk.Entry(root,width=30)
entry2 = ttk.Entry(root,width=30)

#create placeholder
entry.insert(0, 'Please enter your name')
entry2.insert(0, 'Please enter you password')

# create button and labels
# where do we want it - in root and the text
button = ttk.Button(root, text='Enter')
lbltitle = ttk.Label(text='Our Title Here', font=(('Arial'), 30))
lblname = ttk.Label(text='Your Name:')
lblpass = ttk.Label(text='Your Password:')

# position of the buttons, labels and entries as outcome by using geometry manager for grid
# move title to the 2nd column
lbltitle.grid(row=0, column=0, columnspan=2, pady=10)
lblname.grid(row=1, column=0, sticky=W) # W - left
lblpass.grid(row=2, column=0)

entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
# button.grid(row=3, column=1, sticky=E) # E+W spans it across the cell in that column
# button.grid(row=3, column=1, sticky=E) # will have the button on the right
# button.grid(row=3, column=1, sticky=W) # will put button on left side
#gives you a  bit of a gap between two rows 
button.grid(row=3, column=1, sticky=E, pady=5)

root.geometry('500x450')
root.mainloop()