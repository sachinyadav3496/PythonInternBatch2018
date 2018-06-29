"""Hi here are some function"""
class Say_Hello:
    def show(self):
        print("Hello World")

def pat(n):
    for var in range(10):
        for _ in range(10-var):
            print(" ",end='')
        for x in range(var):
            print("*",end='')
        print()

def prime(num):
    from math import sqrt
    c = round(sqrt(num)+1)
    for var in range(2,c):
        if num % var == 0 :
            return False
    return True

def even_odd(num):
    if num % 2 :
        return False
    else :
        return True

if __name__ == "__main__" :
    print("Hi ")
    print(prime(1234))
    print(pat(10))
    print(even_odd(123412312))
