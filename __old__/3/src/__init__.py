from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///learn_flask.db'

db = SQLAlchemy(app)
from src import paths

from .models import employee
