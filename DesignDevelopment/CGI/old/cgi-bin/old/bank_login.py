#!C:\ProgramData\Anaconda3\python.exe
import cgi,cgitb
import pymysql
try :
    db = pymysql.connect('localhost','root','','bank')
    c = db.cursor()
except Exception as e :
    print("Content-type:text/html\n")
    print("<h1>Error Message:Database not running</h1>")
    exit(0)
cgitb.enable()
form = cgi.FieldStorage()
name = form.getvalue('username')
name = cgi.escape(name)
password = form.getvalue('password')
password = cgi.escape(password)

c.execute("select * from data where name = '%s'"%name)
data = c.fetchone()

if data is None :
    flag = False
else :
    if data[2] == password :

        flag = True
    else :
        flag = False

print("Content-type:text/html\n\n")

if flag :
    print("<!Doctype html><html><head><title>Home Page</title></head><body>")
    print("<font size=4>")
    print("Name  = ",data[0])
    print("</br>Account No. = ",data[1] )
    print("</br>Email address =", data[4])
    print("</br>Balance = ",data[3])
    print("</br></font>")
    print('<img src="../%s" height="50px" width="50px" position="relative">'%data[5])
    print("</body></html>")
else :
    print("<h1>Error:No such User Exist Try Again</h1>")

