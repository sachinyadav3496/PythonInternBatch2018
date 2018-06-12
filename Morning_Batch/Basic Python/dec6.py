def dec(fun):
    def make(*args):
        l = len(args)
        for var in range(l):
            print("Var {} = {}".format(var+1,args[var]))
            
        return fun(*args)
    return make

@dec
def add(*args):
    s = 0
    for var in args:
        s += var
    return s
@dec 
def new(*args):
    l = ['name','addr','marks','ph_no' ]
    for key,value in zip(l,args) :
        print("{} = {}".format(key,value))

new('python','india',12312,2332234334)
add(10,9,8,7,6,5,4,3,2,1)
