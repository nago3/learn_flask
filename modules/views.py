"""views.py is a file that contains all the routes for the application"""
from config import HELLO
from modules import app


@app.route('/')
def index():
    """This is the index route
    """  # Import the HELLO variable from the config module
    return HELLO  # Use the imported HELLO variable

@app.route('/about')
def about():
    """This is the about route
    """
    return 'This is an About page'
