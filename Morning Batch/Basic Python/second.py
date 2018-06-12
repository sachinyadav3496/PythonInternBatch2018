mydict = {}
while input("Type something to Continue : ") :

    d = input("Enter key=value pair : ").split('=')
    if d[0] in mydict :
        print("Error: key already exist ")
        print("Try again ")
    else :
        mydict.update((d,))


print(mydict)


