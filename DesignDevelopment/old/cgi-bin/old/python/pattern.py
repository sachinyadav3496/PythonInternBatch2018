#!C:\ProgramData\Anaconda3\python.exe
print("Content-type:text/html")
print()
print("<!Doctype html")
print("<html>")
print("<body bgcolor='pink'")
print("<h1 style=\"color:green\">Hi this python program</h1>")
print("<br />"*2)
print("<a href='/python/'>Home</a>")
print("<br />"*2)
print("<center>")
print('<p style="color:red">')
import random
n = random.randint(10,20)
for var in range(n):
    print('\t\t',end='')
    for _ in range(n-var):

        print("\t*",end='')
    print('<br />')
print("</p></center>")
print("</body>")
print("</html")
