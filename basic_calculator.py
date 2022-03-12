import tkinter

calc = tkinter.Tk()
calc.title("Calculator")
calc.geometry('280x280-8-200')
calc['padx'] = 8

#Number Inputs
def add_to_eq(x):
    global calc_value
    calc_value = calc_value + str(x)
    numeric_eq.set(calc_value)


def calculate_eq():
    total = str(eval(calc_value))
    numeric_eq.set(total)


def clear_input():
    global calc_value
    calc_value = ''
    numeric_eq.set('')


calc_value= ''
numeric_eq = tkinter.StringVar()
data_field = tkinter.Entry(calc, textvariable=numeric_eq)
data_field.grid(row=1, column=0, columnspan=4)

label = tkinter.Label(calc, text="Calculator")
label.grid(row=0, column=0, columnspan=4)


cButton = tkinter.Button(calc, text='C', command=clear_input)
cButton.grid(row=2, column=0)
ceButton = tkinter.Button(calc, text='CE', command=clear_input)
ceButton.grid(row=2, column=1)
button7 = tkinter.Button(calc, text='7', command=lambda: add_to_eq(7))
button7.grid(row=3, column=0)
button4 = tkinter.Button(calc, text='4', command=lambda: add_to_eq(4))
button4.grid(row=4, column=0)
button1 = tkinter.Button(calc, text='1', command=lambda: add_to_eq(1))
button1.grid(row=5, column=0)
button0 = tkinter.Button(calc, text='0', command=lambda: add_to_eq(0))
button0.grid(row=6, column=0)
button8 = tkinter.Button(calc, text='8', command=lambda: add_to_eq(8))
button8.grid(row=3, column=1)
button5 = tkinter.Button(calc, text='5', command=lambda: add_to_eq(5))
button5.grid(row=4, column=1)
button2 = tkinter.Button(calc, text='2', command=lambda: add_to_eq(2))
button2.grid(row=5, column=1)
equalButton = tkinter.Button(calc, text='=', width=7, command=calculate_eq)
equalButton.grid(row=6, column=1, columnspan=2)
button9 = tkinter.Button(calc, text='9', command=lambda: add_to_eq(9))
button9.grid(row=3, column=2)
button6 = tkinter.Button(calc, text='6', command=lambda: add_to_eq(6))
button6.grid(row=4, column=2)
button3 = tkinter.Button(calc, text='3', command=lambda: add_to_eq(3))
button3.grid(row=5, column=2)
plusButton = tkinter.Button(calc, text='+', command=lambda: add_to_eq('+'))
plusButton.grid(row=3, column=3)
minusButton = tkinter.Button(calc, text='-', command=lambda: add_to_eq('-'))
minusButton.grid(row=4, column=3)
starButton = tkinter.Button(calc, text='*', command=lambda: add_to_eq('*'))
starButton.grid(row=5, column=3)
divideButton = tkinter.Button(calc, text='/', command=lambda: add_to_eq('/'))
divideButton.grid(row=6, column=3)

cancelButton = tkinter.Button(calc, text='Cancel', command=calc.destroy)
cancelButton.grid(row=8, column=4)

calc.mainloop()