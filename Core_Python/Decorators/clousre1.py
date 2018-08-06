#Closure
def hello():
    x = 5
    def hi():
        return x
    return hi

var = hello()

print(var())

