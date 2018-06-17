x = 10 
y = 20 
def sub():
    x = 10
    y = 30
    return x - y 
def add():
    global x,y
    x = x + 5
    y = y + 5
    return x +y 
r  = sub()
print(r)
r = add()
print(r )
print(x)
print(y)
