n = input().split()
n = list(map(int,n))
k = list(map(lambda x:True if x % 2 == 0 else False,n))
for key,value in zip(n,k) :
    print("{} = {} ".format(key,value))
