from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200),  nullable=False)
    firstname = db.Column(db.String(200),  nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.Text, nullable=False)
    group = db.Column(db.Integer, nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'))

    def __repr__(self):
        return f'Student({self.name}, {self.firstname})'
    
class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    students = db.relationship(Student, backref='faculty', lazy=True)

    def __repr__(self):
        return f'Faculty({self.name})'


