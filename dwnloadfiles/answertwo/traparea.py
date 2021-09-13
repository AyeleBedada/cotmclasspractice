#computes area of a trapezium
from tkinter import *

def calculate():
    b1=float(entry_b1.get())
    b2=float(entry_b2.get())
    h= float(entry_h.get())
    A =0.5*(b1+b2)*h
    output_label_A.configure(text='Area of the trapezium is: {}'.format(A))

root = Tk()
root.title("EIABC_Salary")

inquiry_label_b1 = Label(text='Enter length of base one(b1):', font=('Broadway', 16), fg='black')
inquiry_label_b1.grid(row=0, column=0)
entry_b1 = Entry(font=('Tekton Pro', 16), width=4)
entry_b1.insert(0, '?!')
entry_b1.grid(row=0, column=1)

inquiry_label_b2 = Label(text='Enter length of base two(b2):', font=('Broadway', 16), fg='black')
inquiry_label_b2.grid(row=1, column=0)
entry_b2 = Entry(font=('Tekton Pro', 16), width=4)
entry_b2.insert(0, '?!')
entry_b2.grid(row=1, column=1)

inquiry_label_h = Label(text='Enter height of trapezium(h):', font=('Broadway', 16), fg='black')
inquiry_label_h.grid(row=2, column=0)
entry_h = Entry(font=('Tekton Pro', 16), width=4)
entry_h.insert(0, '?!')
entry_h.grid(row=2, column=1)

eval_button_A = Button(text='Evaluate', font=('Verdana', 16), command=calculate)
eval_button_A.grid(row=0, column=2)


output_label_A = Label(font=('Bauhaus 93', 16), fg='red')
output_label_A.grid(row=0, column=3)




mainloop()
