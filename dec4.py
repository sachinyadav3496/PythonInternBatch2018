def oldfunc():
    print("Hi i am a old function ")

def decorate(oldfunc):
    def makeup():
        print("Welcome to Decorator ")
        print("Here is your old function ")
        oldfunc()
        print("Bye bye from decorator ")
    return makeup

oldfunc()
print("Let's decorate old function")
new = decorate(oldfunc)
new()

oldfunc = decorate(oldfunc)

oldfunc()
