from math import sqrt
c = 0
def prime(num):
    global c
    c = c + 1
    if num <= 1 :
        return False
    if num <= 3 :
        return True
    for var in range(2,int(sqrt(num)+2)):
        if num % var == 0 :
            return False
    return True
def count():
    print("No of time function prime called is : ",c)

if __name__ == "__main__" :
    while True:
        ch = int(input('1.prime\n2.count\n3.exit'))
        if ch == 1 :
            n = int(input("Number : "))
            print("{} is prime : {}".format(n,prime(n)))
        elif ch == 2 :
            count()
        else :
            exit(0)


