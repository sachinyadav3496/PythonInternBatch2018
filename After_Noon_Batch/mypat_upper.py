n = int(input())
dash = 2*n - 3
rows = 2*n -1
char = 96+n
for row in range(n):
    if row < n :    
        print('-'*(dash-(row*2)),end='')
        char = 96+n
        for var in  range(2*row+1):
            s = ''
            if var % 2 == 0 : 
                if row == n -1 and var == 0:
                    s = chr(char)
                else :
                    s = '-'+chr(char)
                print(s,end='')
                char -= 1
        char = 96+n-row+1
        for var in  range(2*row-1):
            s = ''
            if var % 2 == 0 : 
                if row == n -1 and var == (2*row-1):
                    s = '-'+chr(char)
                else :
                    s = '-'+chr(char)
                print(s,end='')
                char += 1
        if row != n -1 :
           print('-',end='')
        print('-'*(dash-(row*2)),end='')
    print()

