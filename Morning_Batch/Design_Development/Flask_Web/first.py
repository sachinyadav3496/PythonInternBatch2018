from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    s = """<h1 style="color:red">Hi This Flask Powered Web Page</h1>
            <h2><a href='/hello'>Say Hello!</a></h2> """
    return s
@app.route('/hello/')
def hello():
    return "<h1 > Hello World</h1><a href='/'>Home</a></h1>"
if __name__ == '__main__' :
    app.run(host='localhost',port=80,debug=True)
