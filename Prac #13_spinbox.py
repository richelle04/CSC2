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
        print(year.get())

# Create entry boxes
entry = ttk.Entry(root, width=30) # size of the field for entry
entry2 = ttk.Entry(root,width=30)
entry.insert(0, '') # 0 is the index - first character
entry2.insert(0, '')

# Add a button to the window
button=ttk.Button(root,text='Enter') # the difference in this exercise is that we are configuring our button with the callback function
button.config(command=callback) # with the callback function

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

# Checkbox
chvar=IntVar() # checkbox variable
chvar.set(0) # set to 0 (zero) - means not checked

# Checkbox variale
cbox=Checkbutton(root,text='Remember Me', variable=chvar, font='Arial 16').grid(row=4, column=0, sticky=E, columnspan=2) # in order to get it align right

# Create anotehr variable
gender=StringVar()

# Create radio button
# To get value from our radio button - in the callbacl function
ttk.Radiobutton(root, text='Female', value='Female', var=gender).grid(row=5, column=0)
ttk.Radiobutton(root, text='Male', value='Male', var=gender).grid(row=5, column=1)

# Create combobox where our first 

""""Create combobox where our first parameter will be root and the second will be textvariable(months) and use grid geometry
for the Combobox (where it will be on the window). When the application is run the combo box is empty need to create variables 
for our combo box which we will do now"""""

months = StringVar() # StringVar is my function
"""ComboBox = ttk.Combobox(root, textvariable=months, values=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'July', 'Aug', 'Sep', 
'Oct', 'Nov', 'Dec')).grid(row=6, column=0)"""

# There is a problem that when we run the program and click on a month we can actually write over it or delete it

ComboBox = ttk.Combobox(root, textvariable=months, values=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'July', 'Aug', 'Sep', 
'Oct', 'Nov', 'Dec'), state='readonly').grid(row=6, column=0)

# Create spinbox - 'from' is a special keyword for Python - so we need to use _ after it
year = StringVar()
# Spinbox(root,from_=1990, to=2022, textvariable=year).grid(row=6, column=1)
# Information below:
# Use grid geometry Manager to our window but we are unable to edit the values in the spinbox
Spinbox (root, from_=1990, to=2022, textvariable=year, state='readonly').grid(row=6, column=1)
# To get the value to print out when program is run, add a print statement in function 
# print(year,get())

root.geometry('500x450') # size of window
root.mainloop()
