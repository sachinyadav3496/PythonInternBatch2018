#!C:\\ProgramData\\Anaconda3\\python.exe

print("Content-type:text/html")
print()

print("<!Doctype html>")
print("<html>")
print("<body>")
print("<h1 style='color:red'>")
for var in range(15):
    for col in range(var):
        print("*")
    print("</br>")
print("</h1>")
print("</body>")
print("</html>")