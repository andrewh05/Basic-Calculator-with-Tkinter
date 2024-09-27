from tkinter import *

win = Tk()
win.title('Basic calculator')
win.geometry('200x150')

total = 0

v1 = StringVar()

def add():
    global total
    num = int(v1.get())
    total += num
    lb2.config(text= total)
    v1.set("")

def min():
    global total
    num = int(v1.get())
    total -= num
    lb2.config(text= total)
    v1.set("")

def tim():
    global total
    num = int(v1.get())
    total *= num
    lb2.config(text= total)
    v1.set("")

def div():
    global total
    num = float(v1.get())
    total = total/num
    lb2.config(text= total)
    v1.set("")

def reset():
    global total
    v1.set("")
    total = 0
    lb2.config(text = total)


lb1 = Label(win, text="Total: ", font=('Arial', 10))
lb2 = Label(win, text=total, font=('Arial', 10))

e1 = Entry(win, textvariable=v1)

bt1 = Button(win, text="+", width=3, height=1, command=add)
bt2 = Button(win, text="-", width=3, height=1, command=min)
bt3 = Button(win, text="*", width=3, height=1, command=tim)
bt4 = Button(win, text="/", width=3, height=1, command=div)
bt5 = Button(win, text="Reset", width=4, height=3, command=reset)

lb1.place(x=20, y=20)
lb2.place(x=80, y=20)
e1.place(x=20, y=60)
bt1.place(x=20, y=90)
bt2.place(x=60, y=90)
bt3.place(x=20, y=120)
bt4.place(x=60, y=120)
bt5.place(x=100, y=90)

win.mainloop()
