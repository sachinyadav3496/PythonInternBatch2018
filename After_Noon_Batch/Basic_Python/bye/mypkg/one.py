def pat(n):
    for var in range(n):
        for _ in range(n-var):
            print(" ",end='')
        for _ in range(var):
            print("*",end='')
        print()
if __name__ == "__main__" :
    print("Current File or Module Name : ",__name__)
    n = int(input("Enter no of lines : "))
    pat(n)
