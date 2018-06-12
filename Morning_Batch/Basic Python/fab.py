a,b  = 0,1
n = int(input("Enter number of terms : "))
print("{}\t{}".format(a,b),end='\t')
n -= 2
while n :
    a,b=b,a+b
    print(b,end='\t')
    n -= 1

