x = 'hello' #global variable

def hello():
        print(x)

def bye():
    x = 'bye' #local variable
    print(x)

hello()
bye()
print(x)
