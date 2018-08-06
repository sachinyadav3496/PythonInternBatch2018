from time import sleep,ctime
from random import randint

def hello(name):
    for var in range(5):
        sleep(randint(1,3))
        print("\nHello World , ",name,"at ",ctime())
def bye(name):
    for var in range(5):
        sleep(randint(1,4))
        print("\nBye World ,",name,"at ",ctime())

hello('sachin')
bye('sachin')
