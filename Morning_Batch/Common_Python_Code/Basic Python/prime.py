def prime(n):
    c = 2
    while c <= n//2+1 : 
        if n % c == 0 :
            return False
            break 
        elif c == n - 1 :
            return True
    


