def gen(n,p):
    c = 1
    while c <= p :
        yield n**c
        c = c + 1

k = gen(int(input("Enter a Number : ")),int(input("Enter max. Power : ")))

#for var in k:
#    print(var,end='\t')

while True :
    try :
        print(next(k),end='\t')
    except Exception  :
        print("Generators Finished")
        break

