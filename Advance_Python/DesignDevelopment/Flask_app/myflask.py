from flask import Flask,render_template,request,make_response,session
from flask import redirect,url_for
app = Flask(__name__)
import pymysql as sql
app.secret_key = 'alksjflkjaroashfohr9382y98refhsy93yrhoihfohfiudshiofew9'

@app.route('/')
def index():
    if 'name' in session:
            name = session.get('name')
            password = session.get('password')
            return render_template('index.html',login=True)
    #return '<h1 style=\'color:red\'>Bye Bye World</h1>'
    return render_template('index.html')
@app.route('/hello/<string:name>')
@app.route('/hello/')
def hello_world(name=None):
    return render_template('hello.html',name=name)

@app.route('/login/',methods=['POST',"GET"])
def login():

    if 'name' in session :
            name = session.get('name')
            password = session.get('password')

    elif request.method == 'POST' :
        name = request.form.get('name')
        password = request.form.get('password')
        chk = request.form.get('s')
    else :
        return "Bhai only Post Method use kar"

    try:
        db = sql.connect(host='localhost',port=3306,user='root',password='',database='myprojectcgi')
        c = db.cursor()
        c.execute("select * from user where username='{}'".format(name))
        n = c.fetchone()
        if n :
            if password == n[5] :
                data = {
                    'User Name' : n[0],
                    'First Name' : n[1],
                    'Last Name' : n[2],
                    'Email' : n[3],
                    }
                session['name'] = name
                session['password'] = password
                return render_template('login.html',data=data)
                #resp = make_response(render_template('login.html',data=data))
                #resp.set_cookie('name',name)
                #resp.set_cookie('password',password)
                #return resp
            else :
                error = 'Invalid Password Try Again'
                return render_template('index.html',error=error)
        else :
            error = 'No such user Exist in our system'
            return render_template('index.html',error=error)
    except Exception as e :

            return "DATABASE Connectivity Error, {}".format(e)

@app.route('/logout/')
def logout():
    del session['name']
    del session['password']
    return redirect(url_for('index'))
    #resp = make_response(render_template('index.html'))
    #resp.delete_cookie('name')
    #resp.delete_cookie('password')
    #return resp
if __name__ == '__main__':
    app.run(host='localhost',port=80,debug=True)
