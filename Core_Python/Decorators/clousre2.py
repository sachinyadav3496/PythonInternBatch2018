#Closure
def hello(x):
    def hi():
        return x
    return hi

var = hello(6)

print(var())

