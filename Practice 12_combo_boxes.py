from curses import window
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
        # this is where to get our gender value to show when we run the program
        print('Gender is:' +gender.get())
        print(months.get())

# create entry boxes
entry = ttk.Entry(root, width=30) # size of the field for entry
entry2 = ttk.Entry(root,width=30)
entry.insert(0, 'Please enter you name') # 0 is the index - first character
entry2.insert(0, 'Please enter you password')

# add a button to the window
button=ttk.Button(root,text='Enter') # the difference in this exercise is that we are configuring our button with the callback function
button.config(command=callback) # with the callback function

# add label title
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
chvar=IntVar() # checkbox variable
chvar.set(0) # set to 0 (zero) - means not checked

# checkbox variale
cbox=Checkbutton(root,text='Remember Me', variable=chvar, font='Arial 16').grid(row=4, column=0, sticky=E, columnspan=2) # in order to get it align right

#create anotehr variable
gender=StringVar()

# create radio button
# to get value from our radio button - in the callbacl function
ttk.Radiobutton(root, text='Female', value='Female', var=gender).grid(row=5, column=0)
ttk.Radiobutton(root, text='Male', value='Male', var=gender).grid(row=5, column=1)

# Create combobox where our first 

""""Create combobox where our first parameter will be root and the second will be textvariable(months) and use grid geometry
for the Combobox (where it will be on the window). When the application is run the combo box is empty need to create variables 
for our combo box which we will do now"""""

months = StringVar() # StringVar is my function
"""ComboBox = ttk.Combobox(root, textvariable=months, values=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'July', 'Aug', 'Sep', 
'Oct', 'Nov', 'Dec')).grid(row=6, column=0)"""

# there is a problem that when we run the program and click on a month we can actually write over it or delete it

comboBox = ttk.Combobox(root, textvariable=months, values=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'July', 'Aug', 'Sep', 
'Oct', 'Nov', 'Dec'), state='readonly').grid(row=6, column=0)

root.geometry('500x450') # size of window
root.mainloop()
