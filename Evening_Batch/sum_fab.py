a,b = 0,1
k = int(input("Sum of terms : "))
print(0,end='\t')
s = 0
while True :
    if s+b >= k :
        break
    print(b,end='\t')
    s = s + b
    a,b = b,a+b
    
