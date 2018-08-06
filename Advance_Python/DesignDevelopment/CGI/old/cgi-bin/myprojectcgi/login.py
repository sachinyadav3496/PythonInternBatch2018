#!C:\\ProgramData\\Anaconda3\\python.exe
import cgitb,cgi
import pymysql as sql
cgitb.enable()

form = cgi.FieldStorage()

name = form.getvalue('username')
password = form.getvalue('password')
print("Content-type:text/html")
print("\n")

try :
    db = sql.connect(host='localhost',port=3306,user='myprojectcgi',password='redhat',database='myprojectcgi')
    c = db.cursor()
    c.execute("select * from user where username='{}'".format(name))
    data = c.fetchone()
    if data :
        if data[-1] == password :

            f = open('login.html')
            page = f.read()
            f.close()
            page = page.format(data[0],data[1],data[2],data[3])
            print(page)
        else :
            print("<h1 style='color:red'>!!!Error!!!Invalid Password</h1><a href='/'>Home</a>")

    else :
        print("<h1 style='color:red'>Error No such user Exist</h1><a href='/'>Home</a>")
except Exception as e :
    print("<h1 style='color:red;font-size:x-large;'><b><i>!!!ERROR!!!CHECK DATABASE CONNECTIVITY !!!!{}<h1>".format(e))














"""
print("<h1>Your Request Handled Sucessfully</h1><br /><a href='/'>home</a>")
print("<br /")
print("<h1>Welcome Back {} <br />With Password {}</h1>".format(name,password))
#print("<h1>{}</h1>".format(str(dir(form))))
"""