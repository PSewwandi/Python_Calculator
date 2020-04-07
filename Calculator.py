from tkinter import *

expression = ""

def input_expression(number,equation):
    global expression
    expression = expression + str(number)
    equation.set(expression)

def clear_expresion(equation):
    global expression
    expression = ""
    equation.set("Enter the expression")
    
def evaluate(equation):
    global expression
    try:
        expression = str(eval(expression))
        equation.set(expression)
    except:
        equation.set("Enter a valid expression")
        expression = ""

def main():
    window = Tk()
    window.title("Calculator")
    window.geometry("385x295")
    window.configure(bg="dark slate gray")
    equation = StringVar()
    input_field = Entry(window,textvariable = equation )
    input_field.grid(columnspan=5,row=0,column=1,padx=50,ipadx=80,ipady=10,pady=10)
    equation.set("Enter the expression")

    _1 = Button(window, text='1', fg='white', bg='black', bd=0,borderwidth = 3, command=lambda: input_expression(1, equation), height=3, width=12)
    _1.grid(row=1, column=1)
    _2 = Button(window, text='2', fg='white', bg='black', bd=0,borderwidth = 3, command=lambda: input_expression(2, equation), height=3, width=12)
    _2.grid(row=1, column=2)
    _3 = Button(window, text='3', fg='white', bg='black', bd=0,borderwidth = 3, command=lambda: input_expression(3, equation), height=3, width=12)
    _3.grid(row=1, column=3)
    _4 = Button(window, text='4', fg='white', bg='black', bd=0,borderwidth = 3, command=lambda: input_expression(4, equation), height=3, width=12)
    _4.grid(row=2, column=1)
    _5 = Button(window, text='5', fg='white', bg='black', bd=0,borderwidth = 3, command=lambda: input_expression(5, equation), height=3, width=12)
    _5.grid(row=2, column=2)
    _6 = Button(window, text='6', fg='white', bg='black', bd=0,borderwidth = 3, command=lambda: input_expression(6, equation), height=3, width=12)
    _6.grid(row=2, column=3)
    _7 = Button(window, text='7', fg='white', bg='black', bd=0,borderwidth = 3, command=lambda: input_expression(7, equation), height=3, width=12)
    _7.grid(row=3, column=1)
    _8 = Button(window, text='8', fg='white', bg='black', bd=0,borderwidth = 3, command=lambda: input_expression(8, equation), height=3, width=12)
    _8.grid(row=3, column=2)
    _9 = Button(window, text='9', fg='white', bg='black', bd=0,borderwidth = 3, command=lambda: input_expression(9, equation), height=3, width=12)
    _9.grid(row=3, column=3)
    _0 = Button(window, text='0', fg='white', bg='black', bd=0,borderwidth = 3, command=lambda: input_expression(0, equation), height=3, width=12)
    _0.grid(row=4, column=1)
    plus = Button(window, text='+', fg='white', bg='black', bd=0,borderwidth = 3, command=lambda: input_expression('+', equation), height=3, width=12)
    plus.grid(row=1, column=4)
    minus = Button(window, text='-', fg='white', bg='black', bd=0,borderwidth = 3, command=lambda: input_expression('-', equation), height=3, width=12)
    minus.grid(row=2, column=4)
    multiply = Button(window, text='*', fg='white', bg='black', bd=0,borderwidth = 3, command=lambda: input_expression('*', equation), height=3, width=12)
    multiply.grid(row=3, column=4)
    divide = Button(window, text='/', fg='white', bg='black', bd=0,borderwidth = 3, command=lambda: input_expression('/', equation), height=3, width=12)
    divide.grid(row=4, column=4)
    equal = Button(window, text='=', fg='white', bg='black', bd=0,borderwidth = 3, command=lambda: evaluate(equation), height=3, width=12)
    equal.grid(row=4, column=3)
    clear = Button(window, text='Clear', fg='white', bg='black', bd=0,borderwidth = 3, command=lambda: clear_expresion(equation), height=3, width=12)
    clear.grid(row=4, column=2)
    window.mainloop()

if __name__ == '__main__':
    main()
    
