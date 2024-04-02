from flask import render_template, request

from src import app


@app.route('/')
def index():
    """This is the index route
    """
    data = {
        'title': 'Flask App',
        'description': 'This is a simple flask app',
        'articles': [ "title1", "title2", "title3" ],
        # 'articles': [
        #     {
        #         'id': 1,
        #         'title': 'Article 1',
        #         'body': 'This is the content of article 1'
        #     },
        #     {
        #         'id': 2,
        #         'title': 'Article 2',
        #         'body': 'This is the content of article 2'
        #     },
        #     {
        #         'id': 3,
        #         'title': 'Article 3',
        #         'body': 'This is the content of article 3'
        #     },
        # ]
    }
    return render_template('/views/index.html', data=data)

@app.route('/about')
def about():
    """This is the about route
    """
    about_data = {
        'title': 'About',
        'description': 'This is the about page'
    }
    return render_template('/views/about.html', data=about_data)

@app.route('/form')
def form():
    """This is form route
    """
    return render_template('/views/form.html')

@app.route('/form', methods=['POST'])
def form_post():
    """This is form POST Method route
    """
    req = request.form['name']

    print('Name:', req)
    return f'Form POST Method: {req}'
