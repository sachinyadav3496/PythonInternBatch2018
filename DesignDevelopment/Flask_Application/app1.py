from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def home():
    name = "Flask Powered WebSite"
    return render_template('index.html',data=name)
@app.route('/hello123/')
def contact():
    d = {
            'name':'Flask',
            'language':'Python',
            'use':'Web Desgning',
            'version':0.12,
            }

    return render_template('contact.html',data=d)
@app.route('/hello/')
@app.route('/hello/<string:name>/')
def hello(name=None):
    return "Welcome User with id {} ".format(name)


if __name__ == "__main__" :
    app.run(host='localhost',port=80,debug=True)