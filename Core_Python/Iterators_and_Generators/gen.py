def even(num,max_limit):
    c = 0
    while c <= max_limit :
        if num % 2 == 0 :
            yield num
            num = num + 1
            c = c + 1
        else :
            num = num + 1
            c = c + 1
    
x = even(2,1000)
for var in x :
    print(var)
