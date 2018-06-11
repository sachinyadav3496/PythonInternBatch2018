n = list(map(int,input().split()))
for key,value in zip(n,list(map(lambda x:True if x % 2 == 0 else False,n))) :
    print("{} = {} ".format(key,value))
