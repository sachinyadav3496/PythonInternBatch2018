#!C:\\ProgramData\\Anaconda3\\python.exe
import cgi,cgitb
import pymysql as sql
from time import ctime
cgitb.enable()
data = cgi.FieldStorage()
acc = data.getvalue('acc')
password = data.getvalue('password')
db = sql.connect(host='localhost',port=3306,user='root',password='',database='pybank')
c = db.cursor()
try :
    c.execute('select acc,password from  bank where acc={}'.format(acc))
    data = c.fetchone()
    if data :
        if password == data[1] :
            t = ctime()
            t = t.split()
            t[2] = str(int(t[2])+2)
            t = ' '.join(t)
            print('Set-Cookie:Acc="{}";'.format(acc))
            print('Set-Cookie:Password="{}";'.format(password))
            print('Set-Cookie:Expire_Date="{}";'.format(t))
            print('Set-Cookie:Domain="localhost";')
            print("Content-type:text/html")
            print()
            print()
            c.execute('select * from bank where acc={}'.format(acc))
            data = c.fetchone()
            f = open('hello.html')
            page = f.read()
            page = page.format(data[0],data[1],data[2])
            f.close()
            print()
            print(page)

        else :
            print("Content-type:text/html")
            print()
            print("<h1>Invalid Passowd Try Again</h1>")
    else :
        print("Content-type:text/html")
        print()
        print("<h1>No such Account Exist<h1>")
except Exception as e :
    print("Content-type:text/html")
    print()
    print("<h1 style='color:red'>Something Went Wrong {}</h1>".format(e))







"""
page = "
<!Doctype html>
<html>
<body>
<h1>Sucessfully</h1>
<h2>Account no ={} </h2>
<h2>Password = {} </h2>
</body>
</html>
".format(acc,password)
print(page)

"""