from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pathlib import PurePath, Path

app = Flask(__name__)
app.config['SQLALCHEMY DATABASE_URI'] =  'sqlite:///blog.db'
db = SQLAlchemy(app)