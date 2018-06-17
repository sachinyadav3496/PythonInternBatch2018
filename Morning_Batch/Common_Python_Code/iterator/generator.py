import time
def mygen():
    x = 0
    while True :
        x = x + 1
        time.sleep(.3)
        yield print("Hello World {} Times".format(x))

v = mygen()
while True :
    next(v)
