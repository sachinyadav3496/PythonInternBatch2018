#Swastik
n = int(input("Enter no. of rows : "))
if not( n % 2 ) :
    n += 1
for row in range(1,n+1):
    if row == 1 :
        print("*",end='')
        print(" "*(n//2-1),end='')
        print("*"*(n//2+1))
    elif row <= n//2  :
        print('*',end='')
        print(" "*(n//2-1),end='')
        print("*")
    elif row == ( n // 2 + 1 ) :
        print("*"*n)
    elif row <= n -1 :
        print(" "*(n//2),end='')
        print("*",end='')
        print(" "*(n//2-1),end='')
        print("*")
    else :
        print("*"*(n//2+1),end='')
        print(" "*(n//2-1),end='')
        print("*")
