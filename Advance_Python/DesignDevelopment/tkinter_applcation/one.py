from tkinter import * 


root = Tk()

f1 = Frame(root)

l1 = Label(f1,text="Hello world I am frame 1")
b1 = Button(f1,text='Exit',command=f1.destroy)

l1.pack()
b1.pack()


b2 = Button(root,text='EXIT MAIN',command=root.destroy)

f1.grid(row=0,rowspan=10,columnspan=10)
b2.grid(row=11,rowspan=3,columnspan=5)

s1 = Scale(f1,from_=0,to=100)
s2 = Scale(f1,from_=0,to=200,orient=HORIZONTAL)

s1.pack()
s2.pack()

def show():
    print("Slider 1 value = ",s1.get())
    print("slider 2 value = ",s2.get())
b = Button(f1,text='Show Values',command=show)
s1.set(50)
s2.set(100)
b.pack()
v = StringVar()
l3 = Label(f1,text='Name : ')
l3.pack()
e1 = Entry(f1,textvariable=v)
e1.pack()
def submit():
    print(e1.get())
    r = eval(e1.get())
    print("Result = ",eval(e1.get()))
    v.set(r)

b4 = Button(f1,text='Submit',command=submit)
b4.pack()

root.title('myapplication')
root.wm_minsize(500,500)

root.mainloop()

