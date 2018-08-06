def hello() :
    try :
        x = int(input("Enter a Integer : "))
        y = int(input("Enter another Integer : "))
        print("X/Y=",x/y)
        f = open(input("Enter file name : "))
        print(f.read())
        f.close()
    except ValueError as arg :
        print("Error!! Please input Only interger  ")
        hello()
    except FileNotFoundError as e :
        print("Error!! No such file exists make sure path is correct")
        hello()
    except KeyboardInterrupt as k :
        print("Don't be oversmart run code fully")
        hello()
    except Exception as e :
        print("Error!",e)
        hello()

hello()
