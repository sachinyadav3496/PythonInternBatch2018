f = open("hello.txt",'w+')
f.write("Hello World WElcome to python")
f.write("\n\tThis is super easy")
f.seek(0)
data = f.read()
f.close()
print(data)

