# Import necessary modules
from tkinter import*
import tkinter.messagebox as tmsg
import time
from math import*


# Define the function to get the button values
def getvals(event):
    value = event.widget.cget('text')  # Get the text on the button
    # If the button clicked is "clr", clear the screen
    if value == 'clr':
        sc_variable.set(' ')
    # If the button clicked is "=", evaluate the expression and display the result
    elif value == '=':
        try:
            sc_variable.set(eval(screen.get()))
            screen.update()
        # If there's an error in evaluating the expression, clear the screen
        except Exception as e:
            sc_variable.set(' ')
    # Otherwise, concatenate the button value to the current screen value
    else:
        sc_variable.set(f'{sc_variable.get()}{value}')


# Create the main window
root = Tk()
root.title("Calculator")
root.config(bg="#E5E4E2")
root.geometry("755x525+100+100")

# Define the screen widget to display the input and output
sc_variable = StringVar()
screen = Entry(root, textvariable=sc_variable, font=("Times New Roman", 20, "bold"), fg='black', bg='white', borderwidth=10, relief=SUNKEN, width=30)
screen.grid(row=0, column=0, columnspan=8, padx=10, pady=10)

# Define and display the calculator logo
logoImage = PhotoImage(file="photos//cal123.png")
logo = Label(root, image=logoImage, bg="#E5E4E2", highlightthickness=0)
logo.grid(row=0, column=0, padx=10, pady=10, sticky="ew")


# Define and display the calculator buttons
b1=Button(root,text='7',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b1.bind('<Button-1>',getvals)  # Bind the button to the getvals function
b1.grid(row=1, column=0,padx=2, pady=2)

b2=Button(root,text='8',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b2.bind('<Button-1>',getvals)
b2.grid(row=1, column=1,padx=2, pady=2)

b3=Button(root,text='9',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b3.bind('<Button-1>',getvals)
b3.grid(row=1, column=2,padx=2, pady=2)

b4=Button(root,text='*',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b4.bind('<Button-1>',getvals)
b4.grid(row=1, column=3,padx=2, pady=2)

b5=Button(root,text='sin',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b5.bind('<Button-1>',getvals)
b5.grid(row=1, column=4,padx=2, pady=2)

b6=Button(root,text='(',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b6.bind('<Button-1>',getvals)
b6.grid(row=1, column=5,padx=2, pady=2)



b7=Button(root,text='4',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b7.bind('<Button-1>',getvals)
b7.grid(row=2, column=0,padx=2, pady=2)

b8=Button(root,text='5',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b8.bind('<Button-1>',getvals)
b8.grid(row=2, column=1,padx=2, pady=2)

b9=Button(root,text='6',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b9.bind('<Button-1>',getvals)
b9.grid(row=2, column=2,padx=2, pady=2)

b10=Button(root,text='-',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b10.bind('<Button-1>',getvals)
b10.grid(row=2, column=3,padx=2, pady=2)

b11=Button(root,text='cos',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b11.bind('<Button-1>',getvals)
b11.grid(row=2, column=4,padx=2, pady=2)

b12=Button(root,text=')',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b12.bind('<Button-1>',getvals)
b12.grid(row=2, column=5,padx=2, pady=2)




b13=Button(root,text='1',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b13.bind('<Button-1>',getvals)
b13.grid(row=3, column=0,padx=2, pady=2)

b14=Button(root,text='2',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b14.bind('<Button-1>',getvals)
b14.grid(row=3, column=1,padx=2, pady=2)

b15=Button(root,text='3',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b15.bind('<Button-1>',getvals)
b15.grid(row=3, column=2,padx=2, pady=2)

b16=Button(root,text='+',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b16.bind('<Button-1>',getvals)
b16.grid(row=3, column=3,padx=2, pady=2)

b17=Button(root,text='tan',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b17.bind('<Button-1>',getvals)
b17.grid(row=3, column=4,padx=2, pady=2)

b18=Button(root,text='%',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b18.bind('<Button-1>',getvals)
b18.grid(row=3, column=5,padx=2, pady=2)




b19=Button(root,text='.',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b19.bind('<Button-1>',getvals)
b19.grid(row=4, column=0,padx=2, pady=2)

b20=Button(root,text='0',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b20.bind('<Button-1>',getvals)
b20.grid(row=4, column=1,padx=2, pady=2)

b21=Button(root,text='sinh',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b21.bind('<Button-1>',getvals)
b21.grid(row=4, column=2,padx=2, pady=2)

b22=Button(root,text='cosh',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b22.bind('<Button-1>',getvals)
b22.grid(row=4, column=3,padx=2, pady=2)

b23=Button(root,text='tanh',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b23.bind('<Button-1>',getvals)
b23.grid(row=4, column=4,padx=2, pady=2)

b24=Button(root,text='pi',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b24.bind('<Button-1>',getvals)
b24.grid(row=4, column=5,padx=2, pady=2)




b25=Button(root,text='log10',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b25.bind('<Button-1>',getvals)
b25.grid(row=5, column=0,padx=2, pady=2)

b26=Button(root,text='exp',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b26.bind('<Button-1>',getvals)
b26.grid(row=5, column=1,padx=2, pady=2)

b27=Button(root,text='/',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b27.bind('<Button-1>',getvals)
b27.grid(row=5, column=2,padx=2, pady=2)

b28=Button(root,text='clr',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b28.bind('<Button-1>',getvals)
b28.grid(row=5, column=3,padx=2, pady=2)

b29=Button(root,text='log',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b29.bind('<Button-1>',getvals)
b29.grid(row=5, column=4,padx=2, pady=2)

b30=Button(root,text='=',font=("Times New Roman", 20, "bold"), borderwidth=2, fg='white', bg='black', width=7, height=2, relief=SUNKEN)
b30.bind('<Button-1>',getvals)
b30.grid(row=5, column=5,padx=2, pady=2)

# Starting the main event loop
root.mainloop()
