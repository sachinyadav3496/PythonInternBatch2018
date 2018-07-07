#!C:\ProgramData\Anaconda3\python.exe
print("Content-type:text/html")
print()
import cgi,cgitb
import pymysql as sql
try :
    db = sql.connect(host='localhost',port=3306,user='root',password='',database='bank')
    c = db.cursor()
except Exception as e :
    print("Error!!Data Base Temproray Unavailable",e)
cgitb.enable()
data = cgi.FieldStorage()
try :
    name = data.getvalue('name')
    password = data.getvalue('password')
except Exception as e:
    print("Error!",e)

cmd = 'select name,password from data where name="{}"'.format(name)
c.execute(cmd)
data = c.fetchone()
if data :
    if password.strip().lower() == data[1] :
        cmd = 'select * from data where name="{}"'.format(name)
        c.execute(cmd)
        data = c.fetchone()
        acc = data[1]
        bal = data[3]
        email = data[4]
        image = data[5]
        page = """
        <!Doctype html>
        <html>
        <head>
        <title>Account</title>
        <link rel='stylesheet' type='text/css' href='main.css'>
        </head>
        <body>
        <h1>Welcome back , {0} to your account</h1>
        <center>
        <h1> Here is your details</h1>
        <p>Name : <b>{0}</b></p>
        <p>Account Number : <b>{1}</b></p>
        <p>Balance : <b>{2}</b></p>
        <p>Email : <b>{3}</b></p>
        <img src='{4}'>
        </center>
        </body>
        </html>
        """.format(name,acc,bal,email,image)
        print(page)
    else :
        print("<h1 style='color:red'>Error!!Wrong Password</h1>")
else :
    print('<h1 style="color:red">"Error!! No such user Exist Please Signup</h1>')
