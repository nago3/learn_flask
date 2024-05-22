"""flask sample app"""
from flask import Flask, request, redirect, jsonify, render_template

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

@app.route('/req')
def req():
    # Access to... "http://127.0.0.1:8080/req?param=test"
    return 'メソッド：' + request.method + 'パラメータ：' + request.args.get('param')

@app.route('/red')
def red():
    return redirect('/json')

@app.route('/json')
def json():
    return jsonify(
        dict(
            name='Taro',
            age=20,
            address='Tokyo'
        )
    )

@app.route('/view')
def view():
    return render_template(
            'index.html',
            title='Flask Test',
            members=['Taro', 'Jiro', 'Saburo']
        )

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
