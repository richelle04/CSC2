'''In this progam we will create a message box'''

# From msilib .schema import Icon
from tkinter import *
from tkinter import ttk
from tkinter import messagebox  # If we do not import we cannot use message box for ou application

root = Tk()

# Creating callback1
def callback():
    # First parameter will be title and then the text
    mbox = messagebox.askquestion('Delete', 'Are your sure?', icon='warning') # Can change icon by wadding icon='warning')
    if mbox == 'yes': # If its a yes it means its checked and delete it - do '=='      # If its a no - do '!='
        print('Deleted')
    else:
        print('Not Deleted')

# Creating callback2
def callback2():
    messagebox.showinfo('Success', 'Well Done!')
    print('You clicked OK!')

# Creating button
button1 = ttk.Button(root, text='Delete', command=callback).grid(row=0, column=0) # Command will be definition name but need function 
button2 = ttk.Button(root, text='Info', command=callback2).grid(row=0, column=1) # Cannot run without function

root.geometry('350x250') # Size of the window
root.mainloop()