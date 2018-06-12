import math
from functools import reduce
def prime(num):
    if num <= 1 :
        return False
    if num <= 3 :
        return True
    for var in range(2,int(math.sqrt(num)+2)):
        if num % var == 0 :
            return False
    return True
n = list(map(int,input().split()))
"""k = map(prime,n)
for key,value in zip(n,k) :
    print("{} = {}".format(key,value),end=' ')
print()
"""
l = filter(prime,n)
r = reduce(lambda x,y:x+y,l)
print("Result = ",r)


