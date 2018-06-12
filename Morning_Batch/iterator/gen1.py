k = (var**2 for var in range(1000) if var % 2 )

while True :
    try :
        print(next(k),end='\t')
    except StopIteration as e :
        print("Genter Successfully Exited")
        break
    else :
        print("Something is happening")
    finally :
        print("I will execute no matter whatever happens")
