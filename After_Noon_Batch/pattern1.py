n = int(input("Enter a num : "))
for row in range(1,n+1):
    print("\t",end='')
    c = 2*row-1
    print(" "*(n-c//2),end='')
    print("*"*c,end='')
    print()
for row in range(1,n+1):
    print("\t",end='')
    print(" "*(row),end='')
    print("*"*(2*n-1-2*row),end='')
    print()
