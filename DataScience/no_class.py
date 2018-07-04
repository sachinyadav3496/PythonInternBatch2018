n  = int(input("Enter number of classess : "))

k = 1
while n >= 2**k :
    k = k + 1

print("Number of classes {} for {} observation ".format(k,n))
from math import log10
k = 1 + ( 3.322*log10(n))

print("According to Strug's Formula no of classes : ",round(k))
