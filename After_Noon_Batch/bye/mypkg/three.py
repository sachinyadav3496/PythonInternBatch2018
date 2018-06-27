class kuchBhi:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        print("{}+{}={}".format(self.x,self.y,self.x+self.y))
    def sub(self):
        print("{}-{}={}".format(self.x,self.y,self.x-self.y))

class prime:
    def __init__(self,x):
        self.num = x 
    def prime(self):
        from math import sqrt
        y = round(sqrt(self.num))
        for var in range(2,y+1):
            if self.num % var == 0 :
                return False
        return True

if __name__ == '__main__' : 
    a = kuchBhi(int(input("X : ")),int(input("Y : ")))
    b = prime(int(input("Enter a number : ")))
    a.add()
    a.sub()
    print(b.prime())
