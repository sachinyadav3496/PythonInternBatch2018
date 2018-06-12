n = int(input("Enter no of rows : "))

c = 65
for row in range(1,n+1):
    for col in range(1,row+1):
        print(chr(c),end='')
    print()
    c = c + 1
