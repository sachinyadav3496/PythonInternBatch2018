def dec(old_func):
    def make_up(x,y):
        print("Value of x = : ",x)
        print("Value of y = : ",y)
        print("Result = ",x+y)
        print("Thanks")
    return make_up

@dec
def new(x,y):
    pass
new(3,4)

