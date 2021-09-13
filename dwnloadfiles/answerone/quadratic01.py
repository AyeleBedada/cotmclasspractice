#computes quadratic equation solution y=(a*(x**2))+(b*x)+c

from tkinter import *

def bool():


    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())
    i = (b ** 2) - (4 * a * c)


    if i >= 0 :
        x1= ((-1*b)+((b**2)-(4*a*c))**0.5)/(2*a)
        x2= ((-1*b)-((b**2)-(4*a*c))**0.5)/(2*a)
    else:
        x1="null"
        x2="null"

    output_label_x1.configure(text='solution of x1 is: {}'.format(x1))
    output_label_x2.configure(text='solution of x2 is: {}'.format(x2))

root = Tk()
root.title("EIABC_quadratic equation")

inquiry_label_a = Label(text='Enter value of a:', font=('Broadway', 16), fg='black')
inquiry_label_a.grid(row=0, column=0)

entry_a = Entry(font=('Tekton Pro', 16), width=9)
entry_a.grid(row=0, column=1)
entry_a.insert(0, '?!')

inquiry_label_b = Label(text='Enter value of b:', font=('Broadway', 16), fg='black')
inquiry_label_b.grid(row=1, column=0)

entry_b = Entry(font=('Tekton Pro', 16), width=9)
entry_b.grid(row=1, column=1)
entry_b.insert(0, '?!')

inquiry_label_c = Label(text='Enter value of c:', font=('Broadway', 16), fg='black')
inquiry_label_c.grid(row=2, column=0)

entry_c = Entry(font=('Tekton Pro', 16), width=9)
entry_c.grid(row=2, column=1)
entry_c.insert(0, '?!')

eval_button = Button(text='Evaluate', font=('Verdana', 16), command=bool )
eval_button.grid(row=0, column=3)

output_label_x1 = Label(font=('Bauhaus 93', 16), fg='red')
output_label_x1.grid(row=0, column=4)
output_label_x2 = Label(font=('Bauhaus 93', 16), fg='red')
output_label_x2.grid(row=1, column=4)

mainloop()