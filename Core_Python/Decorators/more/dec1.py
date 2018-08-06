def hello(name):
    return "hello , "+name
def dec(old_func):
    def make_up(x):
        s = "Hello World! welcome to python\n"
        s += old_func(x)
        s += "\nHi this is decorator"
        return s
    return make_up
hello = dec(hello)

k = hello('sachin')
print(k)
