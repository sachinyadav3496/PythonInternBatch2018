class MyError(ValueError) :
    def __init__(self,e):
        self.e  = e
    def __str__(self):
        return str(self.e)

try : 
    x = int(input("positive : "))
    if x < 0 : 
        raise MyError("{} is Negative number ".format(x))

except MyError:
    print("Error!something went wrong")
    
