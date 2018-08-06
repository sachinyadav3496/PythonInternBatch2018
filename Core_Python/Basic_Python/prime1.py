n = int(input("Starting Point : "))
e = int(input("Ending Point : "))
s = 0

if n <= 2 :
    print("2",end='\t')
    s = s +1
    
while n <= e :
    c = 2
    while c <= n//2+1 : 
        if n % c == 0 :
            break
        elif c == n//2 + 1 :
            print(n,end='\t')
            s = s + 1
        c = c + 1
    
    n = n + 1

print("\nTotal Prime Numbers = ",s)

