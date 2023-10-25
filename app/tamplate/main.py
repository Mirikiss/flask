from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from model import db, Student, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY DATABASE_URI'] =  'sqlite:///blog.db'
