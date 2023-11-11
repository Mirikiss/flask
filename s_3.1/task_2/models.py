from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.Text, nullable=True)
    password = db.Column(db.String(20), nullable=False)

    def __reper__(self):
        return f'{self.name} {self.email} {self.password} {self.email}'