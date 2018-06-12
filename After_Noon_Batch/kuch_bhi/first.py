fname = input("Enter file to overwrite : ")
f = open('hello.txt','w')

print("\nWrite :wq to exit and save file \n\n")
while True :

    data = input()
    if data.strip().lower() ==  ':wq' :
        f.close()
        print("\n\nThanks")
        break
    else :
        f.write(data)
        f.write('\n')
        

