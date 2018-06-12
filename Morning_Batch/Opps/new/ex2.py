def hello():
    try : 
        x = int(input("Enter a Positive Value : "))
        assert x >= 0 , "{} is not Positive you idiot".format(x)
        print("Good Boy ")
        if input("Type something : ") :
            hello()
    except AssertionError as arg :
        print("Error!!",arg)
        print("Try again")
        hello()
hello()
