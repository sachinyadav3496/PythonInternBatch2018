from flask import Flask
app = Flask(__name__)

@app.route('/') # homepage
def index():
    return "Hello By Flask Web Page"
@app.route('/hello/')
@app.route('/hello/<string:name>')
def hello(name='Nobody'):
    return "Hello mr. {}".format(name)
@app.route('/<int:id>') #int, float, string, path, uuid
def My(id):
    return 'Your id is {}'.format(id)

@app.route('/<path:mypath>')
def my(mypath):
    return "You want to acess %s"%(mypath)
if __name__ == "__main__" :
    app.run(host='localhost',port=80,debug=True)
