def fact(num):
    if num >= 0 :
        if num :
            s = 1
            for var in range(num,0,-1) :
                s = s * var
            return s
        else :
            return 1
    else :
        return 'Error! Negative number does not have factorial'

if __name__ == '__main__' :
        print("__name__" ,__name__)
        n = int(input("Enter a number : "))
        r = fact(n)
        print("Result = ",r)
