from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def index():
    #return '<h1 style=\'color:red\'>Bye Bye World</h1>'
    return render_template('index.html')
@app.route('/hello/<string:name>')
@app.route('/hello/')
def hello_world(name=None):
    return render_template('hello.html',name=name)

@app.route('/login/',methods=['POST',"GET"])
def login():
    if request.method == 'POST' :
        data = {
        'name' : request.form.get('name'),
        'password' : request.form.get('password'),
        'chk' : request.form.get('s'),
        }
        return render_template('login.html',data=data)
    else :
        return "Bhai only Post Method use kar"
if __name__ == '__main__':
    app.run(host='localhost',port=80,debug=True)
