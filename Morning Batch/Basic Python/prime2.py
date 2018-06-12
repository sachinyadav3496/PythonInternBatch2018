
n = int(input("Starting Point : "))
e = int(input("Ending Point : "))
s = 0

if n <= 2 :
    print("2",end='\t')
    s = s +1
    
while n <= e :
    c = 2
    import math
    sq = int(math.sqrt(n)) + 1
    while c <= sq : 
        if n % c == 0 :
            break
        elif c == sq :
            print(n,end='\t')
            s = s + 1
        c = c + 1
    
    n = n + 1

print("\nTotal Prime Numbers = ",s)

