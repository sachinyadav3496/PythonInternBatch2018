import os
def hello():
    print("1.read\n2.write")
    ch = int(input("Choice : "))

    if ch == 1 :
        f = input("ENter file full path :")
        if os.access(f,os.F_OK) and os.access(f,os.R_OK) :
            f = open(f)
            data = f.read()
            f.close()
            print("Here is your data ")
            print(data)
        else :
            print("Either Path invalid or Permission Error")
            print("Try again ")
        hello()
    elif ch == 2 :
            f = input("Enter full path to file : ")
            f = open(f,'w')
            print("Type :wq to save file \n\n")
            while True :
                d = input()
                if d.lower() == ':wq' :
                    f.close()
                    break
                f.write(d)
                f.write('\n')

    else :
        print("Error Invalid Choice ")
        hello()

if __name__ == "__main__" :
    hello()
