from tkinter import * # imports everything from TK
from tkinter import ttk

root = Tk()

def callback(): # callback function 
    print('Your Name is:' +entry.get())
    print('Your Password is:' + entry2.get())
    if chvar.get()==1: # means the checkbox is checked
        print('Remember me selected')
    else: 
        print('not selected')

# Create entry boxes
entry = ttk.Entry(root, width=30) # size of the field for entry
entry2 = ttk.Entry(root,width=30)
entry.insert(0, 'Please enter you name') # 0 is the index - first character
entry2.insert(0, 'Please enter you password')

# Add a button to the window
button=ttk.Button(root,text='Enter') # the difference in this exercise is that we are configuring our button with the callback function
button.config(command=callback) # with the callback function

# Add label title
lbltitle = ttk.Label(text='Your Name')

lblname = ttk.Label(text='Your Name:')
lblpass = ttk.Label(text='Your Password:')
lbltitle.grid(row=0, column=0, columnspan=2)
lblname.grid(row=1, column=0, sticky=W)
lblpass.grid(row=2, column=0)
entry.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid(row=3, column=1, sticky=W+E, pady=5)

# Checkbox
chvar=IntVar() # checkbox variable
chvar.set(0) # set to 0 (zero) - means not checked

# Checkbox
cbox=Checkbutton(root,text='Remember Me', variable=chvar, font='Arial 16').grid(row=4, column=0, sticky=E, columnspan=2) # in order to get it align right

root.geometry('500x450') # the size of the window
root.mainloop()


