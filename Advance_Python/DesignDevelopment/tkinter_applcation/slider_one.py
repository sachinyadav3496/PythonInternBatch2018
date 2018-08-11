from tkinter import * 

master = Tk()

def show():
    print(w.get())
    print(w1.get())
w = Scale(master,from_=0,to=42)
w.pack()

w1 = Scale(master,from_=0,to=200,orient=HORIZONTAL)
w1.pack()
b = Button(master,text='show',command=show)
b.pack()
mainloop()
