#!C:\\ProgramData\\Anaconda3\\python.exe
import cgitb,cgi
import os
import pymysql as sql
cgitb.enable()
form = cgi.FieldStorage()
name = form.getvalue('username')
password = form.getvalue('password')
fname = form.getvalue('fname')
lname = form.getvalue('lname')
email = form.getvalue('email')
file = form['file']
filename = file.filename
ex = filename.split('.')[-1]
path = 'C:/xampp/htdocs/myproject/data/'
nf = name+'.'+ex
path = path+nf
f = open(path,'wb')
f.write(file.file.read())
f.close()
try :
    db = sql.connect(host='localhost',port=3306,user='myprojectcgi',password='redhat',database='myprojectcgi')
    c = db.cursor()
    cmd = "insert into user values('{}','{}','{}','{}','{}','{}')".format(name,fname,lname,email,path,password)
    c.execute(cmd)
    db.commit()
    print("Content-type:text/html")
    print("\n")
    s = """<h1 style='color:red';font-size:x-large>Your Account Sucessfully Created</h1>
            <h1 style='color:red';font-size:x-large>Please Login to use Our Facilities</h1>
            <a href='/'>Login</a>
            """
    print(s)

except Exception as e :
    print("Content-type:text/html")
    print("\n")
    print("Database Error!!",e)
