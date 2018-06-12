def addTag(*tags):
    def dec(func):
        def mk(s):
            k = func(s)
            for tag in tags:

                k = "<{0}>{1}</{0}>".format(tag,k)
            return k
        return mk
    return dec

@addTag('b','p','div')
def new(s):
    s = s.strip()
    return s

s = input("Type something : \n\n")

r = new(s)
print(r)
