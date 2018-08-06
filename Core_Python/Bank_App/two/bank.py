from getpass import getpass
import json
import time
def logupdate(s):
    """to update logs time to time"""
    t = time.ctime()
    f = open('log.db','a')
    f.write(s+' on '+t)
    f.close()
with open('bank.db') as fp:
    """ reading file for data"""
    bank = json.load(fp)
    fp.close()
    s = "\nBank Application Started"
    logupdate(s)


def update():
    """used to write data in file """
    fp = open('bank.db','w')
    json.dump(bank,fp)
    fp.close()

# In[2]:


def profile(i):
    print("Welcome {} ".format(bank['user'][i]).center(200,'*'))
    print("\n1.Update Name ")
    print("2.Update Password")
    print("3.Delete Account")
    print("4.Logout")
    ch = int(input("Choice : "))
    if ch == 1 : 
        name = input("Ener new name : ")
        bank['user'][i] = name
        update()
        choice(i)
    elif ch == 2 : 
        cp = getpass("Enter current Passsword : ")
        if cp == bank['passwd'][i] :
            np = getpass("Ener New Password : ")
            vp = getpass("Confirm Password : ")
            if np == vp :
                bank['passwd'][i] = np
                update()
                print("Password Sucessfully Updated")
                main()
            else :
                print("Password didn't Match ")
                print("Try Again")
                profile(i)
        else :
            print("Password Incorrect ")
            main()
    elif ch == 3 : 
        bank['user'].pop(i)
        bank['acc'].pop(i)
        bank['bal'].pop(i)
        bank['passwd'].pop(i)
        update()
        print("Bye Bye ")
        print("Your account Sucessfully Deleted")
        main()


# In[10]:


def chk_bal(i):
    print("Name = ",bank['user'][i])
    print("Acc Number = ",bank['acc'][i])
    print("Balance = ",bank['bal'][i])
    choice(i)


# In[4]:


def credit(i):
    global bank
    print("\n\nWelcome to Credit Services  ".center(200,'*'))
    amount = int(input("Enter amount to deposite : "))
    bank['bal'][i] += amount
    update()
    print("Now you have {} rs in your account\n{} credited sucessfully in your account".format(bank['bal'][i],amount))
    choice(i)


# In[5]:


def debit(i):
    global bank
    print("\n\nWelcome Debit Services ".center(200,'*'))
    amount = int(input("Enter amount to be withdraw : "))
    if amount > bank['bal'][i] :
        
        print("Insufficient Balance\nyou have only {} rs in your account".format(bank['bal'][i]))
        print("\nTry Again ")
        debit(i)
    else :
        bank['bal'][i] -= amount 
        update()
        print("You have withdrawn {} rs and you have left {} in your account.".format(amount,bank['bal'][i]))
        choice(i)


# In[6]:


def choice(i):
    print("Welcome back {}".format(bank['user'][i]).center(200,'*'))
    print("\n\nMenu\n")
    print("1.Debit\n2.Credit\n3.Statement\n4.Profile Update\n5.Logout")
    ch = int(input("Enter your Choice : "))
    if ch == 1 :
        debit(i)
    elif ch == 2 :
        credit(i)
    elif ch == 3 :
        chk_bal(i)
    elif ch == 4 :
        profile(i)
    elif ch == 5 :
        main()
    else :
        print("Error: Invalid Choice\nTry Again")
        choice(i)
    


# In[7]:


def login():
    print("Welcome to Login Facility".center(200,"*"))
    print("\n\n")
    acc_no = int(input("Login ID : "))
    password = getpass("Password :")
    if acc_no in bank['acc'] : 
        i = bank['acc'].index(acc_no) 
        s = '{} is trying to login into account'.format(bank['user'][i])
        logupdate(s)
        if password == bank['passwd'][i] :
            s = 'User {} sucessfully logged in into Account no '.format(bank['user'][i],acc_no)
            logupdate(s)
            choice(i)
        else :
            print("\n\nError Wrong Password Try Again : ")
            s = 'Login attempt failed due to incorrect password of user {} with acc no {} '.format(bank['user'][i],acc_no)
            logupdate(s)
            login()
    else :
        print("\n\nNo such Account Exist\nYou Should Signup\n\n")
        s = 'An Unauthorized Acess Detected '
        logupdate(s)
        main()


# In[ ]:


def signup():
    name = input("Enter name : ")
    bal = int(input("Enter initial amount : "))
    passwd = getpass("Enter Password : ")
    acc = bank['acc'][-1] + 1
    bank['user'].append(name)
    bank['bal'].append(bal)
    bank['acc'].append(acc)
    bank['passwd'].append(passwd)
    update()
    print("Note down your account number : {} ".format(acc))
    print("Thanks for opening an account ")
    main()
    


# In[8]:


def main():
    print("Welcome to Bank Program".center(200,'*'))
    print("Menu")
    print("1.Login\n2.SignUp\n3.Exit")
    ch = int(input("Enter your Choice : "))
    if ch == 1 : 
        login()
    elif ch == 2 :
        signup()
    elif ch == 3 :
        s = '\nBank Application Closed '
        logupdate(s)
        exit(0)
    else :
        print("\n\nInvalid Input\nTry Again")
        main()


# In[9]:


if __name__ == "__main__" : 
    
    main()

