def hello():
    try :
        x = int(input("Enter a positive value : "))
        if x < 0 :
            raise ValueError("{} is a Negative Number\nPlease \
input only Positive Value Try Again ".format(x))
        print(x,"Good Boy")
        if input("Press something to continue : ") :
            hello()
    except ValueError as e :
        print("Error!",e)
        hello()
hello()
