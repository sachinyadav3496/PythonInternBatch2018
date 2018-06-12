n = int(input("Enter no of rows = "))

for row in range(1,n+1) :
    for col in range(1,n-row+2) :
        print("*",end='')
    print()

row = 1 
while row <= n :
    col = 1
    while col <= n-row+1:
        print("*",end='')
        col += 1
    print()
    row += 1
