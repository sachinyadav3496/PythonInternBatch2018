s = int(input("Enter Start Point : "))
e = int(input("Enter End Point : "))
for n in range(s,e+1) :
    num = n 
    c = 0
    while n > 0 :
        n = n // 10
        c = c + 1
    n = num     
    s = 0   
    while n :
        r = n % 10 
        n = n // 10 
        s = s + r ** c 
    if s == num :
        print(num,end='\t')
