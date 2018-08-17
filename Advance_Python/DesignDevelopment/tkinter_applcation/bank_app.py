from tkinter import * 
import tkinter as tk
import pymysql as sql
from tkinter import messagebox


class Bank:
    def __init__(self,master):
        self.master = master()
        self.master.title('BANK Application')
        self.master.wm_minsize(500,500)
        self.menu_forget = False
    def run(self):
        self.main_frame()
    def menu(self):
        self.menu = tk.Frame(self.master)
        self.m_b1 = tk.Button(self.menu,text='Hello World',command=self.show_f)
        self.m_b1.pack()
        self.menu.grid()
    def show_f(self):
        self.menu.grid_forget()
        self.menu_forget = True
        self.f.grid()
    def main_frame(self):

        self.f = Frame(self.master,bg='gray')
        Bank.username = StringVar()
        Bank.password = StringVar()

        self.l1 = Label(self.f,text='UserName : ',bg='gray',font=('Times','30','bold'),fg='#123456')
        self.l1.grid(row=0,column=0,ipadx=50,pady=50)
        self.e1 = Entry(self.f,textvariable=Bank.username,bg='#123456',width=20,font=('Times','20','bold'),fg='#FFFFFF')
        self.e1.grid(row=0,column=1,padx=30,pady=50)

        self.l2 = Label(self.f,text='Password : ',bg='gray',font=('Times','30','bold'),fg='#123456')
        self.l2.grid(row=1,column=0,ipadx=50)
        self.e2 = Entry(self.f,textvariable=Bank.password,show='*',bg='#123456',width=20,font=('Times','20','bold'),fg='#FFFFFF')
        self.e2.grid(row=1,column=1,padx=30)
        self.b1 = Button(self.f,bg='gray',text='LOGIN',font=('Times','20','bold'),command=self.login,fg='#123456')
        self.master.bind('<Return>',self.login)
        self.b1.grid(row=2,column=0,columnspan=4,padx=70,pady=50)
        self.f.grid(padx=50,pady=120,ipadx=50,ipady=50)



    def login(self,event=None):
        UserName = self.e1.get()
        Password = self.e2.get()
        print(UserName)
        print(Password)
        try :
            db = sql.connect('localhost','root','','bank')
            c = db.cursor()
            cmd = "select * from user where name = '{}'".format(UserName)
            c.execute(cmd)
            data = c.fetchone()
            self.password.set('')
            if data : 
                if Password == data[2] : 
                    self.f.grid_forget()
                    #messagebox.showinfo("Information","!!Khud bhi kuch karo sara main hi karoo yaha")
                    if self.menu_forget : 
                        self.menu.grid()
                    else :

                        self.menu()
                
                else : 
                    messagebox.showerror("Error","!!Invalid Password")

            else : 
                messagebox.showerror("Error","!!No such user exists")
                Bank.username.set('')
        except Exception as e : 
            print("Errorr something is wrong",e)
            messagebox.showerror("Error","!!Check Data BAse Connectivity {}".format(e))




root = Bank(Tk)
root.run()
mainloop()

