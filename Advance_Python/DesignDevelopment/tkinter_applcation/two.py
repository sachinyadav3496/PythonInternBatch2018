from tkinter import * 
import pymysql as sql
from tkinter import messagebox

master = Tk()

f = Frame(master,bg='gray')
username = StringVar()
password = StringVar()

l1 = Label(f,text='UserName : ',bg='gray',font=('Times','30','bold'),fg='#123456')
l1.grid(row=0,column=0,ipadx=50)
e1 = Entry(f,textvariable=username,bg='gray',width=20,font=('Times','20','bold'),fg='#321654')
e1.grid(row=0,column=1,padx=30)

l2 = Label(f,text='Password : ',bg='gray',font=('Times','30','bold'),fg='#123456')
l2.grid(row=1,column=0,ipadx=50)
e2 = Entry(f,textvariable=password,show='*',bg='gray',width=20,font=('Times','20','bold'),fg='#321654')
e2.grid(row=1,column=1,padx=30)


def login():
    UserName = e1.get()
    Password = e2.get()
    print(UserName)
    print(Password)
    try :
        db = sql.connect('localhost','root','','pythoncgi')
        c = db.cursor()
        cmd = "select * from user where name = '{}'".format(UserName)
        c.execute(cmd)
        data = c.fetchone()
        if data : 
            if Password == data[1] : 
                messagebox.showinfo("Information","!!Khud bhi kuch karo sara main hi karoo yaha")
                
            else : 
                password.set('')
                messagebox.showerror("Error","!!Invalid Password")

        else : 
            messagebox.showerror("Error","!!No such user exists")
    except Exception as e : 
        print("Errorr something is wrong",e)
        messagebox.showerror("Error","!!Check Data BAse Connectivity {}".format(e))

b1 = Button(f,bg='gray',text='Login',font=('Times','20','bold'),command=login)
b1.grid(row=2,column=0)

f.pack(padx=50,pady=120,ipadx=50,ipady=50)

master.title('BANK Application')
master.wm_minsize(500,500)
master.mainloop()
