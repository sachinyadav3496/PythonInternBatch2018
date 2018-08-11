
from tkinter import *

def show_values():
        print (w1.get(), w2.get())

master = Tk()
w1 = Scale(master, from_=0, to=42,tickinterval=8,length=300)
w1.pack()
w2 = Scale(master, from_=0, to=200,tickinterval=10, orient=HORIZONTAL,length=600)
w2.pack()
w1.set(20)
w2.set(50)

Button(master, text='Show', command=show_values).pack()

mainloop()


