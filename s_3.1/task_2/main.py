from flask import Flask, render_template, request
from models import db, User
from famous import RegisterForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'secret'
db.init_app(app)
csrf = CSRFProtect(app)


@app.route('/')
def main():
    return 'Welcome!!'

@app.route('/regist', methods = ['GET', 'POST'])
def regist():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        print(email, password)
    return render_template('forms.html', form = form)

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)