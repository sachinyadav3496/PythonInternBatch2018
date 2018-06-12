def calc(x,y,ch):
    """calc(x,y,ch)->This function takes 2 integer numbers x and y and return their operation with ch operator that can be +, -, *, /, %, //, **. """
    if ch == '+' :
        return x+y
    elif ch == '-' :
        return x-y
    elif ch == '*' :
        return x*y
    elif ch == '/' :
        if y :
            return x/y 
        else :
            return "Error! Zero Division Error"
    elif ch == '//' :
        return x//y
    elif ch == '**' :
        return x**y
    elif ch == '%' :
        return x%y 
    else :
        return "Error!!Invalid Choice"

while input("\n\nPress a key to continue ") :
    print("Welcome to calc program")
    print("Defination of Program : ",calc.__doc__)
    print()
    x = int(input("X : = "))
    y = int(input("Y : = "))
    ch = input("Choice (+,-,*,/,%,//,**) : ")
    result = calc(x,y,ch)
    print("\nYour Result = ",result)

