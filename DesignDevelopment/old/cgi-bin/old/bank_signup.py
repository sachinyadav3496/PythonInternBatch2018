#!C:\ProgramData\Anaconda3\python.exe
import cgi,cgitb,os
import pymysql as sql
try :
    db = sql.connect('localhost','root','','bank')
    c = db.cursor()
except Exception as e:
    print("Content-type:text/html\r\n")
    print("<h1>Error: Something Went Wrong")
    exit(0)
cgitb.enable()
form = cgi.FieldStorage()
name = form.getvalue('username')
password = form.getvalue('password')
email = form.getvalue('email')
bal = int(form.getvalue('bal'))
fileitem = form['file']
print("Content-type:text/html")
print()
if fileitem.filename :

    ex = fileitem.filename.split('.')[-1]
    fname = name+'.'+ex
    open('../htdocs/data/'+fname,'wb').write(fileitem.file.read())
    addr = '../data/'+fname
else :
    addr = 'data/logo.jpg'

cmd = "insert into data(name,password,bal,email,image) VALUES('%s','%s',%i,'%s','%s')"%(name,password,bal,email,addr)
try :
    c.execute(cmd)
    db.commit()
except Exception as e :
    print("Error: Something Went wrong ",e)

print("<h1>Thanks for Signing UP </h1>")
print("<h1>Now you can login</h2>")







