def decorator(old_fun):
    def makeup(*arg):
        #l = len(arg)
        print("*"*75)
        print("*"*75)
        #name = name.center((l*3))
        old_fun(*arg)
        print("*"*75)
        print("*"*75)
    return makeup
def my(old):
    def new(*arg):
        print("-"*75)
        print("-"*75)
        print()
        old(*arg)
        print()
        print("-"*75)
        print("-"*75)
    return new
@my
@decorator
def add(x,y):
    print("x = {}".format(x))
    print("y = {}".format(y))
    print("x + y = {}".format(x+y))

@decorator
def hello(name):
    print(name)

#while input("Type something to repet : ") :
print("\n")
    #n = input("Please Enter your name : ")
    #hello(n)
x = int(input("Enter x : "))
y = int(input("Enter y : "))
add(x,y)
print("\n")


