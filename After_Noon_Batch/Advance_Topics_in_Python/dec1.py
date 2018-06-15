def fun(fun1):
    def new(x,y):
        print("x = ",x)
        print("y = ",y)
        fun1(x,y)
    return new

def add(p,q):
    print("{} + {} = {}".format(p,q,p+q))
new = fun(add)

new(6,7)

@fun
def s(var1,var2):
    print(var1+var2)

s('hello ','world')
