#!C:\\ProgramData\\Anaconda3\\python.exe
import cgi,cgitb
cgitb.enable()
print("Content-type:text/html")
print()


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
    x = True
else :
    x = False


s = ''
for key,value in dt.items():
    k = str({})+' = '+str({})
    k = k.format(key,value)
    s = s+k+'</br>'

page = """
<!Doctype html>
<html>
<head>
<title>Hello</title>
<link rel='stylesheet' type='text/css' href='cgi-bin/css/main.css' >
</head>
<body>
<h1> Welcome to first CGI-SCRIPT</h1>
<h1> Hello World In CGI</h1>
<h1>{}</h1>
</body>
</html>
""".format(s)


if x :
    print(page)
else :
    print("Login First")

