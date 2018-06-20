from flask import Flask,render_template,request
from flask import make_response,redirect,url_for

app = Flask(__name__)
@app.route('/home/')
@app.route('/')
def index():
    return render_template('mysite/home.html')
@app.route('/login/')
def login():
    username = request.cookies.get('username')
    if username :
        return render_template('mysite/home.html')
    return render_template('mysite/login.html')
@app.route('/make_login/',methods=['GET','POST'])
def mklogin():
    if request.method == 'POST' :
        form = request.form
        name = form.get('name')
        password = form.get('password')
        if name and password :
            resp = make_response(render_template('mysite/mklogin.html',name=name,password=password))
            resp.set_cookie('username',name)
            return resp
        else :
            return "Invalid Entry"
    else :
        return "Form is not Valid"
@app.route('/signup/')
def signup():
    return render_template('mysite/signup.html')
@app.route('/make_signup/',methods=['POST',"GET"])
def mksignup():
    if request.method == 'POST' :
        form = request.form
        name = form.get('name')
        password = form.get('password')
        email = form.get('email')
        f = request.files['myfile']
        fn = f.filename
        fn = fn.split('.')[-1]
        fn = name+'.'+fn
        f.save('static/data/'+fn)
        return redirect(url_for('login'))

    else :
        return "Invalid Form"
@app.route('/logout/')
def logout():
    resp = make_response(render_template('mysite/home.html'))
    resp.set_cookie('username','')
    return resp

if __name__ == "__main__" :
    app.run(host='localhost',port=80,debug=True)
