from flask import Flask
from l_3.models import db, created_at,  Post, Comment


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')

if __name__ == '__main__':
    app.run(debug=True)
