from models import db, User
from flask import Flask, render_template, request, redirect
from forums import RegistrationForm
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'secret'
db.init_app(app)
csrf = CSRFProtect(app)


@app.route('/')
def hi():
    return f'hi'


@app.route('/register/', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        print(email, password)
    return render_template('index.html', form = form)

    

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)