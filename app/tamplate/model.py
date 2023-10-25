# � Используйте потоки.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datatime import datetime

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    firstname = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, default=datetime.utcnow)
    sex = db.Column(db.Text, nullable=False)
    gtoup = db.Column(db.Integer, nullable=False)
    fakulty_id = db.Column(db.Integer, db.ForeignKey('faculty_id'))
    
    def __repr__(self):
        return f'Student({self.name}, {self.firstname})'
