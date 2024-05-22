"""flask sample app"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index1():
    return 'Hello World!'

@app.route('/param/<name>')
def index2(name):
    return f'Hello, {name}'

@app.route('/user2/<int:id>')
def index3(id):
    return f'YOUR ID: {id}'

@app.route('/user3', methods=['GET','POST'])
def index4():
    return 'GET or POST'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
