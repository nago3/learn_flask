"""Employee model"""
from datetime import datetime

from src import db


class Employee(db.Model):
    """Employee class for sqlalchemy model

    Setup This model to be used with sqlalchemy...
    run this command to create the table in the database.
        - python
        - from src import db
        - with app.app_context():
        -     db.create_all()
    """
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    mail = db.Column(db.String(255))
    department = db.Column(db.String(255))
    is_active = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
