def take_input():
    try : 
        x = int(input("Enter a number : "))
        print("X = ",x)      
    except ValueError as arg :
        print("Error!!Are you stupid we are saying number means number ")
        print("Error!",arg)
        take_input()
take_input()
