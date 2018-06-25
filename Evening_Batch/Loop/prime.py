num = int(input("Enter a num : "))
from math import sqrt
for var in range(2,round(sqrt(num)+1)):
    if num % var == 0 :
        print("Not prime ")
        break
else : 
    print("Prime")


