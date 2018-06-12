def add(x,y):
    print("Result = ",x+y)

def dec(func):
    def n(x,y):
        print("X = ",x)
        print("Y = ",y)
        func(x,y)
        print("Bye bye ")
    return n

new = dec(add)
new(3,3)

@dec
def mul(a,b):
    print("Result = ",a*b)
mul(2,3)
