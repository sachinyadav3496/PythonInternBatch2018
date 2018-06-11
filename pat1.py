n  = int(input("Enter number of rows : "))
row = 1
while row <= n :
    #print("row = ",row,end='')
    col = 1 
    while col <= row : 
        #print(" col = ",col,end='')
        print("*",end='')
        col += 1
    print()
    row += 1

for row in range(1,n+1) :
    for col in range(1,row+1) :
        print("*",end='')
    print()


