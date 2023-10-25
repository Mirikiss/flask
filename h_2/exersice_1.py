# Задание №9
# Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# При отправке которой будет создан cookie файл с данными
# пользователя
# Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.

from flask import Flask, request, render_template, make_response, session, redirect, url_for
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex()


@app.route('/')
def front():
    return render_template('front.html')

@app.route('/check', methods = ['GET', 'POST'])
def check():
    if request.method == 'POST':
        session['name'] = request.form.get('name')
        return redirect(url_for('front'))
    return render_template('login.html')

@app.route('/checkout')
def checkout():
    session.pop('name', None)
    return redirect(url_for('front'))

if __name__ == '__main__':
    app.run(debug=True)
