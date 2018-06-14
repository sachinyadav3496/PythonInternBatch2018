def print_rangoli(n):
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

    pat = 2*n - 3
    for row in range(n-1):
        print("-"*(2*row+1),end='')
        nat = pat-(2*row)
        char = 96+n
        for var in range(nat//2+1):
            if row == 0 and var == 0 :
                s = '-'+chr(char)
                print(s,end='')
                char = char-1
            else :
                s = '-'+chr(char)
                char = char - 1
                print(s,end='')
        char = 97+row+2
        print('-',end='')
        for var in range(nat//2):
            s = chr(char)+'-'
            char += 1
            print(s,end='')
        print("-"*(2*row+1),end='')
        print()
