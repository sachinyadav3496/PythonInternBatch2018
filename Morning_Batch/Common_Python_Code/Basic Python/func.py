def func(x,y=10,*args,**kwargs):
    """This is doc-string of this function"""
    print("\nPositional Argument x = ",x)
    print("\nDefault Argument y = ",y)
    print("\nHere is your Var Length Arguments as tuple : ")
    c = 1
    for var in args :
        print("Var Length Arg {} : {} ".format(c,var))
        c = c+1
    print("\n\nKey with Arguments ")
    for key,value in kwargs.items() :
        print("{} = {}".format(key,value))
    print()
    return "sucess"

print("func(10)",func(10))
print()
print("func(10,20)",func(10,20))
print()
print("func(10,20,'hello','hi',1,2,3,4.5)",func(10,20,'hello','hi',1,2,3,4.5))
print("func(10,name='python',type='programming language')",func(10,name='python',type='programming language'))
