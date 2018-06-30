import tkinter as tk

root = tk.Tk()

def take_value():
    x = eval(e.get())
    print(x)
    l2 = tk.Label(root,text=x)
    l2.pack()

root.title('MyApp')
root.wm_minsize(500,500)

f1 = tk.Frame(root)
value1 = tk.StringVar()
l = tk.Label(f1,text='Name : ',font=50)
l.grid(row=0,column=0,columnspan=3)
e = tk.Entry(f1)
e.grid(row=0,column=3,columnspan=5)
b = tk.Button(f1,text='submit',command=take_value,font=50)
b.grid(row=3,column=2,columnspan=5)

f1.pack()

root.mainloop()