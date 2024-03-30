"""views.py is a file that contains all the routes for the application"""
from modules import app


@app.route('/')
def index():
    """This is the index route
    """
    return 'Say Hello!!'

@app.route('/about')
def about():
    """This is the about route
    """
    return 'This is an About page'
