n = int(input("Enter n : "))
m = int(input("Enter m : "))
def get_matrix():
    A = []
    for row in range(n):
        t = list(map(int,input().split()))
        A.append(t)
    return A
def old_get():
    A = [] 
    for row in range(n):
        t = []
        for col in range(m):
            t.append(int(input("A[{}][{}]".format(n,m))))
        A.append(t)
    return A
A = get_matrix()
B = old_get()
print(A)
print(B)


    
