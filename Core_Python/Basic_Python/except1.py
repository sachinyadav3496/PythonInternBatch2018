def iin():
    try : 
        x  = int(input("Enter x : "))
        y = int(input("Enter y : "))
        r = x/y
        print(r)
        name = input("Enter file name to read : ")
        f = open(name)
        data = f.read()
        print(data)
        
        
    except ValueError as arg : 
        print("You idiot only Interger.")
        iin()
    except ZeroDivisionError as err : 
        print("You idiot nothing can be divided by zero.")
        iin()
    except Exception as err : 
        print("!!ERROR!!",err)
        iin()
    except KeyboardInterrupt as e :
        print("Don't be over smart fill in all inputs ")
        iin()
    except SystemExit as e : 
        print("Let's see")
        inn()
iin()
