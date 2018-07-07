#!C:\ProgramData\Anaconda3\python.exe
print("Content-type:text/html")
print()
import pymysql as sql
db = sql.connect('localhost','root','','student')
c = db.cursor()
c.execute("select * from student")
data = c.fetchall()
k = ''
for row in data:
    s = ''
    for col in row :
        s = s + str(col)+'\t'
    k = k+s+'</br>'
print("<!Doctype html>")
print("<html>")
print("<head>")
print('<link rel="stylesheet" href="c:\\xampp\\cgi-bin\\styles.css">')
print('</head>')
print("<body bgcolor=#FFFFFF>")
print('<link rel="stylesheet" href="styles.css">')
print("<h1>")
"""for var in range(10):

    for v in range(var) :
        print("*",end=' ')
    print("</br>")
"""
print(k)
print("</h1>")
print("</body>")
print("</html>")
