class Prime:
    def __init__(self,start):
        self.start = start
    def __iter__(self):
        return self
    def prime(self):
            num = self.start
            sq = round(sqrt(num)+1)
            for var in range(2,sq):
                if num % var == 0 :
                    self.start += 1
                    return self.prime()
            else :
                self.start += 1
                return num
    def __next__(self):
        return self.prime()

from math import sqrt
x = Prime(1)
x = iter(x)
c = 0
for var in x :
    print(var,end=', ')
    c = c+1
print("Total numbers = ",c)
