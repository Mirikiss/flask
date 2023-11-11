from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Iteger, primary_key=True)
    username = db.Column(db.String(20))
    email = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __reper__(self):
        return f'User({self.username}, {self.email})' 

