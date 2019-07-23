from tkinter import *
from tkinter import messagebox
 
def calc():
    
    str(num1)
    str(oper)
    str(num2)
    
    try:
        #addition
        if oper.get() == '+':
            try:
                value = float(num1.get()) + float(num2.get())
            except:
                messagebox.showerror("Addition Error!", ' + Something went wrong! Maybe invalid entries')
        
        #subtraction
        if oper.get() == '-':
            try:
                value = float(num1.get()) - float(num2.get())
            except:
                messagebox.showerror("Subtraction Error!", ' - Something went wrong! Maybe invalid entries')
        #multiplication
        if oper.get() == 'x' or oper.get() == '*':
            try:
                value = float(num1.get()) * float(num2.get())
            except:
                messagebox.showerror("Error!", ' * Something went wrong! Maybe invalid entries')
                
        #Division
        if oper.get() == '/':
            if num2.get() == '0':
                #checks if user is trying to divide by zero
                messagebox.showerror('Division Error!', 'second number = 0 No division possible')
            else:
                try:
                    value = float(num1.get()) / float(num2.get())
                except:
                    messagebox.showerror("Division Error!", ' / Something went wrong! Maybe invalid entries')
 
        # Answer
        answer = Label(win, text='{0} {1} {2}='.format(num1.get(), oper.get(), num2.get()))
        answer.grid(row=5, column= 0)
        answer2 = Label(win, text=value)
        answer2.grid(row=6, column= 1)
    except:
        messagebox.showwarning("Wrong Input!!!", '#    WRONG INPUT    PLEASE TRY AGAIN   :)    #')
 
 


 
#Modify window
win = Tk()
win.title('CALCULATOR 2')
win.geometry('340x160')


#window attributes below


 #for First Number

X = Label(win, text='Enter number 1 -->')
X.grid(row=0, column=0)

num1 = StringVar()
number1 = Entry(win, textvariable= num1)
number1.grid(row=0, column=1)



 #For the operator

Y = Label(win, text='Enter operator -->')
Y.grid(row=1, column=0,sticky=W)

oper = StringVar()
operator = Entry(win, textvariable= oper)
operator.grid(row=1, column=1)



 #For second Number

Z = Label(win, text='Enter number 2 -->')
Z.grid(row=2, column= 0)

num2 = StringVar()
number2 = Entry(win, textvariable = num2)
number2.grid(row=2, column=1)

 
#for Button CULCULATE

button = Button(win, text='Calculate', command = calc)
button.grid(row=4, column=1)
 
 
 
 
 
 
 
#start main loop
mainloop()
