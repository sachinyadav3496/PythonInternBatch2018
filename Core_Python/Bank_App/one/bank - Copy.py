import getpass
import time
bank = { 
        'name' : [ 'john', 'hari','jadu' ],
        'acc' : [ 1001,  1002 , 1003 ],
        'bal' : [ 10000,20000,30000 ],
        'password' : [ 'abcd','xyz','redhat' ]

        }

while input("\n\n\nPress A key to continue : ") :

    print("\n\n1.Login\n2.Signup\n")
    ch = int(input("your Choice : "))
    print("\n********Processing******\n")
    time.sleep(2)

    if ch == 1 :
        acc = int(input("Login ID : "))
        time.sleep(1)
        passwd = getpass.getpass()
        time.sleep(1)
        if acc in bank['acc'] :
            i = bank['acc'].index(acc)
            if passwd == bank['password'][i] :
                print("******Processing******")
                time.sleep(2)
                print("\n\n1.Debit\n2.Credit\n3.Check Balance")
                ch = int(input("Choice : "))
                time.sleep(2)
                if ch == 1 :
                    amount = int(input("Enter amount to be withdraw : "))
                    if amount > bank['bal'][i] :
                        print("\n\nInsufficient Account Balnce to be Withdraw")
                    else :
                        bank['bal'][i] -= amount
                        time.sleep(1)
                        print("\n{} rs withdrawn from your account".format(amount))
                        print("\nRemaning Balance  = ",bank['bal'][i])

                elif ch == 2 :
                    pass
                elif ch == 3 :
                    pass
                else :
                    print("\n\nInvalid Choice ")
            else :
                print("\nInvalid Password Try Again ")

        else :
            print("\nNo such User Exists")
            print("\nYou can signup to our Bank")


    elif ch == 2 :
        name = input("\n\nEnter name : ")
        time.sleep(1)
        password = getpass.getpass()
        time.sleep(1)
        bal = int(input("Initial balance to deposit : "))
        time.sleep(1)
        acc = bank['acc'][-1] + 1
        bank['name'].append(name)
        bank['password'].append(password)
        bank['bal'].append(bal)
        bank['acc'].append(acc)
        print("\nYour Account Sucessfully Created ")
        print("\nNote down your Account Number : {} ".format(acc))
        time.sleep(3)
        
    else :
        print("Invalid Choice ")
