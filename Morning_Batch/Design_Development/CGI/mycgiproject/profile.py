#!C:\\ProgramData\\Anaconda3\\python.exe

import cgi,cgitb
cgitb.enable()
from os import environ
if 'HTTP_COOKIE' in environ.keys() :
    data = environ['HTTP_COOKIE']
    data = data.split(';')
    data = data[:-4]
    dt = {}
    for d in data:
        #print(d)
        #print("<br />")
        key,value = d.split('=')
        dt[key] = value
else :
    dt = None
print("Content-type:text/html")
print()
print(*dt)
print(dt.keys())
print('<br/>')
print(dt['Acc'])
if 'Acc' in dt.keys():
    print("You are logged in ")
else :
    print("You are not Logged in")