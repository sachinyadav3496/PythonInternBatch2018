import threading
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

th1 = threading.Thread(target=hello,args=('sachin',))
th2 = threading.Thread(target=bye,args=('python',))

th1.start()
th2.start()

th1.join()
th2.join()
