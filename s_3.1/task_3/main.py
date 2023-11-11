from flask import Flask, render_template, request, redirect, url_for
from models import db, SQLAlchemy, Regist
from forms import RegisterForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///baseinfo.db'
app.config['SECRET_KEY'] = 'secret'
db.init_app(app)
csrf = CSRFProtect(app)

@app.route('/')
def new():
    return 'Hi!'


@app.route('/hi/', methods = ['GET', 'POST'])
def hi():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        #password = form.password.data
        #print(email, password)
        user = Regist(name=name,  email=email)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return f'Пользовател добавлен {name}'
    return render_template('index.html', form=form)


if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)