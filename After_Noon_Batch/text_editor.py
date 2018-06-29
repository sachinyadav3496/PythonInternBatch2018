import sys
import os
import shutil
import time
def menu():
    os.system('cls')
    print("\n\n1. Open a file\n2. Create New File\n3Append a File\n4. Copy file\n5. Delete File \n6. Move File \n7. CWD \n8.Exit \n")
    ch = int(input("Your Choice : "))
    print("Processing your choice...........")
    time.sleep(2)
    if ch == 1  :
        read()
    elif ch == 2 :
        create()
    elif ch == 3 :
        append()
    elif ch == 4 :
        copy()
    elif ch == 5 :
        delete()
    elif ch == 6 :
        move()
    elif ch == 7 :
        cwd()
    elif ch == 8 :
        print("\n\nThanks for using our services \n")
        print("Exiting ......")
        time.sleep(2)
        print("\n\n")
        sys.exit(0)
    menu()

def create():
    os.system('cls')
    print("\n\n\nWelcome to Write service ")
    path = input("\n\nEnter your path : ")
    if os.path.exists(path) and os.access(path,os.W_OK) :
        filename = input("\nEnter file name : ")
        print("\nWrite your data and press :wq when ever you want save and exit text edior ")
        os.system('cls')
        print("\n\n\n\n")
        fname = os.path.join(path,filename)
        f = open(fname,'w')
        while True :
            data = input()
            if data.strip().lower() == ':wq' :
                f.close()
                os.system('cls')
                print("\n\n\n\nYour file Saved Sucess fully \n\n")
                time.sleep(1)
                print("\t\t\t\t.....Redirecting.....\t\t\t")
                time.sleep(2)
                menu()
            f.write(data)
            f.write('\n')
    else :
        print("\nNo such Directory Exists\n")
        print("Please Enter a Valid Path\n\n")
        create()



def read():
    os.system('cls')
    print("Welcome to File Read Section")
    print()
    name = input("\nFull path to your file : ")
    os.system('cls')
    print("\n\n\n\n")
    if os.path.exists(name) :
        if os.path.isfile(name) and os.access(name,os.R_OK) :
            fp = open(name)
            data = fp.read()
            fp.close()
            print("\nHere is your file\n\n")
            print(data)
            print("\n\n\n")
            input("Press something to redirect")
            print("Wait....")
            time.sleep(2)
            menu()

    else :
        print("\n\nInvalid File Make sure your path is correct ")
        print("Redirecting to main menu ")
        time.sleep(2)
        os.system('cls')
        menu()
    

menu()
