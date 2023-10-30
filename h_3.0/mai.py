from flask import Flask, render_template, request, session, redirect, url_for
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from model import *



@app.route('/registration3/', methods=['GET', 'POST'])
def registration3():
    form = Registration3Form()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        name = form.name.data.lower()
        surname = form.surname.data.lower()
        email = form.email.data
        user = User2(name=name, surname=surname, email=email)
        if User2.query.filter(User2.email == email).first():
            flash(f'Пользователь с e-mail {email} уже существует')
            return redirect(url_for('registration'))
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Вы успешно зарегистрировались!')
        return redirect(url_for('registration3'))
    return render_template('registration3.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)