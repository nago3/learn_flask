from flask import Flask

app = Flask(__name__)

db = SQLAlchemy(app)
from models import employee

from src import paths
