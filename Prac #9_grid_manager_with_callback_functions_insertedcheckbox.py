from tkinter import * # imports everything from TK
from tkinter import ttk

root = Tk()

def callback():
    val1 = entry.get()
    val2 = entry2.get()
    print('Your Name is:' + val1)
    print('Your Password is:' + val2)

# Create entry boxes
entry = ttk.Entry(root, width=30) # size of the field for entry
entry2 = ttk.Entry(root,width=30)
entry.insert(0, 'Please enter your name:') # 0 is the index - first character

# Add a button to the window
button = ttk.Button(root, text='Enter')

# Add label title
lbltitle = ttk.Label(text='Our Title Goes Here', font=(('Arial'), 22))

lblname = ttk.Label(text='Your Name:')
lblpass = ttk.Label(text='Your Password:')
lbltitle.grid(row=0, column=0, columnspan=2)
lblname.grid(row=1, column=0, sticky=W)
lblpass.grid(row=2, column=0)
entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid(row=3, column=1, sticky=W+E, pady=5)

# checkbox
chvar = IntVar() # checkbox variable
chvar.set(0) # set to 0 (zero) - means not checked

# checkbox variable
cbox = Checkbutton(root, text='Remember me', variable=chvar, font='Arial 16').grid(row=4, column=0, sticky=E, columnspan=2) # in order to get align on the right

# sticky=E, columnspan=2 # in order to get it align right

root.geometry('500x450') # the size of the window
root.mainloop()
