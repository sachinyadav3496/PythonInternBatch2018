n,m = map(int,input("Enter matrix dimension m n : ").lower().split())
#A = [ [ int(input("A[{}][{}] = ".format(row,col))) for col in range(m) ] for row in range(n) ]
def show(X):
    for var in X:
        s = '{:10}'*len(var)
        print('\t',s.format(*var))

print("Please Give matrix A : ")
A = [ list(map(int,input('\t').split())) for var in range(n) ]
print("Please Give matrix B : ")
B = [ list(map(int,input('\t').split())) for var in range(n) ]
print("Matrix A is : ")
show(A)
print("Matrix B is : ")
show(B)
