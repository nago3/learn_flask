# Flask

### What is Flask?

Flask is a micro web framework written in Python. It is classified as a microframework
because it does not require particular tools or libraries.
It has no database abstraction layer, form validation, or any other components
where pre-existing third-party libraries provide common functions.
However, Flask supports extensions that can add application features as if they were implemented in Flask itself.
Extensions exist for object-relational mappers, form validation, upload handling,
various open authentication technologies and several common framework related tools.

### Installation

```sh
$ pyp3 install Flask
```

### Quickstart

Create a new directory for the project and create a new file `sample.py` with the following content.

```py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

### Running the application

```sh
$ export FLASK_APP=sample.py
$ flask run
```

### References

- [Flask Documentation](https://flask.palletsprojects.com/en/3.0.x/)

### DB

Use SQLite3 with Flask-SQLAlchemy

```sh
$ pyp3 install Flask-SQLAlchemy
```

```py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Return a representation of the object
    def __repr__(self):
        return '<User %r>' % self.username
```
