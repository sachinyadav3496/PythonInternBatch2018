n = int(input())
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
